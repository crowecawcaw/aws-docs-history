

# $lookup
<a name="lookup"></a>

The `$lookup` aggregation stage in Amazon DocumentDB allows you to perform a left outer join between two collections. This operation lets you combine data from multiple collections based on matching field values. It is particularly useful when you need to incorporate data from related collections into your query results.

**Parameters**
+ `from`: The name of the collection to perform the join with.
+ `localField`: The field from the input documents to match against the `foreignField`.
+ `foreignField`: The field from the documents in the `from` collection to match against the `localField`.
+ `as`: The name of the new field to add to the output documents containing the matching documents from the `from` collection.
+ `pipeline`: Optional if `localField` and `foreignField` are specified. An aggregation pipeline to run on the `from` collection. The pipeline returns documents from the `from` collection. To return all documents, specify an empty pipeline `[]`. The pipeline cannot include the `$out` or `$merge` stages. See [Join conditions and correlated subqueries (MongoDB Shell)](#lookup-correlated).
+ `let`: Optional. A document that defines variables to use in the `pipeline` stages. Use the variable expressions to access the fields from the input documents that are joined to the `pipeline`. To reference a variable in the pipeline stages, use the `"$$<variable>"` syntax. See [Join conditions and correlated subqueries (MongoDB Shell)](#lookup-correlated).

## Example (MongoDB Shell)
<a name="lookup-examples"></a>

The following example demonstrates a simple `$lookup` operation that joins data from the `orders` collection into the `customers` collection.

**Create sample documents**

```
db.customers.insertMany([
  { _id: 1, name: "Alice" },
  { _id: 2, name: "Bob" },
  { _id: 3, name: "Charlie" }
]);

db.orders.insertMany([
  { _id: 1, customer_id: 1, total: 50 },
  { _id: 2, customer_id: 1, total: 100 },
  { _id: 3, customer_id: 2, total: 75 }
]);
```

**Query example**

```
db.customers.aggregate([
  {
    $lookup: {
      from: "orders",           
      localField: "_id",        
      foreignField: "customer_id", 
      as: "orders" 
    }
  }
]);
```

**Output**

```
[
  {
    _id: 1,
    name: 'Alice',
    orders: [
      { _id: 2, customer_id: 1, total: 100 },
      { _id: 1, customer_id: 1, total: 50 }
    ]
  },
  { _id: 3, name: 'Charlie', orders: [] },
  {
    _id: 2,
    name: 'Bob',
    orders: [ { _id: 3, customer_id: 2, total: 75 } ]
  }
]
```

## Join conditions and correlated subqueries (MongoDB Shell)
<a name="lookup-correlated"></a>

New from version 8.0.2.

In addition to a single equality match, `$lookup` in Amazon DocumentDB can run an aggregation pipeline on the joined collection. This supports uncorrelated subqueries, which run the same subquery for every input document, and correlated subqueries, which use variables defined from each input document's fields to return results correlated to that document.

**Syntax**

To run a correlated subquery, define variables from the input document's fields with `let`, and reference them in the `pipeline` stages:

```
{
  $lookup: {
    from: <collection to join>,
    let: { <var_1>: <expression>, ..., <var_n>: <expression> },
    pipeline: [ <pipeline to run on the joined collection> ],
    as: <output array field>
  }
}
```

**Parameters**
+ `let`: A document that defines variables from the fields of the input documents. To reference a variable in the pipeline stages, use the `"$$<variable>"` syntax. The variables can be accessed by the stages in the `pipeline`, including additional `$lookup` stages nested in the `pipeline`. A `$match` stage requires the use of the `$expr` operator to access the variables. Omit `let` to run an uncorrelated subquery.
+ `pipeline`: The aggregation pipeline to run on the `from` collection. The pipeline cannot access fields of the input documents directly; define variables with `let` and reference the variables instead. To return all documents, specify an empty pipeline `[]`.

The `$eq`, `$gt`, `$gte`, `$lt`, and `$lte` comparison operators placed in an `$expr` operator inside a `$match` stage can use an index on the `from` collection when they compare a field of the joined collection with a `let` variable or a constant.

**Create sample documents**

```
db.customers.insertMany([
  { _id: 1, name: "Alice", min_total: 60 },
  { _id: 2, name: "Bob", min_total: 50 },
  { _id: 3, name: "Charlie", min_total: 20 }
]);

db.orders.insertMany([
  { _id: 1, customer_id: 1, total: 50 },
  { _id: 2, customer_id: 1, total: 100 },
  { _id: 3, customer_id: 2, total: 75 }
]);
```

**Query example**

The following example joins each customer with their orders, and keeps only the orders whose `total` is greater than or equal to that customer's own `min_total` value. The join condition and the per-customer filter both reference `let` variables inside `$expr`:

```
db.customers.aggregate([
  {
    $lookup: {
      from: "orders",
      let: { customer_id: "$_id", min_total: "$min_total" },
      pipeline: [
        {
          $match: {
            $expr: {
              $and: [
                { $eq: [ "$customer_id", "$$customer_id" ] },
                { $gte: [ "$total", "$$min_total" ] }
              ]
            }
          }
        },
        { $project: { _id: 0, total: 1 } }
      ],
      as: "qualifying_orders"
    }
  }
]);
```

**Output**

```
[
  { _id: 1, name: 'Alice', min_total: 60, qualifying_orders: [ { total: 100 } ] },
  { _id: 2, name: 'Bob', min_total: 50, qualifying_orders: [ { total: 75 } ] },
  { _id: 3, name: 'Charlie', min_total: 20, qualifying_orders: [] }
]
```

For each customer, the subquery is evaluated with that customer's `_id` and `min_total` values, so each document receives its own correlated result.

## Correlated subqueries using concise syntax (MongoDB Shell)
<a name="lookup-concise-correlated"></a>

New from version 8.0.2.

Amazon DocumentDB also supports the concise correlated subquery syntax, which combines the equality match on `localField` and `foreignField` with a `pipeline`. The concise syntax removes the requirement to express the equality match inside an `$expr` operator in a `$match` stage.

**Syntax**

```
{
  $lookup: {
    from: <collection to join>,
    localField: <field from the input documents>,
    foreignField: <field from the documents of the "from" collection>,
    let: { <var_1>: <expression>, ..., <var_n>: <expression> },
    pipeline: [ <pipeline to run> ],
    as: <output array field>
  }
}
```

**Query example**

The following example returns the same results as the previous correlated subquery example. The equality match between `_id` and `customer_id` is expressed with `localField` and `foreignField` instead of an `$expr` condition:

```
db.customers.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "customer_id",
      let: { min_total: "$min_total" },
      pipeline: [
        { $match: { $expr: { $gte: [ "$total", "$$min_total" ] } } },
        { $project: { _id: 0, total: 1 } }
      ],
      as: "qualifying_orders"
    }
  }
]);
```

**Output**

```
[
  { _id: 1, name: 'Alice', min_total: 60, qualifying_orders: [ { total: 100 } ] },
  { _id: 2, name: 'Bob', min_total: 50, qualifying_orders: [ { total: 75 } ] },
  { _id: 3, name: 'Charlie', min_total: 20, qualifying_orders: [] }
]
```

## Supported stages in correlated subqueries
<a name="lookup-correlated-stages"></a>

When a `$lookup` pipeline uses `let`, the following stages can reference the `"$$<variable>"` variables:
+ `$match` (using the `$expr` operator)
+ `$project`
+ `$addFields`
+ `$set`
+ `$group`
+ `$bucket`
+ `$bucketAuto`
+ `$sortByCount`
+ `$lookup` (nested)
+ `$graphLookup`

Stages that do not evaluate variable expressions, such as `$sort`, `$skip`, `$limit`, `$count`, `$sample`, `$unwind`, and `$unset`, can also be used in the pipeline but cannot reference the variables.

The following stages are not supported in a `$lookup` pipeline that uses `let`: `$facet`, `$redact`, `$replaceRoot`, `$replaceWith`, `$geoNear`, `$setWindowFields`, `$fill`, and `$match` with `$text`.

**Restrictions**
+ The `pipeline` cannot include the `$out` or `$merge` stages.

## Code examples
<a name="lookup-code"></a>

To view a code example for using the `$lookup` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  await client.connect();

  const db = client.db('test');

  const result = await db.collection('customers').aggregate([
    {
      $lookup: {
        from: 'orders',
        localField: '_id',
        foreignField: 'customer_id',
        as: 'orders'
      }
    }
  ]).toArray();

  console.log(JSON.stringify(result, null, 2));
  await client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    db = client.test
    
    collection = db.customers

    pipeline = [
        {
            "$lookup": {
                "from": "orders",
                "localField": "_id",
                "foreignField": "customer_id",
                "as": "orders"
            }
        }
    ]

    result = collection.aggregate(pipeline)

    for doc in result:
        print(doc)

    client.close()

example()
```

------

## Correlated subquery code examples
<a name="lookup-correlated-code"></a>

To view a code example for using the `$lookup` stage with a correlated subquery (using `let` and `pipeline`), choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  const db = client.db('test');

  const customers = db.collection('customers');
  await customers.insertMany([
    { _id: 1, name: "Alice", min_total: 60 },
    { _id: 2, name: "Bob", min_total: 50 },
    { _id: 3, name: "Charlie", min_total: 20 }
  ]);
  const orders = db.collection('orders');
  await orders.insertMany([
    { _id: 1, customer_id: 1, total: 50 },
    { _id: 2, customer_id: 1, total: 100 },
    { _id: 3, customer_id: 2, total: 75 }
  ]);

  // Correlated subquery: filter each customer's orders with a per-customer threshold
  const result = await customers.aggregate([
    {
      $lookup: {
        from: 'orders',
        localField: '_id',
        foreignField: 'customer_id',
        let: { min_total: '$min_total' },
        pipeline: [
          { $match: { $expr: { $gte: [ '$total', '$$min_total' ] } } },
          { $project: { _id: 0, total: 1 } }
        ],
        as: 'qualifying_orders'
      }
    }
  ]).toArray();

  console.log(JSON.stringify(result, null, 2));
  await client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    db = client.test

    customers = db.customers
    customers.insert_many([
        { "_id": 1, "name": "Alice", "min_total": 60 },
        { "_id": 2, "name": "Bob", "min_total": 50 },
        { "_id": 3, "name": "Charlie", "min_total": 20 }
    ])
    orders = db.orders
    orders.insert_many([
        { "_id": 1, "customer_id": 1, "total": 50 },
        { "_id": 2, "customer_id": 1, "total": 100 },
        { "_id": 3, "customer_id": 2, "total": 75 }
    ])

    # Correlated subquery: filter each customer's orders with a per-customer threshold
    pipeline = [
        {
            "$lookup": {
                "from": "orders",
                "localField": "_id",
                "foreignField": "customer_id",
                "let": { "min_total": "$min_total" },
                "pipeline": [
                    { "$match": { "$expr": { "$gte": [ "$total", "$$min_total" ] } } },
                    { "$project": { "_id": 0, "total": 1 } }
                ],
                "as": "qualifying_orders"
            }
        }
    ]

    result = customers.aggregate(pipeline)

    for doc in result:
        print(doc)

    client.close()

example()
```

------