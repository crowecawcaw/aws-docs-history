# Amazon S3 target data validation

AWS DMS supports validating replicated data in Amazon S3 targets. Because AWS DMS stores replicated
data as flat files in Amazon S3, we use [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") `CREATE TABLE AS SELECT` (CTAS)
queries to validate data.

Queries on data that is stored in Amazon S3 are computationally
intense. Thus, AWS DMS runs validation on Amazon S3 data during
change data capture (CDC) only once a day, at midnight (00:00) UTC. Each daily
validation that AWS DMS runs is called an _interval validation_.
During an interval validation, AWS DMS validates all of the change
records that were migrated to the target Amazon S3 bucket for the previous 24 hours. For more
information about limitations for interval validation, see [Limitations for using S3 target
validation](#CHAP_Validating_S3_limitations "#CHAP_Validating_S3_limitations").

Amazon S3 target validation uses Amazon Athena, so additional costs apply. For more information,
see [Amazon Athena
Pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").

###### Note

S3 target validation requires AWS DMS version 3.5.0 or later.

###### Topics

- [Prerequisites](#CHAP_Validating_S3_prerequisites "#CHAP_Validating_S3_prerequisites")
- [Permissions](#CHAP_Validating_S3_permissions "#CHAP_Validating_S3_permissions")
- [Limitations](#CHAP_Validating_S3_limitations "#CHAP_Validating_S3_limitations")
- [Validation only
  tasks](#CHAP_Validating_S3_only "#CHAP_Validating_S3_only")

## S3 target validation

prerequisites

Before using S3 target validation, check the following settings and permissions:

- Set the `DataFormat` value for your endpoint's [S3Settings](../APIReference/API_S3Settings.md "../APIReference/API_S3Settings.md") to `parquet`. For more information, see [Parquet settings for S3](CHAP_Target.md#CHAP_Target.S3.EndpointSettings.Parquet "CHAP_Target.md#CHAP_Target.S3.EndpointSettings.Parquet").
- Ensure that the role assigned to the user account that was used to create the
  migration task has the correct set of permissions. See [Permissions](#CHAP_Validating_S3_permissions "#CHAP_Validating_S3_permissions") following.

For tasks using ongoing replication (CDC), check the following settings:

- Turn on supplemental logging so you have complete records in the CDC data.
  For information about turning on supplemental
  logging, see [Automatically add supplemental
  logging to an Oracle source endpoint](CHAP_Troubleshooting.md#CHAP_Troubleshooting.Oracle.AutoSupplLogging "CHAP_Troubleshooting.md#CHAP_Troubleshooting.Oracle.AutoSupplLogging") in the [Troubleshooting and diagnostic support](CHAP_Troubleshooting.md "CHAP_Troubleshooting.md") section
  in this guide.
- Set the `TimestampColumnName` parameter for the target endpoint.
  There are no limitations on the timestamp column name. For more information, see
  [S3Settings](../APIReference/API_S3Settings.md "../APIReference/API_S3Settings.md").
- Set up date-based folder partitioning for the target. For more information,
  see [Using date-based folder partitioning](CHAP_Target.md#CHAP_Target.S3.DatePartitioning "CHAP_Target.md#CHAP_Target.S3.DatePartitioning").

## Permissions for using S3 target

validation

To set up access for using S3 target validation, ensure that the role assigned to the
user account that was used to create the migration task has the following set of
permissions. Replace the sample values with your values.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "athena:StartQueryExecution",
 "athena:GetQueryExecution",
 "athena:CreateWorkGroup"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateDatabase",
 "glue:DeleteDatabase",
 "glue:GetDatabase",
 "glue:GetTables",
 "glue:CreateTable",
 "glue:DeleteTable",
 "glue:GetTable"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucketMultipartUploads",
 "s3:AbortMultipartUpload",
 "s3:ListMultipartUploadParts"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Limitations for using S3 target

validation

View the following additional limitations that apply when using S3 target validation.
For limitations that apply to all validations, see [Limitations](CHAP_Validating.md#CHAP_Validating.Limitations "CHAP_Validating.md#CHAP_Validating.Limitations").

- Your `DatePartitionSequence` value needs a Day component. S3 target
  validation does not support the `YYYYMM` format.
- When interval validation is running during CDC, you may see false validation
  errors in the `awsdms_validation_failures_v1` table. These errors
  occur because AWS DMS migrates changes that arrived during the interval validation
  into the next day's partition folder. Normally, these changes are written into
  the current day's partition folder. These false errors are a limitation of
  validating replication from a dynamic source database to a static target, such
  as Amazon S3. To investigate these false errors, check for records near the end of
  the validation window (00:00 UTC), which is when these errors typically appear.

To minimize the number of false errors, ensure that the
`CDCLatencySource` for the task is low. For information about
monitoring latency, see [Replication task metrics](CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task "CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task").

- Tasks in the `failed` or `stopped` state don't validate
  the previous day's changes. To minimize validation errors because of unexpected
  failures, create separate validation only tasks with the same table mappings,
  and source and target endpoints. For more information about validation only
  tasks, see [Using validation only tasks with S3 target
  validation](#CHAP_Validating_S3_only "#CHAP_Validating_S3_only").
- The **Validation Status** column in table statistics reflects
  the state of the most recent interval validation. As a result, a table which has
  mismatches might show up as validated after the next day's interval validation.
  Check the `s3_validation_failures folder` in the target Amazon S3
  bucket for mismatches that occurred more than a day ago.
- S3 Validation uses the bucketed table feature of Amazon Athena. This allows S3
  validation to make a bucketed copy of the target table data. This means that the
  copy of the table data is divided into subsets that match DMS validation's
  internal partitioning. Athena bucketed tables have a limit of 100,000 buckets.
  Any tables that S3 validation attempts to validate that exceed this limit will
  fail validation. The number of buckets that S3 Validation attempts to create is
  equal to the following:

```
(#records in the table) / (validation partition size setting)
```

To work around this limitation, increase the validation partition size setting
so that the number of buckets created by S3 Validation is less than 100,000. For
more information about bucketing, see [Partitioning
and bucketing in Athena](../../../athena/latest/ug/ctas-partitioning-and-bucketing.md "../../../athena/latest/ug/ctas-partitioning-and-bucketing.md") in the _Amazon Athena User
Guide_.

- The table name must not contain special characters except underscore.

S3 Validation uses Amazon Athena which does not support special characters (other
than underscore) in table names. For more information, see
[CREATE TABLE](../../../athena/latest/ug/create-table.md "../../../athena/latest/ug/create-table.md") topic in the _Amazon Athena
User Guide_.

- When AWS DMS data validation feature is used with an Amazon S3 target managed by
  AWS Lake Formation, the validation process fails. This can result in data
  consistency issues.

## Using validation only tasks with S3 target

validation

A _validation only task_ runs validation on data that is to be
migrated without running the migration.

Validation only tasks continue to run, even if the migration task stops, which ensures
that AWS DMS doesn't miss the 00:00 UTC interval validation window.

Using validation only tasks with Amazon S3 target endpoints has the following
limitations:

- Amazon S3 Validation for Full-Load Tasks with the
  Validation
  only setting enabled are supported, but operate differently
  than Full-Load and
  Validation
  only tasks for other endpoints. For S3 as a Target, a task of
  this type validates against only the Full-Load Data in the S3 target, and will
  not validate against any data migrated as part of a CDC migration. Only use this
  feature to validate data created by a Full-Load only task. Using this mode to
  validate data in a target that has an active CDC task running will not produce
  an effective validation.
- Validation only tasks only validate changes since the last interval validation
  window (00:00 UTC). Validation only tasks don't validate full-load data or CDC
  data from previous days.
