import pytest

from wecom_sdk import Wecom
from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.schemas.message import MessageParams, RecallMessageParams


class TestAccessToken:
    msgid: str = None

    @pytest.fixture
    def setup(self) -> Wecom:
        return Wecom(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_access_token(self, setup: Wecom):
        assert await setup.access_token is not None

    @pytest.mark.asyncio
    async def test_send_text_message(self, setup: Wecom):
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="text",
            text={
                "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
            },
        )
        msgid = await setup.send_message(data)
        assert msgid is not None

    @pytest.mark.asyncio
    async def test_recall_message(self, setup: Wecom):
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="text",
            text={
                "content": '你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href="http://work.weixin.qq.com">邮件中心视频实况</a>，聪明避开排队。'
            },
        )
        msgid = await setup.send_message(data)

        result = await setup.recall_message(RecallMessageParams(msgid=msgid))
        assert result is True

    @pytest.mark.asyncio
    async def test_get_department(self, setup: Wecom):
        user = await setup.get_user(userid="821175643076")
        assert user is not None
