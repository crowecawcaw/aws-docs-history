# ISecretCacheHook

An interface to hook into a [SecretsManagerCache](retrieving-secrets_cache-net-SecretsManagerCache.md "retrieving-secrets_cache-net-SecretsManagerCache.md") to perform actions on
the secrets being stored in the cache.

## Methods

### Put

`object Put(object o);`

Prepare the object for storing in the cache.

Returns the object to store in the cache.

### Get

`object Get(object cachedObject);`

Derive the object from the cached object.

Returns the object to return from the cache
