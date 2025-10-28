# MySQL feature support on Amazon RDS

RDS for MySQL supports most of the features and capabilities of MySQL. Some features might have
limited support or restricted privileges.

You can filter new Amazon RDS features on the [What's
New with Database?](https://aws.amazon.com/about-aws/whats-new/database/ "https://aws.amazon.com/about-aws/whats-new/database/") page. For **Products**, choose **Amazon
RDS**. Then search using keywords such as `MySQL 2022`.

###### Note

The following lists are not exhaustive.

###### Topics

- [MySQL feature support on Amazon RDS for MySQL major versions](#MySQL.Concepts.FeatureSupport.MajorVersions "#MySQL.Concepts.FeatureSupport.MajorVersions")
- [Supported storage engines for RDS for MySQL](#MySQL.Concepts.Storage "#MySQL.Concepts.Storage")
- [Using memcached and other options with MySQL on Amazon RDS](#MySQL.Concepts.General.Options "#MySQL.Concepts.General.Options")
- [InnoDB cache warming for MySQL on Amazon RDS](#MySQL.Concepts.InnoDBCacheWarming "#MySQL.Concepts.InnoDBCacheWarming")
- [Inclusive language changes for
  RDS for MySQL 8.4](#mysql-8-4-inclusive-language-changes "#mysql-8-4-inclusive-language-changes")
- [MySQL features not supported by Amazon RDS](#MySQL.Concepts.Features "#MySQL.Concepts.Features")

## MySQL feature support on Amazon RDS for MySQL major versions

In the following sections, find information about MySQL feature support on Amazon RDS for
MySQL major versions:

###### Topics

- [MySQL 8.4 support on Amazon RDS](#MySQL.Concepts.FeatureSupport.8-4 "#MySQL.Concepts.FeatureSupport.8-4")

For information about supported minor versions of Amazon RDS for MySQL, see [Supported MySQL minor versions on
Amazon RDS](MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.Supported "MySQL.Concepts.md#MySQL.Concepts.VersionMgmt.Supported").

### MySQL 8.4 support on Amazon RDS

Amazon RDS supports the following new features for your DB instances running MySQL
version 8.4 or higher.

- **Cryptographic library** – RDS for MySQL
  replaced OpenSSL with AWS Libcrypto (AWS-LC), which is FIPS 140-3
  certified. For more information, see the AWS-LC GitHub repository at
  [https://github.com/aws/aws-lc](https://github.com/aws/aws-lc "https://github.com/aws/aws-lc").
- **TLS changes** – RDS for MySQL only
  supports TLS 1.2 and TLS 1.3. For more information, see [SSL/TLS support for MySQL DB instances on
  Amazon RDS](MySQL.Concepts.md "MySQL.Concepts.md").
- **memcached support** – The memcached
  interface is no longer available on MySQL 8.4. For more information, see
  [MySQL memcached support](Appendix.MySQL.Options.md "Appendix.MySQL.Options.md").
- **Default authentication plugin** –
  The default authentication plugin is `caching_sha2_password`. For
  more information, see [MySQL
  default authentication plugin](MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.authentication-plugin "MySQL.md#MySQL.Concepts.KnownIssuesAndLimitations.authentication-plugin").
- **`mysqlpump` client utility**
  – The `mysqlpump` client utility is no longer available in
  MySQL 8.4. For more information, see [Role-based privilege model for RDS for MySQL](Appendix.MySQL.CommonDBATasks.md "Appendix.MySQL.CommonDBATasks.md") and
  [mysqldump and mysqlpump](../../../prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mysqldump-and-mysqlpump.md "../../../prescriptive-guidance/latest/migration-large-mysql-mariadb-databases/mysqldump-and-mysqlpump.md") in the _AWS
  Prescriptive Guidance_.
- **Managed replication stored procedures**
  – When using stored procedures to manage replication with a
  replication user configured with `caching_sha2_password`, you
  must configure TLS by specifying `SOURCE_SSL=1`.
  `caching_sha2_password` is the default authentication plugin
  for RDS for MySQL 8.4.
- **Parameter behavior changes** – The
  following parameters changed for MySQL 8.4.
  - `innodb_dedicated_server` – This parameter is
    now enabled by default. For more information, see [Configuring buffer pool
    size and redo log capacity in MySQL 8.4](Appendix.MySQL.CommonDBATasks.Config.Size.8.md "Appendix.MySQL.CommonDBATasks.Config.Size.8.md").
  - `innodb_buffer_pool` – The database engine now
    calculates this parameter, but you can override this setting. For
    more information, see [Configuring buffer pool
    size and redo log capacity in MySQL 8.4](Appendix.MySQL.CommonDBATasks.Config.Size.8.md "Appendix.MySQL.CommonDBATasks.Config.Size.8.md").
  - `innodb_redo_log_capacity` – This parameter now
    controls the size of the redo log files. The database engine now
    calculates this parameter, but you can override this setting. For
    more information, see [Configuring buffer pool
    size and redo log capacity in MySQL 8.4](Appendix.MySQL.CommonDBATasks.Config.Size.8.md "Appendix.MySQL.CommonDBATasks.Config.Size.8.md").

- **Deprecated or removed parameters** –
  RDS for MySQL removed the following parameters from parameter groups for MySQL
  8.4 DB instances. The `innodb_redo_log_capacity` parameter now
  controls the size of the redo log files.
  - `innodb_log_file_size`
  - `innodb_log_files_in_group`

- **New default values for parameters**
  – The following parameters have new default values for MySQL 8.4 DB
  instances:
  - Various MySQL community parameters related to performance changed.
    For more information, see [What is New in MySQL 8.4 since MySQL 8.0](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html").

  We recommend that you test your application's performance on
  RDS for MySQL 8.4 before migrating a production instance.
  - `innodb_purge_threads` – The default value is
    set to the formula `LEAST({DBInstanceVCPU/2},4)` to
    prevent the InnoDB history list length from growing too large.
  - `group_replication_exit_state_action` – The
    default value is `OFFLINE_MODE`, which aligns with the
    default in MySQL Community. For more information, see
    [Considerations and
    best practices for RDS for MySQL active-active clusters](mysql-active-active-clusters-considerations-limitations.md#mysql-active-active-clusters-considerations "mysql-active-active-clusters-considerations-limitations.md#mysql-active-active-clusters-considerations").
  - `binlog_format` – The default value is
    `ROW`, which aligns with the default in MySQL
    Community. You can modify the parameter for Single-AZ DB instances
    or Multi-AZ DB instances, but not for Multi-AZ DB clusters. Multi-AZ
    DB clusters use semisynchronous replication, and when
    `binlog_format` is set to `MIXED` or
    `STATEMENT`, replication fails.

- **Inclusive language changes** –
  RDS for MySQL 8.4 includes changes from RDS for MySQL 8.0 related to keywords and
  system schemas for inclusive language. For more information, see [Inclusive language changes for
  RDS for MySQL 8.4](#mysql-8-4-inclusive-language-changes "#mysql-8-4-inclusive-language-changes").

For a list of all MySQL 8.4 features and changes, see [What Is New in
MySQL 8.4 since MySQL 8.0](https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html "https://dev.mysql.com/doc/refman/8.4/en/mysql-nutshell.html") in the MySQL documentation.

For a list of unsupported features, see [MySQL features not supported by Amazon RDS](#MySQL.Concepts.Features "#MySQL.Concepts.Features").

## Supported storage engines for RDS for MySQL

While MySQL supports multiple storage engines with varying capabilities, not all
of them are optimized for recovery and data durability. Amazon RDS fully supports
the InnoDB storage engine for MySQL DB instances. Amazon RDS features such as
Point-In-Time restore and snapshot restore require a recoverable storage engine and
are supported for the InnoDB storage engine only. For more
information, see [MySQL memcached support](Appendix.MySQL.Options.md "Appendix.MySQL.Options.md").

The Federated Storage Engine is currently not supported by Amazon RDS for
MySQL.

For user-created schemas, the MyISAM storage engine does not support reliable recovery and can result in
lost or corrupt data when MySQL is restarted after a recovery, preventing
Point-In-Time restore or snapshot restore from working as intended. However, if you
still choose to use MyISAM with Amazon RDS, snapshots can be helpful under some
conditions.

###### Note

System tables in the `mysql` schema can be in MyISAM storage.

If you want to convert existing MyISAM tables to InnoDB tables, you can use the
`ALTER TABLE` command (for example, `alter table TABLE_NAME engine=innodb;`). Bear in
mind that MyISAM and InnoDB have different strengths and weaknesses, so you should
fully evaluate the impact of making this switch on your applications before doing
so.

MySQL 5.1, 5.5, and 5.6 are no longer supported in Amazon RDS. However, you can restore existing MySQL 5.1, 5.5, and 5.6 snapshots.
When you restore a MySQL 5.1, 5.5, or 5.6 snapshot, the DB instance is automatically upgraded to MySQL 5.7.

## Using memcached and other options with MySQL on Amazon RDS

Most Amazon RDS DB engines support option groups that allow you to select
additional features for your DB instance. RDS for MySQL DB instances support the `memcached` option,
a simple, key-based cache. For more information about `memcached` and other options, see
[Options for MySQL DB instances](Appendix.MySQL.md "Appendix.MySQL.md").
For more information about working with option groups, see
[Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

## InnoDB cache warming for MySQL on Amazon RDS

InnoDB cache warming can provide performance gains for your MySQL DB instance by
saving the current state of the buffer pool when the DB instance is shut down, and then
reloading the buffer pool from the saved information when the DB instance starts up.
This bypasses the need for the buffer pool to "warm up" from normal database use and
instead preloads the buffer pool with the pages for known common queries. The file that
stores the saved buffer pool information only stores metadata for the pages that are in
the buffer pool, and not the pages themselves. As a result, the file does not require
much storage space. The file size is about 0.2 percent of the cache size. For example,
for a 64 GiB cache, the cache warming file size is 128 MiB. For more information on
InnoDB cache warming, see [Saving
and restoring the buffer pool state](https://dev.mysql.com/doc/refman/8.0/en/innodb-preload-buffer-pool.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-preload-buffer-pool.html") in the MySQL documentation.

RDS for MySQL DB instances support InnoDB cache warming. To enable InnoDB cache warming,
set the `innodb_buffer_pool_dump_at_shutdown` and `innodb_buffer_pool_load_at_startup`
parameters to 1 in the parameter group for your DB instance. Changing these parameter values in a parameter group will
affect all MySQL DB instances that use that parameter group. To enable InnoDB cache warming for specific MySQL DB
instances, you might need to create a new parameter group for those instances. For information on parameter groups, see
[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

InnoDB cache warming primarily provides a performance benefit for DB instances that use standard storage. If
you use PIOPS storage, you do not commonly see a significant performance benefit.

###### Important

If your MySQL DB instance does not shut down normally, such as during a failover, then the buffer pool state
will not be saved to disk. In this case, MySQL loads whatever buffer pool file is available when the DB instance
is restarted. No harm is done, but the restored buffer pool might not reflect the most recent state
of the buffer pool prior to the restart. To ensure that you have a recent state of the buffer pool available to
warm the InnoDB cache on startup, we recommend that you periodically dump the buffer pool "on demand."

You can create an event to dump the buffer pool automatically and on a regular
interval. For example, the following statement creates an event named
`periodic_buffer_pool_dump` that dumps the buffer pool every hour.

```
CREATE EVENT periodic_buffer_pool_dump
ON SCHEDULE EVERY 1 HOUR
DO CALL mysql.rds_innodb_buffer_pool_dump_now();
```

For more information on MySQL events, see [Event
syntax](https://dev.mysql.com/doc/refman/8.0/en/events-syntax.html "https://dev.mysql.com/doc/refman/8.0/en/events-syntax.html") in the MySQL documentation.

### Dumping and loading the buffer pool on demand

You can save and load the InnoDB cache "on demand."

- To dump the current state of the buffer pool to disk, call the
  [mysql.rds_innodb_buffer_pool_dump_now](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_dump_now "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_dump_now")
  stored procedure.
- To load the saved state of the buffer pool from disk, call the
  [mysql.rds_innodb_buffer_pool_load_now](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_now "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_now")
  stored procedure.
- To cancel a load operation in progress, call the
  [mysql.rds_innodb_buffer_pool_load_abort](mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_abort "mysql-stored-proc-warming.md#mysql_rds_innodb_buffer_pool_load_abort")
  stored procedure.

## Inclusive language changes for

RDS for MySQL 8.4

RDS for MySQL 8.4 includes changes from the MySQL 8.4 community edition related to
keywords and system schemas for inclusive language. For example, the `SHOW REPLICA
 STATUS` command replaces `SHOW SLAVE STATUS`.

###### Topics

- [Configuration parameter
  name changes](#mysql-8-4-inclusive-language-changes-params "#mysql-8-4-inclusive-language-changes-params")
- [Stored procedure
  name changes](#mysql-8-4-inclusive-language-changes-sp "#mysql-8-4-inclusive-language-changes-sp")

### Configuration parameter

name changes

The following configuration parameters have new names in RDS for MySQL 8.4.

For compatibility, you can check the parameter names in the `mysql` client
by using either name. You can only use the new names when modifying values in a custom
MySQL 8.4 parameter group. For more information, see [Default and custom parameter
groups](parameter-groups-overview.md#parameter-groups-overview.custom "parameter-groups-overview.md#parameter-groups-overview.custom").

| Name to be removed                                 | New or preferred name                              |
| -------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `init_slave`                                       | `init_replica`                                     |
| `log_slave_updates`                                | `log_replica_updates`                              |
| `log_slow_slave_statements`                        | `log_slow_replica_statements`                      |
| `rpl_stop_slave_timeout`                           | `rpl_stop_replica_timeout`                         |
| `skip_slave_start`                                 | `skip_replica_start`                               |
| `slave_checkpoint_group`                           | `replica_checkpoint_group`                         |
| `slave_checkpoint_period`                          | `replica_checkpoint_period`                        |
| `slave_compressed_protocol`                        | `replica_compressed_protocol`                      |
| `slave_exec_mode`                                  | `replica_exec_mode`                                |
| `slave_load_tmpdir`                                | `replica_load_tmpdir`                              |
| `slave_max_allowed_packet`                         | `replica_max_allowed_packet`                       |
| `slave_net_timeout`                                | `replica_net_timeout`                              |
| `slave_parallel_type`                              | `replica_parallel_type`                            |
| `slave_parallel_workers`                           | `replica_parallel_workers`                         |
| `slave_pending_jobs_size_max`                      | `replica_pending_jobs_size_max`                    |
| `slave_preserve_commit_order`                      | `replica_preserve_commit_order`                    |
| `slave_skip_errors`                                | `replica_skip_errors`                              |
| `slave_sql_verify_checksum`                        | `replica_sql_verify_checksum`                      |
| `slave_transaction_retries`                        | `replica_transaction_retries`                      |
| `slave_type_conversions`                           | `replica_type_conversions`                         |
| `sql_slave_skip_counter`                           | `sql_replica_skip_counter`                         | ###### Note The parameter `replica_allow_batching` isn't available because Amazon RDS doesn't support NDB clusters. ### Stored procedure name changes The following stored procedures have new names in RDS for MySQL 8.4. For compatibility, you can use either name in the initial RDS for MySQL 8.4 release. The old procedure names are to be removed in a future release. For more information, see [Configuring, starting, and stopping binary log (binlog) replication](mysql-stored-proc-replicating.md "mysql-stored-proc-replicating.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Name to be removed                                 | New or preferred name                              |
| ---                                                | ---                                                |
| `mysql.rds_next_master_log`                        | `mysql.rds_next_source_log`                        |
| `mysql.rds_reset_external_master`                  | `mysql.rds_reset_external_source`                  |
| `mysql.rds_set_external_master`                    | `mysql.rds_set_external_source`                    |
| `mysql.rds_set_external_master_with_auto_position` | `mysql.rds_set_external_source_with_auto_position` |
| `mysql.rds_set_external_master_with_delay`         | `mysql.rds_set_external_source_with_delay`         |
| `mysql.rds_set_master_auto_position`               | `mysql.rds_set_source_auto_position`               | ## MySQL features not supported by Amazon RDS Amazon RDS doesn't currently support the following MySQL features: <br>• Authentication Plugin <br>• Error Logging to the System Log <br>• InnoDB Tablespace Encryption <br>• NDB clusters <br>• Password Strength Plugin <br>• Persisted system variables <br>• Rewriter Query Rewrite Plugin <br>• Semisynchronous replication, except for Multi-AZ DB clusters <br>• Transportable tablespace <br>• X Plugin To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. It also restricts access to certain system procedures and tables that require advanced privileges. Amazon RDS supports access to databases on a DB instance using any standard SQL client application. Amazon RDS doesn't allow direct host access to a DB instance by using Telnet, Secure Shell (SSH), or Windows Remote Desktop Connection. When you create a DB instance, you are assigned as _db_owner_ for all databases on that instance, and you have all database-level permissions except for those used for backups. Amazon RDS manages backups for you. |
