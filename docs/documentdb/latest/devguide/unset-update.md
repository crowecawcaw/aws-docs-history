

# $unset
<a name="unset-update"></a>

The `$unset` operator in Amazon DocumentDB is used to remove a specified field from a document. When a field is removed using `$unset`, the field is deleted from the document, and the document size is reduced accordingly. This can be useful when you want to remove unnecessary data from your documents.

**Parameters**
+ `field`: The field to remove from the document. This can be a single field or a dotted path to a nested field.

## Example (MongoDB Shell)
<a name="unset-examples"></a>

The following example demonstrates how to use the `$unset` operator to remove the `Words` field from a document in the `example` collection.

**Create sample documents**

```
db.example.insert({
    "DocName": "Document 1",
    "Date": {
        "Month": 4,
        "Day": 18,
        "Year": 1987,
        "DoW": "Saturday"
    },
    "Words": 2482
})
```

**Query example**

```
db.example.update(
    { "DocName" : "Document 1" },
    { $unset: { Words:1 } }
)
```

**Output**

```
{
    "DocName": "Document 1",
    "Date": {
        "Month": 4,
        "Day": 18,
        "Year": 1987,
        "DoW": "Saturday"
    }
}
```

In this example, the `$unset` operator is used to remove the `Words` field from the document with `DocName` equal to "Document 1". The resulting document no longer contains the `Words` field.

## Code examples
<a name="unset-code"></a>

To view a code example for using the `$unset` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function removeField() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('example');

  const result = await collection.updateOne(
    { "DocName": "Document 1" },
    { $unset: { "Words": 1 } }
  );

  console.log(`Modified ${result.modifiedCount} document(s)`);
  client.close();
}

removeField();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def remove_field():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['example']

    result = collection.update_one(
        {"DocName": "Document 1"},
        {"$unset": {"Words": 1}}
    )

    print(f"Modified {result.modified_count} document(s)")
    client.close()

remove_field()
```

------