# Db2 LUW Assessments

This section describes individual premigration assessments for migration tasks
that use a Db2 LUW source endpoint.

###### Topics

- [Validate if the
  IBM Db2 LUW database is configured to be recoverable.](#CHAP_Tasks.AssessmentReport.Db2.config.param "#CHAP_Tasks.AssessmentReport.Db2.config.param")
- [Validate if
  the DMS user has the required permissions on the source database to perform
  a full-load](#CHAP_Tasks.AssessmentReport.Db2.load.privileges "#CHAP_Tasks.AssessmentReport.Db2.load.privileges")
- [Validate if the
  DMS user has the required permissions on the source database to perform
  CDC](#CHAP_Tasks.AssessmentReport.Db2.cdc.privileges "#CHAP_Tasks.AssessmentReport.Db2.cdc.privileges")
- [Validate if the
  source IBM Db2 LUW source table has Db2 XML data type](#CHAP_Tasks.AssessmentReport.Db2.xml.data.type "#CHAP_Tasks.AssessmentReport.Db2.xml.data.type")
- [Validate if the source IBM Db2 LUW version is supported by AWS DMS](#CHAP_Tasks.AssessmentReport.Db2.supported.version.source "#CHAP_Tasks.AssessmentReport.Db2.supported.version.source")
- [Validate if the target IBM Db2 LUW version is supported by AWS DMS](#CHAP_Tasks.AssessmentReport.Db2.supported.version.target "#CHAP_Tasks.AssessmentReport.Db2.supported.version.target")
- [Check
  Transformation Rule for Digits Randomize](#CHAP_Tasks.AssessmentReport.Db2.digits.randomise "#CHAP_Tasks.AssessmentReport.Db2.digits.randomise")
- [Check
  Transformation Rule for Digits mask](#CHAP_Tasks.AssessmentReport.Db2.digits.mask "#CHAP_Tasks.AssessmentReport.Db2.digits.mask")
- [Check Transformation
  Rule for Hashing mask](#CHAP_Tasks.AssessmentReport.Db2.hash.mask "#CHAP_Tasks.AssessmentReport.Db2.hash.mask")
- [Verify that
  Data Validation task settings and Data Masking Digit randomization are not
  enabled simultaneously](#CHAP_Tasks.AssessmentReport.Db2.all.digits.random "#CHAP_Tasks.AssessmentReport.Db2.all.digits.random")
- [Verify that Data
  Validation task settings and Data Masking Hashing mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.Db2.all.hash.mask "#CHAP_Tasks.AssessmentReport.Db2.all.hash.mask")
- [Verify that
  Data Validation task settings and Data Masking Digit mask are not enabled
  simultaneously](#CHAP_Tasks.AssessmentReport.Db2.all.digit.mask "#CHAP_Tasks.AssessmentReport.Db2.all.digit.mask")
- [Verify that target
  tables have the correct index configuration (Primary Key or Unique Index,
  not both) for Batch Apply compatibility](#CHAP_Tasks.AssessmentReport.Db2.pk.absence "#CHAP_Tasks.AssessmentReport.Db2.pk.absence")
- [Validate that only
  ‘Limited LOB mode’ is used when BatchApplyEnabled is set to
  true](#CHAP_Tasks.AssessmentReport.Db2.lob.mode "#CHAP_Tasks.AssessmentReport.Db2.lob.mode")
- [Validate if
  secondary indexes are disabled on the target database during
  full-load](#CHAP_Tasks.AssessmentReport.secondary.indexes "#CHAP_Tasks.AssessmentReport.secondary.indexes")

## Validate if the

IBM Db2 LUW database is configured to be recoverable.

**API key**:
`db2-check-archive-config-param`

This premigration assessment validates whether the Db2 LUW database has either
or both of the database configuration parameters `LOGARCHMETH1` and
`LOGARCHMETH2` set to **ON**.

## Validate if

the DMS user has the required permissions on the source database to perform
a full-load

**API key**:
`db2-check-full-load-privileges`

This premigration assessment validates whether DMS user has all the required
permissions on the source database for full-load operations.

## Validate if the

DMS user has the required permissions on the source database to perform
CDC

**API key**:
`db2-check-cdc-privileges`

This premigration assessment validates whether DMS user has all the required
permissions on the source database for CDC operations.

## Validate if the

source IBM Db2 LUW source table has Db2 XML data type

**API key**:
`db2-check-xml-data-type`

This premigration assessment validates if the source IBM Db2 LUW table has Db2
XML data type.

## Validate if the source IBM Db2 LUW version is supported by AWS DMS

**API key**:
`db2-validate-supported-versions-source`

This premigration assessment validates if the source IBM Db2 LUW version is
supported by AWS DMS.

## Validate if the target IBM Db2 LUW version is supported by AWS DMS

**API key**:
`db2-validate-supported-versions-target`

This premigration assessment validates if the target IBM Db2 LUW version is
supported by AWS DMS.

## Check

Transformation Rule for Digits Randomize

**API key**:
`db2-datamasking-digits-randomize`

This assessment validates whether columns used in table mappings are
compatible with the Digits Randomize transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying digits randomize
transformations does not guarantee any uniqueness.

## Check

Transformation Rule for Digits mask

**API key**:
`db2-datamasking-digits-mask`

This assessment validates whether any columns used in the table mapping are
not supported by the Digits Mask transformation rule. Additionally, the
assessment checks if any columns selected for transformation are part of primary
keys, unique constraints, or foreign keys, as applying Digits Mask
transformations to such columns could cause DMS task failures since uniqueness
cannot be guaranteed.

## Check Transformation

Rule for Hashing mask

**API key**:
`db2-datamasking-hash-mask`

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

## Verify that

Data Validation task settings and Data Masking Digit mask are not enabled
simultaneously

**API key**:
`all-to-all-validation-with-digit-mask`

This premigration assessment verifies that Data Validation setting and Data
Masking Digit mask are not simultaneously enabled, as these features are
incompatible.

## Verify that target

tables have the correct index configuration (Primary Key or Unique Index,
not both) for Batch Apply compatibility

**API key**:
`db2-check-batch-apply-target-pk-ui-absence`

Batch Apply requires the target tables to have either Primary or Unique keys,
but not both. If a table contains both Primary and Unique Key, the apply mode
changes from batch to transactional.

## Validate that only

‘Limited LOB mode’ is used when `BatchApplyEnabled` is set to
true

**API key**:
`db2-check-for-batch-apply-lob-mode`

This premigration assessment validates whether DMS task includes LOB columns.
If LOB columns are included in the scope of the task, you must use ‘Limited LOB
mode’ in order to be able to use `BatchApplyEnabled=true`.

## Validate if

secondary indexes are disabled on the target database during
full-load

**API key**:
`db2-check-secondary-indexes`

This premigration assessment validates whether secondary indexes are disabled
during a full-load on the target database. You must disable or remove the
secondary indexes during full-load.
