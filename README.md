<h1 align="center">安全微伴自动刷课助手</h1>
<p align="center" class="shields">
    <img src="https://badges.toozhao.com/badges/01HAMCFS652W02Z5H3CE02M4JY/blue.svg" alt="Visitors"/>
</p>

相关项目：[安全微伴题库](https://github.com/pooneyy/WeibanQuestionsBank) | 安全微伴自动刷课助手

### 项目介绍

安全微伴自动刷课助手（多账号版），脱胎于[Coaixy/weiban-tool](https://github.com/Coaixy/weiban-tool)，在原项目基础上增加多账号的支持，可以同时进行多个账号的学习任务。

### 使用说明

1. 运行`main.py` 或者 [main.exe](https://github.com/pooneyy/weiban-tool/releases)。

2. **支持验证码识别**，验证码识别使用[TrueCaptcha](https://truecaptcha.org/)，会提示你输入`userid`和`apikey`，注册的方法此处不过多赘述。

   需要提醒的是，这是一个付费服务，每个账号每天享有30次免费识别服务，每个账号总共享有100次免费识别服务。

   关于资费，1美元可以识别3000次。可以使用PayPal国区支付，关于汇率，2023年9月18日，使用PayPal，$1USD=￥7.56CNY。

   **值得一提的是，你可以跳过这一步骤，登录时将手动输入验证码。**

3. 按照提示录入账号密码，可同时依次输入多个账号，会记录上一个账号的学校名称，当有多个账号来自同一个学校，可以不用重复输入学校名。

4. 按`Ctrl`+`C`结束录入账号，开始登录，如果在第二步没有输入`userid`和`apikey`，会提示输入验证码。

   ![](https://telegraph-image1.pages.dev/file/e46f287b9733d3b8d21bc.png)

### 更新日志

- 版本 1.1 at 2022-09-06 15:08:08
     - 优化：增加对多账户的支持。
- 版本 1.2 at 2022-09-07 14:02:39
  -    优化：使用异步函数，提高多账户场景下任务执行效率，避免由于多个账户排队时任务流程过长，Token过期，导致后面的账户任务失败。
  -    优化：使显示内容更简洁。

- 版本 2.0 at 2023-09-18 21:57:16
  - 优化：使用账号密码登录，登录相关的代码来自[Coaixy/weiban-tool/enco.py](https://github.com/Coaixy/weiban-tool/blob/bf08fe823953afa834b49fe8d7e7a1d5abf7e605/enco.py)。
