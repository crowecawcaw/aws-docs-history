# Working with InnoDB tablespaces to improve crash recovery times for RDS for MySQL

Every table in MySQL consists of a table definition, data, and indexes. The MySQL
storage engine InnoDB stores table data and indexes in a
_tablespace_. InnoDB creates a global shared tablespace that contains
a data dictionary and other relevant metadata, and it can contain table data and
indexes. InnoDB can also create separate tablespaces for each table and partition. These
separate tablespaces are stored in files with a .ibd extension and the header of each
tablespace contains a number that uniquely identifies it.

Amazon RDS provides a parameter in a MySQL parameter group called
`innodb_file_per_table`. This parameters controls whether InnoDB adds new
table data and indexes to the shared tablespace (by setting the parameter value to 0) or
to individual tablespaces (by setting the parameter value to 1). Amazon RDS sets the default
value for `innodb_file_per_table` parameter to 1, which allows you to drop
individual InnoDB tables and reclaim storage used by those tables for the DB instance.
In most use cases, setting the `innodb_file_per_table` parameter to 1 is the
recommended setting.

You should set the `innodb_file_per_table` parameter to 0 when you have a
large number of tables, such as over 1000 tables when you use standard (magnetic) or
general purpose SSD storage or over 10,000 tables when you use Provisioned IOPS storage.
When you set this parameter to 0, individual tablespaces are not created and this can
improve the time it takes for database crash recovery.

MySQL processes each metadata file, which includes tablespaces, during the crash
recovery cycle. The time it takes MySQL to process the metadata information in the
shared tablespace is negligible compared to the time it takes to process thousands of
tablespace files when there are multiple tablespaces. Because the tablespace number is
stored within the header of each file, the aggregate time to read all the tablespace
files can take up to several hours. For example, a million InnoDB tablespaces on
standard storage can take from five to eight hours to process during a crash recovery
cycle. In some cases, InnoDB can determine that it needs additional cleanup after a
crash recovery cycle so it will begin another crash recovery cycle, which will extend
the recovery time. Keep in mind that a crash recovery cycle also entails rolling-back
transactions, fixing broken pages, and other operations in addition to the processing of
tablespace information.

Since the `innodb_file_per_table` parameter resides in a parameter group,
you can change the parameter value by editing the parameter group used by your DB
instance without having to reboot the DB instance. After the setting is changed, for
example, from 1 (create individual tables) to 0 (use shared tablespace), new InnoDB
tables will be added to the shared tablespace while existing tables continue to have
individual tablespaces. To move an InnoDB table to the shared tablespace, you must use
the `ALTER TABLE` command.

## Migrating multiple

tablespaces to the shared tablespace

You can move an InnoDB table's metadata from its own tablespace to the shared
tablespace, which will rebuild the table metadata according to the
`innodb_file_per_table` parameter setting. First connect to your
MySQL DB instance, then issue the appropriate commands as shown following. For more
information, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md").

```
ALTER TABLE `table_name` ENGINE = InnoDB, ALGORITHM=COPY;
```

For example, the following query returns an `ALTER TABLE` statement for
every InnoDB table that is not in the shared tablespace.

**For MySQL 5.7 DB instances:**

```
SELECT CONCAT('ALTER TABLE `',
REPLACE(LEFT(NAME , INSTR((NAME), '/') - 1), '`', '``'), '`.`',
REPLACE(SUBSTR(NAME FROM INSTR(NAME, '/') + 1), '`', '``'), '` ENGINE=InnoDB, ALGORITHM=COPY;') AS Query
FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES
WHERE SPACE <> 0 AND LEFT(NAME, INSTR((NAME), '/') - 1) NOT IN ('mysql','');
```

**For MySQL 8.4 and 8.0 DB instances:**

```
SELECT CONCAT('ALTER TABLE `',
REPLACE(LEFT(NAME , INSTR((NAME), '/') - 1), '`', '``'), '`.`',
REPLACE(SUBSTR(NAME FROM INSTR(NAME, '/') + 1), '`', '``'), '` ENGINE=InnoDB, ALGORITHM=COPY;') AS Query
FROM INFORMATION_SCHEMA.INNODB_TABLES
WHERE SPACE <> 0 AND LEFT(NAME, INSTR((NAME), '/') - 1) NOT IN ('mysql','');
```

Rebuilding a MySQL table to move the table's metadata to the shared tablespace
requires additional storage space temporarily to rebuild the table, so the DB
instance must have storage space available. During rebuilding, the table is locked
and inaccessible to queries. For small tables or tables not frequently accessed,
this might not be an issue. For large tables or tables frequently accessed in a
heavily concurrent environment, you can rebuild tables on a read replica.

You can create a read replica and migrate table metadata to the shared tablespace
on the read replica. While the ALTER TABLE statement blocks access on the read
replica, the source DB instance is not affected. The source DB instance will
continue to generate its binary logs while the read replica lags during the table
rebuilding process. Because the rebuilding requires additional storage space and the
replay log file can become large, you should create a read replica with storage
allocated that is larger than the source DB instance.

To create a read replica and rebuild InnoDB tables to use the shared tablespace,
take the following steps:

1. Make sure that backup retention is enabled on the source DB instance so
   that binary logging is enabled.
2. Use the AWS Management Console or AWS CLI to create a read replica for the source DB
   instance. Because the creation of a read replica involves many of the same
   processes as crash recovery, the creation process can take some time if
   there is a large number of InnoDB tablespaces. Allocate more storage space
   on the read replica than is currently used on the source DB instance.
3. When the read replica has been created, create a parameter group with the
   parameter settings `read_only = 0` and
   `innodb_file_per_table = 0`. Then associate the parameter
   group with the read replica.
4. Issue the following SQL statement for all tables that you want migrated on
   the replica:

```
ALTER TABLE `name` ENGINE = InnoDB
```

5. When all of your `ALTER TABLE` statements have completed on the
   read replica, verify that the read replica is connected to the source DB
   instance and that the two instances are in sync.
6. Use the console or CLI to promote the read replica to be the instance.
   Make sure that the parameter group used for the new standalone DB instance
   has the `innodb_file_per_table` parameter set to 0. Change the
   name of the new standalone DB instance, and point any applications to the
   new standalone DB instance.
