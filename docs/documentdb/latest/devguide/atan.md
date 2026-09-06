

# $atan
<a name="atan"></a>

New from version 8.0.1.

The `$atan` operator in Amazon DocumentDB returns the inverse tangent (arc tangent) of a value.

The input expression must resolve to a numeric value.

The result is in radians. To obtain degrees, apply `$radiansToDegrees` to the output.

The return type is `double` by default. If the input is a 128-bit decimal, the output is also a 128-bit decimal.

**Parameters**
+ `expression`: An expression that resolves to a number.

## Behavior
<a name="atan-behavior"></a>

**null and NaN**


| Example | Results | 
| --- | --- | 
| { $atan: NaN } | NaN | 
| { $atan: null } | null | 

When the input is `null` or the referenced field is missing, the result is `null`. An input of `NaN` produces `NaN`.

## Example (MongoDB Shell)
<a name="atan-examples"></a>

The following example shows how to use the `$atan` operator to calculate the arctangent of a value.

**Create sample documents**

```
db.values.insertMany([
  { "_id": 1, "value": 0 },
  { "_id": 2, "value": 1 },
  { "_id": 3, "value": -1 }
]);
```

**Query example**

```
db.values.aggregate([
  { $project: {
    "angle": { $atan: "$value" }
  }}
]);
```

**Output**

```
[
  { "_id": 1, "angle": 0 },
  { "_id": 2, "angle": 0.7853981633974483 },
  { "_id": 3, "angle": -0.7853981633974483 }
]
```

## Code examples
<a name="atan-code"></a>

To view a code example for using the `$atan` operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('values');

  const result = await collection.aggregate([
    { $project: {
      "angle": { $atan: "$value" }
    }}
  ]).toArray();

  console.log(result);
  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def main():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['values']

    result = list(collection.aggregate([
        { '$project': {
            'angle': { '$atan': '$value' }
        }}
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------