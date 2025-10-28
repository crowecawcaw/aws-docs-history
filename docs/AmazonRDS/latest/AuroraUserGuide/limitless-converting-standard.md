# Converting standard tables to limitless tables

You can convert standard tables into sharded or reference tables. During the conversion, data is moved from the standard table to the distributed
table, then the source standard table is deleted. Data is moved using the `INSERT INTO SELECT FROM` command.

###### Contents

- [Creating sharded tables](limitless-converting-standard.md#limitless-creating-sharded "limitless-converting-standard.md#limitless-creating-sharded")
- [Creating collocated tables](limitless-converting-standard.md#limitless-creating-sharded.colocated "limitless-converting-standard.md#limitless-creating-sharded.colocated")
- [Creating reference tables](limitless-converting-standard.md#limitless-creating-reference "limitless-converting-standard.md#limitless-creating-reference")

## Creating sharded tables

You create sharded tables by running the `rds_aurora.limitless_alter_table_type_sharded` procedure on standard tables. This
procedure takes a standard table and a list of columns, then distributes the given table using the list of columns as the shard key. The
procedure runs synchronously, and acquires an `ACCESS EXCLUSIVE` lock on the table.

After the procedure finishes successfully, the source standard table is deleted, and a sharded table with the same name becomes
available.

The `rds_aurora.limitless_alter_table_type_sharded` procedure uses the following syntax:

```
`postgres=>` CALL rds_aurora.limitless_alter_table_type_sharded('`schema`.`table`', ARRAY['`shard_key1`', '`shard_key2`', ... '`shard_keyn`']);
```

The procedure requires the following parameters:

- `schema` – The database schema that contains the table to be sharded. If the schema isn't specified, the procedure
  uses the `search_path`.
- `table` – The table to be sharded.
- `shard_key*n*` – An array of table columns to use as the shard key.

Shard key values are string literals, and are therefore case sensitive. If a shard key contains a single quote ('), use another single
quote to escape it. For example, if a table column is named `customer's id`, use `customer''s id` as the shard
key. Backslashes (\) and double quotes (") don't need to be escaped.

###### Note

All primary and unique keys must include the shard key. This means that the shard key is a subset of the primary or unique key.

In sharded tables, the `CHECK` constraint doesn't support expressions.

For more information, see [Constraints](limitless-reference.md#limitless-reference.DDL-limitations.Constraints "limitless-reference.md#limitless-reference.DDL-limitations.Constraints").

###### To create a sharded table

The following example shows how to create the `customer` sharded table with the shard key `customer_id`.

1. Create the standard table.

```
CREATE TABLE customer (customer_id INT PRIMARY KEY NOT NULL, zipcode INT, email VARCHAR);
```

2. Convert the standard table to a sharded table.

```
`postgres=>` CALL rds_aurora.limitless_alter_table_type_sharded('public.customer', ARRAY['customer_id']);

`postgres=>` \d

                    List of relations
 Schema |     Name     |       Type        |       Owner
--------+--------------+-------------------+--------------------
 public | customer     | partitioned table | postgres_limitless
 public | customer_fs1 | foreign table     | postgres_limitless
 public | customer_fs2 | foreign table     | postgres_limitless
 public | customer_fs3 | foreign table     | postgres_limitless
 public | customer_fs4 | foreign table     | postgres_limitless
 public | customer_fs5 | foreign table     | postgres_limitless
(6 rows)
```

## Creating collocated tables

If two or more tables are sharded using the same shard key, you can explicitly align (collocate) those tables. When two or more tables are
collocated, rows from those tables with the same shard key values are placed on the same shard. Collocation helps to restrict some operations to
a single shard, which results in better performance.

You use the `rds_aurora.limitless_alter_table_type_sharded` procedure with the following syntax:

```
`postgres=>` CALL rds_aurora.limitless_alter_table_type_sharded('`schema`.`collocated_table`', ARRAY['`shard_key1`', '`shard_key2`', ... '`shard_keyn`'], '`schema`.`sharded_table`');
```

The procedure requires the following parameters:

- `schema` – The database schema that contains the tables to be collocated. If the schema isn't specified, the
  procedure uses the `search_path`.
- `collocated_table` – The table to be collocated.
- `shard_key*n*` – An array of table columns to use as the shard key.

You must use the same shard key as for the original sharded table, including the same column names and column types.

- `sharded_table` – The sharded table with which you're collocating the `collocated_table`.

###### To create a collocated table

1. Create the first sharded table by following the procedure in [Creating sharded tables](#limitless-creating-sharded "#limitless-creating-sharded").
2. Create the standard table for the collocated table.

```
CREATE TABLE mytable2 (customer_id INT PRIMARY KEY NOT NULL, column1 INT, column2 VARCHAR);
```

3. Convert the standard table to a collocated table.

```
`postgres=>` CALL rds_aurora.limitless_alter_table_type_sharded('public.mytable2',
ARRAY['customer_id'], 'public.customer');

`postgres=>` \d

                    List of relations
 Schema |     Name     |       Type        |       Owner
--------+--------------+-------------------+--------------------
 public | customer     | partitioned table | postgres_limitless
 public | customer_fs1 | foreign table     | postgres_limitless
 public | customer_fs2 | foreign table     | postgres_limitless
 public | customer_fs3 | foreign table     | postgres_limitless
 public | customer_fs4 | foreign table     | postgres_limitless
 public | customer_fs5 | foreign table     | postgres_limitless
 public | mytable2     | partitioned table | postgres_limitless
 public | mytable2_fs1 | foreign table     | postgres_limitless
 public | mytable2_fs2 | foreign table     | postgres_limitless
 public | mytable2_fs3 | foreign table     | postgres_limitless
 public | mytable2_fs4 | foreign table     | postgres_limitless
 public | mytable2_fs5 | foreign table     | postgres_limitless
(12 rows)
```

## Creating reference tables

You create reference tables by running the `rds_aurora.limitless_alter_table_type_reference` procedure on standard tables. This
procedure replicates a given table to all shards in the DB shard group, and changes the table type to reference. The procedure runs
synchronously, and acquires an `ACCESS EXCLUSIVE` lock on the table.

After the procedure finishes successfully, the source standard table is deleted, and a reference table with the same name becomes
available.

The `rds_aurora.limitless_alter_table_type_reference` procedure uses the following syntax:

```
`postgres=>` CALL rds_aurora.limitless_alter_table_type_reference('`schema`.`table`');
```

The stored procedure requires the following parameters:

- `schema` – The database schema that contains the table to be replicated. If the schema isn't specified, the
  procedure uses the `search_path`.
- `table` – The table to be replicated.

###### Note

The standard table from which you create the reference table must have a primary key.

In reference tables, the `CHECK` constraint doesn't support expressions.

The previous function, `limitless_table_alter_type_reference`, is deprecated.

###### To create a reference table

The following example shows how to create the `zipcodes` reference table.

1. Create the standard table.

```
CREATE TABLE zipcodes (zipcode INT PRIMARY KEY, details VARCHAR);
```

2. Convert the standard table to a reference table.

```
CALL rds_aurora.limitless_alter_table_type_reference('public.zipcodes');

`postgres=>` \d

                    List of relations
 Schema |     Name     |       Type        |       Owner
--------+--------------+-------------------+--------------------
 public | customer     | partitioned table | postgres_limitless
 public | customer_fs1 | foreign table     | postgres_limitless
 public | customer_fs2 | foreign table     | postgres_limitless
 public | customer_fs3 | foreign table     | postgres_limitless
 public | customer_fs4 | foreign table     | postgres_limitless
 public | customer_fs5 | foreign table     | postgres_limitless
 public | zipcodes     | foreign table     | postgres_limitless
(7 rows)
```

The output shows the `customer` sharded table and the `zipcodes` reference table.
