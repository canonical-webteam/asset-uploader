#! /usr/bin/env python3

# Core
import sys
from setuptools import setup

# The importer relies heavily on glob recursive search capability.
# This was only introduced in Python 3.5:
# https://docs.python.org/3.6/whatsnew/3.5.html#glob
assert sys.version_info >= (3, 5), (
    "upload-assets requires Python 3.5 or newer"
)

setup(
    name='canonicalwebteam.upload-assets',
    version='0.1.0',
    author='Canonical webteam',
    author_email='robin+pypi@canonical.com',
    url='https://github.com/canonical-webteam/upload-assets',
    packages=[
        'canonicalwebteam.upload_assets',
    ],
    description=(
        'A command-line tool for uploading assets to an assets server.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        'requests>=2.13.0'
    ],
    scripts=['upload-assets']
)