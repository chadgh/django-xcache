# Getting Started

## Installation

1. `pip install django-xcache`
2. Edit your `CACHES` configuration/settings to include a backend from
   `xcache`.  All of the Django cre caching backends are available. For
   example: 

```python 
CACHES = {
	'default': {
		'BACKEND': 'xcache.backends.FileBasedCache',
		'LOCATION': 'django-cache',
		},
}
```

## Usage

The caching backend should work as normal for all places that use caching in
Django. `xcache` is really meant for the scenario of wanting to update the
cache and still wanting access to the expired version of the cache so that if
something goes wrong with updating the cached value you can still use it.

### Scenario

```python
from django.core.cache import cache

def get_my_cached_value(key):
	cached_value = cache.get(key)
	if cached_value is None:
		# execute code to try to get the new value to cache and return
		# if this is a database call or a web service call you might find
		# you can't actually perform this task.
		try:
			new_value = get_the_new_value()
		except:
			# something went wrong, what are we going to do.
			new_value = cache.get(key, fallback=True)  # this is what xcache provides
			# now new_value is the expired value that was cached before.
		cache.set(key, new_value)
		cached_value = new_value
	return cached_value
```
