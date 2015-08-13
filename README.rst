=====================
djangocms-highlightjs
=====================


.. image:: https://img.shields.io/pypi/v/djangocms-highlightjs.svg
        :target: https://pypi.python.org/pypi/djangocms-highlightjs
        :alt: Latest PyPI version

.. image:: https://img.shields.io/travis/nephila/djangocms-highlightjs.svg
        :target: https://travis-ci.org/nephila/djangocms-highlightjs
        :alt: Latest Travis CI build status

.. image:: https://img.shields.io/pypi/dm/djangocms-highlightjs.svg
        :target: https://pypi.python.org/pypi/djangocms-highlightjs
        :alt: Monthly downloads

.. image:: https://coveralls.io/repos/nephila/djangocms-highlightjs/badge.png
        :target: https://coveralls.io/r/nephila/djangocms-highlightjs
        :alt: Test coverage

highlight.js plugin for django CMS 3.0

Support Python version:

* Python 2.6
* Python 2.7
* Python 3.3
* Python 3.4

Supported Django versions:

* Django 1.6
* Django 1.7
* Django 1.8

Supported django CMS versions:

* django CMS 3.x

Documentation
-------------

The full documentation is at http://djangocms-highlightjs.rtfd.org.

Quickstart
----------

#. Install djangocms-highlightjs::

    pip install djangocms-highlightjs

#. Add to INSTALLED_APPS::

    'djangocms_highlightjs',

#. Update the database schema::

    $ python manage migrate djangocms_highlightjs

#. Add "**highlight.js code**" plugin to your placeholders

Features
--------

* Use `highlight.js`_ to do syntax highlighting on provided code


.. _highlight.js: http://highlightjs.org/

