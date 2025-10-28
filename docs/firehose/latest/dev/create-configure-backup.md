# Configure backup settings

Amazon Data Firehose uses Amazon S3 to backup all or failed only data that it
attempts to deliver to your chosen destination.

###### Important

- Backup settings are only supported if the source for your Firehose stream is
  Direct PUT or Kinesis Data Streams.
- Zero buffering feature is only available for the application destinations
  and is not available for Amazon S3 backup destination.
  You can specify the S3 backup settings for your Firehose stream if you made one of the
  following choices.

- If you set Amazon S3 as the destination for your Firehose stream and you choose to
  specify an AWS Lambda function to transform data records or if you choose to
  convert data record formats for your Firehose stream.
- If you set Amazon Redshift as the destination for your Firehose stream and you
  choose to specify an AWS Lambda function to transform data records.
- If you set any of the following services as the destination for your
  Firehose stream – Amazon OpenSearch Service, Datadog, Dynatrace, HTTP
  Endpoint, LogicMonitor, MongoDB Cloud, New Relic, Splunk, or Sumo Logic,
  Snowflake, Apache Iceberg Tables.
  The following are the backup settings for your Firehose stream.

- Source record backup in Amazon S3 - if S3 or Amazon Redshift is your selected
  destination, this setting indicates whether you want to enable source data
  backup or keep it disabled. If any other supported service (other than S3 or
  Amazon Redshift) is set as your selected destination, then this setting
  indicates if you want to backup all your source data or failed data only.
- S3 backup bucket - this is the S3 bucket where Amazon Data Firehose backs up
  your data.
- S3 backup bucket prefix - this is the prefix where Amazon Data Firehose backs
  up your data.
- S3 backup bucket error output prefix - all failed data is backed up in the
  this S3 bucket error output prefix.
- Buffering hints, compression and encryption for backup - Amazon Data Firehose
  uses Amazon S3 to backup all or failed only data that it attempts to deliver to
  your chosen destination. Amazon Data Firehose buffers incoming data before
  delivering it (backing it up) to Amazon S3. You can choose a buffer size of
  1–128 MiBs and a buffer interval of 60–900 seconds. The condition that is
  satisfied first triggers data delivery to Amazon S3. If you enable data
  transformation, the buffer interval applies from the time transformed data is
  received by Amazon Data Firehose to the data delivery to Amazon S3. If data
  delivery to the destination falls behind data writing to the Firehose stream,
  Amazon Data Firehose raises the buffer size dynamically to catch up. This
  action helps ensure that all data is delivered to the destination.
- S3 compression - choose GZIP, Snappy, Zip, or Hadoop-Compatible Snappy data
  compression, or no data compression. Snappy, Zip, and Hadoop-Compatible Snappy
  compression is not available for Firehose stream with Amazon Redshift as the destination.
- S3 file extension format (optional) – Specify a file extension format for objects delivered to Amazon S3 destination bucket. If you enable this feature, specified file extension will override default file extensions appended by Data Format Conversion or S3 compression features such as .parquet or .gz. Make sure if you configured the right file extension when you use this feature with Data Format Conversion or S3 compression. File extension must start with a period (.) and can contain allowed characters: 0-9a-z!-\_.\*‘().
  File extension cannot exceed 128 characters.
- Firehose supports Amazon S3 server-side encryption with AWS Key Management Service (SSE-KMS) for encrypting delivered data in Amazon S3.

You can choose to use the default encryption type specified in the destination S3 bucket or to encrypt with a key from the list of AWS KMS keys that you own.
If you encrypt the data with AWS KMS keys, you can use either the default AWS managed key (aws/s3) or a customer managed key. For more information, see [Protecting Data Using Server-Side Encryption with AWS KMS-Managed Keys
(SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

## Configure buffering hints

Amazon Data Firehose buffers incoming streaming data in memory to a certain size (buffering size) and for a certain period of time (buffering interval) before delivering it to the specified destinations.
You would use buffering hints when you want to deliver optimal sized files to Amazon S3 and get better performance from data processing applications or to adjust Firehose delivery rate to match destination speed.

You can configure the buffering size and the buffer interval while creating new Firehose streams or update the buffering size and the buffering interval on your existing Firehose streams. Buffering size is measured in MBs
and buffering interval is measured in seconds. However, if you specify a value for one of them, you must also provide a value for the other. The first buffer condition that is satisfied triggers Firehose to deliver the data. If you don't configure the buffering values, then the default values are used.

You can configure Firehose buffering hints through the AWS Management Console, AWS Command Line Interface, or AWS SDKs. For existing streams, you can
reconfigure buffering hints with a value that suits your use cases using the **Edit**
option in the console or using the [UpdateDestination](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md") API.
For new streams, you can configure buffering hints as part of new stream creation using the console or using the [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") API.

To adjust the buffering size, set `SizeInMBs` and `IntervalInSeconds` in the destination specific `DestinationConfiguration`
parameter of the [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md")
or [UpdateDestination](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md") API.

###### Note

- Buffer hints are applied on a shard or partition level, while dynamic
  partitioning buffer hints are applied on stream or topic level.
- To meet lower latencies of real-time use cases, you can use zero buffering
  interval hint. When you configure buffering interval as zero seconds, Firehose
  will not buffer data and will deliver data within a few seconds. Before you
  change buffering hints to a lower value, check with the vendor for
  recommended buffering hints of Firehose for their destinations.
- Zero buffering feature is only available for the application destinations and is not available for Amazon S3 backup destination.
- Zero buffering feature is not available for dynamic partitioning.
- Firehose uses multi-part upload for S3 destination when you configure a
  buffer time interval less than 60 seconds to offer lower latencies. Due to
  multi-part upload for S3 destination, you will see some increase in S3
  `PUT` API costs if you choose a buffer time interval less
  than 60 seconds.

For destination specific buffering hint ranges and default values, see the following table:

| Destination                | Buffering size in MB (default in parenthesis) | Buffering interval in seconds (default in parenthesis) |
| -------------------------- | --------------------------------------------- | ------------------------------------------------------ |
| Amazon S3                  | 1-128 (5)                                     | 0-900 (300)                                            |
| Apache Iceberg Tables      | 1-128 (5)                                     | 0-900 (300)                                            |
| Amazon Redshift            | 1-128 (5)                                     | 0-900 (300)                                            |
| OpenSearch Serverless      | 1-100 (5)                                     | 0-900 (300)                                            |
| OpenSearch                 | 1-100 (5)                                     | 0-900 (300)                                            |
| Splunk                     | 1-5 (5)                                       | 0-60 (60)                                              |
| Datadog                    | 1-4 (4)                                       | 0-900 (60)                                             |
| Coralogix                  | 1-64 (6)                                      | 0-900 (60)                                             |
| Dynatrace                  | 1-64 (5)                                      | 0-900 (60)                                             |
| Elastic                    | 1                                             | 0-900 (60)                                             |
| Honeycomb                  | 1-64 (15)                                     | 0-900 (60)                                             |
| HTTP endpoint              | 1-64 (5)                                      | 0-900 (60)                                             |
| LogicMonitor               | 1-64 (5)                                      | 0-900 (60)                                             |
| Logzio                     | 1-64 (5)                                      | 0-900 (60)                                             |
| mongoDB                    | 1-16 (5)                                      | 0-900 (60)                                             |
| newRelic                   | 1-64 (5)                                      | 0-900 (60)                                             |
| sumoLogic                  | 1-64 (1)                                      | 0-900 (60)                                             |
| Splunk Observability Cloud | 1-64 (1)                                      | 0-900 (60)                                             |
| Snowflake                  | 1 - 128 (1)                                   | 0 - 900 (0)                                            |
