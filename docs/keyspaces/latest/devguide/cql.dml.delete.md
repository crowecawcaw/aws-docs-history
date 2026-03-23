# DELETE

Use the `DELETE` statement to remove a row from a table.

Syntax

```
**delete\_statement** ::=  DELETE [ simple_selection ( ',' simple_selection ) ]
                      FROM table_name
                      [ USING update_parameter ( AND update_parameter )* ]
                      WHERE where_clause
                      [ IF ( EXISTS | condition ( AND condition )*) ]

**simple\_selection** ::=  column_name
                     | column_name '[' term ']'
                     | column_name '.' `field_name

**condition**        ::=  simple_selection operator term

```

Where:

- `*table\_name*` is the table that contains
  the row you want to delete.
  Example

```
DELETE manager_id FROM "myGSGKeyspace".employees_tbl WHERE id='789-01-2345' AND division='Executive' ;
```

`DELETE` supports the following value as
`update_parameter`:

- `TIMESTAMP` – A `bigint` value representing the number of microseconds since the standard base time
  known as the epoch: January 1 1970 at 00:00:00 GMT.
