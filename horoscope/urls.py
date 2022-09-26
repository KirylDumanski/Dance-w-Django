from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<sign_zodiac>', views.get_info_about_zodiac),
]
