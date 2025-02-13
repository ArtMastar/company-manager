from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Payment
from .forms import PaymentForm

class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    context_object_name = 'payments'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/payment_form.html'
    success_url = reverse_lazy('payments:list')
                