from django.db import models
from apps.product.models import Product
from apps.account.models import User

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product', 'user')

    def __str__(self):
        return f'Rating for {self.product.name} by {self.user.username}'
