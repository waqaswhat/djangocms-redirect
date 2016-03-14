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

Add to your MIDDLEWARE_CLASSES in your settings.py file this line:
'djangocms_redirect.middleware.RedirectMiddleware'.

