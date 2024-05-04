from django.core.management.base import BaseCommand
from myapp2.models import Order


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(customer_id=pk).first()
        self.stdout.write(f'{order}')