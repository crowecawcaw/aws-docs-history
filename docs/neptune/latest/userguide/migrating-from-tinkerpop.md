# Migrating an existing graph from an Apache TinkerPop Gremlin server to Amazon Neptune

If you have graph data in an Apache TinkerPop Gremlin Server that you would like
to migrate to Amazon Neptune, you would take the following steps:

1. Export the data from Gremlin server into Amazon Simple Storage Service (Amazon S3).
2. Convert the exported data to a [CSV
   format that the Neptune bulk loader can import](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").
3. Using [Neptune Bulk Loader](bulk-load.md "bulk-load.md"),
   import the data into a Neptune DB cluster that you have prepared.
4. Modify your existing application to connect to Neptune's Gremlin endpoint,
   and make any changes necessary to conform with [Neptune Gremlin implementation
   differences](access-graph-gremlin-differences.md "access-graph-gremlin-differences.md").
