from django.core.management.base import BaseCommand
from django.conf import settings
import os.path
import csv
from freeshelf.models import Book


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        #parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        print("Deleting books...")
        Book.objects.all().delete()
        with open(os.path.join(settings.BASE_DIR, 'initial_data', 
                                'books.csv')) as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                
                book = Book(
                    title=row['title'],
                    author=row['author'],
                    description=row['description'],
                    slug=row['slug']
                )
                book.save()
        print("Books loaded successfully!")