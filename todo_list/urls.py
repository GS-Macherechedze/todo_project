from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_home, name='index'),
    path('task_list/', views.task_list, name='task_list'),
    path('task_view/', views.task_view, name='task_view'),
    path('add/', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
