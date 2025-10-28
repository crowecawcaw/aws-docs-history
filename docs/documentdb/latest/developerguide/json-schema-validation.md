# Using JSON schema validation

Using the `$jsonSchema` evaluation query operator, you can validate documents being inserted into your collections.

###### Topics

- [Creating and using JSON schema validation](#get-started-with-validation "#get-started-with-validation")
- [Supported keywords](#json-supported-keywords "#json-supported-keywords")
- [bypassDocumentValidation](#json-schema-bypass "#json-schema-bypass")
- [Limitations](#json-schema-limitations "#json-schema-limitations")

## Creating and using JSON schema validation

### Creating a collection with schema validation

You can create a collection with `createCollection` operation and validation rules.
These validation rules are applied during inserts or updates of Amazon DocumentDB documents.
The following code example shows validation rules for a collection of employees:

```
db.createCollection("employees", {
   "validator": {
      "$jsonSchema": {
         "bsonType": "object",
         "title": "employee validation",
         "required": [ "name", "employeeId"],
         "properties": {
            "name": {
                  "bsonType": "object",
                  "properties": {
                     "firstName": {
                        "bsonType": ["string"]
                     },
                     "lastName": {
                        "bsonType": ["string"]
                     }
                  },
                  "additionalProperties" : false
            },
            "employeeId": {
               "bsonType": "string",
               "description": "Unique Identifier for employee"
            },
             "salary": {
               "bsonType": "double"
            },
            "age": {
               "bsonType": "number"
            }
         },
         "additionalProperties" : true
      }
   },
   "validationLevel": "strict", "validationAction": "error"
} )
```

### Inserting a valid document

The following example inserts documents that comply with the above schema validation rules:

```
db.employees.insert({"name" : { "firstName" : "Carol" , "lastName" : "Smith"}, "employeeId": "c720a" , "salary": 1000.0 })
db.employees.insert({ "name" : { "firstName" : "William", "lastName" : "Taylor" }, "employeeId" : "c721a", "age" : 24})
```

### Inserting an invalid document

The following example inserts documents that do not comply with the above schema validation rules.
In this example, the employeeId value is not a string:

```
db.employees.insert({
    "name" : { "firstName" : "Carol" , "lastName" : "Smith"},
    "employeeId": 720 ,
    "salary": 1000.0
})
```

This example shows incorrect syntax within the document.

### Modifying a collection

The `collMod` command is used to add or modify validation rules of existing collection.
The following example adds a salary field to the required field list:

```
db.runCommand({"collMod" : "employees",
   "validator": {
      "$jsonSchema": {
         "bsonType": "object",
         "title": "employee validation",
         "required": [ "name", "employeeId", "salary"],
         "properties": {
            "name": {
                  "bsonType": "object",
                  "properties": {
                     "firstName": {
                        "bsonType": ["string"]
                     },
                     "lastName": {
                        "bsonType": ["string"]
                     }
                  },
                  "additionalProperties" : false
            },
            "employeeId": {
               "bsonType": "string",
               "description": "Unique Identifier for employee"
            },
             "salary": {
               "bsonType": "double"
            },
            "age": {
               "bsonType": "number"
            }
         },
         "additionalProperties" : true
      }
   }
} )
```

### Addressing documents added before the validation rules were changed

To address documents that were added to you collection before the validation rules were changed, use the following `validationLevel` modifiers:

- **strict**: Applies validation rules on all inserts and updates.
- **moderate**: Applies validation rules to existing valid documents.
  During updates, existing invalid documents are not checked.

In the following example, after updating the validation rules on the collection named “employees”, the salary field is required.
Updating following document will fail:

```
db.runCommand({
    update: "employees",
    updates: [{
        q: { "employeeId": "c721a" },
        u: { age: 25 , salary : 1000},
        upsert: true }]
})
```

Amazon DocumentDB returns the following output:

```
{
"n" : 0,
    "nModified" : 0,
    "writeErrors" : [
        {
"index" : 0,
            "code" : 121,
            "errmsg" : "Document failed validation"
        }
    ],
    "ok" : 1,
    "operationTime" : Timestamp(1234567890, 1)
}
```

Updating the validation level to `moderate` will allow the above document to be updated successfully:

```
db.runCommand({
    "collMod" : "employees",
    validationLevel : "moderate"
})

db.runCommand({
    update: "employees",
    updates: [{
        q: { "employeeId": "c721a" },
        u: { age: 25 , salary : 1000},
        upsert: true }]
})
```

Amazon DocumentDB returns the following output:

```
{
"n" : 1,
    "nModified" : 1,
    "ok" : 1,
    "operationTime" : Timestamp(1234567890, 1)
}
```

### Retrieving documents with the $jsonSchema

The `$jsonSchema` operator can be used as a filter to query documents that match the JSON schema.
This is a top-level operator which can be present in filter documents as a top level field or used with query operators such as `$and`, `$or`, and `$nor`.
The following examples show the use of $jsonSchema as an individual filter and with other filter operators:

Document inserted into an "employee" collection:

```
{ "name" : { "firstName" : "Carol", "lastName" : "Smith" }, "employeeId" : "c720a", "salary" : 1000 }
{ "name" : { "firstName" : "Emily", "lastName" : "Brown" }, "employeeId" : "c720b", "age" : 25, "salary" : 1050.2 }
{ "name" : { "firstName" : "William", "lastName" : "Taylor" }, "employeeId" : "c721a", "age" : 24, "salary" : 1400.5 }
{ "name" : { "firstName" : "Jane", "lastName" : "Doe" }, "employeeId" : "c721a", "salary" : 1300 }
```

Collection filtered with the `$jsonSchema` operator only:

```
db.employees.find({
       $jsonSchema: { required: ["age"] } })
```

Amazon DocumentDB returns the following output:

```
{ "_id" : ObjectId("64e5f91c6218c620cf0e8f8b"), "name" : { "firstName" : "Emily", "lastName" : "Brown" }, "employeeId" : "c720b", "age" : 25, "salary" : 1050.2 }
{ "_id" : ObjectId("64e5f94e6218c620cf0e8f8c"), "name" : { "firstName" : "William", "lastName" : "Taylor" }, "employeeId" : "c721a", "age" : 24, "salary" : 1400.5 }
```

Collection filtered with the `$jsonSchema` operator and another operator:

```
db.employees.find({
       $or: [{ $jsonSchema: { required: ["age", "name"]}},
            { salary: { $lte:1000}}]});
```

Amazon DocumentDB returns the following output:

```
{ "_id" : ObjectId("64e5f8886218c620cf0e8f8a"), "name" : { "firstName" : "Carol", "lastName" : "Smith" }, "employeeId" : "c720a", "salary" : 1000 }
{ "_id" : ObjectId("64e5f91c6218c620cf0e8f8b"), "name" : { "firstName" : "Emily", "lastName" : "Brown" }, "employeeId" : "c720b", "age" : 25, "salary" : 1050.2 }
{ "_id" : ObjectId("64e5f94e6218c620cf0e8f8c"), "name" : { "firstName" : "William", "lastName" : "Taylor" }, "employeeId" : "c721a", "age" : 24, "salary" : 1400.5 }
```

Collection filtered with the `$jsonSchema` operator and with `$match` in the aggregate filter:

```
db.employees.aggregate(
    [{ $match: {
        $jsonSchema: {
            required: ["name", "employeeId"],
            properties: {"salary" :{"bsonType": "double"}}
        }
       }
    }]
)
```

Amazon DocumentDB returns the following output:

```
{
"_id" : ObjectId("64e5f8886218c620cf0e8f8a"),
 "name" : { "firstName" : "Carol", "lastName" : "Smith" },
"employeeId" : "c720a",
"salary" : 1000
}
{
"_id" : ObjectId("64e5f91c6218c620cf0e8f8b"),
"name" : { "firstName" : "Emily", "lastName" : "Brown" },
"employeeId" : "c720b",
"age" : 25,
"salary" : 1050.2
}
{
"_id" : ObjectId("64e5f94e6218c620cf0e8f8c"),
"name" : { "firstName" : "William", "lastName" : "Taylor" },
"employeeId" : "c721a",
"age" : 24,
"salary" : 1400.5
}
{
"_id" : ObjectId("64e5f9786218c620cf0e8f8d"),
"name" : { "firstName" : "Jane", "lastName" : "Doe" },
"employeeId" : "c721a",
"salary" : 1300
}
```

### Viewing existing validation rules

To see the existing validation rules on a collection, use:

```
db.runCommand({
    listCollections: 1,
    filter: { name: 'employees' }
})
```

Amazon DocumentDB returns the following output:

```
{
    "waitedMS" : NumberLong(0),
    "cursor" : {
        "firstBatch" : [
            {
                "name" : "employees",
                "type" : "collection",
                "options" : {
                    "autoIndexId" : true,
                    "capped" : false,
                    "validator" : {
                        "$jsonSchema" : {
                            "bsonType" : "object",
                            "title" : "employee validation",
                            "required" : [
                                "name",
                                "employeeId",
                                "salary"
                            ],
                            "properties" : {
                                "name" : {
                                    "bsonType" : "object",
                                    "properties" : {
                                        "firstName" : {
                                            "bsonType" : [
                                                "string"
                                            ]
                                        },
                                        "lastName" : {
                                            "bsonType" : [
                                                "string"
                                            ]
                                        }
                                    },
                                    "additionalProperties" : false
                                },
                                "employeeId" : {
                                    "bsonType" : "string",
                                    "description" : "Unique Identifier for employee"
                                },
                                "salary" : {
                                    "bsonType" : "double"
                                },
                                "age" : {
                                    "bsonType" : "number"
                                }
                            },
                            "additionalProperties" : true
                        }
                    },
                    "validationLevel" : "moderate",
                    "validationAction" : "error"
                },
                "info" : {
                    "readOnly" : false
                },
                "idIndex" : {
                    "v" : 2,
                    "key" : {
                        "_id" : 1
                    },
                    "name" : "_id_",
                    "ns" : "test.employees"
                }
            }
        ],
        "id" : NumberLong(0),
        "ns" : "test.$cmd.listCollections"
    },
    "ok" : 1,
    "operationTime" : Timestamp(1692788937, 1)
}
```

Amazon DocumentDB also retains validation rules in the `$out` aggregation stage.

## Supported keywords

The following fields are supported in the `create` and `collMod` commands:

- **`Validator`** — Supports the `$jsonSchem`a operator.
- **`ValidationLevel`** — Supports `off`, `strict`, and `moderate` values.
- **`ValidationAction`** — Supports the `error` value.

The $jsonSchema operator supports the following keywords:

- `additionalItems`
- `additionalProperties`
- `allOf`
- `anyOf`
- `bsonType`
- `dependencies`
- `description`
- `enum`
- `exclusiveMaximum`
- `exclusiveMinimum`
- `items`
- `maximum`
- `minimum`
- `maxItems`
- `minItems`
- `maxLength`
- `minLength`
- `maxProperties`
- `minProperties`
- `multipleOf`
- `not`
- `oneOf`
- `pattern`
- `patternProperties`
- `properties`
- `required`
- `title`
- `type`
- `uniqueItems`

## bypassDocumentValidation

Amazon DocumentDB supports `bypassDocumentValidation` for the following commands and methods:

- `insert`
- `update`
- `findAndModify`
- `$out` stage in `aggregate` command and in `db.collection.aggregate()` method

Amazon DocumentDB does not support the following commands for `bypassDocumentValidation`:

- `$merge` in `aggregate` command and in `db.collection.aggregate()` method
- `mapReduce` command and `db.collection.mapReduce()` method
- `applyOps` command

## Limitations

The following limitations apply to `$jsonSchema` validation:

- Amazon DocumentDB returns the error "Document failed validation" when an operation fails the validation rule.
- Amazon DocumentDB elastic clusters do not support `$jsonSchema`.
