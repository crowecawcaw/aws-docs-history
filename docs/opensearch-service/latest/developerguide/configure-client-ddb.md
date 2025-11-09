# Using an OpenSearch Ingestion pipeline with

Amazon DynamoDB

You can use the [DynamoDB](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/dynamo-db/ "https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/dynamo-db/") plugin to stream table events, such as creates, updates, and deletes,
to Amazon OpenSearch Service domains and Amazon OpenSearch Serverless collections. The pipeline uses change data capture (CDC)
for high-scale, low-latency streaming.

You can process DynamoDB data with or without a full initial snapshot.

- **With a full snapshot** – DynamoDB uses [point-in-time recovery](../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md "../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md") (PITR) to create a backup and uploads it to
  Amazon S3. OpenSearch Ingestion then indexes the snapshot in one or multiple OpenSearch
  indexes. To maintain consistency, the pipeline synchronizes all DynamoDB changes with
  OpenSearch. This option requires you to enable both PITR and [DynamoDB Streams](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.CoreComponents.Streams "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.CoreComponents.Streams").
- **Without a snapshot** – OpenSearch Ingestion
  streams only new DynamoDB events. Choose this option if you already have a snapshot or
  need real-time streaming without historical data. This option requires you to enable
  only DynamoDB Streams.
  For more information, see [DynamoDB
  zero-ETL integration with Amazon OpenSearch Service](../../../amazondynamodb/latest/developerguide/OpenSearchIngestionForDynamoDB.md "../../../amazondynamodb/latest/developerguide/OpenSearchIngestionForDynamoDB.md") in the _Amazon DynamoDB
  Developer Guide_.

###### Topics

- [Prerequisites](#s3-prereqs "#s3-prereqs")
- [Step 1: Configure the pipeline role](#ddb-pipeline-role "#ddb-pipeline-role")
- [Step 2: Create the pipeline](#ddb-pipeline "#ddb-pipeline")
- [Data consistency](#ddb-pipeline-consistency "#ddb-pipeline-consistency")
- [Mapping data types](#ddb-pipeline-mapping "#ddb-pipeline-mapping")
- [Limitations](#ddb-pipeline-limitations "#ddb-pipeline-limitations")
- [Recommended CloudWatch Alarms for DynamoDB](#ddb-pipeline-metrics "#ddb-pipeline-metrics")

## Prerequisites

To set up your pipeline, you must have a DynamoDB table with DynamoDB Streams enabled. Your stream
should use the `NEW_IMAGE` stream view type. However, OpenSearch Ingestion
pipelines can also stream events with `NEW_AND_OLD_IMAGES` if this stream
view type fits your use case.

If you're using snapshots, you must also enable point-in-time recovery on your table.
For more information, see [Creating a table](../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.CreateTable "../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.CreateTable"), [Enabling point-in-time recovery](../../../amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.md#howitworks_enabling "../../../amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.md#howitworks_enabling"), and [Enabling a
stream](../../../amazondynamodb/latest/developerguide/Streams.md#Streams.Enabling "../../../amazondynamodb/latest/developerguide/Streams.md#Streams.Enabling") in the _Amazon DynamoDB Developer Guide_.

## Step 1: Configure the pipeline role

After you have your DynamoDB table set up, [set up
the pipeline role](pipeline-security-overview.md#pipeline-security-sink "pipeline-security-overview.md#pipeline-security-sink") that you want to use in your pipeline configuration, and
add the following DynamoDB permissions in the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "allowRunExportJob",
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeTable",
 "dynamodb:DescribeContinuousBackups",
 "dynamodb:ExportTableToPointInTime"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`my-table`"
 ]
 },
 {
 "Sid": "allowCheckExportjob",
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeExport"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`my-table`/export/*"
 ]
 },
 {
 "Sid": "allowReadFromStream",
 "Effect": "Allow",
 "Action": [
 "dynamodb:DescribeStream",
 "dynamodb:GetRecords",
 "dynamodb:GetShardIterator"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`my-table`/stream/*"
 ]
 },
 {
 "Sid": "allowReadAndWriteToS3ForExport",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:AbortMultipartUpload",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:`us-east-1`:`111122223333`:`amzn-s3-demo-bucket`/`export-folder`/*"
 ]
 }
 ]
}`

```

You can also use an AWS KMS customer managed key to encrypt the export data files. To decrypt the
exported objects, specify `s3_sse_kms_key_id` for the key ID in the export
configuration of the pipeline with the following format:
`arn:aws:kms:`region`:`account-id`:key/`my-key-id``.
The following policy includes the required permissions for using a customer managed key:

```
{
    "Sid": "allowUseOfCustomManagedKey",
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": `arn:aws:kms:`region`:`account-id`:key/`my-key-id``
}
```

## Step 2: Create the pipeline

You can then configure an OpenSearch Ingestion pipeline like the following, which specifies
DynamoDB as the source. This sample pipeline ingests data from `table-a` with
the PITR snapshot, followed by events from DynamoDB Streams. A start position of `LATEST`
indicates that the pipeline should read the latest data from DynamoDB Streams.

```
version: "2"
cdc-pipeline:
  source:
    dynamodb:
      tables:
      - table_arn: "arn:aws:dynamodb:`region`:`account-id`:table/`table-a`"
        export:
          s3_bucket: "`my-bucket`"
          s3_prefix: "export/"
        stream:
          start_position: "LATEST"
      aws:
        region: "`us-east-1`"
  sink:
  - opensearch:
      hosts: ["`https://search-mydomain.region.es.amazonaws.com`"]
      index: "${getMetadata(\"`table-name`\")}"
      index_type: custom
      normalize_index: true
      document_id: "${getMetadata(\"primary_key\")}"
      action: "${getMetadata(\"opensearch_action\")}"
      document_version: "${getMetadata(\"document_version\")}"
      document_version_type: "external"
```

You can use a preconfigured DynamoDB blueprint to create this pipeline. For more information,
see [Working with blueprints](pipeline-blueprint.md "pipeline-blueprint.md").

## Data consistency

OpenSearch Ingestion supports end-to-end acknowledgement to ensure data durability. When a
pipeline reads snapshots or streams, it dynamically creates partitions for parallel
processing. The pipeline marks a partition as complete when it receives an
acknowledgement after ingesting all records in the OpenSearch domain or collection.

If you want to ingest into an OpenSearch Serverless _search_ collection, you can
generate a document ID in the pipeline. If you want to ingest into an OpenSearch Serverless
_time series_ collection, note that the pipeline doesn't generate
a document ID.

An OpenSearch Ingestion pipeline also maps incoming event actions into corresponding bulk
indexing actions to help ingest documents. This keeps data consistent, so that every
data change in DynamoDB is reconciled with the corresponding document changes in
OpenSearch.

## Mapping data types

OpenSearch Service dynamically maps data types in each incoming document to the corresponding data
type in DynamoDB. The following table shows how OpenSearch Service automatically maps various data
types.

| Data type  | OpenSearch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | DynamoDB                                                                                                                                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Number     | OpenSearch automatically maps numeric data. If the number is a<br>whole number, OpenSearch maps it as a long value. If the number is<br>fractional, then OpenSearch maps it as a float value.<br>OpenSearch dynamically maps various attributes based on the first<br>sent document. If you have a mix of data types for the same<br>attribute in DynamoDB, such as both a whole number and a fractional<br>number, mapping might fail.<br>For example, if your first document has an attribute that is a<br>whole number, and a later document has that same attribute as a<br>fractional number, OpenSearch fails to ingest the second document. In<br>these cases, you should provide an explicit mapping template, such<br>as the following:<br>`<br>{<br>"template": {<br>"mappings": {<br>"properties": {<br>"MixedNumberAttribute": {<br>"type": "float"<br>}<br>}<br>}<br>}<br>}<br>`<br>If you need double precision, use string-type field mapping. There<br>is no equivalent numeric type that supports 38 digits of precision<br>in OpenSearch. | DynamoDB supports [numbers](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Number "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Number").                                        |
| Number set | OpenSearch automatically maps a number set into an array of either<br>long values or float values. As with the scalar numbers, this depends on<br>whether the first number ingested is a whole number or a fractional<br>number. You can provide mappings for number sets the same way that you<br>map scalar strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | DynamoDB supports types that represent [sets of numbers](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes").       |
| String     | OpenSearch automatically maps string values as text. In some<br>situations, such as enumerated values, you can map to the keyword<br>type.<br>The following example shows how to map a DynamoDB attribute named<br>`PartType` to an OpenSearch keyword.<br>`<br>{<br>"template": {<br>"mappings": {<br>"properties": {<br>"PartType": {<br>"type": "keyword"<br>}<br>}<br>}<br>}<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | DynamoDB supports [strings](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.String "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.String").                                        |
| String set | OpenSearch automatically maps a string set into an array of<br>strings. You can provide mappings for string sets the same way that<br>you map scalar strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | DynamoDB supports types that represent [sets of strings](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes").       |
| Binary     | OpenSearch automatically maps binary data as text. You can provide<br>a mapping to write these as binary fields in OpenSearch.<br>The following example shows how to map a DynamoDB attribute named<br>`ImageData` to an OpenSearch binary field.<br>`<br>{<br>"template": {<br>"mappings": {<br>"properties": {<br>"ImageData": {<br>"type": "binary"<br>}<br>}<br>}<br>}<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | DynamoDB supports [binary type attributes](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Binary "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Binary").                         |
| Binary set | OpenSearch automatically maps a binary set into an array of binary<br>data as text. You can provide mappings for number sets the same way<br>that you map scalar binary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | DynamoDB supports types that represent [sets of binary values](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes"). |
| Boolean    | OpenSearch maps a DynamoDB Boolean type into an OpenSearch Boolean<br>type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | DynamoDB supports [Boolean type attributes](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Boolean "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Boolean").                      |
| Null       | OpenSearch can ingest documents with the DynamoDB null type. It saves<br>the value as a null value in the document. There is no mapping for<br>this type, and this field is not indexed or searchable.<br>If the same attribute name is used for a null type and then later<br>changes to different type such as string, OpenSearch creates a<br>dynamic mapping for the first non-null value. Subsequent values can<br>still be DynamoDB null values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | DynamoDB supports [null type attributes](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Null "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Null").                               |
| Map        | OpenSearch maps DynamoDB map attributes to nested fields. The same<br>mappings apply within a nested field.<br>The following example maps a string in a nested field to a keyword<br>type in OpenSearch:<br>`<br>{<br>"template": {<br>"mappings": {<br>"properties": {<br>"AdditionalDescriptions": {<br>"properties": {<br>"PartType": {<br>"type": "keyword"<br>}<br>}<br>}<br>}<br>}<br>}<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | DynamoDB supports [map type attributes](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Document.Map "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Document.Map").                |
| List       | OpenSearch provides different results for DynamoDB lists, depending on<br>what is in the list.<br>When a list contains all of the same type of scalar types (for<br>example, a list of all strings), then OpenSearch ingests the list as<br>an array of that type. This works for string, number, Boolean, and<br>null types. The restrictions for each of these types are the same as<br>restrictions for a scalar of that type.<br>You can also provide mappings for lists of maps by using the same<br>mapping as you would use for a map.<br>You can't provide a list of mixed types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | DynamoDB supports [list type attributes](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Document.List "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.Document.List").             |
| Set        | OpenSearch provides different results for DynamoDB sets depending on<br>what is in the set.<br>When a set contains all of the same type of scalar types (for<br>example, a set of all strings), then OpenSearch ingests the set as an<br>array of that type. This works for string, number, Boolean, and null<br>types. The restrictions for each of these types are the same as the<br>restrictions for a scalar of that type.<br>You can also provide mappings for sets of maps by using the same<br>mapping as you would use for a map.<br>You can't provide a set of mixed types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | DynamoDB supports types that represent [sets](../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes "../../../amazondynamodb/latest/developerguide/HowItWorks.md#HowItWorks.DataTypes.SetTypes").                  |

We recommend that you configure the dead-letter queue (DLQ) in your OpenSearch Ingestion
pipeline. If you've configured the queue, OpenSearch Service sends all failed documents that can't be
ingested due to dynamic mapping failures to the queue.

In case automatic mappings fail, you can use `template_type` and
`template_content` in your pipeline configuration to define explicit
mapping rules. Alternatively, you can create mapping templates directly in your search
domain or collection before you start the pipeline.

## Limitations

Consider the following limitations when you set up an OpenSearch Ingestion pipeline for
DynamoDB:

- The OpenSearch Ingestion integration with DynamoDB currently doesn't support
  cross-Region ingestion. Your DynamoDB table and OpenSearch Ingestion
  pipeline must be in the same AWS Region.
- Your DynamoDB table and OpenSearch Ingestion pipeline must be in the same
  AWS account.
- An OpenSearch Ingestion pipeline supports only one DynamoDB table as its source.
- DynamoDB Streams only stores data in a log for up to 24 hours. If ingestion from an
  initial snapshot of a large table takes 24 hours or more, there will be some
  initial data loss. To mitigate this data loss, estimate the size of the table
  and configure appropriate compute units of OpenSearch Ingestion pipelines.

## Recommended CloudWatch Alarms for DynamoDB

The following CloudWatch metrics are recommended for monitioring the performance of your
ingestion pipeline. These metrics can help you identify the amount of data processed
from exports, the amount of events processed from streams, the errors in processing
exports and stream events, and the number of documents written to the destination. You
can setup CloudWatch alarms to perform an action when one of these metrics exceed a specified
value for a specified amount of time.

| Metric                                                              | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `dynamodb-pipeline.BlockingBuffer.bufferUsage.value`                | Indicates how much of the buffer is being utilized.                                                                                                                                                                                                                                                                                                                                      |
| `dynamodb-pipeline.dynamodb.activeExportS3ObjectConsumers.value`    | Shows the total number of OCUs that are actively processing<br>Amazon S3 objects for the export.                                                                                                                                                                                                                                                                                         |
| `dynamodb-pipeline.dynamodb.bytesProcessed.count`                   | Count of bytes processed from DynamoDB source.                                                                                                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.dynamodb.changeEventsProcessed.count`            | Number of change events processed from DynamoDB stream.                                                                                                                                                                                                                                                                                                                                  |
| `dynamodb-pipeline.dynamodb.changeEventsProcessingErrors.count`     | Number of errors from change events processed from DynamoDB.                                                                                                                                                                                                                                                                                                                             |
| `dynamodb-pipeline.dynamodb.exportJobFailure.count`                 | Number of export job submission attempts that have failed.                                                                                                                                                                                                                                                                                                                               |
| `dynamodb-pipeline.dynamodb.exportJobSuccess.count`                 | Number of export jobs that have been submitted successfully.                                                                                                                                                                                                                                                                                                                             |
| `dynamodb-pipeline.dynamodb.exportRecordsProcessed.count`           | Total number of records processed from the export.                                                                                                                                                                                                                                                                                                                                       |
| `dynamodb-pipeline.dynamodb.exportRecordsTotal.count`               | Total number of records exported from DynamoDB, essential for tracking<br>data export volumes.                                                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.dynamodb.exportS3ObjectsProcessed.count`         | Total number of export data files that have been processed successfully from<br>Amazon S3.                                                                                                                                                                                                                                                                                               |
| `dynamodb-pipeline.opensearch.bulkBadRequestErrors.count`           | Count of errors during bulk requests due to malformed request.                                                                                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.opensearch.bulkRequestLatency.avg`               | Average latency for bulk write requests made to OpenSearch.                                                                                                                                                                                                                                                                                                                              |
| `dynamodb-pipeline.opensearch.bulkRequestNotFoundErrors.count`      | Number of bulk requests that failed because the target data could not be<br>found.                                                                                                                                                                                                                                                                                                       |
| `dynamodb-pipeline.opensearch.bulkRequestNumberOfRetries.count`     | Number of retries by OpenSearch Ingestion pipelines to write OpenSearch<br>cluster.                                                                                                                                                                                                                                                                                                      |
| `dynamodb-pipeline.opensearch.bulkRequestSizeBytes.sum`             | Total size in bytes of all bulk requests made to OpenSearch.                                                                                                                                                                                                                                                                                                                             |
| `dynamodb-pipeline.opensearch.documentErrors.count`                 | Number of errors when sending documents to OpenSearch. The documents causing<br>the errors witll be sent to DLQ.                                                                                                                                                                                                                                                                         |
| `dynamodb-pipeline.opensearch.documentsSuccess.count`               | Number of documents successfully written to an OpenSearch cluster or<br>collection.                                                                                                                                                                                                                                                                                                      |
| `dynamodb-pipeline.opensearch.documentsSuccessFirstAttempt.count`   | Number of documents successfully indexed in OpenSearch on the first<br>attempt.                                                                                                                                                                                                                                                                                                          |
| `dynamodb-pipeline.opensearch.documentsVersionConflictErrors.count` | Count of errors due to version conflicts in documents during<br>processing.                                                                                                                                                                                                                                                                                                              |
| `dynamodb-pipeline.opensearch.PipelineLatency.avg`                  | Average latency of OpenSearch Ingestion pipeline to process the data by reading<br>from the source to writint to the destination.                                                                                                                                                                                                                                                        |
| `dynamodb-pipeline.opensearch.PipelineLatency.max`                  | Maximum latency of OpenSearch Ingestion pipeline to process the data by reading<br>from the source to writing the destination.                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.opensearch.recordsIn.count`                      | Count of records successfully ingested into OpenSearch. This metric is<br>essential for tracking the volume of data being processed and stored.                                                                                                                                                                                                                                          |
| `dynamodb-pipeline.opensearch.s3.dlqS3RecordsFailed.count`          | Number of records that failed to write to DLQ.                                                                                                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.opensearch.s3.dlqS3RecordsSuccess.count`         | Number of records that are written to DLQ.                                                                                                                                                                                                                                                                                                                                               |
| `dynamodb-pipeline.opensearch.s3.dlqS3RequestLatency.count`         | Count of latency measurements for requests to the Amazon S3 dead-letter<br>queue.                                                                                                                                                                                                                                                                                                        |
| `dynamodb-pipeline.opensearch.s3.dlqS3RequestLatency.sum`           | Total latency for all requests to the Amazon S3 dead-letter queue                                                                                                                                                                                                                                                                                                                        |
| `dynamodb-pipeline.opensearch.s3.dlqS3RequestSizeBytes.sum`         | Total size in bytes of all requests made to the Amazon S3 dead-letter queue.                                                                                                                                                                                                                                                                                                             |
| `dynamodb-pipeline.recordsProcessed.count`                          | Total number of records processed in the pipeline, a key metric for overal<br>throughput.                                                                                                                                                                                                                                                                                                |
| `dynamodb.changeEventsProcessed.count`                              | No records are being gathered from DynamoDB streams. This could be due to no<br>activitiy on the table, an export being in progress, or an issue accessing<br>the DynamoDB streams.                                                                                                                                                                                                      |
| `dynamodb.exportJobFailure.count`                                   | The attempt to trigger an export to S3 failed.                                                                                                                                                                                                                                                                                                                                           |
| `dynamodb-pipeline.opensearch.bulkRequestInvalidInputErrors.count`  | Count of bulk request errors in OpenSearch due to invalid input, crucial for<br>monitoring data quality and operational issues.                                                                                                                                                                                                                                                          |
| `opensearch.EndToEndLatency.avg`                                    | The end to end latnecy is higher than desired for reading from DynamoDB<br>streams. This could be due to an underscaled OpenSearch cluster or a maximum<br>pipeline OCU capacity that is too low for the WCU throughput on the DynamoDB<br>table. This end to end latency will be high after an export and should<br>decrease over time as it catches up to the latest DynamoDB streams. |
