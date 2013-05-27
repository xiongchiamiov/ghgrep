#!/usr/bin/env python
import os
from distutils.core import setup

from ghgrep import VERSION

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
try:
   import pypandoc
   description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   description = ''

setup(
   name = 'ghgrep',
   version = VERSION,
   author = 'James Pearson',
   author_email = 'pearson@changedmy.name',
   packages = ['ghgrep'],
   scripts = ['bin/ghgrep'],
   url = 'https://github.com/xiongchiamiov/ghgrep',
   license = 'WTFPL',
   description = 'List all your Github repositories containing a filename matching a search pattern.',
   long_description = description,
   install_requires = [
      'docopt >= 0.6.1',
      'envoy >= 0.0.2',
      'github3.py >= 0.7, < 0.8',
   ],
)

