from .models import FoodItem, Order
from django.db.models import Count

def get_recommendations(user):
    """ Return recommended food items based on order history and popularity """

    # Get the user's past orders
    past_orders = Order.objects.filter(customer=user).prefetch_related('items')

    if past_orders.exists():
        # Get most frequently ordered items
        ordered_items = past_orders.values_list('items', flat=True)
        frequent_items = FoodItem.objects.filter(id__in=ordered_items)\
                                         .annotate(order_count=Count('order'))\
                                         .order_by('-order_count')[:5]
        if frequent_items:
            return frequent_items

    # If no order history, return most popular items
    popular_items = FoodItem.objects.annotate(order_count=Count('order'))\
                                    .order_by('-order_count')[:5]
    if popular_items:
        return popular_items

    # If no popular items, return latest available food items
    return FoodItem.objects.filter(availability=True).order_by('-id')[:5]
