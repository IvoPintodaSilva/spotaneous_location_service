# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20151005_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='max_people',
            field=models.IntegerField(blank=True),
        ),
    ]
