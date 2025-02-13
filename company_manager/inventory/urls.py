from django.urls import path
from .views import InventoryListView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView

app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='list'),
    path('create/', InventoryCreateView.as_view(), name='create'),
    path('update/<int:pk>/', InventoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', InventoryDeleteView.as_view(), name='delete'),
]