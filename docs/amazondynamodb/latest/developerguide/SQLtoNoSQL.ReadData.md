# Differences in querying a table

Another common access pattern is reading multiple items from a table, based on
your query criteria.

###### Topics

- [Querying a table with
  SQL](#SQLtoNoSQL.ReadData.Query.SQL "#SQLtoNoSQL.ReadData.Query.SQL")
- [Querying a table in
  DynamoDB](#SQLtoNoSQL.ReadData.Query.DynamoDB "#SQLtoNoSQL.ReadData.Query.DynamoDB")

## Querying a table with

SQL

When using SQL the `SELECT` statement lets you query on key
columns, non-key columns, or any combination. The `WHERE` clause
determines which rows are returned, as shown in the following examples.

```
/* Return a single song, by primary key */

SELECT * FROM Music
WHERE Artist='No One You Know' AND SongTitle = 'Call Me Today';
```

```
/* Return all of the songs by an artist */

SELECT * FROM Music
WHERE Artist='No One You Know';
```

```
/* Return all of the songs by an artist, matching first part of title */

SELECT * FROM Music
WHERE Artist='No One You Know' AND SongTitle LIKE 'Call%';
```

```
/* Return all of the songs by an artist, with a particular word in the title...
...but only if the price is less than 1.00 */

SELECT * FROM Music
WHERE Artist='No One You Know' AND SongTitle LIKE '%Today%'
AND Price < 1.00;
```

Note that the primary key for this table consists of
_Artist_ and _SongTitle_.

## Querying a table in

DynamoDB

In Amazon DynamoDB, you can use either the DynamoDB API or [PartiQL](ql-reference.md "ql-reference.md") (a SQL-compatible query
language) to query an item from a table.

DynamoDB API
With Amazon DynamoDB, you can use the `Query` operation to
retrieve data in a similar fashion. The `Query` operation
provides quick, efficient access to the physical locations where the
data is stored. For more information, see [Partitions and data distribution in DynamoDB](HowItWorks.md "HowItWorks.md").

You can use `Query` with any table or secondary index.
You must specify an equality condition for the partition key's
value, and you can optionally provide another condition for the sort
key attribute if it is defined.

The `KeyConditionExpression` parameter specifies the
key values that you want to query. You can use an optional
`FilterExpression` to remove certain items from the
results before they are returned to you.

In DynamoDB, you must use `ExpressionAttributeValues` as
placeholders in expression parameters (such as
`KeyConditionExpression` and
`FilterExpression`). This is analogous to the use of
_bind variables_ in relational databases,
where you substitute the actual values into the `SELECT`
statement at runtime.

Note that the primary key for this table consists of
_Artist_ and
_SongTitle_.

The following are some DynamoDB `Query` examples.

```
// Return a single song, by primary key

{
    TableName: "Music",
    KeyConditionExpression: "Artist = :a and SongTitle = :t",
    ExpressionAttributeValues: {
        ":a": "No One You Know",
        ":t": "Call Me Today"
    }
}
```

```
// Return all of the songs by an artist

{
    TableName: "Music",
    KeyConditionExpression: "Artist = :a",
    ExpressionAttributeValues: {
        ":a": "No One You Know"
    }
}
```

```
// Return all of the songs by an artist, matching first part of title

{
    TableName: "Music",
    KeyConditionExpression: "Artist = :a and begins_with(SongTitle, :t)",
    ExpressionAttributeValues: {
        ":a": "No One You Know",
        ":t": "Call"
    }
}
```

PartiQL for DynamoDB
With PartiQL, you can perform a query by using the
`ExecuteStatement` operation and the
`Select` statement on the partition key.

```
SELECT AlbumTitle, Year, Price
FROM Music
WHERE Artist='No One You Know'
```

Using the `SELECT` statement in this way returns all
the songs associated with this particular
`Artist`.

For code examples using `Select` and
`ExecuteStatement`, see [PartiQL select statements for DynamoDB](ql-reference.md "ql-reference.md").
