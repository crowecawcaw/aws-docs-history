

# $regex
<a name="regex"></a>

The `$regex` operator allows you to perform regular expression matching on string fields. It is a powerful tool for searching and filtering documents based on complex patterns.

**Parameters**
+ `regular expression`: The regular expression pattern to match against the field.
+ `$options`: (optional) Provides options to modify the search behavior, such as case-sensitivity, global matching, etc.

## Example (MongoDB Shell)
<a name="regex-examples"></a>

The following example demonstrates the usage of the `$regex` operator to search for documents where the "name" field matches a specific pattern.

**Create sample documents**

```
db.users.insertMany([
  { name: "John Doe" },
  { name: "Jane Smith" },
  { name: "Alice Johnson" },
  { name: "Bob Williams" },
  { name: "Charlie Davis" }
]);
```

**Query example**

```
db.users.find({ name: { $regex: /^A/ } })
```

**Output**

```
[
  { "_id" : ObjectId("..."), "name" : "Alice Johnson" }
]
```

This query will return all documents where the "name" field starts with the letter "A".

## Code examples
<a name="regex-code"></a>

To view a code example for using the `$regex` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function main() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('users');

  const results = await collection.find({ name: { $regex: /^A/ } }).toArray();
  console.log(results);

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
    collection = db['users']

    results = list(collection.find({ 'name': { '$regex': '^A' } }))
    print(results)

    client.close()

if __name__ == "__main__":
    main()
```

------