from django.urls import path
from .views import InvoiceListView, InvoiceDetailView, InvoiceCreateView, InvoiceUpdateView, InvoiceDeleteView

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='list'),
    path('create/', InvoiceCreateView.as_view(), name='create'),
    path('<int:pk>/', InvoiceDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', InvoiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', InvoiceDeleteView.as_view(), name='delete'),
]