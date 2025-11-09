Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_TABLE_DEF

Stores information about table columns.

PG_TABLE_DEF only returns information about tables that are visible to the user. If
PG_TABLE_DEF does not return the expected results, verify that the [search_path](r_search_path.md "r_search_path.md") parameter is set correctly
to include the relevant schemas.

You can use [SVV_TABLE_INFO](r_SVV_TABLE_INFO.md "r_SVV_TABLE_INFO.md") to
view more comprehensive information about a table, including data distribution skew, key
distribution skew, table size, and statistics.

## Table columns

| Column name | Data type     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| schemaname  | name          | Schema name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| tablename   | name          | Table name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| column      | name          | Column name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| type        | text          | Datatype of column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| encoding    | character(32) | Encoding of column.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| distkey     | boolean       | True if this column is the distribution key for<br>the table.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| sortkey     | integer       | Order of the column in the sort key. If the table<br>uses a compound sort key, then all columns that are part of the sort<br>key have a positive value that indicates the position of the column<br>in the sort key. If the table uses an interleaved sort key, then<br>each column that is part of the sort key has a value that is<br>alternately positive or negative, where the absolute value indicates<br>the position of the column in the sort key. If 0, the column is not<br>part of a sort key. |
| notnull     | boolean       | True if the column has a NOT NULL<br>constraint.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Example

The following example shows the compound sort key columns for the
LINEORDER_COMPOUND table.

```
select "column", type, encoding, distkey, sortkey, "notnull"
from pg_table_def
where tablename = 'lineorder_compound'
and sortkey <> 0;

column       | type    | encoding | distkey | sortkey | notnull
-------------+---------+----------+---------+---------+--------
lo_orderkey  | integer | delta32k | false   |       1 | true
lo_custkey   | integer | none     | false   |       2 | true
lo_partkey   | integer | none     | true    |       3 | true
lo_suppkey   | integer | delta32k | false   |       4 | true
lo_orderdate | integer | delta    | false   |       5 | true
(5 rows)
```

The following example shows the interleaved sort key columns for the
LINEORDER_INTERLEAVED table.

```
select "column", type, encoding, distkey, sortkey, "notnull"
from pg_table_def
where tablename = 'lineorder_interleaved'
and sortkey <> 0;

column       | type    | encoding | distkey | sortkey | notnull
-------------+---------+----------+---------+---------+--------
lo_orderkey  | integer | delta32k | false   |      -1 | true
lo_custkey   | integer | none     | false   |       2 | true
lo_partkey   | integer | none     | true    |      -3 | true
lo_suppkey   | integer | delta32k | false   |       4 | true
lo_orderdate | integer | delta    | false   |      -5 | true
(5 rows)
```

PG_TABLE_DEF will only return information for tables in schemas that are included
in the search path. For more information, see [search_path](r_search_path.md "r_search_path.md").

For example, suppose you create a new schema and a new table, then query
PG_TABLE_DEF.

```
create schema demo;
create table demo.demotable (one int);
select * from pg_table_def where tablename = 'demotable';

schemaname|tablename|column| type | encoding | distkey | sortkey | notnull
----------+---------+------+------+----------+---------+---------+--------
```

The query returns no rows for the new table. Examine the setting for
`search_path`.

```
show search_path;

  search_path
---------------
 $user, public
(1 row)
```

Add the `demo` schema to the search path and run the query
again.

```
set search_path to '$user', 'public', 'demo';

select * from pg_table_def where tablename = 'demotable';

schemaname| tablename |column|  type   | encoding |distkey|sortkey| notnull
----------+-----------+------+---------+----------+-------+-------+--------
demo      | demotable | one  | integer | none     | f     |     0 | f
(1 row)
```
