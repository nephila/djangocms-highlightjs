# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from djangocms_highlightjs.settings import HIGHLIGHT_LANGUAGES


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_highlightjs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlighttext',
            name='code_language',
            field=models.CharField(default='', max_length=100,
                                   verbose_name='Code Language', blank=True,
                                   choices=HIGHLIGHT_LANGUAGES),
        ),
    ]
