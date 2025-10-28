# INSERT INTO

Inserts data into an Iceberg table. Athena Iceberg `INSERT INTO` is
charged the same as current `INSERT INTO` queries for external Hive
tables by the amount of data scanned. To insert data into an Iceberg table, use the
following syntax, where `query` can be either `VALUES
 (val1, val2, ...)` or `SELECT (col1, col2, …) FROM
 [`db_name`.]`table_name` WHERE`predicate``. For SQL syntax and semantic
details, see [INSERT INTO](insert-into.md "insert-into.md").

```
INSERT INTO [`db_name`.]`table_name` [(col1, col2, …)] `query`
```

The following examples insert values into the table
`iceberg_table`.

```
INSERT INTO iceberg_table VALUES (1,'a','c1')
```

```
INSERT INTO iceberg_table (col1, col2, ...) VALUES (val1, val2, ...)
```

```
INSERT INTO iceberg_table SELECT * FROM another_table
```
