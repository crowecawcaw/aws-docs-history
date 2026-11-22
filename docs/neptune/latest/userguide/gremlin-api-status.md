

# Gremlin query status API

You can list all active Gremlin queries or get the status of a specific query. The underlying HTTP endpoint for both operations is `https://{{your-neptune-endpoint}}:{{port}}/gremlin/status`.

## Listing active Gremlin queries
<a name="gremlin-api-status-list"></a>

To list all active Gremlin queries, call the endpoint with no `queryId` parameter.

### Request parameters
<a name="gremlin-api-status-list-request"></a>
+ **includeWaiting** (*optional*)   –   Specifies whether the response includes waiting queries in addition to running queries. The default is `false`, so the `queries` list contains only running queries.

### Response syntax
<a name="gremlin-api-status-list-response"></a>

```
{
  "acceptedQueryCount": integer,
  "runningQueryCount": integer,
  "queries": [
    {
      "queryId": "guid",
      "queryEvalStats": {
        "waited": integer,
        "elapsed": integer,
        "cancelled": boolean
      },
      "queryString": "string"
    }
  ]
}
```
+ **acceptedQueryCount**   –   The number of queries that have been accepted but not yet completed, including queries in the queue.
+ **runningQueryCount**   –   The number of currently running Gremlin queries.
+ **queries**   –   A list of the current Gremlin queries.

### Example
<a name="gremlin-api-status-list-example"></a>

------
#### [ AWS CLI ]

```
aws neptunedata list-gremlin-queries \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
```

For more information, see [list-gremlin-queries](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/list-gremlin-queries.html) in the AWS CLI Command Reference.

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

response = client.list_gremlin_queries()

print(response)
```

For AWS SDK examples in other languages like Java, .NET, and more, see [AWS SDK](access-graph-gremlin-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status \
  --region {{us-east-1}} \
  --service neptune-db
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------

To include waiting queries, set `includeWaiting` to `true`, as shown in the following examples.

------
#### [ AWS CLI ]

```
aws neptunedata list-gremlin-queries \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --include-waiting
```

------
#### [ SDK ]

```python
response = client.list_gremlin_queries(
    includeWaiting=True
)
```

------
#### [ awscurl ]

```
awscurl "https://{{your-neptune-endpoint}}:{{port}}/gremlin/status?includeWaiting=true" \
  --region {{us-east-1}} \
  --service neptune-db
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------
#### [ curl ]

```
curl "https://{{your-neptune-endpoint}}:{{port}}/gremlin/status?includeWaiting=true"
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------

The following output shows a single running query.

```
{
  "acceptedQueryCount": 9,
  "runningQueryCount": 1,
  "queries": [
    {
      "queryId": "fb34cd3e-f37c-4d12-9cf2-03bb741bf54f",
      "queryEvalStats": {
        "waited": 0,
        "elapsed": 23,
        "cancelled": false
      },
      "queryString": "g.V().out().count()"
    }
  ]
}
```

## Getting the status of a specific Gremlin query
<a name="gremlin-api-status-get-single"></a>

To get the status of a specific Gremlin query, provide the `queryId` parameter.

### Request parameters
<a name="gremlin-api-status-get-request"></a>
+ **queryId** (*required*)   –   The ID of the Gremlin query. Neptune automatically assigns this ID value to each query, or you can assign your own ID (see [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md)).

### Response syntax
<a name="gremlin-api-status-get-response-syntax"></a>

```
{
  "queryId": "guid",
  "queryString": "string",
  "queryEvalStats": {
    "waited": integer,
    "elapsed": integer,
    "cancelled": boolean,
    "subqueries": document
  }
}
```
+ **queryId**   –   The ID of the query.
+ **queryString**   –   The submitted query. This is truncated to 1024 characters if it is longer than that.
+ **queryEvalStats**   –   Statistics for the query, including `waited` (wait time in milliseconds), `elapsed` (run time in milliseconds), `cancelled` (whether the query was cancelled), and `subqueries` (the number of subqueries).

### Example
<a name="gremlin-api-status-get-example"></a>

------
#### [ AWS CLI ]

```
aws neptunedata get-gremlin-query-status \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --query-id "fb34cd3e-f37c-4d12-9cf2-03bb741bf54f"
```

For more information, see [get-gremlin-query-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-gremlin-query-status.html) in the AWS CLI Command Reference.

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

response = client.get_gremlin_query_status(
    queryId='fb34cd3e-f37c-4d12-9cf2-03bb741bf54f'
)

print(response)
```

For AWS SDK examples in other languages like Java, .NET, and more, see [AWS SDK](access-graph-gremlin-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status/fb34cd3e-f37c-4d12-9cf2-03bb741bf54f \
  --region {{us-east-1}} \
  --service neptune-db
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/gremlin/status/fb34cd3e-f37c-4d12-9cf2-03bb741bf54f
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------

The following is an example response.

```
{
  "queryId": "fb34cd3e-f37c-4d12-9cf2-03bb741bf54f",
  "queryString": "g.V().out().count()",
  "queryEvalStats": {
    "waited": 0,
    "elapsed": 23,
    "cancelled": false
  }
}
```