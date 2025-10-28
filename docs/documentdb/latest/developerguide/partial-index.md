# Partial index

A partial index indexes documents in a collection that meets a specified filter criterion.
The partial index feature is supported in Amazon DocumentDB 5.0 instance-based clusters.

###### Topics

- [Create a partial index](#create-partial-index "#create-partial-index")
- [Supported operators](#partial-index-operators "#partial-index-operators")
- [Query using a partial index](#partial-index-query "#partial-index-query")
- [Partial index functionalities](#partial-index-functionalities "#partial-index-functionalities")
- [Partial index limitations](#partial-index-limitations "#partial-index-limitations")

## Create a partial index

To create a partial index, use the `createIndex()` method with the `partialFilterExpression` option.
For example, the following operation creates a unique compound index in the orders collection that indexes documents having an `OrderID` and having the `isDelivered` field as true:

```
db.orders.createIndex(
  {"category": 1, "CustomerId": 1, "OrderId": 1},
  {"unique": true, "partialFilterExpression":
    {"$and": [
      {"OrderId": {"$exists": true}},
      {"isDelivered": {"$eq": false}}
    ]}
  }
)
```

## Supported operators

- **$eq**
- **$exists**
- **$and** (only at top-level)
- **$gt/$gte/$lt/$lte** (index scan is only used when the filter, predicated in the query, matches the partial filter expression exactly) (See Limitations)

## Query using a partial index

The following query patterns are possible using partial indexes:

- The query predicate exactly matches the partial index filter expression:

```
db.orders.find({"$and": [
    {"OrderId": {"$exists": true}},
    {"isDelivered": {"$eq": false}}
  ]}).explain()
```

- The query filter’s expected result is a logical subset of the partial filter:

```
db.orders.find({"$and": [
    {"OrderId": {"$exists": true}},
    {"isDelivered": {"$eq": false}},
    {"OrderAmount": {"$eq": "5"}}
  ]}).explain()
```

- A sub-predicate of the query can be used in conjunction with other indexes:

```
db.orders.createIndex({"anotherIndex":1})
db.orders.find({ "$or": [
      {"$and": [
        {"OrderId": {"$exists": true}},
        {"isDelivered": {"$eq": false}}
      ]},
      {"anotherIndex": {"$eq": 5}}
    ]
  }).explain()
```

###### Note

A query planner may opt to use a collection scan rather than an index scan if it is efficient to do so.
This is typically seen for very small collections or queries that would return a large portion of a collection.

## Partial index functionalities

**List partial indexes**

List partial indexes with partialFilterExpression using the `getIndex` operation.
For example, the `getIndex` operation issued in lists partial indexes with key, name, and partialfilterExpressions fields:

```
db.orders.getIndexes()
```

This example returns the following output:

```
[
  {
    "v" : 4,
    "key" : {
      "_id" : 1
    },
    "name" : "_id_",
    "ns" : "ecommerceApp.orders"
  },
  {
    "v" : 4,
    "unique" : true,
    "key" : {
      "category" : 1,
      "" : 1,
      "CustomerId" : 1,
      "OrderId" : 1
    },
    "name" : "category_1_CustID_1_OrderId_1",
    "ns" : "ecommerceApp.orders",
    "partialFilterExpression" : {
      "$and" : [
        {"OrderId": {"$exists": true}},
        {"isDelivered": {"$eq": false}}
      ]
    }
  }
]
```

**Multiple partial filter expression on same key:order**

Different partial indexes can be created for the same field combinations (key:order).
These indexes must have a different name.

```
db.orders.createIndex(
  {"OrderId":1},
  {
    name:"firstPartialIndex",
    partialFilterExpression:{"OrderId":{"$exists": true}}
  }
)
```

```
db.orders.createIndex(
  {"OrderId":1},
  {
    name:"secondPartialIndex",
    partialFilterExpression:{"OrderId":{"$gt": 1000}}
  }
)
```

Run `getIndexes` operation to list all indexes in the collection:

```
db.orders.getIndexes()
```

These examples returns the following output:

```
[
  {
    "v" : 4,
    "key" : {
      "_id" : 1
    },
    "name" : "_id_",
    "ns" : "ecommerceApp.orders"
  },
  {
    "v" : 4,
    "key" : {
      "OrderId" : 1
    },
    "name" : "firstPartialIndex",
    "ns" : "ecommerceApp.orders",
    "partialFilterExpression" : {"OrderId":{"$exists": true}}
  },
  {
    "v" : 4,
    "key" : {
      "OrderId" : 1
    },
    "name" : "secondPartialIndex",
    "ns" : "ecommerceApp.orders",
    "partialFilterExpression" : {"OrderId":{"$gt": 1000}}
  }
]
```

###### Important

Index names must be different and must be deleted by name only.

**Indexes with partial and TTL properties**

You can also create indexes having partial and TTL properties by specifying both `partialFilterExpression` and `expireAfterSeconds` options during index creation.
This allows you to provide more control over which documents are now removed from a collection.

For example, you may have a TTL index that identifies documents to be deleted after a certain time period.
You can now provide extra conditions on when to delete documents using the partial index option:

```
db.orders.createIndex(
    { "OrderTimestamp": 1 },
    {
        expireAfterSeconds: 3600 ,
        partialFilterExpression: { "isDelivered": { $eq: true } }
    }
)
```

This example returns the following output:

```
{
        "createdCollectionAutomatically" : false,
        "numIndexesBefore" : 1,
        "numIndexesAfter" : 2,
        "ok" : 1,
        "operationTime" : Timestamp(1234567890, 1)
}
```

Run the `getIndexes` operation to list indexes present in the collection:

```
db.orders.getIndexes()
[
    {
        "v" : 4,
        "key" : {
            "_id" : 1
        },
        "name" : "_id_",
        "ns" : "test.orders"
    }
```

This example returns the following output:

```
[
    {
        "v": 4,
        "key": {
            "_id": 1
        },
        "name": "_id_",
        "ns": "ecommerceApp.orders"
    },
    {
        "v": 4,
        "key": {
            "OrderTimestamp": 1
        },
        "name": "OrderTimestamp_1",
        "ns": "ecommerceApp.orders",
        "partialFilterExpression": {
            "isDelivered": {
                "$eq": true
            }
        },
        "expireAfterSeconds": 3600
    }
]
```

## Partial index limitations

The following limitations apply to the partial index feature:

- Inequality queries in Amazon DocumentDB will only use a partial index when the query filter predicate exactly matches the `partialFilterExpression` and is of the same datatype.

###### Note

Even `$hint` cannot be used to force IXSCAN for the above case.

In the following example, the `partialFilterExpression` is only applied to `field1` but not `field2`:

```
db.orders.createIndex(
  {"OrderAmount": 1},
  {"partialFilterExpression": { OrderAmount : {"$gt" : 5}}}
)

db.orders.find({OrderAmount : {"$gt" : 5}}) // Will use partial index
db.orders.find({OrderAmount : {"$gt" : 6}}) // Will not use partial index
db.orders.find({OrderAmount : {"$gt" : Decimal128(5.00)}}) // Will not use partial index
```

- A `partialFilterExpression` with array operators are not supported.
  The following operation will generate an error:

```
db.orders.createIndex(
  {"CustomerId":1},
  {'partialFilterExpression': {'OrderId': {'$eq': [1000, 1001, 1002]}}}
)
```

- The following operators are not supported in partialFilterExpression field:
  - `$all` (array operator)
  - `$mod` (array operator)
  - `$or`
  - `$xor`
  - `$not`
  - `$nor`

- The data type of the filter expression and the filter should be the same.
