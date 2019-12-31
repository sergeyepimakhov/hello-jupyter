from django import template
from nbconvert import filters

register = template.Library()


@register.filter
def ansi2html(text):
    return filters.ansi2html(text)


@register.filter
def markdown2html(text):
    return filters.markdown2html(text)
