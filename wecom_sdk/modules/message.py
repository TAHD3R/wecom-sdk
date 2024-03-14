from typing import Literal

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.schemas.message import (
    MessageParams,
    RecallMessageInfo,
    RecallMessageParams,
    SendMessageInfo,
)
from wecom_sdk.utils.requests import HttpxRequest


class WecomMessageClient(WecomBaseClient):

    async def send_message(
        self,
        data: MessageParams,
    ) -> str:
        """
        企业微信发送消息
        @param data: 发送消息的参数
        各类消息的参数详情 https://developer.work.weixin.qq.com/document/path/90236

        @return: 消息ID
        """
        url = self.BASE_URL + "/message/send"
        params = {"access_token": await self.access_token}

        data = data.model_dump()

        resp = SendMessageInfo(
            **await HttpxRequest.post(url=url, params=params, json=data)
        )

        if resp.errcode == 0:
            return resp.msgid
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def recall_message(self, data: RecallMessageParams) -> bool:
        """
        企业微信撤回消息
        @param msgid: 消息ID

        @return: 撤回状态(Boolean)
        """
        data = data.model_dump()

        url = self.BASE_URL + "/message/recall"
        params = {"access_token": await self.access_token}

        resp = RecallMessageInfo(
            **await HttpxRequest.post(url=url, params=params, json=data)
        )

        if resp.errcode == 0:
            return True
        else:
            raise SDKException(resp.errcode, resp.errmsg)
