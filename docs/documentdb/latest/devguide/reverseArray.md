

# $reverseArray
<a name="reverseArray"></a>

The `$reverseArray` operator in Amazon DocumentDB is used to reverse the elements of an array in the specified order. This operator is useful when you need to reorder the elements of an array in the reverse direction.

**Parameters**
+ `expression`: The array expression to reverse.

## Example (MongoDB Shell)
<a name="reverseArray-examples"></a>

The following example demonstrates how to use the `$reverseArray` operator to reverse the order of elements in an array.

**Create sample documents**

```
db.miles.insertMany([
  { "_id" : 1, "member_since" : ISODate("1987-01-01T00:00:00Z"), "credit_card" : false, "flight_miles" : [ 1205, 2560, 880 ]},
  { "_id" : 2, "member_since" : ISODate("1982-01-01T00:00:00Z"), "credit_card" : true, "flight_miles" : [ 1205, 2560, 890, 2780]},
  { "_id" : 3, "member_since" : ISODate("1999-01-01T00:00:00Z"), "credit_card" : true, "flight_miles" : [ 1205, 880]}
]);
```

**Query example**

```
db.miles.aggregate([
  {
    $project: {
      _id: 1,
      member_since: 1,
      credit_card: 1,
      reversed_flight_miles: { $reverseArray: "$flight_miles" }
    }
  }
]);
```

**Output**

```
{ "_id" : 1, "member_since" : ISODate("1987-01-01T00:00:00Z"), "credit_card" : false, "reversed_flight_miles" : [ 880, 2560, 1205 ] }
{ "_id" : 2, "member_since" : ISODate("1982-01-01T00:00:00Z"), "credit_card" : true, "reversed_flight_miles" : [ 2780, 890, 2560, 1205 ] }
{ "_id" : 3, "member_since" : ISODate("1999-01-01T00:00:00Z"), "credit_card" : true, "reversed_flight_miles" : [ 880, 1205 ] }
```

In this example, the `$reverseArray` operator is used to reverse the order of the `flight_miles` array. The resulting `reversed_flight_miles` field in the output shows the elements of the array in the reversed order.

## Code examples
<a name="reverseArray-code"></a>

To view a code example for using the `$reverseArray` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$reverseArray` operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function reverseArray() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('miles');

  const result = await collection.aggregate([
    {
      $project: {
        _id: 1,
        member_since: 1,
        credit_card: 1,
        reversed_flight_miles: { $reverseArray: '$flight_miles' }
      }
    }
  ]).toArray();

  console.log(result);
  client.close();
}

reverseArray();
```

------
#### [ Python ]

Here's an example of using the `$reverseArray` operator in a Python application:

```
from pymongo import MongoClient

def reverse_array():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.miles

    result = list(collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'member_since': 1,
                'credit_card': 1,
                'reversed_flight_miles': { '$reverseArray': '$flight_miles' }
            }
        }
    ]))

    print(result)
    client.close()

reverse_array()
```

------