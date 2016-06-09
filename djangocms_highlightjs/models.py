# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .settings import HIGHLIGHT_THEMES
from .settings import HIGHLIGHT_LANGUAGES


class HighlightText(CMSPlugin):
    body = models.TextField(_('Code'))
    filename = models.CharField(_('Filename'), max_length=100, default='',
                                blank=True)
    theme = models.CharField(_('Rendering theme'), max_length=100,
                             choices=sorted(HIGHLIGHT_THEMES))
    code_language = models.CharField(_('Code Language'), max_length=100,
                                     default='', blank=True,
                                     choices=sorted(HIGHLIGHT_LANGUAGES))

    def save(self, no_signals=False, *args, **kwargs):
        self.body = self.body.replace("\r", "")
        super(HighlightText, self).save(no_signals, *args, **kwargs)

    class Meta:
        verbose_name = _('Highligh.JS code')
        verbose_name_plural = _('Highligh.JS code')
