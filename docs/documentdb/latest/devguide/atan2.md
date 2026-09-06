

# $atan2
<a name="atan2"></a>

New from version 8.0.1.

The `$atan2` operator in Amazon DocumentDB returns the inverse tangent (arc tangent) of `y / x`, where `y` and `x` are the first and second values passed to the expression respectively.

Both expressions must resolve to numeric values. The operator uses the sign of both arguments to determine the correct quadrant.

The result is in radians. To obtain degrees, apply `$radiansToDegrees` to the output.

The return type is `double` by default. If the inputs are 128-bit decimals, the output is also a 128-bit decimal.

**Parameters**
+ `expression 1` (y): An expression that resolves to a number representing the y-coordinate.
+ `expression 2` (x): An expression that resolves to a number representing the x-coordinate.

## Behavior
<a name="atan2-behavior"></a>

**null and NaN**

If either argument is `null` (or references a missing field), the result is `null`. If either argument is `NaN`, the result is `NaN`. When one argument is `null` and the other is `NaN`, `null` takes precedence.


| Example | Results | 
| --- | --- | 
| { $atan2: [ NaN, <value> ] } | NaN | 
| { $atan2: [ <value>, NaN ] } | NaN | 
| { $atan2: [ null, <value> ] } | null | 
| { $atan2: [ <value>, null ] } | null | 
| { $atan2: [ NaN, null ] } | null | 
| { $atan2: [ null, NaN ] } | null | 

## Example (MongoDB Shell)
<a name="atan2-examples"></a>

The following example shows how to use the `$atan2` operator to calculate the arctangent of y/x for a set of points.

**Create sample documents**

```
db.points.insertMany([
  { "_id": 1, "y": 1, "x": 1 },
  { "_id": 2, "y": 1, "x": 0 },
  { "_id": 3, "y": -1, "x": -1 }
]);
```

**Query example**

```
db.points.aggregate([
  { $project: {
    "angle": { $atan2: ["$y", "$x"] }
  }}
]);
```

**Output**

```
[
  { "_id": 1, "angle": 0.7853981633974483 },
  { "_id": 2, "angle": 1.5707963267948966 },
  { "_id": 3, "angle": -2.356194490192345 }
]
```

## Code examples
<a name="atan2-code"></a>

To view a code example for using the `$atan2` operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('points');

  const result = await collection.aggregate([
    { $project: {
      "angle": { $atan2: ["$y", "$x"] }
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
    collection = db['points']

    result = list(collection.aggregate([
        { '$project': {
            'angle': { '$atan2': ['$y', '$x'] }
        }}
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------