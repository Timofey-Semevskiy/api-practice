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
    """Клиент для публичных методов API /api/v1/users (без авторизации)."""

    def create_user_api(self, request: CreateUserRequest) -> Response:
        return self.post("/api/v1/users", json=request)


def get_public_users_client() -> PublicUsersClient:
    """Создаёт PublicUsersClient с готовым httpx.Client (без токена)."""
    return PublicUsersClient(client=get_public_httpx_builder())
