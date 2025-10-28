# SecretCacheConfiguration

Cache configuration options for a [SecretsManagerCache](retrieving-secrets_cache-net-SecretsManagerCache.md "retrieving-secrets_cache-net-SecretsManagerCache.md"), such as maximum cache
size and Time to Live (TTL) for cached secrets.

## Properties

### CacheItemTTL

`public uint CacheItemTTL { get; set; }`

The TTL of a cache item in milliseconds. The default is
`3600000` ms or 1 hour. The maximum is `4294967295` ms, which is approximately 49.7 days.

### MaxCacheSize

`public ushort MaxCacheSize { get; set; }`

The maximum cache size. The default is 1024 secrets. The maximum is 65,535.

### VersionStage

`public string VersionStage { get; set; }`

The version of secrets that you want to cache. For more information, see
[Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). The default is
`"AWSCURRENT"`.

### Client

`public IAmazonSecretsManager Client { get; set; }`

The [AmazonSecretsManagerClient](../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md "../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md") to retrieve secrets from. If it is
`null`, the cache instantiates a new client. The default is
`null`.

### CacheHook

`public ISecretCacheHook CacheHook { get; set; }`

A [ISecretCacheHook](retrieving-secrets_cache-net-ISecretCacheHook.md "retrieving-secrets_cache-net-ISecretCacheHook.md").
