# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _

from .models import HighlightText


class HighlightPlugin(CMSPluginBase):
    name = _(u"highlight.js code")
    model = HighlightText
    render_template = "djangocms_highlightjs/code.html"
    text_enabled = True
    allow_children = False
    fields = ['theme', 'filename', 'body']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'theme': 'djangocms_highlightjs/themes/%s.css' % instance.theme,
            'highlight': 'djangocms_highlightjs/js/highlight.pack.js'
        })
        return context

    def icon_src(self, instance):
        return static('djangocms_highlightjs/img/icon.png')
plugin_pool.register_plugin(HighlightPlugin)
