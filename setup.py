try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import cmsplugin_multipinmap

version = cmsplugin_multipinmap.__version__

setup(
    name='cmsplugin_multipinmap',
    packages=['cmsplugin_multipinmap'],
    include_package_data=True,
    version=version,
    description="A djangocms carousel slider plugin.",
    author='Christoph Reimers',
    author_email='christoph@superservice-international.com',
    license='MIT License',
    url='https://github.com/creimers/cmsplugin_multipinmap',
    keywords=['djangocms', 'django', 'map', 'plugin'],
    install_requires=[
        'geopy==1.11.0',
        'django-cms>=3.4',
    ],
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Framework :: Django',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
