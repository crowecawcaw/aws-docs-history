# Differences between a relational (SQL) database and

DynamoDB when managing indexes

Indexes give you access to alternate query patterns, and can speed up queries. This
section compares and contrasts index creation and usage in SQL and Amazon DynamoDB.

Whether you are using a relational database or DynamoDB, you should be judicious with
index creation. Whenever a write occurs on a table, all of the table's indexes must be
updated. In a write-heavy environment with large tables, this can consume large amounts
of system resources. In a read-only or read-mostly environment, this is not as much of a
concern. However, you should ensure that the indexes are actually being used by your
application, and not simply taking up space.

###### Topics

- [Differences between a relational (SQL)
  database and DynamoDB when creating an index](#SQLtoNoSQL.Indexes.Creating "#SQLtoNoSQL.Indexes.Creating")
- [Differences between a relational
  (SQL) database and DynamoDB when querying and scanning an index](#SQLtoNoSQL.Indexes.QueryAndScan "#SQLtoNoSQL.Indexes.QueryAndScan")

## Differences between a relational (SQL)

database and DynamoDB when creating an index

Compare the `CREATE INDEX` statement in SQL with the
`UpdateTable` operation in Amazon DynamoDB.

###### Topics

- [Creating an index with
  SQL](#SQLtoNoSQL.Indexes.Creating.SQL "#SQLtoNoSQL.Indexes.Creating.SQL")
- [Creating an index in
  DynamoDB](#SQLtoNoSQL.Indexes.Creating.DynamoDB "#SQLtoNoSQL.Indexes.Creating.DynamoDB")

### Creating an index with

SQL

In a relational database, an index is a data structure that lets you perform
fast queries on different columns in a table. You can use the `CREATE
 INDEX` SQL statement to add an index to an existing table, specifying
the columns to be indexed. After the index has been created, you can query the
data in the table as usual, but now the database can use the index to quickly
find the specified rows in the table instead of scanning the entire
table.

After you create an index, the database maintains it for you. Whenever you
modify data in the table, the index is automatically modified to reflect changes
in the table.

In MySQL, you would create an index like the following.

```
CREATE INDEX GenreAndPriceIndex
ON Music (genre, price);
```

### Creating an index in

DynamoDB

In DynamoDB, you can create and use a _secondary index_ for similar
purposes.

Indexes in DynamoDB are different from their relational counterparts. When you
create a secondary index, you must specify its key attributes—a partition key and a
sort key. After you create the secondary index, you can `Query` it or
`Scan` it just as you would with a table. DynamoDB does not have a
query optimizer, so a secondary index is only used when you `Query` it or
`Scan` it.

DynamoDB supports two different kinds of indexes:

- Global secondary indexes – The primary key of the index can be
  any two attributes from its table.
- Local secondary indexes – The partition key of the index must be
  the same as the partition key of its table. However, the sort key can be
  any other attribute.

DynamoDB ensures that the data in a secondary index is eventually consistent with its table.
You can request strongly consistent `Query` or `Scan`
operations on a table or a local secondary index. However, global secondary indexes support only
eventual consistency.

You can add a global secondary index to an existing table, using the `UpdateTable`
operation and specifying `GlobalSecondaryIndexUpdates`.

```
{
    TableName: "Music",
    AttributeDefinitions:[
        {AttributeName: "Genre", AttributeType: "S"},
        {AttributeName: "Price", AttributeType: "N"}
    ],
    GlobalSecondaryIndexUpdates: [
        {
            Create: {
                IndexName: "GenreAndPriceIndex",
                KeySchema: [
                    {AttributeName: "Genre", KeyType: "HASH"}, //Partition key
                    {AttributeName: "Price", KeyType: "RANGE"}, //Sort key
                ],
                Projection: {
                    "ProjectionType": "ALL"
                },
                ProvisionedThroughput: {                                // Only specified if using provisioned mode
                    "ReadCapacityUnits": 1,"WriteCapacityUnits": 1
                }
            }
        }
    ]
}
```

You must provide the following parameters to `UpdateTable`:

- `TableName` – The table that the index will be
  associated with.
- `AttributeDefinitions` – The data types for the key
  schema attributes of the index.
- `GlobalSecondaryIndexUpdates` – Details about the
  index you want to create:
  - `IndexName` – A name for the index.
  - `KeySchema` – The attributes that are used
    for the index's primary key.
  - `Projection` – Attributes from the table that
    are copied to the index. In this case, `ALL` means
    that all of the attributes are copied.
  - `ProvisionedThroughput (for provisioned tables)`
    – The number of reads and writes per second that you need
    for this index. (This is separate from the provisioned
    throughput settings of the table.)

Part of this operation involves backfilling data from the table into the new
index. During backfilling, the table remains available. However, the index is
not ready until its `Backfilling` attribute changes from true to
false. You can use the `DescribeTable` operation to view this
attribute.

## Differences between a relational

(SQL) database and DynamoDB when querying and scanning an index

Compare querying and scanning an index using the SELECT statement in SQL with the
`Query` and `Scan` operations in Amazon DynamoDB.

###### Topics

- [Querying and scanning an
  index with SQL](#SQLtoNoSQL.Indexes.QueryAndScan.SQL "#SQLtoNoSQL.Indexes.QueryAndScan.SQL")
- [Querying and scanning
  an index in DynamoDB](#SQLtoNoSQL.Indexes.QueryAndScan.DynamoDB "#SQLtoNoSQL.Indexes.QueryAndScan.DynamoDB")

### Querying and scanning an

index with SQL

In a relational database, you do not work directly with indexes. Instead, you
query tables by issuing `SELECT` statements, and the query optimizer
can make use of any indexes.

A _query optimizer_ is a relational database management
system (RDBMS) component that evaluates the available indexes and determines
whether they can be used to speed up a query. If the indexes can be used to
speed up a query, the RDBMS accesses the index first and then uses it to locate
the data in the table.

Here are some SQL statements that can use
_GenreAndPriceIndex_ to improve performance. We assume
that the _Music_ table has enough data in it that the query
optimizer decides to use this index, rather than simply scanning the entire
table.

```
/* All of the rock songs */

SELECT * FROM Music
WHERE Genre = 'Rock';
```

```
/* All of the cheap country songs */

SELECT Artist, SongTitle, Price FROM Music
WHERE Genre = 'Country' AND Price < 0.50;
```

### Querying and scanning

an index in DynamoDB

In DynamoDB, you perform `Query` and `Scan` operations
directly on the index, in the same way that you would on a table. You can use
either the DynamoDB API or [PartiQL](ql-reference.md "ql-reference.md") (a SQL-compatible query language) to query or scan the
index. You must specify both `TableName` and
`IndexName`.

The following are some queries on _GenreAndPriceIndex_ in
DynamoDB. (The key schema for this index consists of _Genre_ and
_Price_.)

DynamoDB API

```
// All of the rock songs

{
    TableName: "Music",
    IndexName: "GenreAndPriceIndex",
    KeyConditionExpression: "Genre = :genre",
    ExpressionAttributeValues: {
        ":genre": "Rock"
    },
};
```

This example uses a `ProjectionExpression` to indicate
that you only want some of the attributes, rather than all of them,
to appear in the results.

```
// All of the cheap country songs

{
    TableName: "Music",
    IndexName: "GenreAndPriceIndex",
    KeyConditionExpression: "Genre = :genre and Price < :price",
    ExpressionAttributeValues: {
        ":genre": "Country",
        ":price": 0.50
    },
    ProjectionExpression: "Artist, SongTitle, Price"
};
```

The following is a scan on
_GenreAndPriceIndex_.

```
// Return all of the data in the index

{
    TableName:  "Music",
    IndexName: "GenreAndPriceIndex"
}
```

PartiQL for DynamoDB
With PartiQL, you use the PartiQL `Select` statement to
perform queries and scans on the index.

```
// All of the rock songs

SELECT *
FROM Music.GenreAndPriceIndex
WHERE Genre = 'Rock'
```

```
// All of the cheap country songs

SELECT *
FROM Music.GenreAndPriceIndex
WHERE Genre = 'Rock' AND Price < 0.50
```

The following is a scan on
_GenreAndPriceIndex_.

```
// Return all of the data in the index

SELECT *
FROM Music.GenreAndPriceIndex
```

###### Note

For code examples using `Select`, see [PartiQL select statements for DynamoDB](ql-reference.md "ql-reference.md").
