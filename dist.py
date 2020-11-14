#!/usr/bin/env python

from mkp import dist
import versioneer

dist({
    'author': 'Thomas Reifenberger',
    'description': 'Monitor ink levels of printers via libinklevel',
    'download_url': 'https://github.com/tom-mi/check_mk-printer_inklevels',
    'name': 'printer_inklevels',
    'title': 'Printer Inklevels',
    'version': versioneer.get_version(),
    'version.min_required': '1.2.6p5',
})
