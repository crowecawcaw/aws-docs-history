

# $regexFind
<a name="regexFind"></a>

New from version 5.0.

Not supported by Elastic cluster.

The `$regexFind` operator in Amazon DocumentDB is used to perform regular expression matching on string fields within documents. It allows you to search for and extract specific substrings that match a given regular expression pattern.

**Parameters**
+ `input`: The string field or expression to search.
+ `regex`: The regular expression pattern to match.
+ `options`: (optional) An object that specifies optional parameters for the regular expression, such as case-sensitivity and multi-line matching. Supported options are `i` (case-insensitive) and `m` (multi-line).

## Example (MongoDB Shell)
<a name="regexFind-examples"></a>

The following example demonstrates how to use the `$regexFind` operator to search for documents where the `name` field matches a specific regular expression pattern.

**Create sample documents**

```
db.users.insertMany([
  { "_id": 1, name: "John Doe", email: "john@example.com" },
  { "_id": 2, name: "Diego Ramirez", email: "diego@example.com" },
  { "_id": 3, name: "Alejandro Rosalez", email: "alejandro@example.com" },
  { "_id": 4, name: "Shirley Rodriguez", email: "shirley@example.com" }
]);
```

**Query example**

```
db.users.aggregate([
  {
    $project: {
      names: {
        $regexFind: { input: '$name', regex: 'j', options: 'i' }
      }
    }
  },
  { $match: {names: {$ne: null}}}
])
```

This query will return all documents where the `name` field contains the letter "j" (case-insensitive).

**Output**

```
[
  { _id: 1, names: { match: 'J', idx: 0, captures: [] } }
]
```

**Note:** If your query is using Amazon DocumentDB planner version 1, you must use a hint to utilize an index. Without a hint, the query may perform a collection scan. To check your planner version and learn more about using hints, see [Query planner v2](query-planner.md).

## Code examples
<a name="regexFind-code"></a>

To view a code example for using the `$regexFind` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const results = await users.aggregate([
    { $project: { names: { $regexFind: { input: "$name", regex: "john", options: "i" }}}},
    { $match: {names: {$ne: null}}}
  ]).toArray();
  

  console.log(results);

  await client.close();
}

main();
```

------
#### [ Python ]

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
users = db['users']

results = list(users.aggregate([
    { "$project": { "names": { "$regexFind": { "input": "$name", "regex": "john", "options": "i" }}}},
    { "$match": {"names": {"$ne": None}}}
]))

print(results)

client.close()
```

------