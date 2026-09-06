

# Compound indexes
<a name="indexes-compound"></a>

Compound indexes store information from two or more fields in a collection of documents, allowing queries on the first field or any prefix fields. These indexes optimize performance for queries that filter on multiple fields simultaneously or combine filtering with sorting operations. They're also effective for single-condition queries on the leftmost indexed fields. The database leverages these index entries to efficiently locate matching documents without performing full collection scans.

Compound field indexes are beneficial when:
+ You need to filter on multiple fields simultaneously.
+ You need to combine filtering with sorting operations.

## Supported index properties
<a name="indexes-compound-properties"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| [name](index-property-name.md) | Yes | Yes | Yes | Yes | Yes | 
| [unique](index-property-unique.md) | Yes | Yes | Yes | Yes | Yes | 
| [sparse](index-property-sparse.md) \* | Yes | Yes | Yes | Yes | Yes | 
| [partialFilterExpression](index-property-partialfilterexpression.md) \* | No | No | Yes | Yes | No | 

\* The `sparse` and `partialFilterExpression` options cannot be used together in the same index definition. If you attempt to create an index with these options, it will fail with the following error:

```
Error in specification: cannot mix partialFilterExpression and sparse options
```

## Creating a compound index
<a name="indexes-compound-creating"></a>

Use the `createIndex()` method to create a compound index. The method syntax is: `db.collection.createIndex(<keys>, <options>)`

The `keys` parameter is a JSON document that specifies the fields and the index sort order:

```
{
  "<field 1>": <1 (ascending)|-1 (descending)>,
  "<field 2>": <1 (ascending)|-1 (descending)>,
  ...
}
```

Note that only one field can be an array in a compound index. If you attempt to create a compound index on two or more array fields, it will fail with the following error:

```
multiple fields of compound index cannot be arrays
```

The `options` parameter is a JSON document that specifies the options for the index:

```
{
  "name": "<name>",
  "unique": <true | false>,
  "sparse": <true | false>,
  "partialFilterExpression": <filter expression>
}
```

See [Index properties](index-properties.md) for examples of creating compound indexes.