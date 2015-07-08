from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='Top25',
      version='0.0.1',
      description='Stemming and Word Indexing App',
      author='Christopher Walker',
      author_email='cnwalker@uchicago.edu',
      url='https://pypi.python.org/pypi',
      install_requires=packages,
)

