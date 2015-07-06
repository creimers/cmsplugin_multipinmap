#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
gettext = lambda s: s

HELPER_SETTINGS = {
    'NOSE_ARGS': [
        '-s',
    ],
    'INSTALLED_APPS': [
        'cmsplugin_multipinmap',
    ],
    'LANGUAGE_CODE': 'en',
    'LANGUAGES': (
        ('en', gettext('en')),
    ),
    'CMS_LANGUAGES': {
        ## Customize this
        1: [
            {
                'redirect_on_fallback': True,
                'hide_untranslated': False,
                'name': gettext('en'),
                'code': 'en',
                'public': True,
            },
        ],
        'default': {
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    },
    'MIDDLEWARE_CLASSES': [
        'django.contrib.messages.middleware.MessageMiddleware',
    ],
    'TEMPLATE_CONTEXT_PROCESSORS': {
        'django.core.context_processors.static'
    },
}
