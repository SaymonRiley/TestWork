from django import template
from main.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def render_menu(menu_name, context):
    current_url = context['request'].path
    items = MenuItem.objects.filter(menu_name=menu_name).prefetch_related('children')
    return {'menu_items': items, 'current_url': current_url}
