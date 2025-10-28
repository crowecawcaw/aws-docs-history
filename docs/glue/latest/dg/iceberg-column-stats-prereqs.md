# Prerequisites for generating column

statistics

To generate or update column statistics for Iceberg tables, the statistics generation
task assumes an AWS Identity and Access Management (IAM) role on your behalf. Based on the permissions granted
to the role, the column statistics generation task can read the data from the Amazon S3 data
store.

When you configure the column statistics generation task, AWS Glue allows you to create a
role that includes the `AWSGlueServiceRole` AWS managed policy plus the
required inline policy for the specified data source.

If you specify an existing role for generating column statistics, ensure that it
includes the `AWSGlueServiceRole` policy or equivalent (or a scoped down
version of this policy), and the required inline policies.

For more information about the required permissions, see [Prerequisites for generating column
statistics](column-stats-prereqs.md "column-stats-prereqs.md").
