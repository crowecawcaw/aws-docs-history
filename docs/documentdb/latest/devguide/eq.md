

# $eq
<a name="eq"></a>

The `$eq` operator in Amazon DocumentDB is used to match documents where the value of a field is equal to the specified value. This operator is commonly used in the `find()` method to retrieve documents that meet the specified criteria.

**Parameters**
+ `field` : The field to check for the equality condition.
+ `value` : The value to compare against the field.

## Example (MongoDB Shell)
<a name="eq-examples"></a>

The following example demonstrates the usage of the `$eq` operator to find all documents where the `name` field is equal to `"Thai Curry Palace"`.

**Create sample documents**

```
db.restaurants.insertMany([
  { name: "Thai Curry Palace", cuisine: "Thai", features: ["Private Dining"] },
  { name: "Italian Bistro", cuisine: "Italian", features: ["Outdoor Seating"] },
  { name: "Mexican Grill", cuisine: "Mexican", features: ["Takeout"] }
]);
```

**Query example**

```
db.restaurants.find({ name: { $eq: "Thai Curry Palace" } });
```

**Output**

```
{ "_id" : ObjectId("68ee586f916df9d39f3d9414"), "name" : "Thai Curry Palace", "cuisine" : "Thai", "features" : [ "Private Dining" ] }
```

## Code examples
<a name="eq-code"></a>

To view a code example for using the `$eq` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function findByName(name) {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('restaurants');

  const results = await collection.find({ name: { $eq: name } }).toArray();
  console.log(results);

  await client.close();
}

findByName("Thai Curry Palace");
```

------
#### [ Python ]

```
from pymongo import MongoClient

def find_by_name(name):
    client = MongoClient("mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
    db = client["test"]
    collection = db["restaurants"]

    results = list(collection.find({ "name": { "$eq": name } }))
    print(results)

    client.close()

find_by_name("Thai Curry Palace")
```

------