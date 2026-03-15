# Supported storage engines for MariaDB on Amazon RDS

RDS for MariaDB supports the following storage engines.

###### Topics

- [The InnoDB storage engine](#MariaDB.Concepts.Storage.InnoDB "#MariaDB.Concepts.Storage.InnoDB")
- [The MyRocks storage engine](#MariaDB.Concepts.Storage.MyRocks "#MariaDB.Concepts.Storage.MyRocks")
  Other storage engines aren't currently supported by RDS for MariaDB.

## The InnoDB storage engine

Although MariaDB supports multiple storage engines with varying capabilities,
not all of them are optimized for recovery and data durability. InnoDB is the
recommended storage engine for MariaDB DB instances on Amazon RDS. Amazon RDS features such as
point-in-time restore and snapshot restore require a recoverable storage engine and
are supported only for the recommended storage engine for the MariaDB
version.

For more information, see [InnoDB](https://mariadb.com/kb/en/innodb/ "https://mariadb.com/kb/en/innodb/").

## The MyRocks storage engine

The MyRocks storage engine is available in RDS for MariaDB version 10.6 and higher. Before using the MyRocks
storage engine in a production database, we recommend that you perform thorough benchmarking and testing to
verify any potential benefits over InnoDB for your use case.

The default parameter group for MariaDB version 10.6 includes MyRocks parameters. For more information,
see [Parameters for MariaDB](Appendix.MariaDB.md "Appendix.MariaDB.md") and
[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

To create a table that uses the MyRocks storage engine, specify
`ENGINE=RocksDB` in the `CREATE TABLE` statement. The
following example creates a table that uses the MyRocks storage engine.

```
CREATE TABLE test (a INT NOT NULL, b CHAR(10)) ENGINE=RocksDB;
```

We strongly recommend that you don't run transactions that span both InnoDB
and MyRocks tables. MariaDB doesn't guarantee ACID (atomicity, consistency,
isolation, durability) for transactions across storage engines. Although it is
possible to have both InnoDB and MyRocks tables in a DB instance, we don't recommend
this approach except during a migration from one storage engine to the other. When
both InnoDB and MyRocks tables exist in a DB instance, each storage engine has its
own buffer pool, which might cause performance to degrade.

MyRocks doesn’t support `SERIALIZABLE` isolation or gap locks. So, generally you can't use MyRocks with
statement-based replication. For more information, see [MyRocks and Replication](https://mariadb.com/kb/en/myrocks-and-replication/ "https://mariadb.com/kb/en/myrocks-and-replication/").

Currently, you can modify only the following MyRocks parameters:

- [`rocksdb_block_cache_size`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_block_cache_size "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_block_cache_size")
- [`rocksdb_bulk_load`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_bulk_load "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_bulk_load")
- [`rocksdb_bulk_load_size`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_bulk_load_size "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_bulk_load_size")
- [`rocksdb_deadlock_detect`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_deadlock_detect "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_deadlock_detect")
- [`rocksdb_deadlock_detect_depth`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_deadlock_detect_depth "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_deadlock_detect_depth")
- [`rocksdb_max_latest_deadlocks`](https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_max_latest_deadlocks "https://mariadb.com/kb/en/myrocks-system-variables/#rocksdb_max_latest_deadlocks")

The MyRocks storage engine and the InnoDB storage engine can compete for
memory based on the settings for the `rocksdb_block_cache_size` and
`innodb_buffer_pool_size` parameters. In some cases, you might only
intend to use the MyRocks storage engine on a particular DB instance. If so, we
recommend setting the `innodb_buffer_pool_size minimal` parameter to a
minimal value and setting the `rocksdb_block_cache_size` as high as
possible.

You can access MyRocks log files by using the [`DescribeDBLogFiles`](../APIReference/API_DescribeDBLogFiles.md "../APIReference/API_DescribeDBLogFiles.md") and [`DownloadDBLogFilePortion`](../APIReference/API_DownloadDBLogFilePortion.md "../APIReference/API_DownloadDBLogFilePortion.md") operations.

For more information about MyRocks, see [MyRocks](https://mariadb.com/kb/en/myrocks/ "https://mariadb.com/kb/en/myrocks/")
on the MariaDB website.
