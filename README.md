# weiban-tool

安全微伴自动刷课助手

[原项目](https://github.com/Coaixy/weiban-tool)作者已停止维护，我在源项目基础上增加多账号的支持

# 使用方法

以`UTF-8`的编码方式创建`config.json`文件。其内容格式如下：

> `config.json`：
>
> ```json
> [
>     {"token":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","userId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx","tenantCode":"00000001","userProjectId":"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"},
>     {"token":"yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy","userId":"yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy","tenantCode":"00000002","userProjectId":"yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"},
>     {"token":"zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz","userId":"zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz","tenantCode":"00000003","userProjectId":"zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz"},
>     {#第4个账号信息#},
>     {#第5个账号信息#},
>     ...
>     {#第n个账号信息#}
> ]
> ```

### 说明

1. 首先，<a href="javascript:(function(){data=JSON.parse(localStorage.user);prompt('',JSON.stringify({token:data['token'],userId:data['userId'], tenantCode:data['tenantCode'], userProjectId: data['preUserProjectId']}));})();">请将这个链接拖入收藏夹</a>。

2. 登录[安全微伴 (mycourse.cn)](http://weiban.mycourse.cn/#/login)，在登录后的页面上运行刚才添加进收藏夹的脚本

3. 复制弹窗内的内容，**按照格式**添加到`config.json`。(格式不对会报错)

   [![1662441411827.png](http://png.eot.ooo/i/2022/09/06/6316d7c7f3567.png)](http://png.eot.ooo/i/2022/09/06/6316d7c7f3567.png)
   
4. 运行`main.exe`。