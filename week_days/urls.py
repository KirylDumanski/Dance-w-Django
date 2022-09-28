from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:day_of_week>', views.todo_list_by_number),
    path('<str:day_of_week>', views.todo_list, name='todo-list'),
]
