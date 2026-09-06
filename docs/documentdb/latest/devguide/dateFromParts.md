

# $dateFromParts
<a name="dateFromParts"></a>

New from version 5.0.1 and 8.0

The `$dateFromParts` aggregation operator in Amazon DocumentDB constructs and returns a date and time value from its constituent parts, such as the year, month, day, hour, minute, second, and millisecond.

**Parameters**
+ `year`: The calendar year. Required when not using ISO 8601 parts.
+ `month`, `day`, `hour`, `minute`, `second`, `millisecond`: (optional) The remaining date and time components. Omitted components default to their lowest valid value.
+ `isoWeekYear`, `isoWeek`, `isoDayOfWeek`: (optional) ISO 8601 date components. Use these instead of `year`, `month`, and `day` to construct a date from an ISO 8601 week date.
+ `timezone`: (optional) The time zone to use when constructing the date. If not specified, UTC is used.

## Example (MongoDB Shell)
<a name="dateFromParts-examples"></a>

The following example demonstrates how to use the `$dateFromParts` operator to construct a date from individual components.

**Create sample documents**

```
db.parts.insertMany([
  { _id: 1, y: 2023, m: 4, d: 1 },
  { _id: 2, y: 2023, m: 12, d: 25 }
]);
```

**Query example**

```
db.parts.aggregate([
  {
    $project: {
      _id: 1,
      constructedDate: {
        $dateFromParts: { year: "$y", month: "$m", day: "$d" }
      }
    }
  }
])
```

**Output**

```
[
  { "_id": 1, "constructedDate": ISODate("2023-04-01T00:00:00Z") },
  { "_id": 2, "constructedDate": ISODate("2023-12-25T00:00:00Z") }
]
```

## Code examples
<a name="dateFromParts-code"></a>

To view a code example for using the `$dateFromParts` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('parts');

  const result = await collection.aggregate([
    {
      $project: {
        _id: 1,
        constructedDate: {
          $dateFromParts: { year: "$y", month: "$m", day: "$d" }
        }
      }
    }
  ]).toArray();

  console.log(result);

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
    collection = db['parts']

    result = list(collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'constructedDate': {
                    '$dateFromParts': { 'year': '$y', 'month': '$m', 'day': '$d' }
                }
            }
        }
    ]))

    print(result)

    client.close()

example()
```

------