

# Example of `explain` output for a mathematical value expression function
<a name="access-graph-opencypher-explain-example-4"></a>

In this example, `RETURN abs(-10)` performs a simple evaluation, taking the absolute value of a constant, `-10`.

`DFEChunkLocalSubQuery` (ID 1) performs a solution injection for the static value `-10`, which is stored in the variable, `?100`.

`DFEApply` (ID 2) is the operator that executes the absolute value function `abs()` on the static value stored in `?100` variable.

Here is the query and resulting `explain` output.

To invoke `explain` for this query:

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-explain-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "RETURN abs(-10)" \
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
    openCypherQuery='RETURN abs(-10)',
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
  -d "query=RETURN abs(-10)" \
  -d "explain=details"
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

```
curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=RETURN abs(-10)" \
  -d "explain=details"
```

------

The `explain` output:

```
Query:
RETURN abs(-10)

╔════╤════════╤════════╤═══════════════════╤═══════════════════════╤═════════════════════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name              │ Arguments             │ Mode                │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════╪═══════════════════════╪═════════════════════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ SolutionInjection │ solutions=[{}]        │ -                   │ 0        │ 1         │ 0.00  │ 0         ║
╟────┼────────┼────────┼───────────────────┼───────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFESubquery       │ subQuery=subQuery1    │ -                   │ 0        │ 1         │ 0.00  │ 4.00      ║
╟────┼────────┼────────┼───────────────────┼───────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ TermResolution    │ vars=[?_internalVar1] │ id2value_opencypher │ 1        │ 1         │ 1.00  │ 1.00      ║
╚════╧════════╧════════╧═══════════════════╧═══════════════════════╧═════════════════════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery1
╔════╤════════╤════════╤═══════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments                                                                                                    │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFESolutionInjection  │ outSchema=[]                                                                                                 │ -    │ 0        │ 1         │ 0.00  │ 0.01      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEChunkLocalSubQuery │ subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#c4cc6148-cce3-4561-93c0-deb91f257356/graph_1 │ -    │ 1        │ 1         │ 1.00  │ 0.03      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 3      │ -      │ DFEApply              │ functor=abs(?100)                                                                                            │ -    │ 1        │ 1         │ 1.00  │ 0.26      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ 4      │ -      │ DFEBindRelation       │ inputVars=[?_internalVar2, ?_internalVar2]                                                                   │ -    │ 1        │ 1         │ 1.00  │ 0.04      ║
║    │        │        │                       │ outputVars=[?_internalVar2, ?_internalVar1]                                                                  │      │          │           │       │           ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 4  │ 5      │ -      │ DFEProject            │ columns=[?_internalVar1]                                                                                     │ -    │ 1        │ 1         │ 1.00  │ 0.06      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 5  │ -      │ -      │ DFEDrain              │ -                                                                                                            │ -    │ 1        │ 0         │ 0.00  │ 0.05      ║
╚════╧════════╧════════╧═══════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝

subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#c4cc6148-cce3-4561-93c0-deb91f257356/graph_1
╔════╤════════╤════════╤══════════════════════╤═════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                 │ Arguments                           │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪══════════════════════╪═════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFESolutionInjection │ solutions=[?100 -> [-10^^<LONG>]]   │ -    │ 0        │ 1         │ 0.00  │ 0.01      ║
║    │        │        │                      │ outSchema=[?100]                    │      │          │           │       │           ║
╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 3      │ -      │ DFERelationalJoin    │ joinVars=[]                         │ -    │ 2        │ 1         │ 0.50  │ 0.18      ║
╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 1      │ -      │ DFESolutionInjection │ outSchema=[]                        │ -    │ 0        │ 1         │ 0.00  │ 0.01      ║
╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ -      │ -      │ DFEDrain             │ -                                   │ -    │ 1        │ 0         │ 0.00  │ 0.02      ║
╚════╧════════╧════════╧══════════════════════╧═════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```