# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20150922_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='skill',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
    ]
