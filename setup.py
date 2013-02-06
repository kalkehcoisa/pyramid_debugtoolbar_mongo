# coding=utf-8
from distutils.core import setup

setup(
    name='pyramid-debugtoolbar-mongo',
    version='0.1.0',
    packages=[
        'pyramid_debugtoolbar_mongo',
        'pyramid_debugtoolbar_mongo.panels'
    ],
    requires=[
        'pyramid-debugtoolbar (>=1.0.4)'
    ],
    url='https://github.com/gilles/pyramid_debugtoolbar_mongo',
    license='MIT',
    author='Gilles Devaux',
    author_email='gilles.devaux@gmail.com',
    description='Pyramid debugtoolbar extension for mongo',
    long_description=open('README.rst').read(),
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
