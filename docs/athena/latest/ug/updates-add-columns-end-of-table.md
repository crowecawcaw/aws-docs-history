# Add columns at the end of the

table

If you create tables in any of the formats that Athena supports, such as Parquet, ORC,
Avro, JSON, CSV, and TSV, you can use the `ALTER TABLE ADD COLUMNS` statement
to add columns after existing columns but before partition columns.

The following example adds a `comment` column at the end of the
`orders_parquet` table before any partition columns:

```
ALTER TABLE orders_parquet ADD COLUMNS (comment string)
```

###### Note

To see a new table column in the Athena Query Editor after you run `ALTER
 TABLE ADD COLUMNS`, manually refresh the table list in the editor, and
then expand the table again.
