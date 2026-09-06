

# Example of `explain` output for a relationship lookup with a limit
<a name="access-graph-opencypher-explain-example-2"></a>

This query looks for relationships between two anonymous nodes with type `route`, and returns at most 10. Again, the `explain` mode is `details` and the output format is the default ASCII format.

Here, `DFEPipelineScan` scans for edges that start from anonymous node `?anon_node7` and end at another anonymous node `?anon_node21`, with a relationship type saved as `?p_type1`. There is a filter for `?p_type1` being `el://route` (where `el` stands for edge label), which corresponds to `[p:route]` in the query string.

`DFEDrain` collects the output solution with a limit of 10, as shown in its `Arguments` column. `DFEDrain` terminates once the limit is reached or the all solutions are produced, whichever happens first.

To invoke `explain` for this query:

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-explain-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "MATCH ()-[p:route]->() RETURN p LIMIT 10" \
  --explain-mode details
```

For more information, see [execute-open-cypher-explain-query](https://docs.aws.amazon.com/cli/latest/reference/neptunedata/execute-open-cypher-explain-query.html) in the AWS CLI Command Reference.

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

response = client.execute_open_cypher_explain_query(
    openCypherQuery='MATCH ()-[p:route]->() RETURN p LIMIT 10',
    explainMode='details'
)

print(response['results'].read().decode('utf-8'))
```

For AWS SDK examples in other languages, see [AWS SDK](access-graph-opencypher-sdk.md).

------
#### [ awscurl ]

```
awscurl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  --region {{us-east-1}} \
  --service neptune-db \
  -X POST \
  -d "query=MATCH ()-[p:route]->() RETURN p LIMIT 10" \
  -d "explain=details"
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=MATCH ()-[p:route]->() RETURN p LIMIT 10" \
  -d "explain=details"
```

------

The `explain` output:

```
Query:
MATCH ()-[p:route]->() RETURN p LIMIT 10

╔════╤════════╤════════╤═══════════════════╤════════════════════╤═════════════════════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name              │ Arguments          │ Mode                │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════╪════════════════════╪═════════════════════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ SolutionInjection │ solutions=[{}]     │ -                   │ 0        │ 1         │ 0.00  │ 0         ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFESubquery       │ subQuery=subQuery1 │ -                   │ 0        │ 10        │ 0.00  │ 5.00      ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ TermResolution    │ vars=[?p]          │ id2value_opencypher │ 10       │ 10        │ 1.00  │ 1.00      ║
╚════╧════════╧════════╧═══════════════════╧════════════════════╧═════════════════════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery1
╔════╤════════╤════════╤═════════════════╤═══════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name            │ Arguments                                                 │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═════════════════╪═══════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan │ pattern=Edge((?anon_node7)-[?p:?p_type1]->(?anon_node21)) │ -    │ 0        │ 1000      │ 0.00  │ 0.66      ║
║    │        │        │                 │ inlineFilters=[(?p_type1 IN [<el://route>])]              │      │          │           │       │           ║
║    │        │        │                 │ patternEstimate=26219                                     │      │          │           │       │           ║
╟────┼────────┼────────┼─────────────────┼───────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEProject      │ columns=[?p]                                              │ -    │ 1000     │ 1000      │ 1.00  │ 0.14      ║
╟────┼────────┼────────┼─────────────────┼───────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ DFEDrain        │ limit=10                                                  │ -    │ 1000     │ 0         │ 0.00  │ 0.11      ║
╚════╧════════╧════════╧═════════════════╧═══════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```