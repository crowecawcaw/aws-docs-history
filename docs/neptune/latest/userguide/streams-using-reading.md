

# Reading Neptune stream data

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

```python
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

```python
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
awscurl 'https://{{your-neptune-endpoint}}:{{port}}/propertygraph/stream?limit=10&iteratorType=TRIM_HORIZON' \
  --region {{us-east-1}} \
  --service neptune-db
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

------
#### [ curl ]

```
curl 'https://{{your-neptune-endpoint}}:{{port}}/propertygraph/stream?limit=10&iteratorType=TRIM_HORIZON'
```

To connect to a cluster that has IAM authentication enabled, each request must be signed. See [Connecting from the command line](iam-auth-connect-command-line.md).

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