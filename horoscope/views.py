from django.http import HttpResponse

zodiac_list = [
    'aries',
    'taurus',
    'gemini',
    'cancer',
    'leo',
    'virgo',
    'libra',
    'scorpio',
    'sagittarius',
    'capricorn',
    'aquarius',
    'pisces'
]


# Create your views here.
def index(request):
    return HttpResponse('Вы попали на страницу приложения Гороскоп')


def get_info_about_zodiac(request, sign_zodiac: str):
    if sign_zodiac in zodiac_list:
        return HttpResponse(f'Гороскоп для {sign_zodiac}')
    return HttpResponse(f'Неверный знак зодиака {sign_zodiac}')
