# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0005_currency_dust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='api_url',
            field=models.CharField(blank=True, default='http://localhost:8332', max_length=100, null=True, verbose_name='API hostname'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='label',
            field=models.CharField(default='Bitcoin', max_length=20, unique=True, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='magicbyte',
            field=models.CommaSeparatedIntegerField(default='0,5', max_length=10, verbose_name='Magicbytes'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='ticker',
            field=models.CharField(default='BTC', max_length=4, primary_key=True, serialize=False, verbose_name='Ticker'),
        ),
    ]
