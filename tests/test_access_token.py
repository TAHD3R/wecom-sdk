import pytest

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient


class TestAccessToken:
    @pytest.fixture
    def setup(self, corpid) -> WecomBaseClient:
        return WecomBaseClient(
            corpid=corpid,
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    @pytest.mark.parametrize("corpid", ["your_corpid"])
    async def test_access_token(self, setup: WecomBaseClient):
        assert await setup.access_token is not None

    @pytest.mark.asyncio
    @pytest.mark.parametrize("corpid", ["your_corpid"])
    async def test_access_token_error(self, setup: WecomBaseClient):
        with pytest.raises(SDKException):
            await setup.access_token
