# Exporting data from a Neptune DB cluster

Neptune provides several ways to export data from your DB cluster, depending
on the data model, format, and scale of export you need.

**[Native
export to Amazon S3](neptune-native-export.md "neptune-native-export.md")**
Use the built-in Neptune export API to export RDF data directly
to Amazon S3 in N-Triples or N-Quads format. This is the simplest approach for
large-scale RDF exports because it requires no external infrastructure.

**[Exporting
query results to Amazon S3](exporting-gremlin.md "exporting-gremlin.md")**
Export the results of a Gremlin traversal directly to Amazon S3 using
the `call()` step. Use this when you need to export query results
that are too large to return as a response, or when you want to store Gremlin
query output for downstream processing.

**[External
neptune-export tool](neptune-export.md "neptune-export.md")**
Use the open-source [`neptune-export`](https://github.com/aws/neptune-export "https://github.com/aws/neptune-export")
tool – a separate application from Neptune that you deploy and operate
yourself – to export property graph or RDF data in CSV and other formats.
Can be run as a managed service (Neptune-Export service) or as a command-line
tool. Use this when you need CSV output or formats not yet supported by native
export.

For small amounts of data, you can also simply use the results of a query. For
RDF data, the [Graph Store Protocol
(GSP)](sparql-graph-store-protocol.md "sparql-graph-store-protocol.md") provides a simple way to export individual named graphs.

###### Topics

- [Native export for RDF data](neptune-native-export.md "neptune-native-export.md")
- [Exporting Gremlin query results to Amazon S3](exporting-gremlin.md "exporting-gremlin.md")
- [External neptune-export tool](neptune-export.md "neptune-export.md")
