from django.db import models

from django.db import models
from django.contrib.auth import get_user_model

class PaymentMethod(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='payment_methods')
    name = models.CharField(max_length=255)
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Payment Method'
        verbose_name_plural = 'Payment Methods'


class Transaction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='transactions')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as per your requirements

    def __str__(self):
        return f"Transaction #{self.pk}"

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

