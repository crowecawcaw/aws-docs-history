

# $text
<a name="text"></a>

The `$text` operator is used to perform full-text search on text-indexed fields within a document collection. This operator allows you to search for documents that contain specific words or phrases, and can be combined with other query operators to filter results based on additional criteria.

**Parameters**
+ `$search`: The text string to search for.

## Example (MongoDB Shell)
<a name="text-examples"></a>

The following example demonstrates how to use the `$text` operator to search for documents containing the word "interest" and filter the results based on a "star\_rating" field.

**Create sample documents**

```
db.test.insertMany([
  { "_id": 1, "star_rating": 4, "comments": "apple is red" },
  { "_id": 2, "star_rating": 5, "comments": "pie is delicious" },
  { "_id": 3, "star_rating": 3, "comments": "apples, oranges - healthy fruit" },
  { "_id": 4, "star_rating": 2, "comments": "bake the apple pie in the oven" },
  { "_id": 5, "star_rating": 5, "comments": "interesting couch" },
  { "_id": 6, "star_rating": 5, "comments": "interested in couch for sale, year 2022" }
]);
```

**Create text index**

```
db.test.createIndex({ comments: "text" });
```

**Query example**

```
db.test.find({$and: [{star_rating: 5}, {$text: {$search: "interest"}}]})
```

**Output**

```
{ "_id" : 5, "star_rating" : 5, "comments" : "interesting couch" }
{ "_id" : 6, "star_rating" : 5, "comments" : "interested in couch for sale, year 2022" }
```

The command above returns documents with a text-indexed field containing any form of "interest" and a "star\_rating" equal to 5.

## Code examples
<a name="text-code"></a>

To view a code example for using the `$text` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function searchDocuments() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('test');

  const result = await collection.find({
    $and: [
      { star_rating: 5 },
      { $text: { $search: 'interest' } }
    ]
  }).toArray();

  console.log(result);
  client.close();
}

searchDocuments();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def search_documents():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db.test

    result = list(collection.find({
        '$and': [
            {'star_rating': 5},
            {'$text': {'$search': 'interest'}}
        ]
    }))

    print(result)
    client.close()

search_documents()
```

------