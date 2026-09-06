

# Neptune openCypher status servlet and status endpoint
<a name="access-graph-opencypher-status"></a>

The openCypher status endpoint provides access to information about queries that are currently running on the server or waiting to run. It also lets you cancel those queries. The endpoint is:

```
https://{{(the server)}}:{{(the port number)}}/openCypher/status
```

You can use the HTTP `GET` and `POST` methods to get current status from the server, or to cancel a query. You can also use the `DELETE` method to cancel a running or waiting query.

## Parameters for status requests
<a name="access-graph-opencypher-status-parameters"></a>

**Status query parameters**
+ **`includeWaiting`** (`true` or `false`)   –   When set to `true` and other parameters are not present, causes status information for waiting queries to be returned as well as for running queries.
+ **`cancelQuery`**   –   Used only with `GET` and `POST` methods, to indicate that this is a cancelation request. The `DELETE` method does not need this parameter.

  The value of the `cancelQuery` parameter is not used, but when `cancelQuery` is present, the `queryId` parameter is required, to identify which query to cancel.
+ **`queryId`**   –   Contains the ID of a specific query.

  When used with the `GET` or `POST` method and the `cancelQuery` parameter is not present, `queryId` causes status information to be returned for the specific query it identifies. If the `cancelQuery` parameter is present, then the specific query that `queryId` identifies is canceled.

  When used with the `DELETE` method, `queryId` always indicates a specific query to be canceled.
+ **`silent`**   –   Only used when canceling a query. If set to `true`, causes the cancelation to happen silently.

## Status request response fields
<a name="access-graph-opencypher-status-response-fields"></a>

**Status response fields if the ID of a specific query is not provided**
+ **acceptedQueryCount**   –   The number of queries that have been accepted but not yet completed, including queries in the queue.
+ **runningQueryCount**   –   The number of currently running openCypher queries.
+ **queries**   –   A list of the current openCypher queries.

**Status response fields for a specific query**
+ **queryId**   –   A GUID id for the query. Neptune automatically assigns this ID value to each query, or you can also assign your own ID (see [Inject a Custom ID Into a Neptune Gremlin or SPARQL Query](features-query-id.md)).
+ **queryString**   –   The submitted query. This is truncated to 1024 characters if it is longer than that.
+ **queryEvalStats**   –   Statistics for this query:
  + **waited**   –   Indicates how long the query waited, in milliseconds.
  + **elapsed**   –   The number of milliseconds the query has been running so far.
  + **cancelled**   –   `True` indicates that the query was cancelled, or `False` that it has not been cancelled.

## Examples of status requests and responses
<a name="access-graph-opencypher-status-samples"></a>
+ **Request for the status of all queries, including those waiting:**

------
#### [ AWS CLI ]

  ```
  aws neptunedata get-open-cypher-query-status \
    --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
    --include-waiting
  ```

  For more information, see [get-open-cypher-query-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-open-cypher-query-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

  ```
  import boto3
  from botocore.config import Config
  
  client = boto3.client(
      'neptunedata',
      endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
      config=Config(read_timeout=None, retries={'total_max_attempts': 1})
  )
  
  response = client.get_open_cypher_query_status(
      includeWaiting=True
  )
  
  print(response)
  ```

  For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

  ```
  awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --region {{us-east-1}} \
    --service neptune-db \
    -X POST \
    -d "includeWaiting=true"
  ```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

  ```
  curl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --data-urlencode "includeWaiting=true"
  ```

------

  *Response:*

  ```
  {
    "acceptedQueryCount" : 0,
    "runningQueryCount" : 0,
    "queries" : [ ]
  }
  ```
+ **Request for the status of running queries, **not** including those waiting:**:

------
#### [ AWS CLI ]

  ```
  aws neptunedata get-open-cypher-query-status \
    --endpoint-url https://{{your-neptune-endpoint}}:{{port}}
  ```

  For more information, see [get-open-cypher-query-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-open-cypher-query-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

  ```
  import boto3
  from botocore.config import Config
  
  client = boto3.client(
      'neptunedata',
      endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
      config=Config(read_timeout=None, retries={'total_max_attempts': 1})
  )
  
  response = client.get_open_cypher_query_status()
  
  print(response)
  ```

  For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

  ```
  awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --region {{us-east-1}} \
    --service neptune-db
  ```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

  ```
  curl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status
  ```

------

  *Response:*

  ```
  {
    "acceptedQueryCount" : 0,
    "runningQueryCount" : 0,
    "queries" : [ ]
  }
  ```
+ **Request for the status of a single query:**

------
#### [ AWS CLI ]

  ```
  aws neptunedata get-open-cypher-query-status \
    --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
    --query-id {{eadc6eea-698b-4a2f-8554-5270ab17ebee}}
  ```

  For more information, see [get-open-cypher-query-status](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/get-open-cypher-query-status.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

  ```
  import boto3
  from botocore.config import Config
  
  client = boto3.client(
      'neptunedata',
      endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
      config=Config(read_timeout=None, retries={'total_max_attempts': 1})
  )
  
  response = client.get_open_cypher_query_status(
      queryId='{{eadc6eea-698b-4a2f-8554-5270ab17ebee}}'
  )
  
  print(response)
  ```

  For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

  ```
  awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --region {{us-east-1}} \
    --service neptune-db \
    -X POST \
    -d "queryId={{eadc6eea-698b-4a2f-8554-5270ab17ebee}}"
  ```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

  ```
  curl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --data-urlencode "queryId={{eadc6eea-698b-4a2f-8554-5270ab17ebee}}"
  ```

------

  *Response:*

  ```
  {
    "queryId" : "eadc6eea-698b-4a2f-8554-5270ab17ebee",
    "queryString" : "MATCH (n1)-[:knows]->(n2), (n2)-[:knows]->(n3), (n3)-[:knows]->(n4), (n4)-[:knows]->(n5), (n5)-[:knows]->(n6), (n6)-[:knows]->(n7), (n7)-[:knows]->(n8), (n8)-[:knows]->(n9), (n9)-[:knows]->(n10) RETURN COUNT(n1);",
    "queryEvalStats" : {
      "waited" : 0,
      "elapsed" : 23463,
      "cancelled" : false
    }
  }
  ```
+ **Requests to cancel a query**

------
#### [ AWS CLI ]

  ```
  aws neptunedata cancel-open-cypher-query \
    --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
    --query-id {{f43ce17b-db01-4d37-a074-c76d1c26d7a9}}
  ```

  For more information, see [cancel-open-cypher-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/cancel-open-cypher-query.html) in the AWS CLI Command Reference.

------
#### [ SDK ]

  ```
  import boto3
  from botocore.config import Config
  
  client = boto3.client(
      'neptunedata',
      endpoint_url='https://{{your-neptune-endpoint}}:{{port}}',
      config=Config(read_timeout=None, retries={'total_max_attempts': 1})
  )
  
  response = client.cancel_open_cypher_query(
      queryId='{{f43ce17b-db01-4d37-a074-c76d1c26d7a9}}'
  )
  
  print(response)
  ```

  For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

  ```
  awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --region {{us-east-1}} \
    --service neptune-db \
    -X POST \
    -d "cancelQuery" \
    -d "queryId={{f43ce17b-db01-4d37-a074-c76d1c26d7a9}}"
  ```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

  1. Using `POST`:

  ```
  curl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --data-urlencode "cancelQuery" \
    --data-urlencode "queryId={{f43ce17b-db01-4d37-a074-c76d1c26d7a9}}"
  ```

  2. Using `GET`:

  ```
  curl -X GET https://{{your-neptune-endpoint}}:{{port}}/openCypher/status \
    --data-urlencode "cancelQuery" \
    --data-urlencode "queryId={{588af350-cfde-4222-bee6-b9cedc87180d}}"
  ```

  3. Using `DELETE`:

  ```
  curl -X DELETE \
    "https://{{your-neptune-endpoint}}:{{port}}/openCypher/status?queryId={{b9a516d1-d25c-4301-bb80-10b2743ecf0e}}"
  ```

------

  *Response:*

  ```
  {
    "status" : "200 OK",
    "payload" : true
  }
  ```