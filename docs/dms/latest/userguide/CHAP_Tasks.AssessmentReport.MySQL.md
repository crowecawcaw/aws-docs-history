

# MySQL assessments
<a name="CHAP_Tasks.AssessmentReport.MySQL"></a>

This section describes individual premigration assessments for migration tasks that use a MySQL, Aurora MySQL-Compatible Edition or Aurora MySQL-Compatible Edition Serverless source endpoint.

**Topics**
+ [Validate if Binary Log transaction compression is disabled](#CHAP_Tasks.AssessmentReport.MySQL.BinaryLogTransaction)
+ [Validate if DMS user has REPLICATION CLIENT and REPLICATION SLAVE permissions for the source database](#CHAP_Tasks.AssessmentReport.MySQL.ReplicationClientPermissions)
+ [Validate if DMS user has SELECT permissions for the source database tables](#CHAP_Tasks.AssessmentReport.MySQL.DMSUserSelectPermissions)
+ [Validate if the server\_id is set to 1 or greater in the source database](#CHAP_Tasks.AssessmentReport.MySQL.ServerID)
+ [Validate if DMS user has necessary permissions for the MySQL database as a target](#CHAP_Tasks.AssessmentReport.MySQL.UserNecessaryPermissions)
+ [Validate if automatic removal of binary logs is set for the source database](#CHAP_Tasks.AssessmentReport.MySQL.BinaryLogAutomaticRemoval)
+ [Validate that limited LOB mode only is used when `BatchApplyEnabled` is set to true](#CHAP_Tasks.AssessmentReport.MySQL.LimitedLOBMode)
+ [Validate if a table uses a storage engine other than Innodb](#CHAP_Tasks.AssessmentReport.MySQL.Innodb)
+ [Validate if auto-increment is enabled on any tables used for migration](#CHAP_Tasks.AssessmentReport.MySQL.AutoIncrement)
+ [Validate if the database binlog image is set to `FULL` to support DMS CDC](#CHAP_Tasks.AssessmentReport.MySQL.BinlogImage)
+ [Validate if the source database is a MySQL Read-Replica](#CHAP_Tasks.AssessmentReport.MySQL.ReadReplica)
+ [Validate if a table has partitions, and recommend `target_table_prep_mode` for full-load task settings](#CHAP_Tasks.AssessmentReport.MySQL.FullLoadTaskSettings)
+ [Validate if DMS supports the database version](#CHAP_Tasks.AssessmentReport.MySQL.DatabaseVersion)
+ [Validate if the target database is configured to set `local_infile` to 1](#CHAP_Tasks.AssessmentReport.MySQL.LocalInfile)
+ [Validate if target database has tables with foreign keys](#CHAP_Tasks.AssessmentReport.MySQL.ForeignKeys)
+ [Validate if source tables in the task scope have cascade constraints](#CHAP_Tasks.AssessmentReport.MySQL.Cascade)
+ [Validate if the timeout values are appropriate for a MySQL source or target](#CHAP_Tasks.AssessmentReport.MySQL.Timeout)
+ [Validate `max_statement_time` database parameter](#CHAP_Tasks.AssessmentReport.MySQL.max_statement_time)
+ [Validate if Primary Key or Unique Index exist on target for Batch Apply](#CHAP_Tasks.AssessmentReport.MySQL.batchapply_absence)
+ [Validate if both Primary Key and Unique index exist on target for Batch Apply](#CHAP_Tasks.AssessmentReport.MySQL.batchapply_simul)
+ [Validate if secondary indexes are enabled during full load on the target database](#CHAP_Tasks.AssessmentReport.MySQL.secondaryindexes)
+ [Validate if table has primary key or unique index when DMS validation is enabled](#CHAP_Tasks.AssessmentReport.MySQL.pk_validity)
+ [Recommendation on using `MaxFullLoadSubTasks` setting](#CHAP_Tasks.AssessmentReport.MySQL.fullload_subtasks)
+ [Check Transformation Rule for Digits Randomize](#CHAP_Tasks.AssessmentReport.MySQL.digits.randomise)
+ [Check Transformation Rule for Digits mask](#CHAP_Tasks.AssessmentReport.MySQL.digits.mask)
+ [Check Transformation Rule for Hashing mask](#CHAP_Tasks.AssessmentReport.MYSQL.hash.mask)
+ [Verify that Data Validation task settings and Data Masking Digit randomization are not enabled simultaneously](#CHAP_Tasks.AssessmentReport.MYSQL.all.digits.random)
+ [Verify that Data Validation task settings and Data Masking Hashing mask are not enabled simultaneously](#CHAP_Tasks.AssessmentReport.MYSQL.all.hash.mask)
+ [Verify that Data Validation task settings and Data Masking Digit mask are not enabled simultaneously](#CHAP_Tasks.AssessmentReport.MYSQL.all.digit.mask)
+ [Check if source Amazon Aurora MySQL instance is not a read replica](#CHAP_Tasks.AssessmentReport.MYSQL.read.only)
+ [Check if binary log retention time is set properly](#CHAP_Tasks.AssessmentReport.MYSQL.retention.time)
+ [Check if source tables do not have invisible columns.](#CHAP_Tasks.AssessmentReport.MYSQL.invisible.columns)
+ [Validate if the database binlog format is set to ROW to support DMS CDC](#CHAP_Tasks.AssessmentReport.MYSQL.binlog.format)
+ [Validate that at least one selected object exists in the source database](#CHAP_Tasks.AssessmentReport.MYSQL.selection.rules)
+ [Validate that tables with generated columns exist in the source database](#CHAP_Tasks.AssessmentReport.MYSQL.generated.columns)
+ [Validate that skipTableSuspensionForPartitionDdl is enabled for partitioned tables](#CHAP_Tasks.AssessmentReport.MYSQL.tablepartition.ddl)
+ [Validate that max\_allowed\_packet size can handle source LOB columns](#CHAP_Tasks.AssessmentReport.MYSQL.maxallowed.packetlob)
+ [Validate that secondary constraints and indexes (non-primary) are present in the source database](#CHAP_Tasks.AssessmentReport.MYSQL.secondary.constraints)
+ [Validate that row size of net changes table does not exceed 65535 when batch apply is enabled](#CHAP_Tasks.AssessmentReport.MYSQL.batchapply.mysql)
+ [Validate that the target endpoint is not a read replica](#CHAP_Tasks.AssessmentReport.MYSQL.read.replica)
+ [Validate that number of tables to be migrated does not exceed 10,000](#CHAP_Tasks.AssessmentReport.MYSQL.10k.tables)
+ [Validate that binary logging is enabled](#CHAP_Tasks.AssessmentReport.MYSQL.binlog.enable)
+ [Validate that AWS DMS is connected to a MySQL primary instance](#CHAP_Tasks.AssessmentReport.MYSQL.source.replica)

## Validate if Binary Log transaction compression is disabled
<a name="CHAP_Tasks.AssessmentReport.MySQL.BinaryLogTransaction"></a>

**API key:** `mysql-check-binlog-compression`

This premigration assessment validates whether binary Log transaction compression is disabled. AWS DMS doesn't support binary log transaction compression.

For more information, see [ Limitations on using a MySQL database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Limitations).

## Validate if DMS user has REPLICATION CLIENT and REPLICATION SLAVE permissions for the source database
<a name="CHAP_Tasks.AssessmentReport.MySQL.ReplicationClientPermissions"></a>

**API key:** `mysql-check-replication-privileges`

This premigration assessment validates whether the DMS user specified in the source endpoint connection settings has `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions for the source database if the DMS task migration type is CDC or full-load \+ CDC.

For more information, see [ Using any MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Prerequisites).

## Validate if DMS user has SELECT permissions for the source database tables
<a name="CHAP_Tasks.AssessmentReport.MySQL.DMSUserSelectPermissions"></a>

**API key:** `mysql-check-select-privileges`

This premigration assessment validates whether the DMS user specified in the source endpoint connection settings has SELECT permissions for the source database tables.

For more information, see [ Using any MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Prerequisites).

## Validate if the server\_id is set to 1 or greater in the source database
<a name="CHAP_Tasks.AssessmentReport.MySQL.ServerID"></a>

**API key:** `mysql-check-server-id`

This premigration assessment validates whether the `server_id` server variable is set to 1 or greater in the source database for CDC migration type.

For more information about sources for AWS DMS, see [ Using a self-managed MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.CustomerManaged).

## Validate if DMS user has necessary permissions for the MySQL database as a target
<a name="CHAP_Tasks.AssessmentReport.MySQL.UserNecessaryPermissions"></a>

**API key:** `mysql-check-target-privileges`

This premigration assessment validates whether the DMS user specified in the target endpoint connection settings has the necessary permissions for the MySQL database as a target.

For more information about MySQL source endpoint prerequisites, see [ Using any MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.Prerequisites).

## Validate if automatic removal of binary logs is set for the source database
<a name="CHAP_Tasks.AssessmentReport.MySQL.BinaryLogAutomaticRemoval"></a>

**API key:** `mysql-check-expire-logs-days`

This premigration assessment validates whether your database is configured to automatically remove binary logs. The values of either `EXPIRE_LOGS_DAYS` or `BINLOG_EXPIRE_LOGS_SECONDS` global system variables should be greater than zero to prevent overuse of disk space during migration.

For more information about sources for AWS DMS, see [ Using a self-managed MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.CustomerManaged).

## Validate that limited LOB mode only is used when `BatchApplyEnabled` is set to true
<a name="CHAP_Tasks.AssessmentReport.MySQL.LimitedLOBMode"></a>

**API key:** `mysql-batch-apply-lob-mode`

This premigration assessment validates whether the DMS task includes LOB columns. If LOB columns are included into the scope of the task, you must use `BatchApplyEnabled` together with limited LOB mode only.

For more information about the `BatchApplyEnabled` setting, see [ How can I use the DMS batch apply feature to improve CDC replication performance?](https://repost.aws/knowledge-center/dms-batch-apply-cdc-replication).

## Validate if a table uses a storage engine other than Innodb
<a name="CHAP_Tasks.AssessmentReport.MySQL.Innodb"></a>

**API key:** `mysql-check-table-storage-engine`

This premigration assessment validates whether the storage engine used for any table in the Source MySQL database is an engine other than Innodb. DMS creates target tables with the InnoDB storage engine by default. If you need to use a storage engine other than InnoDB, you must manually create the table on the target database and configure your DMS task to use `TRUNCATE_BEFORE_LOAD` or `DO_NOTHING` as the full-load task setting. For more information about full-load task settings, see [Full-load task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.md).

**Note**  
This premigration assessment is not available for Aurora MySQL-Compatible Edition or Aurora MySQL-Compatible Edition Serverless.

For more information about MySQL endpoint limitations, see [Limitations on using a MySQL database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Limitations).

## Validate if auto-increment is enabled on any tables used for migration
<a name="CHAP_Tasks.AssessmentReport.MySQL.AutoIncrement"></a>

**API key:** `mysql-check-auto-increment`

This premigration assessment validates whether the source tables that are used in the task have auto-increment enabled. DMS doesn't migrate the AUTO\_INCREMENT attribute on a column to a target database. 

For more information about MySQL endpoint limitations, see [Limitations on using a MySQL database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Limitations). For information about handling identity columns in MySQL, see [ Handle IDENTITY columns in AWS DMS: Part 2](https://aws.amazon.com/blogs/database/handle-identity-columns-in-aws-dms-part-2/).

## Validate if the database binlog image is set to `FULL` to support DMS CDC
<a name="CHAP_Tasks.AssessmentReport.MySQL.BinlogImage"></a>

**API key:** `mysql-check-binlog-image`

This premigration assessment checks whether the source database's binlog image is set to `FULL`. In MySQL, the `binlog_row_image` variable determines how a binary log event is written when using the `ROW` format. To ensure compatibility with DMS and support CDC, set the `binlog_row_image` variable to `FULL`. This setting ensures that DMS receives sufficient information to construct the full Data Manipulation Language (DML) for the target database during migration.

To set the binlog image to `FULL`, do the following:
+ For Amazon RDS, this value is `FULL` by default.
+ For databases hosed on-premises or on Amazon EC2, set the `binlog_row_image` value in `my.ini` (Microsoft Windows) or `my.cnf` (UNIX).

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not valid for a full-load only migration. 

## Validate if the source database is a MySQL Read-Replica
<a name="CHAP_Tasks.AssessmentReport.MySQL.ReadReplica"></a>

**API key:** `mysql-check-database-role`

This premigration assessment verifies whether the source database is a read replica. To enable CDC support for DMS when connected to a read replica, set the `log_slave_updates` parameter to `True`. For more information about using a self-managed MySQL database, see [Using a self-managed MySQL-compatible database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.CustomerManaged).

To set the `log_slave_updates` value to `True`, do the following:
+ For Amazon RDS, use the database's parameter group. For information about using RDS database parameter groups, see [ Working with parameter groups ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.
+ For databases hosed on-premises or on Amazon EC2, set the `log_slave_updates` value in `my.ini` (Microsoft Windows) or `my.cnf` (UNIX).

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not valid for a full-load only migration. 

## Validate if a table has partitions, and recommend `target_table_prep_mode` for full-load task settings
<a name="CHAP_Tasks.AssessmentReport.MySQL.FullLoadTaskSettings"></a>

**API key:** `mysql-check-table-partition`

This premigration assessment checks for the presence of tables with partitions in the source database. DMS creates tables without partitions on the MySQL target. To migrate partitioned tables to a partitioned table on the target, you must do the following:
+ Pre-create the partitioned tables in the target MySQL database.
+ Configure your DMS task to use `TRUNCATE_BEFORE_LOAD` or `DO_NOTHING` as the full-load task setting.

For more information about MySQL endpoint limitations, see [Limitations on using a MySQL database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Limitations).

## Validate if DMS supports the database version
<a name="CHAP_Tasks.AssessmentReport.MySQL.DatabaseVersion"></a>

**API key:** `mysql-check-supported-version`

This premigration assessment verifies whether the source database version is compatible with DMS. For more information about supported MySQL versions, see [Source endpoints for data migration](CHAP_Introduction.Sources.md#CHAP_Introduction.Sources.DataMigration).

## Validate if the target database is configured to set `local_infile` to 1
<a name="CHAP_Tasks.AssessmentReport.MySQL.LocalInfile"></a>

**API key:** `mysql-check-target-localinfile-set`

 This premigration assessment checks whether the `local_infile` parameter in the target database is set to 1. DMS requires the 'local\_infile' parameter to be set to 1 during full load in your target database. For more information, see [Migrating from MySQL to MySQL using AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Homogeneous). 

This assessment is only valid for a full-load or full-load and CDC task.

## Validate if target database has tables with foreign keys
<a name="CHAP_Tasks.AssessmentReport.MySQL.ForeignKeys"></a>

**API key:** `mysql-check-fk-target`

This premigration assessment checks whether a full load or full and CDC task migrating to a MySQL database has tables with foreign keys. The default setting in DMS is to load tables in alphabetical order. Tables with foreign keys and referential integrity constraints can cause the load to fail, as the parent and child tables may not be loaded at the same time.

For more information about referential integrity in DMS, see **Working with indexes, triggers, and referential integrity constraints** in the [Improving the performance of an AWS DMS migration](CHAP_BestPractices.md#CHAP_BestPractices.Performance) topic.

## Validate if source tables in the task scope have cascade constraints
<a name="CHAP_Tasks.AssessmentReport.MySQL.Cascade"></a>

**API key:** `mysql-check-cascade-constraints`

This premigration assessment checks if any of the MySQL source tables have cascade constraints. Cascade constraints are not migrated or replicated by DMS tasks, because MySQL doesn't record the changes for these events in the binlog. While AWS DMS doesn't support these constraints, you can use workarounds for relational database targets.

For information about supporting cascase constrains and other constraints, see [Indexes, Foreign Keys, or Cascade Updates or Deletes Not Migrated](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.FKsAndIndexes) in the **Troubleshooting migration tasks in AWS DMS** topic.

## Validate if the timeout values are appropriate for a MySQL source or target
<a name="CHAP_Tasks.AssessmentReport.MySQL.Timeout"></a>

**API key:** `mysql-check-target-network-parameter`

This premigration assessment checks whether a task’s MySQL endpoint has the `net_read_timeout`, `net_write_timeout` and `wait_timeout` settings set to at least 300 seconds. This is needed to prevent disconnects during the migration.

For more information, see [Connections to a target MySQL instance are disconnected during a task](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ConnectionDisconnect).

## Validate `max_statement_time` database parameter
<a name="CHAP_Tasks.AssessmentReport.MySQL.max_statement_time"></a>

**API key:** `mysql-check-max-statement-time`

Check source parameter - `max_Statement_time` for MySQL based sources. If there are tables larger than 1 billion, validate the value `max_Statement_time` and recommend setting to higher value to avoid any potential data loss.

## Validate if Primary Key or Unique Index exist on target for Batch Apply
<a name="CHAP_Tasks.AssessmentReport.MySQL.batchapply_absence"></a>

**API key:** `mysql-check-batch-apply-target-pk-ui-absence`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on the target table. Tables without Primary Keys or Unique Indexes causes the batch to fail, and changes are processed one by one. It is advisable to move such tables to their own tasks and utilize transactional apply mode instead. Alternatively, you can create a unique key on the target table.

For more information, see [Using a MySQL-compatible database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html).

## Validate if both Primary Key and Unique index exist on target for Batch Apply
<a name="CHAP_Tasks.AssessmentReport.MySQL.batchapply_simul"></a>

**API key:** `mysql-check-batch-apply-target-pk-ui-simultaneously`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on the target table. Tables with Primary Keys and Unique Indexes simultaneously causes the batch to fail, and changes are processed one by one. It is advisable to move such tables to their own tasks and utilize transactional apply mode instead. Alternatively, you can drop a unique key(s) or primary key on the target table and rebuild it if you are doing migration.

For more information, see [Using a MySQL-compatible database as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html).

## Validate if secondary indexes are enabled during full load on the target database
<a name="CHAP_Tasks.AssessmentReport.MySQL.secondaryindexes"></a>

**API key:** `mysql-check-secondary-indexes`

Consider disabling or removing the secondary indexes from the target database. Secondary indexes can affect your migration performance during full load. It is advisable to enable secondary indexes before applying the cached changes.

For more information, see [Best practices for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html).

## Validate if table has primary key or unique index when DMS validation is enabled
<a name="CHAP_Tasks.AssessmentReport.MySQL.pk_validity"></a>

**API key:** `mysql-check-pk-validity`

Data validation requires that the table has a primary key or unique index.

For more information, see [AWS DMS data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html).

## Recommendation on using `MaxFullLoadSubTasks` setting
<a name="CHAP_Tasks.AssessmentReport.MySQL.fullload_subtasks"></a>

**API key:** `mysql-tblnum-for-max-fullload-subtasks`

This assessment checks the number of tables included in the task and recommends increasing the `MaxFullLoadSubTasks` parameter for optimal performance during the full load process. By default, AWS DMS migrates 8 tables simultaneously. Changing the `MaxFullLoadSubTasks` parameter to a higher value improves the full load performance.

For more information, see [Full-load task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.html).

## Check Transformation Rule for Digits Randomize
<a name="CHAP_Tasks.AssessmentReport.MySQL.digits.randomise"></a>

**API key**: `mysql-datamasking-digits-randomize`

This assessment validates whether columns used in table mappings are compatible with the Digits Randomize transformation rule. Additionally, the assessment checks if any columns selected for transformation are part of primary keys, unique constraints, or foreign keys, as applying digits randomize transformations does not guarantee any uniqueness.

## Check Transformation Rule for Digits mask
<a name="CHAP_Tasks.AssessmentReport.MySQL.digits.mask"></a>

**API key**: `mysql-datamasking-digits-mask`

This assessment validates whether any columns used in the table mapping are not supported by the Digits Mask transformation rule. Additionally, the assessment checks if any columns selected for transformation are part of primary keys, unique constraints, or foreign keys, as applying Digits Mask transformations to such columns could cause DMS task failures since uniqueness cannot be guaranteed.

## Check Transformation Rule for Hashing mask
<a name="CHAP_Tasks.AssessmentReport.MYSQL.hash.mask"></a>

**API key**: `mysql-datamasking-hash-mask`

This assessment validates whether any of the columns used in the table mapping are not supported by the Hashing Mask transformation rule. It also checks if the length of the source column exceeds 64 characters. Ideally, the target column length should be greater than 64 characters to support hash masking. Additionally, the assessment checks if any columns selected for transformation are part of primary keys, unique constraints, or foreign keys, as applying digits randomize transformations does not guarantee any uniqueness.

## Verify that Data Validation task settings and Data Masking Digit randomization are not enabled simultaneously
<a name="CHAP_Tasks.AssessmentReport.MYSQL.all.digits.random"></a>

**API key**: `all-to-all-validation-with-datamasking-digits-randomize`

This premigration assessment verifies that Data Validation setting and Data Masking Digit randomization are not simultaneously enabled, as these features are incompatible.

## Verify that Data Validation task settings and Data Masking Hashing mask are not enabled simultaneously
<a name="CHAP_Tasks.AssessmentReport.MYSQL.all.hash.mask"></a>

**API key**: `all-to-all-validation-with-datamasking-hash-mask`

This premigration assessment verifies that Data Validation setting and Data Masking Hashing mask are not simultaneously enabled, as these features are incompatible.

## Verify that Data Validation task settings and Data Masking Digit mask are not enabled simultaneously
<a name="CHAP_Tasks.AssessmentReport.MYSQL.all.digit.mask"></a>

**API key**: `all-to-all-validation-with-digit-mask`

This premigration assessment verifies that Data Validation setting and Data Masking Digit mask are not simultaneously enabled, as these features are incompatible.

## Check if source Amazon Aurora MySQL instance is not a read replica
<a name="CHAP_Tasks.AssessmentReport.MYSQL.read.only"></a>

**API key**: `mysql-check-aurora-read-only`

This premigration assessment validates whether migrating between two Amazon Aurora MySQL clusters, the source endpoint must be a read/write instance, not a replica instance.

## Check if binary log retention time is set properly
<a name="CHAP_Tasks.AssessmentReport.MYSQL.retention.time"></a>

**API key**: `mysql-check-binlog-retention-time`

This premigration assessment validates whether the value of 'binlog retention hours' is larger than 24 hours.

## Check if source tables do not have invisible columns.
<a name="CHAP_Tasks.AssessmentReport.MYSQL.invisible.columns"></a>

**API key**: `mysql-check-invisible-columns`

This premigration assessment validates whether source tables do not have invisible columns. AWS DMS does not migrate data from invisible columns in your source database.

## Validate if the database binlog format is set to ROW to support DMS CDC
<a name="CHAP_Tasks.AssessmentReport.MYSQL.binlog.format"></a>

**API key**: `mysql-check-binlog-format`

This premigration assessment validates whether the source database binlog format is configured to ROW to support Change Data Capture (CDC). To set the binlog format to ROW, do the following:
+ For Amazon RDS, use the database's parameter group. For information, see [Configuring MySQL binary logging for Single-AZ databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html) in the Amazon Relational Database Service User Guide. 
+ For databases hosed on-premises or on Amazon EC2, set the `binlog_format` value in `my.ini` (Microsoft Windows) or `my.cnf `(UNIX).

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not valid for a full-load only migration. For more information about self-hosted MySQL servers, see [Using a self-managed MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.CustomerManaged).

## Validate that at least one selected object exists in the source database
<a name="CHAP_Tasks.AssessmentReport.MYSQL.selection.rules"></a>

**API key**: `all-check-source-selection-rules`

This premigration assessment verifies that at least one object specified in the selection rules exists in the source database, including pattern matching for wildcard-based rules.

## Validate that tables with generated columns exist in the source database
<a name="CHAP_Tasks.AssessmentReport.MYSQL.generated.columns"></a>

**API key**: `mysql-check-generated-columns`

This premigration assessment checks whether any of the MySQL source tables have generated columns. AWS DMS tasks don't migrate or replicate generated columns. For information about how to migrate generated columns, see [Limitations on using a MySQL database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Limitations).

## Validate that skipTableSuspensionForPartitionDdl is enabled for partitioned tables
<a name="CHAP_Tasks.AssessmentReport.MYSQL.tablepartition.ddl"></a>

**API key**: `mysql-check-skip-table-suspension-partition-ddl`

This premigration assessment detects partitioned tables in the source database and verifies the `skipTableSuspensionForPartitionDdl` parameter setting. Failure to set this parameter may result in unnecessary table suspensions during migration. For more details, refer to the following link: [Limitations on using a MySQL database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.Limitations).

## Validate that max\_allowed\_packet size can handle source LOB columns
<a name="CHAP_Tasks.AssessmentReport.MYSQL.maxallowed.packetlob"></a>

**API key**: `mysql-check-max-allowed-packet-lob`

AWS DMS detects LOB columns in source tables that exceed your current `max_allowed_packet` setting. This mismatch can cause replication failures during data migration. For more information, see [Troubleshooting issues with MySQL](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL).

## Validate that secondary constraints and indexes (non-primary) are present in the source database
<a name="CHAP_Tasks.AssessmentReport.MYSQL.secondary.constraints"></a>

**API key**: `all-check-secondary-constraints`

This premigration assessment verifies that secondary constraints and indexes (foreign keys, check constraints, non-clustered indexes) are present in the source database.

## Validate that row size of net changes table does not exceed 65535 when batch apply is enabled
<a name="CHAP_Tasks.AssessmentReport.MYSQL.batchapply.mysql"></a>

**API key**: `all-check-for-batch-apply-to-mysql`

This premigration assessment checks if any table contains rows exceeding 65,535 bytes in size. When batch apply is enabled, AWS DMS cannot create temporary tables for rows exceeding this size due to MySQL engine limitations.

## Validate that the target endpoint is not a read replica
<a name="CHAP_Tasks.AssessmentReport.MYSQL.read.replica"></a>

**API key**: `all-check-target-read-replica`

This premigration assessment verifies that the target endpoint is not configured as a read replica. AWS DMS requires write access to the target database and cannot replicate to read-only replicas.

## Validate that number of tables to be migrated does not exceed 10,000
<a name="CHAP_Tasks.AssessmentReport.MYSQL.10k.tables"></a>

**API key**: `mysql-check-10k-tables`

This premigration assessment validates whether the number of tables to migrate exceeds 10,000 based on your table selection.

## Validate that binary logging is enabled
<a name="CHAP_Tasks.AssessmentReport.MYSQL.binlog.enable"></a>

**API key**: `mysql-check-binlog-enabled`

This premigration assessment validates whether binary logging is enabled on the source database.

For more information, see [Using a self-managed MySQL-compatible database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.CustomerManaged).

## Validate that AWS DMS is connected to a MySQL primary instance
<a name="CHAP_Tasks.AssessmentReport.MYSQL.source.replica"></a>

**API key**: `mysql-check-source-replica`

This premigration assessment validates that the AWS DMS task source endpoint is a primary instance.

For more information, see [Using a self-managed MySQL-compatible database as a source for AWS DMS](CHAP_Source.MySQL.md#CHAP_Source.MySQL.CustomerManaged).