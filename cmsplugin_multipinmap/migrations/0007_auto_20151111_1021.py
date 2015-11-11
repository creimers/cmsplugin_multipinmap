# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0006_auto_20151110_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='link_title',
            field=models.CharField(max_length=255, null=True, verbose_name='link title', blank=True),
        ),
    ]
