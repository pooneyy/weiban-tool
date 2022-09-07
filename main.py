# @Author : Qiuyelin
# @repo : https://github.com/pooneyy/weiban-tool

import os, sys
import Utils
import json
import asyncio

async def weibanTask(user):
    # tenantCode UserId x-token userProjectId
    tenantCode = user.get('tenantCode')
    userId = user.get('userId')
    x_token = user.get('token')
    userProjectId = user.get('userProjectId')
    realName = user.get('realName',userId)
    taskName = '未知的任务名'
    main = Utils.main(tenantCode, userId, x_token, userProjectId)
    main.init()
    try:
        realName = main.getRealName()
        taskName = main.getTaskName()
        print(f"开始进行 {realName} 的任务：{taskName}")
        finishIdList = main.getFinishIdList()
        for i in main.getCourse():
            await main.start(i)
            await asyncio.sleep(20)
            main.finish(finishIdList[i])
        print(f"{realName} 的任务已完成")
    except json.decoder.JSONDecodeError:print(f'{realName} 的账户信息错误或已经过期，请重新获取。详见：https://github.com/pooneyy/weiban-tool')
    except KeyboardInterrupt:print(f'{realName} 的任务被手动终止')

async def main():
    usersConfig = {}
    try:
        with open("config.json", "r+", encoding='utf8') as file:
            try:usersConfig = json.load(file)
            except json.decoder.JSONDecodeError:print('配置文件格式错误，请仔细检查  config.json 。详见：https://github.com/pooneyy/weiban-tool')
        tasks=[]
        for user in usersConfig:
            tasks.append(weibanTask(user))
        try:await asyncio.gather(*tasks)
        except asyncio.CancelledError:pass
    except FileNotFoundError:print('未找到 config.json！详见：https://github.com/pooneyy/weiban-tool')

if __name__ =='__main__':
    try:asyncio.run(main())
    except KeyboardInterrupt:print(f'\n任务被手动终止')
    os.system("pause")