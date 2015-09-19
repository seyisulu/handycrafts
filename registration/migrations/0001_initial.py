# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=10)),
                ('lga', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='producer',
            name='product',
            field=models.ManyToManyField(to='registration.Product'),
        ),
        migrations.AddField(
            model_name='artisan',
            name='skill',
            field=models.ForeignKey(to='registration.Skill'),
        ),
    ]
