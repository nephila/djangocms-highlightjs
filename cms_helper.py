#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals


def gettext(s): return s  # NOQA


HELPER_SETTINGS = dict(
    NOSE_ARGS=[
        '-s',
    ],
    INSTALLED_APPS=[],
    LANGUAGE_CODE='en',
    LANGUAGES=(
        ('en', gettext('English')),
        ('fr', gettext('French')),
        ('it', gettext('Italiano')),
    ),
    CMS_LANGUAGES={
        1: [
            {
                'code': 'en',
                'name': gettext('English'),
                'public': True,
            },
            {
                'code': 'it',
                'name': gettext('Italiano'),
                'public': True,
            },
            {
                'code': 'fr',
                'name': gettext('French'),
                'public': True,
            },
        ],
        'default': {
            'hide_untranslated': False,
        },
    },
)


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_highlightjs')

if __name__ == '__main__':
    run()
