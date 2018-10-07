# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.core.cache import cache
from djangocms_helper.base_test import BaseTestCase


class BaseRedirectTest(BaseTestCase):

    def setUp(self):
        super(BaseRedirectTest, self).setUp()
        cache.clear()
