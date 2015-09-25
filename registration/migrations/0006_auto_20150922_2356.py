# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20150920_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producer',
            name='lga',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='product',
        ),
        migrations.RemoveField(
            model_name='producer',
            name='state',
        ),
        migrations.AddField(
            model_name='artisan',
            name='number_of_ratings',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Producer',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
