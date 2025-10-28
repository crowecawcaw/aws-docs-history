# ExecuteQuery

ExecuteQuery runs queries against a Neptune Analytics graph. Supported language: openCypher.

## ExecuteQuery inputs

- graph-identifier (required)

Type: `String`

The identifier representing a graph.

- region (required)

Type: `String`

The region where the graph is present.

- query-string (required)

Type: `String`

Default: none

A string representing a query.

- language (required)

Type: `Enum`

Default: none

The query language the query is written in. Currently, only `OPEN_CYPHER` is supported.

- parameters (optional)

Type: `Map`

A map from `String` to `String` where the key is the parameter name and the value
is the parameter value.

- plan-cache (optional)

Type: `Enum`

Query plan cache is a feature that saves the query plan and reuses it on successive executions of the
same query, reducing query latency. Query plan cache works for both read-only and mutation queries. The plan
cache is an LRU cache with a five minute TTL and a capacity of 1000. It supports the following values:

    + `AUTO`: The engine will automatically decide to cache the query plan. If the query
     is parameterized and the runtime is shorter than 100ms, the query plan is automatically cached.
    + `ENABLED`: The query plan is cached regardless of the query runtime. The plan cache
     uses the query string as the key, this means that if a query is slightly different (i.e. different constants),
     it will not be able to reuse the plan cache of similar queries.
    + `DISABLED`: The query plan cache is not used.

For more information on the query plan cache, see
[Query plan cache](query-plan-cache.md "query-plan-cache.md").

- explain-mode (optional)

Type: `Enum`

The explain mode parameters allow getting a query explain instead of the actual query results.
A query explain can be used to gather insights about the query execution such as planning decisions,
time spent on each operator, number of records flowing etc. If this parameter is not set the query is
executed normally and the result is returned. The acceptable values for query explain are:

    + `STATIC`: Returns a query explain without executing the query. This can give an
     estimate on what the query plan looks like without actually executing the query. The static query plan may
     differ from the actual query plan. Actual queries may make planning decisions based on runtime statistics,
     which may not be considered when fetching a static query plan. A static query plan is useful when it is
     necessary to observe a plan for a query that either does not complete or runs for too long.
    + `DETAILS`: Returns a detailed query plan that shows what the running query did.
     This includes information such as operators runtime, number of records flowing through the plan, runtime
     planning decisions and more. If a query does not succeed in `NONE` mode, it will not succeed in
     `DETAILS` mode either. In this instance, you would want to use `STATIC` mode.

For more information on query explain and its output, see
[Query explain](query-explain.md "query-explain.md").

- query-timeout-milliseconds (optional)

Type: `Enum`

If specified, provides an upper bound to the query run time. This parameter will override the graph default
timeout (30 minutes). Neptune Analytics graph have a maximum query runtime of 60 minutes. If the specified timeout is greater than
the maximum query runtime, the query will only run for the maximum query runtime.

    + Using the default settings, any CLI or SDK request will timeout in 60 seconds and attempt a retry.
     For the cases where you are running queries that can take longer than 60 seconds, it is recommended
     to set the CLI/SDK timeout to `0` (no timeout), or a much larger value to avoid
     unnecesssary retries.




     It is also recommended to set `MAX_ATTEMPTS` for CLI/SDK to `1` for
     `execute_query` to avoid any retries by CLI/SDK.




     For the Boto client, set the `read_timeout` to `None`, and the
     `total_max_attempts` to `1`.




    ```
    import boto3
    from botocore.config import Config
    n = boto3.client('neptune-graph',
                     config=(Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)))
    ```


     For the CLI, set the `--cli-read-timeout` parameter to `0` for no timeout,
     and set the environment variable `AWS_MAX_ATTEMPTS` to `1` to prevent retries.




    ```
    export AWS_MAX_ATTEMPTS=1
    ```


    ```
    aws neptune-graph execute-query \
    --graph-identifier <graph-id> \
    --region <region> \
    --query-string "MATCH (p:Person)-[r:KNOWS]->(p1) RETURN *;" \
    --cli-read-timeout 0
    --language open_cypher /tmp/out.txt
    ```

## ExecuteQuery examples

AWS CLI

```
# Sample query
aws neptune-graph execute-query \
--graph-identifier <graph-id> \
--region <region> \
--query-string "MATCH (p:Person)-[r:KNOWS]->(p1) RETURN *;" \
--language open_cypher \
/tmp/out.txt

# Sample query that prints directly to the console.
aws neptune-graph execute-query \
--graph-identifier <graph-id> \
--region <region> \
--query-string "MATCH (p:Person)-[r:KNOWS]->(p1) RETURN *;" \
--language open_cypher \
/dev/stdout

# parameters supported
query-string [REQUIRED] : String
language [REQUIRED] : open_cypher
explain-mode [OPTIONAL] : static | details
query-timeout-milliseconds [OPTIONAL] : Integer
plan-cache [OPTIONAL] : enabled | disabled | auto
parameters [OPTIONAL] : Map
```

AWSCURL

```
# Sample query
awscurl -X POST "https://<graph-id>.<endpoint>/queries" \
-H "Content-Type: application/x-www-form-urlencoded" \
--region <region> \
--service neptune-graph \
-d "query=MATCH (p:Person)-[r:KNOWS]->(p1) RETURN *;"
```

## ExecuteQuery output

```
{
  "results": [{
      "p": {
        "~id": "fa1ef9b0-fa32-4b37-8051-78f2bf0e0d63",
        "~entityType": "node",
        "~labels": ["Person"],
        "~properties": {
          "name": "Simone"
        }
      },
      "p1": {
        "~id": "edaded10-b22b-4818-a22e-ddebfcf37acb",
        "~entityType": "node",
        "~labels": ["Person"],
        "~properties": {
          "name": "Mirro"
        }
      },
      "r": {
        "~id": "neptune_reserved_1_1154145192329347075",
        "~entityType": "relationship",
        "~start": "fa1ef9b0-fa32-4b37-8051-78f2bf0e0d63",
        "~end": "edaded10-b22b-4818-a22e-ddebfcf37acb",
        "~type": "KNOWS",
        "~properties": {}
      }
    }]
}
```

## Parameterized queries

Neptune Analytics supports parameterized openCypher queries. This allows you to use the same query structure multiple times
with different arguments. Since the query structure doesn't change, Neptune Analytics tries to cache the plan for these parameterized
queries that run in less than 100 milliseconds.

The following is an example of using a parameterized query with the Neptune openCypher HTTPS endpoint.
The query is:

```
MATCH (n {name: $name, age: $age})
RETURN n
```

The parameters are definied as follows:

```
parameters={"name": "john", "age": 20}
```

AWS CLI

```
# Sample query
aws neptune-graph execute-query \
--graph-identifier <graph-id> \
--region <region> \
--query-string "MATCH (n {name: \$name, age: \$age}) RETURN n" \
--parameters "{\"name\": \"john\", \"age\": 20}"
--language open_cypher /tmp/out.txt
```

AWSCURL

```
# Sample query
awscurl -X POST "https://[graph-id].<endpoint>/queries" \
-H "Content-Type: application/x-www-form-urlencoded" \
--region <region> \
--service neptune-graph \
-d "query=MATCH (n {name: \$name, age: \$age}) RETURN n;&parameters={\"name\": \"john\", \"age\": 20}"
```
