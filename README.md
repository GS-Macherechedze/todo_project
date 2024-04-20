# Integrate-database-with-django

Install Django 
pip install django

Create a Django project:
$django-admin startproject todo_project


Create a Django app
>>python manage.py startapp todo_list

Create migrations:
>>python manage.py makemigrations

Apply migrations:
>>python manage.py migrate
>>
>>Optional unless migration is not applied
>>python manage.py makemigrations --empty todo_list  

Start Django development server:
>>python manage.py runserver

Access Django admin interface:
Open a web browser and go to http://127.0.0.1:8000/admin

Access Django shell:
>>python manage.py shell

Query data from Django shell:
>>from todo_list.models import Task
>>all_tasks = Task.objects.all()
>>print(all_tasks)


#modified the template by including a title bar and footer for appealiness
