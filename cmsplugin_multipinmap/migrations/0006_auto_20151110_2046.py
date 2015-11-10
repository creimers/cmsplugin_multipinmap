# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0005_auto_20151029_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='link',
            field=models.URLField(null=True, verbose_name='link', blank=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='link_title',
            field=models.URLField(null=True, verbose_name='link title', blank=True),
        ),
    ]
