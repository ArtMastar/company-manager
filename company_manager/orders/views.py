from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Order
from .forms import OrderForm, OrderItemFormSet

class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('orders:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = OrderItemFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)
        return response

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'orders/order_form.html'
    success_url = reverse_lazy('orders:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = OrderItemFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)
        return response

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'orders/order_confirm_delete.html'
    uccess_url = reverse_lazy('orders:list')
                                                                                                                                                                                                