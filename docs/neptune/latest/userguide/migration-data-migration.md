# Data migration from Neo4j to Neptune

When performing a migration from Neo4j to Amazon Neptune, migrating the data is a
major step in the process. There are multiple approaches to migrating data. The correct
approach is determined by the needs of the application, the data size, and the type of
migration desired. However, many of these migrations all require assessment of the same
considerations, of which several are highlighted below.

###### Note

See the [Migrating
a Neo4j graph database to Neptune with a fully automated utility](https://aws.amazon.com/blogs/database/migrating-a-neo4j-graph-database-to-amazon-neptune-with-a-fully-automated-utility/ "https://aws.amazon.com/blogs/database/migrating-a-neo4j-graph-database-to-amazon-neptune-with-a-fully-automated-utility/") in the
[AWS
Database Blog](https://aws.amazon.com/blogs/?awsf.blog-master-category=category%23database "https://aws.amazon.com/blogs/?awsf.blog-master-category=category%23database") for a complete, step-by-step walkthrough of one example of how
to perform an offline data migration.

## Assessing data migration from Neo4j to Neptune

The first step when assessing any data migration is to determine how you will
migrate the data. The options depend on the architecture of the application being
migrated, the data size, and the availability needs during the migration. In general,
migrations tend to fall into one of two categories: online or offline.

Offline migrations tend to be the simplest to accomplish, because the application
doesn't accept read or write traffic during the migration. After the application stops
accepting traffic, the data can be exported, optimized, imported, and the application
tested before the application is re-enabled.

Online migrations are more complex, because the application still needs to accept
read and write traffic while the data is being migrated. The exact needs of each online
migration may differ, but the general architecture would generally be similar to the
following:

- A feed of ongoing changes to the database needs to be enabled in
  Neo4j by configuring [Neo4j
  Streams as a source to a Kafka cluster](https://neo4j.com/labs/kafka/4.0/producer/ "https://neo4j.com/labs/kafka/4.0/producer/").
- Once this is completed, an export of the running system can be
  taken, following the instructions in [Exporting data from Neo4j when migrating to Neptune](#migration-data-exporting "#migration-data-exporting"), and the time noted for later
  correlation to the Kafka topic.
- The exported data is then imported into Neptune, following
  instructions in [Importing data from Neo4j when migrating to Neptune](#migration-data-importing "#migration-data-importing").
- Changed data from the Kafka stream can then be copied to the
  Neptune cluster using an architecture similar to the one described in
  [Writing
  to Amazon Neptune from Amazon Kinesis Data Streams](https://github.com/aws-samples/amazon-neptune-samples/tree/master/gremlin/stream-2-neptune "https://github.com/aws-samples/amazon-neptune-samples/tree/master/gremlin/stream-2-neptune"). Note that the
  changes replication can be run in parallel to validate the new application
  architecture and performance.
- After the data migration is validated, then the application
  traffic can be redirected to the Neptune cluster and the Neo4j instance
  can be decommissioned.

## Data-model optimizations for migrating from Neo4j to Neptune

Both Neptune and Neo4j support labeled property graphs (LPG). However, Neptune
has some architectural and data-model differences that you can take advantage of to
optimize performance:

### Optimizing node and edge IDs

Neo4j automatically generates numeric long IDs. Using Cypher you can refer
to nodes by ID, but this is generally discouraged in favor of looking up nodes
by an indexed property.

Neptune allows you to [supply
your own string-based IDs for vertices and edges](access-graph-gremlin-differences.md#feature-gremlin-differences-user-supplied-ids "access-graph-gremlin-differences.md#feature-gremlin-differences-user-supplied-ids"). If you don't supply your own
IDs, Neptune automatically generates string representations of UUIDs for new edges
and vertices.

If you migrate data from Neo4j to Neptune by exporting from Neo4j and then bulk
importing into Neptune, you can preserve Neo4j's IDs. The numeric values generated
by Neo4j can act as user-supplied IDs when importing into Neptune, where they are
represented as strings rather than numeric values.

However, there are circumstances in which you may want to promote a vertex
property to become a vertex ID. Just as looking up a node using an indexed property
is the fastest way to find a node in Neo4j, looking up a vertex by ID is the
fastest way to find a vertex in Neptune. Therefore, if you can identify a
suitable vertex property that contains unique values, you should consider
replacing the vertex ~id with the nominated property value in your bulk load
CSV files. If you do this, you will also have to rewrite any corresponding
~from and ~to edge values in your CSV files.

### Schema constraints when migrating data from Neo4j to Neptune

Within Neptune, the only schema constraint available is the uniqueness of the
ID of a node or edge. Applications that need to leverage a uniqueness constraint
are encouraged to look at this approach for achieving a uniqueness constraint
through specifying the node or edge ID. If the application used multiple columns
as a uniqueness constraint, the ID may be set to a combination of these values.
For instance, `id=123, code='SEA'` could be represented as
`ID='123_SEA'`) to achieve a complex uniqueness constraint.

### Edge direction optimization when migrating data from Neo4j to Neptune

When nodes, edges, or properties are added to Neptune,they are automatically
[indexed in three different ways](feature-overview-storage-indexing.md "feature-overview-storage-indexing.md"),
with an [optional fourth index](features-lab-mode.md#features-lab-mode-features-osgp-index "features-lab-mode.md#features-lab-mode-features-osgp-index").
Because of how Neptune builds and [uses
the indices](feature-overview-storage-indexing.md "feature-overview-storage-indexing.md"), queries that follow outgoing edges are more efficient than ones
that use incoming edges. In terms of Neptune's [graph
data storage model](feature-overview-data-model.md "feature-overview-data-model.md"), these are subject-based searches that use the SPOG index.

If, in migrating your data model and queries to Neptune, you find that your most
important queries rely on traversing incoming edges where there is a high degree of
fan out, you may want to consider altering your model so that these traversals follow
outgoing edges instead, especially when you cannot specify which edge labels to traverse.
To do so, reverse the direction of the relevant edges and update the edge labels to reflect
the semantics of this direction change. For example, you might change:

```
person_A — parent_of — person_B
   to:
person_B — child_of — person_A
```

To make this change in a [bulk-load edge
CSV file](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md"), simply swap the `~from` and `~to` column headings,
and update the values of the `~label` column.

As an alternative to reversing edge direction, you can enable a [fourth Neptune index, the OSGP index](feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp "feature-overview-storage-indexing.md#feature-overview-storage-indexing-osgp"),
which makes traversing incoming edges, or object-based searches, much more efficient.
However, enabling this fourth index will lower insert rates and require more storage.

### Filtering optimization when migrating data from Neo4j to Neptune

Neptune is optimized to work best when properties are filtered to the most
selective property available. When multiple filters are used, the set of matching
items is found for each and then the overlap of all matching sets is calculated.
When possible, combining multiple properties into a single property minimizes
the number of index lookups and decreases the latency of a query.

For example, this query uses two index look-ups and a join:

```
MATCH (n) WHERE n.first_name='John' AND n.last_name='Doe' RETURN n
```

This query retrieves the same information using a single index look-up:

```
MATCH (n) WHERE n.name='John Doe' RETURN n
```

###

Neptune supports [different data types](bulk-load-tutorial-format-opencypher.md#bulk-load-tutorial-format-opencypher-data-types "bulk-load-tutorial-format-opencypher.md#bulk-load-tutorial-format-opencypher-data-types") than Neo4j does.

###### Neo4j data-type mappings into data types that Neptune supports

- **Logical**:   `Boolean`

Map this in Neptune to `Bool` or `Boolean`.

- **Numeric**:   `Number`

Map this in Neptune to the narrowest of the following Neptune openCypher types
that can support all values of the numeric property in question:

```
  Byte
  Short
  Integer
  Long
  Float
  Double
```

- **Text**:   `String`

Map this in Neptune to `String`.

- **Point in time**:

```
  Date
  Time
  LocalTime
  DateTime
  LocalDateTime
```

Map these in Neptune to `Date` as UTC, using one of
the following ISO-8601 formats that Neptune supports:

```
  yyyy-MM-dd
  yyyy-MM-ddTHH:mm
  yyyy-MM-ddTHH:mm:ss
  yyyy-MM-ddTHH:mm:ssZ
```

- **Time duration**:   `Duration`

Map this in Neptune to a numeric value for date arithmetic, if necessary.

- **Spatial**:   `Point`

Map this in Neptune into component numeric values, each of which then becomes
a separate property, or express as a String value to be interpreted by the client
application. Note that Neptune's [full-text
search](full-text-search.md "full-text-search.md") integration using OpenSearch lets you index geolocation properties.

### Migrating multivalued properties from Neo4j to Neptune

Neo4j allows [homogeneous
lists of simple types](https://neo4j.com/docs/cypher-manual/current/values-and-types/ "https://neo4j.com/docs/cypher-manual/current/values-and-types/") to be stored as properties of both nodes and edges. These
lists can contain duplicate values.

Neptune, however, allows only [set
or single cardinality](access-graph-gremlin-differences.md#feature-gremlin-differences-vertex-property-cardinality "access-graph-gremlin-differences.md#feature-gremlin-differences-vertex-property-cardinality") for vertex properties, and single cardinality for edge
properties in property graph data. As a result, there is no straightforward migration
of Neo4j node list properties that contain duplicate values into Neptune vertex
properties, or of Neo4j relationship-list properties into Neptune edge properties.

Some possible strategies for migrating Neo4j multivalued node properties with
duplicate values into Neptune are as follows:

- Discard the duplicate values and convert the multivalued Neo4j node
  property to a set cardinality Neptune vertex property. Note that the Neptune
  set may not then reflect the order of items in the original Neo4j multivalued
  property.
- Convert the multivalued Neo4j node property to a string representation
  of a JSON-formatted list in a Neptune vertex string property.
- Extract each of the multivalued property values into a separate vertex
  with a value property, and connect those vertices to the parent vertex using an edge
  labelled with the property name.

Similarly, possible strategies for migrating Neo4j multivalued relationship properties
into Neptune are as follows:

- Convert the multivalued Neo4j relationship property to a string
  representation of a JSON-formatted list and store it as a Neptune edge string
  property.
- Refactor the Neo4j relationship into incoming and outgoing Neptune
  edges attached to an intermediate vertex. Extract each of the multivalued
  relationship property values into a separate vertex with a value property and
  those vertices to this intermediate vertex using an edge labelled with the property
  name.

Note that a string representation of a JSON-formatted list is opaque to the
openCypher query language, although openCypher includes a `CONTAINS`
predicate that allows for simple searches inside string values.

## Exporting data from Neo4j when migrating to Neptune

When exporting data from Neo4j, use the APOC procedures to export either to [CSV](https://neo4j.com/labs/apoc/4.1/export/csv/ "https://neo4j.com/labs/apoc/4.1/export/csv/") or to [GraphML](https://neo4j.com/labs/apoc/4.1/export/graphml/ "https://neo4j.com/labs/apoc/4.1/export/graphml/").
Although it's possible to export to other formats, there are [open-source
tools](https://github.com/awslabs/amazon-neptune-tools/tree/master/neo4j-to-neptune "https://github.com/awslabs/amazon-neptune-tools/tree/master/neo4j-to-neptune") for converting CSV data exported from Neo4j to Neptune bulk-load
format, and also [open-source
tools](https://github.com/awslabs/amazon-neptune-tools/tree/master/graphml2csv "https://github.com/awslabs/amazon-neptune-tools/tree/master/graphml2csv") for converting GraphML data exported from Neo4j to Neptune bulk-load
format.

You can also export data directly into Amazon S3 using the various APOC procedures.
Exporting to an Amazon S3 bucket is disabled by default, but it can be enabled using the
procedures highlighted in [Exporting
to Amazon S3](https://neo4j.com/labs/apoc/4.3/export/csv/#export-csv-s3-export "https://neo4j.com/labs/apoc/4.3/export/csv/#export-csv-s3-export") in the Neo4j APOC documentation.

## Importing data from Neo4j when migrating to Neptune

You can import data into Neptune either by using the [Neptune
bulk loader](bulk-load.md "bulk-load.md") or by using application logic in a supported query language such as
[openCypher](access-graph-opencypher.md "access-graph-opencypher.md").

The Neptune bulk loader is the preferred approach to importing large amounts
of data because it provides optimized import performance if you follow [best practices](bulk-load-optimize.md "bulk-load-optimize.md"). The bulk loader supports [two different CSV formats](bulk-load-tutorial-format.md "bulk-load-tutorial-format.md"), to which
data exported from Neo4j can be converted using the the open-source utilities
mentioned above in the [Exporting data](#migration-data-exporting "#migration-data-exporting") section.

You can also use openCypher to import data with custom logic for parsing,
transforming, and importing. You can submit the openCypher queries either through
the [HTTPS endpoint](access-graph-opencypher-queries.md "access-graph-opencypher-queries.md")
(which is recommended) or by using the [bolt driver](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md").
