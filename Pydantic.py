from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    # populate_by_name: можно передавать и lastName, и last_name
    model_config = {"populate_by_name": True}

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: Optional[str] = Field(default=None, alias="middleName")


class CreateUserRequest(UserSchema):
    id: Optional[str] = None   # сервер сам присвоит
    password: str = Field(min_length=8)


class CreateUserData(BaseModel):
    user: UserSchema