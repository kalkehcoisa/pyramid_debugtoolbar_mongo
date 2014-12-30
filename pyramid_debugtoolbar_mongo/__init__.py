# coding=utf-8
from pyramid.settings import asbool

__author__ = 'gillesdevaux'


def includeme(config):
    stack_trace = asbool(config.registry.settings.get('debugtoolbarmongo.stacktrace', True))
    config.registry.settings['debugtoolbarmongo.stacktrace'] = stack_trace
