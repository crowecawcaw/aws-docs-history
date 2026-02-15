# Supported clauses

The `SELECT` statement is used to retrieve data from one or more views.
AWS IoT SiteWise supports the `JOIN` and `INNER JOIN` operations.

Views are joined with an explicit `JOIN` syntax, or with comma-separated notations in the `FROM` clause.

###### Example

A general `SELECT` statement:

```
SELECT expression [, ...]
  [ FROM table_name AS alias [, ...] ]
  [ WHERE condition ]
  [ GROUP BY expression [, ...] ]
  [ HAVING condition ]
  [ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST ] [, ...] ]
  [ LIMIT expression ]

```

###### Example

A SELECT statement with the different clauses:

```
SELECT
  a.asset_name,
  a.asset_id,
  p.property_type,
  p.property_data_type,
  p.string_attribute_value,
  p.property_name
FROM asset a, asset_property p
WHERE a.asset_description LIKE '%description%'
AND p.property_type IN ('attribute', 'metric')
OR p.property_id IN (
  SELECT property_id
  FROM raw_time_series
  WHERE event_timestamp BETWEEN TIMESTAMP '2025-01-01 00:00:00' AND TIMESTAMP '2025-01-02 00:00:00'
  GROUP BY asset_id, property_id
  HAVING COUNT(*) > 100
 )
GROUP BY p.property_type
HAVING COUNT(*) > 5
ORDER BY a.asset_name ASC
LIMIT 20;

```

###### Note

An implicit `JOIN` combines two or more different tables without using the `JOIN` keyword
based on AWS IoT SiteWise's internal schema. This is the equivalent of performing a `JOIN` on the
`asset_id` and `property_id` fields between metadata and raw data tables.
This pattern allows SiteWise to leverage any given metadata filters in the query,
when fetching from raw data tables in a way that results in less overall data scanned.

###### Example of a query:

```
SELECT a.asset_name, p.property_name, r.event_timestamp
FROM asset a, asset_property p, raw_time_series r
WHERE a.asset_name='my_asset' AND p.property_name='my_property'

```

The above example only scans data from the asset property belonging to the specified metadata names.

###### Example of a less optimized equivalent of the above query:

```
SELECT a.asset_name, p.property_name, r.event_timestamp
FROM asset a
JOIN asset_property p ON a.asset_id=p.asset_id
JOIN raw_time_series r ON p.asset_id=r.asset_id AND p.property_id=r.property_id
WHERE a.asset_name='my_asset' AND p.property_name='my_property'

```

An explanation of each clause and it's description is listed below:

| **Clause**   | **Signature**                                                                                       | **Description**                                                                                                                                                                                                     |
| ------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `LIMIT`      | `<br>LIMIT { count }<br>`                                                                           | This clause limits the result set to the specified number of rows. You can use<br>`LIMIT` with or without `ORDER BY` and `OFFSET`<br>clauses.<br>`LIMIT` only works with non-negative integers from [0,2147483647]. |
| `ORDER BY`   | ```<br>ORDER BY expression<br>[ ASC                                                                 | DESC ]<br>[ NULLS FIRST                                                                                                                                                                                             | NULLS LAST ]<br>``` | The `ORDER BY` clause sorts the result set of a query.<br>Note<br>When referring to selected columns in an aggregation in the `ORDER BY` clause, use the column's ordinal index rather than the name or alias.<br>`<br>SELECT AVG(t.double_value)<br>FROM latest_value_time_series t<br>GROUP BY t.asset_id<br>ORDER BY 1<br>` |
| `GROUP BY`   | `<br>GROUP BY expression [, ...]<br>`                                                               | The `GROUP BY` clause identifies the grouping columns for the<br>query. It is used in conjunction with an aggregate expression.                                                                                     |
| `HAVING`     | `<br>HAVING boolean-expression<br>`                                                                 | The `HAVING` clause filters group rows created by the GROUP BY<br>clause.                                                                                                                                           |
| `SUB SELECT` | `<br>SELECT column1, column2<br>FROM table1<br>WHERE column3 IN (SELECT column4 FROM table2);<br>`  | A `SELECT` statement embedded within another `SELECT`<br>statement.                                                                                                                                                 |
| `JOIN`       | `<br>SELECT column1, column2<br>FROM table1 JOIN table2<br>ON table1.column1 = table2.column1;<br>` |
| `INNER JOIN` | `<br>SELECT columns<br>FROM table1<br>INNER JOIN table2 ON table1.column = table2.column;<br>`      | An `INNER JOIN` returns all rows from both tables, that match the join condition.                                                                                                                                   |
| `UNION`      | `<br>query<br>{ UNION [ ALL ] }<br>another_query<br>`                                               | The `UNION` operator computes the set union of its two arguments,<br>automatically removing duplicate records from the result set.                                                                                  |
