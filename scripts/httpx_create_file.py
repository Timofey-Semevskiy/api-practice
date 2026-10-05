import httpx

from tools.fakers import get_unique_email

# Создаем пользователя
payload = {
    "email": get_unique_email(),
    "password": "some_password_123",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', json=payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": payload['email'],
    "password": payload['password'],
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Выполняем загрузку файла
create_file_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}


create_file_response =  httpx.post(
    'http://localhost:8000/api/v1/files',
    data={'filename': 'image.jpg',
          'directory': 'courses'},
    files={'upload_file': open('../testdata/files/image.png', 'rb')},
    headers=create_file_headers
)

create_file_response_data = create_file_response.json()
print('Create file data:', create_file_response_data)