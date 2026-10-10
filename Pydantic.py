import uuid

from pydantic import BaseModel, Field, EmailStr, ValidationError


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenSchema(BaseModel):
    tokenType: str
    accessToken: str
    refreshToken: str


class LoginResponse(BaseModel):
    token: TokenSchema


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    def get_username(self) -> str:
        return f"{self.first_name} {self.last_name}"


class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserData(BaseModel):
    user: UserSchema


class ValidationErrorResponse(BaseModel):
    detail: list


# 1. Инициализация через аргументы
user_default = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise",
)
print("User default model:", user_default)
print("Username:", user_default.get_username())

# 2. Инициализация через словарь (как приходит ответ от API)
user_dict = {
    "id": "user-id",
    "email": "user@gmail.com",
    "lastName": "Bond",
    "firstName": "Zara",
    "middleName": "Alise",
}
user_dict_model = UserSchema(**user_dict)
print("User dict model:", user_dict_model.model_dump())
print("User dict by alias:", user_dict_model.model_dump(by_alias=True))

# 3. Инициализация через JSON (ответ 200 от POST /users)
create_user_json = """
{
    "user": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alise"
    }
}
"""
create_user_model = CreateUserData.model_validate_json(create_user_json)
print("Create user model:", create_user_model)
print("Inner user:", create_user_model.user)

# 4. Некорректный email -> ValidationError
try:
    bad_user = UserSchema(
        id="user-id",
        email="not-an-email",
        lastName="Bond",
        firstName="Zara",
        middleName="Alise",
    )
except ValidationError as error:
    print(error)
    print(error.errors())