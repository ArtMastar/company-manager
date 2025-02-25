from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('inventory/', include('inventory.urls', namespace='inventory')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('invoices/', include('invoices.urls', namespace='invoices')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('', lambda request: redirect('accounts:dashboard')),
]
