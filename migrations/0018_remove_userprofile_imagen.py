# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-27 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_auto_20180327_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='imagen',
        ),
    ]
