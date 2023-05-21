
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(primary_key=True, blank=True, max_length=60)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

