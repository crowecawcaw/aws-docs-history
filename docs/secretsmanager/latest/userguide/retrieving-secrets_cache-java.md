# Get a Secrets Manager secret value using Java with client-side caching

When you retrieve a secret, you can use the Secrets Manager Java-based caching component to cache it
for future use. Retrieving a cached secret is faster than retrieving it from Secrets Manager. Because
there is a cost for calling Secrets Manager APIs, using a cache can reduce your costs. For all of the ways you can
retrieve secrets, see [Get secrets](retrieving-secrets.md "retrieving-secrets.md").

The cache policy is Least Recently Used (LRU), so when the cache must discard a secret, it
discards the least recently used secret. By default, the cache refreshes secrets every hour. You can configure [how often the secret is refreshed](retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md#retrieving-secrets_cache-java-ref_SecretCacheConfiguration_methods-getCacheItemTTL "retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md#retrieving-secrets_cache-java-ref_SecretCacheConfiguration_methods-getCacheItemTTL") in the
cache, and you can [hook into the secret retrieval](retrieving-secrets_cache-java-ref_SecretCacheHook.md "retrieving-secrets_cache-java-ref_SecretCacheHook.md") to add more functionality.

The cache does not force garbage collection once cache references are freed. The
cache implementation does not include cache invalidation. The cache implementation
is focused around the cache itself, and is not security hardened or focused. If you require additional
security such as encrypting items in the cache, use the interfaces and abstract methods provided.

To use the component, you must have the following:

- A Java 8 or higher development environment. See [Java
  SE Downloads](https://www.oracle.com/technetwork/java/javase/downloads/index.html "https://www.oracle.com/technetwork/java/javase/downloads/index.html") on the Oracle website.
  To download the source code, see [Secrets Manager Java-based caching
  client component](https://github.com/aws/aws-secretsmanager-caching-java "https://github.com/aws/aws-secretsmanager-caching-java") on GitHub.

To add the component to your project, in your Maven pom.xml file, include the following
dependency. For more information about Maven, see the [Getting Started Guide](https://maven.apache.org/guides/getting-started/index.html "https://maven.apache.org/guides/getting-started/index.html") on the Apache Maven Project website.

```
<dependency>
  <groupId>com.amazonaws.secretsmanager</groupId>
  <artifactId>aws-secretsmanager-caching-java</artifactId>
  <version>1.0.2</version>
</dependency>
```

**Required permissions:**

- `secretsmanager:DescribeSecret`
- `secretsmanager:GetSecretValue`
  For more information, see [Permissions reference](auth-and-access.md#reference_iam-permissions "auth-and-access.md#reference_iam-permissions").

###### Reference

- [SecretCache](retrieving-secrets_cache-java-ref_SecretCache.md "retrieving-secrets_cache-java-ref_SecretCache.md")
- [SecretCacheConfiguration](retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md "retrieving-secrets_cache-java-ref_SecretCacheConfiguration.md")
- [SecretCacheHook](retrieving-secrets_cache-java-ref_SecretCacheHook.md "retrieving-secrets_cache-java-ref_SecretCacheHook.md")

###### Example Retrieve a secret

The following code example shows a Lambda function that retrieves a secret string. It
follows the [best
practice](../../../lambda/latest/dg/best-practices.md "../../../lambda/latest/dg/best-practices.md") of instantiating the cache outside of the function handler, so it
doesn't keep calling the API if you call the Lambda function again.

```
package com.amazonaws.secretsmanager.caching.examples;

    import com.amazonaws.services.lambda.runtime.Context;
    import com.amazonaws.services.lambda.runtime.RequestHandler;
    import com.amazonaws.services.lambda.runtime.LambdaLogger;

    import com.amazonaws.secretsmanager.caching.SecretCache;

    public class SampleClass implements RequestHandler<String, String> {

         private final SecretCache cache  = new SecretCache();

         @Override public String handleRequest(String secretId,  Context context) {
             final String secret  = cache.getSecretString(secretId);

            `// Use the secret, return success;`

        }
    }
```
