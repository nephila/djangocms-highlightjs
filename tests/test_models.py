#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_djangocms_highlightjs
------------

Tests for `djangocms_highlightjs` modules module.
"""
from cms.views import details
from django.contrib.auth.models import AnonymousUser

from djangocms_highlightjs.models import HighlightText

from . import BaseTest


class TestHighlightjsModels(BaseTest):
    example_text = """
    def print_hello():
        print("hello world!")
    """

    def setUp(self):
        pass

    def test_add_plugin(self):
        from cms.api import add_plugin
        page_1, page_2 = self.get_pages()
        data = {
            'filename': 'test.py',
            'body': self.example_text,
            'theme': 'dark'
        }
        placeholder = page_1.placeholders.get(slot='content')
        add_plugin(placeholder, 'HighlightPlugin', 'en', **data)
        page_1.publish('en')

        # Get published page
        public = page_1.get_public_object()
        # plugin is the plugin instance we're going to render
        plugin = public.placeholders.get(slot='content').get_plugins_list()[0]

        request = self.get_page_request(public, AnonymousUser())
        response = details(request, '')
        self.assertContains(response, '<link rel="stylesheet" href="/static/djangocms_highlightjs/themes/dark.css">')
        self.assertContains(response, '''<pre id="highlight-%s" class="highlight-js">\n\t<strong>test.py</strong>\n\t<code>
    def print_hello():
        print("hello world!")
    </code>
</pre>''' % plugin.pk)
        self.assertContains(response, '<script src="/static/djangocms_highlightjs/js/highlight.pack.js"></script>')

    def test_model_save(self):

        plugin = HighlightText()
        plugin.body = self.example_text
        plugin.theme = "arta"
        plugin.save()

        self.assertEqual(self.example_text, plugin.body)

    def tearDown(self):
        pass