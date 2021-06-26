from django.core.management.base import BaseCommand
from api.models import Customer

class Command(BaseCommand):
    #def add_arguments(self, parser):
       
    def handle(self, *args, **options):
        print('Cleaning database...')
        Customer.objects.all().delete()
        print('Database cleaned.')