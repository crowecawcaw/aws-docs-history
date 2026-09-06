

# Single field indexes
<a name="indexes-single-field"></a>

Single field indexes store information from any single field in a collection of documents. By default, all collections have an index on the `_id` field. You can add additional indexes to speed up important queries and operations.

Single field indexes are beneficial when:
+ Your application frequently queries or filters documents based on the values of a specific field.
+ You need to efficiently sort documents by a particular field.
+ You want to ensure uniqueness for a specific field across documents in a collection by creating a unique index.

## Supported index properties
<a name="indexes-single-field-properties"></a>


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

## Creating a single field index
<a name="indexes-single-field-creating"></a>

Use the `createIndex()` method to create a single field index. The syntax is: `db.collection.createIndex(<key>, <options>)`.

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

See [Index properties](index-properties.md) for examples of creating single field indexes.