# Export parameter fields in the `params` top-level JSON object

The Neptune export `params` JSON object allows you to control the
export, including the type and format of the exported data.

## List of possible fields in the export

parameters `params` object

Listed below are all the possible top-level fields that can appear in a
`params` object. Only a subset of these fields appear in any one
object.

### List of fields common to all types of export

- [cloneCluster](#export-params-cloneCluster "#export-params-cloneCluster")
- [cloneClusterInstanceType](#export-params-cloneClusterInstanceType "#export-params-cloneClusterInstanceType")
- [cloneClusterReplicaCount](#export-params-cloneClusterReplicaCount "#export-params-cloneClusterReplicaCount")
- [cloneClusterEnableAuditLogs](#export-params-cloneClusterEnableAuditLogs "#export-params-cloneClusterEnableAuditLogs")
- [clusterId](#export-params-clusterId "#export-params-clusterId")
- [endpoint](#export-params-endpoint "#export-params-endpoint")
- [endpoints](#export-params-endpoints "#export-params-endpoints")
- [profile](#export-params-profile "#export-params-profile")
- [useIamAuth](#export-params-useIamAuth "#export-params-useIamAuth")
- [includeLastEventId](#export-params-includeLastEventId "#export-params-includeLastEventId")

### List of fields for property-graph exports

- [concurrency](#export-params-concurrency "#export-params-concurrency")
- [edgeLabels](#export-params-edgeLabels "#export-params-edgeLabels")
- [filter](#export-params-filter "#export-params-filter")
- [filterConfigFile](#export-params-filterConfigFile "#export-params-filterConfigFile")
- [gremlinFilter](#export-params-gremlinFilter "#export-params-gremlinFilter")
- [gremlinNodeFilter](#export-params-gremlinFilter "#export-params-gremlinFilter")
- [gremlinEdgeFilter](#export-params-gremlinFilter "#export-params-gremlinFilter")
- [format](#export-params-format-pg "#export-params-format-pg")
- [nodeLabels](#export-params-nodeLabels "#export-params-nodeLabels")
- [scope](#export-params-scope "#export-params-scope")

### List of fields for RDF exports

- [format](#export-params-format-rdf "#export-params-format-rdf")
- [rdfExportScope](#export-params-rdfExportScope "#export-params-rdfExportScope")
- [sparql](#export-params-sparql "#export-params-sparql")
- [namedGraph](#namedgraph-params-sparql "#namedgraph-params-sparql")

## Fields common to all types of export

### `cloneCluster` field in `params`

_(Optional)_. Default: `false`.

If the `cloneCluster` parameter is set to `true`,
the export process uses a fast clone of your DB cluster:

```
  "cloneCluster" : true
```

By default, the export process exports data from the DB cluster that you specify
using the `endpoint`, `endpoints` or `clusterId`
parameters. However, if your DB cluster is in use while the export is going on,
and data is changing, the export process cannot guarantee the consistency of the
data being exported.

To ensure that the exported data is consistent, use the `cloneCluster`
parameter to export from a static clone of your DB cluster instead.

The cloned DB cluster is created in the same VPC as the source DB cluster and
inherits the security group, subnet group and IAM database authentication settings of the
source. When the export is complete, Neptune deletes the cloned DB cluster.

By default, a cloned DB cluster consists of a single instance of the same instance
type as the primary instance in the source DB cluster. You can change the instance
type used for the cloned DB cluster by specifying a different one using
`cloneClusterInstanceType`.

###### Note

If you don't use the `cloneCluster` option, and are exporting
directly from your main DB cluster, you might need to increase the timeout on the
instances from which data is being exported. For large data sets, the timeout
should be set to several hours.

### `cloneClusterInstanceType` field in `params`

_(Optional)_.

If the `cloneCluster` parameter is present and set to `true`,
you can use the `cloneClusterInstanceType` parameter to specify the instance type
used for the cloned DB cluster:

By default, a cloned DB cluster consists of a single instance of the same instance
type as the primary instance in the source DB cluster.

```
  "cloneClusterInstanceType" : "`(for example, r5.12xlarge)`"
```

### `cloneClusterReplicaCount` field in `params`

_(Optional)_.

If the `cloneCluster` parameter is present and set to `true`,
you can use the `cloneClusterReplicaCount` parameter to specify the number of
read-replica instances created in the cloned DB cluster:

```
  "cloneClusterReplicaCount" : `(for example, 3)`
```

By default, a cloned DB cluster consists of a single primary instance. The
`cloneClusterReplicaCount` parameter lets you specify how many additional
read-replica instances should be created.

### `cloneClusterEnableAuditLogs` field in `params`

_(Optional)_. Default: false.

If the `cloneCluster` parameter is present and set to true, you can use the
`cloneClusterEnableAuditLogs` parameter to enable or disable audit logs in the cloned cluster.

By default, audit logging is disabled.

```
"cloneClusterEnableAuditLogs" : true
```

### `clusterId` field in `params`

_(Optional)_.

The `clusterId` parameter specifies the ID of a DB cluster to use:

```
  "clusterId" : "`(the ID of your DB cluster)`"
```

If you use the `clusterId` parameter, the export process uses all
available instances in that DB cluster to extract data.

###### Note

The `endpoint`, `endpoints`, and `clusterId`
parameters are mutually exclusive. Use one and only one of them.

### `endpoint` field in `params`

_(Optional)_.

Use `endpoint` to specify an endpoint of a Neptune instance in your
DB cluster that the export process can query to extract data (see [Endpoint Connections](feature-overview-endpoints.md "feature-overview-endpoints.md")).
This is the DNS name only, and does not include the protocol or port:

```
  "endpoint" : "`(a DNS endpoint of your DB cluster)`"
```

Use a cluster or instance endpoint, but not the main reader endpoint.

###### Note

The `endpoint`, `endpoints`, and `clusterId`
parameters are mutually exclusive. Use one and only one of them.

### `endpoints` field in `params`

_(Optional)_.

Use `endpoints` to specify a JSON array of endpoints in your DB cluster
that the export process can query to extract data (see [Endpoint Connections](feature-overview-endpoints.md "feature-overview-endpoints.md")).
These are DNS names only, and do not include the protocol or port:

```
  "endpoints": [
    "`(one endpoint in your DB cluster)`",
    "`(another endpoint in your DB cluster)`",
    "`(a third endpoint in your DB cluster)`"
    ]
```

If you have multiple instances in your cluster (a primary and one or more
read replicas), you can improve export performance by using the `endpoints`
parameter to distribute queries across a list of those endpoints.

###### Note

The `endpoint`, `endpoints`, and `clusterId`
parameters are mutually exclusive. Use one and only one of them.

### `profile` field in `params`

_(Required to export training data for Neptune ML, unless the
`neptune_ml` field is present in the `additionalParams` field)_.

The `profile` parameter provides sets of pre-configured parameters
for specific workloads. At present, the export process only supports the
`neptune_ml` profile

If you are exporting training data for Neptune ML, add the following parameter
to the `params` object:

```
  "profile" : "neptune_ml"
```

### `useIamAuth` field in `params`

_(Optional)_. Default: `false`.

If the database from which you are exporting data has [IAM
authentication enabled](iam-auth-enable.md "iam-auth-enable.md"), you must include the `useIamAuth` parameter
set to `true`:

```
  "useIamAuth" : true
```

### `includeLastEventId` field in `params`

If you set `includeLastEventId` to true, and the database from which
you are exporting data has [Neptune Streams](streams-using.md "streams-using.md")
enabled, the export process writes a `lastEventId.json` file to your
specified export location. This file contains the `commitNum` and
`opNum` of the last event in the stream.

```
  "includeLastEventId" : true
```

A cloned database created by the export process inherits the streams setting
of its parent. If the parent has streams enabled, the clone will likewise have streams
enabled. The contents of the stream on the clone will reflect the contents of the
parent (including the same event IDs) at the point in time the clone was created.

## Fields for property-graph export

### `concurrency` field in `params`

_(Optional)_. Default: `4`.

The `concurrency` parameter specifies the number of parallel queries
that the export process should use:

```
  "concurrency" : `(for example, 24)`
```

A good guideline is to set the concurrency level to twice the number of vCPUs
on all the instances from which you are exporting data. An r5.xlarge instance, for example,
has 4 vCPUs. If you are exporting from a cluster of 3 r5.xlarge instances, you can set
the concurrency level to 24 (= 3 x 2 x 4).

If you are using the Neptune-Export service, the concurrency level is limited by
the [jobSize](export-parameters.md#export-parameters-jobSize "export-parameters.md#export-parameters-jobSize")
setting. A small job, for example, supports a concurrency level of 8.
If you try to specify a concurrency level of 24 for a small job using the
`concurrency` parameter, the effective level remains at 8.

If you export from a cloned cluster, the export process calculates an appropriate
concurrency level based on the size of the cloned instances and the job size.

### `edgeLabels` field in `params`

_(Optional)_.

Use `edgeLabels` to export only those edges that have labels that you
specify:

```
  "edgeLabels" : ["`(a label)`", "`(another label`"]
```

Each label in the JSON array must be a single, simple label.

The `scope` parameter takes precedence over the `edgeLabels`
parameter, so if the `scope` value does not include edges, the
`edgeLabels` parameter has no effect.

### `filter` field in `params`

_(Optional)_.

Use `filter` to specify that only nodes and/or edges with specific labels
should be exported, and to filter the properties that are exported for each node or edge.

The general structure of a `filter` object, either inline or in a
filter-configuration file, is as follows:

```
  "filter" : {
    "nodes": [ `(array of node label and properties objects)` ],
    "edges": [ `(array of edge definition an properties objects)` ]
  }
```

- **`nodes`**   –  
  Contains a JSON array of nodes and node properties in the following form:

```
    "nodes : [
      {
        "label": "`(node label)`",
        "properties": [ "`(a property name)`", "`(another property name)`", `( ... )` ]
      }
    ]
```

    + `label`  –  
     The node's property-graph label or labels.


    Takes a single value or, if the node has multiple labels,
     an array of values.
    + `properties`  –  
     Contains an array of the names of the node's properties
     that you want to export.

- **`edges`**   –  
  Contains a JSON array of edge definitions in the following form:

```
    "edges" : [
      {
        "label": "`(edge label)`",
        "properties": [ "`(a property name)`", "`(another property name)`", `( ... )` ]
      }
    ]
```

    + `label`   –  
     The edge's property graph label. Takes a single value.
    + `properties`  –  
     Contains an array of the names of the edge's properties that you want to export.

### `filterConfigFile` field in `params`

_(Optional)_.

Use `filterConfigFile` to specify a JSON file that contains a filter
configuration in the same form that the `filter` parameter takes:

```
  "filterConfigFile" : "s3://`(your Amazon S3 bucket)`/neptune-export/`(the name of the JSON file)`"
```

See [filter](#export-params-filter "#export-params-filter")
for the format of the `filterConfigFile` file.

### `format` field used for property-graph data in `params`

_(Optional)_. _Default_: `csv` (comma-separated values)

The `format` parameter specifies the output format of the exported
property graph data:

```
  "format" : `(one of: csv, csvNoHeaders, json, neptuneStreamsJson)`
```

- **`csv`**   –  
  Comma-separated value (CSV) formatted output, with column headings formatted
  according to the [Gremlin load
  data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").
- **`csvNoHeaders`**   –  
  CSV formatted data with no column headings.
- **`json`**   –  
  JSON formatted data.
- **`neptuneStreamsJson`**   –  
  JSON formatted data that uses the [GREMLIN_JSON
  change serialization format](streams-change-formats.md "streams-change-formats.md").

### `gremlinFilter` field in `params`

_(Optional)_.

The `gremlinFilter` parameter allows you to supply a Gremlin snippet,
such as a `has()` step, that is used to filter both nodes and edges:

```
  "gremlinFilter" : `(a Gremlin snippet)`
```

Field names and string values should be surrounded by escaped double quotes.
For dates and times, you can use the [datetime](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
method.

The following example exports only those nodes and edges with a date-created
property whose value is greater than 2021-10-10:

```
  "gremlinFilter" : "has(\"created\", gt(datetime(\"2021-10-10\")))"
```

### `gremlinNodeFilter` field in `params`

_(Optional)_.

The `gremlinNodeFilter` parameter allows you to supply a Gremlin snippet,
such as a `has()` step, that is used to filter nodes:

```
  "gremlinNodeFilter" : `(a Gremlin snippet)`
```

Field names and string values should be surrounded by escaped double quotes.
For dates and times, you can use the [datetime](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
method.

The following example exports only those nodes with a `deleted` Boolean
property whose value is `true`:

```
  "gremlinNodeFilter" : "has(\"deleted\", true)"
```

### `gremlinEdgeFilter` field in `params`

_(Optional)_.

The `gremlinEdgeFilter` parameter allows you to supply a Gremlin snippet,
such as a `has()` step, that is used to filter edges:

```
  "gremlinEdgeFilter" : `(a Gremlin snippet)`
```

Field names and string values should be surrounded by escaped double quotes.
For dates and times, you can use the [datetime](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
method.

The following example exports only those edges with a `strength`
numerical property whose value is 5:

```
  "gremlinEdgeFilter" : "has(\"strength\", 5)"
```

### `nodeLabels` field in `params`

_(Optional)_.

Use `nodeLabels` to export only those nodes that have labels you specify:

```
  "nodeLabels" : ["`(a label)`", "`(another label`"]
```

Each label in the JSON array must be a single, simple label.

The `scope` parameter takes precedence over the `nodeLabels`
parameter, so if the `scope` value does not include nodes, the `nodeLabels`
parameter has no effect.

### `scope` field in `params`

_(Optional)_. Default: `all`.

The `scope` parameter specifies whether to export only nodes, or
only edges, or both nodes and edges:

```
  "scope" : `(one of: nodes, edges, or all)`
```

- `nodes`   –   Export nodes and their properties only.
- `edges`   –   Export edges and their properties only.
- `all`   –   Export both nodes and edges and their properties (the default).

## Fields for RDF export

### `format` field used for RDF data in `params`

_(Optional)_. _Default_: `turtle`

The `format` parameter specifies the output format of the exported
RDF data:

```
  "format" : `(one of: turtle, nquads, ntriples, neptuneStreamsJson)`
```

- **`turtle`**   –  
  Turtle formatted output.
- **`nquads`**   –  
  N-Quads formatted data with no column headings.
- **`ntriples`**   –  
  N-Triples formatted data.
- **`neptuneStreamsJson`**   –  
  JSON formatted data that uses the [SPARQL NQUADS
  change serialization format](streams-change-formats.md "streams-change-formats.md").

### `rdfExportScope` field in `params`

_(Optional)_. Default: `graph`.

The `rdfExportScope` parameter specifies the scope of the RDF export:

```
  "rdfExportScope" : `(one of: graph, edges, or query)`
```

- `graph`   –   Export all RDF data.
- `edges`   –   Export only those triples that represent edges.
- `query`   –   Export data retrieved by
  a SPARQL query that issupplied using the `sparql` field.

### `sparql` field in `params`

_(Optional)_.

The `sparql` parameter allows you to specify a SPARQL query to
retrieve the data to export:

```
  "sparql" : `(a SPARQL query)`
```

If you supply a query using the `sparql` field, you must also set the
`rdfExportScope` field to `query`.

### `namedGraph` field in `params`

_(Optional)_.

The `namedGraph` parameter allows you to specify an IRI to limit the export to a single named graph:

```
  "namedGraph" : `(Named graph IRI)`
```

The `namedGraph` parameter can only be used with the `rdfExportScope` field set to
`graph`.
