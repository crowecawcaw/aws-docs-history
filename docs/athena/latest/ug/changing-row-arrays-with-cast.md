# Change field names in arrays using

`CAST`

To change the field name in an array that contains `ROW` values, you can
`CAST` the `ROW` declaration:

```
WITH dataset AS (
  SELECT
    CAST(
      ROW('Bob', 38) AS ROW(name VARCHAR, age INTEGER)
    ) AS users
)
SELECT * FROM dataset
```

This query returns:

````
+--------------------+
| users              | +--------------------+
| {NAME=Bob, AGE=38} | +--------------------+ ``` ###### Note In the example above, you declare `name` as a `VARCHAR` because this is its type in Presto. If you declare this `STRUCT` inside a `CREATE TABLE` statement, use `String` type because Hive defines this data type as `String`.
````
