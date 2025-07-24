# 🚀 UCarTopDoer - Sentiment Analysis API

```bash
# 1. Установка (одной командой)
git clone git@github.com:bazuly/UCar-TopDoer.git && cd UCarTopDoer && \
  (curl -LsSf https://astral.sh/uv/install.sh | sh || powershell -c "irm https://astral.sh/uv/install.ps1 | iex") && \
  uv venv .venv && source .venv/bin/activate && uv sync
```

# 2. Миграции БД
```
make migrate-create
make migrate-apply
```

# 3. Запуск сервера
```
make run locally
```


Пример тестирования через CURL.
Также всегда можно протестировать через встроенный Swagger Fastapi. 
http://127.0.0.1:8000/docs/

```
POST:
curl -X POST "http://localhost:8000/reviews" \
-H "Content-Type: application/json" \
-d '{"text":"Сервис просто отличный, мне нравится!"}'
```

Ответ:
{
  "id": 1,
  "text": "Сервис просто отличный, мне нравится!",
  "sentiment": "positive",
  "created_at": "2023-10-25T12:34:56.789Z"
}

```
GET:
curl "http://localhost:8000/reviews?sentiment=negative"
```
Ответ:
[
  {
    "id": 2,
    "text": "Всё работает плохо, ненавижу!",
    "sentiment": "negative",
    "created_at": "2023-10-25T12:35:10.123Z"
  }
]

Остальные два варианта работаю по тому же принципу
