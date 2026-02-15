# Differences between a relational (SQL) database

and DynamoDB when deleting data from a table

In SQL, the `DELETE` statement removes one or more rows from a table.
Amazon DynamoDB uses the `DeleteItem` operation to delete one item at a
time.

###### Topics

- [Deleting data from a table with
  SQL](#SQLtoNoSQL.DeleteData.SQL "#SQLtoNoSQL.DeleteData.SQL")
- [Deleting data from a table in
  DynamoDB](#SQLtoNoSQL.DeleteData.DynamoDB "#SQLtoNoSQL.DeleteData.DynamoDB")

## Deleting data from a table with

SQL

In SQL, you use the `DELETE` statement to delete one or more rows. The
`WHERE` clause determines the rows that you want to modify. The
following is an example.

```
DELETE FROM Music
WHERE Artist = 'The Acme Band' AND SongTitle = 'Look Out, World';
```

You can modify the `WHERE` clause to delete multiple rows. For example,
you could delete all of the songs by a particular artist, as shown in the following
example.

```
DELETE FROM Music WHERE Artist = 'The Acme Band'
```

## Deleting data from a table in

DynamoDB

In DynamoDB, you can use either the DynamoDB API or [PartiQL](ql-reference.md "ql-reference.md") (a SQL-compatible query
language) to delete a single item. If you want to modify multiple items, you must
use multiple operations.

DynamoDB API
With the DynamoDB API, you use the `DeleteItem` operation to
delete data from a table, one item at a time. You must specify the
item's primary key values.

```
{
    TableName: "Music",
    Key: {
        Artist: "The Acme Band",
        SongTitle: "Look Out, World"
    }
}
```

###### Note

In addition to `DeleteItem`, Amazon DynamoDB supports a
`BatchWriteItem` operation for deleting multiple
items at the same time.

`DeleteItem` supports _conditional
writes_, where the operation succeeds only if a specific
`ConditionExpression` evaluates to true. For example, the
following `DeleteItem` operation deletes the item only if it
has a _RecordLabel_ attribute.

```
{
    TableName: "Music",
    Key: {
        Artist: "The Acme Band",
        SongTitle: "Look Out, World"
    },
   ConditionExpression: "attribute_exists(RecordLabel)"
}
```

PartiQL for DynamoDB
With PartiQL, you use the `Delete` statement through the
`ExecuteStatement` operation to delete data from a table,
one item at a time. You must specify the item's primary key
values.

The primary key for this table consists of _Artist_
and _SongTitle_. You must specify values for these
attributes.

```
DELETE FROM Music
WHERE Artist = 'Acme Band' AND SongTitle = 'PartiQL Rocks'
```

You can also specify additional conditions for the operation. The
following `DELETE` operation only deletes the item if it has
more than 11 _Awards_.

```
DELETE FROM Music
WHERE Artist = 'Acme Band' AND SongTitle = 'PartiQL Rocks' AND Awards > 11
```

###### Note

For code examples using `DELETE` and
`ExecuteStatement`, see [PartiQL delete statements for DynamoDB](ql-reference.md "ql-reference.md").
