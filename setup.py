#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import platform

deps = ['smtplib', 'random', 'email', 'yaml']

if platform.system().lower() == "windows":
    deps.append('pyreadline')
else:
    try:
        import readline
    except ImportError:
        deps.append('readline')

setup(
    name='minimal-secret-santa',
    version=0.1,
    url='https://github.com/mtribaldos/minimal-secret-santa',
    license='GPL-3+',
    author=u'Miguel Ángel Tribaldos',
    tests_require=[],
    install_requires = deps,
    scripts = ['minimal-secret-santa.py'],
    author_email='mtribaldos@gmail.com',
    description='Minimalistic Secret Santa or secret gift assignation',
    packages= find_packages(),
    include_package_data=False,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: Spanish',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment :: Fortune Cookies'
        ],
)