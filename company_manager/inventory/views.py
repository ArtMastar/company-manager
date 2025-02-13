from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import InventoryItem

class InventoryListView(ListView):
    model = InventoryItem
    template_name = 'inventory/inventory_list.html'
    context_object_name = 'items'

class InventoryCreateView(CreateView):
    model = InventoryItem
    fields = ['name', 'description', 'quantity', 'price']
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')

class InventoryUpdateView(UpdateView):
    model = InventoryItem
    fields = ['name', 'description', 'quantity', 'price']
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:list')

class InventoryDeleteView(DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory:list')
                                                