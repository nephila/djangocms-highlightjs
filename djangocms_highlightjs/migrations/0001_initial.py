# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from djangocms_highlightjs.settings import HIGHLIGHT_THEMES


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', serialize=False, parent_link=True, on_delete=models.CASCADE)),
                ('body', models.TextField(verbose_name='Code')),
                ('filename', models.CharField(default='', verbose_name='Filename', max_length=100, blank=True)),
                ('theme', models.CharField(verbose_name='Rendering theme', max_length=100, choices=HIGHLIGHT_THEMES)),
            ],
            options={
                'verbose_name': 'Highligh.JS code',
                'verbose_name_plural': 'Highligh.JS code',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
