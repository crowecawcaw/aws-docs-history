

# $round
<a name="round"></a>

New from version 8.0.1.

The `$round` operator in Amazon DocumentDB rounds a number to a specified decimal place. When a value falls exactly halfway between the two nearest values at that place, `$round` rounds to the nearest even digit. For example, 2.5 rounds to 2, and 3.5 rounds to 4.

**Parameters**
+ `number`: An expression that resolves to a number.
+ `place`: Optional. An integer expression between -20 and 100 that specifies the number of decimal places to round to. A negative value rounds to the left of the decimal. Defaults to 0.

## Example (MongoDB Shell)
<a name="round-examples"></a>

The following example shows how to use the `$round` operator to round numeric values to one decimal place.

**Rounding with a positive place value**

```
db.measurements.insertMany([
  {_id: 1, value: 3.456},
  {_id: 2, value: 7.891},
  {_id: 3, value: 12.345}
]);
```

**Query example**

```
db.measurements.aggregate([
  { $project: { rounded: { $round: ["$value", 1] } } }
]);
```

**Output**

```
[
  {_id: 1, rounded: 3.5},
  {_id: 2, rounded: 7.9},
  {_id: 3, rounded: 12.3}
]
```

**Rounding halfway values to the nearest even digit**

When a value falls exactly halfway between the two nearest values at the target place, `$round` rounds to the nearest even digit rather than always rounding up. The following example rounds halfway values to whole integers.

```
db.halfway.insertMany([
  {_id: 1, value: 10.5},
  {_id: 2, value: 11.5},
  {_id: 3, value: 12.5},
  {_id: 4, value: 13.5}
]);
```

```
db.halfway.aggregate([
  { $project: { rounded: { $round: ["$value", 0] } } }
]);
```

**Output**

```
[
  {_id: 1, rounded: 10},
  {_id: 2, rounded: 12},
  {_id: 3, rounded: 12},
  {_id: 4, rounded: 14}
]
```

Because `10.5` is exactly halfway between `10` and `11`, it rounds to the nearest even value `10`. Similarly, `11.5` and `12.5` both round to the nearest even value `12`, and `13.5` rounds to `14`.

**Rounding with a negative place value**

When `place` is negative, `$round` rounds to the left of the decimal. The following example rounds values using the first digit to the left of the decimal.

```
db.samples.insertMany([
  {_id: 1, value: 19.25},
  {_id: 2, value: 28.73},
  {_id: 3, value: 34.32}
]);
```

```
db.samples.aggregate([
  { $project: { rounded: { $round: ["$value", -1] } } }
]);
```

**Output**

```
[
  {_id: 1, rounded: 20},
  {_id: 2, rounded: 30},
  {_id: 3, rounded: 30}
]
```

## Code examples
<a name="round-code"></a>

To view a code example for using the `$round` operator, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function example() {
  const client = new MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  try {
    await client.connect();
    const db = client.db('test');
    const collection = db.collection('measurements');
    const result = await collection.aggregate([
      { $project: { rounded: { $round: ["$value", 1] } } }
    ]).toArray();
    console.log(result);
  } finally {
    await client.close();
  }
}
example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    try:
        db = client['test']
        collection = db['measurements']
        result = list(collection.aggregate([
            {'$project': {'rounded': {'$round': ['$value', 1]}}}
        ]))
        print(result)
    finally:
        client.close()

example()
```

------