from tools.api_client import ApiClient
from typing import TypedDict
from httpx import Response
from clients.public_httpx_builder import get_public_httpx_builder


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str


# Контракт данных для запроса логина
class LoginRequest(TypedDict):
    email: str
    password: str
class LoginResponse(TypedDict):
    token: Token

# Контракт данных для запроса обновления токена
class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthenticationClient(ApiClient):
    """Клиент для методов авторизации /api/v1/authentication."""

    def login_api(self, request: LoginRequest) -> Response:
        """
        Выполняет логин пользователя.

        :param request: Данные логина (email, password).
        :return: Ответ сервера с токеном доступа.
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Обновляет токен доступа по refresh-токену.

        :param request: Refresh-токен.
        :return: Ответ сервера с новым токеном.
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequest) -> LoginResponse:
        response = self.login_api(request)
        return response.json()

def get_authentication_client() -> AuthenticationClient:
    """
      Функция создает экземпляр httpx.CLient с базовыми настройками.

      :return Готовый к использованию обьект httpx.CLient

      """
    return AuthenticationClient(client=get_public_httpx_builder())