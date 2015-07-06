# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multipinmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='mapbox_access_token',
            field=models.CharField(default=b'', max_length=60, verbose_name='mapbox access token'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='mapbox_map_id',
            field=models.CharField(default=b'', max_length=20, verbose_name='mapbox map id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='postal code'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='street',
            field=models.CharField(help_text='address for center of map', max_length=100, verbose_name='street'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='style',
            field=models.CharField(max_length=25, verbose_name='style', choices=[(b'google', b'Google Maps'), (b'leaflet', b'Leaflet')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pin',
            name='postal_code',
            field=models.CharField(max_length=10, verbose_name='postal code'),
            preserve_default=True,
        ),
    ]
