from clients.authentication_client import LoginRequest
from typing import TypedDict
from tools.api_client import ApiClient
from httpx import Response
from clients.public_httpx_builder import get_public_httpx_builder

class CreateUserRequest(TypedDict):
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(ApiClient):
    """
       Клиент для публичных методов API /api/v1/users.

       Эти методы не требуют авторизации (без токена).
       """
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
               Создаёт нового пользователя.

               :param request: Данные пользователя (email, password, firstName, lastName, middleName).
               :return: Ответ сервера с данными созданного пользователя.
               """
        return self.post("/api/v1/users", json=request)

def get_authentication_client() -> PublicUsersClient:
    """
    Функция создает экземпляр httpx.CLient с базовыми настройками.

    :return Готовый к использованию обьект httpx.CLient

    """

    return PublicUsersClient(client=get_public_httpx_builder())