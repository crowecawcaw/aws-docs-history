

# $multiply
<a name="multiply"></a>

The `$multiply` operator in Amazon DocumentDB is used to multiply the values of two or more fields or expressions. This operator is particularly useful for performing arithmetic operations on numeric fields within documents. It can be employed in various stages of the aggregation pipeline, such as `$project` and `$addFields`, to create new fields or modify existing ones.

**Parameters**
+ `expression1`: The first numeric expression to be multiplied.
+ `expression2`: The second numeric expression to be multiplied.
+ `[expression3, ...]`: (optional) Additional numeric expressions to be multiplied.

## Example (MongoDB Shell)
<a name="multiply-examples"></a>

The following example demonstrates using `$multiply` to calculate `bonus_miles` by multiplying `base_miles` and `bonus_rate` for customers who used a credit card for the trip.

**Sample documents**

```
db.miles.insertMany([
{ "_id": 1, "customer_name": "Arnav Desai", "member_since": ISODate("1997-03-01T00:00:00Z"), "base_miles": 2500, "bonus_rate": 1.8, "credit_card": true, "trip_cost": 250 },
{ "_id": 2, "customer_name": "Jorge Souza", "member_since": ISODate("2004-01-10T00:00:00Z"), "base_miles": 1890, "bonus_rate": 1.4, "credit_card": true, "trip_cost": 189 },
{ "_id": 3, "customer_name": "Saanvi Sarkar", "member_since": ISODate("1999-11-22T00:00:00Z"), "base_miles": 3250, "bonus_rate": 1.8, "credit_card": false, "trip_cost": 325 },
{ "_id": 4, "customer_name": "Paulo Santos", "member_since": ISODate("2021-06-19T00:00:00Z"), "base_miles": 2980, "bonus_rate": 1.2, "credit_card": true, "trip_cost": 298 },
{ "_id": 5, "customer_name": "Wang Xiulan", "member_since": ISODate("1995-12-04T00:00:00Z"), "base_miles": 1350, "bonus_rate": 1.9, "credit_card": false, "trip_cost": 135 }
]);
```

**Query example**

```
db.miles.aggregate([
  {
    $match: { credit_card: true }
  },
  {
    $project: {
      customer_name: 1,
      base_miles: 1,
      bonus_rate:1,
      credit_card: 1,
      total_miles: {
        $multiply: ["$base_miles", "$bonus_rate"]
      }
    }
  }
]);
```

**Output**

```
[
  { _id: 1, customer_name: 'Arnav Desai', base_miles: 12500, bonus_rate: 1.8, credit_card: true, total_miles: 22500 },
  { _id: 3, customer_name: 'Saanvi Sarkar',base_miles: 15200, bonus_rate: 1.8, credit_card: true, total_miles: 27360 },
  { _id: 4, customer_name: 'Paulo Santos', base_miles: 3400, bonus_rate: 1.1, credit_card: true, total_miles: 3740 }
]
```

## Code examples
<a name="multiply-code"></a>

To view a code example for using the `$multiply` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function multiplyBonusMiles() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('miles');

  const result = await collection.aggregate([
    { $match: { credit_card: true } },
    {
      $project: {
        customer_name: 1,
        base_miles: 1,
        bonus_rate: 1,
        credit_card: 1,
        total_miles: {
          $multiply: ["$base_miles", "$bonus_rate"]
        }
      }
    }
  ]).toArray();

  console.log(result);
  await client.close();
}

multiplyBonusMiles();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def multiply_bonus_miles():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['miles']

    result = list(collection.aggregate([
        {'$match': {'credit_card': True}},
        {
            '$project': {
                'customer_name': 1,
                'base_miles': 1,
                'bonus_rate': 1,
                'credit_card': 1,
                'total_miles': {
                    '$multiply': ['$base_miles', '$bonus_rate']
                }
            }
        }
    ]))

    print(result)
    client.close()

multiply_bonus_miles()
```

------