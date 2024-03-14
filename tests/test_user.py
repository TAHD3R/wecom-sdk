import pytest

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.users import WecomUsersClient
from wecom_sdk.schemas.message import (
    MessageContent,
    RecallMessageParams,
    TextMessageParams,
)


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomUsersClient:
        return WecomUsersClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_get_department(self, setup: WecomUsersClient):
        user = await setup.get_user(userid="821175643076")

        assert user is not None
