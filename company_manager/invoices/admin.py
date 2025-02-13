from django.contrib import admin
from .models import Invoice, InvoiceLineItem

class InvoiceLineItemInline(admin.TabularInline):
    model = InvoiceLineItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceLineItemInline]

admin.site.register(Invoice, InvoiceAdmin)
            