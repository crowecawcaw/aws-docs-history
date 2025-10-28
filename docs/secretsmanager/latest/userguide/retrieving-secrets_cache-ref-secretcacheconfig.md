# SecretCacheConfig

Cache configuration options for a [SecretCache](retrieving-secrets_cache-ref-secretcache.md "retrieving-secrets_cache-ref-secretcache.md") such as max cache size and Time
to Live (TTL) for cached secrets.

###### Parameters

`max_cache_size` (_int_)

The maximum cache size. The default is `1024` secrets.

`exception_retry_delay_base` (_int_)

The number of seconds to wait after an exception is encountered before
retrying the request. The default is `1`.

`exception_retry_growth_factor`
(_int_)pur

The growth factor to use for calculating the wait time between retries of
failed requests. The default is `2`.

`exception_retry_delay_max` (_int_)

The maximum amount of time in seconds to wait between failed requests. The
default is `3600`.

`default_version_stage` (_str_)

The version of secrets that you want to cache. For more information, see
[Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). The default is
`'AWSCURRENT'`.

`secret_refresh_interval` (_int_)

The number of seconds to wait between refreshing cached secret
information. The default is `3600`.

`secret_cache_hook` (_SecretCacheHook_)

An implementation of the `SecretCacheHook` abstract class. The
default value is `None`.
