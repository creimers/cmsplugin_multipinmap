# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0004_auto_20151029_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='street',
            field=models.CharField(max_length=100, null=True, verbose_name='street', blank=True),
        ),
    ]
