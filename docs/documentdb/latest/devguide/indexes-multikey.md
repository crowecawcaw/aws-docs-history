

# Multi-key indexes
<a name="indexes-multikey"></a>

For fields that have an array value, a multi-key index allows you to create an index key for each element in the array. Indexing an array creates an index entry for each element of the array.

Multi-key indexes are beneficial when your application frequently queries or filters documents based on values in arrays.

## Supported index properties
<a name="indexes-multikey-properties"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| [name](index-property-name.md) | Yes | Yes | Yes | Yes | Yes | 
| [unique](index-property-unique.md) | Yes | Yes | Yes | Yes | Yes | 
| [sparse](index-property-sparse.md) \* | Yes | Yes | Yes | Yes | Yes | 
| [partialFilterExpression](index-property-partialfilterexpression.md) \* | No | No | Yes | Yes | No | 
| [expireAfterSeconds](index-property-expireafterseconds.md) | Yes | Yes | Yes | Yes | Yes | 

\* The `sparse` and `partialFilterExpression` options cannot be used together in the same index definition. If you attempt to create an index with these options, it will fail with the following error:

```
Error in specification: cannot mix partialFilterExpression and sparse options
```

## Creating a multi-key index
<a name="indexes-multikey-creating"></a>

Use the `createIndex()` method to create a multi-key index. The method syntax is: `db.collection.createIndex(<key>, <options>)`

The `key` parameter is a JSON document that specifies the field and the index sort order:

```
{
  "<field>": <1 (ascending)|-1 (descending)>
}
```

The `options` parameter is a JSON document that specifies the options for the index:

```
{
  "name": "<name>",
  "unique": <true | false>,
  "sparse": <true | false>,
  "partialFilterExpression": <filter expression>,
  "expireAfterSeconds": <seconds before expiry>
}
```

The following example creates a multi-key index on the `categories` field sorted in ascending order with the name `book_categories`:

```
db.collection.createIndex(
  {
    "categories": 1
  },
  {
    "name": "book_categories"
  }
)
```

See [Index properties](index-properties.md) for examples of creating multi-key indexes.