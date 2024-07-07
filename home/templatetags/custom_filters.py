# myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return "{:,.2f}".format(value * arg) 
    except (ValueError, TypeError):
        return ''
    
@register.filter
def currency(value):
    try:
        return "${:,.2f}".format(value)
    except (ValueError, TypeError):
        return ''
