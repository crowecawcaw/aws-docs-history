# Loading data into Amazon Neptune

There are several different ways to load graph data into Amazon Neptune:

- If you only need to load a relatively small amount of data, you can
  use queries such as SPARQL `INSERT` statements or Gremlin
  `addV` and `addE` steps.
- You can take advantage of [Neptune Bulk Loader](bulk-load.md "bulk-load.md") to ingest large amounts of data that reside
  in external files. The bulk loader command is faster and has less overhead than
  the query-language commands. It is optimized for large datasets, and supports
  both RDF (Resource Description Framework) data and Gremlin data.
- You can use AWS Database Migration Service (AWS DMS) to import data from other data stores
  (see [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md "dms-neptune.md"), and [AWS Database Migration Service User Guide](../../../dms/latest/userguide.md "../../../dms/latest/userguide.md")).
- Finally, you can use Gremlin's `g.io(URL).read()`
  step to read in data files in [GraphML](https://tinkerpop.apache.org/docs/current/dev/io/#graphml "https://tinkerpop.apache.org/docs/current/dev/io/#graphml")
  (an XML format), [GraphSON](https://tinkerpop.apache.org/docs/current/dev/io/#graphson "https://tinkerpop.apache.org/docs/current/dev/io/#graphson")
  (a JSON format), and other formats. See [TinkerPop
  documentation](https://tinkerpop.apache.org/docs/current/reference/#io-step "https://tinkerpop.apache.org/docs/current/reference/#io-step") for details.

###### Topics

- [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md "bulk-load.md")
- [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md "dms-neptune.md")
