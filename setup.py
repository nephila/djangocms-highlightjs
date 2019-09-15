#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import djangocms_highlightjs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djangocms_highlightjs.__version__


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='djangocms-highlightjs',
    version=version,
    description='''highlight.js plugin for django CMS''',
    long_description=readme + '\n\n' + history,
    author='Iacopo Spalletti',
    author_email='i.spalletti@nephila.it',
    url='https://github.com/nephila/djangocms-highlightjs',
    packages=[
        str('djangocms_highlightjs'),
    ],
    include_package_data=True,
    install_requires=[
        'django-cms',
    ],
    license='BSD',
    zip_safe=False,
    keywords='djangocms-highlightjs',
    test_suite='cms_helper.run',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
