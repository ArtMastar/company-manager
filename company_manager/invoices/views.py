from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm, InvoiceLineItemFormSet

class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'invoices'

class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoices/invoice_detail.html'

class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/invoice_form.html'
    success_url = reverse_lazy('invoices:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = InvoiceLineItemFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)
        return response

class InvoiceUpdateView(UpdateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/invoice_form.html'
    success_url = reverse_lazy('invoices:list')

    def form_valid(self, form):
        response = super().form_valid(form)
        formset = InvoiceLineItemFormSet(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.save()
        else:
            return self.form_invalid(form)
        return response

class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoices/invoice_confirm_delete.html'
    success_url = reverse_lazy('invoices:list')
                                                                                                                                                                                                