# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0003_auto_20150716_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='mapbox_access_token',
            field=models.CharField(default=b'', max_length=80, blank=True, help_text='required for mapbox map style only', null=True, verbose_name='mapbox access token'),
        ),
        migrations.AlterField(
            model_name='map',
            name='mapbox_map_id',
            field=models.CharField(default=b'', max_length=20, blank=True, help_text='required for mapbox map style only', null=True, verbose_name='mapbox map id'),
        ),
        migrations.AlterField(
            model_name='map',
            name='street',
            field=models.CharField(help_text='address for center of map', max_length=100, null=True, verbose_name='street', blank=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='style',
            field=models.CharField(max_length=25, verbose_name='style', choices=[(b'google', b'Google Maps'), (b'mapbox', b'Mapbox')]),
        ),
        migrations.AlterField(
            model_name='map',
            name='zoom',
            field=models.IntegerField(default=8, verbose_name='zoom', choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12'), (13, b'13'), (14, b'14'), (15, b'15'), (16, b'16'), (17, b'17'), (18, b'18'), (19, b'19'), (20, b'20'), (21, b'21')]),
        ),
        migrations.AlterField(
            model_name='pin',
            name='pin_color',
            field=models.CharField(max_length=20, choices=[(b'redIcon', 'red'), (b'blueIcon', 'blue'), (b'greenIcon', 'green'), (b'yellowIcon', 'yellow')]),
        ),
    ]
