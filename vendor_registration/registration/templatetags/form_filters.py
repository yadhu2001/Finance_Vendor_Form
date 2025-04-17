from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

from django import template

register = template.Library()

@register.filter(name='add_required_label')
def add_required_label(field):
    label = field.label
    if field.field.required:
        label += ' <span style="color: red;">*</span>'
    return label

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})
