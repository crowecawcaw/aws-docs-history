

# $currentDate
<a name="currentDate"></a>

The `$currentDate` operator is used to set the value of a field to the current date and time. This operator is useful for automatically updating a field with the current timestamp when a document is inserted or updated.

**Parameters**
+ `field`: The field to update with the current date and time.
+ `type`: (optional) Specifies the BSON type to use for the current date. Can be either `date` or `timestamp`.

## Example (MongoDB Shell)
<a name="currentDate-examples"></a>

The following example demonstrates how to use the `$currentDate` operator to set the `lastModified` field to the current date and time when a new document is inserted.

**Create sample documents**

```
db.users.insert({
  name: "John Doe",
  email: "john.doe@example.com"
})
```

**Query example**

```
db.users.updateOne(
  { name: "John Doe" },
  { $currentDate: { lastModified: true } }
)
```

**View updated document**

```
db.users.findOne({ name: "John Doe" })
```

**Output**

```
{
  _id: ObjectId('...'),
  name: 'John Doe',
  email: 'john.doe@example.com',
  lastModified: ISODate('2025-10-25T22:50:29.963Z')
}
```

## Code examples
<a name="currentDate-code"></a>

To view a code example for using the `$currentDate` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function updateUserWithCurrentDate() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const users = db.collection('users');

  await users.updateOne(
    { name: 'John Doe' },
    { $currentDate: { lastModified: true } }
  );

  console.log('User updated with current date');
  client.close();
}

updateUserWithCurrentDate();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def update_user_with_current_date():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    users = db.users

    result = users.update_one(
        {'name': 'John Doe'},
        {'$currentDate': {'lastModified': True}}
    )

    print('User updated with current date')
    client.close()

update_user_with_current_date()
```

------