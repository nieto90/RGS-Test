# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0002_auto_20170428_1500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RGS_User',
            new_name='RGSUser',
        ),
    ]
