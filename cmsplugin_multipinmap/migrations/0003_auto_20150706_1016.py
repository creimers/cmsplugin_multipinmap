# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multipinmap', '0002_auto_20150706_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='mapbox_access_token',
            field=models.CharField(default=b'', max_length=60, blank=True, help_text='required for leaflet map style only', null=True, verbose_name='mapbox access token'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='mapbox_map_id',
            field=models.CharField(default=b'', max_length=20, blank=True, help_text='required for leaflet map style only', null=True, verbose_name='mapbox map id'),
            preserve_default=True,
        ),
    ]
