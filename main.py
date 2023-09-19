# @Author : Qiuyelin
# @repo : https://github.com/pooneyy/weiban-tool

import os, sys
import random
import Utils
import json
import asyncio

async def weibanTask(user):
    # tenantCode id x-token userProjectId
    tenantCode = user.get('tenantCode')
    userId = user.get('userId')
    x_token = user.get('token')
    realName = user.get('realName')
    id = user.get('raw_id')
    taskName = '未知的任务名'
    main = Utils.main(tenantCode, userId, x_token, realName)
    main.init()
    try:
        main.get_Project_Info()
        taskName = main.taskName
        print(f"开始进行 {realName} 的任务：{taskName}")
        # 获取列表
        for chooseType in [2,3]:
            finishIdList = main.getFinishIdList(chooseType)
            index = 1
            for i in main.getCourse(chooseType):
                print(f"{realName} 开始学习 {main.resourceNames[index]} {index} / {len(finishIdList)}")
                await main.start(i)
                await asyncio.sleep(random.randint(15,20))
                main.finish(i, finishIdList[i])
                print(f"{realName} 完成学习 {main.resourceNames[index]}")
                index += 1
        print(f"{id} {realName} 的任务已完成")
        with open("config.json", "r+", encoding='utf8') as file:
            config = json.load(file)
            for i in config['Accounts']:
                if i.get('id') == id:i['State'] = 1
            for i in config['Accounts_login_state']:
                if i.get('raw_id') == id:config['Accounts_login_state'].remove(i)
            # seek(0), truncate()用于覆写文件
            file.seek(0)
            file.truncate()
            json.dump(config, file, ensure_ascii=False, indent=4)
    except json.decoder.JSONDecodeError:
        print(f'{realName} 的账户登录态已经过期，已删除该登录态。请重新登录。')
        with open("config.json", "r+", encoding='utf8') as file:
            config = json.load(file)
            config['Accounts_login_state'] = []
            file.seek(0)
            file.truncate()
            json.dump(config, file, ensure_ascii=False, indent=4)
    except KeyboardInterrupt:print(f'{realName} 的任务被手动终止')

async def main():
    usersConfig = []
    try:
        with open("config.json", "r+", encoding='utf8') as file:
            try:usersConfig = json.load(file).get('Accounts_login_state')
            except json.decoder.JSONDecodeError:print('配置文件格式错误，请仔细检查  config.json 。详见：https://github.com/pooneyy/weiban-tool')
        tasks=[]
        for user in usersConfig:
            tasks.append(weibanTask(user))
        try:await asyncio.gather(*tasks)
        except asyncio.CancelledError:pass
    except FileNotFoundError:print('未找到 config.json！详见：https://github.com/pooneyy/weiban-tool')

if __name__ =='__main__':
    try:
        Utils.save_Login_State(Utils.set_accounts())
        asyncio.run(main())
    except KeyboardInterrupt:print(f'\n任务被手动终止')
    os.system("pause")