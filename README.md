[![Build Status](https://travis-ci.org/creimers/cmsplugin_multipinmap.svg?branch=master)](https://travis-ci.org/creimers/cmsplugin_multipinmap)
[![Coverage Status](https://coveralls.io/repos/creimers/cmsplugin_multipinmap/badge.svg?branch=master)](https://coveralls.io/r/creimers/cmsplugin_multipinmap?branch=master)
# djangocms multi pin map plugin

A djangocms map plugin that can display multiple pins. Avaliable as google maps or [leaflet](http://leafletjs.com/) style.

## Installation

* ``pip install cmsplugin_multipinmap``

* Add

  ```
  'cmsplugin_multipinmap',
  ```

  to ``INSTALLED_APPS``.

* Sync the database

* For leaflet, [mapbox](https://www.mapbox.com/) is used as map provider. You can add ``MAPBOX_ACCESS_TOKEN`` and ``MAPBOX_MAP_ID`` default values to ``settings.py``.
