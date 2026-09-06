

# Index Property: sparse
<a name="index-property-sparse"></a>

## Supported index types
<a name="index-property-sparse-supported"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| single field | Yes | Yes | Yes | Yes | Yes | 
| compound | Yes | Yes | Yes | Yes | Yes | 
| multi-key | Yes | Yes | Yes | Yes | Yes | 

Use the sparse option to skip indexing documents missing the indexed field(s), reducing the index size and saving space in memory. Because the index size is smaller, the queries that use it are more efficient. For a query to utilize a sparse index, you must use the $exists clause on the indexed fields. If you omit the $exists clause, Amazon DocumentDB will not use the sparse index.

## Examples
<a name="index-property-sparse-examples"></a>

The following examples show how to create sparse indexes on the following sample document:

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

Note that the reviews, material, and color fields do not exist in all documents.

single field

Create a sparse single field index on the material field:

```
db.collection.createIndex(
  {
    "material": 1
  },
  {
    "name": "material_sparse",
    "sparse": true
  }
)
```

This index will be used when finding all products that have a value for material:

```
db.collection.find({
  "material": {
    $exists: true
  }
})
```

compound

Create a sparse compound index on the material and color fields:

```
db.collection.createIndex(
  {
    "material": 1,
    "color": 1
  },
  {
    "name": "material_and_color_sparse",
    "sparse": true
  }
)
```

This index will be used when finding all products that have any combination of material and color values:

```
db.collection.find({
  "material": {
    $exists: true
  }
})

db.collection.find({
  "color": {
    $exists: true
  }
})

db.collection.find({
  $and: [
    {
      "material": {
        $exists: true
      }
    },
    {
      "color": {
        $exists:true
      }
    }
  ]
})

db.collection.find({
  $and: [
    {
      "color": {
        $exists: true
      }
    },
    {
      "material": {
        $exists:true
      }
    }
  ]
})
```

multi-key

Create a sparse multi-key index on the reviews array:

```
db.collection.createIndex(
  {
    "reviews": 1
  },
  {
    "name": "reviews_sparse",
    "sparse": true
  }
)
```

This index will be used when finding all products that have a reviews array:

```
db.collection.find({
  "reviews": {
    $exists: true
  }
})
```