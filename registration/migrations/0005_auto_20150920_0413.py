# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150920_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artisan',
            old_name='LGA',
            new_name='lga',
        ),
        migrations.RenameField(
            model_name='producer',
            old_name='LGA',
            new_name='lga',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='LGA',
            new_name='lga',
        ),
    ]
