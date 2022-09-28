from math import pi

from django.http import HttpResponse


# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    sqr = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {sqr}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата со стороной {width} равна {pow(width, 2)}')


def get_circle_area(request, radius: int):
    sqr = pi * pow(radius, 2)
    return HttpResponse('Площадь круга с радиусом {radius} равна {sqr:.2f}'.format(radius=radius, sqr=sqr))
