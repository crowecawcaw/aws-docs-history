# Sql Server assessments

This section describes individual premigration assessments for migration tasks that use a Microsoft SQL Server source endpoint.

###### Topics

- [Validate if secondary indexes are enabled on the target database during full-load](#CHAP_Tasks.AssessmentReport.SqlServer.SecondaryIndexesEnabled "#CHAP_Tasks.AssessmentReport.SqlServer.SecondaryIndexesEnabled")
- [Validate that limited LOB mode only is used when BatchApplyEnabled is set to true](#CHAP_Tasks.AssessmentReport.SqlServer.LimitedLOBMode "#CHAP_Tasks.AssessmentReport.SqlServer.LimitedLOBMode")
- [Validate if target database has any triggers enabled on tables in the scope of the task](#CHAP_Tasks.AssessmentReport.SqlServer.TargetDatabaseTriggersEnabled "#CHAP_Tasks.AssessmentReport.SqlServer.TargetDatabaseTriggersEnabled")
- [Check if tables in task scope contain computed columns](#CHAP_Tasks.AssessmentReport.SqlServer.ComputedColumns "#CHAP_Tasks.AssessmentReport.SqlServer.ComputedColumns")
- [Check if tables in task scope have column store indexes](#CHAP_Tasks.AssessmentReport.SqlServer.ColumnstoreIndexes "#CHAP_Tasks.AssessmentReport.SqlServer.ColumnstoreIndexes")
- [Check if memory optimized tables are a part of the task scope](#CHAP_Tasks.AssessmentReport.SqlServer.MemoryOptimized "#CHAP_Tasks.AssessmentReport.SqlServer.MemoryOptimized")
- [Check if temporal tables are a part of the task scope](#CHAP_Tasks.AssessmentReport.SqlServer.TemporalTables "#CHAP_Tasks.AssessmentReport.SqlServer.TemporalTables")
- [Check if delayed durability is enabled at the database level](#CHAP_Tasks.AssessmentReport.SqlServer.DelayedDurability "#CHAP_Tasks.AssessmentReport.SqlServer.DelayedDurability")
- [Check if accelerated data recovery is enabled at the database level](#CHAP_Tasks.AssessmentReport.SqlServer.AcceleratedRecovery "#CHAP_Tasks.AssessmentReport.SqlServer.AcceleratedRecovery")
- [Check if table mapping has more than 10K tables with primary keys](#CHAP_Tasks.AssessmentReport.SqlServer.TableMapping "#CHAP_Tasks.AssessmentReport.SqlServer.TableMapping")
- [Check if the source database has
  tables or schema names with special characters.](#CHAP_Tasks.AssessmentReport.SqlServer.SpecialCharacters "#CHAP_Tasks.AssessmentReport.SqlServer.SpecialCharacters")
- [Check if the source database
  has column names with masked data](#CHAP_Tasks.AssessmentReport.SqlServer.MaskedData "#CHAP_Tasks.AssessmentReport.SqlServer.MaskedData")
- [Check if the source database
  has encrypted backups](#CHAP_Tasks.AssessmentReport.SqlServer.EncryptedBackups "#CHAP_Tasks.AssessmentReport.SqlServer.EncryptedBackups")
- [Check if the source database has
  backups stored at a URL or on Windows Azure.](#CHAP_Tasks.AssessmentReport.SqlServer.RemoteBackups "#CHAP_Tasks.AssessmentReport.SqlServer.RemoteBackups")
- [Check if the source database has
  backups on multiple disks](#CHAP_Tasks.AssessmentReport.SqlServer.MultipleDisks "#CHAP_Tasks.AssessmentReport.SqlServer.MultipleDisks")
- [Check if the source database
  has at least one full backup](#CHAP_Tasks.AssessmentReport.SqlServer.FullBackup "#CHAP_Tasks.AssessmentReport.SqlServer.FullBackup")
- [Check if the source database
  has sparse columns and columnar structure compression.](#CHAP_Tasks.AssessmentReport.SqlServer.SparseOrStructureCompression "#CHAP_Tasks.AssessmentReport.SqlServer.SparseOrStructureCompression")
- [Check if the source database
  instance has server level auditing for SQL Server 2008 or SQL Server 2008 R2](#CHAP_Tasks.AssessmentReport.SqlServer.Audit "#CHAP_Tasks.AssessmentReport.SqlServer.Audit")
- [Check if the source database
  has geometry columns for full LOB mode](#CHAP_Tasks.AssessmentReport.SqlServer.GeometryColumns "#CHAP_Tasks.AssessmentReport.SqlServer.GeometryColumns")
- [Check if the source database
  has columns with the Identity property.](#CHAP_Tasks.AssessmentReport.SqlServer.Identity "#CHAP_Tasks.AssessmentReport.SqlServer.Identity")
- [Check if the DMS user has
  FULL LOAD permissions](#CHAP_Tasks.AssessmentReport.SqlServer.FullLoadPermissions "#CHAP_Tasks.AssessmentReport.SqlServer.FullLoadPermissions")
- [Check if the DMS user has
  FULL LOAD and CDC or CDC only permissions](#CHAP_Tasks.AssessmentReport.SqlServer.FullLoadCDCPermissions "#CHAP_Tasks.AssessmentReport.SqlServer.FullLoadCDCPermissions")
- [Check whether the ignoreMsReplicationEnablement
  ECA is set when using MS-CDC with on-premises or EC2 databases](#CHAP_Tasks.AssessmentReport.SqlServer.IgnoreMsReplicationEnablement "#CHAP_Tasks.AssessmentReport.SqlServer.IgnoreMsReplicationEnablement")
- [Check if the DMS user
  has the VIEW DEFINITION permission.](#CHAP_Tasks.AssessmentReport.SqlServer.ViewDefinition "#CHAP_Tasks.AssessmentReport.SqlServer.ViewDefinition")
- [Check if the DMS user
  has the VIEW DATABASE STATE permission on the MASTER database for users without the Sysadmin role.](#CHAP_Tasks.AssessmentReport.SqlServer.ViewDatabaseState "#CHAP_Tasks.AssessmentReport.SqlServer.ViewDatabaseState")
- [Check if the DMS user has the VIEW SERVER STATE permission.](#CHAP_Tasks.AssessmentReport.SqlServer. "#CHAP_Tasks.AssessmentReport.SqlServer.")
- [Validate if text repl size parameter is not unlimited](#CHAP_Tasks.AssessmentReport.Sqlserver.replsizeparameter "#CHAP_Tasks.AssessmentReport.Sqlserver.replsizeparameter")
- [Validate if
  Primary Key or Unique Index exist on target for Batch Apply](#CHAP_Tasks.AssessmentReport.Sqlserver.batchapply "#CHAP_Tasks.AssessmentReport.Sqlserver.batchapply")
- [Validate if both Primary Key and Unique index exist on target when batch
  apply enabled](#CHAP_Tasks.AssessmentReport.Sqlserver.batchapplysimultaneously "#CHAP_Tasks.AssessmentReport.Sqlserver.batchapplysimultaneously")
- [Validate
  if table has primary key or unique index when DMS validation is
  enabled](#CHAP_Tasks.AssessmentReport.Sqlserver.dmsvalidation "#CHAP_Tasks.AssessmentReport.Sqlserver.dmsvalidation")
- [Validate
  if AWS DMS user has necessary privileges to the target](#CHAP_Tasks.AssessmentReport.Sqlserver.dmsprivileges "#CHAP_Tasks.AssessmentReport.Sqlserver.dmsprivileges")
- [Recommendation on using MaxFullLoadSubTasks setting](#CHAP_Tasks.AssessmentReport.Sqlserver.maxfullloadsubtask "#CHAP_Tasks.AssessmentReport.Sqlserver.maxfullloadsubtask")
- [Check
  Transformation Rule for Digits Randomize](#CHAP_Tasks.AssessmentReport.Sqlserver.gigits.randomise "#CHAP_Tasks.AssessmentReport.Sqlserver.gigits.randomise")
- [Check
  Transformation Rule for Digits mask](#CHAP_Tasks.AssessmentReport.Sqlserver.digits.mask "#CHAP_Tasks.AssessmentReport.Sqlserver.digits.mask")
- [Check
  Transformation Rule for Hashing mask](#CHAP_Tasks.AssessmentReport.Sqlserver.hash.mask "#CHAP_Tasks.AssessmentReport.Sqlserver.hash.mask")
- [Verify
  that Data Validation task settings and Data Masking Digit randomization are
  not enabled simultaneously](#CHAP_Tasks.AssessmentReport.Sqlserver.all.digits.random "#CHAP_Tasks.AssessmentReport.Sqlserver.all.digits.random")
- [Verify
  that Data Validation task settings and Data Masking Hashing mask are not
  enabled simultaneously](#CHAP_Tasks.AssessmentReport.Sqlserver.all.hash.mask "#CHAP_Tasks.AssessmentReport.Sqlserver.all.hash.mask")
- [Verify
  that Data Validation task settings and Data Masking Digit mask are not
  enabled simultaneously](#CHAP_Tasks.AssessmentReport.Sqlserver.all.digit.mask "#CHAP_Tasks.AssessmentReport.Sqlserver.all.digit.mask")
- [Validate that at least one selected object exists in the source database](#CHAP_Tasks.AssessmentReport.Sqlserver.selection.rules "#CHAP_Tasks.AssessmentReport.Sqlserver.selection.rules")
- [Validate that secondary constraints and indexes (non-primary) are present in the source database](#CHAP_Tasks.AssessmentReport.Sqlserver.secondary.constraints "#CHAP_Tasks.AssessmentReport.Sqlserver.secondary.constraints")

## Validate if secondary indexes are enabled on the target database during full-load

**API key:** `sqlserver-check-secondary-indexes`

This premigration assessment validates whether secondary indexes are enabled during full-load on the target database. We recommend that you disable or remove secondary indexes.

For more information,
[Best practices for AWS Database Migration Service](CHAP_BestPractices.md "CHAP_BestPractices.md").

## Validate that limited LOB mode only is used when `BatchApplyEnabled` is set to true

**API key:** `sqlserver-batch-apply-lob-mode`

This premigration assessment validates whether the DMS task includes LOB columns. If LOB columns are included into the scope of the task, you must use `BatchApplyEnabled` together
with limited LOB mode only. We recommend that you create separate tasks for such tables and use transactional apply mode instead.

For more information, see
[How can I use the DMS batch apply feature to improve CDC replication performance?](https://repost.aws/knowledge-center/dms-batch-apply-cdc-replication "https://repost.aws/knowledge-center/dms-batch-apply-cdc-replication").

## Validate if target database has any triggers enabled on tables in the scope of the task

**API key:** `sqlserver-check-for-triggers`

AWS DMS identified triggers in the target database that can impact the performance of the full-load DMS task and latency on target.
Make sure that these triggers are disabled during a task run and enabled during the cut-over period.

## Check if tables in task scope contain computed columns

**API key:** `sqlserver-check-for-computed-fields`

This premigration assessment checks for the presence of computed columns. AWS DMS doesn't support replicating changes from SQL Server computed columns.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if tables in task scope have column store indexes

**API key:** `sqlserver-check-for-columnstore-indexes`

This premigration assessment checks for the presence of tables with columnstore indexes. AWS DMS doesn't support replicating changes from
SQL Server tables with columnstore indexes.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if memory optimized tables are a part of the task scope

**API key:** `sqlserver-check-for-memory-optimized-tables`

This premigration assessment checks for the presence of memory-optimized tables. AWS DMS doesn't support replicating changes from
memory-optimized tables.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if temporal tables are a part of the task scope

**API key:** `sqlserver-check-for-temporal-tables`

This premigration assessment checks for the presence of temporal tables. AWS DMS doesn't support replicating changes from
temporal tables.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if delayed durability is enabled at the database level

**API key:** `sqlserver-check-for-delayed-durability`

This premigration assessment checks for the presence of delayed durability. AWS DMS doesn't support replicating changes from
transactions that use delayed durability.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if accelerated data recovery is enabled at the database level

**API key:** `sqlserver-check-for-accelerated-data-recovery`

This premigration assessment checks for the presence of accelerated data recovery. AWS DMS doesn't support replicating changes from
databases with accelerated data recovery.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if table mapping has more than 10K tables with primary keys

**API key:** `sqlserver-large-number-of-tables`

This premigration assessment checks for the presence of more than 10,000 tables with primary keys. Databases configured
with MS-Replication can experience task failures if there are too many tables with primary keys.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information about configuring MS-Replication, see
[Capturing data changes for ongoing replication from SQL Server](CHAP_Source.SQLServer.md "CHAP_Source.SQLServer.md").

## Check if the source database has

tables or schema names with special characters.

**API key:** `sqlserver-check-for-special-characters`

This premigration assessment verifies whether the source database has table or schema names that include
a character from the following set:

```
\\ -- \n \" \b \r ' \t ;
```

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has column names with masked data

**API key:** `sqlserver-check-for-masked-data`

This premigration assessment verifies whether the source database has masked data.
AWS DMS migrates masked data without masking.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has encrypted backups

**API key:** `sqlserver-check-for-encrypted-backups`

This premigration assessment verifies whether the source database has encrypted backups.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database has

backups stored at a URL or on Windows Azure.

**API key:** `sqlserver-check-for-backup-url`

This premigration assessment verifies whether the source database has backups stored at a URL or on Windows Azure.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database has

backups on multiple disks

**API key:** `sqlserver-check-for-backup-multiple-stripes`

This premigration assessment verifies whether the source database has backups on multiple disks.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has at least one full backup

**API key:** `sqlserver-check-for-full-backup`

This premigration assessment verifies whether the source database has at least one full backup.
SQL Server must be configured for full backup, and you must run a backup before replicating data.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has sparse columns and columnar structure compression.

**API key:** `sqlserver-check-for-sparse-columns`

This premigration assessment verifies whether the source database has sparse columns and
columnar structure compression. DMS doesn't support sparse columns and
columnar structure compression.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

instance has server level auditing for SQL Server 2008 or SQL Server 2008 R2

**API key:** `sqlserver-check-for-audit-2008`

This premigration assessment verifies whether the source database has enabled server-level auditing
for SQL Server 2008 or SQL Server 2008 R2. DMS has a related known issue with SQL Server 2008 and 2008 R2.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has geometry columns for full LOB mode

**API key:** `sqlserver-check-for-geometry-columns`

This premigration assessment verifies whether the source database has geometry columns for
full Large Object (LOB) mode when using SQL Server as a source.
We recommend using limited LOB mode or setting the `InlineLobMaxSize` task setting to use inline LOB mode
when your database includes geometry columns.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the source database

has columns with the Identity property.

**API key:** `sqlserver-check-for-identity-columns`

This premigration assessment verifies whether the source database has a column with the `IDENTITY` property.
DMS doesn't migrate this property to the corresponding target database column.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the DMS user has

FULL LOAD permissions

**API key:** `sqlserver-check-user-permission-for-full-load-only`

This premigration assessment verifies whether the DMS task's user has permissions to run the task in FULL LOAD mode.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the DMS user has

FULL LOAD and CDC or CDC only permissions

**API key:** `sqlserver-check-user-permission-for-cdc`

This premigration assessment verifies whether the DMS User has permissions to run the task in
`FULL LOAD and CDC` or `CDC only` modes.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check whether the `ignoreMsReplicationEnablement`

ECA is set when using MS-CDC with on-premises or EC2 databases

**API key:** `sqlserver-check-attribute-for-enable-ms-cdc-onprem`

Check whether the `ignoreMsReplicationEnablement` extra connection attribute
(ECA) is set when using MS-CDC with on-premises or EC2 databases.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the DMS user

has the VIEW DEFINITION permission.

**API key:** `sqlserver-check-user-permission-on-view-definition`

This premigration assessment verifies whether the user specified in the endpoint settings has the `VIEW DEFINITION` permission.
DMS requires the `VIEW DEFINITION` permission to view object definitions.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the DMS user

has the VIEW DATABASE STATE permission on the MASTER database for users without the Sysadmin role.

**API key:** `sqlserver-check-user-permission-on-view-database-state`

This premigration assessment verifies whether the user specified in the endpoint settings has the `VIEW DATABASE STATE` permission.
DMS requires this permission to access database objects in the MASTER database.
DMS also requires this permission when the user doesn't have sysadmin privileges.
DMS requires this permission to create functions, certificates, and logins,
and to grant credentials.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Check if the DMS user has the VIEW SERVER STATE permission.

**API key:** `sqlserver-check-user-permission-on-view-server-state`

This premigration assessment checks if the user specified in the extra connection attributes (ECA) has the
`VIEW SERVER STATE`permission. `VIEW SERVER STATE` is a server-level permission that
allows a user to view server-wide information and state. This permission provides access to dynamic management views (DMVs) and dynamic management functions (DMFs)
that expose information about the SQL Server instance. This permission is required for the DMS user to have access to CDC resources.
This permission is required to run a DMS task in `FULL LOAD and CDC` or `CDC only` modes.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Validate if text repl size parameter is not unlimited

**API
Key:**`sqlserver-check-for-max-text-repl-size`

Setting Max text repl size parameter on the database could potentially cause
data migration error for LOB columns. DMS highly recommends setting it to
-1.

For more information, see [Troubleshooting issues with Microsoft SQL
Server](CHAP_Troubleshooting.md#CHAP_Troubleshooting.SQLServer "CHAP_Troubleshooting.md#CHAP_Troubleshooting.SQLServer").

## Validate if

Primary Key or Unique Index exist on target for Batch Apply

**API
Key:**`sqlserver-check-batch-apply-target-pk-ui-absence`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on
the target table. Tables without Primary Keys or Unique Indexes causes the batch
to fail, and changes are processed one by one. It is advisable to move such
tables to their own tasks and utilize transactional apply mode instead.
Alternatively, you can create a unique key on the target table.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Validate if both Primary Key and Unique index exist on target when batch

apply enabled

**API
Key:**`sqlserver-check-batch-apply-target-pk-ui-simultaneously`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on
the target table. Tables with Primary Keys and Unique Indexes simultaneously
causes the batch to fail, and changes are processed one by one. It is advisable
to move such tables to their own tasks and utilize transactional apply mode
instead. Alternatively, you can drop unique keys or primary key on the target
table and rebuild it when migrating.

For more information, see [Limitations on using SQL Server
as a source for AWS DMS](CHAP_Source.md#CHAP_Source.SQLServer.Limitations "CHAP_Source.md#CHAP_Source.SQLServer.Limitations").

## Validate

if table has primary key or unique index when DMS validation is
enabled

**API
Key:**`sqlserver-check-pk-validity`

Data validation requires that the table has a primary key or unique index on
both source and target.

For more information, see [AWS DMS data validation](CHAP_Validating.md "CHAP_Validating.md").

## Validate

if AWS DMS user has necessary privileges to the target

**API
Key:**`sqlserver-check-target-privileges`

The AWS DMS user must have must have at least the db_owner user role on the
target database.

For more information, see [Security requirements when using
SQL Server as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.SQLServer.Security "CHAP_Target.md#CHAP_Target.SQLServer.Security").

## Recommendation on using MaxFullLoadSubTasks setting

**API
Key:**`sqlserver-tblnum-for-max-fullload-subtasks`

This assessment checks the number of tables included in the task and
recommends increasing the `MaxFullLoadSubTasks` parameter for optimal
performance during the full load process. By default, AWS DMS migrates 8 tables
simultaneously. Changing the `MaxFullLoadSubTasks` parameter to a
higher value improves the full load performance.

For more information, see [Full-load
task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

## Check

Transformation Rule for Digits Randomize

**API key**:
`sqlserver-datamasking-digits-randomize`

This assessment validates whether columns used in table mappings are
compatible with the Digits Randomize transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying digits randomize
transformations does not guarantee any uniqueness.

## Check

Transformation Rule for Digits mask

**API key**:
`sqlserver-datamasking-digits-mask`

This assessment validates whether any columns used in the table mapping are
not supported by the Digits Mask transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying Digits Mask
transformations to such columns could cause DMS task failures since uniqueness
cannot be guaranteed.

## Check

Transformation Rule for Hashing mask

**API key**:
`sqlserver-datamasking-hash-mask`

This assessment validates whether any of the columns used in the table mapping
are not supported by the Hashing Mask transformation rule. It also checks if the
length of the source column exceeds 64 characters. Ideally, the target column
length should be greater than 64 characters to support hash masking.
Additionally, the assessment checks if any columns selected for transformation
are part of primary keys, unique constraints, or foreign keys, as applying
digits randomize transformations does not guarantee any uniqueness.

## Verify

that Data Validation task settings and Data Masking Digit randomization are
not enabled simultaneously

**API key**:
`all-to-all-validation-with-datamasking-digits-randomize`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit randomization are not simultaneously enabled, as these features
are incompatible.

## Verify

that Data Validation task settings and Data Masking Hashing mask are not
enabled simultaneously

**API key**:
`all-to-all-validation-with-datamasking-hash-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Hashing mask are not simultaneously enabled, as these features are
incompatible.

## Verify

that Data Validation task settings and Data Masking Digit mask are not
enabled simultaneously

**API key**:
`all-to-all-validation-with-digit-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit mask are not simultaneously enabled, as these features are
incompatible.

## Validate that at least one selected object exists in the source database

**API key**:
`all-check-source-selection-rules`

This premigration assessment verifies that at least one object specified in the selection rules exists in the source database, including pattern matching for wildcard-based rules.

## Validate that secondary constraints and indexes (non-primary) are present in the source database

**API key**:
`all-check-secondary-constraints`

This premigration assessment verifies that secondary constraints and indexes (foreign keys, check constraints, non-clustered indexes) are present in the source database.
