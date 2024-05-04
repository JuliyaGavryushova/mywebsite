from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        # product = Product(name=f'Product 1', description=f'Description 1', price=500, quantity=15)
        # product = Product(name=f'Product 2', description=f'Description 2', price=300, quantity=8)
        # product = Product(name=f'Product 3', description=f'Description 3', price=1300, quantity=10)
        product = Product(name=f'Product 4', description=f'Description 4', price=950, quantity=21)
        product.save()
        self.stdout.write(f'{product}')