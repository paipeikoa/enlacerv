# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-11-23 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0025_producto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
