# MVP_connect
### **Задание:**

- создать сервер на Django/Flask (для Python)
- подключить базу данных (mongo DB),
- создать пользователя в базе данных,
- проверить как работает, через Postman


## Подготовка и запуск проекта

#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/MVP_connect.git
```

#### Шаг 3. Создайте в клонированной директории файл mvp/.env или попросить ц меня
Пример:
```bash

HOST=<host:cluster:mongodb>
PORT=27017
USERNAME=<username>
PASSWORD=<password>
AUTH_SOURCE=admin
AUTH_MECHANISM=SCRAM-SHA-1
NAME=<name:db>

```
#### Шаг 4. Выполняем комманду
```python
    pip install -r requirements.txt
```

#### Шаг 5.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate
```

#### Шаг 6.Создать суперюзера
```python
    python manage.py createsuperuser
```
#### Шаг 7 Используя Django Faker заполняем БД
```python
    python manage.py authapp_createdata
```

#### Шаг 8. Запускаем сервер 
```python
    python manage.py runserver
```


## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### Получаем список юзеров
```json
GET http://127.0.0.1:8000/users/
```

### Получаем детальную информацию о юзере
```json
GET http://127.0.0.1:8000/users/1/
```


### Документация по API доступно
```html
http://127.0.0.1:8000/swagger/
```

