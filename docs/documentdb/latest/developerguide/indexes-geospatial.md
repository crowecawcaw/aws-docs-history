# Geospatial Indexes

Geospatial indexes are a specialized type of index designed to efficiently query and manage geospatial data stored within a collection of documents. Amazon DocumentDB supports 2dsphere indexes, which are specifically designed to handle geospatial data on a sphere (like the Earth). This allows for accurate calculations and queries based on spherical geometry.

Geospatial indexes are beneficial when you need applications that need to perform location-based queries, such as:

- finding nearby points of interest,
- determining if a location falls within a specific area
- calculating distances between locations

## Supported index properties

| Option                                                                                                           | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster |
| ---------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --------------- |
| [name](index-property-name.md "index-property-name.md")                                                          | Yes | Yes | Yes | Yes | Yes             |
| [partialFilterExpression](index-property-partialfilterexpression.md "index-property-partialfilterexpression.md") | No  | No  | Yes | Yes | No              |

## Creating a geospatial index

Use the `createIndex()` method to create a geospatial index. The method syntax is: `db.collection.createIndex(<key>, <options>)`

The `key` parameter is a JSON document that specifies the field and 2dsphere index type:

```
{
  "<field>": "2dsphere"
}
```

The `options` parameter is a JSON document that specifies the options for the index:

```
{
  "name": "<name>",
  "partialFilterExpression": <filter expression>
}
```

See [Index Properties](index-properties.md "index-properties.md") for examples of creating geospatial indexes.
