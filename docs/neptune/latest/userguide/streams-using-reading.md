

# Reading Neptune stream data
<a name="streams-using-reading"></a>

The following examples show how to read records from the property graph stream endpoint. You can use the AWS CLI, the AWS SDK for Python (Boto3), **awscurl**, or **curl**.

------
#### [ AWS CLI ]

```
aws neptunedata get-propertygraph-stream \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --iterator-type TRIM_HORIZON \
  --limit 10
```

To read from a specific position in the stream, use the `--commit-num` and `--iterator-type` parameters:

```
aws neptunedata get-propertygraph-stream \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --limit 10 \
  --commit-num 1 \
  --iterator-type AT_SEQUENCE_NUMBER
```

For more information, see [get-propertygraph-stream](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-propertygraph-stream.html) in the AWS CLI Command Reference.

------
#### [ SDK (Python) ]

```
import boto3
import json
from botocore.config import Config

client = boto3.client(
    'neptunedata',
    region_name='{{us-east-1}}',
    endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
    config=Config(read_timeout=65)
)

response = client.get_propertygraph_stream(
    limit=10,
    iteratorType='TRIM_HORIZON'
)

print(json.dumps(response['records'], indent=2, default=str))
```

To paginate through the stream, use the `commitNum` and `opNum` from the `lastEventId` in the response:

```
last_event = response['lastEventId']
next_response = client.get_propertygraph_stream(
    limit=10,
    commitNum=last_event['commitNum'],
    opNum=last_event['opNum'],
    iteratorType='AFTER_SEQUENCE_NUMBER'
)
```

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/propertygraph/stream?limit=10 \
  --region {{us-east-1}} \
  --service neptune-db
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

For more information about using **awscurl** with IAM authentication, see [Using `awscurl` with temporary credentials to securely connect to a DB cluster with IAM authentication enabled](iam-auth-connect-command-line.md#iam-auth-connect-awscurl).

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/propertygraph/stream?limit=10
```

**Note**  
Using **curl** without SigV4 signing only works if IAM authentication is disabled on your Neptune cluster. If IAM authentication is enabled, use **awscurl** or the AWS CLI instead.

------

For SPARQL graphs, replace `/propertygraph/stream` with `/sparql/stream` in the preceding examples. When using the AWS CLI or SDK, use `get-sparql-stream` or `client.get_sparql_stream()` instead.

## Viewing stream data in a graph notebook
<a name="streams-using-notebook"></a>

If you use [Neptune graph notebooks](graph-notebooks.md), the `%stream_viewer` line magic provides a visual interface for browsing stream records interactively without writing code. Run the following in a notebook cell:

```
%stream_viewer
```

You can optionally specify the query language and page size:

```
%stream_viewer sparql --limit 20
```

For more information, see [The `%stream_viewer` line magic](notebooks-magics.md#notebooks-line-magics-stream-viewer).

**Note**  
The `%stream_viewer` magic is fully supported only on engine versions 1.0.5.1 and earlier.