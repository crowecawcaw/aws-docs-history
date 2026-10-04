

# Connect to a cache with a public endpoint
<a name="connecting-public-endpoint"></a>

All public endpoint connections require IAM authentication and TLS 1.3. There are three ways to generate the IAM authentication token:

1. **GLIDE client:** Handles token generation and refresh automatically. No authentication code required.

1. **Developer Toolkit for ElastiCache:** Generates the token for you. Use it with any Valkey or Redis OSS client library.

1. **Manual SigV4 signing:** Generate the token yourself using the AWS SDK.

**Topics**
+ [IAM policy for connecting](#connecting-public-endpoint-iam-policy)
+ [Option 1: GLIDE client with built-in IAM](#connecting-public-endpoint-glide)
+ [Option 2: Developer Toolkit for ElastiCache](#connecting-public-endpoint-toolkit)
+ [Option 3: Manual SigV4 signing](#connecting-public-endpoint-sigv4)
+ [Token and session expiration](#connecting-public-endpoint-behavior)
+ [Troubleshooting](#connecting-public-endpoint-troubleshooting)

## IAM policy for connecting
<a name="connecting-public-endpoint-iam-policy"></a>

Before you connect, your IAM user or role needs permission to call `elasticache:Connect`. The AWS managed policy `AdministratorAccess` includes this permission for all resources.

Create an IAM policy that allows the `elasticache:Connect` action on the ElastiCache cache and ElastiCache user:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "elasticache:Connect",
            "Resource": [
                "arn:aws:elasticache:us-east-1:123456789012:serverlesscache:my-public-cache",
                "arn:aws:elasticache:us-east-1:123456789012:user:default.iam-user"
            ]
        }
    ]
}
```

## Option 1: GLIDE client with built-in IAM
<a name="connecting-public-endpoint-glide"></a>

GLIDE 2.2 and later include built-in IAM authentication support. You configure your AWS credentials, and GLIDE handles token generation, caching, and refresh automatically. For installation instructions, see the [GLIDE documentation](https://glide.valkey.io) on the GLIDE website.

### Python
<a name="connecting-public-endpoint-glide-python"></a>

```
from glide import (
    GlideClusterClient, GlideClusterClientConfiguration, NodeAddress,
    ServerCredentials, IamAuthConfig, ServiceType,
)

config = GlideClusterClientConfiguration(
    addresses=[NodeAddress("my-public-cache-x2e9hv.public.serverless.use1.cache.amazonaws.com", 6379)],
    credentials=ServerCredentials(
        username="default.iam-user",
        iam_config=IamAuthConfig(
            cluster_name="my-public-cache",
            service=ServiceType.ELASTICACHE,
            region="us-east-1",
        ),
    ),
    use_tls=True,
)

client = await GlideClusterClient.create(config)
await client.set("key", "value")
result = await client.get("key")
print(result)  # b"value"
```

### Java
<a name="connecting-public-endpoint-glide-java"></a>

```
import glide.api.GlideClusterClient;
import glide.api.models.configuration.IamAuthConfig;
import glide.api.models.configuration.ServiceType;
import glide.api.models.configuration.ServerCredentials;
import glide.api.models.configuration.GlideClusterClientConfiguration;
import glide.api.models.configuration.NodeAddress;

import java.util.List;
import java.util.Collections;

List<NodeAddress> nodes = Collections.singletonList(
    NodeAddress.builder()
        .host("my-public-cache-x2e9hv.public.serverless.use1.cache.amazonaws.com")
        .port(6379)
        .build()
);

IamAuthConfig iamConfig = IamAuthConfig.builder()
    .clusterName("my-public-cache")
    .service(ServiceType.ELASTICACHE)
    .region("us-east-1")
    .build();

GlideClusterClientConfiguration config = GlideClusterClientConfiguration.builder()
    .addresses(nodes)
    .credentials(ServerCredentials.builder()
        .username("default.iam-user")
        .iamConfig(iamConfig)
        .build())
    .useTLS(true)
    .build();

GlideClusterClient client = GlideClusterClient.createClient(config).get();
client.set("key", "value").get();
String result = client.get("key").get();
System.out.println(result);  // "value"
```

## Option 2: Developer Toolkit for ElastiCache
<a name="connecting-public-endpoint-toolkit"></a>

The Developer Toolkit for ElastiCache (`developer-toolkit-elasticache`) is a standalone Python library and CLI that generates IAM authentication tokens. Use it with a Python Valkey or Redis OSS client library, such as valkey-py.

### Install
<a name="connecting-public-endpoint-toolkit-install"></a>

```
pip install developer-toolkit-elasticache
```

### Python with valkey-py
<a name="connecting-public-endpoint-toolkit-python"></a>

```
import valkey
from valkey.credentials import CredentialProvider

from developer_toolkit_elasticache import ElastiCacheIAMAuthTokenProvider

class ElastiCacheCredentialProvider(CredentialProvider):
    def __init__(self, auth):
        self._auth = auth

    def get_credentials(self):
        return self._auth.user_id, self._auth.get_token()

auth = ElastiCacheIAMAuthTokenProvider(
    serverless_cache_name="my-public-cache",
    user_id="default.iam-user",
    region="us-east-1",
)

client = valkey.ValkeyCluster(
    host="my-public-cache-x2e9hv.public.serverless.use1.cache.amazonaws.com",
    port=6379,
    ssl=True,
    credential_provider=ElastiCacheCredentialProvider(auth),
)

client.set("key", "value")
result = client.get("key")
print(result)  # b"value"
```

The Developer Toolkit does not automatically refresh tokens. IAM authentication tokens are valid for 15 minutes, so your application must generate a new token before the current token expires. The credentials provider in the preceding example calls `get_token()` for each new connection.

### CLI with the Developer Toolkit
<a name="connecting-public-endpoint-toolkit-cli"></a>

To connect with valkey-cli or redis-cli, use the Developer Toolkit CLI to generate a token:

```
export VALKEYCLI_AUTH=$(developer-toolkit-elasticache generate_iam_auth_token \
    --serverless-cache-name my-public-cache \
    --user-id default.iam-user \
    --region us-east-1)

valkey-cli -c -h my-public-cache-x2e9hv.public.serverless.use1.cache.amazonaws.com \
    -p 6379 \
    --tls \
    --user default.iam-user
```

`VALKEYCLI_AUTH` requires valkey-cli 9.0 or later. For redis-cli, use `REDISCLI_AUTH` instead of `VALKEYCLI_AUTH`.

For source code and additional examples, see the [Developer Toolkit for ElastiCache](https://github.com/aws/developer-toolkit-elasticache) repository on GitHub.

## Option 3: Manual SigV4 signing
<a name="connecting-public-endpoint-sigv4"></a>

Generate the IAM authentication token manually using the AWS SDK. For signing code examples, see [Connect with token as password](auth-iam.md#auth-iam-manual-sigv4).

## Token and session expiration
<a name="connecting-public-endpoint-behavior"></a>
+ **Token expiration:** IAM authentication tokens are valid for 15 minutes. GLIDE refreshes the token automatically. If you use the Developer Toolkit or manual signing, generate a new token for each new connection. Token expiration does not affect established connections. If you sign the token with temporary credentials, the token expires when those credentials expire, if that is sooner than 15 minutes.
+ **Session expiration:** Connections expire after 12 hours and reconnect automatically. Revoking an IAM principal's `elasticache:Connect` permission does not immediately disconnect active sessions. To disconnect a user immediately, remove the user from the cache's user group.

## Troubleshooting
<a name="connecting-public-endpoint-troubleshooting"></a>

The following table lists common connection errors, their causes, and how to resolve them.


| Error | Cause | Resolution | 
| --- | --- | --- | 
| WRONGPASS or authentication failure | Expired IAM token, incorrect username, missing IAM permissions, cache name not in lowercase, or expired temporary credentials | Verify that the token is fresh (less than 15 minutes old), the username matches a user in the cache's user group, the IAM principal has elasticache:Connect permission on both the cache ARN and the user ARN, the cache name in your token signing code is lowercase, and, if you signed the token with temporary credentials, that those credentials had not expired. | 
| NOAUTH Authentication required | The client sent a command before authenticating. A public endpoint connection must authenticate with AUTH or HELLO … AUTH as its first command. Some client libraries send a command such as CLIENT SETINFO or PING on connect, before credentials are applied. The connection is closed after repeated unauthenticated commands. | Configure your client so that authentication happens as part of connection setup — pass the token as the connection password or through a credential provider, rather than calling AUTH after connecting. GLIDE does this automatically. | 
| ERR service is not available | This error is returned for any new connection that fails before authentication completes. To avoid disclosing engine-internal state to an unauthenticated caller, ElastiCache reports this same generic message for several distinct underlying causes: IAM authentication is temporarily unavailable, you are being rate-limited due to IAM authentication throttling, or the engine is temporarily overloaded (BUSY, CLUSTERDOWN, or max clients reached). On an already-authenticated connection that re-runs AUTH or HELLO, ElastiCache returns a specific error instead, such as ERR IAM Authentication service is not available or ERR Exceeded limit of IAM Authentication requests. | If you have recently opened a high rate of new connections or re-authentications, reduce that rate and retry with exponential backoff. If your connection and re-authentication rate is normal, check the [AWS Health Dashboard](https://health.aws.amazon.com/) for ElastiCache service issues. | 
| Connection timeout | Network connectivity issue, incorrect endpoint, or TLS not enabled | Verify that the endpoint address is correct, TLS is enabled in your client configuration, and your network allows outbound connections to port 6379. | 
| TLS handshake failure | The client does not support TLS 1.3. Caches with a public endpoint require TLS 1.3. | Update your client or runtime to a version that supports TLS 1.3. | 