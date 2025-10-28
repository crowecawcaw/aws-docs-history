# Using an OpenSearch Ingestion pipeline with

Amazon DocumentDB

You can use the [DocumentDB](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/documentdb/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/documentdb/") plugin to stream document changes, such as creates, updates, and
deletes, to Amazon OpenSearch Service. The pipeline supports change data capture (CDC), if available, or API
polling for high-scale, low-latency streaming.

You can process data with or without a full initial snapshot. A full snapshot captures an
entire Amazon DocumentDB collection and uploads it to Amazon S3. The pipeline then sends the data to one or
more OpenSearch indexes. After it ingests the snapshot, the pipeline synchronizes ongoing
changes to maintain consistency and eventually catches up to near real-time updates.

If you already have a full snapshot from another source, or only need to process new
events, you can stream without a snapshot. In this case, the pipeline reads directly from
Amazon DocumentDB change streams without an initial bulk load.

If you enable streaming, you must [enable a change stream](../../../documentdb/latest/developerguide/change_streams.md#change_streams-enabling "../../../documentdb/latest/developerguide/change_streams.md#change_streams-enabling") on your Amazon DocumentDB collection. However, if you only perform
a full load or export, you don’t need a change stream.

## Prerequisites

Before you create your OpenSearch Ingestion pipeline, perform the following
steps:

1. Create a Amazon DocumentDB cluster with permission to read data by following the steps
   in [Create an Amazon DocumentDB cluster](../../../documentdb/latest/developerguide/get-started-guide.md#cloud9-cluster "../../../documentdb/latest/developerguide/get-started-guide.md#cloud9-cluster") in the _Amazon DocumentDB Developer
   Guide_. If you use CDC infrastructure, configure your Amazon DocumentDB
   cluster to publish change streams.
2. Enable TLS on your Amazon DocumentDB cluster.
3. Set up a VPC CIDR of a private address space for use with
   OpenSearch Ingestion.
4. Set up authentication on your Amazon DocumentDB cluster with AWS Secrets Manager. Enable secrets
   rotation by following the steps in [Automatically rotating passwords for Amazon DocumentDB](../../../documentdb/latest/developerguide/security.md#security.managing-users-rotating-passwords "../../../documentdb/latest/developerguide/security.md#security.managing-users-rotating-passwords"). For more information,
   see [Database access using Role-Based Access Control](../../../documentdb/latest/developerguide/role_based_access_control.md "../../../documentdb/latest/developerguide/role_based_access_control.md") and [Security in Amazon DocumentDB](../../../documentdb/latest/developerguide/security.md "../../../documentdb/latest/developerguide/security.md").
5. If you use a change stream to subscribe to data changes on your Amazon DocumentDB
   collection, avoid data loss by extending the retention period to up to 7 days
   using the `change_stream_log_retention_duration` parameter. Change
   streams events are stored for 3 hours, by default, after the event has been
   recorded, which isn't enough time for large collections. To modify the change
   stream retention period, see [Modifying the change stream log retention duration](../../../documentdb/latest/developerguide/change_streams.md#change_streams-modifying_log_retention "../../../documentdb/latest/developerguide/change_streams.md#change_streams-modifying_log_retention").
6. Create an OpenSearch Service domain or OpenSearch Serverless collection. For more information, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains "createupdatedomains.md#createdomains") and [Creating collections](serverless-create.md "serverless-create.md").
7. Attach a [resource-based policy](ac.md#ac-types-resource "ac.md#ac-types-resource") to your domain or a [data access policy](serverless-data-access.md "serverless-data-access.md") to your collection. These access policies allow
   OpenSearch Ingestion to write data from your Amazon DocumentDB cluster to your domain or
   collection.

The following sample domain access policy allows the pipeline role, which you
create in the next step, to write data to a domain. Make sure that you update
the `resource` with your own ARN.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:role/`pipeline-role`"
 },
 "Action": [
 "es:DescribeDomain",
 "es:ESHttp*"
 ],
 "Resource": [
 "arn:aws:es:`us-east-1`:`111122223333`:domain/`domain-name`"
 ]
 }
 ]
}`

```

To create an IAM role with the correct permissions to access write data to
the collection or domain, see [Setting up roles and users in
Amazon OpenSearch Ingestion](pipeline-security-overview.md "pipeline-security-overview.md").

## Step 1: Configure the pipeline role

After you have your Amazon DocumentDB pipeline prerequisites set up, [configure the pipeline role](pipeline-security-overview.md#pipeline-security-sink "pipeline-security-overview.md#pipeline-security-sink") that you want to
use in your pipeline configuration, and add the following Amazon DocumentDB permissions in the
role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "allowS3ListObjectAccess",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`s3-bucket`"
 ],
 "Condition": {
 "StringLike": {
 "s3:prefix": "`s3-prefix`/*"
 }
 }
 },
 {
 "Sid": "allowReadAndWriteToS3ForExportStream",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::`s3-bucket`/`s3-prefix`/*"
 ]
 },
 {
 "Sid": "SecretsManagerReadAccess",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name`"
 ]
 },
 {
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
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeDhcpOptions",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:Describe*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags"
 ],
 "Resource": "arn:aws:ec2:*:*:network-interface/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/OSISManaged": "true"
 }
 }
 }
 ]
}`

```

You must provide the above Amazon EC2 permissions on the IAM role that you use to create
the OpenSearch Ingestion pipeline because the pipeline uses these permissions to create and
delete a network interface in your VPC. The pipeline can only access the Amazon DocumentDB cluster
through this network interface.

## Step 2: Create the pipeline

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies
Amazon DocumentDB as the source. Note that to populate the index name, the
`getMetadata` function uses
`documentdb_collection` as a metadata key.
If you want to use a different index name without the `getMetadata` method,
you can use the configuration `index:
 "`my_index_name`"`.

```
version: "2"
documentdb-pipeline:
  source:
    documentdb:
      acknowledgments: true
      host: "https://`docdb-cluster-id`.`us-east-1`.docdb.amazonaws.com"
      port: 27017
      authentication:
        username: ${aws_secrets:secret:`username`}
        password: ${aws_secrets:secret:`password`}
      aws:
      s3_bucket: "`bucket-name`"
      s3_region: "`bucket-region`"
      s3_prefix: "`path`" #optional path for storing the temporary data
      collections:
        - collection: "`dbname.collection`"
          export: true
          stream: true
  sink:
  - opensearch:
      hosts: ["`https://search-mydomain.us-east-1.es.amazonaws.com`"]
      index: "${getMetadata(\"`documentdb_collection`\")}"
      index_type: custom
      document_id: "${getMetadata(\"primary_key\")}"
      action: "${getMetadata(\"opensearch_action\")}"
      document_version: "${getMetadata(\"document_version\")}"
      document_version_type: "external"
extension:
  aws:
    secrets:
      secret:
        secret_id: "`my-docdb-secret`"
        region: "`us-east-1`"
        refresh_interval: PT1H
```

You can use a preconfigured Amazon DocumentDB blueprint to create this pipeline. For more
information, see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

If you're using the AWS Management Console to create your pipeline, you must also attach your
pipeline to your VPC in order to use Amazon DocumentDB as a source. To do so, find the
**Source network options** section, select the **Attach to
VPC** checkbox, and choose your CIDR from one of the provided default
options. You can use any CIDR from a private address space as defined in the [RFC 1918 Best Current
Practice](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").

To provide a custom CIDR, select **Other** from the dropdown menu. To
avoid a collision in IP addresses between OpenSearch Ingestion and Amazon DocumentDB, ensure that the
Amazon DocumentDB VPC CIDR is different from the CIDR for OpenSearch Ingestion.

For more information, see [Configuring VPC access for a pipeline](pipeline-security.md#pipeline-vpc-configure "pipeline-security.md#pipeline-vpc-configure").

## Data consistency

The pipeline ensures data consistency by continuously polling or receiving changes
from the Amazon DocumentDB cluster and updating the corresponding documents in the OpenSearch
index.

OpenSearch Ingestion supports end-to-end acknowledgement to ensure data durability. When a
pipeline reads snapshots or streams, it dynamically creates partitions for parallel
processing. The pipeline marks a partition as complete when it receives an
acknowledgement after ingesting all records in the OpenSearch domain or collection.

If you want to ingest into an OpenSearch Serverless _search_ collection, you can
generate a document ID in the pipeline. If you want to ingest into an OpenSearch Serverless
_time series_ collection, note that the pipeline doesn't generate
a document ID, so you must omit `document_id:
 "${getMetadata(\"primary_key\")}"` in your pipeline sink configuration.

An OpenSearch Ingestion pipeline also maps incoming event actions into corresponding bulk
indexing actions to help ingest documents. This keeps data consistent, so that every
data change in Amazon DocumentDB is reconciled with the corresponding document changes in
OpenSearch.

## Mapping data types

OpenSearch Service dynamically maps data types in each incoming document to the corresponding data
type in Amazon DocumentDB. The following table shows how OpenSearch Service automatically maps various data
types.

| Data type                                                 | OpenSearch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Amazon DocumentDB                                                                                                                                                                                                    |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Integer                                                   | OpenSearch automatically maps Amazon DocumentDB integer values to OpenSearch integers. OpenSearch dynamically maps the field based on the first sent document. If you have a mix of data types for the same attribute in Amazon DocumentDB, automatic mapping might fail. For example, if your first document has an attribute that is a long, and a later document has that same attribute as an integer, OpenSearch fails to ingest the second document. In these cases, you should provide an explicit mapping template that chooses the most flexible number type, such as the following: `{ "template": { "mappings": { "properties": { "MixedNumberField": { "type": "float" } } } } }` | Amazon DocumentDB supports [integers](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                |
| Long                                                      | OpenSearch automatically maps Amazon DocumentDB long values to OpenSearch longs. OpenSearch dynamically maps the field based on the first sent document. If you have a mix of data types for the same attribute in Amazon DocumentDB, automatic mapping might fail. For example, if your first document has an attribute that is a long, and a later document has that same attribute as an integer, OpenSearch fails to ingest the second document. In these cases, you should provide an explicit mapping template that chooses the most flexible number type, such as the following: `{ "template": { "mappings": { "properties": { "MixedNumberField": { "type": "float" } } } } }`       | Amazon DocumentDB supports [longs](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                   |
| String                                                    | OpenSearch automatically maps string values as text. In some situations, such as enumerated values, you can map to the keyword type. The following example shows how to map a Amazon DocumentDB attribute named `PartType` to an OpenSearch keyword. `{ "template": { "mappings": { "properties": { "PartType": { "type": "keyword" } } } } }`                                                                                                                                                                                                                                                                                                                                                | Amazon DocumentDB supports [strings](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                 |
| Double                                                    | OpenSearch automatically maps Amazon DocumentDB double values to OpenSearch doubles. OpenSearch dynamically maps the field based on the first sent document. If you have a mix of data types for the same attribute in Amazon DocumentDB, automatic mapping might fail. For example, if your first document has an attribute that is a long, and a later document has that same attribute as an integer, OpenSearch fails to ingest the second document. In these cases, you should provide an explicit mapping template that chooses the most flexible number type, such as the following: `{ "template": { "mappings": { "properties": { "MixedNumberField": { "type": "float" } } } } }`   | Amazon DocumentDB supports [doubles](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                 |
| Date                                                      | By default, date maps to an integer in OpenSearch. You can define a custom mapping template to map a date to an OpenSearch date. `{ "template": { "mappings": { "properties": { "myDateField": { "type": "date", "format": "epoch_second" } } } } }`                                                                                                                                                                                                                                                                                                                                                                                                                                          | Amazon DocumentDB supports [dates](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                   |
| Timestamp                                                 | By default, timestamp maps to an integer in OpenSearch. You can define a custom mapping template to map a date to an OpenSearch date. `{ "template": { "mappings": { "properties": { "myTimestampField": { "type": "date", "format": "epoch_second" } } } } }`                                                                                                                                                                                                                                                                                                                                                                                                                                | Amazon DocumentDB supports [timestamps](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").              |
| Boolean                                                   | OpenSearch maps a Amazon DocumentDB Boolean type into an OpenSearch Boolean type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Amazon DocumentDB supports [Boolean type attributes](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types"). |
| Decimal                                                   | OpenSearch maps Amazon DocumentDB map attributes to nested fields. The same mappings apply within a nested field. The following example maps a string in a nested field to a keyword type in OpenSearch: `{ "template": { "mappings": { "properties": { "myDecimalField": { "type": "double" } } } } }` With this custom mapping, you can query and aggregate the field with double-level precision. The original value retains the full precision in the `_source` property of the OpenSearch document. Without this mapping, OpenSearch uses text by default.                                                                                                                               | Amazon DocumentDB supports [decimals](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").                |
| Regular Expression                                        | The regex type creates nested fields. These include ``<myFieldName>`.pattern` and ``<myFieldName>`.options`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Amazon DocumentDB supports [regular expressions](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").     |
| Binary Data                                               | OpenSearch automatically maps Amazon DocumentDB binary data to OpenSearch text. You can provide a mapping to write these as binary fields in OpenSearch. The following example shows how to map a Amazon DocumentDB field named `imageData` to an OpenSearch binary field. `{ "template": { "mappings": { "properties": { "imageData": { "type": "binary" } } } } }`                                                                                                                                                                                                                                                                                                                          | Amazon DocumentDB supports[binary data fields](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").       |
| ObjectId                                                  | Fields with a type of objectId map to OpenSearch text fields. The value will be the string representation of the objectId.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Amazon DocumentDB supports [objectIds](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").               |
| Null                                                      | OpenSearch can ingest documents with the Amazon DocumentDB null type. It saves the value as a null value in the document. There is no mapping for this type, and this field is not indexed or searchable. If the same attribute name is used for a null type and then later changes to different type such as string, OpenSearch creates a dynamic mapping for the first non-null value. Subsequent values can still be Amazon DocumentDB null values.                                                                                                                                                                                                                                        | Amazon DocumentDB supports [null type fields](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").        |
| Undefined                                                 | OpenSearch can ingest documents with the Amazon DocumentDB undefined type. It saves the value as a null value in the document. There is no mapping for this type, and this field is not indexed or searchable. If the same field name is used for a undefined type and then later changes to different type such as string, OpenSearch creates a dynamic mapping for the first non-undefined value. Subsequent values can still be Amazon DocumentDB undefined values.                                                                                                                                                                                                                        | Amazon DocumentDB supports [undefined type fields](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").   |
| MinKey                                                    | OpenSearch can ingest documents with the Amazon DocumentDB minKey type. It saves the value as a null value in the document. There is no mapping for this type, and this field is not indexed or searchable. If the same field name is used for a minKey type and then later changes to different type such as string, OpenSearch creates a dynamic mapping for the first non-minKey value. Subsequent values can still be Amazon DocumentDB minKey values.                                                                                                                                                                                                                                    | Amazon DocumentDB supports [minKey type fields](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").      |
| MaxKey                                                    | OpenSearch can ingest documents with the Amazon DocumentDB maxKey type. It saves the value as a null value in the document. There is no mapping for this type, and this field is not indexed or searchable. If the same field name is used for a maxKey type and then later changes to different type such as string, OpenSearch creates a dynamic mapping for the first non-maxKey value. Subsequent values can still be Amazon DocumentDB maxKey values.                                                                                                                                                                                                                                    | Amazon DocumentDB supports [maxKey type fields](../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types "../../../documentdb/latest/developerguide/mongo-apis.md#mongo-apis-data-types").      | We recommend that you configure the dead-letter queue (DLQ) in your OpenSearch Ingestion pipeline. If you've configured the queue, OpenSearch Service sends all failed documents that can't be ingested due to dynamic mapping failures to the queue. In case automatic mappings fail, you can use `template_type` and `template_content` in your pipeline configuration to define explicit mapping rules. Alternatively, you can create mapping templates directly in your search domain or collection before you start the pipeline. ## Limitations Consider the following limitations when you set up an OpenSearch Ingestion pipeline for Amazon DocumentDB: <br>• The OpenSearch Ingestion integration with Amazon DocumentDB currently doesn't support cross-Region ingestion. Your Amazon DocumentDB cluster and OpenSearch Ingestion pipeline must be in the same AWS Region. <br>• The OpenSearch Ingestion integration with Amazon DocumentDB currently doesn't support cross-account ingestion. Your Amazon DocumentDB cluster and OpenSearch Ingestion pipeline must be in the same AWS account. <br>• An OpenSearch Ingestion pipeline supports only one Amazon DocumentDB cluster as its source. <br>• The OpenSearch Ingestion integration with Amazon DocumentDB specifically supports Amazon DocumentDB instance-based clusters. It doesn't support Amazon DocumentDB elastic clusters. <br>• The OpenSearch Ingestion integration only supports AWS Secrets Manager as an authentication mechanism for your Amazon DocumentDB cluster. <br>• You can't update the existing pipeline configuration to ingest data from a different database or collection. Instead, you must create a new pipeline. ## Recommended CloudWatch alarms For the best performance, we recommend that you use the following CloudWatch alarms when you create an OpenSearch Ingestion pipeline to access an Amazon DocumentDB cluster as a source. |
| CloudWatch Alarm                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                      | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | ---                                                                                            |
| `<pipeline-name>`.doucmentdb.credentialsChanged           | This metric indicates how often AWS secrets are rotated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.executorRefreshErrors                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | This metric indicates failures to refresh AWS secrets.                                         |
| `<pipeline-name>`.doucmentdb.exportRecordsTotal           | This metric indicates the number of records exported from Amazon DocumentDB.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.exportRecordsProcessed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | This metric indicates the number of records processed by OpenSearch Ingestion pipeline.        |
| `<pipeline-name>`.doucmentdb.exportRecordProcessingErrors | This metric indicates number of processing errors in an OpenSearch Ingestion pipeline while reading the data from an Amazon DocumentDB cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.exportRecordsSuccessTotal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This metric indicates the total number of export records processed successfully.               |
| `<pipeline-name>`.doucmentdb.exportRecordsFailedTotal     | This metric indicates the total number of export records that failed to process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.bytesReceived                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | This metrics indicates the total number of bytes received by an OpenSearch Ingestion pipeline. |
| `<pipeline-name>`.doucmentdb.bytesProcessed               | This metrics indicates the total number of bytes processed by an OpenSearch Ingestion pipeline.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.exportPartitionQueryTotal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | This metric indicates the export partition total.                                              |
| `<pipeline-name>`.doucmentdb.streamRecordsSuccessTotal    | This metric indicates the number of records successfully processed from the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                      | `<pipeline-name>`.doucmentdb.streamRecordsFailedTotal                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | This metrics indicates the total number of records failed to process from the stream.          |
