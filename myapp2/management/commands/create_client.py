from django.core.management.base import BaseCommand
from myapp2.models import Client

from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name=fake.name(),
                         email=fake.ascii_free_email(),
                         phone_number=fake.phone_number(),
                         address=fake.street_address())
        client.save()
        self.stdout.write(f'{client}')
