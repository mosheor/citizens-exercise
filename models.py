from pydantic import BaseModel


class Citizen(BaseModel):
    name: str
    roles: list[str]
    allowed_places: list[str] = []


class Role(BaseModel):
    title: str
    allowed_places: list[str] = []
    sub_roles: list[str] = []


class Config(BaseModel):
    citizens: dict[str, Citizen]
    roles: dict[str, Role]
