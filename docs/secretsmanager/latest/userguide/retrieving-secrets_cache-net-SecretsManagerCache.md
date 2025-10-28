# SecretsManagerCache

An in-memory cache for secrets requested from Secrets Manager. You use [GetSecretString](#retrieving-secrets_cache-net-SecretsManagerCache-methods-GetSecretString "#retrieving-secrets_cache-net-SecretsManagerCache-methods-GetSecretString")
or [GetSecretBinary](#retrieving-secrets_cache-net-SecretsManagerCache-methods-GetSecretBinary "#retrieving-secrets_cache-net-SecretsManagerCache-methods-GetSecretBinary")
to retrieve a secret from the cache. You can configure the cache settings by passing in
a [SecretCacheConfiguration](retrieving-secrets_cache-net-SecretCacheConfiguration.md "retrieving-secrets_cache-net-SecretCacheConfiguration.md") object in the constructor.

For more information, including examples, see [Get a Secrets Manager secret value using .NET with client-side caching](retrieving-secrets_cache-net.md "retrieving-secrets_cache-net.md").

## Constructors

`public SecretsManagerCache()`
Default constructor for a `SecretsManagerCache` object.

`public SecretsManagerCache(IAmazonSecretsManager secretsManager)`
Constructs a new cache using a Secrets Manager client created using the provided [AmazonSecretsManagerClient](../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md "../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md"). Use this constructor to
customize the Secrets Manager client, for example to use a specific
region or endpoint.

###### Parameters

secretsManager

The [AmazonSecretsManagerClient](../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md "../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md") to retrieve secrets
from.

`public SecretsManagerCache(SecretCacheConfiguration config)`
Constructs a new secret cache using the provided [SecretCacheConfiguration](retrieving-secrets_cache-net-SecretCacheConfiguration.md "retrieving-secrets_cache-net-SecretCacheConfiguration.md").
Use this constructor to configure the cache, for example the number of
secrets to cache and how often it refreshes.

###### Parameters

config

A [SecretCacheConfiguration](retrieving-secrets_cache-net-SecretCacheConfiguration.md "retrieving-secrets_cache-net-SecretCacheConfiguration.md") that contains configuration information for the
cache.

`public SecretsManagerCache(IAmazonSecretsManager secretsManager, SecretCacheConfiguration config)`

Constructs a new cache using a Secrets Manager client created using
the provided [AmazonSecretsManagerClient](../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md "../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md") and a [SecretCacheConfiguration](retrieving-secrets_cache-net-SecretCacheConfiguration.md "retrieving-secrets_cache-net-SecretCacheConfiguration.md").
Use this constructor to customize the Secrets Manager client, for
example to use a specific region or endpoint as well as configure the
cache, for example the number of secrets to cache and how often it
refreshes.

###### Parameters

secretsManager

The [AmazonSecretsManagerClient](../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md "../../../sdkfornet/v3/apidocs/items/SecretsManager/TSecretsManagerClient.md") to retrieve secrets
from.

config

A [SecretCacheConfiguration](retrieving-secrets_cache-net-SecretCacheConfiguration.md "retrieving-secrets_cache-net-SecretCacheConfiguration.md") that contains configuration information for the
cache.

## Methods

### GetSecretString

`public async Task<String> GetSecretString(String
 secretId)`

Retrieves a string secret from Secrets Manager.

###### Parameters

secretId

The ARN or name of the secret to retrieve.

### GetSecretBinary

`public async Task<byte[]> GetSecretBinary(String secretId)`

Retrieves a binary secret from Secrets Manager.

###### Parameters

secretId

The ARN or name of the secret to retrieve.

### RefreshNowAsync

`public async Task<bool> RefreshNowAsync(String
 secretId)`

Requests the secret value from Secrets Manager and updates the cache with any
changes. If there is no existing cache entry, creates a new one. Returns
`true` if the refresh is successful.

###### Parameters

secretId

The ARN or name of the secret to retrieve.

### GetCachedSecret

`public SecretCacheItem GetCachedSecret(string
 secretId)`

Returns the cache entry for the specified secret if it exists in the
cache. Otherwise, retrieves the secret from Secrets Manager and creates a new
cache entry.

###### Parameters

secretId

The ARN or name of the secret to retrieve.
