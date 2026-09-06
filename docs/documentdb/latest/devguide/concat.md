

# $concat
<a name="concat"></a>

The `$concat` aggregation operator in Amazon DocumentDB concatenates (or combines) multiple strings in a document to produce a single string that can be returned to the application. This reduces the work done in the application, as the string manipulation is performed at the database level.

**Parameters**
+ `expression1`: The first string to concatenate.
+ `expression2`: The second string to concatenate.
+ `...`: Additional strings to concatenate (optional).

## Example (MongoDB Shell)
<a name="concat-examples"></a>

In this example, we concatenate the first and last names of users to produce each person's full name.

**Create sample documents**

```
db.people.insertMany([
  { "_id":1, "first_name":"Jane", "last_name":"Doe", "DOB":"2/1/1999", "Desk": "MSP102-MN"},
  { "_id":2, "first_name":"John", "last_name":"Doe", "DOB":"12/21/1992", "Desk": "DSM301-IA"},
  { "_id":3, "first_name":"Steve", "last_name":"Smith", "DOB":"3/21/1981", "Desk":"MKE233-WI"}
])
```

**Query example**

```
db.people.aggregate([
  { $project: { full_name: { $concat: [ "$first_name", " ", "$last_name"] } } }
])
```

**Output**

```
{ "_id" : 1, "full_name" : "Jane Doe" }
{ "_id" : 2, "full_name" : "John Doe" }
{ "_id" : 3, "full_name" : "Steve Smith" }
```

## Code examples
<a name="concat-code"></a>

To view a code example for using the `$concat` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function concatenateNames() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');

  const result = await db.collection('people').aggregate([
    { $project: { full_name: { $concat: [ "$first_name", " ", "$last_name"] } } }
  ]).toArray();

  console.log(result);

  await client.close();
}

concatenateNames();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def concatenate_names():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']

    result = list(db.people.aggregate([
        { '$project': { 'full_name': { '$concat': [ '$first_name', ' ', '$last_name' ] } } }
    ]))

    print(result)

    client.close()

concatenate_names()
```

------