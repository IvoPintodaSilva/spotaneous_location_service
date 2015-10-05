# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=250)),
                ('beggining', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('cost', models.IntegerField()),
                ('type', models.CharField(max_length=10, choices=[(b'PRIV', b'Private'), (b'PUB', b'Public')])),
                ('min_people', models.IntegerField()),
                ('max_people', models.IntegerField()),
            ],
        ),
    ]
