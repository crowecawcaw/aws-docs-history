

# Best practices for using the AWS CLI and SDKs with Neptune
<a name="best-practices-cli-sdk"></a>

By default, the AWS CLI and AWS SDKs time out after 60 seconds and automatically retry failed requests. For queries that take longer than 60 seconds to complete, this default behavior causes duplicate query execution. The retry fires a new request while the original query is still running on the server.

**Important**  
When you run long-running queries through the Neptune dataplane API (for example, `execute-open-cypher-query`), disable automatic retries. Also increase or remove the read timeout. Otherwise, the client retries the query while the original is still executing, which doubles the load on your Neptune cluster.

The following recommendations apply to any Neptune dataplane operation that can run longer than the default 60-second timeout:
+ Set the read timeout to 0 (infinite) or a value larger than your longest expected query duration.
+ Set the total maximum attempts to 1 (one attempt, zero retries). This prevents the client from retrying a request that the server is still processing.

The following examples show how to configure these settings for the AWS CLI and popular SDKs.

------
#### [ AWS CLI ]

```
export AWS_MAX_ATTEMPTS=1
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-cluster-endpoint}}:{{port}} \
  --open-cypher-query "RETURN 1" \
  --cli-read-timeout 0
```

The `--cli-read-timeout 0` parameter disables the read timeout, allowing the AWS CLI to wait indefinitely for a response. The `AWS_MAX_ATTEMPTS=1` environment variable sets the total maximum attempts to 1, meaning the request is tried exactly once with no retries.

------
#### [ Python (boto3) ]

```
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-cluster-endpoint}}:{{port}}',
    region_name='{{us-east-1}}',
    config=Config(
        retries={'total_max_attempts': 1, 'mode': 'standard'},
        read_timeout=None
    )
)
```

Setting `read_timeout=None` disables the read timeout. Setting `total_max_attempts` to `1` means the request is tried exactly once with no retries.

------
#### [ Java V2 SDK ]

```
import software.amazon.awssdk.services.neptunedata.NeptunedataClient;
import software.amazon.awssdk.core.client.config.ClientOverrideConfiguration;
import software.amazon.awssdk.core.retry.RetryPolicy;
import software.amazon.awssdk.regions.Region;
import java.time.Duration;
import java.net.URI;

// Build the Neptune dataplane client with no retries and infinite timeout
NeptunedataClient neptunedataClient = NeptunedataClient.builder()
    .endpointOverride(URI.create("https://{{your-cluster-endpoint}}:{{port}}"))
    .region(Region.of("{{us-east-1}}"))
    .overrideConfiguration(ClientOverrideConfiguration.builder()
        .apiCallTimeout(Duration.ZERO)
        .retryPolicy(RetryPolicy.none())
        .build())
    .build();
```

Setting `apiCallTimeout` to `Duration.ZERO` configures an infinite timeout for the API call. Using `RetryPolicy.none()` disables all automatic retries.

------