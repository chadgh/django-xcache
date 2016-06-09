
django-xcache
=============

|build| | |docs|

This Django application can be used as a backend to the cache system that will
keep a backup of cached items even if the value has expired.

All core Django cache backends are provided with the addition of keeping a
backup of expired values.

This is for low-level caching interactions.

See the documentation_.

.. _documentation: https://django-xcache.readthedocs.io/

.. |docs| image:: https://readthedocs.org/projects/django-xcache/badge/?version=latest
    :target: http://django-xcache.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |build| image:: https://semaphoreci.com/api/v1/chadgh/django-xcache/branches/master/shields_badge.svg
    :target: https://semaphoreci.com/chadgh/django-xcache
    :alt: Build Status
