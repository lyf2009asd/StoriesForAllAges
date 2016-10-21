from django.core.management.base import BaseCommand, CommandError
from stories.models import Story
from django.core.files import File
from django.core.files.images import ImageFile


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_name', nargs='+', type=str)


    def handle(self, *args, **options):
            # self.stdout.write('file')
            for img in options["file_name"]:
                # with open(img, 'w+b') as img_file:
                #     img_file.write(img)
                print img
                reopen = open(img, 'r+b')
                print reopen
                django_file = File(reopen)
                print django_file
                storylist = Story.objects.all()
                for story in storylist:
                        print story.id
                        form = Story(suggested_by=story.suggested_by, pk=story.id, image=django_file,
                                         title=story.title, author=story.author, type=story.type, pubdate=story.pubdate)
                        form.save()


