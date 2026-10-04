# api-practice

Практика по API-тестированию на Python (httpx).

## Структура
- `clients/` — API-клиенты (обёртки над httpx)
- `tools/` — утилиты (APIClient, fakers)
- `scripts/` — сценарии (user_flow.py)

## Запуск
Нужен локальный API на `http://localhost:8000`.
Запустить: `python scripts/user_flow.py`