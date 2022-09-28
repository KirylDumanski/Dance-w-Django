from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('types', views.index_types),
    path('types/<str:type_zodiac>', views.zodiacs_by_type, name='zodiacs-by-type'),
    path('<int:zodiac_sign_number>', views.get_info_about_zodiac_by_number),
    path('<int:month>/<int:day>', views.get_info_about_zodiac_by_month_and_day),
    path('<str:sign_zodiac>', views.get_info_about_zodiac, name='zodiac-info'),
]
