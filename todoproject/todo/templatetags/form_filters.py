from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class to a form field widget.
    Usage: {{ form.field|add_class:"class-name" }}
    """
    existing_classes = field.field.widget.attrs.get('class', '')
    if existing_classes:
        new_classes = existing_classes + ' ' + css_class
    else:
        new_classes = css_class
    return field.as_widget(attrs={'class': new_classes})
