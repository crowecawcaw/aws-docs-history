

# Wildcard indexes
<a name="indexes-wildcard"></a>

Amazon DocumentDB supports wildcard indexes beginning with Amazon DocumentDB 8.0.3.

Wildcard indexes store information from every field in a document, or from every field under a path that you specify. You do not need to know the field names when you create the index. If a field contains an embedded document or an array, the index includes every scalar value nested inside it.

Wildcard indexes are beneficial when:
+ Field names vary between documents in a collection, such as user-defined attributes or metadata.
+ You often query an embedded document whose subfields are not the same in every document.
+ You query many different fields, and creating a separate index for each field is not practical.

Wildcard indexes work best when field names vary between documents or change over time. When your queries use a small set of known fields, [single field](indexes-single-field.md) or [compound](indexes-compound.md) indexes on those fields provide the best performance. Because each wildcard index entry stores the full field path, a wildcard index can be larger when documents have long or deeply nested field names.

## Supported index properties
<a name="indexes-wildcard-properties"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0.3\+ | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| [name](index-property-name.md) | No | No | No | Yes | No | 
| [partialFilterExpression](index-property-partialfilterexpression.md) | No | No | No | Yes | No | 
| [wildcardProjection](#indexes-wildcard-projection) | No | No | No | Yes | No | 
| [hidden](index-property-hidden.md) | No | No | No | Yes | No | 

The `unique`, `sparse`, and `expireAfterSeconds` options are not supported on wildcard indexes. Wildcard indexes are sparse. They contain entries only for documents that have an indexed field, even if the field value is `null`.

## Creating a wildcard index
<a name="indexes-wildcard-creating"></a>

Use the `createIndex()` method to create a wildcard index. The method syntax is: `db.collection.createIndex(<key>, <options>)`

The `key` parameter is a JSON document that specifies the wildcard path and the index sort order:

```
{
  "<path>.$**": <1 (ascending)|-1 (descending)>
}
```

Use `{"$**": 1}` to index all fields in each document, or `{"a.$**": 1}` to index all fields under the field `a`. `$**` must be the last element of the path.

The `options` parameter is a JSON document that specifies the options for the index:

```
{
  "name": "<name>",
  "partialFilterExpression": <filter expression>,
  "wildcardProjection": <projection>
}
```

The following example creates a wildcard index on all fields under the `supplier` field:

```
db.collection.createIndex(
  {
    "supplier.$**": 1
  },
  {
    "name": "supplier_wildcard"
  }
)
```

## Wildcard projection
<a name="indexes-wildcard-projection"></a>

The `wildcardProjection` option lets you include or exclude fields from a wildcard index. Use it when you create a `{"$**": 1}` or `{"$**": -1}` index, or a compound wildcard index whose wildcard term is `$**`. In the projection, `1` includes a field and `0` excludes it. Include the fields that you query often to keep unneeded entries out of the index, or exclude fields that you never query.

The following example indexes all fields except `productEmbedding` and `reviews`:

```
db.collection.createIndex(
  {
    "$**": 1
  },
  {
    "name": "all_fields",
    "wildcardProjection": { "productEmbedding": 0, "reviews": 0 }
  }
)
```

The following rules apply to `wildcardProjection`:
+ You can use `wildcardProjection` only when the wildcard term is `$**`. You cannot use it when the wildcard term is a field path, such as `"supplier.$**"`.
+ You cannot mix inclusion and exclusion statements in one projection. The only exception is `_id`: you can exclude `_id` from an inclusion projection, such as `{a: 1, _id: 0}`, or include `_id` in an exclusion projection, such as `{a: 0, _id: 1}`.
+ The projection cannot be empty.
+ Wildcard indexes omit the `_id` field by default. To index `_id`, include `_id: 1` in the projection.
+ The index supports queries only on the fields that the projection covers. A query on any other field cannot use the index.

## Compound wildcard indexes
<a name="indexes-wildcard-compound"></a>

A compound wildcard index combines one wildcard term with one or more regular fields. Use it when your queries filter on a field that every document has, such as `manufacturer`, and also on fields whose names vary, such as the subfields of `supplier`.

The following example creates a compound index with a regular field and a wildcard field:

```
db.collection.createIndex(
  {
    "manufacturer": 1,
    "supplier.$**": 1
  },
  {
    "name": "manufacturer_supplier_wildcard"
  }
)
```

If the wildcard term is `$**`, you must specify a `wildcardProjection`. The projection applies only to the wildcard term. It selects which fields the wildcard term indexes. The fields that the projection includes must not overlap with the regular fields. If the projection is an exclusion, it must exclude every regular field. The following example indexes `manufacturer` as a regular field and every other field except `productEmbedding` and `reviews`:

```
db.collection.createIndex(
  {
    "manufacturer": 1,
    "$**": 1
  },
  {
    "name": "manufacturer_all_fields",
    "wildcardProjection": { "manufacturer": 0, "productEmbedding": 0, "reviews": 0 }
  }
)
```

The projection excludes `manufacturer`, but the index still indexes `manufacturer` as the regular field.

The following rules apply to compound wildcard indexes:
+ A compound wildcard index can have only one wildcard term. The wildcard term can be in any position.
+ You cannot include the same field in the wildcard term and in a regular field. For example, `{o: 1, "o.$**": 1}` is not allowed.
+ Regular fields in a compound wildcard index cannot be arrays.
+ Regular fields cannot include a numeric path component, such as `0` in `reviews.0.review_date`. For example, `{ "reviews.0.review_date": 1, "supplier.$**": 1 }` is not allowed.
+ A compound wildcard index cannot include a `text` or `2dsphere` field.
+ A query uses the index only if it includes a condition on the leading field of the index.

## Limitations
<a name="indexes-wildcard-limitations"></a>

A wildcard index can serve only one field in a query. If a `find` or `$match` filter has conditions on more than one field that the index includes, Amazon DocumentDB uses the index for the condition that appears first in the filter. It then checks the remaining conditions against the documents that the index returns. For best performance, put the condition that matches the fewest documents first.

For example, with a `{"supplier.$**": 1}` index, the following query uses the index for `supplier.supplierId`, and then checks `supplier.location.type` on each document that the index returns:

```
db.collection.find({
  "supplier.supplierId": "SUP4",
  "supplier.location.type": "Point"
})
```

Wildcard indexes do not support queries that use `$exists: true`. Amazon DocumentDB runs these queries with a collection scan.

Each wildcard index entry stores the full field path with the value, so the index key size limit applies to the field path and value together. An insert, update, or `createIndex` operation fails if an indexed field exceeds the limit. To avoid this, exclude fields that can hold large values from the index. For more information, see [Wildcard projection](#indexes-wildcard-projection).