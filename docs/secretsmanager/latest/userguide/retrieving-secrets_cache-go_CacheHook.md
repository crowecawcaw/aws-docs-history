# type CacheHook

An interface to hook into a [Cache](retrieving-secrets_cache-go_cache.md "retrieving-secrets_cache-go_cache.md") to perform actions on the secret being stored in the
cache.

## Methods

### Put

`Put(data interface{}) interface{}`

Prepares the object for storing in the cache.

### Get

`Get(data interface{}) interface{}`

Derives the object from the cached object.
