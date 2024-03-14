from typing import AnyStr, List

from wecom_sdk.schemas.base import BaseSchema


class UserInfo(BaseSchema):
    """
    用户单体响应数据
    """

    errcode: int
    errmsg: AnyStr
    userid: AnyStr | None = None
    name: AnyStr | None = None
    department: List[int] | None = None
    position: AnyStr | None = None
    moblie: AnyStr | None = None
    gender: int | None = None
    email: AnyStr | None = None
    status: int | None = None


class UserSimpleInfo(BaseSchema):
    userid: AnyStr
    name: AnyStr
    department: List[int]
    open_userid: AnyStr | None = None


class DepartmentUserInfo(BaseSchema):
    errcode: int
    errmsg: AnyStr
    userlist: List[UserSimpleInfo]


class DepartmentUserDetailInfo(BaseSchema):
    errcode: int
    errmsg: AnyStr
    userlist: List[UserInfo]
