from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceLineItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['order', 'due_date', 'total_amount', 'paid']

InvoiceLineItemFormSet = inlineformset_factory(Invoice, InvoiceLineItem,
                                                        fields=('description', 'quantity', 'unit_price'),
                                                        extra=1, can_delete=True)            