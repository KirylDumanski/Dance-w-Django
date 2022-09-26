from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Вы попали на страницу приложения Week days')


days_of_week = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
]


def todo_list(request, day_of_week: str):
    if day_of_week in days_of_week:
        return HttpResponse(f'Список дел на {day_of_week}')
    return HttpResponse(f'Неверный день недели - {day_of_week}')
