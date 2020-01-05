from django import template
from nbconvert import filters
import re

register = template.Library()


@register.filter
def ansi2html(text):
    return filters.ansi2html(text)


@register.filter
def markdown2html(text):
    return filters.markdown2html(text)


@register.filter
def language(lines):
    first_line = lines[0]

    first_line = first_line.lstrip()  # trim whitespaces from the left
    if (re.search(r'^%%(bash|sh)(.*)\n?$', first_line) or
            re.search(r'^\s*[!]+\s*(.*)$', first_line) or
            re.search(r'^%env\s*(.*)$', first_line) or
            re.search(r'^%(cat|cp|ls|man|mkdir|more|mv|pwd|rm|rmdir)(.*)$', first_line)):
        language = 'shell' # TODO: shell may be?
    elif re.search(r'^%%(html|HTML)\n?$', first_line):
        language = 'html'
    else:
        language = 'python'

    return language
