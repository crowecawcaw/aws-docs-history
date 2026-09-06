

# Index Property: name
<a name="index-property-name"></a>

## Supported index types
<a name="index-property-name-supported"></a>


| Option | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| single field | Yes | Yes | Yes | Yes | Yes | 
| compound | Yes | Yes | Yes | Yes | Yes | 
| multi-key | Yes | Yes | Yes | Yes | Yes | 
| text | No | No | Yes | Yes | No | 
| geospatial | Yes | Yes | Yes | Yes | Yes | 
| vector | No | No | Yes | Yes | No | 

Use the name option to provide an optional name for the index.

All examples use the following sample document:

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

## Single field
<a name="index-property-name-single-field"></a>

```
db.collection.createIndex(
  {
    "productId": 1
  },
  {
    "name": "single_field_index"
  }
)
```

## Compound
<a name="index-property-name-compound"></a>

```
db.collection.createIndex(
  {
    "productId": 1,
    "manufacturer": 1
  },
  {
    "name": "compound_index"
  }
)
```

## Multi-key
<a name="index-property-name-multi-key"></a>

```
db.collection.createIndex(
  {
    "tags": 1
  },
  {
    "name": "multikey_index"
  }
)
```

## Text
<a name="index-property-name-text"></a>

```
db.collection.createIndex(
  {
    "name": "text"
  },
  {
    "name": "text_index"
  }
)
```

## Geospatial
<a name="index-property-name-geospatial"></a>

```
db.collection.createIndex(
  {
    "supplier.location": "2dsphere"
  },
  {
    "name": "geospatial_index"
  }
)
```

## Vector
<a name="index-property-name-vector"></a>

```
db.runCommand({
  "createIndexes": "collection", 
  "indexes": [{
    "key": {
      "productEmbedding": "vector"
    },
    "name": "hnsw_index",
    "vectorOptions": {
      "type": "hnsw",
      "dimensions": 2,
      "similarity": "euclidean",
      "m": 16,
      "efConstruction": 64
    }
  }] 
})
```