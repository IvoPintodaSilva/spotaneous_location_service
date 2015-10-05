# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0001_initial'),
        ('events', '0004_auto_20151005_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AddField(
            model_name='event',
            name='interest',
            field=models.ForeignKey(default='', to='interests.Interest'),
            preserve_default=False,
        ),
    ]
