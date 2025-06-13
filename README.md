# ✨ Winx Club API with Docker ✨

 API для управления феями Winx Club, созданный с использованием FastAPI, MySQL и Docker.

---

##  Демонстрация

[![asciicast](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1.svg)](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1)

---


## Установка и запуск

1. Клонируйте репозиторий:

   
    git clone https://github.com/deyanka/docker_project
    cd winx-api-git

    
2. Соберите и запустите контейнеры:

   
    docker-compose up --build
    
    Приложение будет доступно по адресу:  
    http://localhost:8000

---

## Использование API

### Основные эндпоинты:

| Метод  | Путь             | Описание                  |
|--------|------------------|---------------------------|
| POST   | /fairies/      | Создать новую фею         |
| GET    | /fairies/      | Получить всех фей         |
| GET    | /fairies/{id}  | Получить фею по ID        |
| DELETE | /fairies/{id}  | Удалить фею               |

---
##Отправка запросов
```bash
# Подключиться к MySQL
docker exec -it winx_mysql mysql -uflora -ppower_of_friendship winx_club_db

# Проверить данные
SELECT * FROM winx_fairies;
```
### Примеры запросов

Создание феи:

```bash
curl -X POST http://localhost:8000/fairies/ \
  -H "Content-Type: application/json" \
  -d '{"fairy_name":"Bloom","age":17,"zodiac_sign":"Dragon","wing_color":"Blue","magic_power":"Fire"}'
```

![Логотип Winx](https://avatars.mds.yandex.net/i?id=1b8456082045de2ca8175ee617090ae8a57ea5b9-5887755-images-thumbs&n=13)
