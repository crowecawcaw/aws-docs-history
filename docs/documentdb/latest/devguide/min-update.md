

# $min
<a name="min-update"></a>

The `$min` update operator updates a field's value only if the specified value is less than the current field value. This operator is useful for maintaining minimum values across updates.

**Parameters**
+ `field`: The field to update.
+ `value`: The value to compare with the current field value.

## Example (MongoDB Shell)
<a name="min-update-examples"></a>

The following example demonstrates using the `$min` operator to update the lowest recorded temperature for a weather station.

**Create sample documents**

```
db.weather.insertMany([
  { _id: 1, station: "Station A", lowestTemp: 15 },
  { _id: 2, station: "Station B", lowestTemp: 20 },
  { _id: 3, station: "Station C", lowestTemp: 18 }
])
```

**Update example**

```
db.weather.updateOne(
  { _id: 1 },
  { $min: { lowestTemp: 12 } }
)
```

**Result**

The `lowestTemp` field for Station A is updated to 12 because 12 is less than the current value of 15.

```
{ "_id": 1, "station": "Station A", "lowestTemp": 12 }
```

## Code examples
<a name="min-update-code"></a>

To view a code example for using the `$min` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('weather');

  const result = await collection.updateOne(
    { _id: 1 },
    { $min: { lowestTemp: 12 } }
  );

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
    collection = db['weather']

    result = collection.update_one(
        { '_id': 1 },
        { '$min': { 'lowestTemp': 12 } }
    )

    print(result)
    client.close()

example()
```

------