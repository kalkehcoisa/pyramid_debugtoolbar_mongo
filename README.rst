===================================
Pyramid Debug Toolbar MongoDB Panel
===================================


An extension panel for Pyramid Debug Toolbar that adds
MongoDB debugging information

This is a clone of https://github.com/hmarr/django-debug-toolbar-mongo
for the Pyramid Debug Toolbar (https://github.com/Pylons/pyramid_debugtoolbar)


Setup
=====
Add the following lines to your paster config file:

.. code-block:: ini

    pyramid.includes =
        ...
        pyramid_debugtoolbar
        pyramid_debugtoolbar_mongo
        ...

    debugtoolbar.panels =
        pyramid_debugtoolbar.panels.versions.VersionDebugPanel
        pyramid_debugtoolbar.panels.settings.SettingsDebugPanel
        pyramid_debugtoolbar.panels.headers.HeaderDebugPanel
        pyramid_debugtoolbar.panels.request_vars.RequestVarsDebugPanel
        pyramid_debugtoolbar.panels.renderings.RenderingsDebugPanel
        pyramid_debugtoolbar.panels.logger.LoggingPanel
        pyramid_debugtoolbar.panels.performance.PerformanceDebugPanel
        pyramid_debugtoolbar.panels.routes.RoutesDebugPanel
        pyramid_debugtoolbar.panels.sqla.SQLADebugPanel
        pyramid_debugtoolbar.panels.tweens.TweensDebugPanel
        pyramid_debugtoolbar.panels.introspection.IntrospectionDebugPanel
        pyramid_debugtoolbar_mongo.panels.mongo.MongoDebugPanel

An extra panel titled "MongoDB" should appear in your debug toolbar.

Obtaining stack traces can slow down queries significantly. To turn them off
add the following lines to your paster config file:

.. code-block:: python

    debugtoolbarmongo.stacktrace = false

TODO
====

* Nice layout
* Drop down for the stack trace
* Tests

Contributions welcome
