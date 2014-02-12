from setuptools import setup, find_packages
import sys, os


setup(name='ci',
      version='${version}',
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='jackyu',
      author_email='jackyu@sohu-inc.com',
      url='m.sohu.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data = {'':['*.yaml']},
      zip_safe=False,
      install_requires=[
        'pyyaml',
        'bottle',
        'fabric',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
