#AuctionAPI

Задача: реализовать API сервиса-аукциона

Функционал для пользователей системы:

    получение списка активных лотов (для все пользователей)
    создание/просмотр лота, возможность повысить ставку по активному лоту (только для зарегистрированных пользователей).
    При повышении ставки владельцу лота приходит уведомление об этом на почту
    редактирование/удаление лота (только свой лот)

Функционал для администратора системы:
    весь функционал пользователей вне зависимости от владельца лота

Технологии:
- Python3
- Django >=3
- СУБД PostgresSQL
- Docker
- Celery, Redis - для отправки email
- Описание API - Swagger OpenApi Version 3

### Installation guide
```
cd auctionAPI
docker-compose up --build
```

Для создания суперпользователя необходимо войти в запущенный контйнер

docker exec -it auctionapi_container bash
python manage.py createsuperuser

Вход в админку: 127.0.0.1:8000/admin/

## Создание пользователя

Пользователя можно создать через админку или:

http://127.0.0.1:8000/auth/users/ (ввести username, почту пароль и отправить post запрос)

После post запроса на указанную при регистрации почту придет письмо, которые будет содержать ссылку с uid и token. Пример: http://127.0.0.1:8000/#/activate/MjA3/ahj9ec-0883dba0434bf57525725e586cbab31

ahj9ec-0883dba0434bf57525725e586cbab31 - token

MjA3 - uid

Для подтверждения email необходимо отправить post запрос с uid  и token по адресу: http://127.0.0.1:8000/auth/users/activation/

*** отправка email реализована через консоль, т.е. в консоли вы увидите все отправленные email с нужной информацией

## API documentation

### Swagger Open API

Для входа в документацию swagger необходимо при запущенном контейнере перейти по ссылке http://127.0.0.1:8000/api/docs/
Документация построена с помощью библиотеки drf_spectacular

#### JWT-token

Для тестирования api приложения необходимо выписать себе jwt-token, для этого нужно перейти по адресу

http://127.0.0.1:8000/auth/jwt/create/

отправить post запрос с логином и паролем далее использовать этот token

