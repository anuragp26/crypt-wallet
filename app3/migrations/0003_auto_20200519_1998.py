# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_auto_20200519_1997'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawtransaction',
            name='fee',
            field=models.DecimalField(null=True, verbose_name='Fee', max_digits=18, decimal_places=8, blank=True),
        ),
    ]
