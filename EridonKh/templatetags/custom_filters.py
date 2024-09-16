from django import template

register = template.Library()


@register.filter(name="unique")
def unique(value):
    return list(dict.fromkeys(value))
