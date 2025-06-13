# ✨ Winx Club API with Docker ✨

 API для управления феями Winx Club, созданный с использованием FastAPI, MySQL и Docker.

---

##  Демонстрация

[![asciicast](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1.svg)](https://asciinema.org/a/yaCCWGf8wfrhGKee0BLTlIaS1)

---

## Требования

- Docker 20.10+
- Docker Compose 2.0+

---

## Установка и запуск

1. Клонируйте репозиторий:

   
    git clone https://github.com/your-repo/winx-api-git
    cd winx-api-git
    
2. Создайте файл .env.db с переменными окружения для базы данных:

   
    MYSQL_ROOT_PASSWORD=power_of_friendship
    MYSQL_DATABASE=winx_club_db
    MYSQL_USER=winx_user
    MYSQL_PASSWORD=magic123
    
3. Создайте файл .env.app с настройками подключения к базе данных для FastAPI:

   
    DB_HOST=mysql
    DB_PORT=3306
    DB_NAME=winx_club_db
    DB_USER=winx_user
    DB_PASSWORD=magic123
    
4. Соберите и запустите контейнеры:

   
    docker-compose up --build
    
    Приложение будет доступно по адресу:  
    [http://localhost:8000](http://localhost:8000)  

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
docker exec -it winx_mysql mysql -uwinx_user -ppower_of_friendship winx_club_db

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
