

# $dateToParts
<a name="dateToParts"></a>

New from version 5.0.1 and 8.0

The `$dateToParts` aggregation operator in Amazon DocumentDB returns a document that contains the constituent parts of a date and time value, such as the year, month, day, hour, minute, second, and millisecond.

**Parameters**
+ `date`: The date and time value to break into parts.
+ `timezone`: (optional) The time zone to use when extracting the date parts. If not specified, the parts are returned in UTC.
+ `iso8601`: (optional) If set to `true`, the returned document uses ISO 8601 date parts (`isoWeekYear`, `isoWeek`, `isoDayOfWeek`). The default is `false`.

## Example (MongoDB Shell)
<a name="dateToParts-examples"></a>

The following example demonstrates how to use the `$dateToParts` operator to return the individual parts of a date.

**Create sample documents**

```
db.events.insertMany([
  { _id: 1, eventDate: ISODate("2023-04-01T10:30:15Z") },
  { _id: 2, eventDate: ISODate("2023-12-25T18:45:00Z") }
]);
```

**Query example**

```
db.events.aggregate([
  {
    $project: {
      _id: 1,
      parts: { $dateToParts: { date: "$eventDate" } }
    }
  }
])
```

**Output**

```
[
  {
    "_id": 1,
    "parts": { "year": 2023, "month": 4, "day": 1, "hour": 10, "minute": 30, "second": 15, "millisecond": 0 }
  },
  {
    "_id": 2,
    "parts": { "year": 2023, "month": 12, "day": 25, "hour": 18, "minute": 45, "second": 0, "millisecond": 0 }
  }
]
```

## Code examples
<a name="dateToParts-code"></a>

To view a code example for using the `$dateToParts` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('events');

  const result = await collection.aggregate([
    {
      $project: {
        _id: 1,
        parts: { $dateToParts: { date: "$eventDate" } }
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
    collection = db['events']

    result = list(collection.aggregate([
        {
            '$project': {
                '_id': 1,
                'parts': { '$dateToParts': { 'date': '$eventDate' } }
            }
        }
    ]))

    print(result)

    client.close()

example()
```

------