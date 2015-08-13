# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__latest__'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighlightText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='cms.CMSPlugin', serialize=False, parent_link=True)),
                ('body', models.TextField(verbose_name='Code')),
                ('filename', models.CharField(default='', verbose_name='Filename', max_length=100, blank=True)),
                ('theme', models.CharField(verbose_name='Rendering theme', max_length=100, choices=[('arta', 'Arta'), ('ascetic', 'Ascetic'), ('atelier-dune.dark', 'Atelier Dune - Dark'), ('atelier-dune.light', 'Atelier Dune - Light'), ('atelier-forest.dark', 'Atelier forest - Dark'), ('atelier-forest.light', 'Atelier forest - Light'), ('atelier-heath.dark', 'Atelier heath - Dark'), ('atelier-heath.light', 'Atelier heath - Light'), ('atelier-lakeside.dark', 'Atelier lakeside - Dark'), ('atelier-lakeside.light', 'Atelier lakeside - Light'), ('atelier-seaside.dark', 'Atelier seaside - Dark'), ('atelier-seaside.light', 'Atelier seaside - Light'), ('brown_paper', 'Brown Paper'), ('dark', 'Dark'), ('default', 'Default'), ('docco', 'Docco'), ('far', 'Far'), ('foundation', 'Foundation'), ('github', 'Github'), ('googlecode', 'GoogleCode'), ('idea', 'IDEA'), ('ir_black', 'Ir black'), ('magula', 'Magula'), ('mono-blue', 'Mono Blue'), ('monokai', 'Monokai'), ('monokai_sublime', 'Monokai sublime'), ('obsidian', 'Obsidian'), ('paraiso.dark', 'Paraiso - Dark'), ('paraiso.light', 'éaraiso - Light'), ('pojoaque', 'Pojoaque'), ('railscasts', 'RailsCasts'), ('rainbow', 'Rainbow'), ('school_book', 'School Book'), ('solarized_dark', 'Solarized - Dark'), ('solarized_light', 'Solarized - Light'), ('sunburst', 'Sunburst'), ('tomorrow', 'Tomorrow'), ('tomorrow-night', 'Tomorrow night'), ('tomorrow-night-blue', 'Tomorrow night - Blug'), ('tomorrow-night-bright', 'Tomorrow night - Bright'), ('tomorrow-night-eighties', 'Tomorrow night - Eighties'), ('vs', 'VS'), ('xcode', 'XCode'), ('zenburn', 'Zenburn')])),
            ],
            options={
                'verbose_name': 'Highligh.JS code',
                'verbose_name_plural': 'Highligh.JS code',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
