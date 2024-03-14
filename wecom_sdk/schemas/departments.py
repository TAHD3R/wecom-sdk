from typing import AnyStr, List

from wecom_sdk.schemas.base import BaseSchema


class CreateDepartmentParams(BaseSchema):
    """
    创建部门

    @param name: 部门名称。长度限制为1~32个字节，字符不能包括\:?”<>
    @param name_en: 英文名称
    @param parentid: 父部门id。根部门id为1
    @param order: 在父部门中的次序值。order值小的排序靠前。
    @param id: 部门id，整型。指定时必须大于1，不指定时则自动生成
    """

    name: str
    name_en: str | None = None
    parentid: int
    order: int | None = None
    id: int | None = None


class UpdateDepartmentParams(CreateDepartmentParams): ...


class UpdateDepartmentInfo(BaseSchema):
    errcode: int
    errmsg: AnyStr


class CreateDepartmentInfo(BaseSchema):
    errcode: int
    errmsg: AnyStr
    id: int


class DepartmentInfo(BaseSchema):
    """
    部门单体响应数据
    """

    id: int
    name: AnyStr
    name_en: AnyStr | None = None
    department_leader: List[str] | None = None
    parentid: int | None = None
    order: int | None = None


class DepartmentInfo(BaseSchema):
    """
    部门整体响应数据
    """

    errcode: int
    errmsg: AnyStr
    department: List[DepartmentInfo]
