# coding: utf-8
#!/usr/bin/env python

from setuptools import setup, find_packages

readme = open('README').read()

setup(
    name='ci',
    version='${version}',
    description='',
    long_description=readme,
    author='jackyu',
    author_email='jackyu@sohu-inc.com',
    url='http://m.sohu.com',
    packages=find_packages(exclude=['*.pyc']),
    include_package_data = True,
    package_data = {
    },
    install_requires=[
        'essay>=2.9.1.1',
        'bottle',
        'yaml'
        ],
    entry_points={
    },
)
