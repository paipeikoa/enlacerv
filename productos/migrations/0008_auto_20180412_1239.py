# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-12 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_auto_20180412_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precios',
            name='precio_unitario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Producto', verbose_name='Precios'),
        ),
    ]