import pytest

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.message import WecomMessageClient
from wecom_sdk.schemas.message import MessageParams, RecallMessageParams


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomMessageClient:
        return WecomMessageClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_send_text_message(self, setup: WecomMessageClient):
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
    async def test_send_textcard_message(self, setup: WecomMessageClient):
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="textcard",
            textcard={
                "title": "领奖通知",
                "description": '<div class="gray">2016年9月26日</div> <div class="normal">恭喜你抽中iPhone 7一台，领奖码：xxxx</div><div class="highlight">请于2016年10月10日前联系行政同事领取</div>',
                "url": "URL",
                "btntxt": "更多",
            },
        )
        msgid = await setup.send_message(data)
        assert msgid is not None

    @pytest.mark.asyncio
    async def test_send_news_message(self, setup: WecomMessageClient):
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="news",
            news={
                "articles": [
                    {
                        "title": "中秋节礼品领取",
                        "description": "今年中秋节公司有豪礼相送",
                        "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png",
                    }
                ]
            },
        )
        msgid = await setup.send_message(data)
        assert msgid is not None

    @pytest.mark.asyncio
    async def test_send_markdown_message(self, setup: WecomMessageClient):
        data = MessageParams(
            touser="821175643076",
            agentid=48,
            msgtype="markdown",
            markdown={
                "content": '您的会议室已经预定，稍后会同步到`邮箱`  \n>**事项详情**  \n>事　项：<font color="info">开会</font>  \n>组织者：@miglioguan  \n>参与者：@miglioguan、@kunliu、@jamdeezhou、@kanexiong、@kisonwang  \n>  \n>会议室：<font color="info">广州TIT 1楼 301</font>  \n>日　期：<font color="warning">2018年5月18日</font>  \n>时　间：<font color="comment">上午9:00-11:00</font>  \n>  \n>请准时参加会议。  \n>  \n>如需修改会议信息，请点击：[修改会议信息](https://work.weixin.qq.com)'
            },
        )
        msgid = await setup.send_message(data)
        assert msgid is not None
