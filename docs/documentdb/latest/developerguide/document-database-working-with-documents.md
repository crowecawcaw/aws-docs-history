# Working with documents

As a document database, Amazon DocumentDB makes it easy to store, query, and
index JSON data. In Amazon DocumentDB, a collection is analogous to a table in
a relational database, except there is no single schema enforced upon
all documents. Collections let you group similar documents together
while keeping them all in the same database, without requiring that
they be identical in structure.

Using the example documents from earlier sections, it is likely
that you'd have collections for `reading_material` and
`office_supplies`. It is the responsibility of your
software to enforce which collection a document belongs in.

The following examples use the MongoDB API to show how to add,
query, update, and delete documents.

###### Topics

- [Adding documents](#document-database-adding-documents "#document-database-adding-documents")
- [Querying documents](#document-database-queries "#document-database-queries")
- [Updating documents](#document-database-updating "#document-database-updating")
- [Deleting documents](#document-database-deleting "#document-database-deleting")

## Adding documents

In Amazon DocumentDB, a database is created when first you add a document
to a collection. In this example, you are creating a collection
named `example` in the `test` database,
which is the default database when you connect to a cluster.
Because the collection is implicitly created when the first
document is inserted, there is no error checking of the collection
name. Therefore, a typo in the collection name, such as
`eexample` instead of `example`, will create
and add the document to `eexample` collection rather
than the intended collection. Error checking must be handled by
your application.

The following examples use the MongoDB API to add documents.

###### Topics

- [Adding a single document](#document-database-adding-documents-single "#document-database-adding-documents-single")
- [Adding multiple documents](#document-database-adding-documents-multiple "#document-database-adding-documents-multiple")

### Adding a single document

To add a single document to a collection, use the `insertOne( {} )` operation with the document that you want added to the
collection.

```
db.example.insertOne(
    {
        "Item": "Ruler",
        "Colors": ["Red","Green","Blue","Clear","Yellow"],
        "Inventory": {
            "OnHand": 47,
            "MinOnHand": 40
        },
        "UnitPrice": 0.89
    }
)
```

Output from this operation looks something like the following (JSON format).

```
{
    "acknowledged" : true,
    "insertedId" : ObjectId("5bedafbcf65ff161707de24f")
}
```

### Adding multiple documents

To add multiple documents to a collection, use the `insertMany( [{},...,{}] )` operation with a list of the documents
that you want added to the collection. Although the documents in this particular list have different schemas, they can all be added to the same
collection.

```
db.example.insertMany(
    [
        {
            "Item": "Pen",
            "Colors": ["Red","Green","Blue","Black"],
            "Inventory": {
                "OnHand": 244,
                "MinOnHand": 72
            }
        },
        {
            "Item": "Poster Paint",
            "Colors": ["Red","Green","Blue","Black","White"],
            "Inventory": {
                "OnHand": 47,
                "MinOnHand": 50
            }
        },
        {
            "Item": "Spray Paint",
            "Colors": ["Black","Red","Green","Blue"],
            "Inventory": {
                "OnHand": 47,
                "MinOnHand": 50,
                "OrderQnty": 36
            }
        }
    ]
)
```

Output from this operation looks something like the following (JSON format).

```
{
    "acknowledged" : true,
    "insertedIds" : [
            ObjectId("5bedb07941ca8d9198f5934c"),
            ObjectId("5bedb07941ca8d9198f5934d"),
            ObjectId("5bedb07941ca8d9198f5934e")
    ]
}
```

## Querying documents

At times, you might need to look up your online store's
inventory so that customers can see and purchase what you're
selling. Querying a collection is relatively easy, whether you
want all documents in the collection or only those documents that
satisfy a particular criterion.

To query for documents, use the `find()` operation.
The `find()` command has a single document parameter
that defines the criteria to use in choosing the documents to
return. The output from `find()` is a document
formatted as a single line of text with no line breaks. To format
the output document for easier reading, use `find().pretty()`.
All the examples in this topic use `.pretty()` to
format the output.

Use the four documents you inserted into the `example`
collection in the preceding two exercises —
`insertOne()` and `insertMany()`.

###### Topics

- [Retrieving all documents in a collection](#document-database-queries-all-documents "#document-database-queries-all-documents")
- [Retrieving documents that match a field value](#document-database-queries-match-criteria "#document-database-queries-match-criteria")
- [Retrieving documents that match an embedded document](#document-database-queries-entire-embedded-document "#document-database-queries-entire-embedded-document")
- [Retrieving documents that match a field value in an embedded document](#document-database-queries-embeded-document-field "#document-database-queries-embeded-document-field")
- [Retrieving documents that match an array](#document-database-queries-array-match "#document-database-queries-array-match")
- [Retrieving documents that match a value in an array](#document-database-queries-array-value-match "#document-database-queries-array-value-match")
- [Retrieving documents using operators](#document-database-query-operators "#document-database-query-operators")

### Retrieving all documents in a collection

To retrieve all the documents in your collection, use the
`find()` operation with an empty query document.

The following query returns all documents in the `example` collection.

```
db.example.find( {} ).pretty()
```

### Retrieving documents that match a field value

To retrieve all documents that match a field and value, use
the `find()` operation with a query document that
identifies the fields and values to match.

Using the preceding documents, this query returns all
documents where the "Item" field equals "Pen".

```
db.example.find( { "Item": "Pen" } ).pretty()
```

### Retrieving documents that match an embedded document

To find all the documents that match an embedded document,
use the `find()` operation with a query document
that specifies the embedded document name and all the fields
and values for that embedded document.

When matching an embedded document, the document's embedded
document must have the same name as in the query. In addition,
the fields and values in the embedded document must match the
query.

The following query returns only the "Poster Paint" document.
This is because the "Pen" has different values for
"`OnHand`" and "`MinOnHand`", and "Spray
Paint" has one more field (`OrderQnty`) than the
query document.

```
db.example.find({"Inventory": {
    "OnHand": 47,
    "MinOnHand": 50 } } ).pretty()
```

### Retrieving documents that match a field value in an embedded document

To find all the documents that match an embedded document,
use the `find()` operation with a query document
that specifies the embedded document name and all the fields
and values for that embedded document.

Given the preceding documents, the following query uses
"dot notation" to specify the embedded document and fields
of interest. Any document that matches these are returned,
regardless of what other fields might be present in the
embedded document. The query returns "Poster Paint" and
"Spray Paint" because they both match the specified fields
and values.

```
db.example.find({"Inventory.OnHand": 47, "Inventory.MinOnHand": 50 }).pretty()
```

### Retrieving documents that match an array

To find all documents that match an array, use the
`find()` operation with the array name that you
are interested in and all the values in that array. The query
returns all documents that have an array with that name in
which the array values are identical to and in the same order
as in the query.

The following query returns only the "Pen" because the
"Poster Paint" has an additional color (White), and "Spray
Paint" has the colors in a different order.

```
db.example.find( { "Colors": ["Red","Green","Blue","Black"] } ).pretty()
```

### Retrieving documents that match a value in an array

To find all the documents that have a particular array value,
use the `find()` operation with the array name and
the value that you're interested in.

```
db.example.find( { "Colors": "Red" } ).pretty()
```

The preceding operation returns all three documents because
each of them has an array named `Colors` and the
value "`Red`" somewhere in the array. If you specify
the value "`White`," the query would only return
"Poster Paint."

### Retrieving documents using operators

The following query returns all documents where the
"`Inventory.OnHand`" value is less than 50.

```
db.example.find(
        { "Inventory.OnHand": { $lt: 50 } } )
```

For a listing of supported query operators, see [Query and projection operators](mongo-apis.md#mongo-apis-query "mongo-apis.md#mongo-apis-query").

## Updating documents

Typically, your documents are not static and are updated as
part of your application workflows. The following examples show
some of the ways that you can update documents.

To update an existing document, use the `update()`
operation. The `update()` operation has two document
parameters. The first document identifies which document or
documents to update. The second document specifies the updates to
make.

When you update an existing field — whether that field
is a simple field, an array, or an embedded document — you
specify the field name and its values. At the end of the operation,
it is as though the field in the old document has been replaced
by the new field and values.

###### Topics

- [Updating the values of an existing field](#document-database-updating-existing-fields "#document-database-updating-existing-fields")
- [Adding a new field](#document-database-updating-adding-field "#document-database-updating-adding-field")
- [Replacing an embedded document](#document-database-replacing-embedded-document "#document-database-replacing-embedded-document")
- [Inserting new fields into an embedded document](#document-database-updating-adding-field-embedded "#document-database-updating-adding-field-embedded")
- [Removing a field from a document](#document-database-remove-field "#document-database-remove-field")
- [Removing a field from multiple documents](#document-database-remove-field-all "#document-database-remove-field-all")

### Updating the values of an existing field

Use the following four documents that you added earlier for
the following updating operations.

```
{
    "Item": "Ruler",
    "Colors": ["Red","Green","Blue","Clear","Yellow"],
    "Inventory": {
        "OnHand": 47,
        "MinOnHand": 40
    },
    "UnitPrice": 0.89
},
{
    "Item": "Pen",
    "Colors": ["Red","Green","Blue","Black"],
    "Inventory": {
        "OnHand": 244,
        "MinOnHand": 72
    }
},
{
    "Item": "Poster Paint",
    "Colors": ["Red","Green","Blue","Black","White"],
    "Inventory": {
        "OnHand": 47,
        "MinOnHand": 50
    }
},
{
    "Item": "Spray Paint",
    "Colors": ["Black","Red","Green","Blue"],
    "Inventory": {
        "OnHand": 47,
        "MinOnHand": 50,
        "OrderQnty": 36
    }
}
```

###### To update a simple field

To update a simple field, use `update()`
with `$set` to specify the field name and new
value. The following example changes the `Item`
from "Pen" to "Gel Pen".

```
db.example.update(
    { "Item" : "Pen" },
    { $set: { "Item": "Gel Pen" } }
)
```

Results from this operation look something like the following.

```
{
    "Item": "Gel Pen",
    "Colors": ["Red","Green","Blue","Black"],
    "Inventory": {
        "OnHand": 244,
        "MinOnHand": 72
    }
}
```

###### To update an array

The following example replaces the existing array of
colors with a new array that includes `Orange`
and drops `White` from the list of colors.
The new list of colors is in the order specified in the
`update()` operation.

```
db.example.update(
    { "Item" : "Poster Paint" },
    { $set: { "Colors": ["Red","Green","Blue","Orange","Black"] } }
)
```

Results from this operation look something like the following.

```
{
    "Item": "Poster Paint",
    "Colors": ["Red","Green","Blue","Orange","Black"],
    "Inventory": {
        "OnHand": 47,
        "MinOnHand": 50
    }
}
```

###

Adding a new field

To modify a document by adding one or more new fields, use
the `update()` operation with a query document
that identifies the document to insert into and the new fields
and values to insert using the `$set` operator.

The following example adds the field `UnitPrice`
with the value `3.99` to the Spray Paints document.
Note that the value `3.99` is numeric and not a
string.

```
db.example.update(
    { "Item": "Spray Paint" },
    { $set: { "UnitPrice": 3.99 } }
)
```

Results from this operation look something like the following (JSON format).

```
{
    "Item": "Spray Paint",
    "Colors": ["Black","Red","Green","Blue"],
    "Inventory": {
        "OnHand": 47,
        "MinOnHand": 50,
        "OrderQnty": 36
    }`,
 "UnitPrice": 3.99`
}
```

### Replacing an embedded document

To modify a document by replacing an embedded document, use
the `update()` operation with documents that
identify the embedded document and its new fields and values
using the `$set` operator.

Given the following document.

```
db.example.insert({
    "DocName": "Document 1",
    "Date": {
        "Year": 1987,
        "Month": 4,
        "Day": 18
    }
})
```

###### To replace an embedded document

The following example replaces the current Date document
with a new one that has only the fields `Month`
and `Day`; `Year` has been eliminated.

```
db.example.update(
    { "DocName" : "Document 1" },
    { $set: { "Date": { "Month": 4, "Day": 18 } } }
)
```

Results from this operation look something like the following.

```
{
    "DocName": "Document 1",
    "Date": {
        "Month": 4,
        "Day": 18
    }
}
```

### Inserting new fields into an embedded document

###### To add fields to an embedded document

To modify a document by adding one or more new fields
to an embedded document, use the `update()`
operation with documents that identify the embedded
document and "dot notation" to specify the embedded
document and the new fields and values to insert using
the `$set` operator.

Given the following document, the following code uses "dot
notation" to insert the `Year` and `DoW`
fields to the embedded `Date` document, and
`Words` into the parent document.

```
{
    "DocName": "Document 1",
    "Date": {
        "Month": 4,
        "Day": 18
    }
}
```

```
db.example.update(
    { "DocName" : "Document 1" },
    { $set: { "Date.Year": 1987,
              "Date.DoW": "Saturday",
              "Words": 2482 } }
)
```

Results from this operation look something like the following.

```
{
    "DocName": "Document 1",
    "Date": {
        "Month": 4,
        "Day": 18`,
 "Year": 1987,
 "DoW": "Saturday"`
    }`,
 "Words": 2482`
}
```

### Removing a field from a document

To modify a document by removing a field from the document,
use the `update()` operation with a query document
that identifies the document to remove the field from, and
the `$unset` operator to specify the field to remove.

The following example removes the `Words` field
from the preceding document.

```
db.example.update(
    { "DocName" : "Document 1" },
    { $unset: { Words:1 } }
)
```

Results from this operation look something like the following.

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

### Removing a field from multiple documents

To modify a document by removing a field from multiple
documents, use the `update()` operation with the
`$unset` operator and the `multi`
option set to `true`.

The following example removes the `Inventory`
field from all documents in the example collection. If a
document does not have the `Inventory` field, no
action is taken on that document. If `multi: true`
is omitted, the action is performed only on the first document
that meets the criterion.

```
db.example.update(
    {},
    { $unset: { Inventory:1 } },
    { multi: true }
)

```

## Deleting documents

To remove a document from your database, use the
`remove()` operation, specifying which document to
remove. The following code removes "Gel Pen" from your
`example` collection.

```
db.example.remove( { "Item": "Gel Pen" } )
```

To remove all documents from your database, use the
`remove()` operation with an empty query.

```
db.example.remove( { } )
```
