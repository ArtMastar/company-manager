from django import forms
from django.forms import inlineformset_factory
from .models import Order, OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'status']

OrderItemFormSet = inlineformset_factory(Order, OrderItem, fields=('inventory_item', 'quantity'),
                                        extra=1, can_delete=True)
            