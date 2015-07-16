# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_multipinmap', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='pin_color',
            field=models.CharField(default='red', max_length=20, choices=[(b'red', 'red'), (b'blue', 'blue'), (b'green', 'green'), (b'yellow', 'yellow')]),
            preserve_default=False,
        ),
    ]
