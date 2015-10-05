# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0005_auto_20151005_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attending',
            field=models.ManyToManyField(related_name='event_attending', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(related_name='event_host', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
