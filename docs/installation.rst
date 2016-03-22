============
Installation
============

* Install djangocms-redirect::

    pip install djangocms-redirect

* Add to INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        djangocms_redirect
        ...
    ]

* Add to MIDDLEWARE_CLASSES:

  If you intend to use ``process_request`` the add it near the top (after
  ``django.middleware.cache.UpdateCacheMiddleware``); if using ``process_response`` add at the
  bottom (before ``django.middleware.cache.FetchFromCacheMiddleware``)::

    MIDDLEWARE_CLASSES = [
        ...
        djangocms_redirect.middleware.RedirectMiddleware
        ...
    ]


* Choose if you want to process the redirect during the request (default) or response by setting:

    * ``DJANGOCMS_REDIRECT_USE_REQUEST = True``: during request
    * ``DJANGOCMS_REDIRECT_USE_REQUEST = False``: during response

* Migrate

    python manage.py migrate

The go to ``http://mysite.com/admin/djangocms_redirect/`` and create redirect instances.
