Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using a user-defined function (UDF) in a materialized view

You can use a scalar UDF in an Amazon Redshift materialized view. Define these either in python
or SQL and reference them in the materialized view definition.

## Referencing a UDF in a materialized view

The following procedure shows how to use UDFs that perform simple
arithmetic comparisons, in a materialized-view definition.

1. Create a table to use in the materialized-view definition.

```
CREATE TABLE base_table (a int, b int);
```

2. Create a scalar user-defined function in python that returns a boolean value
   indicating whether an integer is larger than a comparison integer.

```
CREATE OR REPLACE FUNCTION udf_python_bool(x1 int, x2 int) RETURNS bool IMMUTABLE
AS $$
  return x1 > x2
$$ LANGUAGE plpythonu;
```

Optionally, create a functionally similar UDF with SQL, which you can use to compare results with the first.

```
CREATE OR REPLACE FUNCTION udf_sql_bool(int, int) RETURNS bool IMMUTABLE
AS $$
  select $1 > $2;
$$ LANGUAGE SQL;
```

3. Create a materialized view that selects from the table you created and references the UDF.

```
CREATE MATERIALIZED VIEW mv_python_udf AS SELECT udf_python_bool(a, b) AS a FROM base_table;
```

Optionally, you can create a materialized view that references the SQL UDF.

```
CREATE MATERIALIZED VIEW mv_sql_udf AS SELECT udf_sql_bool(a, b) AS a FROM base_table;
```

4. Add data to the table and refresh the materialized view.

```
INSERT INTO base_table VALUES (1,2), (1,3), (4,2);
```

```
REFRESH MATERIALIZED VIEW mv_python_udf;
```

Optionally, you can refresh the materialized view that references the SQL UDF.

```
REFRESH MATERIALIZED VIEW mv_sql_udf;
```

5. Query data from your materialized view.

```
SELECT * FROM mv_python_udf ORDER BY a;
```

The results of the query are the following:

```
a
-----
false
false
true
```

This returns `true` for the last set of values because the value for
column `a` (4) is greater than the value for column `b` (2). 6. Optionally, you can query the materialized view that references the SQL UDF. The results for the SQL
function match the results from the Python version.

```
SELECT * FROM mv_sql_udf ORDER BY a;
```

The results of the query are the following:

```
a
-----
false
false
true
```

This returns `true` for the last set of values to compare. 7. Use a DROP statement with CASCADE to drop the user-defined function and the materialized
view that references it.

```
DROP FUNCTION udf_python_bool(int, int) CASCADE;
```

```
DROP FUNCTION udf_sql_bool(int, int) CASCADE;
```
