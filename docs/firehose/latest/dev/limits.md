# Amazon Data Firehose Quota

This section describes current quotas, formerly referred to as limits, within Amazon Data Firehose.
Each quota applies on a per-Region basis unless otherwise specified.

The Service Quotas console is a central location where you can view and manage your quotas
for AWS services, and request a quota increase for many of the resources that you use. Use
the quota information that we provide to manage your AWS infrastructure. Plan to request
any quota increases in advance of the time that you'll need them.

For more information, see [Amazon Data Firehose endpoints and quotas](../../../general/latest/gr/fh.md "../../../general/latest/gr/fh.md") in the Amazon Web Services General Reference.

The following section shows Amazon Data Firehose has the following quota.

- With Amazon MSK as the source for the Firehose stream, each Firehose stream has a default
  quota of 10 MB/sec of read throughput per partition and 10MB max record size.
- With Amazon MSK as the source for the Firehose stream, there is a 6 MB maximum record
  size if AWS Lambda is enabled, and 10 MB maximum record size if Lambda is
  disabled. AWS Lambda caps its incoming record to 6 MB, and Amazon Data Firehose forwards
  records above 6Mb to an error S3 bucket. If Lambda is disabled, Firehose cap its
  incoming record to 10 MB. If Amazon Data Firehose receives a record size from Amazon MSK that
  is larger than 10 MB, then Amazon Data Firehose delivers this record to S3 error bucket and
  emits Cloudwatch metrics to your account. For more information on AWS Lambda
  limits, see [Lambda quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md").
- When [dynamic partitioning](dynamic-partitioning.md "dynamic-partitioning.md") on a
  Firehose stream is enabled, there is a default quota of 500 active partitions that can be
  created for that Firehose stream. The active partition count is the total number of
  active partitions within the delivery buffer. For example, if the dynamic
  partitioning query constructs 3 partitions per second and you have a buffer hint
  configuration that triggers delivery every 60 seconds, then, on average, you would
  have 180 active partitions. Once data is delivered in a partition, then this
  partition is no longer active. If you need more partitions, you can create more
  Firehose streams and distribute the active partitions across them.
- When [dynamic partitioning](dynamic-partitioning.md "dynamic-partitioning.md") on a Firehose stream is enabled, a max throughput

of 1 GB per second is supported for each active partition.

- Each account will have following quota for the number of Firehose streams per Region:
  - US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland), Asia Pacific
    (Tokyo): 5,000 Firehose streams
  - Europe (Frankfurt), Europe (London), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia
    Pacific (Seoul), Asia Pacific (Mumbai), AWS GovCloud (US-West), Canada
    (West), Canada (Central): 2,000 Firehose streams
  - Europe (Paris), Europe (Milan), Europe (Stockholm), Asia Pacific (Hong Kong), Asia Pacific
    (Osaka), South America (Sao Paulo), China (Ningxia), China (Beijing), Middle
    East (Bahrain), AWS GovCloud (US-East), Africa (Cape Town): 500
    Firehose streams
  - Europe (Zurich), Europe (Spain), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia
    Pacific (Melbourne), Middle East (UAE), Israel (Tel Aviv), Canada West
    (Calgary), Canada (Central), Asia Pacific (Malaysia),
    Asia Pacific (Thailand), Mexico (Central): 100 Firehose streams
  - If you exceed this number, a call to [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") results in a
    `LimitExceededException` exception. To increase this quota,
    you can use [Service Quotas](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/") if it's available in your Region. For
    information about using Service Quotas, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-increase.md "../../../servicequotas/latest/userguide/request-increase.md").

- When **Direct PUT** is configured as the data source, each
  Firehose stream provides the following combined quota for [PutRecord](../APIReference/API_PutRecord.md "../APIReference/API_PutRecord.md") and
  [PutRecordBatch](../APIReference/API_PutRecordBatch.md "../APIReference/API_PutRecordBatch.md") requests:

      + For US East (N. Virginia), US West (Oregon), and Europe (Ireland):
       500,000 records/second, 2,000 requests/second, and 5 MiB/second.
      + For other AWS Regions: 100,000 records/second, 1,000 requests/second,
       and 1 MiB/second.

  If a Direct PUT stream experiences throttling due to higher data ingest volumes
  that exceed the throughput capacity of a Firehose stream, Amazon Data Firehose automatically
  increases the throughput limit of the stream until the throttling is contained.
  Depending on increased throughput and throttling, it might take longer for Firehose to
  increase the throughput of a stream to the desired levels. Because of this, continue
  to retry the failed data ingest records. If you expect the data volume to increase
  in sudden large bursts, or if your new stream needs a higher throughput than the
  default throughput limit, request to increase the throughput limit.

There is three quota scale proportionally for quotas. For example, if you increase
the throughput quota in US East (N. Virginia), US West (Oregon), or
Europe (Ireland) to 10 MiB/second, the other two quota increase to 4,000
requests/second and 1,000,000 records/second.

###### Note

    + Do not use resource-level limits and quotas as a way to control
     your usage of the service.
    + When Kinesis Data Streams is configured as the data source, this quota doesn't apply, and
     Amazon Data Firehose scales up and down with no limit.
    + If the increased quota is much higher than the running traffic, it causes
     small delivery batches to destinations. This is inefficient and can result in
     higher costs at the destination services. Be sure to increase the quota only to
     match current running traffic, and increase the quota further if traffic
     increases.
    + Smaller data records can lead to higher costs. [Firehose ingestion pricing](https://aws.amazon.com/kinesis/data-firehose/pricing/ "https://aws.amazon.com/kinesis/data-firehose/pricing/") is based on the number of data records

     you send to the service, times the size of each record rounded up to the nearest
     5KB (5120 bytes). So, for the same volume of incoming data (bytes), if there is
     a greater number of incoming records, the cost incurred would be higher. For
     example, if the total incoming data volume is 5MiB, sending 5MiB of data over
     5,000 records costs more compared to sending the same amount of data using 1,000
     records. For more information, see Amazon Data Firehose in the [AWS
     Calculator](https://calculator.aws/#/createCalculator "https://calculator.aws/#/createCalculator").

- Each Firehose stream stores data records for up to 24 hours in case the delivery
  destination is unavailable and if the source is DirectPut. If the source is Kinesis
  Data Streams (KDS) and the destination is unavailable, then the data will be
  retained based on your KDS configuration.
- The maximum size of a record sent to Amazon Data Firehose, before base64-encoding, is 1,000
  KiB.
- The [PutRecordBatch](../APIReference/API_PutRecordBatch.md "../APIReference/API_PutRecordBatch.md") operation can take up to 500 records per call or
  4 MiB per call, whichever is smaller. This quota cannot be changed.
- Each of the following operations can provide up to five invocations per second,
  which is a hard limit.
  - [`CreateDeliveryStream`](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md")
  - [`DeleteDeliveryStream`](../APIReference/API_DeleteDeliveryStream.md "../APIReference/API_DeleteDeliveryStream.md")
  - [`DescribeDeliveryStream`](../APIReference/API_DescribeDeliveryStream.md "../APIReference/API_DescribeDeliveryStream.md")
  - [`ListDeliveryStreams`](../APIReference/API_ListDeliveryStreams.md "../APIReference/API_ListDeliveryStreams.md")
  - [`UpdateDestination`](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md")
  - [`TagDeliveryStream`](../APIReference/API_TagDeliveryStream.md "../APIReference/API_TagDeliveryStream.md")
  - [`UntagDeliveryStream`](../APIReference/API_UntagDeliveryStream.md "../APIReference/API_UntagDeliveryStream.md")
  - [`ListTagsForDeliveryStream`](../APIReference/API_ListTagsForDeliveryStream.md "../APIReference/API_ListTagsForDeliveryStream.md")
  - [`StartDeliveryStreamEncryption`](../APIReference/API_StartDeliveryStreamEncryption.md "../APIReference/API_StartDeliveryStreamEncryption.md")
  - [`StopDeliveryStreamEncryption`](../APIReference/API_StopDeliveryStreamEncryption.md "../APIReference/API_StopDeliveryStreamEncryption.md")

- The buffer interval hints range from 60 seconds to 900 seconds.
- For delivery from Amazon Data Firehose to Amazon Redshift, only publicly accessible Amazon Redshift clusters are
  supported.
- The retry duration range is from 0 seconds to 7,200 seconds for Amazon Redshift and
  OpenSearch Service delivery.
- When the destination is Amazon S3, Amazon Redshift, or OpenSearch Service, Amazon Data Firehose allows up to 5
  outstanding Lambda invocations per shard. For Splunk, the quota is 10 outstanding
  Lambda invocations per shard.
- You can use a CMK of type `CUSTOMER_MANAGED_CMK` to encrypt up to 500
  Firehose streams.
