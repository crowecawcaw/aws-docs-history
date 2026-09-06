

# $subtract
<a name="subtract"></a>

The `$subtract` operator in Amazon DocumentDB is used to subtract values. It can be used to subtract dates, numbers, or a combination of both. This operator is useful for calculating the difference between two dates or subtracting a value from a number.

**Parameters**
+ `expression1`: The first value to be subtracted.
+ `expression2`: The second value to be subtracted from `<expression1>`.

## Example (MongoDB Shell)
<a name="subtract-examples"></a>

The following example demonstrates how to use the `$subtract` operator to calculate the difference between two dates.

**Create sample document**

```
db.dates.insert([
  {
  "_id": 1,
  "startDate": ISODate("2023-01-01T00:00:00Z"),
  "endDate": ISODate("2023-01-05T12:00:00Z")
  }
]);
```

**Query example**

```
db.dates.aggregate([
  {
    $project: {
      _id: 1,
      durationDays: {
        $divide: [
          { $subtract: ["$endDate", "$startDate"] },
          1000 * 60 * 60 * 24  // milliseconds in a day
        ]
      }
    }
  }
]);
```

**Output**

```
[ { _id: 1, durationDays: 4.5 } ]
```

In this example, the `$subtract` operator is used to calculate the difference between the `$endDate` and `$startDate` in days.

## Code examples
<a name="subtract-code"></a>

To view a code example for using the `$subtract` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('dates');

    const pipeline = [
      {
        $project: {
          _id: 1,
          durationDays: {
            $divide: [
              { $subtract: ["$endDate", "$startDate"] },
              1000 * 60 * 60 * 24  // Convert milliseconds to days
            ]
          }
        }
      }
    ];

    const results = await collection.aggregate(pipeline).toArray();

    console.dir(results, { depth: null });

  } finally {
    await client.close();
  }
}

example().catch(console.error);
```

------
#### [ Python ]

```
from datetime import datetime, timedelta
from pymongo import MongoClient

def example():
  
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

    try:
        db = client.test
        collection = db.dates

        pipeline = [
            {
                "$project": {
                    "_id": 1,
                    "durationDays": {
                        "$divide": [
                            { "$subtract": ["$endDate", "$startDate"] },
                            1000 * 60 * 60 * 24  # Convert milliseconds to days
                        ]
                    }
                }
            }
        ]

        results = collection.aggregate(pipeline)

        for doc in results:
            print(doc)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()

example()
```

------