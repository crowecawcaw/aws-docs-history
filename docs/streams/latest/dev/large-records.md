# Handle large records

Amazon Kinesis Data Streams supports records up to 10 mebibytes (MiBs). This capability is recommended for
processing intermittent data payloads that exceed the default 1 MiB record size limit. The
default maximum record size for existing, and newly created streams is set to 1 MiB.

This feature benefits Internet of Things (IoT) applications, change data capture (CDC)
pipelines, and machine learning workflows that require processing occasional larger data
payloads. To start using large records in your stream, update your stream's maximum record
size limit.

###### Important

Individual shard throughput limit of 1 MB/s for writes, and 2 MB/s for reads remain
unchanged with support for larger record sizes. Kinesis Data Streams is designed to accommodate
intermittent large records alongside a baseline traffic of records less than, or equal
to 1 MiB. It is not designed to accommodate sustained high-volume large record
ingestion.

## Update your stream to use large records

###### To process larger records with Kinesis Data Streams

1. Navigate to the Kinesis Data Streams console.
2. Select your stream, and go to the **Configuration** tab.
3. Click **Edit**, which is located next to **Maximum record size**.
4. Set your maximum record size (up to 10 MiB).
5. Save your changes.

This setting only adjusts the maximum record size for this Kinesis data stream. Before increasing this limit, verify that all downstream applications can handle larger records.

You can also update this setting using the AWS CLI:

```
aws kinesis update-max-record-size \ --stream-arn  \
        --max-record-size-in-ki-b 5000
```

## Optimize your stream performance with large

records

It's recommended to maintain large records to less than 2% of your overall traffic. In
a stream, each shard has a throughput capacity of 1 MiB per second. To accommodate large
records, Kinesis Data streams bursts up to 10 MiBs, while averaging out to 1 MiB per
second. This capacity to support large records is continuously refilled into the stream.
The rate of refilling depends on the size of the large records and the size of the
baseline record. For best results, use a uniformly distributed partition key. For more
information on how Kinesis on-demand scales, see [On-demand mode features and use
cases](how-do-i-size-a-stream.md#ondemandmode "how-do-i-size-a-stream.md#ondemandmode").

## Mitigate throttling with large records

###### To mitigate throttling

1. Implement retry logic with exponential back-off in your producer application.
2. Use randomized partition keys to distribute large records across available shards.
3. Store payloads in Amazon S3 and send only metadata references to the stream for continuous streams
   of large records. For more information, see [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/ "https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/").

## Handle large records using the Kinesis Data Streams APIs

Large record support introduces one new API, and updates two existing control plane
APIs to handle records up to 10 MiBs.

API for modifying record size:

- `UpdateMaxRecordSize`: Configures the maximum record size limit for existing
  streams up to 10 MiBs.

Updates to existing APIs:

- `CreateStream`: Adds the optional `MaxRecordSizeInKiB` parameter for setting record size limits during the stream creation.
- `DescribeStreamSummary`: Returns the `MaxRecordSizeInKiB` field to show the current stream configuration.

All APIs listed maintain backward compatibility for existing streams. For complete API documentation, see the [Amazon Kinesis Data Streams Service API Reference](../../../kinesis/latest/APIReference/Welcome.md "../../../kinesis/latest/APIReference/Welcome.md").

## AWS components compatible with large records

The following AWS components are compatible with large records:

| Component                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS SDK                                  | AWS SDK supports handling large records. You can update your stream’s maximum record size<br>up-to 10 MiB using available methods in the AWS SDKs. For more<br>information, see [Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Kinesis Consumer Library (KCL)           | Starting with version 2.x, KCL supports handling large records. To use large record support,<br>update the `maxRecordSize` of your stream, and use KCL.<br>For more information, see [Use Kinesis Client Library](kcl.md "kcl.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Kinesis Producer Library (KPL)           | Starting with version 1.0.5, KPL supports handling large records. To use large record support, update the `maxRecordSize` of your stream, and use KPL. For more<br>information, see [Develop producers using the Amazon Kinesis Producer Library (KPL)](developing-producers-with-kpl.md "developing-producers-with-kpl.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Amazon EMR                               | Amazon EMR with Apache Spark supports handling large records up to the Kinesis Data Streams limit (10 MiBs). To<br>use large record support, use the `readStream` function.<br>For more information, see [Amazon EMR and Amazon Kinesis integration](../../../emr/latest/ReleaseGuide/emr-kinesis.md "../../../emr/latest/ReleaseGuide/emr-kinesis.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Amazon Data Firehose                     | When used with Kinesis Data Streams, the Amazon Data Firehose behavior with large records depends on the delivery<br>destination:<br>• Amazon S3: Delivery of large records is supported without any additional configuration. When you<br>use the [data format conversion](../../../firehose/latest/dev/record-format-conversion.md "../../../firehose/latest/dev/record-format-conversion.md"), delivery of large<br>records is supported with Firehose. When you use [dynamic partitioning](../../../firehose/latest/dev/dynamic-partitioning.md "../../../firehose/latest/dev/dynamic-partitioning.md"), delivery of large records<br>is not supported with Firehose.<br>• Lambda: We don't recommend using large records with Firehose when it triggers Lambda functions<br>downstream. This may lead to intermittent failures.<br>• HTTP: Delivery of large records is not supported with Firehose.<br>• Snowflake: Delivery of large records is not supported with Firehose.<br>• Amazon Redshift: Delivery of large records is not supported with Firehose.<br>For applications requiring delivery to Snowflake or Redshift with<br>large records, deliver the data to Amazon S3 first. After that, use<br>Extract, Transform, Load (ETL) processes to load the data. For all<br>other destinations, test the behavior with large records in a<br>proof-of-concept environment before scaling to production usage.<br>Handling large records varies by destination. |
| AWS Lambda                               | AWS Lambda supports payloads up to 6 MiBs. This limit includes the Kinesis payload converted to<br>base-64 encoding, and the metadata associated with Event Source<br>Mapping (ESM). For records less than 6 MiBs, Lambda processes them<br>using ESM with no additional configuration required. For records<br>larger than 6 MiBs, Lambda processes them using an on-failure<br>destination. You must configure an on-failure destination using ESM<br>to handle records that exceed Lambda's processing limits. Each event<br>sent to the on-failure destination is a JSON document that contains<br>metadata regarding the failed invocation.<br>It is recommended to create an on-failure destination in the ESM,<br>regardless of record size. This ensures that no records are<br>discarded. For more information, see [Configuring destinations for failed invocations](../../../lambda/latest/dg/kinesis-on-failure-destination.md#kinesis-on-failure-destination-console "../../../lambda/latest/dg/kinesis-on-failure-destination.md#kinesis-on-failure-destination-console").                                                                                                                                                                                                                                                                                                                                                                                    |
| Amazon Redshift                          | Amazon Redshift only supports record sizes less than 1 MiB when streaming data from Kinesis Data Streams. Records that<br>exceed this limit are not be processed. Records that are not<br>processed are logged as `sys_stream_scan_errors`. For<br>more information, see [SYS_STREAM_SCAN_ERRORS](../../../redshift/latest/dg/r_SYS_STREAM_SCAN_ERRORS.md "../../../redshift/latest/dg/r_SYS_STREAM_SCAN_ERRORS.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Flink connector for Kinesis Data Streams | There are two approaches for consuming data from Kinesis Data Streams: the Kinesis source connector, and the<br>Kinesis sink connector. The source connector supports handling records<br>less than 1 MiB, and up to 10 MiBs. Do not use the sink connector<br>for records larger than 1 MiB. For more information, see [Use connectors to move data in Amazon Managed Service for Apache Flink with the DataStream<br>API](../../../managed-flink/latest/java/how-connectors.md "../../../managed-flink/latest/java/how-connectors.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Regions where large records are supported

This Amazon Kinesis Data Streams feature is available only in the following AWS Regions:

| AWS Region     | Region Name               |
| -------------- | ------------------------- |
| eu-north-1     | Europe (Stockholm)        |
| me-south-1     | Middle East (Bahrain)     |
| ap-south-1     | Asia Pacific (Mumbai)     |
| eu-west-3      | Europe (Paris)            |
| ap-southeast-3 | Asia Pacific (Jakarta)    |
| us-east-2      | US East (Ohio)            |
| af-south-1     | Africa (Cape Town)        |
| eu-west-1      | Europe (Ireland)          |
| me-central-1   | Middle East (UAE)         |
| eu-central-1   | Europe (Frankfurt)        |
| sa-east-1      | South America (São Paulo) |
| ap-east-1      | Asia Pacific (Hong Kong)  |
| ap-south-2     | Asia Pacific (Hyderabad)  |
| us-east-1      | US East (N. Virginia)     |
| ap-northeast-2 | Asia Pacific (Seoul)      |
| ap-northeast-3 | Asia Pacific (Osaka)      |
| eu-west-2      | Europe (London)           |
| ap-southeast-4 | Asia Pacific (Melbourne)  |
| ap-northeast-1 | Asia Pacific (Tokyo)      |
| us-west-2      | US West (Oregon)          |
| us-west-1      | US West (N. California)   |
| ap-southeast-1 | Asia Pacific (Singapore)  |
| ap-southeast-2 | Asia Pacific (Sydney)     |
| il-central-1   | Israel (Tel Aviv)         |
| ca-central-1   | Canada (Central)          |
| ca-west-1      | Canada West (Calgary)     |
| eu-south-2     | Europe (Spain)            |
| cn-northwest-1 | China (Ningxia)           |
| eu-central-2   | Europe (Zurich)           |
| us-gov-east-1  | AWS GovCloud (US-East)    |
| us-gov-west-1  | AWS GovCloud (US-West)    |
