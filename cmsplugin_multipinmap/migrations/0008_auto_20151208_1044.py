# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0007_auto_20151111_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='mapbox_access_token',
        ),
        migrations.RemoveField(
            model_name='map',
            name='mapbox_map_id',
        ),
        migrations.AddField(
            model_name='map',
            name='leaflet_tile_url',
            field=models.CharField(default=b'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', max_length=255, verbose_name='tile url'),
        ),
        migrations.AlterField(
            model_name='map',
            name='style',
            field=models.CharField(default=b'leaflet', max_length=25, verbose_name='style', choices=[(b'google', b'Google Maps'), (b'leaflet', b'Leaflet')]),
        ),
    ]
