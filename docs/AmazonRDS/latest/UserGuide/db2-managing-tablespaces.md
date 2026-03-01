# Common tasks for tablespaces

You can create, alter, rename, or drop tablespaces for an RDS for Db2 database. Creating, altering,
renaming, or dropping tablespaces requires higher-level `SYSADM` authority, which isn't
available to the master user. Instead, use Amazon RDS stored procedures.

###### Topics

- [Creating a tablespace](#db2-creating-tablespace "#db2-creating-tablespace")
- [Altering a tablespace](#db2-altering-tablespace "#db2-altering-tablespace")
- [Renaming a tablespace](#db2-renaming-tablespace "#db2-renaming-tablespace")
- [Dropping a tablespace](#db2-dropping-tablespace "#db2-dropping-tablespace")
- [Checking the status of a tablespace](#db2-checking-tablespaces-procedure "#db2-checking-tablespaces-procedure")
- [Returning detailed information about tablespaces](#db2-tablespaces-info-db2pd "#db2-tablespaces-info-db2pd")
- [Listing the state and storage group for a tablespace](#db2-state-storage-group-tablespace-sql "#db2-state-storage-group-tablespace-sql")
- [Listing the tablespaces of a table](#db2-return-tablespaces-sql "#db2-return-tablespaces-sql")
- [Listing tablespace containers](#db2-listing-tablespace-containers "#db2-listing-tablespace-containers")

## Creating a tablespace

To create a tablespace for your RDS for Db2 database, call the
`rdsadmin.create_tablespace` stored procedure. For more information, see
[CREATE TABLESPACE statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-tablespace "https://www.ibm.com/docs/en/db2/11.5?topic=statements-create-tablespace") in the IBM Db2
documentation.

###### Important

To create a tablespace, you must have a buffer pool of the same page size to
associate with the tablespace. For more information, see [Common tasks for buffer pools](db2-managing-buffer-pools.md "db2-managing-buffer-pools.md").

###### To create a tablespace

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Create a tablespace by calling `rdsadmin.create_tablespace`. For
   more information, see [rdsadmin.create_tablespace](db2-sp-managing-tablespaces.md#db2-sp-create-tablespace "db2-sp-managing-tablespaces.md#db2-sp-create-tablespace").

```
db2 "call rdsadmin.create_tablespace(
    '`database_name`',
    '`tablespace_name`',
    '`buffer_pool_name`',
    `tablespace_initial_size`,
    `tablespace_increase_size`,
    '`tablespace_type`')"
```

## Altering a tablespace

To alter a tablespace for your RDS for Db2 database, call the
`rdsadmin.alter_tablespace` stored procedure. You can use this stored
procedure to change the buffer pool of a tablespace, lower the high water mark, or bring
a tablespace online. For more information, see [ALTER TABLESPACE statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-alter-tablespace "https://www.ibm.com/docs/en/db2/11.5?topic=statements-alter-tablespace") in the IBM Db2
documentation.

###### To alter a tablespace

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Alter a tablespace by calling `rdsadmin.alter_tablespace`. For
   more information, see [rdsadmin.alter_tablespace](db2-sp-managing-tablespaces.md#db2-sp-alter-tablespace "db2-sp-managing-tablespaces.md#db2-sp-alter-tablespace").

```
db2 "call rdsadmin.alter_tablespace(
    '`database_name`',
    '`tablespace_name`',
    '`buffer_pool_name`',
    `buffer_pool_size`,
    `tablespace_increase_size`,
    '`max_size`', '`reduce_max`',
    '`reduce_stop`',
    '`reduce_value`',
    '`lower_high_water`',
    '`lower_high_water_stop`',
    '`switch_online`')"
```

## Renaming a tablespace

To change the name of a tablespace for your RDS for Db2 database, call the
`rdsadmin.rename_tablespace` stored procedure. For more information, see
[RENAME TABLESPACE statement](https://www.ibm.com/docs/en/db2/11.5?topic=statements-rename-tablespace "https://www.ibm.com/docs/en/db2/11.5?topic=statements-rename-tablespace") in the IBM Db2
documentation.

###### To rename a tablespace

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Rename a tablespace by calling `rdsadmin.rename_tablespace`. For
   more information, including restrictions on what you can name a tablespace, see
   [rdsadmin.rename_tablespace](db2-sp-managing-tablespaces.md#db2-sp-rename-tablespace "db2-sp-managing-tablespaces.md#db2-sp-rename-tablespace").

```
db2 "call rdsadmin.rename_tablespace(
    '`database_name`',
    '`source_tablespace_name`',
    '`target_tablespace_name`')"
```

## Dropping a tablespace

To drop a tablespace for your RDS for Db2 database, call the
`rdsadmin.drop_tablespace` stored procedure. Before you drop a
tablespace, first drop any objects in the tablespace such as tables, indexes, or large
objects (LOBs). For more information, see [Dropping
table spaces](https://www.ibm.com/docs/en/db2/11.5?topic=spaces-dropping-table "https://www.ibm.com/docs/en/db2/11.5?topic=spaces-dropping-table") in the IBM Db2 documentation.

###### To drop a tablespace

1. Connect to the `rdsadmin` database using the master username and
   master password for your RDS for Db2 DB instance. In the following example, replace
   `master_username` and
   `master_password` with your own information.

```
db2 "connect to rdsadmin user `master_username` using `master_password`"
```

2. Drop a tablespace by calling `rdsadmin.drop_tablespace`. For
   more information, see [rdsadmin.drop_tablespace](db2-sp-managing-tablespaces.md#db2-sp-drop-tablespace "db2-sp-managing-tablespaces.md#db2-sp-drop-tablespace").

```
db2 "call rdsadmin.drop_tablespace(
    '`database_name`',
    '`tablespace_name`')"
```

## Checking the status of a tablespace

You can check the status of a tablespace by using the `cast`
function.

###### To check the status of a tablespace

1. Connect to your Db2 database using the master username and master password for
   your RDS for Db2 DB instance. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with your own information.

```
db2 connect to `rds_database_alias` user `master_username` using `master_password`
```

2. Return a summary output.

For a summary output:

```
db2 "select cast(tbsp_id as smallint) as tbsp_id,
cast(tbsp_name as varchar(35)) as tbsp_name,
cast(tbsp_type as varchar(3)) as tbsp_type,
cast(tbsp_state as varchar(10)) as state,
cast(tbsp_content_type as varchar(8)) as contents from table(mon_get_tablespace(null,-1)) order by tbsp_id"
```

## Returning detailed information about tablespaces

You can return information about a tablespace for one member or all members by using
the `cast` function.

###### To return detailed information about tablespaces

1. Connect to your Db2 database using the master username and master password for
   your RDS for Db2 DB instance. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with your own information.

```
db2 connect to `rds_database_alias` user `master_username` using `master_password`
```

2. Return details about all tablespaces in the database for one member or for
   all members.

For one member:

```
db2 "select cast(member as smallint) as member,
cast(tbsp_id as smallint) as tbsp_id,
cast(tbsp_name as varchar(35)) as tbsp_name,
cast(tbsp_type as varchar(3)) as tbsp_type,
cast(tbsp_state as varchar(10)) as state,
cast(tbsp_content_type as varchar(8)) as contents,
cast(tbsp_total_pages as integer) as total_pages,
cast(tbsp_used_pages as integer) as used_pages,
cast(tbsp_free_pages as integer) as free_pages,
cast(tbsp_page_top as integer) as page_hwm,
cast(tbsp_page_size as integer) as page_sz,
cast(tbsp_extent_size as smallint) as extent_sz,
cast(tbsp_prefetch_size as smallint) as prefetch_sz,
cast(tbsp_initial_size as integer) as initial_size,
cast(tbsp_increase_size_percent as smallint) as increase_pct,
cast(storage_group_name as varchar(12)) as stogroup from table(mon_get_tablespace(null,-1)) order by member, tbsp_id "
```

For all members:

```
db2 "select cast(member as smallint) as member
cast(tbsp_id as smallint) as tbsp_id,
cast(tbsp_name as varchar(35)) as tbsp_name,
cast(tbsp_type as varchar(3)) as tbsp_type,
cast(tbsp_state as varchar(10)) as state,
cast(tbsp_content_type as varchar(8)) as contents,
cast(tbsp_total_pages as integer) as total_pages,
cast(tbsp_used_pages as integer) as used_pages,
cast(tbsp_free_pages as integer) as free_pages,
cast(tbsp_page_top as integer) as page_hwm,
cast(tbsp_page_size as integer) as page_sz,
cast(tbsp_extent_size as smallint) as extent_sz,
cast(tbsp_prefetch_size as smallint) as prefetch_sz,
cast(tbsp_initial_size as integer) as initial_size,
cast(tbsp_increase_size_percent as smallint) as increase_pct,
cast(storage_group_name as varchar(12)) as stogroup from table(mon_get_tablespace(null,-2)) order by member, tbsp_id "
```

## Listing the state and storage group for a tablespace

You can list the state and storage group for a tablespace by running a SQL
statement.

To list the state and storage group for a tablespace, run the following SQL
statement:

```
db2 "SELECT varchar(tbsp_name, 30) as tbsp_name,
                  varchar(TBSP_STATE, 30) state,
                  tbsp_type,
                  varchar(storage_group_name,30) storage_group
FROM TABLE(MON_GET_TABLESPACE('',-2)) AS t"
```

## Listing the tablespaces of a table

You can list the tablespaces for a table by running a SQL statement.

To list the tablespaces of a table, run the following SQL statement. In the following
example, replace `SCHEMA_NAME` and
`TABLE_NAME` with the names of your schema and
table:

```
db2 "SELECT
   VARCHAR(SD.TBSPACE,30) AS DATA_SPACE,
   VARCHAR(SL.TBSPACE,30) AS LONG_SPACE,
   VARCHAR(SI.TBSPACE,30) AS INDEX_SPACE
 FROM
   SYSCAT.DATAPARTITIONS P
   JOIN SYSCAT.TABLESPACES SD ON SD.TBSPACEID = P.TBSPACEID
   LEFT JOIN SYSCAT.TABLESPACES SL ON SL.TBSPACEID = P.LONG_TBSPACEID
   LEFT JOIN SYSCAT.TABLESPACES SI ON SI.TBSPACEID = P.INDEX_TBSPACEID
 WHERE
    TABSCHEMA = '`SCHEMA_NAME`'
 AND TABNAME   = '`TABLE_NAME`'"
```

## Listing tablespace containers

You can list all tablespace containers or specific tablespace containers by using the
`cast` command.

###### To list the tablespace containers for a tablespace

1. Connect to your Db2 database using the master username and master password for
   your RDS for Db2 DB instance. In the following example, replace
   `rds_database_alias`,
   `master_username`, and
   `master_password` with your own information:

```
db2 connect to `rds_database_alias` user `master_username` using `master_password`
```

2. Return a list of all tablespace containers in the database or specific
   tablespace containers.

For all tablespace containers:

```
db2 "select cast(member as smallint) as member,
cast(tbsp_name as varchar(35)) as tbsp_name,
cast(container_id as smallint) as id,
cast(container_name as varchar(60)) as container_path, container_type as type from table(mon_get_container(null,-2)) order by member,tbsp_id,container_id"
```

For specific tablespace containers:

```
db2 "select cast(member as smallint) as member,
cast(tbsp_name as varchar(35)) as tbsp_name,
cast(container_id as smallint) as id,
cast(container_name as varchar(60)) as container_path, container_type as type from table(mon_get_container('TBSP_1',-2)) order by member, tbsp_id,container_id"
```
