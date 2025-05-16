from django import template
from django.db import models
from ..models import Menu, MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu = (
            Menu.objects.prefetch_related(
                models.Prefetch(
                    'items',
                    queryset=MenuItem.objects.prefetch_related('children')
                )
            )
            .get(name=menu_name)
        )


        data = {
            'name': menu.name,
            'items': []
        }

        items = menu.items.filter(parent=None)
        for item in items:
            data['items'].append(build_menu_item(item))

        return data
    except Menu.DoesNotExist:
        return {'name': menu_name, 'items': []}


def build_menu_item(item):
    item_dict = {
        'title': item.title,
        'get_absolute_url': item.get_absolute_url(),
        'children': []
    }

    for child in item.children.all():
        item_dict['children'].append(build_menu_item(child))

    return item_dict
