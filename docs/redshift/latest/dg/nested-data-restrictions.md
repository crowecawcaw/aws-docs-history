Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Nested data limitations (preview)

This topic describes limitations for reading nested data with Redshift Spectrum. Nested data is
data that contains nested fields. Nested fields are fields that are joined together
as a single entity, such as arrays, structs, or objects.

###### Note

The limitations marked (preview) in the following list only
apply to preview clusters created
in the following Regions.

- US East (Ohio) (us-east-2)
- US East (N. Virginia) (us-east-1)
- US West (N. California) (us-west-1)
- Asia Pacific (Tokyo) (ap-northeast-1)
- Europe (Ireland) (eu-west-1)
- Europe (Stockholm) (eu-north-1)
  For information about
  setting up Preview clusters, see [Creating a
  preview cluster](../mgmt/managing-clusters-console.md#cluster-preview "../mgmt/managing-clusters-console.md#cluster-preview") in the _Amazon Redshift Management Guide_.

The following limitations apply to nested data:

- An `array` or `map` type can contain other
  `array` or `map` types as long as queries on
  the nested `arrays` or `maps` don't return `scalar` values. (preview)
- Amazon Redshift Spectrum supports complex data types only as external
  tables.
- Subquery result columns must be top-level. (preview)
- If an `OUTER JOIN` expression refers to a nested table, it can
  refer only to that table and its nested arrays (and maps). If an `OUTER
JOIN` expression doesn't refer to a nested table, it can refer to
  any number of non-nested tables.
- If a `FROM` clause in a subquery refers to a nested table, it
  can't refer to any other table.
- If a subquery depends on a nested table that refers to a parent table, the subquery can
  only use the parent table in the `FROM` clause. You can't use the parent in
  any other clauses, such as a `SELECT` or `WHERE` clause.
  For example, the following query doesn't run because the subquery's `SELECT`
  clause refers to the parent table `c`.

```
SELECT c.name.given
FROM   spectrum.customers c
WHERE (SELECT COUNT(c.id) FROM c.phones p WHERE p LIKE '858%') > 1;
```

The following query works because the parent `c` is used only
in the `FROM` clause of the subquery.

```
SELECT c.name.given
FROM   spectrum.customers c
WHERE (SELECT COUNT(*) FROM c.phones p WHERE p LIKE '858%') > 1;
```

- A subquery that accesses nested data anywhere other than the
  `FROM` clause must return a single value. The only exceptions
  are `(NOT) EXISTS` operators in a `WHERE`
  clause.
- `(NOT) IN` is not supported.
- The maximum nesting depth for all nested types is 100. This restriction
  applies to all file formats (Parquet, ORC, Ion, and JSON).
- Aggregation subqueries that access nested data can only refer to `arrays` and `maps` in their `FROM` clause, not to an external table.
- Querying the pseudocolumns of nested data in a Redshift Spectrum table is not supported. For more information, see
  [Pseudocolumns](c-spectrum-external-tables.md#c-spectrum-external-tables-pseudocolumns "c-spectrum-external-tables.md#c-spectrum-external-tables-pseudocolumns").
- When extracting data from array or map columns by specifying them in a
  `FROM` clause, you can only select values from those columns
  if the values are `scalar`. For example, the following queries both try to `SELECT`
  elements from inside an array. The query that selects `arr.a` works
  because `arr.a` is a `scalar` value. The second query doesn't work
  because `array` is an array extracted from `s3.nested table`
  in the `FROM` clause. (preview)

```
SELECT array_column FROM s3.nested_table;

`array_column
-----------------
[{"a":1},{"b":2}]`

SELECT arr.a FROM s3.nested_table t, t.array_column arr;

`arr.a
-----
1`

--This query fails to run.
SELECT array FROM s3.nested_table tab, tab.array_column array;

```

You can’t use an array or map in the `FROM` clause that
itself comes from another array or map. To select arrays or other complex
structures that are nested inside other arrays, consider
using indexes in the `SELECT` statement.
