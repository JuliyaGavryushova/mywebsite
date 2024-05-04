from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/<int:client_id>/period/<int:time_period>', views.products_ordered_by_customer,
         name='products_ordered_by_customer'),
    path('product/add', views.product_form, name='product_form'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]
