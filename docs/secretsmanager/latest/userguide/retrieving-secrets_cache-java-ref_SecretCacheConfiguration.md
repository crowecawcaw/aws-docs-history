# SecretCacheConfiguration

Cache configuration options for a [SecretCache](retrieving-secrets_cache-java-ref_SecretCache.md "retrieving-secrets_cache-java-ref_SecretCache.md"), such as max cache size
and Time to Live (TTL) for cached secrets.

## Constructor

`public SecretCacheConfiguration`

Default constructor for a `SecretCacheConfiguration` object.

## Methods

### getClient

`public AWSSecretsManager getClient()`

Returns the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md") that the cache retrieves
secrets from.

### setClient

`public void setClient(AWSSecretsManager client)`

Sets the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md") client that the cache
retrieves secrets from.

### getCacheHook

`public SecretCacheHook getCacheHook()`

Returns the [SecretCacheHook](retrieving-secrets_cache-java-ref_SecretCacheHook.md "retrieving-secrets_cache-java-ref_SecretCacheHook.md") interface used to hook cache updates.

### setCacheHook

`public void setCacheHook(SecretCacheHook cacheHook)`

Sets the [SecretCacheHook](retrieving-secrets_cache-java-ref_SecretCacheHook.md "retrieving-secrets_cache-java-ref_SecretCacheHook.md")
interface used to hook cache updates.

### getMaxCacheSize

`public int getMaxCacheSize()`

Returns the maximum cache size. The default is 1024 secrets.

### setMaxCacheSize

`public void setMaxCacheSize(int maxCacheSize)`

Sets the maximum cache size. The default is 1024 secrets.

### getCacheItemTTL

`public long getCacheItemTTL()`

Returns the TTL in milliseconds for the cached items. When a cached secret
exceeds this TTL, the cache retrieves a new copy of the secret from the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md"). The default is 1 hour in
milliseconds.

The cache refreshes the secret synchronously when the secret is requested
after the TTL. If the synchronous refresh fails, the cache returns the stale
secret.

### setCacheItemTTL

`public void setCacheItemTTL(long cacheItemTTL)`

Sets the TTL in milliseconds for the cached items. When a cached secret
exceeds this TTL, the cache retrieves a new copy of the secret from the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md"). The default is 1 hour in
milliseconds.

### getVersionStage

`public String getVersionStage()`

Returns the version of secrets that you want to cache. For more information,
see [Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). The default is`"AWSCURRENT"`.

### setVersionStage

`public void setVersionStage(String versionStage)`

Sets the version of secrets that you want to cache. For more information, see
[Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). The default is
`"AWSCURRENT"`.

### SecretCacheConfiguration withClient

`public SecretCacheConfiguration withClient(AWSSecretsManager
 client)`

Sets the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md") to retrieve secrets from.
Returns the updated `SecretCacheConfiguration` object with the new
setting.

### SecretCacheConfiguration withCacheHook

`public SecretCacheConfiguration withCacheHook(SecretCacheHook
 cacheHook)`

Sets the interface used to hook the in-memory cache. Returns the updated
`SecretCacheConfiguration` object with the new setting.

### SecretCacheConfiguration withMaxCacheSize

`public SecretCacheConfiguration withMaxCacheSize(int
 maxCacheSize)`

Sets the maximum cache size. Returns the updated
`SecretCacheConfiguration` object with the new setting.

### SecretCacheConfiguration withCacheItemTTL

`public SecretCacheConfiguration withCacheItemTTL(long
 cacheItemTTL)`

Sets the TTL in milliseconds for the cached items. When a cached secret
exceeds this TTL, the cache retrieves a new copy of the secret from the [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md"). The default is 1 hour in
milliseconds. Returns the updated `SecretCacheConfiguration` object
with the new setting.

### SecretCacheConfiguration withVersionStage

`public SecretCacheConfiguration withVersionStage(String
 versionStage)`

Sets the version of secrets that you want to cache. For more information, see
[Secret versions](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). Returns the updated
`SecretCacheConfiguration` object with the new setting.
