# Тестовое задание на позицию Python разработчик в компанию "ПУЛЬСАР МСК"

---

## Технологии:

- Python 3.10
- Django==4.1.4
- django-filter==22.1
- djangorestframework==3.14.0
- drf-spectacular==0.25.0
- Pillow==9.3.0
- БД sqlite3
---

## Запуск:
- `git clone `
- `pip install -r requirements.txt`
- `./manage.py migrate`
- `./manage.py runserver`

## Эндпоинты:
- http://127.0.0.1:8000/admin/ - панель администратора Django (login: admin, pass: qwe123)
- http://127.0.0.1:8000/products/ - список всех товаров
- http://127.0.0.1:8000/products/<int:pk>/ - детальная информация конкретного товара
- http://127.0.0.1:8000/api/schema/swagger_ui/ - документация (Swagger)

