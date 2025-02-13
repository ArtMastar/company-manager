from django.urls import path
from .views import PaymentListView, PaymentCreateView

app_name = 'payments'

urlpatterns = [
    path('', PaymentListView.as_view(), name='list'),
    path('create/', PaymentCreateView.as_view(), name='create'),
]
