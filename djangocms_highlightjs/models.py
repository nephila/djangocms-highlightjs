# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models

from .settings import HIGHLIGHT_THEME


class HighlightText(CMSPlugin):
    body = models.TextField(_('Code'))
    filename = models.CharField(_('Filename'), max_length=100, default='',
                                blank=True)
    theme = models.CharField(_(u'Rendering theme'), max_length=100,
                             choices=sorted(HIGHLIGHT_THEME.items()))

    def save(self, no_signals=False, *args, **kwargs):
        self.body = self.body.replace("\r", "").strip()
        super(HighlightText, self).save(no_signals, *args, **kwargs)

    class Meta:
        verbose_name = _('Highligh.JS code')
        verbose_name_plural = _('Highligh.JS code')