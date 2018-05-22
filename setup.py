#!/bin/env python

import os
import string

from setuptools import setup, find_packages


NAME = 'Noto Sans CJK'
LICENSE = 'SIL Open Font License (OFL)'

ENTRY_POINT_NAME = NAME.lower()
IDENTIFIER = ''.join(char for char in ENTRY_POINT_NAME
                     if char in string.ascii_lowercase + string.digits)
PACKAGE_NAME = 'rinoh-typeface-{}'.format(IDENTIFIER)
PACKAGE_DIR = PACKAGE_NAME.replace('-', '_')

SETUP_PATH = os.path.dirname(os.path.abspath(__file__))


setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    packages=find_packages(),
    package_data={PACKAGE_DIR: ['*.otf', '*.txt']},
    install_requires=['rinohtype'],
    entry_points={
        'rinoh.typefaces':
            ['{} = {}:typeface'.format(ENTRY_POINT_NAME, PACKAGE_DIR)]
    },

    author='kumanoko',
    author_email='noeleon930.hater.1@gmail.com',
    description='Noto Sans CJK typeface',
    long_description=open(os.path.join(SETUP_PATH, 'README.rst')).read(),
    url='https://github.com/kumanoko24/rinoh-typeface-notosanscjk',
    keywords='opentype font noto sans notosans rinohtype rino rinoh sphinx',
    license=LICENSE,
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Fonts',
    ]
)
