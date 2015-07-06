# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name', blank=True)),
                ('style', models.CharField(max_length=25, verbose_name='style', choices=[(b'google', b'google maps'), (b'leaflet', b'leaflet maps')])),
                ('height', models.IntegerField(default=400, help_text='height of the map in px.', verbose_name='height')),
                ('zoom', models.IntegerField(default=8, verbose_name='zoom')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal_code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('lat', models.DecimalField(null=True, verbose_name='lat', max_digits=10, decimal_places=6, blank=True)),
                ('lng', models.DecimalField(null=True, verbose_name='lng', max_digits=10, decimal_places=6, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('postal_code', models.CharField(max_length=10, verbose_name='postal_code')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('lat', models.DecimalField(null=True, verbose_name='lat', max_digits=10, decimal_places=6, blank=True)),
                ('lng', models.DecimalField(null=True, verbose_name='lng', max_digits=10, decimal_places=6, blank=True)),
                ('map_plugin', models.ForeignKey(related_name='pins', to='cmsplugin_multipinmap.Map')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
