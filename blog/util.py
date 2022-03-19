from django.template import Library

register = Library()

@register.filter
def cut(value, cut):
    value = value.replace(cut, '')
    return value