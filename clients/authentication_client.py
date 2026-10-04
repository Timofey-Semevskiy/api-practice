from tools.api_client import ApiClient
from typing import TypedDict
from httpx import Response


# Контракт данных для запроса логина
class LoginRequest(TypedDict):
    email: str
    password: str


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