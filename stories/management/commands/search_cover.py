from py_bing_search import PyBingImageSearch
from django.core.management.base import BaseCommand
import requests
from StoriesForAllAges.settings import MEDIA_ROOT
import os
from django.core.files import File
from stories.models import Story


class Command(BaseCommand):

    def handle(self, *args, **options):
        storylist = Story.objects.all()
        for story in storylist:
            if not story.image:
                key_phrase = story.title + story.author + "cover"
                bing_image = PyBingImageSearch('zPkmU+Z1Sp9TlWqX0tEvmTy/U5s3+A0MsPGqiUzHKL4', key_phrase)
                result = bing_image.search(limit=1, format='json')

                img_url = result[0].media_url
                img = requests.get(img_url)
                upload_location = MEDIA_ROOT+"\%s\cover.png" % story.id
                print upload_location
                upload_dir = MEDIA_ROOT+ "\%s" % story.id
                try:
                    os.makedirs(upload_dir)
                except OSError as e:
                    if e.errno == 17:
                        print "dir already exists"

                with open(upload_location, 'wb') as f:
                    f.write(img.content)

                reopen = open(upload_location, "rb")
                django_file = File(reopen)
                story.image.save("\cover.png", django_file, save=True)

                print "Uploaded cover for %s" % story.id
            else:
                pass
