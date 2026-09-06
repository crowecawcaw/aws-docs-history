

# Using the HTTPS REST endpoint to connect to a Neptune DB instance
<a name="access-graph-gremlin-rest"></a>

Amazon Neptune provides an HTTPS endpoint for Gremlin queries. The REST interface is compatible with whatever Gremlin version your DB cluster is using (see the [engine release page](engine-releases.md) of the Neptune engine version you are running to determine which Gremlin release it supports).

**Note**  
As discussed in [Encrypting connections to your Amazon Neptune database with SSL/HTTPS](security-ssl.md), Neptune now requires that you connect using HTTPS instead of HTTP. In addition, Neptune does not currently support HTTP/2 for REST API requests. Clients must use HTTP/1.1 when connecting to endpoints.

The following instructions walk you through connecting to the Gremlin endpoint using the `curl` command and HTTPS. You must follow these instructions from an Amazon EC2 instance in the same virtual private cloud (VPC) as your Neptune DB instance.

The HTTPS endpoint for Gremlin queries to a Neptune DB instance is `https://{{your-neptune-endpoint}}:{{port}}/gremlin`.

**Note**  
For information about finding the hostname of your Neptune DB instance, see [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md).

## To connect to Neptune using the HTTP REST endpoint
<a name="access-graph-gremlin-rest-connect"></a>

The following examples show how to submit a Gremlin query to the REST endpoint. You can use the AWS SDK, the AWS CLI, or **curl**.

------
#### [ AWS CLI ]

```
aws neptunedata execute-gremlin-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --gremlin-query "g.V().limit(1)"
```

For more information, see [execute-gremlin-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/execute-gremlin-query.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.execute_gremlin_query(
    gremlinQuery='g.V().limit(1)',
    serializer='application/vnd.gremlin-v3.0+json;types=false'
)

print(json.dumps(response['result'], indent=2))
```

For AWS SDK examples in other languages like Java, .NET, and more, see [AWS SDK](access-graph-gremlin-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/gremlin \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -d '{"gremlin":"g.V().limit(1)"}'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

For more information about using **awscurl** with IAM authentication, see [Using `awscurl` with temporary credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl).

------
#### [ curl ]

The following example uses **curl** to submit a Gremlin query through HTTP **POST**. The query is submitted in JSON format in the body of the post as the `gremlin` property.

```
curl -X POST -d '{"gremlin":"g.V().limit(1)"}' https://{{your-neptune-endpoint}}:{{port}}/gremlin
```

Although HTTP **POST** requests are recommended for sending Gremlin queries, it is also possible to use HTTP **GET** requests:

```
curl -G "https://{{your-neptune-endpoint}}:{{port}}?gremlin=g.V().count()"
```

------

These examples return the first vertex in the graph by using the `g.V().limit(1)` traversal. You can query for something else by replacing it with another Gremlin traversal.

**Important**  
By default, the REST endpoint returns all results in a single JSON result set. If this result set is too large, an `OutOfMemoryError` exception can occur on the Neptune DB instance.  
You can avoid this by enabling chunked responses (results returned in a series of separate responses). See [Use optional HTTP trailing headers to enable multi-part Gremlin responses](access-graph-gremlin-rest-trailing-headers.md).

**Note**  
Neptune does not support the `bindings` property.