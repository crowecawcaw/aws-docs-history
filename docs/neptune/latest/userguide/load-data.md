

# Loading data into Amazon Neptune
<a name="load-data"></a>

There are several different ways to load graph data into Amazon Neptune:
+ If you only need to load a relatively small amount of data, you can use queries such as SPARQL `INSERT` statements or Gremlin `mergeV` and `mergeE` steps. openCypher also includes `CREATE` and `MERGE` clauses.
+ You can take advantage of [Neptune Bulk Loader](bulk-load.md) to ingest large amounts of data that reside in external files. The bulk loader command is faster and has less overhead than the query-language commands. It is optimized for large datasets, and supports both RDF (Resource Description Framework) data and Gremlin data.
+ You can use AWS Database Migration Service (AWS DMS) to import data from other data stores (see [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md), and [AWS Database Migration Service User Guide](https://docs.aws.amazon.com/dms/latest/userguide/)).
+ For smaller datasets in one or a few Amazon S3 files, you can use query-based loading functions to read and process data directly within your queries. See [Loading data into Amazon Neptune using queries](load-data-via-query.md) for more details.

**Topics**
+ [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md)
+ [Using AWS Database Migration Service to load data into Amazon Neptune from a different data store](dms-neptune.md)
+ [Loading data into Amazon Neptune using queries](load-data-via-query.md)