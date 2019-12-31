========
Features
========

Supported languages
-------------------

* Apache
* Bash
* C#
* C++
* CSS
* CoffeeScript
* Diff
* HTML, XML
* HTTP
* Ini, TOML
* JSON
* Java
* JavaScript
* Makefile
* Markdown
* Nginx
* Objective-C
* PHP
* Perl
* Properties
* Python
* Ruby
* SQL
* Shell Session
* YAML

You can add more languages by compiling your own version of **highlight.js** at
http://highlightjs.org/download/ and put it in a ``static/djangocms_highlight/js``
directory in an application loaded **before** ``djangocms_highlight``.

Themes
------

All default **highlight.js** themes are provided. You can write your own,
put the relevant css file in ``static/djangocms_highlight/css`` directory in
any application, add ``HIGHLIGHT_THEME`` in the project settings and update
it to include your theme.
