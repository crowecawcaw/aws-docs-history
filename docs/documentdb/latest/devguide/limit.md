

# $limit
<a name="limit"></a>

The `$limit` operator in Amazon DocumentDB is used to restrict the number of documents returned by a query. It is similar to the MongoDB `$limit` operator, but there are some specific considerations when using it with Amazon DocumentDB.

In Amazon DocumentDB, the `$limit` operator is useful for pagination, where you want to retrieve a subset of the total matching documents. It allows you to control the number of documents returned in each response, improving performance and reducing the amount of data transferred over the network.

**Parameters**
+ `limit`: The maximum number of documents to return. This must be a non-negative integer value.

## Example (MongoDB Shell)
<a name="limit-examples"></a>

The following example demonstrates how to use the `$limit` operator to return a maximum of one document that matches the given filter.

**Create sample documents**

```
db.test.insertMany([
  { "_id": 1, "star_rating": 4, "comments": "apple is red" },
  { "_id": 2, "star_rating": 5, "comments": "comfortable couch" },
  { "_id": 3, "star_rating": 3, "comments": "apples, oranges - healthy fruit" },
  { "_id": 4, "star_rating": 5, "comments": "this is a great couch" },
  { "_id": 5, "star_rating": 5, "comments": "interesting couch" }
]);
```

**Query example**

```
db.test.createIndex({ comments: "text" });

db.test.find({
  $and: [
    { star_rating: 5 },
    { $text: { $search: "couch" } }
  ]
}).limit(1);
```

**Output**

```
[ { _id: 2, star_rating: 5, comments: 'comfortable couch' } ]
```

## Code examples
<a name="limit-code"></a>

To view a code example for using the `$limit` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function limitExample() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');

  try {
      await client.connect();
      
      const db = client.db('test');
      const collection = db.collection('test');

      await collection.createIndex({ comments: 'text' });

      const query = {
        $and: [
          { star_rating: 5 },
          { $text: { $search: "couch" } }
        ]
      };

      const result = await collection.find(query).limit(1).toArray();

      console.log(result);

    } catch (err) {
        console.error("Error:", err);
    } finally {
        await client.close();
    }

}

limitExample();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def limit_example():
    try:
        client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')

        db = client['test']
        collection = db['test']

        collection.create_index([('comments', 'text')])

        query = {
            '$and': [
                {'star_rating': 5},
                {'$text': {'$search': 'couch'}}
            ]
        }

        result = collection.find(query).limit(1)

        for doc in result:
            print(doc)

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        client.close()

limit_example()
```

------