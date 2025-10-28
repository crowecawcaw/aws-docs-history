# Get a Secrets Manager secret value using Rust with client-side caching

When you retrieve a secret, you can use the Secrets Manager Rust-based caching component to cache it
for future use. Retrieving a cached secret is faster than retrieving it from Secrets Manager. Because
there is a cost for calling Secrets Manager APIs, using a cache can reduce your costs. For all of the ways you can
retrieve secrets, see [Get secrets](retrieving-secrets.md "retrieving-secrets.md").

The cache policy is First In First Out (FIFO), so when the cache must discard a secret, it discards the oldest secret. By default, the cache refreshes secrets every hour. You can configure the following:

- `max_size` – The maximum number of cached secrets to maintain before evicting secrets that have not been accessed recently.
- `ttl` – The duration a cached item is considered valid before requiring a refresh of the secret state.
  The cache implementation does not include cache invalidation. The cache implementation is focused around the cache itself, and is not security hardened or focused. If you require additional security such as encrypting items in the cache, use the traits provided to modify the cache.

To use the component, you must have a Rust 2021 development environment with `tokio`. For more information, see [Getting started](https://www.rust-lang.org/learn/get-started "https://www.rust-lang.org/learn/get-started") on the Rust Programming Language website.

To download the source code, see [Secrets Manager Rust-based caching client component](https://github.com/aws/aws-secretsmanager-agent/tree/main/aws_secretsmanager_caching "https://github.com/aws/aws-secretsmanager-agent/tree/main/aws_secretsmanager_caching") on GitHub.

To install the caching component, use the following command.

```
cargo add aws_secretsmanager_caching
```

**Required permissions:**

- `secretsmanager:DescribeSecret`
- `secretsmanager:GetSecretValue`
  For more information, see [Permissions reference](auth-and-access.md#reference_iam-permissions "auth-and-access.md#reference_iam-permissions").

###### Example Retrieve a secret

The following example shows how to get the secret value for a secret named
`MyTest`.

```
use aws_secretsmanager_caching::SecretsManagerCachingClient;
use std::num::NonZeroUsize;
use std::time::Duration;

let client = match SecretsManagerCachingClient::default(
    NonZeroUsize::new(10).unwrap(),
    Duration::from_secs(60),
)
.await
{
    Ok(c) => c,
    Err(_) => panic!("`Handle this error`"),
};

let secret_string = match client.get_secret_value("MyTest", None, None).await {
    Ok(s) => s.secret_string.unwrap(),
    Err(_) => panic!("`Handle this error`"),
};

// Your code here

```

###### Example Instantiating Cache with a custom configuration and a custom client

The following example shows how to configure the cache and then get the secret value for a secret named `MyTest`.

```
let config = aws_config::load_defaults(BehaviorVersion::latest())
    .await
    .into_builder()
    .region(Region::from_static("us-west-2"))
    .build();

let asm_builder = aws_sdk_secretsmanager::config::Builder::from(&config);

let client = match SecretsManagerCachingClient::from_builder(
    asm_builder,
    NonZeroUsize::new(10).unwrap(),
    Duration::from_secs(60),
)
.await
{
    Ok(c) => c,
    Err(_) => panic!("Handle this error"),
};

let secret_string = client
    .get_secret_value("MyTest", None, None)
    .await
    {
        Ok(c) => c.secret_string.unwrap(),
        Err(_) => panic!("Handle this error"),
    };

// Your code here
```

```

```
