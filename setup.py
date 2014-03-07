#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
NAME = 'aes_gcm'
DESCRIPTION = 'A Python implementation of the authenticated ' + \
              'encryption mode Galois/Counter Mode (GCM).'
PACKAGES = ['ase_gcm', ]

import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

if __name__ == '__main__':
    setup(
        name=NAME,
        long_description=read('README.md'),
        download_url='https://github.com/bozhu/AES-GCM-Python',
        platforms=['any'],
        package_dir={'': '.'},
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
    )
