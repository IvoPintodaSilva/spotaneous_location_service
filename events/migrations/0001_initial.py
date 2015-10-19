# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0001_initial'),
        ('interests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('beggining', models.DateTimeField()),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('cost', models.IntegerField(null=True, blank=True)),
                ('type', models.CharField(max_length=10, choices=[(b'PRIV', b'Private'), (b'PUB', b'Public')])),
                ('min_people', models.IntegerField()),
                ('max_people', models.IntegerField(null=True, blank=True)),
                ('attending', models.ManyToManyField(related_name='event_attending', to='custom_users.CustomUser', blank=True)),
                ('host', models.ForeignKey(related_name='event_host', to='custom_users.CustomUser')),
                ('interest', models.ForeignKey(to='interests.Interest')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
