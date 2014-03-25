from setuptools import setup, find_packages
import sys, os


setup(name='ci',
      version='${version}',
      description="",
      long_description="",
      classifiers=[],
      keywords='',
      author='Flowerowl',
      author_email='lazynightz@gmail.com',
      url='lazynight.me',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      package_data = {'':['*.yaml']},
      zip_safe=False,
      install_requires=[
        'pyyaml',
        'bottle',
        'fabric',
      ],
      entry_points="",
      )
