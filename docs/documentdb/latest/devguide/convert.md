

# $convert
<a name="convert"></a>

New from version 4.0

The `$convert` operator in Amazon DocumentDB is used to convert a value from one data type to another. This operator is useful when you need to perform operations on data of different types, such as converting a string to a number or a date to a timestamp.

**Parameters**
+ `to`: The target data type to convert the value to. Supported values are `"string"`, `"double"`, `"long"`, `"int"`, `"date"`, and `"boolean"`.
+ `from`: The current data type of the value. If not specified, Amazon DocumentDB will attempt to automatically detect the data type.
+ `onError`: (optional) The value to return if the conversion fails. Can be a specific value or one of the following special values: `"null"`, `"zerofill"`, or `"error"`.
+ `onNull`: (optional) The value to return if the input value is `null`. Can be a specific value or one of the following special values: `"null"`, `"zerofill"`, or `"error"`.

## Example (MongoDB Shell)
<a name="convert-examples"></a>

The following example demonstrates converting a string value to a date using the `$convert` operator.

**Create sample documents**

```
db.users.insertMany([
  { _id: 1, name: "John Doe", joinedOn: "2022-01-01" },
  { _id: 2, name: "Jane Smith", joinedOn: "2023-02-15" },
  { _id: 3, name: "Bob Johnson", joinedOn: "invalid date" }
]);
```

**Query example**

```
db.users.aggregate([
  {
    $project: {
      _id: 1,
      name: 1,
      joinedOn: {
        $convert: {
          input: "$joinedOn",
          to: "date",
          onError: "null",
          onNull: "null"
        }
      }
    }
  }
])
```

**Output**

```
[
  { "_id" : 1, "name" : "John Doe", "joinedOn" : ISODate("2022-01-01T00:00:00Z") },
  { "_id" : 2, "name" : "Jane Smith", "joinedOn" : ISODate("2023-02-15T00:00:00Z") },
  { "_id" : 3, "name" : "Bob Johnson", "joinedOn" : null }
]
```

## Code examples
<a name="convert-code"></a>

To view a code example for using the `$convert` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require("mongodb");

async function example() {
  const client = await MongoClient.connect("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false");
  const db = client.db("test");
  const users = db.collection("users");

  const results = await users.aggregate([
    {
      $project: {
        _id: 1,
        name: 1,
        joinedOn: {
          $convert: {
            input: "$joinedOn",
            to: "date",
            onError: "null",
            onNull: "null"
          }
        }
      }
    }
  ]).toArray();

  console.log(results);
  client.close();
}

example();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def example():
    client = MongoClient("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    db = client["test"]
    users = db["users"]

    results = list(users.aggregate([
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "joinedOn": {
                    "$convert": {
                        "input": "$joinedOn",
                        "to": "date",
                        "onError": "null",
                        "onNull": "null"
                    }
                }
            }
        }
    ]))

    print(results)
    client.close()

example()
```

------