from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.modules.department import WecomDepartmentClient
from wecom_sdk.modules.message import WecomMessageClient
from wecom_sdk.modules.users import WecomUsersClient


class Wecom(
    WecomDepartmentClient, WecomUsersClient, WecomMessageClient, WecomBaseClient
):
    pass
