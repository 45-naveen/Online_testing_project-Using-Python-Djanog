import datetime
from django import template

register= template.Library()

@register.simple_tag(name="today")
def get_date():
    n=datetime.datetime.now()
    return n

@register.filter
def quotes(value):
    s='"'+str(value)+'"'
    return s
    