

# openCypher query timeout hint
<a name="opencypher-query-hints-timeout-hint"></a>

 Query timeout behavior can be configured on a per-query basis by query-level query hint `QUERY:TIMEOUTMILLISECONDS`. It must be used with the `USING` clause. The query hint accepts non-negative long as a value. 

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"
```

For more information, see [execute-open-cypher-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/execute-open-cypher-query.html) in the AWS CLI Command Reference.

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

response = client.execute_open_cypher_query(
    openCypherQuery='USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1'
)

print(response['results'])
```

For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"
```

------

 Query timeout behavior will consider the minimum of cluster-level timeout and query-level timeout. Please see below examples to understand query timeout behavior. For more information on cluster-level query timeout, see [neptune\_query\_timeout](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html#parameters-db-cluster-parameters-neptune_query_timeout). 

```
# Suppose `neptune_query_timeout` is 10000 ms and query-level timeout is set to 100 ms
# It will consider 100 ms as the final timeout 

curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"

# Suppose `neptune_query_timeout` is 100 ms and query-level timeout is set to 10000 ms
# It will still consider 100 ms as the final timeout 

curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 10000 MATCH(n) RETURN n LIMIT 1"
```

If a query exceeds the timeout, Neptune terminates it and returns a time-out error. Whether to retry a timed-out query depends on the nature of the failure and your workload. For guidance, see [Exception Handling and Retries](transactions-exceptions.md).