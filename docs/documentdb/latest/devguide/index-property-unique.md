

# Index Property: unique
<a name="index-property-unique"></a>

## Supported index types
<a name="index-property-unique-supported"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| single field | Yes | Yes | Yes | Yes | Yes | 
| compound | Yes | Yes | Yes | Yes | Yes | 
| multi-key | Yes | Yes | Yes | Yes | Yes | 

Use the unique option to ensure uniqueness for the field(s) across documents in a collection.

## Examples
<a name="index-property-unique-examples"></a>

The following examples show how to create unique indexes on the following sample document:

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

Create a unique single field index on productId to ensure that the same productId does not exist in more than 1 document:

```
db.collection.createIndex(
  {
    "productId": 1
  },
  {
    name: "productId_unique",
    unique: true
  }
)
```

Compound

Create a unique compound index on sku and manufacturer to ensure that the same combination of sku and manufacturer does not exist in more than 1 document:

```
db.collection.createIndex(
  {
    "sku": 1,
    "manufacturer": 1
  },
  {
    name: "sku_and_manufacturer_unique",
    unique: true
  }
)
```

multi-key

Create a unique multi-key index on barcodes to ensure that any value in the barcodes array does not exist in more than 1 document:

```
db.collection.createIndex(
  {
    "barcodes": 1
  },
  {
    name: "barcodes_unique",
    unique: true
  }
)
```

Indexing an array creates an index entry for each element of the array. For example, if an array has 50 items, it has 50 index entries. Because of this, unique multi-key indexes enforce uniqueness across all individual items. For example, the following documents will violate the unique constraint on the values array field index:

```
{ "values": [ 1, 2, 3] }
{ "values": [ 3, 2 ] }   --> 3 and 2 already exist
{ "values": [ 1 ] }      --> 1 already exists
```

Note the following behavior with unique indexes:

1. If you create a unique index on existing data where two (or more) documents have the same values for the indexed fields, the index build will fail with the following error: `could not create unique index: <collection> index: <index name>`

1. If you insert a document where the value of the indexed field matches the value of that field in another document, the insert will fail with the following error: `E11000 duplicate key error collection: <collection> index: <index name>`

1. If you update an existing document so the new value of the indexed field matches the value of that field in another document, the update will fail with the following error: `E11000 duplicate key error collection: <collection> index: <index name>`

1. If the indexed field is missing from a document, the value will be treated as null. Index builds, inserts, and updates will fail as described above if the indexed field is missing from two (or more) documents.