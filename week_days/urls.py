from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<str:day_of_week>', views.todo_list),
]
