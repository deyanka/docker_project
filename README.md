# Winx Club API with Docker

API для управления феями Winx Club с использованием FastAPI и MySQL в Docker-контейнерах.

## Демонстрация работы
[![asciicast](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1.svg)](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1)  
*(Замените XXXXXX на ID вашей записи asciinema)*

## Требования
- Docker 20.10+
- Docker Compose 2.0+

## Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-repo/winx-api-git
cd winx-api
```
2. Запуск докера
```bash
docker-compose up --build
```

##  Использование API

API доступно по адресу: `http://localhost:8000`

### Эндпоинты

| Метод  | Путь            | Описание                  | Пример запроса |
|--------|-----------------|---------------------------|----------------|
| `POST`   | `/fairies/`     | Создать новую фею         | ```bash
curl -X POST http://localhost:8000/fairies/ \
  -H "Content-Type: application/json" \
  -d '{"fairy_name":"Bloom","age":17,"zodiac_sign":"Dragon","wing_color":"Blue","magic_power":"Fire"}'
``` |
| `GET`    | `/fairies/`     | Получить всех фей         | ```bash
curl http://localhost:8000/fairies/
``` |
| `GET`    | `/fairies/{id}` | Получить фею по ID        | ```bash
curl http://localhost:8000/fairies/1
``` |
| `PATCH`  | `/fairies/{id}` | Обновить данные феи       | ```bash
curl -X PATCH http://localhost:8000/fairies/1 \
  -H "Content-Type: application/json" \
  -d '{"wing_color":"Rainbow"}'
``` |
| `DELETE` | `/fairies/{id}` | Удалить фею               | ```bash
curl -X DELETE http://localhost:8000/fairies/1
``` |
