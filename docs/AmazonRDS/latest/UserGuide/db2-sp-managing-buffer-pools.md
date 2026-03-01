# Stored procedures for buffer pools for RDS for Db2

The built-in stored procedures described in this topic manage buffer pools for
Amazon RDS for Db2 databases. To run these procedures, the master user must first connect to the
`rdsadmin` database.

These stored procedures are used in a variety of tasks. This list isn't exhaustive.

- [Common tasks for buffer pools](db2-managing-buffer-pools.md "db2-managing-buffer-pools.md")
- [Generating performance reports](db2-managing-databases.md#db2-generating-performance-reports "db2-managing-databases.md#db2-generating-performance-reports")
- [Copying database metadata with
  db2look](db2-native-db2-tools-db2look.md "db2-native-db2-tools-db2look.md")
- [Creating a repository database
  for IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md#db2-creating-repo-db-monitoring-dmc "db2-connecting-with-ibm-data-management-console.md#db2-creating-repo-db-monitoring-dmc")
  Refer to the following built-in stored procedures for information about their syntax,
  parameters, usage notes, and examples.

###### Stored procedures

- [rdsadmin.create_bufferpool](#db2-sp-create-buffer-pool "#db2-sp-create-buffer-pool")
- [rdsadmin.alter_bufferpool](#db2-sp-alter-buffer-pool "#db2-sp-alter-buffer-pool")
- [rdsadmin.drop_bufferpool](#db2-sp-drop-buffer-pool "#db2-sp-drop-buffer-pool")

## rdsadmin.create_bufferpool

Creates a buffer pool.

### Syntax

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

### Parameters

The following parameters are required:

`database_name`

The name of the database to run the command on. The data type is
`varchar`.

`buffer_pool_name`

The name of the buffer pool to create. The data type is
`varchar`.

The following parameters are optional:

`buffer_pool_size`

The size of the buffer pool in number of pages. The data type is
`integer`. The default is `-1`.

`immediate`

Specifies whether the command runs immediately. The data type is
`char`. The default is `Y`.

`automatic`

Specifies whether to set the buffer pool to automatic. The data type
is `char`. The default is `Y`.

`page_size`

The page size of the buffer pool. The data type is
`integer`. Valid values: `4096`,
`8192`, `16384`, `32768`. The
default is `8192`.

`number_block_pages`

The number of block pages in the buffer pools. The data type is
`integer`. The default is `0`.

`block_size`

The block size for the block pages. The data type is
`integer`. Valid values: `2` to
`256`. The default is `32`.

### Usage notes

For information about checking the status of creating a buffer pool, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

**Example 1: Creating buffer pool with default
parameters**

The following example creates a buffer pool called `BP8` for a database
called `TESTDB` with default parameters, so the buffer pool uses an 8 KB
page size.

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB',
    'BP8')"
```

**Example 2: Creating buffer pool to run immediately with
automatic allocation**

The following example creates a buffer pool called `BP16` for a
database called `TESTDB` that uses a 16 KB page size with an initial page
count of 1,000 and is set to automatic. Db2 runs the command immediately. If you use
an initial page count of -1, then Db2 will use automatic allocation of pages.

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB',
    'BP16',
    1000,
    'Y',
    'Y',
    16384)"
```

**Example 3: Creating buffer pool to run immediately using
block pages**

The following example creates a buffer pool called `BP16` for a
database called `TESTDB`. This buffer pool has a 16 KB page size with an
initial page count of 10,000. Db2 runs the command immediately using 500 block pages
with a block size of 512.

```
db2 "call rdsadmin.create_bufferpool(
    'TESTDB',
    'BP16',
    10000,
    'Y',
    'Y',
    16384,
    500,
    512)"
```

## rdsadmin.alter_bufferpool

Alters a buffer pool.

### Syntax

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

### Parameters

The following parameters are required:

`database_name`

The name of the database to run the command on. The data type is
`varchar`.

`buffer_pool_name`

The name of the buffer pool to alter. The data type is
`varchar`.

`buffer_pool_size`

The size of the buffer pool in number of pages. The data type is
`integer`.

The following parameters are optional:

`immediate`

Specifies whether the command runs immediately. The data type is
`char`. The default is `Y`.

`automatic`

Specifies whether to set the buffer pool to automatic. The data type
is `char`. The default is `N`.

`change_number_blocks`

Specifies whether there is a change to the number of block pages in
the buffer pool. The data type is `char`. The default is
`N`.

`number_block_pages`

The number of block pages in the buffer pools. The data type is
`integer`. The default is `0`.

`block_size`

The block size for the block pages. The data type is
`integer`. Valid values: `2` to
`256`. The default is `32`.

### Usage notes

For information about checking the status of altering a buffer pool, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

The following example alters a buffer pool called `BP16` for a database
called `TESTDB` to non-automatic, and changes the size to 10,000 pages.
Db2 runs this command immediately.

```
db2 "call rdsadmin.alter_bufferpool(
    'TESTDB',
    'BP16',
    10000,
    'Y',
    'N')"
```

## rdsadmin.drop_bufferpool

Drops a buffer pool.

### Syntax

```
db2 "call rdsadmin.drop_bufferpool(
    '`database_name`',
    '`buffer_pool_name`'"
```

### Parameters

The following parameters are required:

`database_name`

The name of the database that the buffer pool belongs to. The data
type is `varchar`.

`buffer_pool_name`

The name of the buffer pool to drop. The data type is
`varchar`.

### Usage notes

For information about checking the status of dropping a buffer pool, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

The following example drops a buffer pool called `BP16` for a database
called `TESTDB`.

```
db2 "call rdsadmin.drop_bufferpool(
    'TESTDB',
    'BP16')"
```
