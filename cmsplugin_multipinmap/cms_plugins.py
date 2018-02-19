# -*- coding: utf-8 -*-

from django.contrib import admin

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from django.utils.translation import ugettext as _

from .models import Map, Pin


class PinInline(admin.StackedInline):
    model = Pin
    extra = 1
    fields = [
        'pin_color',
        'name',
        'street',
        'postal_code',
        'city',
        'link',
        'link_title',
        'description',
    ]


class MapPlugin(CMSPluginBase):
    model = Map
    name = _("Multipin Map")
    render_template = "cmsplugin_multipinmap/google.html"
    inlines = [PinInline, ]
    exclude = ['lat', 'lng']

    def render(self, context, instance, placeholder):
        template_choices = {
                'google': 'google.html',
                'leaflet': 'leaflet.html',
        }

        self.render_template = '/'.join(
            ['cmsplugin_multipinmap', template_choices[instance.style]])

        context.update({
            'pins': instance.pins.all(),
            'map': instance
        })

        return context


plugin_pool.register_plugin(MapPlugin)
