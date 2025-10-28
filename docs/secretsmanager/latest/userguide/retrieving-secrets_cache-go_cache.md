# type Cache

An in-memory cache for secrets requested from Secrets Manager. You use [GetSecretString](#retrieving-secrets_cache-go_cache_operations_GetCachedSecret "#retrieving-secrets_cache-go_cache_operations_GetCachedSecret")
or [GetSecretBinary](#retrieving-secrets_cache-go_cache_operations_GetSecretBinary "#retrieving-secrets_cache-go_cache_operations_GetSecretBinary")
to retrieve a secret from the cache.

The following example shows how to configure the cache settings.

```
// Create a custom secretsmanager client
client := getCustomClient()

// Create a custom CacheConfig struct
config := secretcache. CacheConfig{
    MaxCacheSize:  secretcache.DefaultMaxCacheSize + 10,
    VersionStage:  secretcache.DefaultVersionStage,
    CacheItemTTL:  secretcache.DefaultCacheItemTTL,
}

// Instantiate the cache
cache, _ := secretcache.New(
    func( c *secretcache.Cache) {  c. CacheConfig = config },
    func( c *secretcache.Cache) {  c. Client = client },
)
```

For more information, including examples, see [Get a Secrets Manager secret value using Go with client-side caching](retrieving-secrets_cache-go.md "retrieving-secrets_cache-go.md").

## Methods

### New

`func New(optFns ...func(*Cache)) (*Cache, error)`

New constructs a secret cache using functional options, uses defaults
otherwise. Initializes a SecretsManager Client from a new session. Initializes
CacheConfig to default values. Initialises LRU cache with a default max
size.

### GetSecretString

`func (c *Cache) GetSecretString(secretId string) (string, error)`

GetSecretString gets the secret string value from the cache for given secret
ID. Returns the secret string and an error if operation failed.

### GetSecretStringWithStage

`func (c *Cache) GetSecretStringWithStage(secretId string, versionStage string) (string, error)`

GetSecretStringWithStage gets the secret string value from the cache for given
secret ID and [version stage](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). Returns the secret string and an error if operation
failed.

### GetSecretBinary

`func (c *Cache) GetSecretBinary(secretId string) ([]byte, error) {`

GetSecretBinary gets the secret binary value from the cache for given secret
ID. Returns the secret binary and an error if operation failed.

### GetSecretBinaryWithStage

`func (c *Cache) GetSecretBinaryWithStage(secretId string, versionStage string) ([]byte, error)`

GetSecretBinaryWithStage gets the secret binary value from the cache for given
secret ID and [version stage](whats-in-a-secret.md#term_version "whats-in-a-secret.md#term_version"). Returns the
secret binary and an error if operation failed.
