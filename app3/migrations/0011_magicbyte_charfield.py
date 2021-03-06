# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-02-04 16:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0010_withdrawtransaction_walletconflicts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='magicbyte',
            field=models.CharField(default='0,5', max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='Magicbytes'),
        ),
    ]
