# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import HighlightText


@plugin_pool.register_plugin
class HighlightPlugin(CMSPluginBase):
    name = _('highlight.js code')
    model = HighlightText
    render_template = 'djangocms_highlightjs/code.html'
    text_enabled = True
    allow_children = False
    fields = ['theme', 'code_language', 'filename', 'body']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'theme': 'djangocms_highlightjs/themes/%s.css' % instance.theme,
            'highlight': 'djangocms_highlightjs/js/highlight.pack.js'
        })
        return context
