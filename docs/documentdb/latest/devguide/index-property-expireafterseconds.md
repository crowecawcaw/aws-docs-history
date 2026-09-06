

# Index Property: expireAfterSeconds
<a name="index-property-expireafterseconds"></a>

## Supported index types
<a name="index-property-expireafterseconds-supported"></a>


| Index type | 3.6 | 4.0 | 5.0 | 8.0 | Elastic Cluster | 
| --- | --- | --- | --- | --- | --- | 
| single field | Yes | Yes | Yes | Yes | Yes | 
| multi-key | Yes | Yes | Yes | Yes | Yes | 

Use the expireAfterSeconds option to create a time to live (TTL) index. TTL indexes enable you to delete documents based on their age based on the timeout condition for each document. When a document reaches the specified TTL age, it is deleted from the collection.

For best practices with TTL deletes, see [TTL and time series workloads](best_practices.md#best_practices-ttl_timeseries).

## Examples
<a name="index-property-expireafterseconds-examples"></a>

The following examples show how to create TTL indexes on the following sample document:

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
      "rating": 4,
      "comment": "Good product"
    },
    {
      "review_date": ISODate('2024-03-15T14:22:33.120Z'),
      "rating": 5,
      "comment": "Excellent printer"
    },
    {
      "review_date": ISODate('2024-06-08T09:45:18.890Z'),
      "rating": 3,
      "comment": "Average quality"
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

**single field**

Create a TTL index on lastUpdated to delete documents that have not been updated in 90 days:

```
db.collection.createIndex(
  {
    "lastUpdated": 1
  },
  {
    "name": "lastUpdated_ttl",
    "expireAfterSeconds": 7776000
  }
)
```

**multi-key**

Create a TTL index on reviews.review\_date to delete documents that have had no reviews in the past year:

```
db.collection.createIndex(
  {
    "reviews.review_date": 1
  },
  {
    "name": "reviews_review_date_ttl",
    "expireAfterSeconds": 31536000
  }
)
```

Note that if the TTL index is on an array field, all items in the array are checked. If any timestamp in the array satisfies the timeout condition, the document will be deleted.