# UPDATE

Athena Iceberg `UPDATE` writes Iceberg position delete files and newly
updated rows as data files in the same transaction. `UPDATE` can be
imagined as a combination of `INSERT INTO` and `DELETE`.
`UPDATE` operations are charged by the amount of data scanned. For
syntax, see [UPDATE](update-statement.md "update-statement.md").

The following example updates the specified values in the table
`iceberg_table`.

```
UPDATE iceberg_table SET category='c2' WHERE category='c1'
```
