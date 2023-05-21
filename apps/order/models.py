
from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product

class OrderStatus(models.TextChoices):
    opened = 'opened'
    in_process = 'in_process'
    completed = 'completed'
    canceled = 'canceled'

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.opened)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.pk}"

    class Meta:
        verbose_name = 'Order Information'
        verbose_name_plural = 'Order Information'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveSmallIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.total_cost = self.quantity * self.product.price
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
