# Known issues and limitations for RDS for MariaDB

The following items are known issues and limitations when using RDS for MariaDB.

###### Note

This list is not exhaustive.

###### Topics

- [MariaDB file size limits in Amazon RDS](#RDS_Limits.FileSize.MariaDB "#RDS_Limits.FileSize.MariaDB")
- [InnoDB reserved word](#MariaDB.Concepts.InnodbDatabaseName "#MariaDB.Concepts.InnodbDatabaseName")
- [Custom ports](#MariaDB.Concepts.CustomPorts "#MariaDB.Concepts.CustomPorts")
- [Performance Insights](#MariaDB.Concepts.PerformanceInsights "#MariaDB.Concepts.PerformanceInsights")

## MariaDB file size limits in Amazon RDS

For MariaDB DB instances, the maximum size of a table is 16 TB when using InnoDB
file-per-table tablespaces. This limit also constrains the system tablespace to a
maximum size of 16 TB. InnoDB file-per-table tablespaces (with tables each in their own
tablespace) are set by default for MariaDB DB instances. This limit isn't related to the
maximum storage limit for MariaDB DB instances. For more information about the storage
limit, see [Amazon RDS DB instance storage](CHAP_Storage.md "CHAP_Storage.md").

There are advantages and disadvantages to using InnoDB file-per-table tablespaces,
depending on your application. To determine the best approach for your application, see
[File-per-table tablespaces](https://dev.mysql.com/doc/refman/5.7/en/innodb-file-per-table-tablespaces.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-file-per-table-tablespaces.html") in the MySQL documentation.

We don't recommend allowing tables to grow to the maximum file size. In general, a
better practice is to partition data into smaller tables, which can improve performance
and recovery times.

One option that you can use for breaking up a large table into smaller tables is
partitioning. _Partitioning_ distributes portions of
your large table into separate files based on rules that you specify. For example, if
you store transactions by date, you can create partitioning rules that distribute older
transactions into separate files using partitioning. Then periodically, you can archive
the historical transaction data that doesn't need to be readily available to your
application. For more information, see [Partitioning](https://dev.mysql.com/doc/refman/5.7/en/partitioning.html "https://dev.mysql.com/doc/refman/5.7/en/partitioning.html")
in the MySQL documentation.

###### To determine the size of all InnoDB tablespaces

- Use the following SQL command to determine if any of your tables are too large
  and are candidates for partitioning.

###### Note

For MariaDB 10.6 and higher, this query also returns the size of the
InnoDB system tablespace.

For MariaDB versions earlier than 10.6, you can't determine the size of
the InnoDB system tablespace by querying the system tables. We recommend
that you upgrade to a later version.

```
SELECT SPACE,NAME,ROUND((ALLOCATED_SIZE/1024/1024/1024), 2)
as "Tablespace Size (GB)"
FROM information_schema.INNODB_SYS_TABLESPACES ORDER BY 3 DESC;
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

To enable InnoDB file-per-table tablespaces

- Set the `innodb_file_per_table` parameter to `1` in the parameter group
  for the DB instance.

To disable InnoDB file-per-table tablespaces

- Set the `innodb_file_per_table` parameter to `0` in the parameter group
  for the DB instance.

For information on updating
a parameter group, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

When you have enabled or disabled InnoDB file-per-table tablespaces, you can issue an
`ALTER TABLE` command. You can use this command to move a table from the
global tablespace to its own tablespace. Or you can move a table from its own tablespace
to the global tablespace. Following is an example.

```
ALTER TABLE table_name ENGINE=InnoDB, ALGORITHM=COPY;
```

## InnoDB reserved word

`InnoDB` is a reserved word for RDS for MariaDB. You can't use this name for a MariaDB database.

## Custom ports

Amazon RDS blocks connections to custom port 33060 for the MariaDB engine. Choose a different port for your MariaDB engine.

## Performance Insights

InnoDB counters are not visible in Performance Insights for RDS for MariaDB version 10.11
because the MariaDB community no longer supports them.
