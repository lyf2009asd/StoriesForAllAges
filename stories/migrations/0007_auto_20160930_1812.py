# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-30 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_auto_20160929_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='date',
            field=models.DateField(),
        ),
    ]
