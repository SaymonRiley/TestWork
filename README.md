# TreeMenu Django App

## Описание

Это приложение Django реализует древовидное меню, которое позволяет управлять элементами меню через админку Django. Меню хранится в базе данных и отображается на страницах сайта.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/SaymonRiley/TestWork.git
   cd TestWork/TreeMenu
Создайте виртуальное окружение:

bash
Копировать код
python -m venv env
Активируйте виртуальное окружение:

Windows:

bash
Копировать код
.\env\Scripts\activate
Mac/Linux:

bash
Копировать код
source env/bin/activate
Установите зависимости:

bash
Копировать код
pip install -r requirements.txt
Проведите миграции базы данных:

bash
Копировать код
python manage.py migrate
Создайте суперпользователя для доступа к админке:

bash
Копировать код
python manage.py createsuperuser
Запустите сервер разработки:

bash
Копировать код
python manage.py runserver
Перейдите в админку по адресу: http://127.0.0.1:8000/admin и добавьте элементы меню.

Использование
Для отображения меню на странице используйте тег:

html
Копировать код
{% draw_menu 'main_menu' %}
Структура проекта
main/: Основное приложение, которое содержит модели, представления и URL-адреса.
templates/: Шаблоны HTML для страниц.
requirements.txt:Информация о библиотек

Требования
Django (версия, указанная в requirements.txt)
Python (рекомендуемая версия: 3.8+)

