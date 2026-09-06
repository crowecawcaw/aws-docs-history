

# Examples of openCypher parameterized queries
<a name="opencypher-parameterized-queries"></a>

Neptune supports parameterized openCypher queries. This lets you use the same query structure multiple times with different arguments. Since the query structure doesn't change, Neptune can cache its abstract syntax tree (AST) rather than having to parse it multiple times.

## Example of an openCypher parameterized query using the HTTPS endpoint
<a name="opencypher-http-parameterized-queries"></a>

Below is an example of using a parameterized query with the Neptune openCypher HTTPS endpoint. The query is:

```
MATCH (n {name: $name, age: $age})
RETURN n
```

The parameters are defined as follows:

```
parameters={"name": "john", "age": 20}
```

You can submit the parameterized query like this:

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "MATCH (n {name: \$name, age: \$age}) RETURN n" \
  --parameters '{"name": "john", "age": 20}'
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
    openCypherQuery='MATCH (n {name: $name, age: $age}) RETURN n',
    parameters='{"name": "john", "age": 20}'
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
  -d "query=MATCH (n {name: \$name, age: \$age}) RETURN n" \
  -d 'parameters={"name": "john", "age": 20}'
```

**Note**  
This example assumes that your AWS credentials are configured in your environment. Replace {{us-east-1}} with the Region of your Neptune cluster.

------
#### [ curl ]

Using `POST`:

```
curl https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -d "query=MATCH (n {name: \$name, age: \$age}) RETURN n" \
  -d "parameters={\"name\": \"john\", \"age\": 20}"
```

Using `GET` (URL-encoded):

```
curl -X GET \
  "https://{{your-neptune-endpoint}}:{{port}}/openCypher?query=MATCH%20%28n%20%7Bname:\$name,age:\$age%7D%29%20RETURN%20n&parameters=%7B%22name%22:%22john%22,%22age%22:20%7D"
```

Using `DIRECT POST`:

```
curl -H "Content-Type: application/opencypher" \
  "https://{{your-neptune-endpoint}}:{{port}}/openCypher?parameters=%7B%22name%22:%22john%22,%22age%22:20%7D" \
  -d "MATCH (n {name: \$name, age: \$age}) RETURN n"
```

------

## Examples of openCypher parameterized queries using Bolt
<a name="opencypher-bolt-parameterized-queries"></a>

Here is a Python example of an openCypher parameterized query using the Bolt protocol:

```
from neo4j import GraphDatabase
uri = "bolt://[neptune-endpoint-url]:8182"
driver = GraphDatabase.driver(uri, auth=("", ""))

def match_name_and_age(tx, name, age):
  # Parameterized Query
  tx.run("MATCH (n {name: $name, age: $age}) RETURN n", name=name, age=age)

with driver.session() as session:
  # Parameters
  session.read_transaction(match_name_and_age, "john", 20)

driver.close()
```

Here is a Java example of an openCypher parameterized query using the Bolt protocol:

```
Driver driver = GraphDatabase.driver("bolt+s://{{(your cluster endpoint URL)}}:8182");
HashMap<String, Object> parameters = new HashMap<>();
parameters.put("name", "john");
parameters.put("age", 20);
String queryString = "MATCH (n {name: $name, age: $age}) RETURN n";
Result result = driver.session().run(queryString, parameters);
```