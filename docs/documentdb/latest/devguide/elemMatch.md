

# $elemMatch
<a name="elemMatch"></a>

The `$elemMatch` operator in Amazon DocumentDB is used to query an array field and return documents where at least one element in the array matches the specified criteria. This operator is particularly useful when you have complex data structures with nested arrays or embedded documents.

Planner version 2.0 added index support for `$elemMatch`.

**Parameters**
+ `field`: The array field to query.
+ `query`: The criteria to match against the array elements.

 

**Using `$elemMatch` within an `$all` expression**

See [Using `$elemMatch` within an `$all` expression](functional-differences.md#functional-differences.elemMatch) for limitations regarding the use of the `$elemMatch` operator within an `$all` expression.

## Example (MongoDB Shell)
<a name="elemMatch-examples"></a>

The following example demonstrates how to use the `$elemMatch` operator to find documents where the `parts` array has at least one element that matches the specified criteria.

**Create sample documents**

```
db.col.insertMany([
  { _id: 1, parts: [{ part: "xyz", qty: 10 }, { part: "abc", qty: 20 }] },
  { _id: 2, parts: [{ part: "xyz", qty: 5 }, { part: "abc", qty: 10 }] },
  { _id: 3, parts: [{ part: "xyz", qty: 15 }, { part: "abc", qty: 100 }] },
  { _id: 4, parts: [{ part: "abc", qty: 150 }] }
]);
```

**Query example**

```
db.col.find({
  parts: { "$elemMatch": { part: "xyz", qty: { $lt: 11 } } }
})
```

**Output**

```
{ "_id" : 1, "parts" : [ { "part" : "xyz", "qty" : 10 }, { "part" : "abc", "qty" : 20 } ] }
{ "_id" : 2, "parts" : [ { "part" : "xyz", "qty" : 5 }, { "part" : "abc", "qty" : 10 } ] }
```

## Code examples
<a name="elemMatch-code"></a>

To view a code example for using the `$elemMatch` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const col = db.collection('col');

  const result = await col.find({
    parts: { 
      "$elemMatch": { part: "xyz", qty: { $lt: 11 } } 
    }
  }).toArray();

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
    db = client['test']
    col = db['col']

    result = list(col.find({
      'parts': { 
        '$elemMatch': {'part': 'xyz', 'qty': {'$lt': 11}} 
      }
    }))

    print(result)
    client.close()

example()
```

------