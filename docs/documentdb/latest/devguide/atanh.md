

# $atanh
<a name="atanh"></a>

New from version 8.0.1.

The `$atanh` operator in Amazon DocumentDB returns the inverse hyperbolic tangent (hyperbolic arc tangent) of a value.

The input expression must resolve to a number in the range `-1` to `1` (inclusive). Values outside this range cause an error.

The return type is `double` by default. If the input is a 128-bit decimal, the output is also a 128-bit decimal.

**Parameters**
+ `expression`: An expression that resolves to a number between `-1` and `1`, inclusive.

## Behavior
<a name="atanh-behavior"></a>

**null, NaN, and \+/- Infinity**


| Example | Results | 
| --- | --- | 
| { $atanh: NaN } | NaN | 
| { $atanh: null } | null | 
| { $atanh: 1 } | Infinity | 
| { $atanh: -1 } | -Infinity | 
| { $atanh: Infinity } or { $atanh: -Infinity } | Throws an error. | 

When the input is `null` or the referenced field is missing, the result is `null`. An input of `NaN` produces `NaN`. The boundary values `1` and `-1` produce `Infinity` and `-Infinity` respectively. Any value outside the `[-1, 1]` range (including `±Infinity`) causes an error.

## Example (MongoDB Shell)
<a name="atanh-examples"></a>

The following example shows how to use the `$atanh` operator to calculate the inverse hyperbolic tangent of a value.

**Create sample documents**

```
db.values.insertMany([
  { "_id": 1, "value": 0 },
  { "_id": 2, "value": 0.5 },
  { "_id": 3, "value": -0.5 }
]);
```

**Query example**

```
db.values.aggregate([
  { $project: {
    "result": { $atanh: "$value" }
  }}
]);
```

**Output**

```
[
  { "_id": 1, "result": 0 },
  { "_id": 2, "result": 0.5493061443340548 },
  { "_id": 3, "result": -0.5493061443340548 }
]
```

## Code examples
<a name="atanh-code"></a>

To view a code example for using the `$atanh` operator, choose the tab for the language that you want to use:

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
      "result": { $atanh: "$value" }
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
            'result': { '$atanh': '$value' }
        }}
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------