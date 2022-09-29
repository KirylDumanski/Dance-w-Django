from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='split')
@stringfilter
def split(value: str, key=' '):
    return value.split(key)


@register.filter(name='description')
def description(value: dict, key='desc'):
    return value.get(key)
