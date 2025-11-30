# Core components of Amazon DynamoDB

In DynamoDB, tables, items, and attributes are the core components that you work with. A
_table_ is a collection of _items_, and each item is a collection of _attributes_. DynamoDB uses primary keys to uniquely identify each item in a
table. You can use DynamoDB Streams to
capture data modification events in DynamoDB tables.

There are limits in DynamoDB. For more information, see [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").

The following video will give you an introductory look at tables, items, and
attributes.

[Tables, items, and
attributes](https://www.youtube.com/embed/Mw8wCj0gkRc "https://www.youtube.com/embed/Mw8wCj0gkRc")

## Tables, items, and

attributes

![Each DynamoDB table contains zero or more items that are made of one or more attributes.](images/HowItWorksTables-2024.png)

The following are the basic DynamoDB components:

- **Tables** – Similar to other database
  systems, DynamoDB stores data in tables. A _table_ is a
  collection of data. For example, see the example table called
  _People_ that you could use to store personal contact
  information about friends, family, or anyone else of interest. You could
  also have a _Cars_ table to store information about
  vehicles that people drive.
- **Items** – Each table contains zero or
  more items. An _item_ is a group of attributes that is
  uniquely identifiable among all of the other items. In a
  _People_ table, each item represents a person. For a
  _Cars_ table, each item represents one vehicle. Items
  in DynamoDB are similar in many ways to rows, records, or tuples in other
  database systems. In DynamoDB, there is no limit to the number of items you can
  store in a table.
- **Attributes** – Each item is composed
  of one or more attributes. An _attribute_ is a
  fundamental data element, something that does not need to be broken down any
  further. For example, an item in a _People_ table
  contains attributes called _PersonID_,
  _LastName_, _FirstName_, and so
  on. For a _Department_ table, an item might have
  attributes such as _DepartmentID_,
  _Name_, _Manager_, and so on.
  Attributes in DynamoDB are similar in many ways to fields or columns in other
  database systems.

The following diagram shows a table named _People_ with some
example items and attributes.

```

People

{
    "PersonID": 101,
    "LastName": "Smith",
    "FirstName": "Fred",
    "Phone": "555-4321"
}

{
    "PersonID": 102,
    "LastName": "Jones",
    "FirstName": "Mary",
    "Address": {
                "Street": "123 Main",
                "City": "Anytown",
                "State": "OH",
                "ZIPCode": 12345
    }
}

{
    "PersonID": 103,
    "LastName": "Stephens",
    "FirstName": "Howard",
    "Address": {
                "Street": "123 Main",
                "City": "London",
                "PostalCode": "ER3 5K8"
    },
    "FavoriteColor": "Blue"
}
```

Note the following about the _People_ table:

- Each item in the table has a unique identifier, or primary key, that
  distinguishes the item from all of the others in the table. In the
  _People_ table, the primary key consists of one
  attribute (_PersonID_).
- Other than the primary key, the _People_ table is
  schemaless, which means that neither the attributes nor their data types
  need to be defined beforehand. Each item can have its own distinct
  attributes.
- Most of the attributes are _scalar_, which means that
  they can have only one value. Strings and numbers are common examples of
  scalars.
- Some of the items have a nested attribute (_Address_).
  DynamoDB supports nested attributes up to 32 levels
  deep.

The following is another example table named _Music_ that you
could use to keep track of your music collection.

```

Music

{
    "Artist": "No One You Know",
    "SongTitle": "My Dog Spot",
    "AlbumTitle": "Hey Now",
    "Price": 1.98,
    "Genre": "Country",
    "CriticRating": 8.4
}

{
    "Artist": "No One You Know",
    "SongTitle": "Somewhere Down The Road",
    "AlbumTitle": "Somewhat Famous",
    "Genre": "Country",
    "CriticRating": 8.4,
    "Year": 1984
}

{
    "Artist": "The Acme Band",
    "SongTitle": "Still in Love",
    "AlbumTitle": "The Buck Starts Here",
    "Price": 2.47,
    "Genre": "Rock",
    "PromotionInfo": {
        "RadioStationsPlaying": [
            "KHCR",
            "KQBX",
            "WTNR",
            "WJJH"
        ],
        "TourDates": {
            "Seattle": "20150622",
            "Cleveland": "20150630"
        },
        "Rotation": "Heavy"
    }
}

{
    "Artist": "The Acme Band",
    "SongTitle": "Look Out, World",
    "AlbumTitle": "The Buck Starts Here",
    "Price": 0.99,
    "Genre": "Rock"
}
```

Note the following about the _Music_ table:

- The primary key for _Music_ consists of two attributes
  (_Artist_ and _SongTitle_). Each
  item in the table must have these two attributes. The combination of
  _Artist_ and _SongTitle_
  distinguishes each item in the table from all of the others.
- Other than the primary key, the _Music_ table is
  schemaless, which means that neither the attributes nor their data types
  need to be defined beforehand. Each item can have its own distinct
  attributes.
- One of the items has a nested attribute
  (_PromotionInfo_), which contains other nested
  attributes. DynamoDB supports nested attributes up to 32
  levels deep.

For more information, see [Working with tables and data in DynamoDB](WorkingWithTables.md "WorkingWithTables.md").

## Primary key

When you create a table, in addition to the table name, you must specify the
primary key of the table. The primary key uniquely identifies each item in the
table, so that no two items can have the same key.

DynamoDB supports two different kinds of primary keys:

- **Partition key** – A simple primary
  key, composed of one attribute known as the _partition
  key_.

DynamoDB uses the partition key's value as input to an internal hash
function. The output from the hash function determines the partition
(physical storage internal to DynamoDB) in which the item will be stored.

In a table that has only a partition key, no two items can have the same
partition key value.

The _People_ table described in [Tables, items, and
attributes](#HowItWorks.CoreComponents.TablesItemsAttributes "#HowItWorks.CoreComponents.TablesItemsAttributes") is an
example of a table with a simple primary key
(_PersonID_). You can access any item in the
_People_ table directly by providing the
_PersonId_ value for that item.

- **Partition key and sort key** –
  Referred to as a _composite primary key_, this type of
  key is composed of two attributes. The first attribute is the
  _partition key_, and the second attribute is the
  _sort key_.

DynamoDB uses the partition key value as input to an internal hash function.
The output from the hash function determines the partition (physical storage
internal to DynamoDB) in which the item will be stored. All items with the same
partition key value are stored together, in sorted order by sort key
value.

In a table that has a partition key and a sort key, it's possible for
multiple items to have the same partition key value. However, those items
must have different sort key values.

The _Music_ table described in [Tables, items, and
attributes](#HowItWorks.CoreComponents.TablesItemsAttributes "#HowItWorks.CoreComponents.TablesItemsAttributes") is an
example of a table with a composite primary key (_Artist_
and _SongTitle_). You can access any item in the
_Music_ table directly, if you provide the
_Artist_ and _SongTitle_ values
for that item.

A composite primary key gives you additional flexibility when querying
data. For example, if you provide only the value for
_Artist_, DynamoDB retrieves all of the songs by that
artist. To retrieve only a subset of songs by a particular artist, you can
provide a value for _Artist_ along with a range of values
for _SongTitle_.

###### Note

The partition key of an item is also known as its _hash
attribute_. The term _hash attribute_ derives
from the use of an internal hash function in DynamoDB that evenly distributes data
items across partitions, based on their partition key values.

The sort key of an item is also known as its _range
attribute_. The term _range attribute_ derives
from the way DynamoDB stores items with the same partition key physically close
together, in sorted order by the sort key value.

Each primary key attribute must be a scalar (meaning that it can hold only a
single value). The only data types allowed for primary key attributes are string,
number, or binary. There are no such restrictions for other, non-key
attributes.

## Secondary

indexes

You can create one or more secondary indexes on a table. A
_secondary index_ lets you query the data in the table using an
alternate key, in addition to queries against the primary key. DynamoDB doesn't require
that you use indexes, but they give your applications more flexibility when querying
your data. After you create a secondary index on a table, you can read data from the
index in much the same way as you do from the table.

DynamoDB supports two kinds of indexes:

- Global secondary index – An index with a partition key and sort key that can be
  different from those on the table. The primary key values in global secondary indexes don't need to be unique.
- Local secondary index – An index that has the same partition key as the table, but a
  different sort key.

In DynamoDB, global secondary indexes (GSIs) are indexes that span the entire
table, allowing you to query across all partition keys. Local secondary indexes (LSIs)
are indexes that have the same partition key as the base table but a different sort key.

Each table in DynamoDB has a quota of 20 global secondary indexes
(default quota) and 5 local secondary indexes.

In the example _Music_ table shown previously, you can query
data items by _Artist_ (partition key) or by
_Artist_ and _SongTitle_ (partition key
and sort key). What if you also wanted to query the data by
_Genre_ and _AlbumTitle_? To do this, you
could create an index on _Genre_ and
_AlbumTitle_, and then query the index in much the same way
as you'd query the _Music_ table.

The following diagram shows the example _Music_ table, with a
new index called _GenreAlbumTitle_. In the index,
_Genre_ is the partition key and
_AlbumTitle_ is the sort key.

| Music Table                                                                                                                                                                                                                                                                                                                                                                 | _GenreAlbumTitle_                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<br>{<br>"Artist": "No One You Know",<br>"SongTitle": "My Dog Spot",<br>"AlbumTitle": "Hey Now",<br>"Price": 1.98,<br>"Genre": "Country",<br>"CriticRating": 8.4<br>}<br>`                                                                                                                                                                                                 | `<br>{<br>"Genre": "Country",<br>"AlbumTitle": "Hey Now",<br>"Artist": "No One You Know",<br>"SongTitle": "My Dog Spot"<br>}<br>`                     |
| `<br>{<br>"Artist": "No One You Know",<br>"SongTitle": "Somewhere Down The Road",<br>"AlbumTitle": "Somewhat Famous",<br>"Genre": "Country",<br>"CriticRating": 8.4,<br>"Year": 1984<br>}<br>`                                                                                                                                                                              | `<br>{<br>"Genre": "Country",<br>"AlbumTitle": "Somewhat Famous",<br>"Artist": "No One You Know",<br>"SongTitle": "Somewhere Down The Road"<br>}<br>` |
| `<br>{<br>"Artist": "The Acme Band",<br>"SongTitle": "Still in Love",<br>"AlbumTitle": "The Buck Starts Here",<br>"Price": 2.47,<br>"Genre": "Rock",<br>"PromotionInfo": {<br>"RadioStationsPlaying": {<br>"KHCR",<br>"KQBX",<br>"WTNR",<br>"WJJH"<br>},<br>"TourDates": {<br>"Seattle": "20150622",<br>"Cleveland": "20150630"<br>},<br>"Rotation": "Heavy"<br>}<br>}<br>` | `<br>{<br>"Genre": "Rock",<br>"AlbumTitle": "The Buck Starts Here",<br>"Artist": "The Acme Band",<br>"SongTitle": "Still In Love"<br>}<br>`           |
| `<br>{<br>"Artist": "The Acme Band",<br>"SongTitle": "Look Out, World",<br>"AlbumTitle": "The Buck Starts Here",<br>"Price": 0.99,<br>"Genre": "Rock"<br>}<br>`                                                                                                                                                                                                             | `<br>{<br>"Genre": "Rock",<br>"AlbumTitle": "The Buck Starts Here",<br>"Artist": "The Acme Band",<br>"SongTitle": "Look Out, World"<br>}<br>`         |

Note the following about the _GenreAlbumTitle_ index:

- Every index belongs to a table, which is called the _base
  table_ for the index. In the preceding example,
  _Music_ is the base table for the
  _GenreAlbumTitle_ index.
- DynamoDB maintains indexes automatically. When you add, update, or delete an
  item in the base table, DynamoDB adds, updates, or deletes the corresponding
  item in any indexes that belong to that table.
- When you create an index, you specify which attributes will be copied, or
  _projected_, from the base table to the index. At a
  minimum, DynamoDB projects the key attributes from the base table into the
  index. This is the case with `GenreAlbumTitle`, where only the
  key attributes from the `Music` table are projected into the
  index.

You can query the _GenreAlbumTitle_ index to find all albums of
a particular genre (for example, all _Rock_ albums). You can also
query the index to find all albums within a particular genre that have certain album
titles (for example, all _Country_ albums with titles that start
with the letter H).

For more information, see [Improving data access with secondary indexes in
DynamoDB](SecondaryIndexes.md "SecondaryIndexes.md").

## DynamoDB Streams

DynamoDB Streams is an optional feature that captures data modification events in DynamoDB
tables. The data about these events appear in the stream in near-real time, and in
the order that the events occurred.

Each event is represented by a _stream record_. If you enable a
stream on a table, DynamoDB Streams writes a stream record whenever one of the following events
occurs:

- A new item is added to the table: The stream captures an image of the
  entire item, including all of its attributes.
- An item is updated: The stream captures the "before" and "after" image of
  any attributes that were modified in the item.
- An item is deleted from the table: The stream captures an image of the
  entire item before it was deleted.

Each stream record also contains the name of the table, the event timestamp, and
other metadata. Stream records have a lifetime of 24 hours; after that, they are
automatically removed from the stream.

You can use DynamoDB Streams together with AWS Lambda to create a
_trigger_—code that runs automatically whenever an event of
interest appears in a stream. For example, consider a _Customers_
table that contains customer information for a company. Suppose that you want to
send a "welcome" email to each new customer. You could enable a stream on that
table, and then associate the stream with a Lambda function. The Lambda function would
run whenever a new stream record appears, but only process new items added to the
_Customers_ table. For any item that has an
`EmailAddress` attribute, the Lambda function would invoke Amazon Simple Email Service
(Amazon SES) to send an email to that address.

![Integration of DynamoDB Streams and Lambda to automatically send a welcome email to new customers.](images/HowItWorksStreams.png)

###### Note

In this example, the last customer, Craig Roe, will not receive an email
because he doesn't have an `EmailAddress`.

In addition to triggers, DynamoDB Streams enables powerful solutions such as data replication
within and across AWS Regions, materialized views of data in DynamoDB tables, data
analysis using Kinesis materialized views, and much more.

For more information, see [Change data capture for DynamoDB Streams](Streams.md "Streams.md").
