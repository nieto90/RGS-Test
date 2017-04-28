# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 14:56
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RGS_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(18)])),
                ('interests', models.ManyToManyField(to='matching.Interest')),
            ],
        ),
    ]
