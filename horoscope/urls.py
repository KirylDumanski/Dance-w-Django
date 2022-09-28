from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:zodiac_sign_number>', views.get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac, name='zodiac-info'),
]
