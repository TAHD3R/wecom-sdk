import pytest

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.message import WecomMessageClient
from wecom_sdk.schemas.message import (
    MessageContent,
    RecallMessageParams,
    TextMessageParams,
)


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomMessageClient:
        return WecomMessageClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_send_text_message(self, setup: WecomMessageClient):
        data = TextMessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="text",
            text={
                "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
            },
        )
        msgid = await setup.send_text_message(data)
        assert msgid is not None

    @pytest.mark.asyncio
    async def test_send_text_message_invalid_user(self, setup: WecomMessageClient):
        with pytest.raises(SDKException):
            data = TextMessageParams(
                touser="2021060301",
                agentid=48,
                msgtype="text",
                text={
                    "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
                },
            )
            await setup.send_text_message(data)

    @pytest.mark.asyncio
    async def test_recall_message(self, setup: WecomMessageClient):
        data = TextMessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="text",
            text={
                "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
            },
        )
        msgid = await setup.send_text_message(data)

        recalled = await setup.recall_message(RecallMessageParams(msgid=msgid))

        assert recalled is True

    @pytest.mark.asyncio
    async def test_recall_message_failed(self, setup: WecomMessageClient):
        with pytest.raises(SDKException):
            await setup.recall_message(RecallMessageParams(msgid="123"))
