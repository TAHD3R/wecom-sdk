from datetime import datetime, timedelta

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.schemas.token import (
    AccessTokenInfo,
    AccessTokenParams,
)
from wecom_sdk.utils.requests import HttpxRequest

BASE_URL: str = "https://qyapi.weixin.qq.com/cgi-bin"


class WecomBaseClient:
    BASE_URL: str = BASE_URL

    def __init__(self, corpid: str, corpsecret: str):
        """
        企业微信SDK
        @param corpid: 企业ID
        @param corpsecret: 应用的凭证密钥

        每个应用有独立的secret，获取到的access_token只能本应用使用，所以每个应用的access_token应该分开来获取
        """
        self.corpid = corpid
        self.corpsecret = corpsecret
        self._access_token = None
        self.access_token_valid_time = None

    @property
    async def access_token(self) -> str:
        """企业微信SDK的access_token"""
        if (
            self.access_token_valid_time
            and datetime.now() < self.access_token_valid_time
        ):
            return self._access_token

        await self.__get_access_token()

        return self._access_token

    @access_token.setter
    def access_token(self, value: str):
        self._access_token = value

    async def __get_access_token(self, refresh: bool = False) -> str:
        """
        获取access_token

        access_token的有效期通过返回的expires_in来传达，正常情况下为7200秒（2小时），有效期内重复获取返回相同结果，过期后获取会返回新的access_token。
        由于企业微信每个应用的access_token是彼此独立的，所以进行缓存时需要区分应用来进行存储。

        详细说明：https://work.weixin.qq.com/api/doc/90000/90135/91039

        @return: access_token: str 或 None
        """

        if (
            not refresh
            and self.access_token_valid_time
            and datetime.now() < self.access_token_valid_time
        ):
            return self.access_token

        url = self.BASE_URL + "/gettoken"
        params = AccessTokenParams(
            corpid=self.corpid, corpsecret=self.corpsecret
        ).model_dump()
        resp = AccessTokenInfo(**await HttpxRequest.get(url=url, params=params))

        if resp.errcode == 0:
            self.access_token_valid_time = datetime.now() + timedelta(
                seconds=resp.expires_in
            )
            self.access_token = resp.access_token
            return resp.access_token
        else:
            raise SDKException(resp.errcode, resp.errmsg)
