

# $reduce
<a name="reduce"></a>

The `$reduce` aggregation operator in Amazon DocumentDB is used to apply a function of two arguments cumulatively to the elements of an array to reduce the array to a single value. This operator is particularly useful for performing complex calculations or transformations on array data within the aggregation pipeline.

**Parameters**
+ `input`: The array to be reduced.
+ `initialValue`: The initial value to be used in the reduction operation.
+ `in`: The expression to be evaluated on each element of the `input` array. This expression should return a value that will be used in the next iteration of the reduction.

## Example (MongoDB Shell)
<a name="reduce-examples"></a>

The following example demonstrates how to use the `$reduce` operator to calculate the sum of all elements in an array.

**Create sample documents**

```
db.orders.insertMany([
  { "_id": 1, "items": [1, 2, 3, 4, 5] },
  { "_id": 2, "items": [10, 20, 30] },
  { "_id": 3, "items": [5, 15, 25, 35] },
  { "_id": 4, "items": [100, 200] }
])
```

**Query example**

```
db.orders.aggregate([
  {
    $project: {
      total: {
        $reduce: {
          input: "$items",
          initialValue: 0,
          in: { $add: ["$$value", "$$this"] }
        }
      }
    }
  }
])
```

**Output**

```
[
  { "_id": 1, "total": 15 },
  { "_id": 2, "total": 60 },
  { "_id": 3, "total": 80 },
  { "_id": 4, "total": 300 }
]
```

The `$reduce` operator iterates over the `items` array, adding each element to the `initialValue` of 0. The result is the sum of all elements in the array.

## Code examples
<a name="reduce-code"></a>

To view a code example for using the `$reduce` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$reduce` operator in a Node.js application:

```
const { MongoClient } = require("mongodb");

async function main() {
  const client = await MongoClient.connect("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false");
  const db = client.db("test");
  const orders = db.collection("orders");

  const result = await orders.aggregate([
    {
      $project: {
        total: {
          $reduce: {
            input: "$items",
            initialValue: 0,
            in: { $add: ["$$value", "$$this"] }
          }
        }
      }
    }
  ]).toArray();

  console.log(result);
  await client.close();
}

main();
```

------
#### [ Python ]

Here's an example of using the `$reduce` operator in a python application:

```
from pymongo import MongoClient

def main():
    client = MongoClient("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    db = client["test"]
    orders = db["orders"]

    result = list(orders.aggregate([
        {
            "$project": {
                "total": {
                    "$reduce": {
                        "input": "$items",
                        "initialValue": 0,
                        "in": { "$add": ["$$value", "$$this"] }
                    }
                }
            }
        }
    ]))

    print(result)
    client.close()

if __name__ == "__main__":
    main()
```

------