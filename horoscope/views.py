from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}


# Create your views here.
def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ''
    for zodiac in zodiacs:
        redirect_path = reverse('zodiac-info', args=[zodiac])
        li_elements += f"<li> <a href='{redirect_path}'>{zodiac.title()}</a> </li>"
    response = f'<ol>{li_elements}</ol>'
    return HttpResponse(response)


def get_info_about_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(description)
    return HttpResponse(f'Неверный знак зодиака {sign_zodiac}')


def get_info_about_zodiac_by_number(request, zodiac_sign_number: int):
    zodiacs = list(zodiac_dict)
    if zodiac_sign_number > len(zodiacs):
        return HttpResponse(f'Неправильный порядковый номер зодиака - {zodiac_sign_number}')
    zodiac_name = zodiacs[zodiac_sign_number - 1]
    redirect_url = reverse('zodiac-info', args=[zodiac_name])
    return HttpResponseRedirect(redirect_url)
