# coding=utf-8
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''


setup(
    name='pyramid_debugtoolbar_mongo',
    version='0.1.1',
    packages=find_packages(),
    requires=[
        'pyramid_debugtoolbar (>=1.0.4)'
    ],
    url='https://github.com/gilles/pyramid_debugtoolbar_mongo',
    license='MIT',
    author='Gilles Devaux',
    author_email='gilles.devaux@gmail.com',
    description='Pyramid debugtoolbar extension for mongo',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Pyramid',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
