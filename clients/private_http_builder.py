from httpx import Client
from typing import TypedDict

from clients.authentication_client import get_authentication_client, LoginRequest


class AuthenticationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user: AuthenticationUserDict) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequest(email=user['email'], password=user['password'])
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=10,
        base_url="http://localhost:8000",
        headers={"Authorization": f"Bearer {login_response['token']['access_token']}"} )