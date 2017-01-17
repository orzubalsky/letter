# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-17 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('letters', '0002_auto_20170116_2041'),
        ('events', '0002_auto_20170116_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='related_letters',
            field=models.ManyToManyField(blank=True, to='letters.Letter'),
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('person', 'event')]),
        ),
    ]
