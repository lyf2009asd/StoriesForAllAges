from django.core.management.base import BaseCommand, CommandError
from stories.models import Story
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
            self.stdout.write('file')
            for filename in options['file_name']:
                update_location = "%s" % filename
                datas = Story.objects.all()
                with open(update_location, 'wb') as csvfile:
                    writer = csv.writer(csvfile, dialect="excel")

                    for data in datas:
                        writer.writerow([data.title, data.author, data.pubdate])



