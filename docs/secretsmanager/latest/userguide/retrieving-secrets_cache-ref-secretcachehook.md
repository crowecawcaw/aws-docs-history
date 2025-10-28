# SecretCacheHook

An interface to hook into a [SecretCache](retrieving-secrets_cache-ref-secretcache.md "retrieving-secrets_cache-ref-secretcache.md")
to perform actions on the secrets being stored in the cache.

###### These are the available methods:

- [put](#retrieving-secrets_cache-ref-secretcachehook_put "#retrieving-secrets_cache-ref-secretcachehook_put")
- [get](#retrieving-secrets_cache-ref-secretcachehook_get "#retrieving-secrets_cache-ref-secretcachehook_get")

## put

Prepares the object for storing in the cache.

Request syntax

```
response = hook.put(
    obj='`secret_object`'
)
```

Parameters

- `obj` (_object_) -- [Required]
  The secret or object that contains the secret.

Return type

object

## get

Derives the object from the cached object.

Request syntax

```
response = hook.get(
    obj='`secret_object`'
)
```

Parameters

- `obj` (_object_): [Required]
  The secret or object that contains the secret.

Return type

object
