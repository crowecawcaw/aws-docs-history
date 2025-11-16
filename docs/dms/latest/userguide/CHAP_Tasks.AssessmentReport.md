# PostgreSQL assessments

This section describes individual premigration assessments for migration tasks that use a PostgreSQL source endpoint.

###### Topics

- [Validate if DDL event trigger is set to ENABLE ALWAYS](#CHAP_Tasks.AssessmentReport.PG.DDLEventTrigger "#CHAP_Tasks.AssessmentReport.PG.DDLEventTrigger")
- [Validate if PostGIS columns exist in the source database](#CHAP_Tasks.AssessmentReport.PG.PostGISColumns "#CHAP_Tasks.AssessmentReport.PG.PostGISColumns")
- [Validate if foreign key constraint is disabled on the target tables during the full-load process](#CHAP_Tasks.AssessmentReport.PG.ForeignKeyConstraintDisabled "#CHAP_Tasks.AssessmentReport.PG.ForeignKeyConstraintDisabled")
- [Validate if tables with similar names exist](#CHAP_Tasks.AssessmentReport.PG.ValidateSimilarNames "#CHAP_Tasks.AssessmentReport.PG.ValidateSimilarNames")
- [Validate if there are tables with ARRAY data type without a primary key](#CHAP_Tasks.AssessmentReport.PG.ValidateArrayWithoutPrimaryKey "#CHAP_Tasks.AssessmentReport.PG.ValidateArrayWithoutPrimaryKey")
- [Validate if primary keys or unique indexes exist on the target tables when BatchApplyEnabled is enabled](#CHAP_Tasks.AssessmentReport.PG.PrimaryKeysUniqueIndexes "#CHAP_Tasks.AssessmentReport.PG.PrimaryKeysUniqueIndexes")
- [Validate if any table of the target database has
  secondary indexes for the full-load migration task](#CHAP_Tasks.AssessmentReport.PG.TargetDatabaseSecondaryIndexes "#CHAP_Tasks.AssessmentReport.PG.TargetDatabaseSecondaryIndexes")
- [Validate that limited LOB mode only is used
  when BatchApplyEnabled is set to true](#CHAP_Tasks.AssessmentReport.PG.LimitedLOBMode "#CHAP_Tasks.AssessmentReport.PG.LimitedLOBMode")
- [Validate if source database version is supported by DMS for migration](#CHAP_Tasks.AssessmentReport.PG.SourceVersion "#CHAP_Tasks.AssessmentReport.PG.SourceVersion")
- [Validate the logical_decoding_work_mem
  parameter on the source database](#CHAP_Tasks.AssessmentReport.PG.LogicalDecoding "#CHAP_Tasks.AssessmentReport.PG.LogicalDecoding")
- [Validate whether the source
  database has any long running transactions](#CHAP_Tasks.AssessmentReport.PG.LongRunning "#CHAP_Tasks.AssessmentReport.PG.LongRunning")
- [Validate the source database parameter max_slot_wal_keep_size](#CHAP_Tasks.AssessmentReport.PG. "#CHAP_Tasks.AssessmentReport.PG.")
- [Check if the source database parameter
  postgres-check-maxwalsenders is set to support CDC.](#CHAP_Tasks.AssessmentReport.PG.MaxWalSenders "#CHAP_Tasks.AssessmentReport.PG.MaxWalSenders")
- [Check if the source database is configured
  for PGLOGICAL](#CHAP_Tasks.AssessmentReport.PG.pglogical "#CHAP_Tasks.AssessmentReport.PG.pglogical")
- [Validate if the source table primary key is of LOB Datatype](#CHAP_Tasks.AssessmentReport.PG.pklob "#CHAP_Tasks.AssessmentReport.PG.pklob")
- [Validate if the source table has a primary key](#CHAP_Tasks.AssessmentReport.PG.pk "#CHAP_Tasks.AssessmentReport.PG.pk")
- [Validate if prepared transactions
  are present on the source database](#CHAP_Tasks.AssessmentReport.PG.preparedtransactions "#CHAP_Tasks.AssessmentReport.PG.preparedtransactions")
- [Validate if wal_sender_timeout is set
  to a minimum required value to support DMS CDC](#CHAP_Tasks.AssessmentReport.PG.waltime "#CHAP_Tasks.AssessmentReport.PG.waltime")
- [Validate if wal_level is
  set to logical on the source database](#CHAP_Tasks.AssessmentReport.PG.wallevel "#CHAP_Tasks.AssessmentReport.PG.wallevel")
- [Validate if both
  Primary Key and Unique index exist on target for Batch Apply](#CHAP_Tasks.AssessmentReport.PG.batchapply "#CHAP_Tasks.AssessmentReport.PG.batchapply")
- [Recommend Max LOB
  setting when LOB objects are found](#CHAP_Tasks.AssessmentReport.PG.lobsize "#CHAP_Tasks.AssessmentReport.PG.lobsize")
- [Validate if table
  has primary key or unique index and its state is well when DMS validation is
  enabled](#CHAP_Tasks.AssessmentReport.PG.pkvalidity "#CHAP_Tasks.AssessmentReport.PG.pkvalidity")
- [Validate if
  AWS DMS user has necessary privileges to the target](#CHAP_Tasks.AssessmentReport.PG.targetprivileges "#CHAP_Tasks.AssessmentReport.PG.targetprivileges")
- [Validates
  availability of free replication slots for CDC](#CHAP_Tasks.AssessmentReport.PG.slotscount "#CHAP_Tasks.AssessmentReport.PG.slotscount")
- [Verify DMS
  User Full Load Permissions](#CHAP_Tasks.AssessmentReport.PG.object.privileges "#CHAP_Tasks.AssessmentReport.PG.object.privileges")
- [Check
  Transformation Rule for Digits Randomize](#CHAP_Tasks.AssessmentReport.PG.digits.randomize "#CHAP_Tasks.AssessmentReport.PG.digits.randomize")
- [Check
  Transformation Rule for Digits mask](#CHAP_Tasks.AssessmentReport.PG.digits.mask "#CHAP_Tasks.AssessmentReport.PG.digits.mask")
- [Check Transformation Rule
  for Hashing mask](#CHAP_Tasks.AssessmentReport.PG.hash.mask "#CHAP_Tasks.AssessmentReport.PG.hash.mask")
- [Verify that
  Data Validation task settings and Data Masking Digit randomization are not
  enabled simultaneously](#CHAP_Tasks.AssessmentReport.PG.all.digit.random "#CHAP_Tasks.AssessmentReport.PG.all.digit.random")
- [Verify that Data
  Validation task settings and Data Masking Hashing mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.PG.all.hash.mask "#CHAP_Tasks.AssessmentReport.PG.all.hash.mask")
- [Verify that Data
  Validation task settings and Data Masking Digit mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.PG.all.digit.mask "#CHAP_Tasks.AssessmentReport.PG.all.digit.mask")

## Validate if DDL event trigger is set to ENABLE ALWAYS

**API key:** `postgres-check-ddl-event-trigger`

This premigration assessment validates whether the DDL event trigger is set to `ENABLE ALWAYS`. When your source database is also a target for another third–party replication system,
DDL changes might not migrate during CDC. This situation can prevent DMS from triggering the the `awsdms_intercept_ddl` event.
To work around the situation, modify the trigger on your source database like in the follwoing example:

```
alter event trigger awsdms_intercept_ddl enable always;
```

For more information, see
[Limitations on using a PostgreSQL database as a DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations "CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations").

## Validate if PostGIS columns exist in the source database

**API key:** `postgres-check-postgis-data-type`

This premigration assessment validates whether the columns of PostGIS data type that exist in case source and target engines are different. AWS DMS supports the PostGIS data type only
for homogeneous (like-to-like) migrations.

For more information, see
[Limitations on using a PostgreSQL database as a DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations "CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations").

## Validate if foreign key constraint is disabled on the target tables during the full-load process

**API key:** `postgres-check-session-replication-role`

This premigration assessment validates whether the `session_replication_role parameter` is set to `REPLICA` on the target to disable foreign key constraints during full-load phase.
For full-load migration types, you should disabled foreign key constraints.

For more information about PostgreSQL endpoint limitations, see
[Using a PostgreSQL database as a target for AWS Database Migration Service](CHAP_Target.md "CHAP_Target.md").

## Validate if tables with similar names exist

**API key:** `postgres-check-similar-table-name`

This premigration assessment validates whether there are tables with similar names on the source. Having
multiple tables with the same name written in different case can cause unpredictable behaviors during replication.

For more information about PostgreSQL endpoint limitations, see
[Limitations on using a PostgreSQL database as a DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations "CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations").

## Validate if there are tables with ARRAY data type without a primary key

**API key:** `postgres-check-table-with-array`

This premigration assessment validates whether there are tables with array data type without a primary key. A table with an `ARRAY`
data type missing a primary key is ignored during the full-load.

For more information about PostgreSQL endpoint limitations, see
[Limitations on using a PostgreSQL database as a DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations "CHAP_Source.md#CHAP_Source.PostgreSQL.Limitations").

## Validate if primary keys or unique indexes exist on the target tables when BatchApplyEnabled is enabled

**API key:** `postgres-check-batch-apply-target-pk-ui-absence`

Batch apply is only supported on tables with primary keys or unique indexes on the target table. Tables without primary keys
or unique indexes will cause the batch to fail, and AWS DMS will process the changes one by one. We recommend that you create separate tasks for such tables and use transactional
apply mode instead. Alternatively, you can create a unique key on the target table.

For more information, see
[Using a PostgreSQL database as a target for AWS Database Migration Service](CHAP_Target.md "CHAP_Target.md").

## Validate if any table of the target database has

secondary indexes for the full-load migration task

**API key:** `postgres-check-target-secondary-indexes`

This premigration assessment validates whether there are tables with secondary indexes in the scope of the
full-load migration task. We recommend that you drop the secondary indexes for the duration of the full-load task.

For more information, see
[Using a PostgreSQL database as a target for AWS Database Migration Service](CHAP_Target.md "CHAP_Target.md").

## Validate that limited LOB mode only is used

when BatchApplyEnabled is set to true

**API key:** `postgres-batch-apply-lob-mode`

When LOB columns are included in the replication, you can use `BatchApplyEnabled` in limited LOB mode only.
Using other options of the LOB mode will cause the batch to fail, and AWS DMS will process changes one by one.
We recommend that you move these tables to their own tasks and use transactional apply mode instead.

For more information about the `BatchApplyEnabled` setting, see
[How can I use the DMS batch apply feature to improve CDC replication performance?](https://repost.aws/knowledge-center/dms-batch-apply-cdc-replication "https://repost.aws/knowledge-center/dms-batch-apply-cdc-replication").

## Validate if source database version is supported by DMS for migration

**API key:** `postgres-check-dbversion`

This premigration assessment verifies whether the source database version is compatible with AWS DMS.

## Validate the `logical_decoding_work_mem`

parameter on the source database

**API key:** `postgres-check-for-logical-decoding-work-mem`

This premigration assessment recommends tuning the `logical_decoding_work_mem`
parameter on the source database. On a highly transactional database where you might have long
running transactions or many sub-transactions, it may result in increased logical decoding
memory consumption and the need to spill to disk. This results in high DMS source latency
during replication. In such scenarios, you might need to tune `logical_decoding_work_mem`.
This parameter is supported in PostgreSQL versions 13 and greater.

## Validate whether the source

database has any long running transactions

**API key:** `postgres-check-longrunningtxn`

This premigration assessment verifies whether the source database has any long running
transactions which lasted more than 10 minutes. Starting the task might fail, because by
default, DMS checks for any open transactions while starting the task.

## Validate the source database parameter `max_slot_wal_keep_size`

**API key:** `postgres-check-maxslot-wal-keep-size`

This premigration assessment verifies the value configured for `max_slot_wal_keep_size`.
When `max_slot_wal_keep_size` is set to a non-default value, the DMS task may fail due to
the removal of required WAL files.

## Check if the source database parameter

`postgres-check-maxwalsenders` is set to support CDC.

**API key:** `postgres-check-maxwalsenders`

This premigration assessment verifies the value configured for `max_wal_senders`
on the source database. DMS requires `max_wal_senders` to be set greater than 1 to support
Change Data Capture (CDC).

## Check if the source database is configured

for `PGLOGICAL`

**API key:** `postgres-check-pglogical`

This premigration assessment verifies if the `shared_preload_libraries` value is set
to `pglogical` to support `PGLOGICAL` for CDC. Note that you can ignore this
assessment if you are planning to use test decoding for logical replication.

## Validate if the source table primary key is of LOB Datatype

**API key:** `postgres-check-pk-lob`

This premigration assessment verifies if a table's primary key is of Large Object (LOB) datatype. DMS does not support replication if
the source table has an LOB column as a primary key.

## Validate if the source table has a primary key

**API key:** `postgres-check-pk`

This premigration assessment verifies if primary keys exist for the tables used in the task scope.
DMS doesn’t support replication for tables without primary keys, unless the replica identity is set
to `full` on the source table.

## Validate if prepared transactions

are present on the source database

**API key:** `postgres-check-preparedtxn`

This premigration assessment verifies if there are any prepared transactions present on the
source database. Replication slot creation might stop responding if there are any prepared
transactions on the source database.

## Validate if `wal_sender_timeout` is set

to a minimum required value to support DMS CDC

**API key:** `postgres-check-walsenderstimeout`

This premigration assessment verifies if `wal_sender_timeout` is set to a minimum of
10000 milliseconds (10 seconds). A DMS task with CDC requires a minimum of 10000 milliseconds
(10 seconds), and fails if the value is less than 10000.

## Validate if `wal_level` is

set to logical on the source database

**API key:** `postgres-check-wallevel`

This premigration assessment verifies if `wal_level` is set to logical. For
DMS CDC to work, this parameter needs to be enabled on the source database.

## Validate if both

Primary Key and Unique index exist on target for Batch Apply

**API key:**
`postgres-check-batch-apply-target-pk-ui-simultaneously`

Batch apply is only supported on tables with Primary Keys or Unique Indexes on
the target table. Tables with Primary Keys and Unique Indexes simultaneously
cause the batch to fail, and changes are processed one by one. It is advisable
to move such tables to their own tasks and utilize transactional apply mode
instead. Alternatively, you can drop a unique key(s) or primary key on the
target table and rebuild it if you are doing migration.

For more information, see [Enabling CDC using a
self-managed PostgreSQL database as a AWS DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Prerequisites.CDC "CHAP_Source.md#CHAP_Source.PostgreSQL.Prerequisites.CDC").

## Recommend Max LOB

setting when LOB objects are found

**API key:**
`postgres-check-limited-lob-size`

The LOB Size Calculation for PostgreSQL is different from other Engine. Ensure
you are setting the right Maximum LOB size on your task setting to avoid any
data truncation.

For more information, see [AWS DMS data validation](CHAP_Validating.md "CHAP_Validating.md").

## Validate if table

has primary key or unique index and its state is well when DMS validation is
enabled

**API key:**
`postgres-check-pk-validity`

Data validation requires that the table has a primary key or unique
index.

For more information, see [AWS DMS data validation](CHAP_Validating.md "CHAP_Validating.md").

## Validate if

AWS DMS user has necessary privileges to the target

**API key:**
`postgres-check-target-privileges`

The AWS DMS user must have at least the db_owner user role on the target
database.

For more information, see [Security requirements when using a
PostgreSQL database as a target for AWS Database Migration Service](CHAP_Target.md#CHAP_Target.PostgreSQL.Security "CHAP_Target.md#CHAP_Target.PostgreSQL.Security").

## Validates

availability of free replication slots for CDC

**API key**:
`postgres-check-replication-slots-count`

This assessment validates whether replication slots are available for CDC to
replicate changes.

## Verify DMS

User Full Load Permissions

**API key**:
`postgres-check-select-object-privileges`

This assessment validates whether the DMS user has the necessary SELECT
privileges on tables required for Full Load operations.

## Check

Transformation Rule for Digits Randomize

**API key**:
`postgres-datamasking-digits-randomize`

This assessment validates whether columns used in table mappings are
compatible with the Digits Randomize transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying digits randomize
transformations does not guarantee any uniqueness.

## Check

Transformation Rule for Digits mask

**API key**:
`postgres-datamasking-digits-mask`

This assessment validates whether any columns used in the table mapping are
not supported by the Digits Mask transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying Digits Mask
transformations to such columns could cause DMS task failures since uniqueness
cannot be guaranteed.

## Check Transformation Rule

for Hashing mask

**API key**:
`postgres-datamasking-hash-mask`

This assessment validates whether any of the columns used in the table mapping
are not supported by the Hashing Mask transformation rule. It also checks if the
length of the source column exceeds 64 characters. Ideally, the target column
length should be greater than 64 characters to support hash masking.
Additionally, the assessment checks if any columns selected for transformation
are part of primary keys, unique constraints, or foreign keys, as applying
digits randomize transformations does not guarantee any uniqueness.

## Verify that

Data Validation task settings and Data Masking Digit randomization are not
enabled simultaneously

**API key**:
`all-to-all-validation-with-datamasking-digits-randomize`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit randomization are not simultaneously enabled, as these features
are incompatible.

## Verify that Data

Validation task settings and Data Masking Hashing mask are not enabled
simultaneously

**API key**:
`all-to-all-validation-with-datamasking-hash-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Hashing mask are not simultaneously enabled, as these features are
incompatible.

## Verify that Data

Validation task settings and Data Masking Digit mask are not enabled
simultaneously

**API key**:
`all-to-all-validation-with-digit-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit mask are not simultaneously enabled, as these features are
incompatible.
