# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-11 18:31
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='reader',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Reader'),
        ),
        migrations.AlterField(
            model_name='reading',
            name='story',
            field=select2.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.Story'),
        ),
        migrations.AlterField(
            model_name='story',
            name='themes',
            field=select2.fields.ManyToManyField(to='stories.Themes'),
        ),
    ]
