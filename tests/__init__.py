# -*- coding: utf-8 -*-
"""
Tests for `djangocms_highlightjs` module.
"""
from cms.utils import get_language_list
from django.http import SimpleCookie
from django.test import TestCase, RequestFactory
from django.utils.six import StringIO
from djangocms_helper.base_test import BaseTestCase


class BaseTest(BaseTestCase):
    """
    Base class with utility function
    """
    languages = get_language_list()

    def get_pages(self):
        from cms.api import create_page, create_title
        page = create_page(u'page one', 'page.html', language='en')
        page_2 = create_page(u'page two', 'page.html', language='en')
        create_title(language='fr', title=u'page un', page=page)
        create_title(language='it', title=u'pagina uno', page=page)
        for lang in self.languages:
            page.publish(lang)
        page_2.publish('en')
        return page.get_draft_object(), page_2.get_draft_object()
