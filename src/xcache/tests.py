from time import sleep

from django.core.cache import caches
from django.test import TestCase


class TestXCache(TestCase):

    """Tests"""

    def setUp(self):
        self.cache_names = ['default', 'locmem']

    def tearDown(self):
        pass

    def test_standard_usage(self):
        for cache_name in self.cache_names:
            cache = caches[cache_name]
            cache.set('key', 'value')
            self.assertEqual(cache.get('key'), 'value')

    def test_fallback(self):
        for cache_name in self.cache_names:
            cache = caches[cache_name]
            cache.set('key', 'value', 0)
            self.assertEqual(cache.get('key', 'def'), 'def')
            self.assertEqual(cache.get('key', 'def', fallback=True), 'value')
            cache.set('key', 'value', 1)
            sleep(2)
            self.assertEqual(cache.get('key', 'def'), 'def')
            self.assertEqual(cache.get('key', 'def', fallback=True), 'value')
