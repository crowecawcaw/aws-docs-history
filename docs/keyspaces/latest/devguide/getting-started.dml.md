# Delete data from a table using the CQL `DELETE` statement

To delete data in your `book_awards` table, use the `DELETE`
statement.

You can delete data from a row or from a partition. Be careful when deleting data, because
deletions are irreversible.

Deleting one or all rows from a table doesn't delete the table. Thus you can
repopulate it with data. Deleting a table deletes the table and all data in it. To use
the table again, you must re-create it and add data to it. Deleting a keyspace deletes
the keyspace and all tables within it. To use the keyspace and tables, you must
re-create them, and then populate them with data. You can use Amazon Keyspaces Point-in-time (PITR) recovery to
help restore deleted tables, to learn more see [Backup and restore data with point-in-time recovery for Amazon Keyspaces](PointInTimeRecovery.md "PointInTimeRecovery.md") .
To learn how to restore a deleted table with PITR enabled, see [Restore a deleted table using Amazon Keyspaces PITR](restoredeleted.md "restoredeleted.md").

## Delete cells

Deleting a column from a row removes the data from the specified cell. When you
display that column using a `SELECT` statement, the data is displayed as
`null`, though a null value is not stored in that
location.

The general syntax to delete one or more specific columns is as follows.

```
DELETE column_name1[, column_name2...] FROM table_name WHERE condition ;
```

In your `book_awards` table, you can see that the title of the
book that won the first price of the 2020 "Richard Roe" price is "Long Summer".
Imagine that this title has been recalled, and you need to delete the data from this cell.

###### To delete a specific cell

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. Run the following `DELETE` query.

```
DELETE book_title FROM catalog.book_awards WHERE year=2020 AND award='Richard Roe' AND category='Fiction' AND rank=1;
```

3. Verify that the delete request was made as expected.

```
SELECT * FROM catalog.book_awards WHERE year=2020 AND award='Richard Roe' AND category='Fiction' AND rank=1;
```

The output of this statement looks like this.

```
 `year | award | category | rank | author | book_title | publisher
------+-------------+----------+------+-------------------+------------+---------------
 2020 | Richard Roe | Fiction | 1 | Alejandro Rosalez | null | SomePublisher`
```

## Delete rows

There might be a time when you need to delete an entire row, for example to meet
a data deletion request. The general syntax for deleting a row is as
follows.

```
DELETE FROM table_name WHERE condition ;
```

###### To delete a row

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. Run the following `DELETE` query.

```
DELETE FROM catalog.book_awards WHERE year=2020 AND award='Richard Roe' AND category='Fiction' AND rank=1;
```

3. Verify that the delete was made as expected.

```
SELECT * FROM catalog.book_awards WHERE year=2020 AND award='Richard Roe' AND category='Fiction' AND rank=1;
```

The output of this statement looks like this after the row has been deleted.

```
 `year | award | category | rank | author | book_title | publisher
------+-------+----------+------+--------+------------+-----------

(0 rows)`
```

You can delete expired data automatically from your table using Amazon Keyspaces Time to Live, for more information, see [Expire data with Time to Live (TTL) for Amazon Keyspaces (for Apache Cassandra)](TTL.md "TTL.md").
