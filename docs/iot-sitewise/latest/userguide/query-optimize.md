# Query optimization

## Metadata filters

When you query metadata or raw data, use the `WHERE` clause to filter by metadata fields to reduce the amount
of data scanned. Use the following operators to limit the metadata scan:

- Equals (=)
- Not equals (!=)
- LIKE
- IN
- AND
- OR

For attribute properties, use the following fields to filter results.:

- `double_attribute_value`
- `int_attribute_value`
- `boolean_attribute_value`
- `string_attribute_value`

These fields provide better performance than the **latest_value_time_series** table
for asset properties of attribute type.

###### Note

Use literals on the right side of operators to properly limit the data scan.
For example, the following query performs worse than using a strict string literal:

```
SELECT property_id FROM asset_property WHERE property_name = CONCAT('my', 'property')
```

###### Example for metadata filters:

```
SELECT p.property_name FROM asset_property p
WHERE p.property_type = 'attribute' AND p.string_attribute_value LIKE 'my-property-%'

```

## Raw data filters

All raw data tables (**raw_time_series**,
**latest_value_time_series**, **precomputed_aggregates**) have
timestamps associated with their rows. In addition to metadata filters, use `WHERE`
clause filters on the `event_timestamp` field to reduce the amount of data scanned.
Use the following operations to limit the raw data scan:

- Equals (=)
- Greater than (>)
- Less than (<)
- Greater than or equals (>=)
- Less than or equals (<=)
- BETWEEN
- AND

**Examples of filters**:

- When querying the **precomputed_aggregates** table, always specify a quality filter in the `WHERE` clause.
  This reduces the amount of data that the query scans, especially if you're looking for `BAD` or `UNCERTAIN` data.

We also highly recommend using a resolution filter (1m, 15m, 1h, or 1d) when querying the
**precomputed_aggregates** table. If you don't specify a resolution filter,
AWS IoT SiteWise will default to a full table scan across all resolutions, which is inefficient.

- When querying raw data, timestamp functions can also be used in the `WHERE` clause to filter the amount of data scanned.
  For example, the following query only scans the last 30 minutes of data from the **raw_time_series** table:

```
SELECT r.event_timestamp, r.double_value
FROM raw_time_series r
WHERE r.event_timestamp > TIMESTAMP_SUB(MINUTE, 30, NOW())
```

###### Note

Not equals `(!=)` and `OR` operators typically don't apply meaningful filters
to the raw data scan.
Filters on raw data values (string_value, double_value, etc.) also don't limit the raw data scan.

## JOIN optimization

AWS IoT SiteWise SQL supports the `JOIN` keyword to merge two tables together.
Only `JOIN`s that actively filter on a field (using the `ON` keyword) are supported.
Full Cartesian joins are prohibited.

AWS IoT SiteWise also supports implicit `JOIN`s without using the `JOIN` keyword. These are allowed
between different metadata tables and between a metadata table and a raw table. For example, this query:

```
SELECT a.asset_name, p.property_name FROM asset a, asset_property p
```

Performs better than this equivalent query:

```
SELECT a.asset_name, p.property_name FROM asset a
JOIN asset_property p ON a.asset_id = p.asset_id
```

The following implicit joins are allowed (O is allowed, X is prohibited):

|                          | asset | asset_property | latest_value_time_series | raw_time_series | precomputed_aggregates | subquery |
| ------------------------ | ----- | -------------- | ------------------------ | --------------- | ---------------------- | -------- |
| asset                    | X     | O              | O                        | O               | O                      | X        |
| asset_property           | O     | X              | O                        | O               | O                      | X        |
| latest_value_time_series | O     | O              | X                        | X               | X                      | X        |
| raw_time_series          | O     | O              | X                        | X               | X                      | X        |
| precomputed_aggregates   | O     | O              | X                        | X               | X                      | X        |
| subquery                 | X     | X              | X                        | X               | X                      | X        |

Use implicit `JOIN`s where possible. If you must use the `JOIN` keyword, apply filters on the individual `JOIN`ed tables to minimize data scanned. For example, instead of this query:

```
SELECT level1.asset_id, level2.asset_id, level3.asset_id
FROM asset AS level1
JOIN asset AS level2 ON level2.parent_asset_id = level1.asset_id
JOIN asset AS level3 ON level3.parent_asset_id = level2.asset_id
WHERE level1.asset_name LIKE 'level1%'
AND level2.asset_name LIKE 'level2%'
AND level3.asset_name LIKE 'level3%'
```

Use this more efficient query:

```
SELECT level1.asset_id, level2.asset_id, level3.asset_id
FROM asset AS level1
JOIN (SELECT asset_id, parent_asset_id FROM asset WHERE asset_name LIKE 'level2%') AS level2 ON level2.parent_asset_id = level1.asset_id
JOIN (SELECT asset_id, parent_asset_id FROM asset WHERE asset_name LIKE 'level3%') AS level3 ON level3.parent_asset_id = level2.asset_id
WHERE level1.asset_name LIKE 'level1%'
```

By pushing metadata filters into subqueries, you ensure that individual tables in the `JOIN`s are
filtered during the scanning process. You can also use the `LIMIT` keyword in subqueries for the same effect.

## Large queries

For queries that produce more rows than the default,
set the page size of the
[ExecuteQuery](../APIReference/API_ExecuteQuery.md "../APIReference/API_ExecuteQuery.md") API
to the maximum value of 20000. This improves overall query performance.

Use the `LIMIT` clause to reduce the amount of data scanned for some queries.
Note that aggregate functions and certain table-wide clauses (`GROUP BY`, `ORDER BY`,
`JOIN`) require a full scan to complete before applying the `LIMIT` clause.

###### Note

AWS IoT SiteWise may scan a minimum amount of data even with the `LIMIT` clause applied,
especially for raw data queries that scan over multiple properties.
