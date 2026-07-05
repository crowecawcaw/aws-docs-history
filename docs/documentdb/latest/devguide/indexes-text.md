# Text indexes

Text indexes are useful in searching for words or phrases in text fields within documents, allowing you to perform full-text search functionality. You can create single field text indexes or compound text indexes with more than one text field. However, you can only have one text index per collection. For more information, see [Performing text search with Amazon DocumentDB](text-search.md "text-search.md").

## Supported index properties

| Option                                                  | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster |
| ------------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [name](index-property-name.md "index-property-name.md") | No  | No  | Yes | Yes | No              |

## Creating a text index

Use the `createIndex()` method to create a text index. The method syntax is: `db.collection.createIndex(<keys>, <options>)`

The `keys` parameter is a JSON document that specifies the field(s) and text index type:

```
{
  "<field 1>": "text",
  "<field 2>": "text"
}
```

The `options` parameter is a JSON document that specifies the name of the index:

```
{
  "name": "<name>"
}
```

See [Index properties](index-properties.md "index-properties.md") for examples of creating text indexes.
