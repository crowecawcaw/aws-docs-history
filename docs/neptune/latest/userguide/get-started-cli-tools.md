

# Using command-line tools to access Amazon Neptune
<a name="get-started-cli-tools"></a>

You can use the AWS CLI, AWS SDKs, and HTTP tools such as `curl` and `awscurl` to submit queries to your Neptune DB cluster. The following sections show how to set up each tool and run basic Gremlin and openCypher queries.

## Using the AWS CLI
<a name="get-started-cli-tools-cli"></a>

The `aws neptunedata` commands let you run Gremlin and openCypher queries, check engine status, manage bulk loads, and more. For the full command reference, see [neptunedata](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/) in the AWS CLI Command Reference.

The following examples show how to run a basic query:

------
#### [ Gremlin ]

```
aws neptunedata execute-gremlin-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --region {{us-east-1}} \
  --gremlin-query "g.V().limit(1)"
```

For more information, see [execute-gremlin-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/execute-gremlin-query.html) in the AWS CLI Command Reference.

------
#### [ openCypher ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --region {{us-east-1}} \
  --open-cypher-query "MATCH (n) RETURN n LIMIT 1"
```

For more information, see [execute-open-cypher-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/execute-open-cypher-query.html) in the AWS CLI Command Reference.

------

## Using the AWS SDK
<a name="get-started-cli-tools-sdk"></a>

You can use the Neptune Data API through the AWS SDKs to run queries programmatically. The following Python examples show how to run a basic query:

------
#### [ Gremlin ]

```
import boto3
import json
from botocore.config import Config

# Disable the client-side read timeout and retries so that
# Neptune's server-side neptune_query_timeout controls query duration.
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

For AWS SDK examples in other languages, see [AWS SDK](access-graph-gremlin-sdk.md).

------
#### [ openCypher ]

```
import boto3
import json
from botocore.config import Config

# Disable the client-side read timeout and retries so that
# Neptune's server-side neptune_query_timeout controls query duration.
client = boto3.client(
    'neptunedata',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=None, retries={'total_max_attempts': 1})
)

response = client.execute_open_cypher_query(
    openCypherQuery='MATCH (n) RETURN n LIMIT 1'
)

print(json.dumps(response['results'], indent=2))
```

For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------

## Using `curl` and `awscurl`
<a name="get-started-cli-tools-curl"></a>

The [curl](https://curl.haxx.se/) command-line tool submits HTTP requests directly to the Neptune endpoints. If IAM authentication is enabled, use [awscurl](https://github.com/okigan/awscurl) or `curl` 7.75.0\+ with the `--aws-sigv4` option to sign requests. For more information, see [Using `awscurl` with temporary credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl).

### Setting up `curl` for HTTPS
<a name="get-started-cli-tools-curl-setup"></a>

To connect using HTTPS (as Neptune requires in most Regions), `curl` needs access to appropriate certificates. For information about how to obtain certificates and format them into a certificate authority (CA) store, see [SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html) in the `curl` documentation.

You can specify the location of this CA certificate store using the `CURL_CA_BUNDLE` environment variable. On Windows, `curl` automatically looks for it in a file named `curl-ca-bundle.crt`. It looks first in the same directory as `curl.exe` and then elsewhere on the path. For more information, see [SSL Certificate Verification](https://curl.haxx.se/docs/sslcerts.html).

As long as `curl` can locate the appropriate certificates, it handles HTTPS connections just like HTTP connections, without extra parameters. Examples in this documentation are based on that scenario.

For more information about the tool, see the [curl man page](https://curl.haxx.se/docs/manpage.html), and the book *[Everything curl](https://ec.haxx.se/)*.

### Query examples
<a name="get-started-cli-tools-curl-examples"></a>

The following examples show how to run a basic query using `curl` and `awscurl`:

------
#### [ Gremlin (awscurl) ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/gremlin \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -d '{"gremlin":"g.V().limit(1)"}'
```

------
#### [ Gremlin (curl) ]

```
curl -X POST \
  -d '{"gremlin":"g.V().limit(1)"}' \
  https://{{your-neptune-endpoint}}:{{port}}/gremlin
```

**Note**  
Plain `curl` works only when IAM authentication is not enabled on your cluster.

------
#### [ openCypher (awscurl) ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -d "query=MATCH (n) RETURN n LIMIT 1"
```

------
#### [ openCypher (curl) ]

```
curl -X POST \
  -d "query=MATCH (n) RETURN n LIMIT 1" \
  https://{{your-neptune-endpoint}}:{{port}}/openCypher
```

**Note**  
Plain `curl` works only when IAM authentication is not enabled on your cluster.

------

For more Gremlin HTTP examples, see [HTTPS REST](access-graph-gremlin-rest.md). For more openCypher HTTP examples, see [HTTPS endpoint](access-graph-opencypher-queries.md).