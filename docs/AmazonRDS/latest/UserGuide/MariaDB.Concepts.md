# MariaDB feature support on Amazon RDS

RDS for MariaDB supports most of the features and capabilities of MariaDB. Some features might have
limited support or restricted privileges.

You can filter new Amazon RDS features on the [What's New with Database?](https://aws.amazon.com/about-aws/whats-new/database/ "https://aws.amazon.com/about-aws/whats-new/database/") page. For
**Products**, choose **Amazon RDS**. Then search using
keywords such as `MariaDB 2023`.

###### Note

The following lists are not exhaustive.

For more information about MariaDB feature support on Amazon RDS, see the following topics.

###### Topics

- [Supported storage engines for MariaDB on Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md")
- [Cache warming for MariaDB on Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md")
- [MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md")

## MariaDB feature support on Amazon RDS for MariaDB major versions

In the following sections, find information about MariaDB feature support on Amazon RDS for
MariaDB major versions:

###### Topics

- [MariaDB 11.8 support on Amazon RDS](#MariaDB.Concepts.FeatureSupport.11-8 "#MariaDB.Concepts.FeatureSupport.11-8")
- [MariaDB 11.4 support on
  Amazon RDS](#MariaDB.Concepts.FeatureSupport.11-4 "#MariaDB.Concepts.FeatureSupport.11-4")
- [MariaDB 10.11 support on
  Amazon RDS](#MariaDB.Concepts.FeatureSupport.10-11 "#MariaDB.Concepts.FeatureSupport.10-11")
- [MariaDB 10.6 support on Amazon RDS](#MariaDB.Concepts.FeatureSupport.10-6 "#MariaDB.Concepts.FeatureSupport.10-6")
- [MariaDB 10.5 support on Amazon RDS](#MariaDB.Concepts.FeatureSupport.10-5 "#MariaDB.Concepts.FeatureSupport.10-5")
- [MariaDB 10.4 support on Amazon RDS](#MariaDB.Concepts.FeatureSupport.10-4 "#MariaDB.Concepts.FeatureSupport.10-4")

For information about supported minor versions of Amazon RDS for MariaDB, see [MariaDB on Amazon RDS versions](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 11.8 support on Amazon RDS

Amazon RDS supports the following new features for your DB instances running MariaDB version 11.8 or higher.

###### Note

In MariaDB 11.8, the default value for `require_secure_transport` is now `1`, requiring secure SSL/TLS connections. Set to `0` if non-secure connections are needed.

- **New default value for parameter** – The default value of `require_secure_transport` parameter changed from `0` to `1`, enforcing secure transport connections by default.
  For more information, see [Requiring SSL/TLS for all
  connections to a MariaDB DB instance on Amazon RDS](mariadb-ssl-connections.md "mariadb-ssl-connections.md").
- **Vector support** – You can use the MariaDB Vector to store and search AI-generated vectors directly in MariaDB.
  This feature introduces the following system variables:
  - The variable [`mhnsw_default_distance`](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_distance "https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_distance") specifies the default distance metric for MHNSW vector indexing.
  - The variable [`mhnsw_default_m`](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_m "https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_default_m") defines the default value for the `M` parameter in MHNSW vector indexing.
  - The variable [`mhnsw_ef_search`](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_ef_search "https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_ef_search") defines the minimal number of result candidates for vector index searches.
  - The variable [`mhnsw_max_cache_size`](https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_max_cache_size "https://mariadb.com/docs/server/reference/sql-structure/vectors/vector-system-variables#mhnsw_max_cache_size") sets the upper limit for one MHNSW vector index cache.

- **Temporary file size limits** – You can now limit the size of created disk temporary files and tables using two system variables available in the RDS Maria DB 11.8 parameter group:
  - The variable [`max_tmp_session_space_usage`](https://mariadb.com/docs/server/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable "https://mariadb.com/docs/server/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_session_space_usage-system-variable") limits the temporary space allowance per user.
  - The variable [`max_tmp_total_space_usage`](https://mariadb.com/docs/server/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable "https://mariadb.com/docs/server/security/limiting-size-of-created-disk-temporary-files-and-tables/max_tmp_total_space_usage-system-variable") limits the temporary space allowance for all users.

- **Temporary tablespace management** – The temporary tablespace stores temporary tables and grows as data is added. When temporary tables are dropped,
  the space is not automatically reclaimed. You can use the [mysql.rds_execute_operation](mysql_rds_execute_operation.md "mysql_rds_execute_operation.md") procedure
  to shrink the temporary tablespace and reclaim disk space.

For a list of all MariaDB 11.8 features and their documentation, see [Changes and improvements in MariaDB 11.8](https://mariadb.com/kb/en/changes-improvements-in-mariadb-11-8/ "https://mariadb.com/kb/en/changes-improvements-in-mariadb-11-8/") and [Release notes - MariaDB 11.8 series](https://mariadb.com/kb/en/release-notes-mariadb-11-8-series/ "https://mariadb.com/kb/en/release-notes-mariadb-11-8-series/") on the MariaDB website.

For a list of unsupported features, see [MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 11.4 support on

Amazon RDS

Amazon RDS supports the following new features for your DB instances running MariaDB
version 11.4 or higher.

- **Crypographic library** – RDS for MariaDB replaced OpenSSL with AWS Libcrypto (AWS-LC), which is FIPS 140-3 certified.
- **Simple Password Check plugin** – You
  can use the MariaDB [Simple
  Password Check Plugin](https://mariadb.com/kb/en/simple-password-check-plugin/ "https://mariadb.com/kb/en/simple-password-check-plugin/") to check whether a password contains at
  least a specific number of characters of a specific type. For more information,
  see [Using the password validation
  plugins for RDS for MariaDB](MariaDB.Concepts.md "MariaDB.Concepts.md").
- **Cracklib Password Check plugin** – You
  can use the MariaDB [Cracklib
  Password Check Plugin](https://mariadb.com/kb/en/cracklib-password-check-plugin/ "https://mariadb.com/kb/en/cracklib-password-check-plugin/") to check the strength of new passwords. For more information,
  see [Using the password validation
  plugins for RDS for MariaDB](MariaDB.Concepts.md "MariaDB.Concepts.md").
- **InnoDB enhancements** – These
  enhancements include the following items:
  - The change buffer was removed. For more information, see [InnoDB Change Buffering](https://mariadb.com/kb/en/innodb-change-buffering/ "https://mariadb.com/kb/en/innodb-change-buffering/").
  - InnoDB Defragmentation was removed. For more information, see [InnoDB Defragmentation](https://mariadb.com/kb/en/defragmenting-innodb-tablespaces/#innodb-defragmentation "https://mariadb.com/kb/en/defragmenting-innodb-tablespaces/#innodb-defragmentation").

- **New privilege** – The admin user now
  also has the `SHOW CREATE ROUTINE` privilege. This privilege
  permits the grantee to view the `SHOW CREATE` definition
  statement of a routine that's owned by another user. For more information,
  see [Database Privileges](https://mariadb.com/kb/en/grant/#database-privileges "https://mariadb.com/kb/en/grant/#database-privileges").
- **Replication improvement** – MariaDB
  version 11.4 DB instances support binlog indexing. You can create a GTID
  index for each binlog file. These indexes improve the performance of
  replication by reducing the time it takes to locate a GTID. For more information, see [Binlog Indexing](https://mariadb.com/kb/en/gtid/#binlog-indexing "https://mariadb.com/kb/en/gtid/#binlog-indexing").
- **Deprecated or removed parameters** –
  The following parameters have been deprecated or removed for MariaDB version
  11.4 DB instances:
  - `engine_condition_pushdown` is removed from [optimizer_switch](https://mariadb.com/kb/en/optimizer-switch/ "https://mariadb.com/kb/en/optimizer-switch/")
  - [innodb_change_buffer_max_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_change_buffer_max_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_change_buffer_max_size")
  - [innodb_defragment](https://mariadb.com/kb/en/innodb-system-variables/#innodb_defragment "https://mariadb.com/kb/en/innodb-system-variables/#innodb_defragment")
  - `TLSv1.0` and `TLSv1.1` are removed from [tls_version](https://mariadb.com/kb/en/ssltls-system-variables/#tls_version "https://mariadb.com/kb/en/ssltls-system-variables/#tls_version")

- **New default values for a parameter**
  – The default value of the [innodb_undo_tablespaces](https://mariadb.com/kb/en/innodb-system-variables/#innodb_undo_tablespaces "https://mariadb.com/kb/en/innodb-system-variables/#innodb_undo_tablespaces") parameter changed from `0` to
  `3`.
- **New valid values for parameters** –
  The following parameters have new valid values for MariaDB version 11.4 DB
  instances:
  - The valid values for the [binlog_row_image](https://mariadb.com/kb/en/replication-and-binary-log-system-variables/#binlog_row_image "https://mariadb.com/kb/en/replication-and-binary-log-system-variables/#binlog_row_image") parameter now include
    `FULL_NODUP`.
  - The valid values for the [OLD_MODE](https://mariadb.com/kb/en/old-mode/ "https://mariadb.com/kb/en/old-mode/") parameter now include
    `NO_NULL_COLLATION_IDS`.

- **New parameters** – The following
  parameters are new for MariaDB version 11.4 DB instances:
  - The [transaction_isolation](https://mariadb.com/kb/en/server-system-variables/#transaction_isolation "https://mariadb.com/kb/en/server-system-variables/#transaction_isolation") parameter replaces the [tx_isolation](https://mariadb.com/kb/en/server-system-variables/#tx_isolation "https://mariadb.com/kb/en/server-system-variables/#tx_isolation")
    parameter.
  - The [transaction_read_only](https://mariadb.com/kb/en/server-system-variables/#transaction_read_only "https://mariadb.com/kb/en/server-system-variables/#transaction_read_only") parameter replaces the [tx_read_only](https://mariadb.com/kb/en/server-system-variables/#tx_read_only "https://mariadb.com/kb/en/server-system-variables/#tx_read_only")
    parameter.
  - The [block_encryption_mode](https://mariadb.com/kb/en/server-system-variables/#block_encryption_mode "https://mariadb.com/kb/en/server-system-variables/#block_encryption_mode") parameter defines the default block encryption mode for the
    [AES_ENCRYPT()](https://mariadb.com/kb/en/aes_encrypt/ "https://mariadb.com/kb/en/aes_encrypt/") and [AES_DECRYPT()](https://mariadb.com/kb/en/aes_decrypt/ "https://mariadb.com/kb/en/aes_decrypt/") functions.
  - The [character_set_collations](https://mariadb.com/kb/en/server-system-variables/#character_set_collations "https://mariadb.com/kb/en/server-system-variables/#character_set_collations") defines overrides for character set default collations.
  - The [binlog_gtid_index](https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index "https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index"),
    [binlog_gtid_index_page_size](https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index_page_size "https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index_page_size"), and
    [binlog_gtid_index_span_min](https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index_span_min "https://mariadb.com/kb/en/system-versioned-tables/#binlog_gtid_index_span_min") define the properties
    of the binlog GTID index. For more information, see [Binlog Indexing](https://mariadb.com/kb/en/gtid/#binlog-indexing "https://mariadb.com/kb/en/gtid/#binlog-indexing").

For a list of all MariaDB 11.4 features and their documentation, see [Changes
and improvements in MariaDB 11.4](https://mariadb.com/kb/en/changes-improvements-in-mariadb-11-4/ "https://mariadb.com/kb/en/changes-improvements-in-mariadb-11-4/") and [Release notes

- MariaDB 11.4 series](https://mariadb.com/kb/en/release-notes-mariadb-11-4-series/ "https://mariadb.com/kb/en/release-notes-mariadb-11-4-series/") on the MariaDB website.

For a list of unsupported features, see [MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 10.11 support on

Amazon RDS

Amazon RDS supports the following new features for your DB instances running MariaDB
version 10.11 or higher.

- **Password Reuse Check plugin** – You
  can use the MariaDB Password Reuse Check plugin to prevent users from
  reusing passwords and to set the retention period of passwords. For more
  information, see [Password
  Reuse Check Plugin](https://mariadb.com/kb/en/password-reuse-check-plugin/ "https://mariadb.com/kb/en/password-reuse-check-plugin/").
- **GRANT TO PUBLIC authorization** –
  You can grant privileges to all users who have access to your server. For
  more information, see [GRANT TO
  PUBLIC](https://mariadb.com/kb/en/grant/#to-public "https://mariadb.com/kb/en/grant/#to-public").
- **Separation of SUPER and READ ONLY ADMIN
  privileges** – You can remove READ ONLY ADMIN privileges
  from all users, even users that previously had SUPER privileges.
- **Security** – You can now set option
  `--ssl` as the default for your MariaDB client. MariaDB no
  longer silently disables SSL if the configuration is incorrect.
- **SQL commands and functions** – You
  can now use the `SHOW ANALYZE FORMAT=JSON` command and the functions
  `ROW_NUMBER`, `SFORMAT`, and `RANDOM_BYTES`.
  `SFORMAT` allows string formatting and is enabled by default.
  You can convert partition to table and table to partition in a single
  command. There are also several improvements around `JSON_*()`
  functions. `DES_ENCRYPT` and `DES_DECRYPT` functions
  were deprecated for version 10.10 and higher. For more information, see
  [SFORMAT](https://mariadb.com/kb/en/sformat/ "https://mariadb.com/kb/en/sformat/").
- **InnoDB enhancements** – These
  enhancements include the following items:
  - Performance improvements in the redo log to reduce write
    amplification and to improve concurrency.
  - The ability for you to change the undo tablespace without
    reinitializing the data directory. This enhancement reduces control
    plane overhead. It requires restarting but it doesn't require
    reinitialization after changing undo tablespace.
  - Support for `CHECK TABLE … EXTENDED` and for descending
    indexes internally.
  - Improvements to bulk insert.

- **Binlog changes** – These changes
  include the following items:
  - Logging `ALTER` in two phases to decrease replication
    latency. The `binlog_alter_two_phase` parameter is
    disabled by default, but can be enabled through parameter
    groups.
  - Logging `explicit_defaults_for_timestamp`.
  - No longer logging `INCIDENT_EVENT` if the transaction can be
    safely rolled back.

- **Replication**
  **improvement**s – MariaDB version 10.11
  DB instances use GTID replication by default if the master supports it. Also,
  `Seconds_Behind_Master` is more precise.
- **Clients** – You can use new
  command-line options for `mysqlbinglog` and
  `mariadb-dump`. You can use `mariadb-dump` to dump
  and restore historical data.
- **System versioning** – You can modify
  history. MariaDB automatically creates new partitions.
- **Atomic DDL** – `CREATE OR
REPLACE` is now atomic. Either the statement succeeds or it's
  completely reversed.
- **Redo log write** – Redo log writes
  asynchronously.
- **Stored functions** – Stored
  functions now support the same `IN`, `OUT`, and
  `INOUT` parameters as in stored procedures.
- **Deprecated or removed parameters** –
  The following parameters have been deprecated or removed for MariaDB version
  10.11 DB instances:
  - [innodb_change_buffering](https://mariadb.com/kb/en/innodb-system-variables/#innodb_change_buffering "https://mariadb.com/kb/en/innodb-system-variables/#innodb_change_buffering")
  - [innodb_disallow_writes](https://mariadb.com/kb/en/innodb-system-variables/#innodb_disallow_writes "https://mariadb.com/kb/en/innodb-system-variables/#innodb_disallow_writes")
  - [innodb_log_write_ahead_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_write_ahead_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_write_ahead_size")
  - [innodb_prefix_index_cluster_optimization](https://mariadb.com/kb/en/innodb-system-variables/#innodb_prefix_index_cluster_optimization "https://mariadb.com/kb/en/innodb-system-variables/#innodb_prefix_index_cluster_optimization")
  - [keep_files_on_create](https://mariadb.com/kb/en/server-system-variables/#keep_files_on_create "https://mariadb.com/kb/en/server-system-variables/#keep_files_on_create")
  - [old](https://mariadb.com/kb/en/server-system-variables/#old "https://mariadb.com/kb/en/server-system-variables/#old")

- **Dynamic parameters** – The following
  parameters are now dynamic for MariaDB version 10.11 DB instances:
  - [innodb_log_file_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size")
  - [innodb_write_io_threads](https://mariadb.com/kb/en/innodb-system-variables/#innodb_write_io_threads "https://mariadb.com/kb/en/innodb-system-variables/#innodb_write_io_threads")
  - [innodb_read_io_threads](https://mariadb.com/kb/en/innodb-system-variables/#innodb_read_io_threads "https://mariadb.com/kb/en/innodb-system-variables/#innodb_read_io_threads")

- **New default values for parameters**
  – The following parameters have new default values for MariaDB
  version 10.11 DB instances:
  - The default value of the [explicit_defaults_for_timestamp](https://mariadb.com/kb/en/server-system-variables/#explicit_defaults_for_timestamp "https://mariadb.com/kb/en/server-system-variables/#explicit_defaults_for_timestamp") parameter changed from
    `OFF` to `ON`.
  - The default value of the [optimizer_prune_level](https://mariadb.com/kb/en/server-system-variables/#optimizer_prune_level "https://mariadb.com/kb/en/server-system-variables/#optimizer_prune_level") parameter changed from
    `1` to `2`.

- **New valid values for parameters** –
  The following parameters have new valid values for MariaDB version 10.11 DB
  instances:
  - The valid values for the [old](https://mariadb.com/kb/en/server-system-variables/#old "https://mariadb.com/kb/en/server-system-variables/#old") parameter were merged into those for the [old_mode](https://mariadb.com/kb/en/server-system-variables/#old_mode "https://mariadb.com/kb/en/server-system-variables/#old_mode") parameter.
  - The valid values for the [histogram_type](https://mariadb.com/kb/en/server-system-variables/#histogram_type "https://mariadb.com/kb/en/server-system-variables/#histogram_type") parameter now include
    `JSON_HB`.
  - The valid value range for the [innodb_log_buffer_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_buffer_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_buffer_size") parameter is now
    `262144` to `4294967295` (256KB to
    4096MB).
  - The valid value range for the [innodb_log_file_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size") parameter is now
    `4194304` to `512GB` (4MB to
    512GB).
  - The valid values for the [optimizer_prune_level](https://mariadb.com/kb/en/server-system-variables/#optimizer_prune_level "https://mariadb.com/kb/en/server-system-variables/#optimizer_prune_level") parameter now include
    `2`.

- **New parameters** – The following
  parameters are new for MariaDB version 10.11 DB instances:
  - The [binlog_alter_two_phase](https://mariadb.com/kb/en/replication-and-binary-log-system-variables//#binlog_alter_two_phase "https://mariadb.com/kb/en/replication-and-binary-log-system-variables//#binlog_alter_two_phase") parameter can improve
    replication performance.
  - The [log_slow_min_examined_row_limit](https://mariadb.com/kb/en/server-system-variables/#log_slow_min_examined_row_limit "https://mariadb.com/kb/en/server-system-variables/#log_slow_min_examined_row_limit") parameter can improve
    performance.
  - The [log_slow_query](https://mariadb.com/kb/en/server-system-variables/#log_slow_query "https://mariadb.com/kb/en/server-system-variables/#log_slow_query") parameter and the [log_slow_query_file](https://mariadb.com/kb/en/server-system-variables/#log_slow_query_file "https://mariadb.com/kb/en/server-system-variables/#log_slow_query_file") parameter are aliases for
    `slow_query_log` and `slow_query_log_file`, respectively.
  - [optimizer_extra_pruning_depth](https://mariadb.com/kb/en/server-system-variables/#optimizer_extra_pruning_depth "https://mariadb.com/kb/en/server-system-variables/#optimizer_extra_pruning_depth")
  - [system_versioning_insert_history](https://mariadb.com/kb/en/system-versioned-tables/#system_versioning_insert_history "https://mariadb.com/kb/en/system-versioned-tables/#system_versioning_insert_history")

For a list of all MariaDB 10.11 features and their documentation, see
[Changes and improvements in MariaDB 10.11](https://mariadb.com/kb/en/changes-improvements-in-mariadb-1011/ "https://mariadb.com/kb/en/changes-improvements-in-mariadb-1011/")
and [Release notes - MariaDB 10.11 series](https://mariadb.com/kb/en/release-notes-mariadb-1011-series/ "https://mariadb.com/kb/en/release-notes-mariadb-1011-series/")
on the MariaDB website.

For a list of unsupported features, see [MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 10.6 support on Amazon RDS

Amazon RDS supports the following new features for your DB instances running MariaDB
version 10.6 or higher:

- **MyRocks storage engine** –
  You can use the MyRocks storage engine with RDS for MariaDB to optimize storage consumption
  of your write-intensive, high-performance web applications. For more information, see
  [Supported storage engines for MariaDB on Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md") and
  [MyRocks](https://mariadb.com/kb/en/myrocks/ "https://mariadb.com/kb/en/myrocks/").
- **AWS Identity and Access Management (IAM) DB authentication** –
  You can use IAM DB authentication for better security and central management of connections to
  your MariaDB DB instances. For more information, see
  [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").
- **Upgrade options** – You can now
  upgrade to RDS for MariaDB version 10.6 from any prior major release (10.3, 10.4,
  10.5). You can also restore a snapshot of an existing MySQL 5.6 or 5.7 DB
  instance to a MariaDB 10.6 instance. For more information, see [Upgrades of the MariaDB DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").
- **Delayed replication** – You can now set a configurable time period
  for which a read replica lags behind the source database. In a standard MariaDB replication configuration,
  there is minimal replication delay between the source and the replica. With delayed replication, you can set an
  intentional delay as a strategy for disaster recovery. For more information, see
  [Configuring delayed replication with MariaDB](USER_MariaDB.Replication.ReadReplicas.md "USER_MariaDB.Replication.ReadReplicas.md").
- **Oracle PL/SQL compatibility** – By
  using RDS for MariaDB version 10.6, you can more easily migrate your legacy
  Oracle applications to Amazon RDS. For more information, see [SQL_MODE=ORACLE](https://mariadb.com/kb/en/sql_modeoracle/ "https://mariadb.com/kb/en/sql_modeoracle/").
- **Atomic DDL** – Your dynamic data
  language (DDL) statements can be relatively crash-safe with RDS for MariaDB
  version 10.6. `CREATE TABLE`, `ALTER TABLE`,
  `RENAME TABLE`, `DROP TABLE`, `DROP
DATABASE` and related DDL statements are now atomic. Either the
  statement succeeds, or it's completely reversed. For more information, see
  [Atomic
  DDL](https://mariadb.com/kb/en/atomic-ddl/ "https://mariadb.com/kb/en/atomic-ddl/").
- **Other enhancements** – These
  enhancements include a `JSON_TABLE` function for transforming
  JSON data to relational format within SQL, and faster empty table data load
  with Innodb. They also include new `sys_schema` for analysis and
  troubleshooting, optimizer enhancement for ignoring unused indexes, and
  performance improvements. For more information, see [JSON_TABLE](https://mariadb.com/kb/en/json_table/ "https://mariadb.com/kb/en/json_table/").
- **New default values for parameters** – The following parameters have
  new default values for MariaDB version 10.6 DB instances:
  - The default value for the following parameters has changed from `utf8` to `utf8mb3`:

        - [character\_set\_client](https://mariadb.com/kb/en/server-system-variables/#character_set_client "https://mariadb.com/kb/en/server-system-variables/#character_set_client")
        - [character\_set\_connection](https://mariadb.com/kb/en/server-system-variables/#character_set_connection "https://mariadb.com/kb/en/server-system-variables/#character_set_connection")
        - [character\_set\_results](https://mariadb.com/kb/en/server-system-variables/#character_set_results "https://mariadb.com/kb/en/server-system-variables/#character_set_results")
        - [character\_set\_system](https://mariadb.com/kb/en/server-system-variables/#character_set_system "https://mariadb.com/kb/en/server-system-variables/#character_set_system")

    Although the default values have changed for these parameters, there is no functional change. For more information,
    see [Supported Character Sets and Collations](https://mariadb.com/kb/en/supported-character-sets-and-collations/ "https://mariadb.com/kb/en/supported-character-sets-and-collations/")
    in the MariaDB documentation.

  - The default value of the [collation_connection](https://mariadb.com/kb/en/server-system-variables/#collation_connection "https://mariadb.com/kb/en/server-system-variables/#collation_connection") parameter has changed from `utf8_general_ci` to `utf8mb3_general_ci`.
    Although the default value has changed for this parameter, there is no functional change.
  - The default value of the [old_mode](https://mariadb.com/kb/en/server-system-variables/#old_mode "https://mariadb.com/kb/en/server-system-variables/#old_mode") parameter has changed from unset to `UTF8_IS_UTF8MB3`. Although the default value
    has changed for this parameter, there is no functional change.

For a list of all MariaDB 10.6 features and their documentation, see
[Changes and improvements in MariaDB 10.6](https://mariadb.com/kb/en/changes-improvements-in-mariadb-106/ "https://mariadb.com/kb/en/changes-improvements-in-mariadb-106/")
and [Release notes - MariaDB 10.6 series](https://mariadb.com/kb/en/release-notes-mariadb-106-series/ "https://mariadb.com/kb/en/release-notes-mariadb-106-series/")
on the MariaDB website.

For a list of unsupported features, see [MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 10.5 support on Amazon RDS

Amazon RDS supports the following new features for your DB instances
running MariaDB version 10.5 or later:

- **InnoDB enhancements** –
  MariaDB version 10.5 includes InnoDB enhancements. For more information, see
  [InnoDB: Performance Improvements etc.](https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/#innodb-performance-improvements-etc "https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/#innodb-performance-improvements-etc") in the MariaDB documentation.
- **Performance schema updates** –
  MariaDB version 10.5 includes performance schema updates. For more
  information, see [Performance Schema Updates to Match MySQL 5.7 Instrumentation and
  Tables](https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/#performance-schema-updates-to-match-mysql-57-instrumentation-and-tables "https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/#performance-schema-updates-to-match-mysql-57-instrumentation-and-tables") in the MariaDB documentation.
- **One file in the InnoDB redo log** –
  In versions of MariaDB before version 10.5, the value of the
  `innodb_log_files_in_group` parameter was set to
  `2`. In MariaDB version 10.5, the value of this parameter is
  set to `1`.

If you are upgrading from a prior version to MariaDB version 10.5, and you
don't modify the parameters, the `innodb_log_file_size`
parameter value is unchanged. However, it applies to one log file instead of
two. The result is that your upgraded MariaDB version 10.5 DB instance uses
half of the redo log size that it was using before the upgrade. This change
can have a noticeable performance impact. To address this issue, you can
double the value of the `innodb_log_file_size` parameter. For
information about modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

- **SHOW SLAVE STATUS command not
  supported** – In versions of MariaDB before version
  10.5, the `SHOW SLAVE STATUS` command required the
  `REPLICATION SLAVE` privilege. In MariaDB version 10.5, the
  equivalent `SHOW REPLICA STATUS` command requires the `REPLICATION REPLICA ADMIN` privilege. This
  new privilege isn't granted to the RDS master user.

Instead of using the `SHOW REPLICA STATUS` command, run the new `mysql.rds_replica_status` stored procedure
to return similar information. For more information, see [mysql.rds_replica_status](mysql_rds_replica_status.md "mysql_rds_replica_status.md").

- **SHOW RELAYLOG EVENTS command not
  supported** – In versions of MariaDB before version
  10.5, the `SHOW RELAYLOG EVENTS` command required the
  `REPLICATION SLAVE` privilege. In MariaDB version 10.5, this
  command requires the `REPLICATION REPLICA ADMIN` privilege. This
  new privilege isn't granted to the RDS master user.
- **New default values for parameters** – The following parameters have
  new default values for MariaDB version 10.5 DB instances:
  - The default value of the [max_connections](https://mariadb.com/kb/en/server-system-variables/#max_connections "https://mariadb.com/kb/en/server-system-variables/#max_connections")
    parameter has changed to `LEAST({DBInstanceClassMemory/25165760},12000)`. For information about the `LEAST` parameter function,
    see [DB parameter functions](USER_ParamValuesRef.md#USER_ParamFunctions "USER_ParamValuesRef.md#USER_ParamFunctions").
  - The default value of the [innodb_adaptive_hash_index](https://mariadb.com/kb/en/innodb-system-variables/#innodb_adaptive_hash_index "https://mariadb.com/kb/en/innodb-system-variables/#innodb_adaptive_hash_index") parameter has changed to `OFF` (`0`).
  - The default value of the [innodb_checksum_algorithm](https://mariadb.com/kb/en/innodb-system-variables/#innodb_checksum_algorithm "https://mariadb.com/kb/en/innodb-system-variables/#innodb_checksum_algorithm") parameter has changed to `full_crc32`.
  - The default value of the [innodb_log_file_size](https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size "https://mariadb.com/kb/en/innodb-system-variables/#innodb_log_file_size")
    parameter has changed to 2 GB.

For a list of all MariaDB 10.5 features and their documentation, see
[Changes and improvements in MariaDB 10.5](https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/ "https://mariadb.com/kb/en/changes-improvements-in-mariadb-105/")
and
[Release notes - MariaDB 10.5 series](https://mariadb.com/kb/en/release-notes-mariadb-105-series/ "https://mariadb.com/kb/en/release-notes-mariadb-105-series/")
on the MariaDB website.

For a list of unsupported features, see
[MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").

### MariaDB 10.4 support on Amazon RDS

Amazon RDS supports the following new features for your DB instances
running MariaDB version 10.4 or later:

- **User account security enhancements** –
  [Password expiration](https://mariadb.com/kb/en/user-password-expiry/ "https://mariadb.com/kb/en/user-password-expiry/") and
  [account locking](https://mariadb.com/kb/en/account-locking/ "https://mariadb.com/kb/en/account-locking/") improvements
- **Optimizer enhancements** –
  [Optimizer trace feature](https://mariadb.com/kb/en/optimizer-trace-overview/ "https://mariadb.com/kb/en/optimizer-trace-overview/")
- **InnoDB enhancements** –
  [Instant DROP COLUMN support](https://mariadb.com/kb/en/alter-table/#drop-column "https://mariadb.com/kb/en/alter-table/#drop-column") and
  instant `VARCHAR` extension for `ROW_FORMAT=DYNAMIC` and `ROW_FORMAT=COMPACT`
- **New parameters** –
  Including [tcp_nodedelay](https://mariadb.com/kb/en/server-system-variables/#tcp_nodelay "https://mariadb.com/kb/en/server-system-variables/#tcp_nodelay"),
  [tls_version](https://mariadb.com/kb/en/ssltls-system-variables/#tls_version "https://mariadb.com/kb/en/ssltls-system-variables/#tls_version"), and
  [gtid_cleanup_batch_size](https://mariadb.com/kb/en/gtid/#gtid_cleanup_batch_size "https://mariadb.com/kb/en/gtid/#gtid_cleanup_batch_size")

For a list of all MariaDB 10.4 features and their documentation, see
[Changes and improvements in MariaDB 10.4](https://mariadb.com/kb/en/library/changes-improvements-in-mariadb-104/ "https://mariadb.com/kb/en/library/changes-improvements-in-mariadb-104/")
and
[Release notes - MariaDB 10.4 series](https://mariadb.com/kb/en/library/release-notes-mariadb-104-series/ "https://mariadb.com/kb/en/library/release-notes-mariadb-104-series/")
on the MariaDB website.

For a list of unsupported features, see
[MariaDB features not supported by Amazon RDS](MariaDB.Concepts.md "MariaDB.Concepts.md").
