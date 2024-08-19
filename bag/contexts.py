from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total_price = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, int):
            quantity = item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            for size, quantity in item_data['items_by_size'].items():
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                })
        total_price += quantity * product.price
        product_count += quantity

    if total_price < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total_price * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total_price
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

    grand_total = total_price + delivery

    context = {
        'bag_items': bag_items,
        'total': total_price,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
