from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
import select2.fields
import select2.models
from django.db.models import Q


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)
# Create your models here.


class Themes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Story(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    # content = models.TextField(default=None, blank=True, null=True)
    pubdate = models.DateField(auto_now=False, auto_now_add=False, null=True)
    suggested_by = models.CharField(max_length=200)
    themes = select2.fields.ManyToManyField(Themes)
    image = models.FileField(upload_to=upload_location,null=True, blank=True)
    # width_field="width_field", height_field="height_field"
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    def last_reading(self):
        last_reading = Reading.objects.filter(story=self).latest('date')

        return last_reading.date or None

    def get_absolute_url(self):
        return reverse("story_detail", kwargs={"id": self.id})
    class Meta:
        ordering = ('title',)


class Reader(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=12)

    def __unicode__(self):
        return self.last_name
    def get_absolute_url(self):
        return reverse("reader_detail", kwargs={"id": self.id})


class Reading(models.Model):
    event = models.CharField(max_length=200, default=None)
    story = select2.fields.ForeignKey(Story, ajax=True, search_field=lambda q: Q(title__icontains=q),overlay="Select a Story.")
    reader = select2.fields.ForeignKey(Reader, ajax=True,search_field=lambda q: Q(last_name__icontains=q),overlay="Select a Reader.")
    date = models.DateField(auto_now=False)

    def __str__(self):
        return self.event

    def get_absolute_url(self):
        return reverse("reading_detail", kwargs={"id": self.id})

    class Meta:
        ordering = ('-date', )