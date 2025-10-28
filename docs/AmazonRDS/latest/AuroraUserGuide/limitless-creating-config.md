# Creating limitless tables by using variables

You can use variables to create sharded and reference tables by setting the table creation mode. Then the tables that you create will use this
mode until you set a different mode.

Use the following variables to create sharded and reference tables:

- `rds_aurora.limitless_create_table_mode` – Set this session variable to `sharded` or `reference`.
  The default value of this variable is `standard`.
- `rds_aurora.limitless_create_table_shard_key` – Set this session variable to an array of column names to use as shard
  keys. This variable is ignored when `rds_aurora.limitless_create_table_mode` isn't `sharded`.

Format the value as `untyped array literal`, similar to when you insert literals into an array column. For more information,
see [Arrays](https://www.postgresql.org/docs/current/arrays.html "https://www.postgresql.org/docs/current/arrays.html") in the PostgreSQL documentation.

- `rds_aurora.limitless_create_table_collocate_with` – Set this session variable to a specific table name to collocate
  newly created tables with that table.

If two or more tables are sharded using the same shard key, you can explicitly align (collocate) those tables. When two or more tables are
collocated, rows from those tables with the same shard key values are placed on the same shard. Collocation helps to restrict some
operations to a single shard, which results in better performance.

###### Note

All primary and unique keys must include the shard key. This means that the shard key is a subset of the primary or unique key.

Limitless tables have some limitations. For more information, see [DDL limitations and other information for Aurora PostgreSQL Limitless Database](limitless-reference.md "limitless-reference.md").

###### Topics

- [Examples using variables to create limitless tables](#limitless-tables-examples "#limitless-tables-examples")
- [Aurora PostgreSQL Limitless Database table views](#limitless-table-views "#limitless-table-views")

## Examples using variables to create limitless tables

The following examples show how to use these variables to create sharded and reference tables.

Create a sharded table named `items`, with the shard key `id`.

```
BEGIN;
SET LOCAL rds_aurora.limitless_create_table_mode='sharded';
SET LOCAL rds_aurora.limitless_create_table_shard_key='{"id"}';
CREATE TABLE items(id int, val int, item text);
COMMIT;
```

Create a sharded table named `items`, with a shard key composed of the `item_id` and `item_cat`
columns.

```
BEGIN;
SET LOCAL rds_aurora.limitless_create_table_mode='sharded';
SET LOCAL rds_aurora.limitless_create_table_shard_key='{"item_id", "item_cat"}';
CREATE TABLE items(item_id int, item_cat varchar, val int, item text);
COMMIT;
```

Create a sharded table named `item_description`, with a shard key composed of the `item_id` and `item_cat`
columns, and collocate it with the `items` table from the previous example.

```
BEGIN;
SET LOCAL rds_aurora.limitless_create_table_mode='sharded';
SET LOCAL rds_aurora.limitless_create_table_shard_key='{"item_id", "item_cat"}';
SET LOCAL rds_aurora.limitless_create_table_collocate_with='items';
CREATE TABLE item_description(item_id int, item_cat varchar, color_id int);
COMMIT;
```

Create a reference table named `colors`.

```
BEGIN;
SET LOCAL rds_aurora.limitless_create_table_mode='reference';
CREATE TABLE colors(color_id int primary key, color varchar);
COMMIT;
```

To reset the `rds_aurora.limitless_create_table_mode` session variable to `standard`, use the following
statement:

```
RESET rds_aurora.limitless_create_table_mode;
```

After you reset this variable, tables are created as standard tables, which is the default. For more information on standard tables, see [Converting standard tables to limitless tables](limitless-converting-standard.md "limitless-converting-standard.md").

## Aurora PostgreSQL Limitless Database table views

You can find information about Limitless Database tables by using the following views.

**rds_aurora.limitless_tables**

The `rds_aurora.limitless_tables` view contains information about limitless tables and their types.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_tables;

 table_gid | local_oid | schema_name | table_name  | table_status | table_type  | distribution_key
-----------+-----------+-------------+-------------+--------------+-------------+------------------
         5 |     18635 | public      | standard    | active       | standard    |
         6 |     18641 | public      | ref         | active       | reference   |
         7 |     18797 | public      | orders      | active       | sharded     | HASH (order_id)
         2 |     18579 | public      | customer    | active       | sharded     | HASH (cust_id)
(4 rows)
```

**rds_aurora.limitless_table_collocations**

The `rds_aurora.limitless_table_collocations` view contains information about collocated sharded tables. For example,
the `orders` and `customers` tables are collocated, and have the same `collocation_id`. The
`users` and `followers` tables are collocated, and have the same `collocation_id`.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_table_collocations ORDER BY collocation_id;

 collocation_id | schema_name | table_name
----------------+-------------+------------
          16002 | public      | orders
          16002 | public      | customers
          16005 | public      | users
          16005 | public      | followers
(4 rows)
```

**rds_aurora.limitless_table_collocation_distributions**

The `rds_aurora.limitless_table_collocation_distributions` shows the key distribution for each collocation.

```
postgres_limitless=> SELECT * FROM rds_aurora.limitless_table_collocation_distributions ORDER BY collocation_id, lower_bound;

 collocation_id | subcluster_id |     lower_bound      |     upper_bound
----------------+---------------+----------------------+----------------------
          16002 |             6 | -9223372036854775808 | -4611686018427387904
          16002 |             5 | -4611686018427387904 |                    0
          16002 |             4 |                    0 |  4611686018427387904
          16002 |             3 |  4611686018427387904 |  9223372036854775807
          16005 |             6 | -9223372036854775808 | -4611686018427387904
          16005 |             5 | -4611686018427387904 |                    0
          16005 |             4 |                    0 |  4611686018427387904
          16005 |             3 |  4611686018427387904 |  9223372036854775807
(8 rows)
```
