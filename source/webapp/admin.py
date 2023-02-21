from django.contrib import admin

from webapp.models import Category, Product


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description')
    list_filter = ('id', 'category')
    search_fields = ('id', 'category', 'description')
    fields = ('id', 'category', 'description')
    readonly_fields = ('id', 'category', 'description')


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'description', 'added_at', 'price', 'image')
    list_filter = ('id', 'category_id', 'description', 'added_at', 'price')
    search_fields = ('id', 'category_id', 'description', 'added_at', 'price')
    fields = ('id', 'category_id', 'description', 'added_at', 'price', 'image')
    readonly_fields = ('id', 'category_id', 'description', 'added_at', 'price', 'image')


admin.site.register(Category, CategoriesAdmin)
admin.site.register(Product, ProductsAdmin)
