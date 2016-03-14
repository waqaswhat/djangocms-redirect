# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib.sites.models import Site
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

RESPONSE_CODES = (
    ('301', _('301 - Permanent redirection')),
    ('302', _('302- Temporary redirection'),),
    ('410',  ('410 - Permanently unavailable'),),
)


@python_2_unicode_compatible
class Redirect(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'))
    old_path = models.CharField(
        ('redirect from'),
        max_length=200,
        db_index=True,
        help_text=_("Select a Page or write an url")
    )
    new_path = models.CharField(
        ('redirect to'),
        max_length=200,
        blank=True,
        help_text=_("Select a Page or write an url")
    )
    response_code = models.CharField(
        _('response code'),
        max_length=3,
        choices=RESPONSE_CODES,
        default=RESPONSE_CODES[0][0],
        help_text=_("This is the http response code returned if a destination "
                    "is specified. If no destination is specified the response code will be 410."))

    class Meta:
        verbose_name = _('redirect')
        verbose_name_plural = _('redirects')
        db_table = 'django_redirect'
        unique_together = (('site', 'old_path'),)
        ordering = ('old_path',)

    def __str__(self):
        return "%s ---> %s" % (self.old_path, self.new_path)
