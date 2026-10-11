from Pydantic import UserSchema, CreateUserRequest, CreateUserData

# 1. Проверяем ответ сервера (GET /users/{id})
response_json = {
    "id": "user-id",
    "email": "user@gmail.com",
    "lastName": "Bond",
    "firstName": "Zara",
    "middleName": "Alise",
}
user = UserSchema.model_validate(response_json)
print(user.last_name)
print(user.model_dump(by_alias=True))

# 2. Готовим запрос (POST /users)
req = CreateUserRequest(
    email="new@gmail.com",
    password="12345678",
    lastName="Bond",
    firstName="Zara",
)
print(req.model_dump(by_alias=True, exclude={"id"}))
