#!/usr/bin/python3

from setuptools import setup

setup(name='dev-scripts-ubuntu',
      version='0.1',
      description='A collection of useful scripts for Ubuntu developers',
      url='https://github.com/ubuntu/dev-scripts-ubuntu',
      author='Iain Lane',
      author_email='iain.lane@canonical.com',
      license='gpl-3.0+',
      scripts=['make-sru-tasks'],
      install_requires=[
          'keyring',
          'keyrings.alt',
          'launchpadlib',
          'lazr.restfulclient'
      ],
      zip_safe=False)
