from typing import AnyStr, Literal

from wecom_sdk.schemas.base import BaseSchema


class MessageParams(BaseSchema):
    """
    发送消息参数
    各类消息的参数详情 https://developer.work.weixin.qq.com/document/path/90236

    根据msgtype的不同，选择对应的消息内容填充即可

    @param touser: 指定接收消息的成员，成员ID列表（多个接收者用‘|’分隔，最多支持1000个）。
    @param toparty: 指定接收消息的部门，部门ID列表，多个接收者用‘|’分隔，最多支持100个。
    @param totag: 指定接收消息的标签，标签ID列表，多个接收者用‘|’分隔，最多支持100个。
    @param msgtype: 消息类型，此时固定为：text
    @param agentid: 企业应用的id，整型。企业内部开发，可在应用的设置页面查看；第三方服务商，可通过接口 获取企业授权信息 获取该参数值

    @param safe: 表示是否是保密消息，0表示可对外分享，1表示不能分享且内容显示水印，默认为0
    @param enable_id_trans: 表示是否开启id转译，0表示否，1表示是，默认0。仅第三方应用需要用到，企业自建应用可以忽略。
    @param enable_duplicate_check: 表示是否开启重复消息检查，0表示否，1表示是，默认0
    @param duplicate_check_interval: 表示是否重复消息检查的时间间隔，默认1800s，最大不超过4小时

    touser、toparty、totag不能同时为空，后面不再强调
    """

    touser: AnyStr | None = None
    toparty: AnyStr | None = None
    totag: AnyStr | None = None
    msgtype: Literal[
        "text", "image", "voice", "video", "textcard", "news", "mpnews", "markdown"
    ]
    agentid: int

    # 各种类型的消息内容
    text: dict | None = None
    voice: dict | None = None
    video: dict | None = None
    file: dict | None = None
    textcard: dict | None = None
    news: dict | None = None
    mpnews: dict | None = None
    markdown: dict | None = None

    safe: int = 0
    enable_id_trans: int = 0
    enable_duplicate_check: int = 0
    duplicate_check_interval: int = 1800


class SendMessageInfo(BaseSchema):
    """
    发送消息响应数据

    """

    errcode: int
    errmsg: AnyStr
    invaliduser: AnyStr | None = None
    invalidparty: AnyStr | None = None
    invalidtag: AnyStr | None = None
    unlicenseduser: AnyStr | None = None
    msgid: AnyStr | None = None
    response_code: AnyStr | None = None


class SendMessageInvalid(BaseSchema):
    """
    发送消息失败响应数据

    """

    errmsg: AnyStr
    invaliduser: AnyStr | None = None
    invalidparty: AnyStr | None = None
    invalidtag: AnyStr | None = None
    unlicenseduser: AnyStr | None = None


class RecallMessageParams(BaseSchema):
    """
    撤回消息请求参数
    """

    msgid: AnyStr


class RecallMessageInfo(BaseSchema):
    """
    撤回消息响应数据
    """

    errcode: int
    errmsg: AnyStr
