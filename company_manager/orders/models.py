from django.db import models
from inventory.models import InventoryItem
from accounts.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    order_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    accountant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    limit_choices_to={'role': 'accountant'})

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.inventory_item.name} (x{self.quantity})"                                                                                                   