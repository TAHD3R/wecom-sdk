import pytest

from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.department import WecomDepartmentClient
from wecom_sdk.schemas.message import (
    MessageContent,
    RecallMessageParams,
    TextMessageParams,
)


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomDepartmentClient:
        return WecomDepartmentClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_get_departments(self, setup: WecomDepartmentClient):
        depts = await setup.get_departments()

        assert depts is not None

    @pytest.mark.asyncio
    async def test_get_department(self, setup: WecomDepartmentClient):
        depts = await setup.get_departments(id=1)

        assert depts is not None

    @pytest.mark.asyncio
    async def test_get_department_no_privilege(self, setup: WecomDepartmentClient):
        with pytest.raises(SDKException):
            await setup.get_departments(id=1)
