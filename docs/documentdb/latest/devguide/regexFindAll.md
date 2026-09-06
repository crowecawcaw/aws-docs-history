

# $regexFindAll
<a name="regexFindAll"></a>

Introduced in 5.0

The `$regexFindAll` operator in Amazon DocumentDB is used to perform regular expression matching on string fields within documents. It allows you to search for and extract specific substrings that match a given regular expression pattern, returning all matches of the regular expression.

**Parameters**
+ `input`: The string field or expression to search.
+ `regex`: The regular expression pattern to match.
+ `options`: (optional) An object that specifies optional parameters for the regular expression, such as case-sensitivity and multi-line matching. Supported options are `i` (case-insensitive) and `m` (multi-line).

## Example (MongoDB Shell)
<a name="regexFindAll-examples"></a>

The following example demonstrates how to use the `$regexFindAll` operator to extract all letter sequences from the `email` field.

**Create sample documents**

```
db.users.insertMany([
  { _id: 1, name: "John Doe", email: "john@example.com", phone: "555-1234" },
  { _id: 2, name: "Jane Roe", email: "jane@example.com", phone: "555-5678" },
  { _id: 3, name: "Carlos Salazar", email: "carlos@example.com", phone: "555-3456" },
  { _id: 4, name: "Saanvi Sarkar", email: "saanvi@example.com", phone: "555-7890" }
  
]);
```

**Query example**

```
db.users.aggregate([
  {
    $project: {
      name: 1,
      emailMatches: {
        $regexFindAll: { input: '$email', regex: '[a-z]+', options: 'i' }
      }
    }
  }
])
```

**Output**

```
[
  {
    _id: 1,
    name: 'John Doe',
    emailMatches: [
      { match: 'john', idx: 0, captures: [] },
      { match: 'example', idx: 5, captures: [] },
      { match: 'com', idx: 13, captures: [] }
    ]
  },
  {
    _id: 2,
    name: 'Jane Roe',
    emailMatches: [
      { match: 'jane', idx: 0, captures: [] },
      { match: 'example', idx: 5, captures: [] },
      { match: 'com', idx: 13, captures: [] }
    ]
  },
  {
    _id: 3,
    name: 'Carlos Salazar',
    emailMatches: [
      { match: 'carlos', idx: 0, captures: [] },
      { match: 'example', idx: 7, captures: [] },
      { match: 'com', idx: 15, captures: [] }
    ]
  },
  {
    _id: 4,
    name: 'Saanvi Sarkar',
    emailMatches: [
      { match: 'saanvi', idx: 0, captures: [] },
      { match: 'example', idx: 7, captures: [] },
      { match: 'com', idx: 15, captures: [] }
    ]
  }
]
```

**Note:** If your query is using Amazon DocumentDB planner version 1, you must use a hint to utilize an index. Without a hint, the query may perform a collection scan. To check your planner version and learn more about using hints, see [Query planner v2](query-planner.md).

## Code examples
<a name="regexFindAll-code"></a>

To view a code example for using the `$regexFindAll` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

Here's an example of using the `$regexFind` operator in a Node.js application:

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  const results = await users.aggregate([
    {
      $project: {
        name: 1,
        emailMatches: {
          $regexFindAll: { input: "$email", regex: "[a-z]+", options: "i" }
        }
      }
    }
  ]).toArray();
  
  console.log(JSON.stringify(results, null, 2));

  await client.close();
}

main();
```

------
#### [ Python ]

Here's an example of using the `$regexFind` operator in a Python application:

```
from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
db = client['test']
users = db['users']

results = list(users.aggregate([
    { 
        "$project": { 
            "name": 1,
            "emailMatches": { 
                "$regexFindAll": { 
                    "input": "$email", 
                    "regex": "[a-z]+", 
                    "options": "i" 
                }
            }
        }
    }
]))

print(results)

client.close()
```

------