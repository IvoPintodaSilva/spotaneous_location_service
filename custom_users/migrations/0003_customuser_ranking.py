# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_auto_20151005_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]
