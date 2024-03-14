from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.schemas.departments import DepartmentInfo
from wecom_sdk.schemas.users import (
    DepartmentUserDetailInfo,
    DepartmentUserInfo,
    UserInfo,
)
from wecom_sdk.utils.requests import HttpxRequest


class WecomUsersClient(WecomBaseClient):
    async def get_user(self, userid: str) -> dict:
        """
        读取成员
        @param userid: 成员UserID。对应管理端的账号，企业内必须唯一。不区分大小写，长度为1~64个字节


        @return: 成员信息
        """
        url = self.BASE_URL + "/user/get"
        params = {"access_token": await self.access_token, "userid": userid}
        resp = UserInfo(**await HttpxRequest.get(url=url, params=params))

        if resp.errcode == 0:
            return resp.model_dump(exclude={"errcode", "errmsg"})
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def get_user_in_department_detail(self, department_id: str) -> dict:
        """
        读取部门成员完整信息
        @param department_id: 	获取的部门id


        @return: 部门成员信息
        """
        url = self.BASE_URL + "/user/list"
        params = {
            "access_token": await self.access_token,
            "department_id": department_id,
        }
        resp = DepartmentUserDetailInfo(
            **await HttpxRequest.get(url=url, params=params)
        )

        if resp.errcode == 0:
            return resp.model_dump(exclude={"errcode", "errmsg"})
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def get_user_in_department(self, department_id: int) -> dict:
        """
        读取部门成员简要信息
        @param department_id: 	获取的部门id


        @return: 部门成员信息
        """
        url = self.BASE_URL + "/user/simplelist"
        params = {
            "access_token": await self.access_token,
            "department_id": department_id,
        }
        resp = DepartmentUserInfo(**await HttpxRequest.get(url=url, params=params))

        if resp.errcode == 0:
            return resp.model_dump(exclude={"errcode", "errmsg"})
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    @staticmethod
    def convert_userid(userid: str, decrypt: bool = False):
        """
        学工号/企业微信ID转换方法

        @param userid: 学工号/企业微信ID
        @param decrypt: 是否解密

        @return: 转换后的学工号/企业微信ID
        """
        if decrypt:
            year = str(int(userid[10:12]) + 1945)
            no = str(int(userid[2:9]) - 115342)
            no = no[1:7]
            userid = year + no
        else:
            userid = (
                "8"
                + userid[2:3]
                + str(int(userid[-6:]) + 1115342)
                + userid[8:9]
                + str(int(userid[0:4]) - 1945)
            )
        return userid
