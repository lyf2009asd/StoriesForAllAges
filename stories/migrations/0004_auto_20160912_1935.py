# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-13 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='story',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
