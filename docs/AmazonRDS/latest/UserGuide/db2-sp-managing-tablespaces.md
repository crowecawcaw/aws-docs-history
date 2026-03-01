# Stored procedures for tablespaces for RDS for Db2

The built-in stored procedures described in this topic manage tablespaces for Amazon RDS for Db2
databases. To run these procedures, the master user must first connect to the
`rdsadmin` database.

These stored procedures are used in a variety of tasks. This list isn't exhaustive.

- [Common tasks for tablespaces](db2-managing-tablespaces.md "db2-managing-tablespaces.md")
- [Generating performance reports](db2-managing-databases.md#db2-generating-performance-reports "db2-managing-databases.md#db2-generating-performance-reports")
- [Copying database metadata with db2look](db2-native-db2-tools-db2look.md "db2-native-db2-tools-db2look.md")
- [Creating a repository database for
  IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md#db2-creating-repo-db-monitoring-dmc "db2-connecting-with-ibm-data-management-console.md#db2-creating-repo-db-monitoring-dmc")
  Refer to the following built-in stored procedures for information about their syntax,
  parameters, usage notes, and examples.

###### Stored procedures

- [rdsadmin.create_tablespace](#db2-sp-create-tablespace "#db2-sp-create-tablespace")
- [rdsadmin.alter_tablespace](#db2-sp-alter-tablespace "#db2-sp-alter-tablespace")
- [rdsadmin.rename_tablespace](#db2-sp-rename-tablespace "#db2-sp-rename-tablespace")
- [rdsadmin.drop_tablespace](#db2-sp-drop-tablespace "#db2-sp-drop-tablespace")

## rdsadmin.create_tablespace

Creates a tablespace.

### Syntax

```
db2 "call rdsadmin.create_tablespace(
    '`database_name`',
    '`tablespace_name`',
    '`buffer_pool_name`',
    `tablespace_page_size`,
    `tablespace_initial_size`,
    `tablespace_increase_size`,
    '`tablespace_type`',
    '`tablespace_prefetch_size`')"
```

### Parameters

The following parameters are required:

`database_name`

The name of the database to create the tablespace in. The data type is
`varchar`.

`tablespace_name`

The name of the tablespace to create. The data type is
`varchar`.

The tablespace name has the following restrictions:

- It can't be the same as the name of an existing tablespace in
  this database.
- It can only contain the characters
  `_$#@a-zA-Z0-9`.
- It can't start with `_` or `$`.
- It can't start with `SYS`.

The following parameters are optional:

`buffer_pool_name`

The name of the buffer pool to assign the tablespace. The data type is
`varchar`. The default is an empty string.

###### Important

You must already have a buffer pool of the same page size to
associate with the tablespace.

`tablespace_page_size`

The page size of the tablespace in bytes. The data type is
`integer`. Valid values: `4096`,
`8192`, `16384`, `32768`. The
default is the page size used when you created the database by calling
[rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database").

###### Important

Amazon RDS supports write atomicity for 4 KiB, 8 KiB, and 16 KiB pages.
In contrast, 32 KiB pages risk torn writes, or partial data being
written to the desk. If you use 32 KiB pages, we recommend that you
enable point-in-time recovery and automated backups. Otherwise, you
run the risk of being unable to recover from torn pages. For more
information, see [Introduction to backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md")
and [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

`tablespace_initial_size`

The initial size of the tablespace in kilobytes (KB). The data type is
`integer`. Valid values: `48` or higher. The
default is null.

If you don't set a value, Db2 sets an appropriate value for you.

###### Note

This parameter isn't applicable for temporary tablespaces because
the system manages temporary tablespaces.

`tablespace_increase_size`

The percentage by which to increase the tablespace when it becomes
full. The data type is `integer`. Valid values:
`1`–`100`. The default is null.

If you don't set a value, Db2 sets an appropriate value for
you.

###### Note

This parameter isn't applicable for temporary tablespaces because
the system manages temporary tablespaces.

`tablespace_type`

The type of the tablespace. The data type is `char`. Valid
values: `U` (for user data), `T` (for user
temporary data), or `S` (for system temporary data). The
default is `U`.

`tablespace_prefetch_size`

The prefetch page size of the tablespace. The data type is
`char`. Valid values: `AUTOMATIC` (case
insensitive), or non-zero positive integers that are less than or equal
to 32767.

### Usage notes

RDS for Db2 always creates a large database for data.

For information about checking the status of creating a tablespace, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

**Example 1: Creating a tablespace and assigning a buffer
pool**

The following example creates a tablespace called `SP8` and assigns a
buffer pool called `BP8` for a database called `TESTDB`. The
tablespace has an initial tablespace page size of 4,096 bytes, an initial tablespace
of 1,000 KB, and a table size increase set to 50%.

```
db2 "call rdsadmin.create_tablespace(
    'TESTDB',
    'SP8',
    'BP8',
    4096,
    1000,
    50)"
```

**Example 2: Creating a temporary tablespace and assigning a
buffer pool**

The following example creates a temporary tablespace called `SP8`. It
assigns a buffer pool called `BP8` that is 8 KiB in size for a database
called `TESTDB`.

```
db2 "call rdsadmin.create_tablespace(
    'TESTDB',
    'SP8',
    'BP8',
    8192,
    NULL,
    NULL,
    'T')"
```

**Example 3: Creating a tablespace and assigning a prefetch
page size**

The following example creates a tablespace called `SP8` for a database
called `TESTDB`. The tablespace has an initial tablespace increase size
of `50` and a prefetch page size of `800`.

```
db2 "call rdsadmin.create_tablespace(
    'TESTDB',
    'SP8',
    NULL,
    NULL,
    NULL,
    50,
    NULL,
    '800')"

```

## rdsadmin.alter_tablespace

Alters a tablespace.

### Syntax

```
db2 "call rdsadmin.alter_tablespace(
    '`database_name`',
    '`tablespace_name`',
    '`buffer_pool_name`',
    `tablespace_increase_size`,
    '`max_size`',
    '`reduce_max`',
    '`reduce_stop`',
    '`reduce_value`',
    '`lower_high_water`',
    '`lower_high_water_stop`',
    '`switch_online`',
    '`tablespace_prefetch_size`')"
```

### Parameters

The following parameters are required:

`database_name`

The name of the database that uses the tablespace. The data type is
`varchar`.

`tablespace_name`

The name of the tablespace to alter. The data type is
`varchar`.

The following parameters are optional:

`buffer_pool_name`

The name of the buffer pool to assign the tablespace. The data type is
`varchar`. The default is an empty string.

###### Important

You must already have a buffer pool of the same page size to
associate with the tablespace.

`tablespace_increase_size`

The percentage by which to increase the tablespace when it becomes
full. The data type is `integer`. Valid values:
`1`–`100`. The default is
`0`.

`max_size`

The maximum size for the tablespace. The data type is
`varchar`. Valid values:
`integer`
`K` | `M` | `G`, or `NONE`.
The default is `NONE`.

`reduce_max`

Specifies whether to reduce the high water mark to its maximum limit.
The data type is `char`. The default is
`N`.

`reduce_stop`

Specifies whether to interrupt a previous `reduce_max` or
`reduce_value` command. The data type is
`char`. The default is `N`.

`reduce_value`

The number or percentage to reduce the tablespace high water mark by.
The data type is `varchar`. Valid values:
`integer`
`K`| `M` | `G`, or
`1`–`100`. The default is
`N`.

`lower_high_water`

Specifies whether to run the `ALTER TABLESPACE LOWER HIGH WATER
 MARK` command. The data type is `char`. The default
is `N`.

`lower_high_water_stop`

Specifies whether to run the `ALTER TABLESPACE LOWER HIGH WATER
 MARK STOP` command. The data type is `char`. The
default is `N`.

`switch_online`

Specifies whether to run the `ALTER TABLESPACE SWITCH
 ONLINE` command. The data type is `char`. The
default is `N`.

`tablespace_prefetch_size`

The prefetch page size of the tablespace. The data type is
`char`. Valid values: `AUTOMATIC` (case
insensitive), or non-zero positive integers that are less than or equal
to 32767.

###### Note

This parameter only works with `buffer_pool_name`,
`table_increase_size`, `max_size`, and
`switch_online`. It doesn't work with
`reduce_max`, `reduce_stop`,
`reduce_value`, `lower_high_water`, and
`lower_high_water_stop`.

### Usage notes

Before calling the stored procedure, review the following considerations:

- The `rdsadmin.alter_tablespace` stored procedure won't work on
  a tablespace with the `tablespace_type` set to `T` for
  user temporary data.
- The optional parameters `reduce_max`, `reduce_stop`,
  `reduce_value`, `lower_high_water`,
  `lower_high_water_stop`, and `switch_online` are
  mutually exclusive. You can't combine them with any other optional
  parameter, such as `buffer_pool_name`, in the
  `rdsadmin.alter_tablespace` command. For more information,
  see [Statement not valid](db2-troubleshooting.md#alter-tablespace-sp-statement-not-valid "db2-troubleshooting.md#alter-tablespace-sp-statement-not-valid").

For information about checking the status of altering a tablespace, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

For error messages returned when calling stored procedures, see [Stored procedure errors](db2-troubleshooting.md#db2-troubleshooting-stored-procedures "db2-troubleshooting.md#db2-troubleshooting-stored-procedures").

### Examples

**Example 1: Lowering the high water mark**

The following example alters a tablespace called `SP8` and assigns a
buffer pool called `BP8` for a database called `TESTDB` to
lower the high water mark.

```
db2 "call rdsadmin.alter_tablespace(
    'TESTDB',
    'SP8',
    'BP8',
    NULL,
    NULL,
    'Y')"
```

**Example 2: Reducing the high water mark**

The following example runs the `REDUCE MAX` command on a tablespace
called `TBSP_TEST` in the database `TESTDB`.

```
db2 "call rdsadmin.alter_tablespace(
    'TESTDB',
    'TBSP_TEST',
    NULL,
    NULL,
    NULL,
    'Y')"
```

**Example 3: Interrupting commands to reduce high water
mark**

The following example runs the `REDUCE STOP` command on a tablespace
called `TBSP_TEST` in the database `TESTDB`.

```
db2 "call rdsadmin.alter_tablespace(
    'TESTDB',
    'TBSP_TEST',
    NULL,
    NULL,
    NULL,
    NULL,
    'Y')"
```

**Example 4: Changing existing prefetch page size**

The following example runs the `ALTER TABLESPACE SWITCH ONLINE` command
on a tablespace called `TSBP_TEST` and changes the existing prefetch page
size to `64`.

```
db2 "call rdsadmin.alter_tablespace(
    'TESTDB',
    'TBSP_TEST',
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    ‘Y’,
    ‘64’)"
```

## rdsadmin.rename_tablespace

Renames a tablespace.

### Syntax

```
db2 "call rdsadmin.rename_tablespace(
    ?,
    '`database_name`',
    '`source_tablespace_name`',
    '`target_tablespace_name`')"
```

### Parameters

The following parameters are required:

?

A parameter marker that outputs an error message. This parameter only
accepts ?.

`database_name`

The name of the database that the tablespace belongs to. The data type
is `varchar`.

`source_tablespace_name`

The name of the tablespace to rename. The data type is
`varchar`.

`target_tablespace_name`

The new name of the tablespace. The data type is
`varchar`.

The new name has the following restrictions:

- It can't be the same as the name of an existing
  tablespace.
- It can only contain the characters
  `_$#@a-zA-Z0-9`.
- It can't start with `_` or `$`.
- It can't start with `SYS`.

### Usage notes

For information about checking the status of renaming a tablespace, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

You can't rename tablespaces that belong to the `rdsadmin`
database.

### Examples

The following example renames a tablespace called `SP8` to
`SP9` in a database called `TESTDB`.

```
db2 "call rdsadmin.rename_tablespace(
    ?,
    'TESTDB',
    'SP8',
    'SP9')"
```

## rdsadmin.drop_tablespace

Drops a tablespace.

### Syntax

```
db2 "call rdsadmin.drop_tablespace(
    '`database_name`',
    '`tablespace_name`')"
```

### Parameters

The following parameters are required:

`database_name`

The name of the database that the tablespace belongs to. The data type
is `varchar`.

`tablespace_name`

The name of the tablespace to drop. The data type is
`varchar`.

### Usage notes

For information about checking the status of dropping a tablespace, see [rdsadmin.get_task_status](db2-user-defined-functions.md#db2-udf-get-task-status "db2-user-defined-functions.md#db2-udf-get-task-status").

### Examples

The following example drops a tablespace called `SP8` from a database
called `TESTDB`.

```
db2 "call rdsadmin.drop_tablespace(
    'TESTDB',
    'SP8')"
```
