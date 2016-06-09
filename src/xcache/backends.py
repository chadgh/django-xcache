"""
"""
from django.core.cache.backends import (
    db,
    dummy,
    filebased,
    locmem,
    memcached,
)
from django.core.cache.backends.base import DEFAULT_TIMEOUT


class XCacheMixin(object):
    """
    """

    @staticmethod
    def _get_backup_version(version):
        return '{}-backup'.format(version)

    def get(self, key, default=None, version=None, fallback=False):
        """
        """
        value = super(XCacheMixin, self).get(key, None, version)
        if fallback and value is None:
            value = super(XCacheMixin, self).get(
                key, default, self._get_backup_version(version))
        elif value is None:
            value = default
        return value

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        """
        """
        super(XCacheMixin, self).set(
            key, value, timeout=timeout, version=version)
        super(XCacheMixin, self).set(
            key, value, timeout=None, version=self._get_backup_version(version))


class FileBasedCache(XCacheMixin, filebased.FileBasedCache):
    pass


class DatabaseCache(XCacheMixin, db.DatabaseCache):
    pass


class DummyCache(XCacheMixin, dummy.DummyCache):
    pass


class LocMemCache(XCacheMixin, locmem.LocMemCache):
    pass


class MemcachedCache(XCacheMixin, memcached.MemcachedCache):
    pass


class PyLibMCCache(XCacheMixin, memcached.PyLibMCCache):
    pass
