

# Loading data into Amazon Neptune using queries

Neptune supports writing data directly through query language operations. You can use standard write operations like `CREATE` and `MERGE` in openCypher, `INSERT` in SPARQL, or `mergeV()` and `mergeE()` in Gremlin to add or modify data in your graph. These operations are suitable for incremental updates and transactional writes.

For loading data from Amazon S3, use the [Using the Amazon Neptune bulk loader to ingest data](bulk-load.md) for large datasets requiring optimized performance. For smaller datasets in one or a few Amazon S3 files, you can use query-based loading functions to read and process data directly within your queries.

The following query-based loading functions are available:

## openCypher: neptune.read()
<a name="opencypher-neptune-read"></a>

The `neptune.read()` function reads CSV or Parquet files from Amazon S3 within a `CALL` subquery, allowing you to process and load data at query time.

```
CALL neptune.read({
  source: "s3://bucket/data.csv",
  format: "csv"
})
YIELD row
CREATE (n:Person {id: row.id, name: row.name})
```

For complete documentation, see [neptune.read()](access-graph-opencypher-21-extensions-s3-read.md).

## SPARQL: LOAD and UNLOAD
<a name="sparql-load-unload"></a>

SPARQL `LOAD` operations import RDF data from a URI into a named graph. `UNLOAD` is the counterpart operation: it removes the data that a remote source file contains from a named graph.

```
LOAD <s3://bucket/data.ttl> INTO GRAPH <http://example.org/graph>
```

For more information about each operation, see [Using SPARQL UPDATE LOAD to import data into Neptune](sparql-api-reference-update-load.md) and [Using SPARQL UPDATE UNLOAD to delete data from Neptune](sparql-api-reference-unload.md).

## Gremlin: io() step
<a name="gremlin-io-step"></a>

You can also use Gremlin's `g.io(URL).read()` step to read in data files in [GraphML](https://tinkerpop.apache.org/docs/current/dev/io/#graphml) (an XML format), [GraphSON](https://tinkerpop.apache.org/docs/current/dev/io/#graphson) (a JSON format), and other formats.

```
g.io("https://example.com/data/my-graph.graphml").read().iterate()
```

Use the `g.io()` step to read from an HTTPS URL. To load a file that you store as an Amazon S3 object, first generate a presigned URL. Then pass that HTTPS URL to `g.io()`. You can generate a presigned URL with the AWS CLI `aws s3 presign` command:

```
aws s3 presign s3://amzn-s3-demo-bucket/data/vertices.graphml
```

A presigned URL ends with a query string and has no file extension, so `g.io()` cannot detect the file format automatically. Specify the format explicitly with the `IO.reader` option. The following Gremlin command substitutes the presigned URL from the preceding command into `g.io()` and reads it as GraphML:

```
g.io("https://amzn-s3-demo-bucket.s3.amazonaws.com/data/vertices.graphml?X-Amz-Algorithm=...&X-Amz-Signature=...").with(IO.reader, IO.graphml).read().iterate()
```

For a GraphSON file, use `IO.graphson` as the reader.

For more information about presigned URLs, see [Download and upload objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) in the *Amazon S3 User Guide*.

 See [TinkerPop documentation](https://tinkerpop.apache.org/docs/current/reference/#io-step) for details.