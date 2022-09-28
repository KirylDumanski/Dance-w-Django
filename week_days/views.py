from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

days_of_week = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday'
]


def index(request):
    li_elements = ''
    for day in days_of_week:
        redirect_path = reverse('todo-list', args=[day])
        li_elements += f'<li> <a href="{redirect_path}"> {day.title()} </a> </li>'
    response = f'<ol> {li_elements} </ol>'
    return HttpResponse(response)


def todo_list(request, day_of_week: str):
    if day_of_week in days_of_week:
        return HttpResponse(f'Список дел на {day_of_week}')
    return HttpResponse(f'Неверный день недели - {day_of_week}')


def todo_list_by_number(request, day_of_week: int):
    if day_of_week not in range(1, 8):
        return HttpResponse(f'Неверный порядковый номер недели - {day_of_week}')
    day = days_of_week[day_of_week - 1]
    redirect_url = reverse('to-do-list', args=[day])
    return HttpResponseRedirect(redirect_url)
