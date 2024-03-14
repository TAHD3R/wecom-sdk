from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.schemas.departments import (
    CreateDepartmentInfo,
    CreateDepartmentParams,
    DepartmentInfo,
    UpdateDepartmentInfo,
    UpdateDepartmentParams,
)
from wecom_sdk.utils.requests import HttpxRequest


class WecomDepartmentClient(WecomBaseClient):

    async def create_departments(self, data: CreateDepartmentParams) -> int:
        """
        创建部门
        @param data: 创建部门的参数

        @return: 部门id
        """
        url = self.BASE_URL + "/department/create"
        params = {"access_token": await self.access_token}
        resp = CreateDepartmentInfo(
            **await HttpxRequest.post(url=url, params=params, json=data)
        )

        if resp.errcode == 0:
            return resp.id
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def delete_departments(self, id: int) -> bool:
        """
        删除部门
        @param id: 部门id

        @return: 删除状态(Boolean)
        """
        url = self.BASE_URL + "/department/delete"
        params = {"access_token": await self.access_token, "id": id}
        resp = await HttpxRequest.get(url=url, params=params)

        if resp.errcode == 0:
            return True
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def update_departments(self, data: UpdateDepartmentParams) -> bool:
        """
        更新部门
        @param data: 更新部门的参数

        @return: 更新状态(Boolean)
        """
        url = self.BASE_URL + "/department/update"
        params = {"access_token": await self.access_token}
        resp = UpdateDepartmentInfo(
            **await HttpxRequest.post(url=url, params=params, json=data)
        )

        if resp.errcode == 0:
            return True
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def get_departments(self, id: int = None) -> list[DepartmentInfo]:
        """
        获取部门列表
        @param id: 部门id。获取指定部门及其下的子部门。
        如果不填，默认获取全量组织架构

        @return: 部门列表
        """
        url = self.BASE_URL + "/department/list"
        params = {"access_token": await self.access_token, "id": id}
        resp = DepartmentInfo(**await HttpxRequest.get(url=url, params=params))

        if resp.errcode == 0:
            return resp.department
        else:
            raise SDKException(resp.errcode, resp.errmsg)
