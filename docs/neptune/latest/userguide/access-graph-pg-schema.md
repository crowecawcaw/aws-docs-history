

# Property graph schema
<a name="access-graph-pg-schema"></a>

The `neptune.graph.pg_schema()` procedure provides a comprehensive overview of your property graph structure. It returns all node labels, edge labels, properties with their data types, and label triples (`{~from, ~type, ~to}` patterns that describe how node types connect through edge types).

This procedure is currently available only through the openCypher endpoint and discovers the schema for all property graph data.

Use this procedure for tasks such as:
+ **AI and LLM query generation** – Give LLMs the graph structure they need to generate valid Cypher queries from natural language (Text-to-Cypher, GraphRAG applications).
+ **Graph visualization and exploration** – Tools like [Graph Explorer](visualization-graph-explorer.md) use schema information to render interactive visual representations of graph data without scanning the entire database.
+ **Application schema discovery** – Applications that need to understand graph structure at startup, such as GraphQL schema generators or data validation tools.

## Comparison with Neptune Analytics
<a name="access-graph-pg-schema-comparison-analytics"></a>

In Neptune Analytics, [`neptune.graph.pg_schema()`](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/custom-algorithms-property-graph-schema.html) is synchronous. It computes the schema on every call.

In Neptune Database, you explicitly trigger an asynchronous schema computation by calling `neptune.graph.pg_schema.compute()`, which returns immediately. The computation runs in the background while you poll for completion using `neptune.graph.pg_schema()`. Once computed, Neptune persists the schema and returns it instantly on subsequent reads without recomputation. Partial results are also available while the computation is still in progress. You can also stop a running computation and resume it later.

## Comparison with the Graph Summary API
<a name="access-graph-pg-schema-comparison-summary"></a>

The [Graph Summary API](neptune-graph-summary.md) does not provide label triples or property data types. The property graph schema procedure fills this gap. Label triples show the specific relationship patterns in your graph. For example, a `Person` connects to a `Company` via a `worksAt` edge. This information is critical for LLMs to generate semantically correct queries.

## Prerequisites
<a name="access-graph-pg-schema-prerequisites"></a>

### Engine version
<a name="access-graph-pg-schema-engine-version"></a>

The property graph schema procedure requires Neptune engine version 1.4.8.0 or later.

### IAM permissions
<a name="access-graph-pg-schema-iam"></a>

The following IAM actions are required for each schema operation:
+ `CALL neptune.graph.pg_schema()` – requires `neptune-db:ReadDataViaQuery`.
+ `CALL neptune.graph.pg_schema.compute()` – requires `neptune-db:ReadDataViaQuery` and `neptune-db:WriteDataViaQuery`.
+ `CALL neptune.graph.pg_schema.stop()` – requires `neptune-db:ReadDataViaQuery` and `neptune-db:WriteDataViaQuery`.

The `compute()` and `stop()` operations require write permissions because they modify internal state used to cache and persist the schema.

**Example IAM policy**  
The following policy grants the minimum permissions needed for all schema operations:  

```
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "neptune-db:ReadDataViaQuery",
      "neptune-db:WriteDataViaQuery"
    ],
    "Resource": "arn:aws:neptune-db:us-east-1:123456789012:cluster-resource-id/*"
  }]
}
```

To grant read-only access to the schema (without the ability to trigger computation), use only `neptune-db:ReadDataViaQuery`.

### Writer and reader instances
<a name="access-graph-pg-schema-writer-reader"></a>

You can trigger schema computation only on the writer instance. Read replica instances can read the schema (which is replicated from the writer) but cannot run `compute()` or `stop()`.

## API reference
<a name="access-graph-pg-schema-api"></a>

### Read schema
<a name="access-graph-pg-schema-read"></a>

Retrieves the current schema and computation status.

**Syntax:**

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "CALL neptune.graph.pg_schema()"
```

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
    openCypherQuery='CALL neptune.graph.pg_schema()'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --region {{us-east-1}} --service neptune-db \
  -d 'query=CALL neptune.graph.pg_schema()'
```

------

**Behavior:** Returns immediately with the current schema and status. Always non-blocking. If no schema has been computed, returns state: `"NotStarted"` with empty schema fields. If a computation is in progress, returns partial results with state: `"InProgress"`.

**Response format:**

The response contains a schema object with the following fields:

**Status object:**
+ `state` (String) – Current lifecycle state: `NotStarted`, `InProgress`, `Completed`, `Stopped`, `Failed`
+ `concurrency` (String) – Number of threads used for the computation. 0 means auto (determined based on hardware). Range: 1 (lowest) to 16 (highest).
+ `lastComputedTimestamp` (String) – ISO-8601 UTC timestamp of the last successful computation (e.g., `2026-05-29T08:00:00Z`)
+ `progressPercentage` (String) – Computation progress: 0 when not started, 0–99 during computation, 100 when completed
+ `errorMessage` (String) – Present only when a request is rejected or the computation fails. Explains the reason.

**Schema object:**
+ `nodeLabels` – Array of all unique node labels in the graph
+ `edgeLabels` – Array of all unique edge labels in the graph
+ `nodeLabelDetails` – For each node label: properties and their data types
+ `edgeLabelDetails` – For each edge label: properties and their data types
+ `labelTriples` – Array of relationship patterns: `{~from, ~type, ~to}` describing which node types connect through which edge types

**Supported data types:** `String`, `Int`, `Long`, `Double`, `Bool`, `Date`

If a property has multiple data types across different nodes (for example, some nodes store `age` as `Int` and others as `String`), all observed types are listed in the `datatypes` array.

### Compute schema
<a name="access-graph-pg-schema-compute"></a>

Triggers a background schema computation.

**Syntax:**

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "CALL neptune.graph.pg_schema.compute()"
```

With optional concurrency parameter:

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "CALL neptune.graph.pg_schema.compute({concurrency: 2})"
```

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
    openCypherQuery='CALL neptune.graph.pg_schema.compute()'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --region {{us-east-1}} --service neptune-db \
  -d 'query=CALL neptune.graph.pg_schema.compute()'
```

With optional concurrency parameter:

```
awscurl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --region {{us-east-1}} --service neptune-db \
  -d 'query=CALL neptune.graph.pg_schema.compute({concurrency: 2})'
```

------

**IAM actions required:** `neptune-db:ReadDataViaQuery` and `neptune-db:WriteDataViaQuery`

**Parameters:**
+ `concurrency` (Integer, optional) – Number of threads for the background computation. 0 (default) = determined automatically based on hardware. Range: 1 (lowest) to 16 (highest). Use lower values on smaller instances to reduce resource impact.

**Behavior:**
+ Returns immediately with the current status. The computation runs asynchronously in the background.
+ If called when state is `Stopped`, the computation resumes from where it left off.
+ If called when state is `Completed`, starts a fresh recomputation. The previous schema continues serving reads until the new computation completes.
+ If called when a computation is already `InProgress`, Neptune rejects the request with an error message.
+ If called during an active bulk load, Neptune rejects the request with an error message.

**Response:** Returns the status object showing state: `"InProgress"` with the `concurrency` and `progressPercentage` fields.

### Stop schema computation
<a name="access-graph-pg-schema-stop"></a>

Stops a running background computation.

**Syntax:**

------
#### [ AWS CLI ]

```
aws neptunedata execute-open-cypher-query \
  --endpoint-url https://{{your-neptune-endpoint}}:{{port}} \
  --open-cypher-query "CALL neptune.graph.pg_schema.stop()"
```

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
    openCypherQuery='CALL neptune.graph.pg_schema.stop()'
)

print(response)
```

------
#### [ awscurl ]

```
awscurl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --region {{us-east-1}} --service neptune-db \
  -d 'query=CALL neptune.graph.pg_schema.stop()'
```

------

**IAM actions required:** `neptune-db:ReadDataViaQuery` and `neptune-db:WriteDataViaQuery`

**Behavior:**
+ Stops the running computation. Progress is saved so it can resume from where it left off when you call `compute()` again.
+ A stopped computation does *not* automatically resume on engine restart. You must explicitly call `compute()`.

**Response:** Returns the status object showing state: `"Stopped"` with the current `progressPercentage`.

## Using YIELD with schema results
<a name="access-graph-pg-schema-yield"></a>

You can use `YIELD` to extract schema fields and combine them with other queries. The following example retrieves all node labels and counts the number of nodes for each label. The `collSort()` function sorts the list alphabetically:

```
CALL neptune.graph.pg_schema()
  YIELD schema
  WITH schema.nodeLabels as nl
  UNWIND collSort(nl) as label
  MATCH (n)
  WHERE label in labels(n)
  RETURN label, COUNT(n) as count
```

Sample output:

```
{
  "results": [{
      "label": "airport",
      "count": 3503
    }, {
      "label": "continent",
      "count": 7
    }, {
      "label": "country",
      "count": 237
    }, {
      "label": "version",
      "count": 1
    }]
}
```

## Schema computation lifecycle
<a name="access-graph-pg-schema-lifecycle"></a>

### Asynchronous operation
<a name="access-graph-pg-schema-async"></a>

Schema computation is an asynchronous operation. When you call `neptune.graph.pg_schema.compute()`, it returns immediately with the current status. The computation runs in the background. You poll for progress and completion by calling `neptune.graph.pg_schema()`, which returns the current state and `progressPercentage`.

### States
<a name="access-graph-pg-schema-states"></a>

The schema computation moves through the following states:
+ `NotStarted` – No schema has been computed yet. `pg_schema()` returns an empty schema.
+ `InProgress` – A background computation is running. `pg_schema()` returns partial results (a union of the last complete schema and discoveries from the current computation).
+ `Completed` – The computation finished successfully. The full schema is available.
+ `Stopped` – The computation was stopped, either by calling `stop()` or because an engine restart interrupted it. Partial results are available. Progress is saved so the computation can resume from where it left off when you call `compute()`.
+ `Failed` – The computation encountered an error. The last successfully computed schema (if any) remains available.

### Persistence and restart behavior
<a name="access-graph-pg-schema-persistence"></a>

The computed schema is persisted and survives engine restarts. The restart behavior depends on the state at the time of restart:
+ `InProgress` – If the engine restarts during computation, the computation transitions to `Stopped`. Call `compute()` to resume from where it left off. Progress is preserved and the computation continues from its last checkpoint.
+ `Stopped` – The computation does *not* automatically resume. You must call `compute()` to continue from where it left off.
+ `Completed` – The schema is loaded and available immediately.

### Partial results
<a name="access-graph-pg-schema-partial"></a>

While a computation is in progress, `pg_schema()` returns partial results. These include any previously completed schema merged with the labels, properties, and triples discovered so far in the current computation. This means you do not have to wait for a full computation to complete before retrieving useful schema information.

### Read replicas
<a name="access-graph-pg-schema-replicas"></a>

Read replica instances can read the schema using `CALL neptune.graph.pg_schema()`. Neptune replicates the schema from the writer instance and makes it available on replicas almost immediately as schema elements are discovered on the writer.

Read replicas cannot run `compute()` or `stop()`. These calls return an error:
+ `compute()` – `"Schema cannot be computed on read replica"`
+ `stop()` – `"Schema compute cannot be stopped on read replica"`

## Best practices
<a name="access-graph-pg-schema-best-practices"></a>
+ **Recompute after mutations** – The schema does not update automatically when data changes. Recompute the schema after bulk loads or significant data mutations. Use the `lastComputedTimestamp` field to determine whether the schema is outdated relative to recent changes in your graph.
+ **Concurrency** – The default concurrency value (0) automatically adapts to your instance hardware. For most workloads this is the recommended setting. If the background computation impacts your query workload, specify a lower value (for example, 1 or 2) to reduce resource usage.
+ **Stop and resume** – If the background computation impacts your query workload, stop it with `stop()` and resume later during a lower-traffic period by calling `compute()` again. The computation continues from where it left off.
+ **Handle restarts gracefully** – If the engine restarts while a schema computation is in progress, the computation transitions to `Stopped`. Call `compute()` to resume from where it left off. Progress is preserved.
+ **Large databases** – For databases with large storage volumes (multiple TB), a full schema computation may take extended time. You can start a compute, let it run until 10–20% progress, then stop. The partial results collected during this window provide a useful schema sample with many labels, properties, and triples already discovered. Read the partial schema with `pg_schema()` while the computation is in progress or after stopping. Resume later when your workload allows.

## Limitations
<a name="access-graph-pg-schema-limitations"></a>
+ **Deletes require recompute** – Deleted labels, properties, and triples are only removed from the schema after the next full recomputation. Until then, deleted elements might still appear in schema results.
+ **OpenCypher only** – You can call this procedure only through the openCypher query endpoint.
+ **Cannot compute during bulk load** – Neptune rejects schema computation while a bulk load operation is active. Trigger compute after the bulk load completes.

## Sample output
<a name="access-graph-pg-schema-sample"></a>

The following example shows the schema output for the air-routes dataset:

```
awscurl -X POST https://{{your-neptune-endpoint}}:{{port}}/openCypher \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --region {{us-east-1}} --service neptune-db \
  -d 'query=CALL neptune.graph.pg_schema()'
```

```
{
  "results": [{
      "schema": {
        "edgeLabelDetails": {
          "route": {
            "properties": {
              "dist": ["Int"]
            }
          },
          "contains": {
            "properties": {}
          }
        },
        "edgeLabels": ["route", "contains"],
        "status": {
          "concurrency": "16",
          "lastComputedTimestamp": "2026-06-04T23:58:17Z",
          "state": "Completed",
          "progressPercentage": "100"
        },
        "nodeLabels": ["version", "continent", "airport", "country"],
        "labelTriples": [{
            "~type": "route",
            "~from": "airport",
            "~to": "airport"
          }, {
            "~type": "contains",
            "~from": "country",
            "~to": "airport"
          }, {
            "~type": "contains",
            "~from": "continent",
            "~to": "airport"
          }],
        "nodeLabelDetails": {
          "continent": {
            "properties": {
              "type": ["String"],
              "code": ["String"],
              "desc": ["String"]
            }
          },
          "airport": {
            "properties": {
              "type": ["String"],
              "city": ["String"],
              "icao": ["String"],
              "code": ["String"],
              "country": ["String"],
              "lat": ["Double"],
              "longest": ["Int"],
              "runways": ["Int"],
              "desc": ["String"],
              "lon": ["Double"],
              "region": ["String"],
              "elev": ["Int"]
            }
          },
          "country": {
            "properties": {
              "type": ["String"],
              "code": ["String"],
              "desc": ["String"]
            }
          },
          "version": {
            "properties": {
              "date": ["String"],
              "desc": ["String"],
              "author": ["String"],
              "type": ["String"],
              "code": ["String"]
            }
          }
        }
      }
    }]
}
```