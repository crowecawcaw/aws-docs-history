

# $search
<a name="search"></a>

New from version 5.0.

The `$search` operator in Amazon DocumentDB is used to provide text search capabilities.

**Parameters**

None

## Example (MongoDB Shell)
<a name="search-examples"></a>

The following example demonstrates how to use the `$search` operator to perform a text search query.

**Create sample documents**

```
db.textcollection.createIndex({"description": "text"});

db.textcollection.insertMany([
  { _id: 1, name: "John Doe", description: "This is a sample document about John Doe." },
  { _id: 2, name: "Jane Smith", description: "This is a sample document about Jane Smith." },
  { _id: 3, name: "Bob Johnson", description: "This is a sample document about Bob Johnson." },
  { _id: 4, name: "Jon Jeffries", description: "This is a sample document about Jon Jeffries." }
]);
```

**Query example**

```
db.textcollection.find(
  { $text: { $search: "John" } }
);
```

**Output**

```
[
  {
    _id: 1,
    name: 'John Doe',
    description: 'This is a sample document about John Doe.'
  }
]
```

## Code examples
<a name="search-code"></a>

To view a code example for using the `$search` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findWithText() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('textcollection');

  const result = await collection.find(
    { $text: { $search: "John" } }
  ).sort({ score: { $meta: "textScore" } }).toArray();

  console.log(result);
  client.close();
}

findWithText();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_with_text():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['textcollection']

    result = list(collection.find(
        { '$text': { '$search': 'John' } }
    ))

    print(result)
    client.close()

find_with_text()
```

------