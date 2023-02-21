from django.urls import path

from webapp.view.base import products_view, product_view, product_add_view
from webapp.view.category import category_add, category_view, category_delete, category_edit

urlpatterns = [
    path('', products_view, name='index'),
    path('products', products_view, name='products_view'),
    path('product/<int:pk>', product_view, name='product_detail_view'),
    path('products/add', product_add_view, name='products_add'),
    path('categories/add', category_add, name='category_add'),
    path('categories', category_view, name='categories_view'),
    path('categories/<int:pk>/delete', category_delete, name='category_delete'),
    path('category/<int:pk>/edit', category_edit, name='category_edit')

]
