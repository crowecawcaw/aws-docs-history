# Differences in reading an item

using its primary key

One common access pattern for databases is to read a single item from a table. You
have to specify the primary key of the item you want.

###### Topics

- [Reading an item using its
  primary key with SQL](#SQLtoNoSQL.ReadData.SingleItem.SQL "#SQLtoNoSQL.ReadData.SingleItem.SQL")
- [Reading an item using
  its primary key in DynamoDB](#SQLtoNoSQL.ReadData.SingleItem.DynamoDB "#SQLtoNoSQL.ReadData.SingleItem.DynamoDB")

## Reading an item using its

primary key with SQL

In SQL, you would use the `SELECT` statement to retrieve data from
a table. You can request one or more columns in the result (or all of them, if
you use the `*` operator). The `WHERE` clause determines
which rows to return.

The following is a `SELECT` statement to retrieve a single row from
the _Music_ table. The `WHERE` clause specifies
the primary key values.

```
SELECT *
FROM Music
WHERE Artist='No One You Know' AND SongTitle = 'Call Me Today'
```

You can modify this query to retrieve only a subset of the columns.

```
SELECT AlbumTitle, Year, Price
FROM Music
WHERE Artist='No One You Know' AND SongTitle = 'Call Me Today'
```

Note that the primary key for this table consists of
_Artist_ and _SongTitle_.

## Reading an item using

its primary key in DynamoDB

In Amazon DynamoDB, you can use either the DynamoDB API or [PartiQL](ql-reference.md "ql-reference.md") (a SQL-compatible query
language) to read an item from a table.

DynamoDB API
With the DynamoDB API, you use the `PutItem` operation to
add an item to a table.

DynamoDB provides the `GetItem` operation for retrieving
an item by its primary key. `GetItem` is highly efficient
because it provides direct access to the physical location of the
item. (For more information, see [Partitions and data distribution in DynamoDB](HowItWorks.md "HowItWorks.md").)

By default, `GetItem` returns the entire item with all
of its attributes.

```
{
    TableName: "Music",
    Key: {
        "Artist": "No One You Know",
        "SongTitle": "Call Me Today"
    }
}
```

You can add a `ProjectionExpression` parameter to
return only some of the attributes.

```
{
    TableName: "Music",
    Key: {
        "Artist": "No One You Know",
        "SongTitle": "Call Me Today"
    },
    "ProjectionExpression": "AlbumTitle, Year, Price"
}
```

Note that the primary key for this table consists of
_Artist_ and
_SongTitle_.

The DynamoDB `GetItem` operation is very efficient. It
uses the primary key values to determine the exact storage location
of the item in question, and retrieves it directly from there. The
SQL `SELECT` statement is similarly efficient, in the
case of retrieving items by primary key values.

The SQL `SELECT` statement supports many kinds of
queries and table scans. DynamoDB provides similar functionality with
its `Query` and `Scan` operations, which are
described in [Differences in querying a table](SQLtoNoSQL.ReadData.md "SQLtoNoSQL.ReadData.md") and [Differences in scanning a table](SQLtoNoSQL.ReadData.md "SQLtoNoSQL.ReadData.md").

The SQL `SELECT` statement can perform table joins,
allowing you to retrieve data from multiple tables at the same time.
Joins are most effective where the database tables are normalized
and the relationships among the tables are clear. However, if you
join too many tables in one `SELECT` statement
application performance can be affected. You can work around such
issues by using database replication, materialized views, or query
rewrites.

DynamoDB is a nonrelational database and doesn't support table joins.
If you are migrating an existing application from a relational
database to DynamoDB, you need to denormalize your data model to
eliminate the need for joins.

PartiQL for DynamoDB
With PartiQL, you use the `ExecuteStatement` operation
to read an item from a table, using the PartiQL `Select`
statement.

```
SELECT AlbumTitle, Year, Price
FROM Music
WHERE Artist='No One You Know' AND SongTitle = 'Call Me Today'
```

Note that the primary key for this table consists of Artist and
SongTitle.

###### Note

The select PartiQL statement can also be used to Query or
Scan a DynamoDB table

For code examples using `Select` and
`ExecuteStatement`, see [PartiQL select statements for DynamoDB](ql-reference.md "ql-reference.md").
