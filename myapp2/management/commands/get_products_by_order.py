from django.core.management.base import BaseCommand
from myapp2.models import Order, Product
from datetime import datetime, timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('day', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        day = kwargs.get('day')
        today = timezone.now()
        start_date = today - timezone.timedelta(days=day)
        orders = Order.objects.filter(customer_id=pk, date_ordered__range=(start_date, today))
        products = []
        for order in orders:
            products.extend(order.products.all())

        unique_products = list(set(products))
        for product in unique_products:
            self.stdout.write(f'{product.name}')
