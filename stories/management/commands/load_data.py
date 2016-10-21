from django.core.management.base import BaseCommand, CommandError
from stories.models import Story
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_name', nargs='+', type=str)

    def handle(self, *args, **options):
            self.stdout.write('file')
            for csvfile in options['file_name']:
                with open(csvfile, 'rb') as file:
                    rows = csv.reader(file, delimiter=",", quotechar='"')
                    # def get_row_info():
                    #     global title_row = raw_input("Column for title?")
                    #     global author_row = raw_input("Column for author?")
                    #     global pubdate_row= raw_input("Column for pubdate?")
                    # get_row_info()
                    for row in rows:
                        if rows.line_num == 1:
                            continue
                        row[3] = row[3].replace("\n", " ")

                        print "title: " + row[2]
                        print "author:  " + row[3]
                        print "pubdate:   " + row[5]

                        db_row = Story(title=row[2], author=row[3], pubdate=row[5]+"-01-01")
                        db_row.save()

               # dump entire table
                        for story in Story.objects.all():
                            print story
