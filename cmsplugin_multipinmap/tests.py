from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cms import api
from cms.models import CMSPlugin
from cms.test_utils.testcases import BaseCMSTestCase
from cms.utils import get_cms_setting


from . import models
from . import cms_plugins


class MultipinmapTestCase(TestCase, BaseCMSTestCase):
    su_username = 'user'
    su_password = 'pass'

    def setUp(self):
        self.template = get_cms_setting('TEMPLATES')[0][0]
        self.language = settings.LANGUAGES[0][0]
        self.page = api.create_page('page', self.template, self.language, published=True)
        self.placeholder = self.page.placeholders.all()[0]
        self.superuser = self.create_superuser()

    def tearDown(self):
        self.client.logout()

    def create_superuser(self):
        return User.objects.create_superuser(self.su_username, 'email@example.com', self.su_password)

    def test_add_multipinmap_plugin_google(self):
        street = 'Hongkongstrasse 10'
        postal_code = '20457'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='google',
           street=street,
           postal_code=postal_code,
           city=city
        )
        pin1 = models.Pin(
            name="greenpeace",
            street=street,
            postal_code=postal_code,
            city=city,
            map_plugin=multipinmap_plugin
        )
        pin1.save()

        self.assertTrue(pin1.__str__() == 'greenpeace')
        self.assertTrue(multipinmap_plugin.__str__() == 'test')
        self.assertTrue(
            models.Map.objects.filter(pk=multipinmap_plugin.pk).exists()
        )

    def test_add_multipinmap_plugin_google_wrong_pin(self):
        street = 'Hongkongstrasse 10'
        postal_code = '20457'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='google',
           street=street,
           postal_code=postal_code,
           city=city
        )
        pin1 = models.Pin(
            name="greenpeace",
            street='Paul-Roosen-Strasse 999',
            postal_code=postal_code,
            city=city,
            map_plugin=multipinmap_plugin
        )
        self.assertRaises(ValidationError, pin1.full_clean)

    def test_add_multipinmap_plugin_leaflet(self):
        street = 'Hongkongstrasse 10'
        postal_code = '20457'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='leaflet',
           mapbox_access_token='waddehaddedudeda',
           mapbox_map_id='waddehaddedudeda',
           street=street,
           postal_code=postal_code,
           city=city
        )
        pin1 = models.Pin(
            name="greenpeace",
            street=street,
            postal_code=postal_code,
            city=city,
            map_plugin=multipinmap_plugin
        )
        pin1.save()

        self.assertTrue(pin1.__str__() == 'greenpeace')
        self.assertTrue(
            models.Map.objects.filter(pk=multipinmap_plugin.pk).exists()
        )

    def test_add_multipinmap_plugin_leaflet_error(self):
        street = 'Hongkongstrasse 10'
        postal_code = '20457'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='leaflet',
           street=street,
           postal_code=postal_code,
           city=city
        )
        self.assertRaises(ValidationError, multipinmap_plugin.full_clean)

    def test_add_multipinmap_plugin_leaflet_error_two(self):
        street = 'Hongkongstrasse 10'
        postal_code = '20457'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='leaflet',
           mapbox_access_token='waddehaddedudeda',
           street=street,
           postal_code=postal_code,
           city=city
        )
        self.assertRaises(ValidationError, multipinmap_plugin.full_clean)

    def test_add_multipinmap_plugin_leaflet_error_three(self):
        street = 'Miaumiau 10'
        postal_code = '66666'
        city = 'Hamburg'
        multipinmap_plugin = api.add_plugin(
           self.placeholder,
           cms_plugins.MapPlugin,
           self.language,
           name='test',
           style='leaflet',
           mapbox_access_token='waddehaddedudeda',
           mapbox_map_id='waddehaddedudeda',
           street=street,
           postal_code=postal_code,
           city=city
        )
        self.assertRaises(ValidationError, multipinmap_plugin.full_clean)

    def test_render_page(self):
        self.test_add_multipinmap_plugin_google()
        api.publish_page(self.page, self.superuser, self.language)
        response = self.client.get(self.page.get_absolute_url())

        self.assertTrue("map" in response.rendered_content)
