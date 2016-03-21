============
Installation
============

At the command line::

    $ easy_install djangocms-redirect

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv djangocms-redirect
    $ pip install djangocms-redirect


Configuration and setup
=======================
Configuring django-cms redirect is extremely easy:

* Add 'djangocms_redirect.middleware.RedirectMiddleware' to your MIDDLEWARE_CLASSES in your settings.py file

* Add 'djangocms_redirect' to your INSTALLED_APPS in your settings.py file.

* Choose if you want to process the redirect during the request (default) or response by setting:

    * ``DJANGOCMS_REDIRECT_USE_REQUEST = True``: during request
    * ``DJANGOCMS_REDIRECT_USE_REQUEST = False``: during response
