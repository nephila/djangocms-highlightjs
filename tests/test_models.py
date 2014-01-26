#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms_highlightjs
------------

Tests for `djangocms_highlightjs` modules module.
"""
from cms.views import details
from django.contrib.auth.models import AnonymousUser

from . import BaseTest


class TestHighlightjsModels(BaseTest):

    def setUp(self):
        pass

    def test_add_plugin(self):
        from cms.api import add_plugin
        page_1, page_2 = self.get_pages()
        data = {
            'filename': 'test.py',
            'body': 'print("Hello world!")',
            'theme': 'dark'
        }
        placeholder = page_1.placeholders.get(slot='placeholder')
        add_plugin(placeholder, 'HighlightPlugin', 'en', **data)
        page_1.publish('en')

        # Get published page
        public = page_1.get_public_object()
        # plugin is the plugin instance we're going to render
        plugin = public.placeholders.get(slot='placeholder').get_plugins_list()[0]

        request = self.get_page_request(public, AnonymousUser())
        response = details(request, '')

        self.assertContains(response, '<link rel="stylesheet" href="djangocms_highlightjs/themes/dark.css">')
        self.assertContains(response, '<pre id="highlight-%s" class="highlight-js"><strong>test.py</strong><code>print("Hello world!")</code></pre>' % plugin.pk)
        self.assertContains(response, '<script src="djangocms_highlightjs/js/highlight.pack.js"></script>')

    def tearDown(self):
        pass