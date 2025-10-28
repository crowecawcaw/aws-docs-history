# SecretCache

An in-memory cache for secrets requested from Secrets Manager. You use [getSecretString](#retrieving-secrets_cache-java-ref_SecretCache-methods-getSecretString "#retrieving-secrets_cache-java-ref_SecretCache-methods-getSecretString") or
[getSecretBinary](#retrieving-secrets_cache-java-ref_SecretCache-methods-getSecretBinary "#retrieving-secrets_cache-java-ref_SecretCache-methods-getSecretBinary") to
retrieve a secret from the cache. You can configure the cache settings by passing in a
[SecretCacheConfiguration](retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md "retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md") object
in the constructor.

For more information, including examples, see [Get a Secrets Manager secret value using Java with client-side caching](retrieving-secrets_cache-java.md "retrieving-secrets_cache-java.md").

## Constructors

`public SecretCache()`

Default constructor for a `SecretCache` object.

`public SecretCache(AWSSecretsManagerClientBuilder
 builder)`

Constructs a new cache using a Secrets Manager client created using the provided
[`AWSSecretsManagerClientBuilder`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClientBuilder.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClientBuilder.md"). Use this
constructor to customize the Secrets Manager client, for example to use a specific
Region or endpoint.

`public SecretCache(AWSSecretsManager client)`

Constructs a new secret cache using the provided [`AWSSecretsManagerClient`](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerClient.md"). Use this
constructor to customize the Secrets Manager client, for example to use a specific
Region or endpoint.

`public SecretCache(SecretCacheConfiguration config)`

Constructs a new secret cache using the provided `SecretCacheConfiguration`.

## Methods

### getSecretString

`public String getSecretString(final String secretId)`

Retrieves a string secret from Secrets Manager. Returns a [`String`](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html?is-external=true "https://docs.oracle.com/javase/7/docs/api/java/lang/String.html?is-external=true").

### getSecretBinary

`public ByteBuffer getSecretBinary(final String secretId)`

Retrieves a binary secret from Secrets Manager. Returns a [`ByteBuffer`](https://docs.oracle.com/javase/7/docs/api/java/nio/ByteBuffer.html "https://docs.oracle.com/javase/7/docs/api/java/nio/ByteBuffer.html").

### refreshNow

`public boolean refreshNow(final String secretId) throws
 InterruptedException`

Forces the cache to refresh. Returns `true` if the refresh
completed without error, otherwise `false`.

### close

`public void close()`

Closes the cache.
