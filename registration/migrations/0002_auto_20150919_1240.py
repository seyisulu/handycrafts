# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalGovernment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('state_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('state_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='artisan',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='lga',
            field=models.ForeignKey(to='registration.LocalGovernment'),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='state',
            field=models.ForeignKey(to='registration.State'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='producer',
            name='lga',
            field=models.ForeignKey(to='registration.LocalGovernment'),
        ),
        migrations.AlterField(
            model_name='producer',
            name='state',
            field=models.ForeignKey(to='registration.State'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='lga',
            field=models.ForeignKey(to='registration.LocalGovernment'),
        ),
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.ForeignKey(to='registration.State'),
        ),
    ]
