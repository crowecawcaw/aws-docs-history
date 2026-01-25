# Oracle assessments

For more information about permissions when using Oracle as a source, see [User account
privileges required on a self-managed Oracle source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Privileges "CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Privileges") or [User account privileges required on an AWS-managed Oracle source for
AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed "CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed").

###### Note

This section describes individual premigration assessments for migration tasks
that use Oracle as a source or a target for AWS DMS.

If you are using self-managed Oracle database as a source for AWS DMS, please
use following permission set:

```
grant select on gv_$parameter to dms_user;
grant select on v_$instance to dms_user;
grant select on v_$version to dms_user;
grant select on gv_$ASM_DISKGROUP to dms_user;
grant select on gv_$database to dms_user;
grant select on DBA_DB_LINKS to to dms_user;
grant select on gv_$log_History to dms_user;
grant select on gv_$log to dms_user;
grant select on dba_types to dms_user;
grant select on dba_users to dms_user;
grant select on dba_directories to dms_user;
grant execute on SYS.DBMS_XMLGEN to dms_user;
```

Additional permissions is required if you are using a self-managed Oracle
database as a source for AWS DMS Serverless:

```
grant select on dba_segments to dms_user;
grant select on v_$tablespace to dms_user;
grant select on dba_tab_subpartitions to dms_user;
grant select on dba_extents to dms_user;
```

If you are using an AWS-managed Oracle database as a source for AWS DMS, use
the following set of permissions:

```
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('V_$PARAMETER', 'dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('V_$INSTANCE', 'dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('V_$VERSION','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('GV_$ASM_DISKGROUP','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('GV_$DATABASE','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_DB_LINKS','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('GV_$LOG_HISTORY','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('GV_$LOG','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_TYPES','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_USERS','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_DIRECTORIES','dms_user', 'SELECT');
GRANT SELECT ON RDSADMIN.RDS_CONFIGURATION to dms_user;
GRANT EXECUTE ON SYS.DBMS_XMLGEN TO dms_user;

```

Additional permissions is required if you are using an AWS-managed Oracle
database as a source for AWS DMS Serverless:

```
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_SEGMENTS','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_TAB_SUBPARTITIONS','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('DBA_EXTENTS','dms_user', 'SELECT');
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('V_$TABLESPACE','dms_user', 'SELECT');
```

If you are using a self-managed Oracle database as a target for AWS DMS, use the
following set of permissions:

```
grant select on v_$instance to dms_user;
grant execute on SYS.DBMS_XMLGEN to dms_user;
```

If you are using an AWS-managed Oracle database as a target for AWS DMS, use
the following set of permissions:

```
EXEC RDSADMIN.RDSADMIN_UTIL.GRANT_SYS_OBJECT('V_$INSTANCE', 'dms_user', 'SELECT');
GRANT EXECUTE ON SYS.DBMS_XMLGEN TO dms_user;
```

###### Topics

- [Validate that limited LOB mode only is used when BatchApplyEnabled is enabled](#CHAP_Tasks.AssessmentReport.Oracle.LimitedLOBMode "#CHAP_Tasks.AssessmentReport.Oracle.LimitedLOBMode")
- [Validate if tables on the source has columns without scale specified for the Number data type](#CHAP_Tasks.AssessmentReport.Oracle.NumberTypeWithoutScale "#CHAP_Tasks.AssessmentReport.Oracle.NumberTypeWithoutScale")
- [Validate triggers on the target database](#CHAP_Tasks.AssessmentReport.Oracle.TriggersOnTargetDatabase "#CHAP_Tasks.AssessmentReport.Oracle.TriggersOnTargetDatabase")
- [Validate if source has archivelog DEST_ID set to 0](#CHAP_Tasks.AssessmentReport.Oracle.UseZeroDestIDTrue "#CHAP_Tasks.AssessmentReport.Oracle.UseZeroDestIDTrue")
- [Validate if secondary indexes are enabled on the target database during full-load](#CHAP_Tasks.AssessmentReport.Oracle.SecondaryIndexesEnabled "#CHAP_Tasks.AssessmentReport.Oracle.SecondaryIndexesEnabled")
- [Validate if tables used in the DMS task scope with BatchApplyEnabled have more than 999 columns](#CHAP_Tasks.AssessmentReport.Oracle.SetBatchApplyEnabledTrue "#CHAP_Tasks.AssessmentReport.Oracle.SetBatchApplyEnabledTrue")
- [Check supplemental logging on database level](#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLogging "#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLogging")
- [Validate if required DB link is created for Standby](#CHAP_Tasks.AssessmentReport.Oracle.DbLink "#CHAP_Tasks.AssessmentReport.Oracle.DbLink")
- [Oracle validation for LOB datatype and if binary reader is configured](#CHAP_Tasks.AssessmentReport.Oracle.Lob "#CHAP_Tasks.AssessmentReport.Oracle.Lob")
- [Validate if the database is CDB](#CHAP_Tasks.AssessmentReport.Oracle.Cdb "#CHAP_Tasks.AssessmentReport.Oracle.Cdb")
- [Check the Oracle Database Edition](#CHAP_Tasks.AssessmentReport.Oracle.Express "#CHAP_Tasks.AssessmentReport.Oracle.Express")
- [Validate Oracle CDC method for DMS](#CHAP_Tasks.AssessmentReport.Oracle.CdcConfigurations "#CHAP_Tasks.AssessmentReport.Oracle.CdcConfigurations")
- [Validate Oracle RAC configuration for DMS](#CHAP_Tasks.AssessmentReport.Oracle.Rac "#CHAP_Tasks.AssessmentReport.Oracle.Rac")
- [Validate if DMS user has permissions on target](#CHAP_Tasks.AssessmentReport.Oracle.TargetPermissions "#CHAP_Tasks.AssessmentReport.Oracle.TargetPermissions")
- [Validate if supplemental logging is
  required for all columns](#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLoggingColumns "#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLoggingColumns")
- [Validate if supplemental
  logging is enabled on tables with Primary or Unique keys](#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLoggingIndexes "#CHAP_Tasks.AssessmentReport.Oracle.SupplementalLoggingIndexes")
- [Validate if there are SecureFile LOBs and the task is
  configured for Full LOB mode](#CHAP_Tasks.AssessmentReport.Oracle.SecureFileLOBs "#CHAP_Tasks.AssessmentReport.Oracle.SecureFileLOBs")
- [Validate whether Function-Based
  Indexes are being used within the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.FunctionBasedIndexes "#CHAP_Tasks.AssessmentReport.Oracle.FunctionBasedIndexes")
- [Validate whether global
  temporary tables are being used on the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.GlobalTemporaryTables "#CHAP_Tasks.AssessmentReport.Oracle.GlobalTemporaryTables")
- [Validate whether
  index-organized tables with an overflow segment are being used on the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.IndexOrganizedTables "#CHAP_Tasks.AssessmentReport.Oracle.IndexOrganizedTables")
- [Validate if multilevel nesting
  tables are used on the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.MultilevelNestingTables "#CHAP_Tasks.AssessmentReport.Oracle.MultilevelNestingTables")
- [Validate if invisible columns are
  used on the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.InvisibleColumns "#CHAP_Tasks.AssessmentReport.Oracle.InvisibleColumns")
- [Validate if materialized views based on
  a ROWID column are used on the tables included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.RowIDMaterialViews "#CHAP_Tasks.AssessmentReport.Oracle.RowIDMaterialViews")
- [Validate if Active Data Guard DML
  Redirect feature is used.](#CHAP_Tasks.AssessmentReport.Oracle.ActiveDataGuard "#CHAP_Tasks.AssessmentReport.Oracle.ActiveDataGuard")
- [Validate if Hybrid Partitioned
  Tables are used.](#CHAP_Tasks.AssessmentReport.Oracle.HybridPartitionedTables "#CHAP_Tasks.AssessmentReport.Oracle.HybridPartitionedTables")
- [Validate if schema-only Oracle
  accounts are used](#CHAP_Tasks.AssessmentReport.Oracle.SchemaOnly "#CHAP_Tasks.AssessmentReport.Oracle.SchemaOnly")
- [Validate if Virtual Columns are used](#CHAP_Tasks.AssessmentReport.Oracle.VirtualColumns "#CHAP_Tasks.AssessmentReport.Oracle.VirtualColumns")
- [Validate whether table names defined in the task
  scope contain apostrophes.](#CHAP_Tasks.AssessmentReport.Oracle.NamesWithApostrophes "#CHAP_Tasks.AssessmentReport.Oracle.NamesWithApostrophes")
- [Validate whether the
  columns defined in the task scope have
  XMLType, Long, or Long Raw datatypes and verify the LOB mode configuration in the task settings.](#CHAP_Tasks.AssessmentReport.Oracle.XMLLongRawDatatypes "#CHAP_Tasks.AssessmentReport.Oracle.XMLLongRawDatatypes")
- [Validate whether the source Oracle
  version is supported by AWS DMS.](#CHAP_Tasks.AssessmentReport.Oracle.SourceOracleVersion "#CHAP_Tasks.AssessmentReport.Oracle.SourceOracleVersion")
- [Validate whether the target Oracle
  version is supported by AWS DMS.](#CHAP_Tasks.AssessmentReport.Oracle.TargetOracleVersion "#CHAP_Tasks.AssessmentReport.Oracle.TargetOracleVersion")
- [Validate whether the DMS user has the
  required permissions to use data validation.](#CHAP_Tasks.AssessmentReport.Oracle.DataValidation "#CHAP_Tasks.AssessmentReport.Oracle.DataValidation")
- [Validate if the DMS user has permissions
  to use Binary Reader with Oracle ASM](#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderPrivilegesASM "#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderPrivilegesASM")
- [Validate if the DMS user has permissions
  to use Binary Reader with Oracle non-ASM](#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderPrivilegesNonASM "#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderPrivilegesNonASM")
- [Validate if the DMS user has permissions to use
  Binary Reader with CopyToTempFolder method](#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderTemp "#CHAP_Tasks.AssessmentReport.Oracle.BinaryReaderTemp")
- [Validate if the DMS user has permissions to
  use Oracle Standby as a Source](#CHAP_Tasks.AssessmentReport.Oracle.StandbySource "#CHAP_Tasks.AssessmentReport.Oracle.StandbySource")
- [Validate if the DMS source is connected
  to an application container PDB](#CHAP_Tasks.AssessmentReport.Oracle.AppPdb "#CHAP_Tasks.AssessmentReport.Oracle.AppPdb")
- [Validate if the table has XML datatypes
  included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.XmlColumns "#CHAP_Tasks.AssessmentReport.Oracle.XmlColumns")
- [Validate whether archivelog mode is
  enabled on the source database.](#CHAP_Tasks.AssessmentReport.Oracle.Archivelog "#CHAP_Tasks.AssessmentReport.Oracle.Archivelog")
- [Validates the archivelog
  retention for RDS Oracle.](#CHAP_Tasks.AssessmentReport.Oracle.ArchivelogRetention "#CHAP_Tasks.AssessmentReport.Oracle.ArchivelogRetention")
- [Validate if the table has
  Extended datatypes included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.ExtendedColumns "#CHAP_Tasks.AssessmentReport.Oracle.ExtendedColumns")
- [Validate the length of the object
  name included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.30ByteLimit "#CHAP_Tasks.AssessmentReport.Oracle.30ByteLimit")
- [Validate if the DMS source is
  connected to an Oracle PDB](#CHAP_Tasks.AssessmentReport.Oracle.PDBEnabled "#CHAP_Tasks.AssessmentReport.Oracle.PDBEnabled")
- [Validate if the table has spatial
  columns included in the task scope.](#CHAP_Tasks.AssessmentReport.Oracle.SpatialColumns "#CHAP_Tasks.AssessmentReport.Oracle.SpatialColumns")
- [Validate if the DMS source is connected
  to an Oracle standby.](#CHAP_Tasks.AssessmentReport.Oracle.StandbyDB "#CHAP_Tasks.AssessmentReport.Oracle.StandbyDB")
- [Validate if the source
  database tablespace is encrypted using TDE.](#CHAP_Tasks.AssessmentReport.Oracle.StandbyDB "#CHAP_Tasks.AssessmentReport.Oracle.StandbyDB")
- [Validates if the source database
  uses Automatic Storage Management (ASM)](#CHAP_Tasks.AssessmentReport.Oracle.ASMSource "#CHAP_Tasks.AssessmentReport.Oracle.ASMSource")
- [Validate if batch apply is
  enabled and whether the table on the target Oracle database has parallelism enabled at the
  table or index level](#CHAP_Tasks.AssessmentReport.Oracle.batchapply "#CHAP_Tasks.AssessmentReport.Oracle.batchapply")
- [Recommend
  “Bulk Array Size” parameter by validating the tables in the task
  scope](#CHAP_Tasks.AssessmentReport.Oracle.bulkarraysize "#CHAP_Tasks.AssessmentReport.Oracle.bulkarraysize")
- [Validate if HandleCollationDiff task setting is Configured](#CHAP_Tasks.AssessmentReport.Oracle.handlecollationdiff "#CHAP_Tasks.AssessmentReport.Oracle.handlecollationdiff")
- [Validate if
  table has primary key or unique index and its state is VALID when DMS
  validation is enabled](#CHAP_Tasks.AssessmentReport.Oracle.pkvalidity "#CHAP_Tasks.AssessmentReport.Oracle.pkvalidity")
- [Validate if
  Binary Reader is used for Oracle Standby as a source](#CHAP_Tasks.AssessmentReport.Oracle.binaryreader "#CHAP_Tasks.AssessmentReport.Oracle.binaryreader")
- [Validate if the AWS DMS user has the required directory permissions to
  replicate data from an Oracle RDS Standby database.](#CHAP_Tasks.AssessmentReport.Oracle.directorypermissions "#CHAP_Tasks.AssessmentReport.Oracle.directorypermissions")
- [Validate the type of Oracle Standby used for replication](#CHAP_Tasks.AssessmentReport.Oracle.physicalstandby "#CHAP_Tasks.AssessmentReport.Oracle.physicalstandby")
- [Validate if
  required directories are created for RDS Oracle standby](#CHAP_Tasks.AssessmentReport.Oracle.rdsstandby "#CHAP_Tasks.AssessmentReport.Oracle.rdsstandby")
- [Validate if
  Primary Key or Unique Index exists on target for Batch Apply](#CHAP_Tasks.AssessmentReport.Oracle.batchapplypkui "#CHAP_Tasks.AssessmentReport.Oracle.batchapplypkui")
- [Validate if both Primary Key and Unique index exist on target for Batch
  Apply](#CHAP_Tasks.AssessmentReport.Oracle.batchapplypkuitarget "#CHAP_Tasks.AssessmentReport.Oracle.batchapplypkuitarget")
- [Validate if
  unsupported HCC levels are used for Full Load](#CHAP_Tasks.AssessmentReport.Oracle.hccfullload "#CHAP_Tasks.AssessmentReport.Oracle.hccfullload")
- [Validate if
  unsupported HCC levels are used for Full Load with CDC](#CHAP_Tasks.AssessmentReport.Oracle.hccandcdc "#CHAP_Tasks.AssessmentReport.Oracle.hccandcdc")
- [Validate
  if unsupported HCC compression used for CDC](#CHAP_Tasks.AssessmentReport.Oracle.binaryreaderhcccdc "#CHAP_Tasks.AssessmentReport.Oracle.binaryreaderhcccdc")
- [CDC
  Recommendation based on source compression method](#CHAP_Tasks.AssessmentReport.Oracle.cdcmethodbycompression "#CHAP_Tasks.AssessmentReport.Oracle.cdcmethodbycompression")
- [Check if
  batch apply is enabled and validate whether the table has more than 999
  columns](#CHAP_Tasks.AssessmentReport.Oracle.batchapplylob "#CHAP_Tasks.AssessmentReport.Oracle.batchapplylob")
- [Check
  Transformation Rule for Digits Randomize](#CHAP_Tasks.AssessmentReport.Oracle.digits.randomize "#CHAP_Tasks.AssessmentReport.Oracle.digits.randomize")
- [Check
  Transformation Rule for Digits mask](#CHAP_Tasks.AssessmentReport.Oracle.digits.mask "#CHAP_Tasks.AssessmentReport.Oracle.digits.mask")
- [Check
  Transformation Rule for Hashing mask](#CHAP_Tasks.AssessmentReport.Oracle.hash.mask "#CHAP_Tasks.AssessmentReport.Oracle.hash.mask")
- [Verify
  that Data Validation task settings and Data Masking Digit randomization are
  not enabled simultaneously](#CHAP_Tasks.AssessmentReport.Oracle.all.digit.random "#CHAP_Tasks.AssessmentReport.Oracle.all.digit.random")
- [Verify that
  Data Validation task settings and Data Masking Hashing mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.Oracle.all.hash.mask "#CHAP_Tasks.AssessmentReport.Oracle.all.hash.mask")
- [Verify that
  Data Validation task settings and Data Masking Digit mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.Oracle.all.digit.mask "#CHAP_Tasks.AssessmentReport.Oracle.all.digit.mask")
- [Validate
  that replication to a streaming target does not include LOBs or extended
  data type columns](#CHAP_Tasks.AssessmentReport.Oracle.streaming-target "#CHAP_Tasks.AssessmentReport.Oracle.streaming-target")
- [Validate that
  CDC-only task is configured to use the OpenTransactionWindow endpoint
  setting](#CHAP_Tasks.AssessmentReport.Oracle.open.tx.window "#CHAP_Tasks.AssessmentReport.Oracle.open.tx.window")
- [Validate
  that at least one selected object exists in the source database](#CHAP_Tasks.AssessmentReport.Oracle.all.check.source.selection.rules "#CHAP_Tasks.AssessmentReport.Oracle.all.check.source.selection.rules")
- [Validate
  that target foreign key constraints are disabled for migration](#CHAP_Tasks.AssessmentReport.Oracle.target.foreign.key.constraints.check "#CHAP_Tasks.AssessmentReport.Oracle.target.foreign.key.constraints.check")
- [Validate that
  the Oracle database and AWS DMS versions are compatible](#CHAP_Tasks.AssessmentReport.Oracle.dms.compatibility.version.check "#CHAP_Tasks.AssessmentReport.Oracle.dms.compatibility.version.check")
- [Validate that
  secondary constraints and indexes (non-primary) are present in the source database](#CHAP_Tasks.AssessmentReport.Oracle.all.check.secondary.constraints "#CHAP_Tasks.AssessmentReport.Oracle.all.check.secondary.constraints")
- [Validate that session timeout
  settings (IDLE_TIME) are set to UNLIMITED](#CHAP_Tasks.AssessmentReport.Oracle.check.idle.time "#CHAP_Tasks.AssessmentReport.Oracle.check.idle.time")
- [Validate that
  the AWS DMS user has all required permissions on the source database](#CHAP_Tasks.AssessmentReport.Oracle.validate.permissions.on.source "#CHAP_Tasks.AssessmentReport.Oracle.validate.permissions.on.source")
- [Validate that
  XMLTYPE or LOB columns exist when Oracle LogMiner is used](#CHAP_Tasks.AssessmentReport.Oracle.update.lob.columns "#CHAP_Tasks.AssessmentReport.Oracle.update.lob.columns")

##

Validate that limited LOB mode only is used when `BatchApplyEnabled` is enabled

**API key:** `oracle-batch-apply-lob-mode`

This premigration assessment validates whether tables in the DMS task includes LOB columns. If LOB columns are
included in the scope of the task, you must use `BatchApplyEnabled` together with
limited LOB mode only.

For more information, see
[Target metadata task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

##

Validate if tables on the source has columns without scale specified for the Number data type

**API key:** `oracle-number-columns-without-scale`

This premigration assessment validates whether the DMS task includes columns of NUMBER data type without
scale specified. We recommend that you set the endpoint setting `NumberDataTypeScale` to the value specified
in the assessment report.

For more information, see
[Endpoint settings when using Oracle as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.ConnectionAttrib "CHAP_Source.md#CHAP_Source.Oracle.ConnectionAttrib").

##

Validate triggers on the target database

**API key:** `oracle-target-triggers-are-enabled`

This premigration assessment validates whether triggers are enabled on the target database. The assessment will fail if triggers are enabled. We
recommend that you disable or remove the triggers during the migration.

For more information, see
[For more information, see DMS best practices](CHAP_BestPractices.md "CHAP_BestPractices.md").

##

Validate if source has archivelog `DEST_ID` set to 0

**API key:** `oracle-zero-archive-log-dest-id`

This premigration assessment validates whether endpoint extra connection attribute
`useZeroDestid=true` is set for source if archived log `DEST_ID` is set to 0.

For more information, see
[How to handle AWS DMS replication when used with Oracle database in fail-over scenarios](https://aws.amazon.com/blogs/database/how-to-handle-aws-dms-replication-when-used-with-oracle-database-in-fail-over-scenarios/ "https://aws.amazon.com/blogs/database/how-to-handle-aws-dms-replication-when-used-with-oracle-database-in-fail-over-scenarios/").

##

Validate if secondary indexes are enabled on the target database during full-load

**API key:** `oracle-check-secondary-indexes`

This premigration assessment validates whether secondary indexes are enabled during a full-load on the target database.
We recommend that you disable or remove the secondary indexes during full-load.

For more information,
[Best practices for AWS Database Migration Service](CHAP_BestPractices.md "CHAP_BestPractices.md").

##

Validate if tables used in the DMS task scope with BatchApplyEnabled have more than 999 columns

**API key:** `oracle-batch-apply-lob-999`

Tables with batch optimized apply mode enabled can't have more than a total of 999 columns.
Tables that have more than 999 columns will cause AWS DMS to process the batch one by one, which increases latency.
DMS uses the formula **2 \* columns_in_original_table + columns_in_primary_key <= 999**
to calculate the total number of columns per table supported in batch-optimized apply mode.

For more information, see
[Limitations on Oracle as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.Oracle.Limitations "CHAP_Target.md#CHAP_Target.Oracle.Limitations").

## Check supplemental logging on database level

**API key:** `oracle-supplemental-db-level`

This premigration assessment validates if minimum supplemental logging is enabled at the database level.
You must enable supplemental logging to use an Oracle database as a source for migration.

To enable supplemental logging, use the following query:

```
ALTER DATABASE ADD SUPPLEMENTAL LOG DATA
```

For more information, see
[Setting up supplemental logging](CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Configuration.SupplementalLogging "CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.Configuration.SupplementalLogging").

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

## Validate if required DB link is created for Standby

**API key:** `oracle-validate-standby-dblink`

This premigration assessment validates if Dblink is created for the Oracle standby database source. AWSDMS_DBLINK is a
prerequisite for using a standby database as a source. When using Oracle Standby as a source,
AWS DMS does not validate open transactions by default.

For more information, see
[Working with a self-managed Oracle
database as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Self-Managed "CHAP_Source.md#CHAP_Source.Oracle.Self-Managed").

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

## Oracle validation for LOB datatype and if binary reader is configured

**API key:** `oracle-binary-lob-source-validation`

This premigration assessment validates if Oracle LogMiner is used for an Oracle database endpoint version 12c or later.
AWS DMS does not support Oracle LogMiner for migrations of LOB columns from Oracle databases version 12c. This assessment
also checks for the presence of LOB columns and provides appropriate recommendations.

To configure your migration to not use Oracle LogMiner, add the following configuration to your source endpoint:

```
useLogMinerReader=N;useBfile=Y;
```

For more information, see
[Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

## Validate if the database is CDB

**API key:** `oracle-validate-cdb`

This premigration assessment validates if the database is a container database.
AWS DMS doesn't support the multi-tenant container root database (CDB$ROOT).

###### Note

This assessment is only required for Oracle versions 12.1.0.1 or later. This assessment
is not applicable for Oracle versions prior to 12.1.0.1.

For more information, see
[Limitations on using Oracle as a
source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Limitations "CHAP_Source.md#CHAP_Source.Oracle.Limitations").

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

## Check the Oracle Database Edition

**API key:** `oracle-check-cdc-support-express-edition`

This premigration assessment validates if the Oracle source database is Express Edition. AWS DMS
doesn't support CDC for Oracle Express Edition (Oracle Database XE) version 18.0 and later.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

## Validate Oracle CDC method for DMS

**API key:** `oracle-recommendation-cdc-method`

This premigration assessment validates redo log generation for the last seven days, and makes a recommendation
whether to use AWS DMS Binary Reader or Oracle LogMiner for CDC.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information about deciding which CDC method to use, see
[Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

## Validate Oracle RAC configuration for DMS

**API key:** `oracle-check-rac`

This premigration assessment validates if the oracle database is a Real Application Cluster. Real Application Cluster databases
must be configured correctly. If the database is based on RAC, we recommend that you use AWS DMS Binary Reader for CDC
rather than Oracle LogMiner.

This assessment is only valid for a full-load and CDC migration, or a CDC-only migration. This assessment is not
valid for a full-load only migration.

For more information, see
[Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

## Validate if DMS user has permissions on target

**API key:** `oracle-validate-permissions-on-target`

This premigration assessment validates whether DMS users have all the required permissions on the target database.

## Validate if supplemental logging is

required for all columns

**API key:** `oracle-validate-supplemental-logging-all-columns`

This premigration assessment validates, for the tables mentioned in the task scope, whether supplemental
logging has been added to all columns of tables without a primary or unique key. Without supplemental
logging on all columns for a table lacking a primary or unique key, the before-and-after image of the data
won't be available in the redo logs. DMS requires supplemental logging for tables without a primary or
unique key to generate DML statements.

## Validate if supplemental

logging is enabled on tables with Primary or Unique keys

**API key:** `oracle-validate-supplemental-logging-for-pk`

This premigration assessment validates whether supplemental logging is enabled for tables with a primary
key or unique index and also checks if `AddSupplementalLogging` is enabled at the endpoint level.
To ensure DMS can replicate changes, you can either manually add supplemental logging on the table level
based on the primary key or unique key or utilize the endpoint setting `AddSupplementalLogging = true`
with a DMS user having the ALTER permission on any replicated table.

## Validate if there are SecureFile LOBs and the task is

configured for Full LOB mode

**API key:** `oracle-validate-securefile-lobs`

This premigration assessment checks for the presence of SecureFile LOBs in tables within the
task scope and verifies their LOB settings. It's important to note that SecureFile LOBs are
currently supported only during FULL LOB mode. Consider assigning LOB tables to a separate task
to enhance performance, as running tasks in full LOB mode may result in slower performance.

## Validate whether Function-Based

Indexes are being used within the tables included in the task scope.

**API key:** `oracle-validate-function-based-indexes`

This premigration assessment checks for function-based indexes on tables within the task scope.
Note that AWS DMS doesn't support replicating function-based indexes. Consider creating the indexes
after your migration on your target database.

## Validate whether global

temporary tables are being used on the tables included in the task scope.

**API key:** `oracle-validate-global-temporary-tables`

This premigration assessment checks whether global temporary tables are used within the task
table-mapping scope. Note that AWS DMS doesn't support migrating or replicating global temporary tables.

## Validate whether

index-organized tables with an overflow segment are being used on the tables included in the task scope.

**API key:** `oracle-validate-iot-overflow-segments`

Validate whether index-organized tables with an overflow segment are being used on the tables
included in the task scope. AWS DMS doesn't support CDC for index-organized tables with an overflow segment.

## Validate if multilevel nesting

tables are used on the tables included in the task scope.

**API key:** `oracle-validate-more-than-one-nesting-table-level`

This premigration assessment checks the nesting level of the nested table used on the task scope.
AWS DMS supports only one level of table nesting.

## Validate if invisible columns are

used on the tables included in the task scope.

**API key:** `oracle-validate-invisible-columns`

This premigration assessment validates whether the tables used in the task scope have invisible columns.
AWS DMS doesn't migrate data from invisible columns in your source database. To migrate the columns that
are invisible, you need to modify them to be visible.

## Validate if materialized views based on

a ROWID column are used on the tables included in the task scope.

**API key:** `oracle-validate-rowid-based-materialized-views`

This premigration assessment validates whether the materialized views used in the migration are created
based on the ROWID column. AWS DMS doesn't support the ROWID data type or materialized views based on a ROWID column.

## Validate if Active Data Guard DML

Redirect feature is used.

**API key:** `oracle-validate-adg-redirect-dml`

This premigration assessment validates whether the Active Data Guard DML Redirect feature is used.
When using Oracle 19.0 as the source, AWS DMS doesn't support the Data Guard DML Redirect feature.

## Validate if Hybrid Partitioned

Tables are used.

**API key:** `oracle-validate-hybrid-partitioned-tables`

This premigration assessment validates whether hybrid partitioned tables are used for the tables
defined in the task scope.

## Validate if schema-only Oracle

accounts are used

**API key:** `oracle-validate-schema-only-accounts`

This premigration assessment validates whether Schema-Only Accounts are found within the task scope.

## Validate if Virtual Columns are used

**API key:** `oracle-validate-virtual-columns`

This premigration assessment validates whether the Oracle Instance has Virtual Columns in tables within the task scope.

## Validate whether table names defined in the task

scope contain apostrophes.

**API key:** `oracle-validate-names-with-apostrophes`

This premigration assessment validates whether the tables used in the task scope contain apostrophes.
AWS DMS doesn't replicate tables with names containing apostrophes. If identified, consider renaming such tables.
Alternatively, you could create a view or materialized view without apostrophes to load these tables.

## Validate whether the

columns defined in the task scope have
`XMLType`, `Long`, or `Long Raw` datatypes and verify the LOB mode configuration in the task settings.

**API key:** `oracle-validate-limited-lob-mode-for-longs`

This premigration assessment validates whether the tables defined in the task scope have the
datatypes `XMLType`, `Long`, or `Long Raw`, and checks if the task setting
is configured to use Limited Size LOB Mode. AWS DMS doesn't support replicating these datatypes using FULL LOB
mode. Consider changing the task setting to use Limited Size LOB mode upon identifying tables with such datatypes.

## Validate whether the source Oracle

version is supported by AWS DMS.

**API key:** `oracle-validate-supported-versions-of-source`

This premigration assessment validates if the source Oracle instance version is supported by AWS DMS.

## Validate whether the target Oracle

version is supported by AWS DMS.

**API key:** `oracle-validate-supported-versions-of-target`

This premigration assessment validates if the target Oracle instance version is supported by AWS DMS.

## Validate whether the DMS user has the

required permissions to use data validation.

**API key:** `oracle-prerequisites-privileges-of-validation-feature`

This premigration assessment validates whether the DMS user has the necessary privileges to use
DMS Data Validation. You can ignore enabling this validation if you do not intend to use data validation.

## Validate if the DMS user has permissions

to use Binary Reader with Oracle ASM

**API key:** `oracle-prerequisites-privileges-of-binary-reader-asm`

This premigration assessment validates whether the DMS user has the necessary privileges to use
Binary Reader on the Oracle ASM instance. You can ignore enabling this assessment if your source
is not an Oracle ASM instance or if you are not using Binary Reader for CDC.

## Validate if the DMS user has permissions

to use Binary Reader with Oracle non-ASM

**API key:** `oracle-prerequisites-privileges-of-binary-reader-non-asm`

This premigration assessment validates whether the DMS user has the necessary privileges to use
Binary Reader on the Oracle non-ASM instance. This assessment is only valid if you have an Oracle non-ASM instance.

## Validate if the DMS user has permissions to use

Binary Reader with CopyToTempFolder method

**API key:** `oracle-prerequisites-privileges-of-binary-reader-copy-to-temp-folder`

This premigration assessment validates whether the DMS user has the necessary privileges to use
the Binary Reader with the 'Copy to Temp Folder' method. This assessment is relevant only if you are planning to use
CopyToTempFolder to read CDC changes while using the Binary Reader, and have an ASM instance connected to the source.
You can ignore enabling this assessment if you don't intend to use the CopyToTempFolder feature.

We recommend not using the CopyToTempFolder feature because it is deprecated.

## Validate if the DMS user has permissions to

use Oracle Standby as a Source

**API key:** `oracle-prerequisites-privileges-of-standby-as-source`

This premigration assessment validates whether the DMS user has the necessary privileges to use a
StandBy Oracle Instance as a source. You can ignore enabling this assessment if you don't intend to use a
StandBy Oracle Instance as a source.

## Validate if the DMS source is connected

to an application container PDB

**API key:** `oracle-check-app-pdb`

This premigration assessment validates whether the DMS source is connected to an application container PDB.
DMS doesn't support replication from an application container PDB.

## Validate if the table has XML datatypes

included in the task scope.

**API key:** `oracle-check-xml-columns`

This premigration assessment validates whether the tables used in the task scope have XML datatypes.
It also checks if the task is configured for Limited LOB mode when the table contains an XML datatype.
DMS only supports Limited LOB mode for migrating Oracle XML Columns.

## Validate whether archivelog mode is

enabled on the source database.

**API key:** `oracle-check-archivelog-mode`

This premigration assessment validates whether archivelog mode is enabled on the source database.
Enabling archive log mode on the source database is necessary for DMS to replicate changes.

## Validates the archivelog

retention for RDS Oracle.

**API key:** `oracle-check-archivelog-retention-rds`

This premigration assessment validates whether archivelog retention on your RDS Oracle database
is configured for at least 24 hours.

## Validate if the table has

Extended datatypes included in the task scope.

**API key:** `oracle-check-extended-columns`

This premigration assessment validates whether the tables used in the task scope have extended datatypes.
Note that extended datatypes are supported only with DMS version 3.5 onwards.

## Validate the length of the object

name included in the task scope.

**API key:** `oracle-check-object-30-bytes-limit`

This premigration assessment validates whether the length of the object name exceeds 30 bytes.
DMS doesn't support long object names (over 30 bytes).

## Validate if the DMS source is

connected to an Oracle PDB

**API key:** `oracle-check-pdb-enabled`

This premigration assessment validates whether the DMS source is connected to a PDB.
DMS supports CDC only when using the Binary Reader with Oracle PDB as the source.
The assessment also evaluates if the task is configured to use the binary reader when
DMS is connected to Oracle PDB.

## Validate if the table has spatial

columns included in the task scope.

**API key:** `oracle-check-spatial-columns`

This premigration assessment validates whether the table has spatial columns included in the task scope.
DMS supports Spatial datatypes only using Full LOB mode. The assessment also evaluates whether the task
is configured to use Full LOB mode when DMS identifies spatial columns.

## Validate if the DMS source is connected

to an Oracle standby.

**API key:** `oracle-check-standby-db`

This premigration assessment validates whether the source is connected to an Oracle standby.
DMS supports CDC only when using the binary reader with Oracle Standby as the source. The
assessment also evaluates if the task is configured to use binary reader when DMS
is connected to Oracle Standby.

## Validate if the source

database tablespace is encrypted using TDE.

**API key:** `oracle-check-tde-enabled`

This premigration assessment validates whether the source has TDE Encryption enabled on the tablespace.
DMS supports TDE only with encrypted tablespaces when using Oracle LogMiner for RDS Oracle.

## Validates if the source database

uses Automatic Storage Management (ASM)

**API key:** `oracle-check-asm`

This premigration assessment detects if your source database uses ASM. For optimal performance,
configure Binary Reader with `parallelASMReadThreads` and `readAheadBlocks`
parameters in your endpoint settings. These settings enhance data extraction performance when working
with ASM storage

For more information, see [Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

## Validate if batch apply is

enabled and whether the table on the target Oracle database has parallelism enabled at the
table or index level

**API key:**
`oracle-check-degree-of-parallelism`

AWS DMS validates that the table in the target database has any parallelism
enabled. Having parallelism enabled on the target database causes the batch
process to fail. Therefore, it is required to disable parallelism at the table
or index level when using the batch apply feature.

## Recommend

“Bulk Array Size” parameter by validating the tables in the task
scope

**API key:**
`oracle-check-bulk-array-size`

This assessment recommends setting the `BulkArraySize` ECA (Extra
Connection Attribute) if there are no tables with LOB (Large Object) data types
found within the task scope. Setting the `BulkArraySize` ECA can
improve performance of the full load phase of the migration. You can set the
bulk array size using the ECA on the Source/Target endpoint to get optimal
performance during the full load phase of the migration.

## Validate if HandleCollationDiff task setting is Configured

**API key:**
`oracle-check-handlecollationdiff`

This assessment validates if DMS task is configured for validation and
recommend `HandleCollationDiff` task setting to avoid any incorrect
validation results while validating data between Oracle and PostgreSQL.

For more information, see [Data
validation task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

## Validate if

table has primary key or unique index and its state is VALID when DMS
validation is enabled

**API key:**
`oracle-check-pk-validity`

Data validation requires that the table has a primary key or unique index on
both source and target.

For more information, see [AWS DMS data validation](CHAP_Validating.md "CHAP_Validating.md").

## Validate if

Binary Reader is used for Oracle Standby as a source

**API key:**
`oracle-check-binary-reader`

This assessment validates if the source database is a standby database and is
using the Binary Reader for Change Data Capture (CDC).

For more information, see [Using an Oracle database as a source for
AWS DMS](CHAP_Source.md "CHAP_Source.md").

## Validate if the AWS DMS user has the required directory permissions to

replicate data from an Oracle RDS Standby database.

**API key:**
`oracle-check-directory-permissions`

This assessment validates if the AWS DMS user has the required read privileges
on the `ARCHIVELOG_DIR_%` and `ONLINELOG_DIR_%`
directories when the source database is an Oracle RDS Standby.

For more information, see [Working with an AWS-managed
Oracle database as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed "CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed").

## Validate the type of Oracle Standby used for replication

**API key:**
`oracle-check-physical-standby-with-apply`

This assessment validates the type of Oracle standby database used for the
AWS DMS replication. AWS DMS only supports Physical standby databases, which must be
opened in Read Only mode with the redo logs being applied automatically. AWS DMS
does not support Snapshot or Logical standby databases for replication.

For more information, see [Using a
self-managed Oracle Standby as a source with Binary Reader for CDC in
AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.BinaryStandby "CHAP_Source.md#CHAP_Source.Oracle.Self-Managed.BinaryStandby").

## Validate if

required directories are created for RDS Oracle standby

**API key:**
`oracle-check-rds-standby-directories`

This assessment validates if the required oracle directories are created for
archive logs and online logs on the RDS Standby instance.

For more information, see [Using an Amazon RDS
Oracle Standby (read replica) as a source with Binary Reader for CDC in
AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed.StandBy "CHAP_Source.md#CHAP_Source.Oracle.Amazon-Managed.StandBy").

## Validate if

Primary Key or Unique Index exists on target for Batch Apply

**API key:**
`oracle-check-batch-apply-target-pk-ui-absence`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on
the target table. Tables without Primary Keys or Unique Indexes causes the batch
to fail, and changes are processed one by one. It is advisable to move such
tables to their own tasks and utilize transactional apply mode instead.
Alternatively, you can create a unique key on the target table.

For more information, see [Using an Oracle database as a target for
AWS Database Migration Service](CHAP_Target.md "CHAP_Target.md").

## Validate if both Primary Key and Unique index exist on target for Batch

Apply

**API key:**
`oracle-check-batch-apply-target-pk-ui-simultaneously`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on
the target table. Tables with Primary Keys and Unique Indexes simultaneously
causes the batch to fail, and changes are processed one by one. It is advisable
to move such tables to their own tasks and utilize transactional apply mode
instead. Alternatively, you can drop a unique key(s) or primary key on the
target table and rebuild it if you are doing migration.

For more information, see [Using an Oracle database as a target for
AWS Database Migration Service](CHAP_Target.md "CHAP_Target.md").

## Validate if

unsupported HCC levels are used for Full Load

**API key:**
`oracle-check-binary-reader-hcc-full-load`

The Oracle source endpoint is configured to use Binary Reader, the Query Low
level of the HCC compression method is supported for full-load tasks
only.

For more information, see [Supported compression methods for
using Oracle as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Compression "CHAP_Source.md#CHAP_Source.Oracle.Compression").

## Validate if

unsupported HCC levels are used for Full Load with CDC

**API key:**
`oracle-check-binary-reader-hcc-full-load-and-cdc`

The Oracle source endpoint is configured to use Binary Reader, HCC with Query
low is supported for Full Load task only.

[Supported compression methods for
using Oracle as a source for AWS DMS](CHAP_Source.md#CHAP_Source.Oracle.Compression "CHAP_Source.md#CHAP_Source.Oracle.Compression")

## Validate

if unsupported HCC compression used for CDC

**API key:**
`oracle-check-binary-reader-hcc-cdc`

The Oracle source endpoint is configured to use Binary Reader. Binary Reader
doesn't support Query low for tasks with CDC.

For more information, see [Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

## CDC

Recommendation based on source compression method

**API key:**
`oracle-recommend-cdc-method-by-compression`

Compressed objects are detected. Please navigate into the Result section of
the specific assessment for further recommendation.

For more information, see [Using Oracle LogMiner or AWS DMS Binary
Reader for CDC](CHAP_Source.md#CHAP_Source.Oracle.CDC "CHAP_Source.md#CHAP_Source.Oracle.CDC").

## Check if

batch apply is enabled and validate whether the table has more than 999
columns

**API key:**
`oracle-batch-apply-lob-999`

DMS uses the `2 * columns_in_original_table +
 columns_in_primary_key` formula to determine the number of columns on
customer table. Based on this formula, we have identified tables with more than
999 columns. This impacts the batch process, causing it to fail and switch to
one-by-one mode.

For more information, see [Limitations on Oracle as a target
for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.Oracle.Limitations "CHAP_Target.md#CHAP_Target.Oracle.Limitations").

## Check

Transformation Rule for Digits Randomize

**API key**:
`oracle-datamasking-digits-randomize`

This assessment validates whether columns used in table mappings are
compatible with the Digits Randomize transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying digits randomize
transformations does not guarantee any uniqueness.

## Check

Transformation Rule for Digits mask

**API key**:
`oracle-datamasking-digits-mask`

This assessment validates whether any columns used in the table mapping are
not supported by the Digits Mask transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying Digits Mask
transformations to such columns could cause DMS task failures since uniqueness
cannot be guaranteed.

## Check

Transformation Rule for Hashing mask

**API key**:
`oracle-datamasking-hash-mask`

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

## Verify that

Data Validation task settings and Data Masking Hashing mask are not enabled
simultaneously

**API key**:
`all-to-all-validation-with-datamasking-hash-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Hashing mask are not simultaneously enabled, as these features are
incompatible.

## Verify that

Data Validation task settings and Data Masking Digit mask are not enabled
simultaneously

**API key**:
`all-to-all-validation-with-digit-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit mask are not simultaneously enabled, as these features are
incompatible.

## Validate

that replication to a streaming target does not include LOBs or extended
data type columns

**API key**:
`oracle-validate-lob-to-streaming-target`

This assessment identifies potential data loss when migrating LOB or extended
data types to streaming target endpoints (such as S3, Kinesis, or Kafka). Oracle
database does not track changes to these data types in its log files causing DMS
to write `NULL` values to the streaming target. To prevent data loss,
you can implement a '`before`' trigger on the source database which
forces Oracle to log these changes.

## Validate that

CDC-only task is configured to use the `OpenTransactionWindow` endpoint
setting

**API key**:
`oracle-check-cdc-open-tx-window`

For CDC-only tasks, use `OpenTransactionWindow` to avoid missing data. For more
information, see [Creating tasks for ongoing replication using
AWS DMS](CHAP_Task.md "CHAP_Task.md").

## Validate

that at least one selected object exists in the source database

**API key**:
`all-check-source-selection-rules`

This premigration assessment verifies that at least one object specified in the selection rules
exists in the source database, including pattern matching for wildcard-based rules.

## Validate

that target foreign key constraints are disabled for migration

**API key**:
`oracle-target-foreign-key-constraints-check`

This premigration assessment detects active foreign key constraints on the target database that
can cause migration failures (ORA-02291).

## Validate that

the Oracle database and AWS DMS versions are compatible

**API key**:
`oracle-dms-compatibility-version-check`

This premigration assessment detects if your Oracle database version is incompatible with your
AWS DMS version. This mismatch can cause task failures due to unsupported Oracle Redo compatibility
settings.

## Validate that

secondary constraints and indexes (non-primary) are present in the source database

**API key**:
`all-check-secondary-constraints`

This premigration assessment verifies that secondary constraints and indexes (foreign keys,
check constraints, non-clustered indexes) are present in the source database.

## Validate that session timeout

settings (`IDLE_TIME`) are set to `UNLIMITED`

**API key**:
`oracle-check-idle-time`

This premigration assessment verifies that the Oracle database `IDLE_TIME` parameter
is set to `UNLIMITED` for the AWS DMS user. Limited session timeout can cause migration
task failures due to connection timeouts.

## Validate that

the AWS DMS user has all required permissions on the source database

**API key**:
`oracle-validate-permissions-on-source`

This premigration assessment verifies that the AWS DMS user has been configured with all required
permissions on the source database.

## Validate that

`XMLTYPE` or LOB columns exist when Oracle LogMiner is used

**API key**:
`oracle-update-lob-columns`

This premigration assessment warns that `XMLTYPE` or LOB columns exist in the
source database when Oracle LogMiner is used.
