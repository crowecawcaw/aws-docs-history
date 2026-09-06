

# $tan
<a name="tan"></a>

New from version 8.0.1.

The `$tan` operator in Amazon DocumentDB returns the tangent of a value that is measured in radians.

The input expression must resolve to a numeric value. If your value is in degrees, apply `$degreesToRadians` before passing it to `$tan`.

The return type is `double` by default. If the input is a 128-bit decimal, the output is also a 128-bit decimal.

**Parameters**
+ `expression`: An expression that resolves to a number in radians.

## Behavior
<a name="tan-behavior"></a>

**null, NaN, and \+/- Infinity**


| Example | Results | 
| --- | --- | 
| { $tan: NaN } | NaN | 
| { $tan: null } | null | 
| { $tan: Infinity } or { $tan: -Infinity } | Throws an error. | 

When the input is `null` or the referenced field is missing, `$tan` returns `null`. An input of `NaN` produces `NaN`. Positive or negative infinity causes an error because tangent is undefined at those values.

## Example (MongoDB Shell)
<a name="tan-examples"></a>

The following example shows how to use the `$tan` operator to calculate the tangent of an angle in radians.

**Create sample documents**

```
db.angles.insertMany([
  { "_id": 1, "angle": 0 },
  { "_id": 2, "angle": 0.7853981633974483 },
  { "_id": 3, "angle": -0.7853981633974483 }
]);
```

**Query example**

```
db.angles.aggregate([
  { $project: {
    "tangent": { $tan: "$angle" }
  }}
]);
```

**Output**

```
[
  { "_id": 1, "tangent": 0 },
  { "_id": 2, "tangent": 0.9999999999999999 },
  { "_id": 3, "tangent": -0.9999999999999999 }
]
```

## Code examples
<a name="tan-code"></a>

To view a code example for using the `$tan` operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('angles');

  const result = await collection.aggregate([
    { $project: {
      "tangent": { $tan: "$angle" }
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
    collection = db['angles']

    result = list(collection.aggregate([
        { '$project': {
            'tangent': { '$tan': '$angle' }
        }}
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------