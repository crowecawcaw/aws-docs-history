# Aurora MySQL

Complete the following steps to configure an OpenSearch Ingestion pipeline with Amazon Aurora
for Aurora MySQL.

###### Topics

- [Aurora MySQL prerequisites](#aurora-mysql-prereqs "#aurora-mysql-prereqs")
- [Step 1: Configure the pipeline role](#aurora-mysql-pipeline-role "#aurora-mysql-pipeline-role")
- [Step 2: Create the pipeline](#aurora-mysql-pipeline "#aurora-mysql-pipeline")
- [Data consistency](#aurora-mysql-pipeline-consistency "#aurora-mysql-pipeline-consistency")
- [Mapping data types](#aurora-mysql-pipeline-mapping "#aurora-mysql-pipeline-mapping")
- [Limitations](#aurora-mysql-pipeline-limitations "#aurora-mysql-pipeline-limitations")
- [Recommended CloudWatch Alarms](#aurora-mysql-pipeline-metrics "#aurora-mysql-pipeline-metrics")

## Aurora MySQL prerequisites

Before you create your OpenSearch Ingestion pipeline, perform the following
steps:

1. [Create a custom Aurora DB cluster parameter group in Amazon Aurora to
   configure binary logging](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.parameters").

```
aurora_enhanced_binlog=1
binlog_backup=0
binlog_format=ROW
binlog_replication_globaldb=0
binlog_row_image=full
binlog_row_metadata=full
```

Additionally, make sure the `binlog_transaction_compression`
parameter is not set to `ON`, and that the
`binlog_row_value_options` parameter is not set to
`PARTIAL_JSON`. 2. [Select or create an Aurora MySQL DB cluster](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.md") and associate the
parameter group created in the previous step with the DB cluster. 3. [Configure binary log retention to 24 hours or longer](../../../AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-configuring.md "../../../AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-configuring.md"). 4. Set up username and password authentication on your Amazon Aurora cluster
using [password
management with Aurora and AWS Secrets Manager](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md"). You can also create a
username/password combination by [creating a
Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md"). 5. If you use the full initial snapshot feature, create an AWS KMS key and
an IAM role for exporting data from Amazon Aurora to Amazon S3.

The IAM role should have the following permission policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ExportPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject*",
 "s3:ListBucket",
 "s3:GetObject*",
 "s3:DeleteObject*",
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`s3-bucket-used-in-pipeline`",
 "arn:aws:s3:::`s3-bucket-used-in-pipeline`/*"
 ]
 }
 ]
}`

```

The role should also have the following trust relationships:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "export.rds.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

6. Select or create an OpenSearch Service domain or OpenSearch Serverless collection. For
   more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains "createupdatedomains.md#createdomains") and [Creating collections](serverless-manage.md#serverless-create "serverless-manage.md#serverless-create").
7. Attach a [resource-based policy](ac.md#ac-types-resource "ac.md#ac-types-resource") to your domain or a [data access policy](serverless-data-access.md "serverless-data-access.md") to your collection. These access policies
   allow OpenSearch Ingestion to write data from your Amazon Aurora DB cluster to your
   domain or collection.

## Step 1: Configure the pipeline role

After you have your Amazon Aurora pipeline prerequisites set up, [configure the
pipeline role](pipeline-security-overview.md#pipeline-security-sink "pipeline-security-overview.md#pipeline-security-sink") to use in your pipeline configuration. Also add the
following permissions for Amazon Aurora source to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "allowReadingFromS3Buckets",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:DeleteObject",
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`s3_bucket`",
 "arn:aws:s3:::`s3_bucket`/*"
 ]
 },
 {
 "Sid": "allowNetworkInterfacesActions",
 "Effect": "Allow",
 "Action": [
 "ec2:AttachNetworkInterface",
 "ec2:CreateNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterface",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DetachNetworkInterface",
 "ec2:DescribeNetworkInterfaces"
 ],
 "Resource": [
 "arn:aws:ec2:*:`111122223333`:network-interface/*",
 "arn:aws:ec2:*:`111122223333`:subnet/*",
 "arn:aws:ec2:*:`111122223333`:security-group/*"
 ]
 },
 {
 "Sid": "allowDescribeEC2",
 "Effect": "Allow",
 "Action": [
 "ec2:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "allowTagCreation",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:`111122223333`:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/OSISManaged": "true"
 }
 }
 },
 {
 "Sid": "AllowDescribeInstances",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBInstances"
 ],
 "Resource": [
 "arn:aws:rds:`us-east-2`:`111122223333`:db:*"
 ]
 },
 {
 "Sid": "AllowDescribeClusters",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBClusters"
 ],
 "Resource": [
 "arn:aws:rds:`us-east-2`:`111122223333`:cluster:`DB-id`"
 ]
 },
 {
 "Sid": "AllowSnapshots",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeDBClusterSnapshots",
 "rds:CreateDBClusterSnapshot",
 "rds:AddTagsToResource"
 ],
 "Resource": [
 "arn:aws:rds:`us-east-2`:`111122223333`:cluster:`DB-id`",
 "arn:aws:rds:`us-east-2`:`111122223333`:cluster-snapshot:`DB-id`*"
 ]
 },
 {
 "Sid": "AllowExport",
 "Effect": "Allow",
 "Action": [
 "rds:StartExportTask"
 ],
 "Resource": [
 "arn:aws:rds:`us-east-2`:`111122223333`:cluster:`DB-id`",
 "arn:aws:rds:`us-east-2`:`111122223333`:cluster-snapshot:`DB-id`*"
 ]
 },
 {
 "Sid": "AllowDescribeExports",
 "Effect": "Allow",
 "Action": [
 "rds:DescribeExportTasks"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "`us-east-2`",
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 },
 {
 "Sid": "AllowAccessToKmsForExport",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:Encrypt",
 "kms:DescribeKey",
 "kms:RetireGrant",
 "kms:CreateGrant",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-2`:`111122223333`:key/`export-key-id`"
 ]
 },
 {
 "Sid": "AllowPassingExportRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::`111122223333`:role/`export-role`"
 ]
 },
 {
 "Sid": "SecretsManagerReadAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:*:`111122223333`:secret:*"
 ]
 }
 ]
 }`

```

## Step 2: Create the pipeline

Configure an OpenSearch Ingestion pipeline similar to the following. The example
pipeline specifies an Amazon Aurora cluster as the source.

```
version: "2"
aurora-mysql-pipeline:
  source:
    rds:
      db_identifier: "`cluster-id`"
      engine: aurora-mysql
      database: "`database-name`"
      tables:
        include:
          - "`table1`"
          - "`table2`"
      s3_bucket: "`bucket-name`"
      s3_region: "`bucket-region`"
      s3_prefix: "`prefix-name`"
      export:
        kms_key_id: "`kms-key-id`"
        iam_role_arn: "`export-role-arn`"
      stream: true
      aws:
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        region: "us-east-1"
      authentication:
        username: ${{aws_secrets:secret:username}}
        password: ${{aws_secrets:secret:password}}
  sink:
    - opensearch:
        hosts: ["https://search-mydomain.us-east-1.es.amazonaws.com"]
        index: "${getMetadata(\"table_name\")}"
        index_type: custom
        document_id: "${getMetadata(\"primary_key\")}"
        action: "${getMetadata(\"opensearch_action\")}"
        document_version: "${getMetadata(\"document_version\")}"
        document_version_type: "external"
        aws:
          sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
          region: "us-east-1"
extension:
  aws:
    secrets:
      secret:
        secret_id: "`rds-secret-id`"
        region: "us-east-1"
        sts_role_arn: "arn:aws:iam::`account-id`:role/`pipeline-role`"
        refresh_interval: PT1H
```

You can use a preconfigured Amazon Aurora blueprint to create this pipeline. For more
information, see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

To use Amazon Aurora as a source, you need to configure VPC access for the pipeline.
The VPC you choose should be the same VPC your Amazon Aurora source uses. Then choose
one or more subnets and one or more VPC security groups. Note that the pipeline
needs network access to a Aurora MySQL database, so you should also verify that your
Aurora cluster is configured with a VPC security group that allows inbound traffic
from the pipeline's VPC security group to the database port. For more information,
see [Controlling access with security groups](../../../AmazonRDS/latest/AuroraUserGuide/Overview.md "../../../AmazonRDS/latest/AuroraUserGuide/Overview.md").

If you're using the AWS Management Console to create your pipeline, you must also attach your
pipeline to your VPC in order to use Amazon Aurora as a source. To do so, find the
**Network configuration** section, select the **Attach
to VPC** checkbox, and choose your CIDR from one of the provided
default options, or select your own. You can use any CIDR from a private address
space as defined in the [RFC 1918 Best Current Practice](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").

To provide a custom CIDR, select **Other** from the dropdown
menu. To avoid a collision in IP addresses between OpenSearch Ingestion and Amazon Aurora,
ensure that the Amazon Aurora VPC CIDR is different from the CIDR for
OpenSearch Ingestion.

For more information, see [Configuring VPC access for a pipeline](pipeline-security.md#pipeline-vpc-configure "pipeline-security.md#pipeline-vpc-configure").

## Data consistency

The pipeline ensures data consistency by continuously polling or receiving changes
from the Amazon Aurora cluster and updating the corresponding documents in the OpenSearch
index.

OpenSearch Ingestion supports end-to-end acknowledgement to ensure data durability.
When a pipeline reads snapshots or streams, it dynamically creates partitions for
parallel processing. The pipeline marks a partition as complete when it receives an
acknowledgement after ingesting all records in the OpenSearch domain or collection.
If you want to ingest into an OpenSearch Serverless search collection, you can
generate a document ID in the pipeline. If you want to ingest into an OpenSearch
Serverless time series collection, note that the pipeline doesn't generate a
document ID, so you must omit `document_id: "${getMetadata(\"primary_key\")}"` in your
pipeline sink configuration.

An OpenSearch Ingestion pipeline also maps incoming event actions into corresponding
bulk indexing actions to help ingest documents. This keeps data consistent, so that
every data change in Amazon Aurora is reconciled with the corresponding document changes
in OpenSearch.

## Mapping data types

OpenSearch Ingestion pipeline maps MySQL data types to representations that are
suitable for OpenSearch Service domains or collections to consume. If no mapping template is
defined in OpenSearch, OpenSearch automatically determines field types with [dynamic
mapping](https://opensearch.org/docs/latest/field-types/#dynamic-mapping "https://opensearch.org/docs/latest/field-types/#dynamic-mapping") based on the first sent document. You can also explicitly define
the field types that work best for you in OpenSearch through a mapping template.

The table below lists MySQL data types and corresponding OpenSearch field types.
The _Default OpenSearch Field Type_ column shows the corresponding
field type in OpenSearch if no explicit mapping is defined. In this case, OpenSearch
automatically determines field types with dynamic mapping. The _Recommended
OpenSearch Field Type_ column is the corresponding field type that is
recommended to explicitly specify in a mapping template. These field types are more
closely aligned with the data types in MySQL and can usually enable better search
features available in OpenSearch.

| MySQL Data Type                                  | Default OpenSearch Field Type                                                                                                               | Recommended OpenSearch Field Type                         |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| BIGINT                                           | long                                                                                                                                        | long                                                      |
| BIGINT UNSIGNED                                  | long                                                                                                                                        | unsigned long                                             |
| BIT                                              | long                                                                                                                                        | byte, short, integer, or long depending on number of bits |
| DECIMAL                                          | text                                                                                                                                        | double or keyword                                         |
| DOUBLE                                           | float                                                                                                                                       | double                                                    |
| FLOAT                                            | float                                                                                                                                       | float                                                     |
| INT                                              | long                                                                                                                                        | integer                                                   |
| INT UNSIGNED                                     | long                                                                                                                                        | long                                                      |
| MEDIUMINT                                        | long                                                                                                                                        | integer                                                   |
| MEDIUMINT UNSIGNED                               | long                                                                                                                                        | integer                                                   |
| NUMERIC                                          | text                                                                                                                                        | double or keyword                                         |
| SMALLINT                                         | long                                                                                                                                        | short                                                     |
| SMALLINT UNSIGNED                                | long                                                                                                                                        | integer                                                   |
| TINYINT                                          | long                                                                                                                                        | byte                                                      |
| TINYINT UNSIGNED                                 | long                                                                                                                                        | short                                                     |
| BINARY                                           | text                                                                                                                                        | binary                                                    |
| BLOB                                             | text                                                                                                                                        | binary                                                    |
| CHAR                                             | text                                                                                                                                        | text                                                      |
| ENUM                                             | text                                                                                                                                        | keyword                                                   |
| LONGBLOB                                         | text                                                                                                                                        | binary                                                    |
| LONGTEXT                                         | text                                                                                                                                        | text                                                      |
| MEDIUMBLOB                                       | text                                                                                                                                        | binary                                                    |
| MEDIUMTEXT                                       | text                                                                                                                                        | text                                                      |
| SET                                              | text                                                                                                                                        | keyword                                                   |
| TEXT                                             | text                                                                                                                                        | text                                                      |
| TINYBLOB                                         | text                                                                                                                                        | binary                                                    |
| TINYTEXT                                         | text                                                                                                                                        | text                                                      |
| VARBINARY                                        | text                                                                                                                                        | binary                                                    |
| VARCHAR                                          | text                                                                                                                                        | text                                                      |
| DATE                                             | long (in epoch milliseconds)                                                                                                                | date                                                      |
| DATETIME                                         | long (in epoch milliseconds)                                                                                                                | date                                                      |
| TIME                                             | long (in epoch milliseconds)                                                                                                                | date                                                      |
| TIMESTAMP                                        | long (in epoch milliseconds)                                                                                                                | date                                                      |
| YEAR                                             | long (in epoch milliseconds)                                                                                                                | date                                                      |
| GEOMETRY                                         | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| GEOMETRYCOLLECTION                               | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| LINESTRING                                       | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| MULTILINESTRING                                  | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| MULTIPOINT                                       | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| MULTIPOLYGON                                     | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| POINT                                            | text (in WKT format)                                                                                                                        | geo_point or geo_shape                                    |
| POLYGON                                          | text (in WKT format)                                                                                                                        | geo_shape                                                 |
| JSON                                             | text                                                                                                                                        | object                                                    | We recommend that you configure the dead-letter queue (DLQ) in your OpenSearch Ingestion pipeline. If you've configured the queue, OpenSearch Service sends all failed documents that can't be ingested due to dynamic mapping failures to the queue. If automatic mappings fail, you can use `template_type` and `template_content` in your pipeline configuration to define explicit mapping rules. Alternatively, you can create mapping templates directly in your search domain or collection before you start the pipeline. ## Limitations Consider the following limitations when you set up an OpenSearch Ingestion pipeline for Aurora MySQL: <br>• The integration only supports one MySQL database per pipeline. <br>• The integration does not currently support cross-region data ingestion; your Amazon Aurora cluster and OpenSearch domain must be in the same AWS Region. <br>• The integration does not currently support cross-account data ingestion; your Amazon Aurora cluster and OpenSearch Ingestion pipeline must be in the same AWS account. <br>• Ensure that the Amazon Aurora cluster has authentication enabled using Secrets Manager, which is the only supported authentication mechanism. <br>• The existing pipeline configuration can't be updated to ingest data from a different database and/or a different table. To update the database and/or table name of a pipeline, you have to stop the pipeline and restart it with an updated configuration, or create a new pipeline. <br>• Data Definition Language (DDL) statements are generally not supported. Data consistency will not be maintained if: + Primary keys are changed (add/delete/rename). + Tables are dropped/truncated. + Column names or data types are changed. <br>• If the MySQL tables to sync don't have primary keys defined, data consistency are not guaranteed. You will need to define custom `document_id` option in OpenSearch sink configuration properly to be able to sync updates/deletes to OpenSearch. <br>• Foreign key references with cascading delete actions are not supported and can result in data inconsistency between Aurora MySQL and OpenSearch. <br>• Supported versions: Aurora MySQL version 3.05.2 and higher. ## Recommended CloudWatch Alarms The following CloudWatch metrics are recommended for monitoring the performance of your ingestion pipeline. These metrics can help you identify the amount of data processed from exports, the number of events processed from streams, the errors in processing exports and stream events, and the number of documents written to the destination. You can setup CloudWatch alarms to perform an action when one of these metrics exceed a specified value for a specified amount of time. |
| Metric                                           | Description                                                                                                                                 |                                                           | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ---                                                                                            |
| `pipeline-name`.rds.credentialsChanged           | This metric indicates how often AWS secrets are rotated.                                                                                    |                                                           | `pipeline-name`.rds.executorRefreshErrors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | This metric indicates failures to refresh AWS secrets.                                         |
| `pipeline-name`.rds.exportRecordsTotal           | This metric indicates the number of records exported from Amazon Aurora.                                                                    |                                                           | `pipeline-name`.rds.exportRecordsProcessed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | This metric indicates the number of records processed by OpenSearch Ingestion pipeline.        |
| `pipeline-name`.rds.exportRecordProcessingErrors | This metric indicates number of processing errors in an OpenSearch Ingestion pipeline while reading the data from an Amazon Aurora cluster. |                                                           | `pipeline-name`.rds.exportRecordsSuccessTotal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This metric indicates the total number of export records processed successfully.               |
| `pipeline-name`.rds.exportRecordsFailedTotal     | This metric indicates the total number of export records that failed to process.                                                            |                                                           | `pipeline-name`.rds.bytesReceived                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | This metrics indicates the total number of bytes received by an OpenSearch Ingestion pipeline. |
| `pipeline-name`.rds.bytesProcessed               | This metrics indicates the total number of bytes processed by an OpenSearch Ingestion pipeline.                                             |                                                           | `pipeline-name`.rds.streamRecordsSuccessTotal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This metric indicates the number of records successfully processed from the stream.            |
| `pipeline-name`.rds.streamRecordsFailedTotal     | This metrics indicates the total number of records failed to process from the stream.                                                       |
