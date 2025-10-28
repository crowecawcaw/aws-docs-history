# Working with unlogged tables in

Aurora PostgreSQL

Amazon Aurora PostgreSQL supports unlogged tables that are crash-safe and maintain data
integrity even after writer instance failures or failovers. In standard PostgreSQL, unlogged
tables bypass the Write-Ahead Log (WAL) during write operations, resulting in faster write
speeds. However, this comes at the cost of reduced durability, as unlogged tables are not
crash-safe and can lose data after a system failure or unclean shutdown. These unlogged
tables are automatically truncated after a crash or unclean shutdown. Their contents and
indexes are also not replicated to standby servers.

In contrast, Aurora PostgreSQL handles unlogged tables differently due to its distributed
storage architecture. This is because Aurora's storage system does not rely on the
traditional PostgreSQL WAL for durability. However, the performance benefits typically
associated with unlogged tables in standard PostgreSQL may not be as significant in Aurora.
This is due to Aurora's distributed storage architecture, which can introduce additional
overhead compared to the local storage used in standard PostgreSQL.

When using unlogged tables in Aurora PostgreSQL, consider the following:

- You can access unlogged tables only from the writer node in the Aurora
  DB cluster.
- Reader nodes can access unlogged tables only when promoted to writer
  status.
- When you try to access unlogged tables from a reader node, it will result in the
  following error:

`cannot access temporary or unlogged relations during recovery.`

## Creating unlogged

tables

To create an unlogged table in Aurora PostgreSQL, add the UNLOGGED keyword in your CREATE
TABLE statement:

```

CREATE UNLOGGED TABLE staging_sales_data (
    transaction_id bigint,
    customer_id bigint,
    product_id bigint,
    transaction_date date,
    amount NUMERIC
);

```

## Handling unlogged tables

during migration

When preparing to migrate data to Aurora PostgreSQL, it's important to identify and handle
unlogged tables appropriately. Unlogged tables are not WAL-logged and are excluded from
the replication stream, meaning they will not be replicated to an Aurora read
replica.

Convert unlogged tables to logged tables or drop them if they are not being used
before creating an Aurora read replica.

To verify the presence of unlogged tables in each database within the instance, use
the following command:

```

SELECT oid, relfilenode, relname, relpersistence, relkind
FROM pg_class
WHERE relpersistence ='u';

```

To convert an unlogged table back to a logged table, use the following command:

```

ALTER TABLE `table_name` SET LOGGED;

```

This operation rewrites the entire table and places an exclusive lock on it until
completion. For large tables, this may result in significant downtime.

## Converting unlogged tables

to logged tables

When you need to convert an unlogged table back to a logged table, you can use the
following command:

```

ALTER TABLE `table_name` SET LOGGED;

```

This operation rewrites the entire table and places an exclusive lock on it until the
operation completes. For large tables, this can result in significant downtime.

## Unlogged tables and

logical replication

Unlogged tables are generally not included in logical replication because logical
replication relies on the WAL to capture and transfer changes. By default, changes to
unlogged tables are not WAL-logged and excluded from the replication stream, making them
unsuitable for use cases where logical replication is required. However, Aurora PostgreSQL
provides a parameter called `rds.logically_replicate_unlogged_tables` that
allows you to control this behavior:

- When `rds.logically_replicate_unlogged_tables` is set to 0 (off)
  the unlogged tables are excluded from logical replication.
- When `rds.logically_replicate_unlogged_tables` is set to 1 (on)
  the unlogged tables are included in logical replication.

###### Note

In Aurora PostgreSQL, the `rds.logically_replicate_unlogged_tables`
parameter is set by default to 1 (on) in versions 14 and earlier, and to 0 (off) in
versions 15 and later.
