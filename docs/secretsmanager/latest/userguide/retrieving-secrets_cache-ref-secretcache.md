# SecretCache

An in-memory cache for secrets retrieved from Secrets Manager. You use [get_secret_string](#retrieving-secrets_cache-ref-secretcache_get_secret_string "#retrieving-secrets_cache-ref-secretcache_get_secret_string") or [get_secret_binary](#retrieving-secrets_cache-ref-secretcache_get_secret_binary "#retrieving-secrets_cache-ref-secretcache_get_secret_binary") to retrieve a
secret from the cache. You can configure the cache settings by passing in a [SecretCacheConfig](retrieving-secrets_cache-ref-secretcacheconfig.md "retrieving-secrets_cache-ref-secretcacheconfig.md") object in the
constructor.

For more information, including examples, see [Get a Secrets Manager secret value using Python with client-side caching](retrieving-secrets_cache-python.md "retrieving-secrets_cache-python.md").

```
cache = SecretCache(
    config = SecretCacheConfig,
    client = client
)
```

###### These are the available methods:

- [get_secret_string](#retrieving-secrets_cache-ref-secretcache_get_secret_string "#retrieving-secrets_cache-ref-secretcache_get_secret_string")
- [get_secret_binary](#retrieving-secrets_cache-ref-secretcache_get_secret_binary "#retrieving-secrets_cache-ref-secretcache_get_secret_binary")

## get_secret_string

Retrieves the secret string value.

Request syntax

```
response = cache.get_secret_string(
    secret_id='`string`',
    version_stage='`string`' )
```

Parameters

- `secret_id` (_string_):
  [Required] The name or ARN of the secret.
- `version_stage` (_string_):
  The version of secrets that you want to retrieve. For more
  information, see [secret versions](whats-in-a-secret.md "whats-in-a-secret.md"). The default is 'AWSCURRENT'.

Return type

string

## get_secret_binary

Retrieves the secret binary value.

Request syntax

```
response = cache.get_secret_binary(
    secret_id='`string`',
    version_stage='`string`'
)
```

Parameters

- `secret_id` (_string_):
  [Required] The name or ARN of the secret.
- `version_stage` (_string_):
  The version of secrets that you want to retrieve. For more
  information, see [secret versions](whats-in-a-secret.md "whats-in-a-secret.md"). The default is 'AWSCURRENT'.

Return type

[base64-encoded](https://tools.ietf.org/html/rfc4648#section-4 "https://tools.ietf.org/html/rfc4648#section-4") string
