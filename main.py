# @Author : Qiuyelin
# @repo : https://github.com/pooneyy/weiban-tool

import Utils
import time
import json

# tenantCode UserId x-token userProjectId
try:
    with open("config.json", "r+", encoding='utf8') as file:
        usersConfig = json.load(file)
    for user in usersConfig:
        tenantCode = user['tenantCode']
        userId = user['userId']
        x_token = user['token']
        userProjectId = user['userProjectId']
        main = Utils.main(tenantCode, userId, x_token, userProjectId)
        main.init()
        finishIdList = main.getFinishIdList()
        for i in main.getCourse():
            main.start(i)
            time.sleep(20)
            main.finish(finishIdList[i])
except FileNotFoundError:print('未找到 config.json !')