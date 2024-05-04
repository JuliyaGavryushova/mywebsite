from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                'fields': ['name'],
            },
        ),
        (
            'Подробное описание',
            {
                'fields': ['description'],
            },
        ),
        (
            'Цена и количество товара',
            {
                'fields': ['price', 'quantity'],
            },
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email']
    ordering = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    list_filter = ['date_ordered', 'total_price']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)