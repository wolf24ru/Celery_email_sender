
## Отправка email всем пользователям 
Реализованно на основе проекта [flask_app](https://github.com/wolf24ru/flask_app).  
К основному проекту добавлено:
- асинхронная отправка сообщений;
- celery 

###Команда для запуска дебага smtp сервера
```shell
python -m smtpd -n -c DebuggingServer localhost:1025
```

###Команда для запуска миграций 
```shell
./migrate.sh
```
###Команда для запуска **Сrlery**
```shell
celery -A selery_email.celery worker
```

###Запуск приложения run.py
```shell
export FLASK_APP=run
flask run -p 8000
 ```
#Работа за API:
###Отправку запроса производить на адрес запущенного Flask приложения.   
Адрес по умолчанию -  http://127.0.0.1:8000/

|Описание                   | Метод  | Ссылка              |JSON аргументы | 
|---------------------------|--------|---------------------|---------------| 
|Проверка соединения:       | GET    | /health             |                                                |
|Создание пользователя      | POST   | /new_user           |<span style="color: #E79234;">**user_name**</span> - имя пользователя;  <span style="color: #E79234;">**password**</span> - пароль|
|Получтиь пользователя по id| GET    | /get_user/<user_id> |                                                |
|Создание рекламного объявления          | POST   | /adv_new            |<span style="color: #E79234;">**user_name**</span> - имя пользователя;  <span style="color: #E79234;">**password**</span> - пароль; <span style="color: #E79234;">**title**</span> - название объявления; <span style="color: #E79234;">**description**</span> - описание объвления|
|Получение всех рекламных объявлений| GET    | /adv                ||
|Получение ремногого объявления по id| GET    | /adv/<adv_id>       ||
|Удаление рекламного объявления| DELETE | /adv_del/<adv_id>   |<span style="color: #E79234;">**user_name**</span> - имя пользователя;  <span style="color: #E79234;">**password**</span> - пароль;|
|Изменение рекламного объявления| PATCH  | /adv_patch/<adv_id> |<span style="color: #E79234;">**user_name**</span> - имя пользователя;  <span style="color: #E79234;">**password**</span> - пароль; <span style="color: #E79234;">**title**</span> - название объявления; <span style="color: #E79234;">**description**</span> - описание объвления|
|Отправка сообщений на все email адреса| POST   |/email/send/|
|Проверка состояния запроса|GET|/email/task/<task_id>|<span style="color: #E79234;">**task_id**</span> - токен полученный при POST запросе

**<user_id>** - идентификатор пользователя  
**<adv_id>** - идентификатор рекламного объявления
