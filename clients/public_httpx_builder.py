from httpx import Client

def get_public_httpx_builder() -> Client:
    return Client(timeout=100, base_url="https://httpx:8000")