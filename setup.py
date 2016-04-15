# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open

version = '0.1'

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name="AIS.py",
    version=version,
    description=("Python interface for the Swisscom All-in Signing Service"),
    long_description=readme + '\n\n' + history,
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    author="Camptocamp SA",
    author_email="info@camptocamp.com",
    url="www.camptocamp.com",
    packages=['AIS'],
    install_requires=["requests >= 2.0"],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved',
        'License :: OSI Approved :: '
        'GNU Affero General Public License v3 or later (AGPLv3+)'
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)