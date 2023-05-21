# from django.contrib import admin
# from .models import Product, ProductImage

# class ProductImageInline(admin.TabularInline):
#     model = ProductImage

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductImageInline]

#     list_display = ['title', 'category', 'author', 'created_at']
#     list_filter = ['category', 'author']
#     search_fields = ['title']

#     fieldsets = (
#         (None, {
#             'fields': ('title', 'category', 'author')
#         }),
#         ('Additional Information', {
#             'fields': ('description', 'price')
#         }),
#     )

# admin.site.unregister(Product)
# admin.site.register(Product, ProductAdmin)

from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register([Product], ProductAdmin)