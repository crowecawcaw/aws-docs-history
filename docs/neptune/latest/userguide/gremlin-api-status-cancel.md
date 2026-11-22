

# Gremlin query cancellation

To get the status of Gremlin queries, use HTTP `GET` or `POST` to make a request to the `https://{{your-neptune-endpoint}}:{{port}}/gremlin/status` endpoint.

## Gremlin query cancellation request parameters
<a name="gremlin-api-status-cancel-request"></a>
+ **cancelQuery**   –   Required for cancellation. This parameter has no corresponding value.
+ **queryId**   –   The ID of the running Gremlin query to cancel.

**Note**  
To find the ID of a running query, list the active queries as described in [Listing active Gremlin queries](gremlin-api-status.md#gremlin-api-status-list).

## Gremlin query cancellation example
<a name="gremlin-api-status-cancel-example"></a>

The following is an example of cancelling a query.

------
#### [ AWS CLI ]

```
aws neptunedata cancel-gremlin-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --query-id "fb34cd3e-f37c-4d12-9cf2-03bb741bf54f"
```

For more information, see [cancel-gremlin-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-gremlin-query.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```python
import boto3
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.cancel_gremlin_query(
    queryId='fb34cd3e-f37c-4d12-9cf2-03bb741bf54f'
)

print(response)
```

For AWS SDK examples in other languages like Java, .NET, and more, see [AWS SDK](access-graph-gremlin-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "cancelQuery&queryId=fb34cd3e-f37c-4d12-9cf2-03bb741bf54f"
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status \
  --data-urlencode "cancelQuery" \
  --data-urlencode "queryId=fb34cd3e-f37c-4d12-9cf2-03bb741bf54f"
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------

Successful cancellation returns HTTP `200` OK.