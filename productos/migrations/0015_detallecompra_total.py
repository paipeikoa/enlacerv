# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-18 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_auto_20180506_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
