=====================
djangocms-highlightjs
=====================

|Gitter| |PyPiVersion| |PyVersion| |Status| |TestCoverage| |CodeClimate| |License|

highlight.js plugin for django CMS

Support Python version:

* Python 2.7, python 3.5+

Supported Django versions:

* Django 1.11, 2.0, 2.1, 2.2

Supported django CMS versions:

* django CMS 3.5+

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


.. |Gitter| image:: https://img.shields.io/badge/GITTER-join%20chat-brightgreen.svg?style=flat-square
    :target: https://gitter.im/nephila/applications
    :alt: Join the Gitter chat

.. |PyPiVersion| image:: https://img.shields.io/pypi/v/djangocms-highlightjs.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-highlightjs
    :alt: Latest PyPI version

.. |PyVersion| image:: https://img.shields.io/pypi/pyversions/djangocms-highlightjs.svg?style=flat-square
    :target: https://pypi.python.org/pypi/djangocms-highlightjs
    :alt: Python versions

.. |Status| image:: https://img.shields.io/travis/nephila/djangocms-highlightjs.svg?style=flat-square
    :target: https://travis-ci.org/nephila/djangocms-highlightjs
    :alt: Latest Travis CI build status

.. |TestCoverage| image:: https://img.shields.io/coveralls/nephila/djangocms-highlightjs/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/djangocms-highlightjs?branch=master
    :alt: Test coverage

.. |License| image:: https://img.shields.io/github/license/nephila/djangocms-highlightjs.svg?style=flat-square
   :target: https://pypi.python.org/pypi/djangocms-highlightjs/
    :alt: License

.. |CodeClimate| image:: https://codeclimate.com/github/nephila/djangocms-highlightjs/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/djangocms-highlightjs
   :alt: Code Climate
