# template tag for wishlist

from django import template

register = template.Library()


@register.filter(name='is_in_wishlist')
def is_in_wishlist(product, user):
    if user.is_authenticated:
        return product in user.wishlist.products.all()
    return False