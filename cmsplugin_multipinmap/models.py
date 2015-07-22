from django.db import models

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from django.core.exceptions import ValidationError

from django.conf import settings

from cms.models import CMSPlugin

from geopy.geocoders import Nominatim

@python_2_unicode_compatible
class Map(CMSPlugin):

    name = models.CharField(_('name'), max_length=50, blank=True, null=True)

    STYLE_CHOICES = (
        ('google', 'Google Maps'),
        ('leaflet', 'Leaflet'),
    )
    style = models.CharField(_('style'), max_length=25, choices=STYLE_CHOICES)

    mapbox_access_token = models.CharField(
        _('mapbox access token'),
        max_length=80,
        default=getattr(settings, 'MAPBOX_ACCESS_TOKEN', ''),
        help_text=_('required for leaflet map style only'),
        blank=True,
        null=True
    )
    mapbox_map_id = models.CharField(
        _('mapbox map id'),
        max_length=20,
        default=getattr(settings, 'MAPBOX_MAP_ID', ''),
        help_text=_('required for leaflet map style only'),
        blank=True,
        null=True
    )

    height = models.IntegerField(
        _('height'),
        help_text=_("height of the map in px."),
        default=400
    )
    ZOOM_LEVELS = map(lambda c: (c, str(c)), range(22))
    zoom = models.IntegerField(
        _('zoom'),
        choices=ZOOM_LEVELS,
        default=8
    )
    
    # center address
    street = models.CharField(
        _('street'),
        max_length=100,
        help_text=_('address for center of map')
        )
    postal_code = models.CharField(_('postal code'), max_length=10)
    city = models.CharField(_('city'), max_length=100)
    lat = models.DecimalField(
        _('lat'),
        null=True,
        blank=True,
        decimal_places=6,
        max_digits=10
    )
    lng = models.DecimalField(
        _('lng'),
        null=True,
        blank=True,
        decimal_places=6,
        max_digits=10
    )

    def clean(self, *args, **kwargs):
        if self.style == 'leaflet' and self.mapbox_access_token == '':
            raise ValidationError({
                'mapbox_access_token': _('mapbox access token is required')
                })
        if self.style == 'leaflet' and self.mapbox_map_id == '':
            raise ValidationError({
                'mapbox_map_id': _('mapbox map id is required')
                })

        geolocator = Nominatim() 
        location = geolocator.geocode(
            " ".join([self.street, self.postal_code, self.city])
        )
        if location:
            self.lat = location.latitude
            self.lng = location.longitude
        else:
            raise ValidationError({
                'street': _('not a valid address'),
                'postal_code': _('not a valid address'),
                'city': _('not a valid address'),
            })

    def copy_relations(self, oldinstance):
        for pin in oldinstance.pins.all():
            pin.pk = None
            pin.map_plugin = self
            pin.save()

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'multipin map'

@python_2_unicode_compatible
class Pin(models.Model):
    name = models.CharField(_('name'), max_length=50)
    map_plugin = models.ForeignKey(Map, related_name="pins")

    street = models.CharField(_('street'), max_length=100)
    postal_code = models.CharField(_('postal code'), max_length=10)
    city = models.CharField(_('city'), max_length=100)
    COLOR_CHOICES = (
        ('redIcon', _('red')),
        ('blueIcon', _('blue')),
        ('greenIcon', _('green')),
        ('yellowIcon', _('yellow'))
    )

    pin_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
    )

    lat = models.DecimalField(
        _('lat'),
        null=True,
        blank=True,
        decimal_places=6,
        max_digits=10
    )
    lng = models.DecimalField(
        _('lng'),
        null=True,
        blank=True,
        decimal_places=6,
        max_digits=10
    )

    def clean(self, *args, **kwargs):
        geolocator = Nominatim() 
        location = geolocator.geocode(
            " ".join([self.street, self.postal_code, self.city])
        )
        if location:
            self.lat = location.latitude
            self.lng = location.longitude
        else:
            raise ValidationError({
                'street': _('not a valid address'),
                'postal_code': _('not a valid address'),
                'city': _('not a valid address'),
            })

    def __str__(self):
        return self.name
