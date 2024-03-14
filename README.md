# 企业微信SDK - Python语言实现

[更新日志](./CHANGELOG.md) 

## 项目介绍

本项目通过封装企业微信服务端API开发了一个企业微信SDK，具备基础常用功能，以便提高相关脚本、程序开发效率。

项目基于异步开发，能有效提高请求效率，具有以下模块：

- `WecomBaseClient` 基本模块，获取access_token(具备内存缓存机制)

- `WecomDepartmentClient` 部门处理模块，具有增删改查部门功能

- `WecomMessageClient` 消息发送模块，兼容多种方式发送消息

- `WecomUsersClient` 用户管理模块，具有查询信息、学工号转换功能（不通用）

- `HttpxRequest` Httpx请求库封装，具有`GET`、`POST`方法

基于以上模块，Mixin后成为 `Wecom` 类，可通过`from wecom-sdk import Wecom`进行实例化

项目使用`Pydantic`库对数据建模，具有完备的类型提示与数据校验功能。

项目各类、各方法、各数据模型均有文档注释，可读性高。

可访问`test`文件夹查看用例。

## 项目架构

```bash
-- wecom_sdk
    |-- exceptions
    |   `-- general.py # 异常类
    |-- modules
    |   |-- base.py # 基本模块
    |   |-- department.py # 部门处理模块
    |   |-- message.py # 消息发送模块
    |   |-- mixin.py # Mixin类
    |   `-- users.py # 用户管理模块
    |-- schemas
    |   |-- base.py # 基础模型
    |   |-- departments.py # 部门模型
    |   |-- message.py # 消息模型
    |   |-- token.py # 密钥模型
    |   `-- users.py # 用户模型
    `-- utils
        |-- convert.py # 学工号转换
        `-- requests.py # Httpx库封装
```

## 使用方法

1. 安装`wecom-sdk`库

```bash
pip install wecom-sdk
```

2. 在项目中引用`wecom-sdk`库

```python
from wecom_sdk import Wecom
from wecom_sdk.schemas.message import MessageParams
from wecom_sdk.exceptions.general import SDKException

client = Wecom(corpid="your_corpid", corpsecret="your_corpsecret")

# 发送消息
async def send_message():
    try:
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="text",
            text={
                "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
            },
        )
        msgid = await setup.send_message(data)
    except SDKException:
    ...

```

## 软件协议

本项目遵循[License: MIT](./LICENSE)协议
