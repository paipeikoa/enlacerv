# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-10 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_detallecompra_precio_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='precio_compra',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
