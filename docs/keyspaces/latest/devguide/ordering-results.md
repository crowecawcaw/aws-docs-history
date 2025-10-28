# Order results with `ORDER BY` in Amazon Keyspaces

The `ORDER BY` clause specifies the sort order of the results returned
in a `SELECT` statement. The statement takes a list of column names as arguments and for each column you can
specify the sort order for the data. You can only specify clustering columns in ordering clauses, non-clustering columns are not allowed.

The two available sort order options for the returned results are `ASC` for ascending and `DESC`
for descending sort order.

```
`SELECT * FROM my_keyspace.my_table ORDER BY (col1 ASC, col2 DESC, col3 ASC);

 col1 | col2 | col3
 ------+------+------
 0 | 6 | a
 1 | 5 | b
 2 | 4 | c
 3 | 3 | d
 4 | 2 | e
 5 | 1 | f
 6 | 0 | g`
```

```
`SELECT * FROM my_keyspace.my_table ORDER BY (col1 DESC, col2 ASC, col3 DESC);

 col1 | col2 | col3
 ------+------+------
 6 | 0 | g
 5 | 1 | f
 4 | 2 | e
 3 | 3 | d
 2 | 4 | c
 1 | 5 | b
 0 | 6 | a`
```

If you don't specify the sort order in the query statement, the default ordering of the
clustering column is used.

The possible sort orders you can use in an ordering clause depend on the sort order assigned to each clustering column at table
creation. Query results can only be sorted in the order defined for all clustering
columns at table creation or the inverse of the defined sort order. Other possible combinations are not allowed.

For example, if the table's `CLUSTERING ORDER` is (col1 ASC, col2 DESC, col3 ASC), then the valid
parameters for `ORDER BY` are either (col1 ASC, col2 DESC, col3 ASC) or (col1 DESC,
col2 ASC, col3 DESC). For more information on `CLUSTERING ORDER`, see `table_options` under [CREATE TABLE](cql.ddl.md#cql.ddl.table.create "cql.ddl.md#cql.ddl.table.create").
