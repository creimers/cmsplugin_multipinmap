# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multipinmap', '0003_auto_20150706_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='mapbox_access_token',
            field=models.CharField(default=b'', max_length=80, blank=True, help_text='required for leaflet map style only', null=True, verbose_name='mapbox access token'),
            preserve_default=True,
        ),
    ]
