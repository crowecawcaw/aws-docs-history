

# $sortArray
<a name="sortArray"></a>

New from version 8.0

Not supported by Elastic cluster.

The `$sortArray` operator in Amazon DocumentDB sorts the elements of an array. For arrays of scalar values, the array is sorted by element value. For arrays of documents, the array is sorted by the specified field or fields. The operator returns the sorted array in ascending (`1`) or descending (`-1`) order.

**Note**  
`$sortArray` is supported in the `$project` stage of the aggregation pipeline with query planner version 3.

**Syntax**

```
{ $sortArray: { input: <array>, sortBy: <sort specification> } }
```

**Parameters**
+ `input`: The array to sort.
+ `sortBy`: The sort order. For an array of scalar values, specify `1` for ascending or `-1` for descending. For an array of documents, specify a document of the form `{ field: 1 }` or `{ field: -1 }` for each field to sort by.

## Example (MongoDB Shell)
<a name="sortArray-examples"></a>

The following example demonstrates how to use the `$sortArray` operator to sort the elements of an array in ascending order.

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
      sorted_flight_miles: { $sortArray: { input: "$flight_miles", sortBy: 1 } }
    }
  }
]);
```

**Output**

```
{ "_id" : 1, "member_since" : ISODate("1987-01-01T00:00:00Z"), "credit_card" : false, "sorted_flight_miles" : [ 880, 1205, 2560 ] }
{ "_id" : 2, "member_since" : ISODate("1982-01-01T00:00:00Z"), "credit_card" : true, "sorted_flight_miles" : [ 890, 1205, 2560, 2780 ] }
{ "_id" : 3, "member_since" : ISODate("1999-01-01T00:00:00Z"), "credit_card" : true, "sorted_flight_miles" : [ 880, 1205 ] }
```

In this example, the `$sortArray` operator sorts the `flight_miles` array in ascending order. The resulting `sorted_flight_miles` field in the output shows the elements of the array in sorted order.

## Code examples
<a name="sortArray-code"></a>

To view a code example for using the `$sortArray` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$sortArray` operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function sortArray() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('miles');

  const result = await collection.aggregate([
    {
      $project: {
        _id: 1,
        member_since: 1,
        credit_card: 1,
        sorted_flight_miles: { $sortArray: { input: '$flight_miles', sortBy: 1 } }
      }
    }
  ]).toArray();

  console.log(result);
  client.close();
}

sortArray();
```

------
#### [ Python ]

Here's an example of using the `$sortArray` operator in a Python application:

```
from pymongo import MongoClient

def sort_array():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client.test
    collection = db.miles

    result = list(collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'member_since': 1,
                'credit_card': 1,
                'sorted_flight_miles': { '$sortArray': { 'input': '$flight_miles', 'sortBy': 1 } }
            }
        }
    ]))

    print(result)
    client.close()

sort_array()
```

------