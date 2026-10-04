import time
""" Метод для генерации уникального email """
def get_unique_email():
    return f'email{time.time()}@example.com'