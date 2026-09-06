

# $position
<a name="position"></a>

The `$position` modifier in Amazon DocumentDB specifies the location in the array at which the `$push` operator inserts elements. Without the `$position` modifier, the `$push` operator inserts elements to the end of the array.

**Parameters**
+ `field`: The array field to update.
+ `num`: The position in the array where elements should be inserted, based on zero-based indexing.

**Note**: To use the `$position` modifier, it must appear with the `$each` modifier.

## Example (MongoDB Shell)
<a name="position-examples"></a>

The following example demonstrates how to use the `$position` operator to insert tasks at specific positions in a project management system.

**Create sample documents**

```
db.projects.insertOne({ "_id": 1, "name": "Website Redesign", "tasks": ["Design mockups"] })
```

**Query example 1 - Add urgent tasks at the beginning**

```
db.projects.updateOne(
   { _id: 1 },
   {
     $push: {
        tasks: {
           $each: ["Security audit", "Performance review"],
           $position: 0
        }
     }
   }
)
```

**Output 1**

```
{ "_id": 1, "name": "Website Redesign", "tasks": ["Security audit", "Performance review", "Design mockups"] }
```

**Query example 2 - Add tasks at specific position**

```
db.projects.insertOne({ "_id": 2, "name": "Mobile App", "tasks": ["Setup project", "Create wireframes", "Deploy to store"] })

db.projects.updateOne(
   { _id: 2 },
   {
     $push: {
        tasks: {
           $each: ["Code review", "Testing phase"],
           $position: 2
        }
     }
   }
)
```

**Output 2**

```
{ "_id": 2, "name": "Mobile App", "tasks": ["Setup project", "Create wireframes", "Code review", "Testing phase", "Deploy to store"] }
```

## Code examples
<a name="position-code"></a>

To view a code example for using the `$position` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function insertTasksAtPosition() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('projects');

  await collection.updateOne(
    { _id: 1 },
    {
      $push: {
        tasks: {
          $each: ["Security audit", "Performance review"],
          $position: 0
        }
      }
    }
  );

  const updatedProject = await collection.findOne({ _id: 1 });
  console.log(updatedProject);

  await client.close();
}

insertTasksAtPosition();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def insert_tasks_at_position():
    client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
    db = client['test']
    collection = db['projects']

    result = collection.update_one(
        {'_id': 1},
        {
            '$push': {
                'tasks': {
                    '$each': ['Security audit', 'Performance review'],
                    '$position': 0
                }
            }
        }
    )

    updated_project = collection.find_one({'_id': 1})
    print(updated_project)

    client.close()

insert_tasks_at_position()
```

------