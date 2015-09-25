# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_remove_state_state_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artisan',
            old_name='lga',
            new_name='LGA',
        ),
        migrations.RenameField(
            model_name='producer',
            old_name='lga',
            new_name='LGA',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lga',
            new_name='LGA',
        ),
        migrations.AddField(
            model_name='artisan',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producer',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
