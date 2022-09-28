from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse

zodiac_dict = {
    'aries': {
        'desc': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
        'days': [80, 110]
    },
    'taurus': {
        'desc': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
        'days': [111, 141]
    },
    'gemini': {
        'desc': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
        'days': [142, 172]
    },
    'cancer': {
        'desc': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
        'days': [173, 203]
    },
    'leo': {
        'desc': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
        'days': [204, 233]
    },
    'virgo': {
        'desc': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
        'days': [234, 266]
    },
    'libra': {
        'desc': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
        'days': [267, 296]
    },
    'scorpio': {
        'desc': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
        'days': [297, 326]
    },
    'sagittarius': {
        'desc': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
        'days': [327, 356]
    },
    'capricorn': {
        'desc': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
        'days': [357, 20]
    },
    'aquarius': {
        'desc': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
        'days': [21, 50]
    },
    'pisces': {
        'desc': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
        'days': [51, 79]
    },
}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


# Create your views here.
def index(request):
    zodiacs = list(zodiac_dict)
    # li_elements = ''
    # for zodiac in zodiacs:
    #     redirect_path = reverse('zodiac-info', args=[zodiac])
    #     li_elements += f"<li> <a href='{redirect_path}'>{zodiac.title()}</a> </li>"
    # response = f'<ol>{li_elements}</ol>'
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_about_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    context = {
        'description_zodiac': description['desc'] if description else description,
        'sign': sign_zodiac
    }
    return render(request, 'horoscope/info_zodiac.html', context=context)


def get_info_about_zodiac_by_number(request, zodiac_sign_number: int):
    zodiacs = list(zodiac_dict)
    if zodiac_sign_number > len(zodiacs):
        return HttpResponse(f'Неправильный порядковый номер зодиака - {zodiac_sign_number}')
    zodiac_name = zodiacs[zodiac_sign_number - 1]
    redirect_url = reverse('zodiac-info', args=[zodiac_name])
    return HttpResponseRedirect(redirect_url)


def get_info_about_zodiac_by_month_and_day(request, month, day):
    try:
        day_from_begin_of_year = int(datetime.strptime(f'2022-{month}-{day}', '%Y-%m-%d').strftime('%j'))
    except ValueError:
        return HttpResponseNotFound(f'Ошибка формата даты. Не существует - {month} месяца и/или {day} - дня')

    for key in zodiac_dict:
        if 357 <= day_from_begin_of_year <= 365 or 1 <= day_from_begin_of_year <= 20:  # cause capricorn days number between 357-365 and 1-20
            redirect_path = reverse('zodiac-info', args=['capricorn'])
            return HttpResponseRedirect(redirect_path)
        elif zodiac_dict[key]['days'][0] <= day_from_begin_of_year <= zodiac_dict[key]['days'][1]:
            redirect_path = reverse('zodiac-info', args=[key])
            return HttpResponseRedirect(redirect_path)


def index_types(request):
    types_list = types
    context = {
        'types_list': types_list
    }
    return render(request, 'horoscope/types_zodiac.html', context=context)


def zodiacs_by_type(request, type_zodiac):
    li_elements = ''
    if type_zodiac in types:
        for zodiac in types[type_zodiac]:
            redirect_path = reverse('zodiac-info', args=[zodiac])
            li_elements += f'<li> <a href="{redirect_path}"> {zodiac.title()} </a> </li>'
        response = f"<ul> {li_elements} </ul>"
        return HttpResponse(response)

    return HttpResponseNotFound(f"Не найдена стихия: {type_zodiac}")
