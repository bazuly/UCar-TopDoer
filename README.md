# 🚀 UCarTopDoer - Sentiment Analysis API

```bash
# 1. Установка (одной командой)
git clone https://github.com/yourusername/UCarTopDoer.git && cd UCarTopDoer && \
  (curl -LsSf https://astral.sh/uv/install.sh | sh || powershell -c "irm https://astral.sh/uv/install.ps1 | iex") && \
  uv venv .venv && source .venv/bin/activate && uv sync

# 2. Миграции БД
make migrate-create
make migrate-apply

# 3. Запуск сервера
make run locally

# installation 

git clone ....
cd UCarTopDoer
uv installation 
mac os | linux 
curl -LsSf https://astral.sh/uv/install.sh | sh
windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv venv .venv
uv sync
make migrate-apply
make migrate-create
make migrate-apply


curls

POST:
curl -X POST "http://localhost:8000/reviews" \
-H "Content-Type: application/json" \
-d '{"text":"Сервис просто отличный, мне нравится!"}'

ответ:
{
  "id": 1,
  "text": "Сервис просто отличный, мне нравится!",
  "sentiment": "positive",
  "created_at": "2023-10-25T12:34:56.789Z"
}

GET:
curl "http://localhost:8000/reviews?sentiment=negative"

[
  {
    "id": 2,
    "text": "Всё работает плохо, ненавижу!",
    "sentiment": "negative",
    "created_at": "2023-10-25T12:35:10.123Z"
  }
]

Остальные два варианта работаю по тому же принципу