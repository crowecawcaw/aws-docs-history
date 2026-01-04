# Comparing Aurora MySQL version 2 and Aurora MySQL version 3

Use the following to learn about changes to be aware of when you upgrade your Aurora MySQL version 2 cluster to version 3.

###### Topics

- [Atomic Data Definition Language (DDL) support](#AuroraMySQL.Compare-v2-v3-atomic-ddl "#AuroraMySQL.Compare-v2-v3-atomic-ddl")
- [Feature differences between Aurora MySQL version 2 and 3](#AuroraMySQL.Compare-v2-v3-features "#AuroraMySQL.Compare-v2-v3-features")
- [Instance class support](#AuroraMySQL.mysql80-instance-classes "#AuroraMySQL.mysql80-instance-classes")
- [Parameter changes for Aurora MySQL version 3](#AuroraMySQL.mysql80-parameter-changes "#AuroraMySQL.mysql80-parameter-changes")
- [Status variables](#AuroraMySQL.mysql80-status-vars "#AuroraMySQL.mysql80-status-vars")
- [Inclusive language changes for Aurora MySQL version 3](#AuroraMySQL.8.0-inclusive-language "#AuroraMySQL.8.0-inclusive-language")
- [AUTO_INCREMENT values](#AuroraMySQL.mysql80-autoincrement "#AuroraMySQL.mysql80-autoincrement")
- [Binary log replication](#AuroraMySQL.mysql80-binlog "#AuroraMySQL.mysql80-binlog")

## Atomic Data Definition Language (DDL) support

One of the largest changes from MySQL 5.7 to 8.0 is the introduction of the [Atomic Data Dictionary](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html"). Before MySQL 8.0, the MySQL
data dictionary used a file-based approach to store metadata such as table definitions (.frm), triggers (.trg), and functions separately from
the storage engine's metadata (such as InnoDB's). This had some issues, including the risk of tables becoming "[orphaned](https://dev.mysql.com/doc/refman/5.7/en/innodb-troubleshooting-datadict.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-troubleshooting-datadict.html")" if something unexpected happened during
a DDL operation, causing the file-based and storage engine metadata to get out of sync.

To fix this, MySQL 8.0 introduced the Atomic Data Dictionary, which stores all metadata in a set of internal InnoDB tables in the
`mysql` schema. This new architecture provides a transactional, [ACID](https://en.wikipedia.org/wiki/ACID "https://en.wikipedia.org/wiki/ACID")-compliant way to manage database metadata, solving the "atomic DDL" problem from the old file-based approach. For more information
on the Atomic Data Dictionary, see [Removal of file-based
metadata storage](https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html "https://dev.mysql.com/doc/refman/8.0/en/data-dictionary-file-removal.html") and [Atomic data definition statement
support](https://dev.mysql.com/doc/refman/8.0/en/atomic-ddl.html "https://dev.mysql.com/doc/refman/8.0/en/atomic-ddl.html") in the _MySQL Reference Manual_.

Due to this architectural change, you must consider the following when upgrading from Aurora MySQL version 2 to version 3:

- The file-based metadata from version 2 must be migrated to the new data dictionary tables during the upgrade process to version 3.
  Depending on how many database objects are migrated, this could take some time.
- The changes have also introduced some new incompatibilities that might need to be addressed before you can upgrade from MySQL 5.7 to
  8.0. For example, 8.0 has some new reserved keywords that could conflict with existing database object names.

To help you identify these incompatibilities before upgrading the engine, Aurora MySQL runs a series of upgrade compatibility checks (prechecks)
to determine whether there are any incompatible objects in your database dictionary, before performing the data dictionary upgrade. For more
information on the prechecks, see [Major version upgrade prechecks for Aurora MySQL](AuroraMySQL.md "AuroraMySQL.md").

## Feature differences between Aurora MySQL version 2 and 3

The following Amazon Aurora MySQL features are supported in Aurora MySQL for MySQL 5.7, but these features aren't supported
in Aurora MySQL for MySQL 8.0:

- You can't use Aurora MySQL version 3 for Aurora Serverless v1 clusters. Aurora MySQL version 3
  works with Aurora Serverless v2.
- Lab mode doesn't apply to Aurora MySQL version 3. There aren't any lab mode features in Aurora MySQL version

3.  Instant DDL supersedes the fast online DDL feature that was formerly available in lab mode. For an example, see
    [Instant DDL (Aurora MySQL version 3)](AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl "AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl").

- The query cache is removed from community MySQL 8.0 and also from Aurora MySQL version 3.
- Aurora MySQL version 3 is compatible with the community MySQL hash join feature. The Aurora-specific implementation
  of hash joins in Aurora MySQL version 2 isn't used. For information about using hash joins with Aurora parallel
  query, see [Turning on hash join for
  parallel query clusters](aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join "aurora-mysql-parallel-query-enabling.md#aurora-mysql-parallel-query-enabling-hash-join") and [Aurora MySQL hints](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md"). For general usage information about hash joins, see [Hash Join Optimization](https://dev.mysql.com/doc/refman/8.0/en/hash-joins.html "https://dev.mysql.com/doc/refman/8.0/en/hash-joins.html") in the
  _MySQL Reference Manual_.
- The `mysql.lambda_async` stored procedure that was deprecated in Aurora MySQL version 2 is removed in
  version 3. For version 3, use the asynchronous function `lambda_async` instead.
- The default character set in Aurora MySQL version 3 is `utf8mb4`. In Aurora MySQL version 2, the default
  character set was `latin1`. For information about this character set, see [The utf8mb4 Character Set (4-Byte
  UTF-8 Unicode Encoding)](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html "https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html") in the _MySQL Reference Manual_.

Some Aurora MySQL features are available for certain combinations of AWS Region and DB engine version. For details, see
[Supported features in
Amazon Aurora by AWS Region and Aurora DB engine](Concepts.AuroraFeaturesRegionsDBEngines.md "Concepts.AuroraFeaturesRegionsDBEngines.md").

## Instance class support

Aurora MySQL version 3 supports a different set of instance classes from Aurora MySQL version 2:

- For larger instances, you can use the modern instance classes such as `db.r5`, `db.r6g`, and
  `db.x2g`.
- For smaller instances, you can use the modern instance classes such as `db.t3` and
  `db.t4g`.

###### Note

We recommend using the T DB instance classes only for development and test servers, or other non-production
servers. For more details on the T instance classes, see [Using T instance classes for development and testing](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium").

The following instance classes from Aurora MySQL version 2 aren't available for Aurora MySQL version 3:

- `db.r4`
- `db.r3`
- `db.t3.small`
- `db.t2`

Check your administration scripts for any CLI statements that create Aurora MySQL
DB instances. Hardcode instance class names that aren't available for
Aurora MySQL version 3. If necessary, modify the instance class names to ones that
Aurora MySQL version 3 supports.

###### Tip

To check the instance classes that you can use for a specific combination of Aurora MySQL version and AWS Region, use
the `describe-orderable-db-instance-options` AWS CLI command.

For full details about Aurora instance classes, see [Amazon Aurora DB instance classes](Concepts.md "Concepts.md").

## Parameter changes for Aurora MySQL version 3

Aurora MySQL version 3 includes new cluster-level and instance-level configuration parameters. Aurora MySQL version 3 also
removes some parameters that were present in Aurora MySQL version 2. Some parameter names are changed as a result of the
initiative for inclusive language. For backward compatibility, you can still retrieve the parameter values using either the
old names or the new names. However, you must use the new names to specify parameter values in a custom parameter
group.

In Aurora MySQL version 3, the value of the `lower_case_table_names` parameter is set permanently at the time the
cluster is created. If you use a nondefault value for this option, set up your Aurora MySQL version 3 custom parameter group
before upgrading. Then specify the parameter group during the create cluster or snapshot restore operation.

###### Note

With an Aurora global database based on Aurora MySQL, you can't perform an in-place upgrade from Aurora MySQL version
2 to version 3 if the `lower_case_table_names` parameter is turned on. Use the snapshot restore method
instead.

In Aurora MySQL version 3, the `init_connect` and `read_only` parameters don't apply for users who
have the `CONNECTION_ADMIN` privilege. This includes the Aurora master user. For more information, see [Role-based privilege model](AuroraMySQL.md#AuroraMySQL.privilege-model "AuroraMySQL.md#AuroraMySQL.privilege-model").

For the full list of Aurora MySQL cluster parameters, see [Cluster-level parameters](AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Cluster "AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Cluster"). The table covers all the parameters from Aurora MySQL version
2 and 3. The table includes notes showing which parameters are new in Aurora MySQL version 3 or were removed from Aurora MySQL
version 3.

For the full list of Aurora MySQL instance parameters, see [Instance-level parameters](AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Instance "AuroraMySQL.Reference.md#AuroraMySQL.Reference.Parameters.Instance"). The table covers all the parameters from Aurora MySQL version
2 and 3. The table includes notes showing which parameters are new in Aurora MySQL version 3 and which parameters were removed
from Aurora MySQL version 3. It also includes notes showing which parameters were modifiable in earlier versions but not
Aurora MySQL version 3.

For information about parameter names that changed, see [Inclusive language changes for Aurora MySQL version 3](#AuroraMySQL.8.0-inclusive-language "#AuroraMySQL.8.0-inclusive-language").

## Status variables

For information about status variables that aren't applicable to Aurora MySQL, see [MySQL status variables that don't apply to
Aurora MySQL](AuroraMySQL.Reference.md#AuroraMySQL.Reference.StatusVars.Inapplicable "AuroraMySQL.Reference.md#AuroraMySQL.Reference.StatusVars.Inapplicable").

## Inclusive language changes for Aurora MySQL version 3

Aurora MySQL version 3 is compatible with version 8.0.23 from the MySQL community edition. Aurora MySQL version 3 also
includes changes from MySQL 8.0.26 related to keywords and system schemas for inclusive language. For example, the
`SHOW REPLICA STATUS` command is now preferred instead of `SHOW SLAVE STATUS`.

The following Amazon CloudWatch metrics have new names in Aurora MySQL version 3.

In Aurora MySQL version 3, only the new metric names are available. Make sure to update any alarms or other automation that
relies on metric names when you upgrade to Aurora MySQL version 3.

| Old name                        | New name                        |
| ------------------------------- | ------------------------------- |
| `ForwardingMasterDMLLatency`    | `ForwardingWriterDMLLatency`    |
| `ForwardingMasterOpenSessions`  | `ForwardingWriterOpenSessions`  |
| `AuroraDMLRejectedMasterFull`   | `AuroraDMLRejectedWriterFull`   |
| `ForwardingMasterDMLThroughput` | `ForwardingWriterDMLThroughput` |

The following status variables have new names in Aurora MySQL version 3.

For compatibility, you can use either name in the initial Aurora MySQL version 3 release. The old status variable names are
to be removed in a future release.

| Name to be removed                         | New or preferred name                      |
| ------------------------------------------ | ------------------------------------------ |
| `Aurora_fwd_master_dml_stmt_duration`      | `Aurora_fwd_writer_dml_stmt_duration`      |
| `Aurora_fwd_master_dml_stmt_count`         | `Aurora_fwd_writer_dml_stmt_count`         |
| `Aurora_fwd_master_select_stmt_duration`   | `Aurora_fwd_writer_select_stmt_duration`   |
| `Aurora_fwd_master_select_stmt_count`      | `Aurora_fwd_writer_select_stmt_count`      |
| `Aurora_fwd_master_errors_session_timeout` | `Aurora_fwd_writer_errors_session_timeout` |
| `Aurora_fwd_master_open_sessions`          | `Aurora_fwd_writer_open_sessions`          |
| `Aurora_fwd_master_errors_session_limit`   | `Aurora_fwd_writer_errors_session_limit`   |
| `Aurora_fwd_master_errors_rpc_timeout`     | `Aurora_fwd_writer_errors_rpc_timeout`     |

The following configuration parameters have new names in Aurora MySQL version 3.

For compatibility, you can check the parameter values in the `mysql` client by using either name in the initial
Aurora MySQL version 3 release. You can use only the new names when modifying values in a custom parameter group. The old
parameter names are to be removed in a future release.

| Name to be removed                      | New or preferred name                   |
| --------------------------------------- | --------------------------------------- |
| `aurora_fwd_master_idle_timeout`        | `aurora_fwd_writer_idle_timeout`        |
| `aurora_fwd_master_max_connections_pct` | `aurora_fwd_writer_max_connections_pct` |
| `master_verify_checksum`                | `source_verify_checksum`                |
| `sync_master_info`                      | `sync_source_info`                      |
| `init_slave`                            | `init_replica`                          |
| `rpl_stop_slave_timeout`                | `rpl_stop_replica_timeout`              |
| `log_slow_slave_statements`             | `log_slow_replica_statements`           |
| `slave_max_allowed_packet`              | `replica_max_allowed_packet`            |
| `slave_compressed_protocol`             | `replica_compressed_protocol`           |
| `slave_exec_mode`                       | `replica_exec_mode`                     |
| `slave_type_conversions`                | `replica_type_conversions`              |
| `slave_sql_verify_checksum`             | `replica_sql_verify_checksum`           |
| `slave_parallel_type`                   | `replica_parallel_type`                 |
| `slave_preserve_commit_order`           | `replica_preserve_commit_order`         |
| `log_slave_updates`                     | `log_replica_updates`                   |
| `slave_allow_batching`                  | `replica_allow_batching`                |
| `slave_load_tmpdir`                     | `replica_load_tmpdir`                   |
| `slave_net_timeout`                     | `replica_net_timeout`                   |
| `sql_slave_skip_counter`                | `sql_replica_skip_counter`              |
| `slave_skip_errors`                     | `replica_skip_errors`                   |
| `slave_checkpoint_period`               | `replica_checkpoint_period`             |
| `slave_checkpoint_group`                | `replica_checkpoint_group`              |
| `slave_transaction_retries`             | `replica_transaction_retries`           |
| `slave_parallel_workers`                | `replica_parallel_workers`              |
| `slave_pending_jobs_size_max`           | `replica_pending_jobs_size_max`         |
| `pseudo_slave_mode`                     | `pseudo_replica_mode`                   |

The following stored procedures have new names in Aurora MySQL version 3.

For compatibility, you can use either name in the initial Aurora MySQL version 3 release. The old procedure names are to be
removed in a future release.

| Name to be removed                                 | New or preferred name                              |
| -------------------------------------------------- | -------------------------------------------------- |
| `mysql.rds_set_master_auto_position`               | `mysql.rds_set_source_auto_position`               |
| `mysql.rds_set_external_master`                    | `mysql.rds_set_external_source`                    |
| `mysql.rds_set_external_master_with_auto_position` | `mysql.rds_set_external_source_with_auto_position` |
| `mysql.rds_reset_external_master`                  | `mysql.rds_reset_external_source`                  |
| `mysql.rds_next_master_log`                        | `mysql.rds_next_source_log`                        |

## AUTO_INCREMENT values

In Aurora MySQL version 3, Aurora preserves the `AUTO_INCREMENT` value for each table when it restarts each DB
instance. In Aurora MySQL version 2, the `AUTO_INCREMENT` value wasn't preserved after a restart.

The `AUTO_INCREMENT` value isn't preserved when you set up a new cluster by restoring from a snapshot,
performing a point-in-time recovery, and cloning a cluster. In these cases, the `AUTO_INCREMENT` value is
initialized to the value based on the largest column value in the table at the time the snapshot was created. This behavior
is different than in RDS for MySQL 8.0, where the `AUTO_INCREMENT` value is preserved during these operations.

## Binary log replication

In MySQL 8.0 community edition, binary log replication is turned on by default. In Aurora MySQL version 3, binary log
replication is turned off by default.

###### Tip

If your high availability requirements are fulfilled by the Aurora built-in replication features, you can leave binary
log replication turned off. That way, you can avoid the performance overhead of binary log replication. You can also
avoid the associated monitoring and troubleshooting that are needed to manage binary log replication.

Aurora supports binary log replication from a MySQL 5.7–compatible source to Aurora MySQL version 3. The source
system can be an Aurora MySQL DB cluster, an RDS for MySQL DB instance, or an on-premises MySQL instance.

As does community MySQL, Aurora MySQL supports replication from a source running a specific version to a target running the
same major version or one major version higher. For example, replication from a MySQL 5.6–compatible system to
Aurora MySQL version 3 isn't supported. Replicating from Aurora MySQL version 3 to a MySQL 5.7–compatible or MySQL
5.6–compatible system isn't supported. For details about using binary log replication, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

Aurora MySQL version 3 includes improvements to binary log replication in community MySQL 8.0, such as filtered
replication. For details about the community MySQL 8.0 improvements, see [How Servers Evaluate Replication Filtering
Rules](https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html") in the _MySQL Reference Manual_.

### Transaction compression for binary log replication

For usage information about binary log compression, see [Binary Log Transaction
Compression](https://dev.mysql.com/doc/refman/8.0/en/binary-log-transaction-compression.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log-transaction-compression.html") in the MySQL Reference Manual.

The following limitations apply to binary log compression in Aurora MySQL version 3:

- Transactions whose binary log data is larger than the maximum allowed
  packet size aren't compressed. This is true regardless of whether
  the Aurora MySQL binary log compression setting is turned on. Such
  transactions are replicated without being compressed.
- If you use a connector for change data capture (CDC) that
  doesn't support MySQL 8.0 yet, you can't use this feature. We
  recommend that you test any third-party connectors thoroughly with
  binary log compression. Also, we recommend that you do so before turning
  on binlog compression on systems that use binlog replication for CDC.
