# Use client-side timestamps in queries in Amazon Keyspaces

After you have turned on client-side timestamps, you can pass the timestamp in your
`INSERT`, `UPDATE`, and `DELETE` statements with the
`USING TIMESTAMP` clause.

The timestamp value is a `bigint`
representing a number of microseconds since the standard base time known as the
epoch: January 1 1970 at 00:00:00 GMT. A timestamp that is supplied
by the client has to fall between the range of 2 days in the past and 5 minutes in the
future from the current wall clock time.

Amazon Keyspaces keeps timestamp metadata for the life of
the data. You can use the `WRITETIME` function to look up timestamps that
occurred years in the past. For more information about CQL syntax, see [DML statements (data manipulation language) in Amazon Keyspaces](cql.md "cql.md").

The following CQL statement is an example of how to use a timestamp as an
`update_parameter`.

```
INSERT INTO `catalog.book_awards` (year, award, rank, category, book_title, author, publisher)
   VALUES (2022, 'Wolf', 4, 'Non-Fiction', 'Science Update', 'Ana Carolina Silva', 'SomePublisher')
   USING TIMESTAMP 1669069624;
```

If you do not specify a timestamp in your CQL query, Amazon Keyspaces uses the timestamp passed by your
client driver. If no timestamp is supplied by the client driver, Amazon Keyspaces assigns a
server-side timestamp for your write operation.

To see the timestamp value that is
stored for a specific column, you can use the `WRITETIME` function in a
`SELECT` statement as shown in the following example.

```
SELECT year, award, rank, category, book_title, author, publisher, WRITETIME(year), WRITETIME(award), WRITETIME(rank),
  WRITETIME(category), WRITETIME(book_title), WRITETIME(author), WRITETIME(publisher) from catalog.book_awards;
```
