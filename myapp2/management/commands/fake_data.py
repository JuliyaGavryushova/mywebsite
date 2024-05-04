from django.core.management.base import BaseCommand
from myapp2.models import Client, Product, Order

from faker import Faker
from random import randint

fake = Faker("ru_RU")


class Command(BaseCommand):
    help = "Generate fake client, product and order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        product1 = Product(name=f'Product 1', description=f'Description 1', price=500, quantity=15)
        product1.save()
        product2 = Product(name=f'Product 2', description=f'Description 2', price=1000, quantity=8)
        product2.save()
        product3 = Product(name=f'Product 3', description=f'Description 3', price=3600, quantity=3)
        product3.save()

        for i in range(1, count + 1):
            client = Client(name=fake.name(),
                            email=fake.ascii_free_email(),
                            phone_number=fake.phone_number(),
                            address=fake.street_address())
            client.save()

            for j in range(1, count + 1):
                order = Order(customer=client, total_price=0)
                order.save()
                order.products.add(product1, product2, product3)

