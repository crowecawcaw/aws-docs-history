# Known issues and limitations for Amazon RDS for MySQL

Known issues and limitations for working with Amazon RDS for MySQL are as follows.

###### Topics

- [InnoDB reserved word](#MySQL.Concepts.KnownIssuesAndLimitations.InnodbDatabaseName "#MySQL.Concepts.KnownIssuesAndLimitations.InnodbDatabaseName")
- [Storage-full behavior for Amazon RDS for MySQL](#MySQL.Concepts.StorageFullBehavior "#MySQL.Concepts.StorageFullBehavior")
- [Inconsistent InnoDB buffer pool size](#MySQL.Concepts.KnownIssuesAndLimitations.InnodbBufferPoolSize "#MySQL.Concepts.KnownIssuesAndLimitations.InnodbBufferPoolSize")
- [Index merge optimization returns incorrect results](#MySQL.Concepts.KnownIssuesAndLimitations.IndexMergeOptimization "#MySQL.Concepts.KnownIssuesAndLimitations.IndexMergeOptimization")
- [MySQL parameter exceptions for Amazon RDS DB instances](#MySQL.Concepts.ParameterNotes "#MySQL.Concepts.ParameterNotes")
- [MySQL file size limits in Amazon RDS](#MySQL.Concepts.Limits.FileSize "#MySQL.Concepts.Limits.FileSize")
- [MySQL Keyring Plugin not supported](#MySQL.Concepts.Limits.KeyRing "#MySQL.Concepts.Limits.KeyRing")
- [Custom ports](#MySQL.Concepts.KnownIssuesAndLimitations.CustomPorts "#MySQL.Concepts.KnownIssuesAndLimitations.CustomPorts")
- [MySQL stored procedure limitations](#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures "#MySQL.Concepts.KnownIssuesAndLimitations.KillProcedures")
- [GTID-based replication with an external source instance](#MySQL.Concepts.KnownIssuesAndLimitations.GTID "#MySQL.Concepts.KnownIssuesAndLimitations.GTID")
- [MySQL default authentication plugin](#MySQL.Concepts.KnownIssuesAndLimitations.authentication-plugin "#MySQL.Concepts.KnownIssuesAndLimitations.authentication-plugin")
- [Overriding innodb_buffer_pool_size](#MySQL.Concepts.KnownIssuesAndLimitations.innodb-bp-size "#MySQL.Concepts.KnownIssuesAndLimitations.innodb-bp-size")
- [Upgrading from MySQL 5.7 to MySQL 8.4](#MySQL.Concepts.KnownIssuesAndLimitations.upgrade-8-4 "#MySQL.Concepts.KnownIssuesAndLimitations.upgrade-8-4")
- [InnoDB page compression](#MySQL.Concepts.KnownIssuesAndLimitations.innodb-page-compression "#MySQL.Concepts.KnownIssuesAndLimitations.innodb-page-compression")

## InnoDB reserved word

`InnoDB` is a reserved word for RDS for MySQL. You can't use this name for a MySQL database.

## Storage-full behavior for Amazon RDS for MySQL

When storage becomes full for a MySQL DB instance, there can be metadata
inconsistencies, dictionary mismatches, and orphan tables. To prevent these issues,
Amazon RDS automatically stops a DB instance that reaches the `storage-full`
state.

A MySQL DB instance reaches the `storage-full` state in the following cases:

- The DB instance has less than 20,000 MiB of storage, and available storage reaches 200 MiB or less.
- The DB instance has more than 102,400 MiB of storage, and available storage reaches 1024 MiB or less.
- The DB instance has between 20,000 MiB and 102,400 MiB of storage, and has less than 1% of storage available.

After Amazon RDS stops a DB instance automatically because it reached the
`storage-full` state, you can still modify it. To restart the DB
instance, complete at least one of the following:

- Modify the DB instance to enable storage autoscaling.

For more information about storage autoscaling, see
[Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.md "USER_PIOPS.md").

- Modify the DB instance to increase its storage capacity.

For more information about increasing storage capacity, see
[Increasing DB instance storage capacity](USER_PIOPS.md "USER_PIOPS.md").

After you make one of these changes, the DB instance is restarted automatically. For information about
modifying a DB instance, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Inconsistent InnoDB buffer pool size

For MySQL 5.7, there is currently a bug in the way that the InnoDB buffer pool size is
managed. MySQL 5.7 might adjust the value of the `innodb_buffer_pool_size`
parameter to a large value that can result in the InnoDB buffer pool growing too large
and using up too much memory. This effect can cause the MySQL database engine to stop
running or can prevent it from starting. This issue is more common for DB instance
classes that have less memory available.

To resolve this issue, set the value of the
`innodb_buffer_pool_size` parameter to a multiple of the product
of the `innodb_buffer_pool_instances` parameter value and the
`innodb_buffer_pool_chunk_size` parameter value. For example, you
might set the `innodb_buffer_pool_size` parameter value to a multiple
of eight times the product of the `innodb_buffer_pool_instances` and
`innodb_buffer_pool_chunk_size` parameter values, as shown in the
following example.

```
innodb_buffer_pool_chunk_size = 536870912
innodb_buffer_pool_instances = 4
innodb_buffer_pool_size = (536870912 * 4) * 8 = 17179869184
```

For details on this MySQL 5.7 bug, see [https://bugs.mysql.com/bug.php?id=79379](https://bugs.mysql.com/bug.php?id=79379 "https://bugs.mysql.com/bug.php?id=79379") in the MySQL documentation.

## Index merge optimization returns incorrect results

Queries that use index merge optimization might return incorrect results because of a
bug in the MySQL query optimizer that was introduced in MySQL 5.5.37. When you issue a
query against a table with multiple indexes, the optimizer scans ranges of rows based on
the multiple indexes, but does not merge the results together correctly. For more
information on the query optimizer bug, see [http://bugs.mysql.com/bug.php?id=72745](https://bugs.mysql.com/bug.php?id=72745 "https://bugs.mysql.com/bug.php?id=72745") and [http://bugs.mysql.com/bug.php?id=68194](https://bugs.mysql.com/bug.php?id=68194 "https://bugs.mysql.com/bug.php?id=68194") in the MySQL bug database.

For example, consider a query on a table with two indexes where the search arguments reference the indexed columns.

```
SELECT * FROM table1
WHERE indexed_col1 = 'value1' AND indexed_col2 = 'value2';
```

In this case, the search engine will search both indexes. However, because of the bug,
the merged results are incorrect.

To resolve this issue, you can do one of the following:

- Set the `optimizer_switch` parameter to `index_merge=off` in the DB parameter
  group for your MySQL DB instance. For information on setting DB parameter group parameters, see
  [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
- Upgrade your MySQL DB instance to MySQL version 5.7 or 8.0.
  For more information, see
  [Upgrades of the RDS for MySQL DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
- If you cannot upgrade your instance or change the `optimizer_switch` parameter, you can work around the
  bug by explicitly identifying an index for the query, for example:

```
SELECT * FROM table1
USE INDEX covering_index
WHERE indexed_col1 = 'value1' AND indexed_col2 = 'value2';
```

For more information, see [Index
merge optimization](https://dev.mysql.com/doc/refman/8.0/en/index-merge-optimization.html "https://dev.mysql.com/doc/refman/8.0/en/index-merge-optimization.html") in the MySQL documentation.

## MySQL parameter exceptions for Amazon RDS DB instances

Some MySQL parameters require special considerations when used with an Amazon RDS DB instance.

### lower_case_table_names

Because Amazon RDS uses a case-sensitive file system, setting the value of the
`lower_case_table_names` server parameter to 2 (names stored as given
but compared in lowercase) is not supported. The following are the supported values
for Amazon RDS for MySQL DB instances:

- 0 (names stored as given and comparisons are case-sensitive) is supported
  for all RDS for MySQL versions.
- 1 (names stored in lowercase and comparisons are not case-sensitive) is
  supported for RDS for MySQL version 5.7, version 8.0.28 and higher 8.0
  versions, and version 8.4.

Set the `lower_case_table_names` parameter in a custom
DB parameter group before creating a DB instance. Then, specify the custom DB parameter
group when you create the DB instance.

When a parameter group is associated with a MySQL DB instance with a version lower
than 8.0, we recommend that you avoid changing the
`lower_case_table_names` parameter in the parameter group. Changing
it could cause inconsistencies with point-in-time recovery backups and read replica
DB instances.

When a parameter group is associated with a version 8.0 or 8.4 MySQL DB instance,
you can't modify the `lower_case_table_names` parameter in the
parameter group.

Read replicas should always use the same `lower_case_table_names`
parameter value as the source DB instance.

### long_query_time

You can set the `long_query_time` parameter to a floating point value
so that you can log slow queries to the MySQL slow query log with microsecond
resolution. You can set a value such as 0.1 seconds, which would be 100
milliseconds, to help when debugging slow transactions that take less than one
second.

## MySQL file size limits in Amazon RDS

For MySQL versions 8.0 and higher DB instances, the maximum file size is 16 TiB. When
using file-per-table tablespaces, the maximum file size limits the size of an InnoDB
table to 16 TiB. InnoDB file-per-table tablespaces (with tables each in their own
tablespace) is set by default for MySQL DB instances. For more
information, see [InnoDB Limits](https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-limits.html") in the MySQL documentation.

###### Note

Some existing DB instances have a lower limit. For example, MySQL DB instances
created before April 2014 have a file and table size limit of 2 TB. This 2 TB file
size limit also applies to DB instances or read replicas created from DB snapshots
taken before April 2014, regardless of when the DB instance was created.

There are advantages and disadvantages to using InnoDB file-per-table tablespaces,
depending on your application. To determine the best approach for your
application, see [File-per-table tablespaces](https://dev.mysql.com/doc/refman/8.0/en/innodb-file-per-table-tablespaces.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-file-per-table-tablespaces.html")
in the MySQL documentation.

We don't recommend allowing tables to grow to the maximum file size. In general, a better
practice is to partition data into smaller tables, which can improve performance and
recovery times.

One option that you can use for breaking up a large table into smaller tables is
partitioning. Partitioning distributes portions of your large table into separate files
based on rules that you specify. For example, if you store transactions by date, you can
create partitioning rules that distribute older transactions into separate files using
partitioning. Then periodically, you can archive the historical transaction data that
doesn't need to be readily available to your application. For more information, see
[Partitioning](https://dev.mysql.com/doc/refman/8.0/en/partitioning.html "https://dev.mysql.com/doc/refman/8.0/en/partitioning.html") in the MySQL documentation.

Because there is no single system table or view that provides the size of all the
tables and the InnoDB system tablespace, you must query multiple tables to determine the
size of the tablespaces.

###### To determine the size of the InnoDB system tablespace and the data dictionary tablespace

- Use the following SQL command to determine if any of your tablespaces are too
  large and are candidates for partitioning.

###### Note

The data dictionary tablespace is specific to MySQL 8.0 and higher
versions.

```
select FILE_NAME,TABLESPACE_NAME, ROUND(((TOTAL_EXTENTS*EXTENT_SIZE)
/1024/1024/1024), 2)  as "File Size (GB)" from information_schema.FILES
where tablespace_name in ('mysql','innodb_system');
```

###### To determine the size of InnoDB user tables outside of the InnoDB system tablespace (for MySQL 5.7 versions)

- Use the following SQL command to determine if any of your tables are too
  large and are candidates for partitioning.

```
SELECT SPACE,NAME,ROUND((ALLOCATED_SIZE/1024/1024/1024), 2)
as "Tablespace Size (GB)"
FROM information_schema.INNODB_SYS_TABLESPACES ORDER BY 3 DESC;
```

###### To determine the size of InnoDB user tables outside of the InnoDB system tablespace (for MySQL 8.0 and higher versions)

- Use the following SQL command to determine if any of your tables are too
  large and are candidates for partitioning.

```
SELECT SPACE,NAME,ROUND((ALLOCATED_SIZE/1024/1024/1024), 2)
as "Tablespace Size (GB)"
FROM information_schema.INNODB_TABLESPACES ORDER BY 3 DESC;
```

###### To determine the size of non-InnoDB user tables

- Use the following SQL command to determine if any of your non-InnoDB user
  tables are too large.

```
SELECT TABLE_SCHEMA, TABLE_NAME, round(((DATA_LENGTH + INDEX_LENGTH+DATA_FREE)
/ 1024 / 1024/ 1024), 2) As "Approximate size (GB)" FROM information_schema.TABLES
WHERE TABLE_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema')
and ENGINE<>'InnoDB';
```

###### To enable InnoDB file-per-table tablespaces

- Set the _innodb_file_per_table_ parameter to `1`
  in the parameter group for the DB instance.

###### To disable InnoDB file-per-table tablespaces

- Set the _innodb_file_per_table_ parameter to `0`
  in the parameter group for the DB instance.

For information on updating
a parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

When you have enabled or disabled InnoDB file-per-table tablespaces, you can issue an `ALTER
 TABLE` command to move a table from the global tablespace to its own
tablespace, or from its own tablespace to the global tablespace as shown in the
following example:

```
ALTER TABLE table_name TABLESPACE=innodb_file_per_table;
```

## MySQL Keyring Plugin not supported

Currently, Amazon RDS for MySQL doesn't support the MySQL `keyring_aws`
Amazon Web Services Keyring Plugin.

## Custom ports

Amazon RDS blocks connections to custom port 33060 for the MySQL engine. Choose a different port for your MySQL engine.

## MySQL stored procedure limitations

The [mysql.rds_kill](mysql-stored-proc-ending.md#mysql_rds_kill "mysql-stored-proc-ending.md#mysql_rds_kill") and [mysql.rds_kill_query](mysql-stored-proc-ending.md#mysql_rds_kill_query "mysql-stored-proc-ending.md#mysql_rds_kill_query") stored
procedures can't terminate sessions or queries owned by MySQL users with usernames
longer than 16 characters on the following RDS for MySQL versions:

- 8.0.32 and lower 8 versions
- 5.7.41 and lower 5.7 versions

## GTID-based replication with an external source instance

Amazon RDS supports replication based on global transaction identifiers (GTIDs) from an
external MySQL instance into an Amazon RDS for MySQL DB instance that requires setting
GTID_PURGED during configuration. However, only RDS for MySQL 8.0.37 and higher versions
support this functionality.

## MySQL default authentication plugin

RDS for MySQL version 8.0.34 and higher 8.0 versions use the
`mysql_native_password` plugin. You can't change the
`default_authentication_plugin` setting.

RDS for MySQL version 8.4 and higher versions use the `caching_sha2_password`
plugin as the default authentication plugin. You can change the default authentication
plugin for MySQL 8.4. The `mysql_native_password` plugin still works with
MySQL 8.4, but support of this plugin ends with MySQL 8.4. To change the default
authentication plugin, create a custom parameter group and modify the value of the
`authentication_policy` parameter. For more information, see [Default and custom parameter groups](parameter-groups-overview.md#parameter-groups-overview.custom "parameter-groups-overview.md#parameter-groups-overview.custom").

## Overriding innodb_buffer_pool_size

With micro or small DB instance classes, the default value for the
`innodb_buffer_pool_size` parameter might differ from the value returned
by running the following command:

```
mysql> SELECT @@innodb_buffer_pool_size;
```

This difference can occur when Amazon RDS needs to override the default value as part of
managing the DB instance classes. If necessary, you can override the default value and
set it to a value that your DB instance class supports. To determine a valid value,
add the memory usage and the total memory available on your DB instance. For more
information, see [Amazon RDS instance
types](https://aws.amazon.com/rds/instance-types/ "https://aws.amazon.com/rds/instance-types/").

If your DB instance has only 4 GB of memory, you can't set
`innodb_buffer_pool_size` to 8 GB but you might be able to set it to 3
GB, depending on how much memory you allocated for other parameters.

If the value that you input is too large, Amazon RDS lowers the value to the
following limits:

- Micro DB instance classes: 256 MB
- db.t4g.micro DB instance classes: 128 MB

## Upgrading from MySQL 5.7 to MySQL 8.4

You can't upgrade directly from MySQL 5.7 to MySQL 8.4. You must first upgrade from
MySQL 5.7 to MySQL 8.0, and then upgrade from MySQL 8.0 to MySQL 8.4. For more
information, see [Major version upgrades for RDS for MySQL](USER_UpgradeDBInstance.MySQL.md "USER_UpgradeDBInstance.MySQL.md").

## InnoDB page compression

InnoDB page compression doesn't work with Amazon RDS DB instances that have a file system
block size of 16k because the file system block size must be smaller than the InnoDB
page size. Starting in February 2024, all newly created DB instances have a file system
block size of 16k, which increases throughput and decreases IOPS consumption during page
flushes.
