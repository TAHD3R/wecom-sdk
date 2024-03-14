from wecom_sdk.schemas.base import BaseSchema


class AccessTokenParams(BaseSchema):
    """
    获取access_token的参数
    @param corpid: 企业ID
    @param corpsecret: 应用的凭证密钥
    """

    corpid: str
    corpsecret: str


class AccessTokenInfo(BaseSchema):
    """
    获取access_token的返回数据
    @param errcode: 返回码 出错返回码，为0表示成功，非0表示调用失败
    @param errmsg: 对返回码的文本描述内容
    @param access_token: 获取到的凭证 最长为512字节
    @param expires_in: 凭证的有效时间（秒）
    """

    errcode: int
    errmsg: str
    access_token: str | None = None
    expires_in: int | None = None


class AccessTokenInvalid(BaseSchema):
    """
    获取access_token失败时的返回数据
    @param errmsg: 错误信息
    """

    errmsg: str
