# Django-project-menu

Tree menu in Django           


## Приложение для отрисовки меню с помощью templatetag

### Содержание:
+ [Краткое описание](#краткое-описание)
+ [Полезные ссылки](#полезные-ссылки)
+ [Requirements](#requirements)
+ [Сборка и запуск проекта](#сборка-и-запуск)        




### Краткое описание:
Простое Django приложение для отрисовки древовидного меню, реализованное через templatetag. Меню и его элементы создаются и редактируются в админ панели Django. С помощью тега {% draw_menu 'menu_name' %} меню можно расположить на любой странице приложения.




### Полезные ссылки:
+ [Django documentation](https://docs.djangoproject.com/en/2.2/)         



### Requirements:
+ django==2.2.16
+ djangorestframework==3.12.4
+ pytest==6.2.4
+ pytest-django==4.4.0
+ pytest-pythonpath==0.7.3
+ requests==2.26.0
+ Pillow==8.3.1
+ sorl-thumbnail==12.7.0
+ djoser==2.1.0
+ pytz==2019.3
+ sqlparse==0.3.0      




### Сборка и запуск:
! Для корректного отображения меню при запуске следует сначала создать его а так-же добавить в него элементы в админ панели Django.
```bash
git clone git@github.com:Mane26/django-project-menu.git
cd django-project-menu
python -m venv venv
source venv/Scripts/activate 
pip install -r requirements.txt
cd project_test/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
```

### License
This project is licensed under the terms of the MIT license