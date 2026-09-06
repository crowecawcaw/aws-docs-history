

# Index Property: partialFilterExpression
<a name="index-property-partialfilterexpression"></a>

## Supported index types
<a name="index-property-partialfilterexpression-supported"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| single field | No | No | Yes | Yes | No | 
| compound | No | No | Yes | Yes | No | 
| multi-key | No | No | Yes | Yes | No | 
| geospatial | No | No | No | No | No | 

Use the partialFilterExpression option to create a partial index that only includes documents that meet a specified filter condition. This allows you to create more efficient indexes by indexing only a subset of documents in a collection, rather than indexing all documents, reducing the index size and saving space in memory. Because the index size is smaller, the queries that use it are more efficient. Amazon DocumentDB will use the partial index in the following scenarios:
+ The query predicate exactly matches the partial index filter expression.
+ The query filter's expected result is a logical subset of the partial filter.
+ A sub-predicate of the query can be used in conjunction with other indexes.

For more information, see [Partial index](partial-index.md).

## Examples
<a name="index-property-partialfilterexpression-examples"></a>

The following examples show how to create partial indexes on the following sample document:

```
{
  "productId": "PROD133726",
  "sku": "SKU24224",
  "name": "Basic Printer",
  "manufacturer": "The Manufacturer",
  "tags": [ "printer", "basic", "electronics", "business" ],
  "barcodes": [ "542364671", "886330670", "437445606" ],
  "reviews": [
    {
      "review_date": ISODate('2024-01-19T21:37:10.585Z'),
      ...
    }
  ],
  "material": "Polycarbonate",
  "color": "Space Gray",
  "supplier": {
    "supplierId": "SUP4",
    "location": {
      "type": "Point",
      "coordinates": [ -71.0589, 42.3601 ]
    }
  },
  "productEmbedding": [
    -0.019320633663838058,
    0.019672111388113596
  ],
  "lastUpdated": ISODate('2025-10-20T21:37:10.585Z')
}
```

single field

Create a partial single field index on manufacturer for products that have a color of Space Gray:

```
db.collection.createIndex(
  {
    "manufacturer": 1
  },
  {
    "name": "manufacturer_space_gray",
    "partialFilterExpression": {
      "color": {
        $eq: "Space Gray"
      }
    }
  }
)
```

This index will be used when finding Space Gray color products by manufacturer:

```
db.collection.find({
  "manufacturer": "The Manufacturer",
  "color": {
    $eq: "Space Gray"
  }
})
```

compound

Create a partial compound index on manufacturer and color for products that have a material of Polycarbonate:

```
db.collection.createIndex(
  {
    "manufacturer": 1,
    "color": 1
  },
  {
    "name": "manufacturer_and_color_polycarbonate",
    "partialFilterExpression": {
      "material": {
        $eq: "Polycarbonate"
      }
    }
  }
)
```

This index will be used when finding Polycarbonate material products by manufacturer and color:

```
db.collection.find({
  "manufacturer": "The Manufacturer",
  "color": "Space Gray",
  "material": {
    $eq: "Polycarbonate"
  }
})
```

multi-key

Create a partial multi-key index on tags for products that have a manufacturer of The Manufacturer:

```
db.collection.createIndex(
  {
    "tags": 1
  },
  {
    "name": "tags_the_manufacturer",
    "partialFilterExpression": {
      "manufacturer": {
        $eq: "The Manufacturer"
      }
    }
  }
)
```

This index will be used when finding products tagged with printer that have a manufacturer of The Manufacturer:

```
db.collection.find({
  "tags": "printer",
  "manufacturer": {
    $eq: "The Manufacturer"
  }
})
```