# Assessments for all endpoint types

This section describes individual premigration assessments for all endpoint types.

###### Topics

- [Unsupported data types](#CHAP_Tasks.AssessmentReport.Assessments.All.UnsupportedDataTypes "#CHAP_Tasks.AssessmentReport.Assessments.All.UnsupportedDataTypes")
- [Large objects (LOBs) are used but target LOB columns are not nullable](#CHAP_Tasks.AssessmentReport.Assessments.All.LOBsColsNotNullable "#CHAP_Tasks.AssessmentReport.Assessments.All.LOBsColsNotNullable")
- [Source table with Large objects (LOBs) but without primary keys or unique constraints](#CHAP_Tasks.AssessmentReport.Assessments.All.LOBsNoPrimaryKey "#CHAP_Tasks.AssessmentReport.Assessments.All.LOBsNoPrimaryKey")
- [Source table without primary key for CDC or full load and CDC tasks only](#CHAP_Tasks.AssessmentReport.Assessments.All.CDCNoPrimaryKey "#CHAP_Tasks.AssessmentReport.Assessments.All.CDCNoPrimaryKey")
- [Target table without primary keys for CDC tasks only](#CHAP_Tasks.AssessmentReport.Assessments.All.CDCOnlyNoPrimaryKey "#CHAP_Tasks.AssessmentReport.Assessments.All.CDCOnlyNoPrimaryKey")
- [Unsupported source primary key types - composite primary keys](#CHAP_Tasks.AssessmentReport.Assessments.All.CompositeNoPrimaryKey "#CHAP_Tasks.AssessmentReport.Assessments.All.CompositeNoPrimaryKey")

##

Unsupported data types

**API key:** `unsupported-data-types-in-source`

Checks for data types in the source endpoint that DMS doesn't support.
Not all data types can be migrated between engines.

##

Large objects (LOBs) are used but target LOB columns are not nullable

**API key:** `full-lob-not-nullable-at-target`

Checks for the nullability of a LOB column in the target when the replication usese full LOB mode or inline LOB mode.
DMS requires a LOB column to be null when using these LOB modes. This assessment requires the source and target
databases to be relational.

##

Source table with Large objects (LOBs) but without primary keys or unique constraints

**API key:** `table-with-lob-but-without-primary-key-or-unique-constraint`

Checks for the presence of source tables with LOBs but without a primary key or a unique key.
A table must have a primary key or a unique key for DMS to migrate LOBs. This assessment requires
the source database to be relational.

##

Source table without primary key for CDC or full load and CDC tasks only

**API key:** `table-with-no-primary-key-or-unique-constraint`

Checks for the presence of a primary key or a unique key in source tables for a full-load
and change data capture (CDC) migration, or a CDC-only migration. A lack of a primary key
or a unique key can cause performance issues during the CDC migration. This assessment requires
the source database to be relational, and the migration type to include CDC.

##

Target table without primary keys for CDC tasks only

**API key:** `target-table-has-unique-key-or-primary-key-for-cdc`

Checks for the presence of a primary key or a unique key in already-created target tables
for a CDC-only migration. A lack of a primary key or a unique key can cause full table scans
in the target when DMS applies updates and deletes. This can result in performance issues
during the CDC migration. This assessment requires the target database to be relational,
and the migration type to include CDC.

##

Unsupported source primary key types - composite primary keys

**API key:** `unsupported-source-pk-type-for-elasticsearch-target`

Checks for the presence of composite primary keys in source tables when migrating to
Amazon OpenSearch Service. The primary key of the source table must consist of a single column.
This assessment requires the source database to be relational, and the target
database to be DynamoDB.

###### Note

DMS supports migrating a source database to an OpenSearch Service target where the
source primary key consists of multiple columns.
