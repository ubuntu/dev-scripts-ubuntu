#!/usr/bin/python3

from setuptools import setup

setup(name='ubuntu-scripts',
      version='0.1',
      description='A collection of useful scripts for Ubuntu developers',
      url='https://github.com/ubuntu/ubuntu-scripts',
      author='Iain Lane',
      author_email='iain.lane@canonical.com',
      license='gpl-3.0+',
      scripts=['make-sru-tasks'],
      install_requires=[
          'launchpadlib',
          'lazr.restfulclient'
      ],
      zip_safe=False)
