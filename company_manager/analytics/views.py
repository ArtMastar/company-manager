from django.shortcuts import render
from orders.models import Order
from inventory.models import InventoryItem
from django.db.models import Count

def analytics_dashboard(request):
    # Example: count orders by status
    order_status_counts = Order.objects.values('status').annotate(count=Count('id'))
    inventory_items = InventoryItem.objects.all()
    context = {
        'order_status_counts': list(order_status_counts),
        'inventory_items': inventory_items,
    }
    return render(request, 'analytics/dashboard.html', context)