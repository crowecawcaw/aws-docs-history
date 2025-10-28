# Common tasks for buffer pools

You can create, alter, or drop buffer pools for an RDS for Db2 database. Creating, altering,
or dropping buffer pools requires higher-level `SYSADM` or `SYSCTRL`
authority, which isn't available to the master user. Instead, use Amazon RDS stored
procedures.

You can also flush buffer pools.

###### Topics

- [Creating a buffer pool](#db2-creating-buffer-pool "#db2-creating-buffer-pool")
- [Altering a buffer pool](#db2-altering-buffer-pool "#db2-altering-buffer-pool")
- [Dropping a buffer pool](#db2-dropping-buffer-pool "#db2-dropping-buffer-pool")
- [Flushing the buffer pools](#db2-flushing-buffer-pools "#db2-flushing-buffer-pools")

## Creating a buffer pool

To create a buffer pool for your RDS for Db2 database, call the
`rdsadmin.create_bufferpool` stored procedure. For more information, see
[CREATE BUFFERPOOL statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-bufferpool "https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-bufferpool") in the IBM Db2
documentation.

###### To create a buffer pool

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Create a buffer pool by calling `rdsadmin.create_bufferpool`. For
   more information, see [rdsadmin.create_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-create-buffer-pool").

```
db2 "call rdsadmin.create_bufferpool(
    '`database_name`',
    '`buffer_pool_name`',
    `buffer_pool_size`,
    '`immediate`',
    '`automatic`',
    `page_size`,
    `number_block_pages`,
    `block_size`)"
```

## Altering a buffer pool

To alter a buffer pool for your RDS for Db2 database, call the
`rdsadmin.alter_bufferpool` stored procedure. For more information, see
[ALTER BUFFERPOOL statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-alter-bufferpool "https://www.ibm.com/docs/en/db2/11.5?topic=statements-alter-bufferpool") in the IBM Db2
documentation.

###### To alter a buffer pool

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Alter a buffer pool by calling `rdsadmin.alter_bufferpool`. For
   more information, see [rdsadmin.alter_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-alter-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-alter-buffer-pool").

```
db2 "call rdsadmin.alter_bufferpool(
    '`database_name`',
    '`buffer_pool_name`',
    `buffer_pool_size`,
    '`immediate`',
    '`automatic`',
    `change_number_blocks`,
    `number_block_pages`,
    `block_size`)"
```

## Dropping a buffer pool

To drop a buffer pool for your RDS for Db2 database, call the
`rdsadmin.drop_bufferpool` stored procedure. For more information, see
[Dropping buffer pools](https://www.ibm.com/docs/en/db2/11.5?topic=pools-dropping-buffer "https://www.ibm.com/docs/en/db2/11.5?topic=pools-dropping-buffer") in the IBM Db2 documentation.

###### Important

Make sure that no tablespaces are assigned to the buffer pool that you want to
drop.

###### To drop a buffer pool

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Drop a buffer pool by calling `rdsadmin.drop_bufferpool`. For more
   information, see [rdsadmin.drop_bufferpool](db2-sp-managing-buffer-pools.md#db2-sp-drop-buffer-pool "db2-sp-managing-buffer-pools.md#db2-sp-drop-buffer-pool").

```
db2 "call rdsadmin.drop_bufferpool(
    '`database_name`',
    '`buffer_pool_name`')"
```

## Flushing the buffer pools

You can flush the buffer pools to force a checkpoint so that RDS for Db2 writes pages
from memory to storage.

###### Note

You don't need to flush the buffer pools. Db2 writes logs synchronously before it
commits transactions. The dirty pages might still be in a buffer pool, but Db2
writes them to storage asynchronously. Even if the system shuts down unexpectedly,
when you restart the database, Db2 automatically performs crash recovery. During
crash recovery, Db2 writes committed changes to the database or rolls back changes
for uncommitted transactions.

###### To flush the buffer pools

1. Connect to your Db2 database using the master username and master password for
   your RDS for Db2 DB instance. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with your own information.

```
db2 connect to `rds_database_alias` user `master_username` using `master_password`
```

2. Flush the buffer pools.

```
db2 flush bufferpools all
```
