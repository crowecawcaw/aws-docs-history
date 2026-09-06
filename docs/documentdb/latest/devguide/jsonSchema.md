

# $jsonSchema
<a name="jsonSchema"></a>

New from version 4.0.

Not supported by Elastic cluster.

The `$jsonSchema` operator in Amazon DocumentDB is used to filter documents based on a specified JSON schema. This operator allows you to query documents that match a particular JSON schema, ensuring that the retrieved documents adhere to specific structural and data type requirements.

Using the `$jsonSchema` evaluation query operator as part of a collection creation, you can validate the schema of the documents being inserted into the collection. See [Using JSON schema validation](json-schema-validation.md) for additional information.

**Parameters**
+ `required` (array): Specifies the required fields in the document.
+ `properties` (object): Defines the data type and other constraints for each field in the document.

## Example (MongoDB Shell)
<a name="jsonSchema-examples"></a>

The following example demonstrates the use of the `$jsonSchema` operator to filter the `employees` collection to only retrieve documents that have the `name`, `employeeId` and `age` fields, and the `employeeId` field is of type `string`.

**Create sample documents**

```
db.employees.insertMany([
  { "name": { "firstName": "Carol", "lastName": "Smith" }, "employeeId": "1" },
  { "name": { "firstName": "Emily", "lastName": "Brown" }, "employeeId": "2", "age": 25 },
  { "name": { "firstName": "William", "lastName": "Taylor" }, "employeeId": 3, "age": 24 },
  { "name": { "firstName": "Jane", "lastName": "Doe" }, "employeeId": "4" }
]);
```

**Query example**

```
db.employees.aggregate([
  { $match: {
    $jsonSchema: {
      required: ["name", "employeeId", "age"],
      properties: { "employeeId": { "bsonType": "string" } }
    }
  }}
]);
```

**Output**

```
{ "_id" : ObjectId("6908e8b61f77fc26b2ecd26f"), "name" : { "firstName" : "Emily", "lastName" : "Brown" }, "employeeId" : "2", "age" : 25 }
```

## Code examples
<a name="jsonSchema-code"></a>

To view a code example for using the `$jsonSchema` command, choose the tab for the language that you want to use:

------
#### [ Node.js ]

```
const { MongoClient } = require('mongodb');

async function filterByJsonSchema() {
  const client = await MongoClient.connect('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false');
  const db = client.db('test');
  const collection = db.collection('employees');

  const result = await collection.aggregate([
    {
      $match: {
        $jsonSchema: {
          required: ['name', 'employeeId', 'age'],
          properties: { 'employeeId': { 'bsonType': 'string' } }
        }
      }
    }
  ]).toArray();

  console.log(result);
  await client.close();
}

filterByJsonSchema();
```

------
#### [ Python ]

```
from pymongo import MongoClient

def filter_by_json_schema():
  client = MongoClient('mongodb://<username>:<password>@<cluster-endpoint>:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
  db = client['test']
  collection = db['employees']

  result = list(collection.aggregate([
    {
      '$match': {
        '$jsonSchema': {
          'required': ['name', 'employeeId', 'age'],
          'properties': {'employeeId': {'bsonType': 'string'}}
        }
      }
    }
  ]))

  print(result)
  client.close()

filter_by_json_schema()
```

------