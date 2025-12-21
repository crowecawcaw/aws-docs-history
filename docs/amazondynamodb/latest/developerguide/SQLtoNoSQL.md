# Differences between a relational (SQL) database

and DynamoDB when writing data to a table

Relational database tables contain _rows_ of data. Rows are
composed of _columns_. Amazon DynamoDB tables contain
_items_. Items are composed of
_attributes_.

This section describes how to write one row (or item) to a table.

###### Topics

- [Writing data to a table with SQL](#SQLtoNoSQL.WriteData.SQL "#SQLtoNoSQL.WriteData.SQL")
- [Writing data to a table in
  DynamoDB](#SQLtoNoSQL.WriteData.DynamoDB "#SQLtoNoSQL.WriteData.DynamoDB")

## Writing data to a table with SQL

A table in a relational database is a two-dimensional data structure composed of
rows and columns. Some database management systems also provide support for
semistructured data, usually with native JSON or XML data types. However, the
implementation details vary among vendors.

In SQL, you would use the `INSERT` statement to add a row to a
table.

```
INSERT INTO Music
    (Artist, SongTitle, AlbumTitle,
    Year, Price, Genre,
    Tags)
VALUES(
    'No One You Know', 'Call Me Today', 'Somewhat Famous',
    2015, 2.14, 'Country',
    '{"Composers": ["Smith", "Jones", "Davis"],"LengthInSeconds": 214}'
);
```

The primary key for this table consists of _Artist_ and
_SongTitle_. You must specify values for these
columns.

###### Note

This example uses the _Tags_ column to store semistructured
data about the songs in the _Music_ table. The
_Tags_ column is defined as type TEXT, which can store up
to 65,535 characters in MySQL.

## Writing data to a table in

DynamoDB

In Amazon DynamoDB, you can use either the DynamoDB API or [PartiQL](ql-reference.md "ql-reference.md") (a SQL-compatible query
language) to add an item to a table.

DynamoDB API
With the DynamoDB API, you use the `PutItem` operation to add
an item to a table.

```
{
    TableName: "Music",
    Item: {
        "Artist":"No One You Know",
        "SongTitle":"Call Me Today",
        "AlbumTitle":"Somewhat Famous",
        "Year": 2015,
        "Price": 2.14,
        "Genre": "Country",
        "Tags": {
            "Composers": [
                  "Smith",
                  "Jones",
                  "Davis"
            ],
            "LengthInSeconds": 214
        }
    }
}
```

The primary key for this table consists of _Artist_
and _SongTitle_. You must specify values for these
attributes.

Here are some key things to know about this `PutItem`
example:

- DynamoDB provides native support for documents, using JSON. This
  makes DynamoDB ideal for storing semistructured data, such as
  _Tags_. You can also retrieve and
  manipulate data from within JSON documents.
- The _Music_ table does not have any
  predefined attributes, other than the primary key
  (_Artist_ and
  _SongTitle_).
- Most SQL databases are transaction oriented. When you issue an
  `INSERT` statement, the data modifications are
  not permanent until you issue a `COMMIT` statement.
  With Amazon DynamoDB, the effects of a `PutItem` operation
  are permanent when DynamoDB replies with an HTTP 200 status code
  (`OK`).

The following are some other `PutItem` examples.

```
{
    TableName: "Music",
    Item: {
        "Artist": "No One You Know",
        "SongTitle": "My Dog Spot",
        "AlbumTitle":"Hey Now",
        "Price": 1.98,
        "Genre": "Country",
        "CriticRating": 8.4
    }
}
```

```
{
    TableName: "Music",
    Item: {
        "Artist": "No One You Know",
        "SongTitle": "Somewhere Down The Road",
        "AlbumTitle":"Somewhat Famous",
        "Genre": "Country",
        "CriticRating": 8.4,
        "Year": 1984
    }
}
```

```
{
    TableName: "Music",
    Item: {
        "Artist": "The Acme Band",
        "SongTitle": "Still In Love",
        "AlbumTitle":"The Buck Starts Here",
        "Price": 2.47,
        "Genre": "Rock",
        "PromotionInfo": {
            "RadioStationsPlaying":[
                 "KHCR", "KBQX", "WTNR", "WJJH"
            ],
            "TourDates": {
                "Seattle": "20150625",
                "Cleveland": "20150630"
            },
            "Rotation": "Heavy"
        }
    }
}
```

```
{
    TableName: "Music",
    Item: {
        "Artist": "The Acme Band",
        "SongTitle": "Look Out, World",
        "AlbumTitle":"The Buck Starts Here",
        "Price": 0.99,
        "Genre": "Rock"
    }
}
```

###### Note

In addition to `PutItem`, DynamoDB supports a
`BatchWriteItem` operation for writing multiple items
at the same time.

PartiQL for DynamoDB
With PartiQL, you use the `ExecuteStatement` operation to
add an item to a table, using the PartiQL `Insert`
statement.

```
INSERT into Music value {
    'Artist': 'No One You Know',
    'SongTitle': 'Call Me Today',
    'AlbumTitle': 'Somewhat Famous',
    'Year' : '2015',
    'Genre' : 'Acme'
}
```

The primary key for this table consists of _Artist_
and _SongTitle_. You must specify values for these
attributes.

###### Note

For code examples using `Insert` and
`ExecuteStatement`, see [PartiQL insert statements for DynamoDB](ql-reference.md "ql-reference.md").
