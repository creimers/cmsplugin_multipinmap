# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0002_pin_pin_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_color',
            field=models.CharField(help_text=b'Only works for leaflet', max_length=20, choices=[(b'redIcon', 'red'), (b'blueIcon', 'blue'), (b'greenIcon', 'green'), (b'yellowIcon', 'yellow')]),
            preserve_default=True,
        ),
    ]
