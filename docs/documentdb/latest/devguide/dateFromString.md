

# $dateFromString
<a name="dateFromString"></a>

The `$dateFromString` aggregation operator in Amazon DocumentDB allows you to convert a date-time string into a date object. This is useful when your data is stored as strings but you need to perform date-based operations on the data.

**Parameters**
+ `dateString`: A string that represents a date and time.
+ `format`: (optional) A string that specifies the format of the `dateString`. If not provided, Amazon DocumentDB will attempt to parse the string in the ISO-8601 format.
+ `timezone`: (optional) A string that specifies the time zone. If not provided, Amazon DocumentDB will use the time zone of the server.
+ `onError`: (optional) Specifies the action to take if the conversion fails. Possible values are `'error'` (the default, which throws an error), `'null'` (returns `null`), or `'replace'` (replaces the value with the replacement string specified in the `onErrorMessage` option).
+ `onErrorMessage`: (optional) If `onError` is set to `'replace'`, this option specifies the replacement string.

## Example (MongoDB Shell)
<a name="dateFromString-examples"></a>

The following example demonstrates how to use `$dateFromString` to convert a date string to a date object in Amazon DocumentDB.

**Create sample documents**

```
db.missionLog.insertMany([
{ _id: 1, event: "missionStart", logDate: "2020-03-15T13:41:33"},
{ _id: 2, event: "jumpPoint1", logDate: "2020-03-15T13:45:34"},
{ _id: 3, event: "jumpPoint2", logDate: "2020-03-15T13:48:21"},
{ _id: 4, event: "jumpPoint3", logDate: "2020-03-15T13:52:09"},
{ _id: 5, event: "missionEnd", logDate: "2020-03-15T13:58:44"}
]);
```

**Query example**

```
db.missionLog.aggregate([
  {
    $project: {
      event: '$event',
      logDate: {
        $dateFromString: {
          dateString: '$logDate'
        }
      }
    }
  }
]);
```

**Output**

```
[
  {
    "_id": 1,
    "event": "missionStart",
    "logDate": ISODate("2020-03-15T13:41:33Z")
  },
  {
    "_id": 2,
    "event": "jumpPoint1",
    "logDate": ISODate("2020-03-15T13:45:34Z")
  },
  {
    "_id": 3,
    "event": "jumpPoint2",
    "logDate": ISODate("2020-03-15T13:48:21Z")
  },
  {
    "_id": 4,
    "event": "jumpPoint3",
    "logDate": ISODate("2020-03-15T13:52:09Z")
  },
  {
    "_id": 5,
    "event": "missionEnd",
    "logDate": ISODate("2020-03-15T13:58:44Z")
  }
]
```

## Code examples
<a name="dateFromString-code"></a>

To view a code example for using the `$dateFromString` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('missionLog');

  const result = await collection.aggregate([
    {
      $project: {
        event: '$event',
        logDate: {
          $dateFromString: {
            dateString: '$logDate'
          }
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
    collection = db['missionLog']

    result = list(collection.aggregate([
        {
            '$project': {
                'event': '$event',
                'logDate': {
                    '$dateFromString': {
                        'dateString': '$logDate'
                    }
                }
            }
        }
    ]))

    print(result)
    client.close()

example()
```

------