# Understanding documents

Document databases are used for storing semistructured data as a document—rather than normalizing data across multiple tables, each with a
unique and fixed structure, as in a relational database. Documents stored in a document database use nested key-value pairs to provide the document's
structure or schema. However, different types of documents can be stored in the same document database, thus meeting the requirement for processing
similar data that is in different formats. For example, because each document is self-describing, the JSON-encoded documents for an online store that
are described in the topic [Example documents in a document database](#document-database-documents "#document-database-documents") can be stored in the same document
database.

###### Topics

- [SQL vs. non-relational terminology](#document-database-sql-vs-nosql-terms "#document-database-sql-vs-nosql-terms")
- [Simple documents](#document-database-documents-simple "#document-database-documents-simple")
- [Embedded documents](#document-database-documents-embeded "#document-database-documents-embeded")
- [Example documents in a document database](#document-database-documents "#document-database-documents")
- [Understanding normalization in a document database](#document-database-normalization "#document-database-normalization")

## SQL vs. non-relational terminology

The following table compares terminology used by document databases (MongoDB) with terminology used by SQL databases.

| SQL                    | MongoDB           |
| ---------------------- | ----------------- |
| Table                  | Collection        |
| Row                    | Document          |
| Column                 | Field             |
| Primary key            | ObjectId          |
| Index                  | Index             |
| View                   | View              |
| Nested table or object | Embedded document |
| Array                  | Array             |

## Simple documents

All documents in a document database are self-describing. This documentation uses JSON-like formatted documents, although you can use other means
of encoding.

A simple document has one or more fields that are all at the same level within the document. In the following example, the fields
`SSN`, `LName`, `FName`, `DOB`, `Street`, `City`, `State-Province`,
`PostalCode`, and `Country` are all siblings within the document.

```
{
   "SSN": "123-45-6789",
   "LName": "Rivera",
   "FName": "Martha",
   "DOB": "1992-11-16",
   "Street": "125 Main St.",
   "City": "Anytown",
   "State-Province": "WA",
   "PostalCode": "98117",
   "Country": "USA"
}
```

When information is organized in a simple document, each field is managed individually. To retrieve a person's address, you must retrieve
`Street`, `City`, `State-Province`, `PostalCode`, and `Country` as individual data
items.

## Embedded documents

A complex document organizes its data by creating embedded documents within the document. Embedded documents help manage data in groupings and as
individual data items, whichever is more efficient in a given case. Using the preceding example, you could embed an `Address` document in
the main document. Doing this results in the following document structure:

```
{
   "SSN": "123-45-6789",
   "LName": "Rivera",
   "FName": "Martha",
   "DOB": "1992-11-16",
   "Address":
   {
       "Street": "125 Main St.",
       "City": "Anytown",
       "State-Province": "WA",
       "PostalCode": "98117",
       "Country": "USA"
   }
}
```

You can now access the data in the document as individual fields ( `"SSN":` ), as an embedded document
( `"Address":` ), or as a member of an embedded document ( `"Address":{"Street":}` ).

## Example documents in a document database

As stated earlier, because each document in a document database is self-describing, the structure of documents within a document database can be
different from one another. The following two documents, one for a book and another for a periodical, are different structurally. Yet both of them
can be in the same document database.

The following is a sample book document:

```
{
    "_id" : "9876543210123",
    "Type": "book",
    "ISBN": "987-6-543-21012-3",
    "Author":
    {
        "LName":"Roe",
        "MI": "T",
        "FName": "Richard"
    },
    "Title": "Understanding Document Databases"
}
```

The following is a sample periodical document with two articles:

```
{
    "_id" : "0123456789012",
    "Publication": "Programming Today",
    "Issue":
    {
        "Volume": "14",
        "Number": "09"
    },
    "Articles" : [
        {
            "Title": "Is a Document Database Your Best Solution?",
            "Author":
            {
                "LName": "Major",
                "FName": "Mary"
            }
        },
        {
            "Title": "Databases for Online Solutions",
            "Author":
            {
                "LName": "Stiles",
                "FName": "John"
            }
        }
    ],
    "Type": "periodical"
}
```

Compare the structure of these two documents. With a relational database, you need either separate "periodical" and "books" tables, or a single
table with unused fields, such as "Publication," "Issue," "Articles," and "MI," as `null` values. Because document databases are
semistructured, with each document defining its own structure, these two documents can coexist in the same document database with no
`null` fields. Document databases are good at dealing with sparse data.

Developing against a document database enables quick, iterative development. This is because you can change the data structure of a document
dynamically, without having to change the schema for the entire collection. Document databases are well suited for agile development and dynamically
changing environments.

## Understanding normalization in a document database

Document databases are not normalized; data found in one document can be repeated in another document. Further, some data discrepancies can exist
between documents. For example, consider the scenario in which you make a purchase at an online store and all the details of your purchases are
stored in a single document. The document might look something like the following JSON document:

```
{
    "DateTime": "2018-08-15T12:13:10Z",
    "LName" : "Santos",
    "FName" : "Paul",
    "Cart" : [
        {
            "ItemId" : "9876543210123",
            "Description" : "Understanding Document Databases",
            "Price" : "29.95"
        },
        {
            "ItemId" : "0123456789012",
            "Description" : "Programming Today",
            "Issue": {
                "Volume": "14",
                "Number": "09"
            },
            "Price" : "8.95"
        },
        {
            "ItemId": "234567890-K",
            "Description": "Gel Pen (black)",
            "Price": "2.49"
        }
    ],
    "PaymentMethod" :
    {
        "Issuer" : "MasterCard",
        "Number" : "1234-5678-9012-3456"
    },
    "ShopperId" : "1234567890"
}
```

All this information is stored as a document in a transaction collection. Later, you realize that you forgot to purchase one item. So you again
log on to the same store and make another purchase, which is also stored as another document in the transaction collection.

```
{
    "DateTime": "2018-08-15T14:49:00Z",
    "LName" : "Santos",
    "FName" : "Paul",
    "Cart" : [
        {
            "ItemId" : "2109876543210",
            "Description" : "Document Databases for Fun and Profit",
            "Price" : "45.95"
        }
    ],
    "PaymentMethod" :
    {
        "Issuer" : "Visa",
        "Number" : "0987-6543-2109-8765"
    },
    "ShopperId" : "1234567890"
}
```

Notice the redundancy between these two documents—your name and shopper ID (and, if you used the same credit card, your credit card
information). But that's okay because storage is inexpensive, and each document completely records a single transaction that can be retrieved
quickly with a simple key-value query that requires no joins.

There is also an apparent discrepancy between the two documents—your credit card information. This is only an apparent discrepancy because
it is likely that you used a different credit card for each purchase. Each document is accurate for the transaction that it documents.
