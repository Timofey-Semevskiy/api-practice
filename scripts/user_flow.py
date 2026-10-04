import httpx
from tools.fakers import get_unique_email
from clients.users.public_users_client import PublicUsersClient

# Общий httpx-клиент: базовый URL локального API и таймаут 5 секунд
client = httpx.Client(base_url='http://localhost:8000', timeout=5)

# Обёртка над клиентом для публичных методов /api/v1/users (без авторизации)
users_client = PublicUsersClient(client)

# Данные для создания пользователя; email генерируем уникальным,
# чтобы каждый запуск не конфликтовал с предыдущими
payload = {
    "email": get_unique_email(),
    "password": "some_password_123",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

# Шаг 1: создаём пользователя
response_user = users_client.create_user_api(payload)
response_user_data = response_user.json()

print(response_user.status_code)
print(response_user_data)

# Шаг 2: логинимся под только что созданным пользователем
login_payload = {
    'email': response_user_data['user']['email'],
    "password": "some_password_123"
}

response_login = client.post('/api/v1/authentication/login', json=login_payload)
response_login_data = response_login.json()
print(response_login.status_code)
print(response_login_data)

# Шаг 3: извлекаем токен, добавляем его в заголовки
# и запрашиваем профиль с авторизацией
token = response_login_data['token']['accessToken']
client.headers.update({'Authorization': f'Bearer {token}'})
response_me = client.get('/api/v1/users/me')
response_me_data = response_me.json()
print(response_me.status_code)
print(response_me_data)