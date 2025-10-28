# SecretCacheHook

An interface to hook into a [SecretCache](retrieving-secrets_cache-java-ref_SecretCache.md "retrieving-secrets_cache-java-ref_SecretCache.md") to perform actions on the secrets being stored in
the cache.

## put

`Object put(final Object o)`

Prepare the object for storing in the cache.

Returns the object to store in the cache.

## get

`Object get(final Object cachedObject)`

Derive the object from the cached object.

Returns the object to return from the cache
