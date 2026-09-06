

# $tanh
<a name="tanh"></a>

New from version 8.0.1.

The `$tanh` operator in Amazon DocumentDB returns the hyperbolic tangent of a value.

The input expression must resolve to a numeric value.

The return type is `double` by default. If the input is a 128-bit decimal, the output is also a 128-bit decimal.

**Parameters**
+ `expression`: An expression that resolves to a number.

## Behavior
<a name="tanh-behavior"></a>

**null, NaN, and \+/- Infinity**


| Example | Results | 
| --- | --- | 
| { $tanh: NaN } | NaN | 
| { $tanh: null } | null | 
| { $tanh: -Infinity } | -1 | 
| { $tanh: Infinity } | 1 | 

When the input is `null` or the referenced field is missing, `$tanh` returns `null`. An input of `NaN` produces `NaN`. For positive infinity the result is `1`; for negative infinity the result is `-1`.

## Example (MongoDB Shell)
<a name="tanh-examples"></a>

The following example shows how to use the `$tanh` operator to calculate the hyperbolic tangent of a value.

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
    "result": { $tanh: "$value" }
  }}
]);
```

**Output**

```
[
  { "_id": 1, "result": 0 },
  { "_id": 2, "result": 0.7615941559557649 },
  { "_id": 3, "result": -0.7615941559557649 }
]
```

## Code examples
<a name="tanh-code"></a>

To view a code example for using the `$tanh` operator, choose the tab for the language that you want to use:

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
      "result": { $tanh: "$value" }
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
            'result': { '$tanh': '$value' }
        }}
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------