# Troubleshoot Kinesis Data Streams consumers

###### The following topics offer solutions to common issues with Amazon Kinesis Data Streams

consumers:

- [Compilation error with the LeaseManagementConfig constructor](#compilation-error-leasemanagementconfig "#compilation-error-leasemanagementconfig")
- [Some Kinesis Data Streams records are skipped when using the Kinesis Client
  Library](#records-skipped "#records-skipped")
- [Records belonging to the same
  shard are processed by different record processors at the same time](#records-belonging-to-the-same-shard "#records-belonging-to-the-same-shard")
- [The consumer application is reading at a
  slower rate than expected](#consumer-app-reading-slower "#consumer-app-reading-slower")
- [GetRecords returns an empty records array
  even when there is data in the stream](#getrecords-returns-empty "#getrecords-returns-empty")
- [The shard iterator expires
  unexpectedly](#shard-iterator-expires-unexpectedly "#shard-iterator-expires-unexpectedly")
- [Consumer record processing is falling
  behind](#record-processing-falls-behind "#record-processing-falls-behind")
- [Unauthorized KMS key permission
  error](#unauthorized-kms-consumer "#unauthorized-kms-consumer")
- [DynamoDbException: The document path provided in
  the update expression is invalid for update](#dynamo-db-exception "#dynamo-db-exception")
- [Troubleshoot other common issues for
  consumers](#misc-troubleshooting-consumer "#misc-troubleshooting-consumer")

## Compilation error with the LeaseManagementConfig constructor

When upgrading to Kinesis Client Library (KCL) version 3.x or later, you may encounter
a compilation error related to the `LeaseManagementConfig` constructor. If
you are directly creating a `LeaseManagementConfig` object to set
configurations instead of using `ConfigsBuilder` in KCL versions 3.x
or later, you might see the following error message while compiling your KCL
application code.

```
Cannot resolve constructor 'LeaseManagementConfig(String, DynamoDbAsyncClient, KinesisAsyncClient, String)'
```

KCL with versions 3.x or later requires you to add one more parameter,
applicationName (type: String), after the tableName parameter.

- _Before_: leaseManagementConfig = new
  LeaseManagementConfig(tableName, dynamoDBClient, kinesisClient, streamName,
  workerIdentifier)
- _After_: leaseManagementConfig = new
  LeaseManagementConfig(tableName, **applicationName**, dynamoDBClient, kinesisClient, streamName,
  workerIdentifier)

Instead of directly creating a LeaseManagementConfig object, we recommend using
`ConfigsBuilder` to set configurations in KCL 3.x and later
versions. `ConfigsBuilder` provides a more flexible and maintainable way to
configure your KCL application.

The following is an example of using `ConfigsBuilder` to set KCL
configurations.

```
ConfigsBuilder configsBuilder = new ConfigsBuilder(
    streamName,
    applicationName,
    kinesisClient,
    dynamoClient,
    cloudWatchClient,
    UUID.randomUUID().toString(),
    new SampleRecordProcessorFactory()
);

Scheduler scheduler = new Scheduler(
    configsBuilder.checkpointConfig(),
    configsBuilder.coordinatorConfig(),
    configsBuilder.leaseManagementConfig()
    .failoverTimeMillis(60000), // this is an example
    configsBuilder.lifecycleConfig(),
    configsBuilder.metricsConfig(),
    configsBuilder.processorConfig(),
    configsBuilder.retrievalConfig()
);
```

## Some Kinesis Data Streams records are skipped when using the Kinesis Client

Library

The most common cause of skipped records is an unhandled exception thrown from
`processRecords`. The Kinesis Client Library (KCL) relies on your
`processRecords` code to handle any exceptions that arise from processing
the data records. Any exception thrown from `processRecords` is absorbed by
the KCL. To avoid infinite retries on a recurring failure, the KCL does not resend
the batch of records processed at the time of the exception. The KCL then calls
`processRecords` for the next batch of data records without restarting
the record processor. This effectively results in consumer applications observing
skipped records. To prevent skipped records, handle all exceptions within
`processRecords` appropriately.

## Records belonging to the same

shard are processed by different record processors at the same time

For any running Kinesis Client Library (KCL) application, a shard only has one owner.
However, multiple record processors may temporarily process the same shard. If a worker
instance loses network connectivity, the KCL assumes that the unreachable worker is no
longer processing records after the failover time expires, and directs other worker
instances to take over. For a brief period, new record processors and record processors
from the unreachable worker may process data from the same shard.

Set a failover time that is appropriate for your application. For low-latency
applications, the 10-second default may represent the maximum time you want to wait.
However, in cases where you expect connectivity issues such as making calls across
geographical areas where connectivity could be lost more frequently, this number may be
too low.

Your application should anticipate and handle this scenario, especially because
network connectivity is usually restored to the previously unreachable worker. If a
record processor has its shards taken by another record processor, it must handle the
following two cases to perform graceful shutdown:

1. After the current call to `processRecords` is completed, the KCL
   invokes the shutdown method on the record processor with shutdown reason
   'ZOMBIE.' Your record processors are expected to clean up any resources as
   appropriate and then exit.
2. When you attempt to checkpoint from a 'zombie' worker, the KCL throws
   `ShutdownException`. After receiving this exception, your code is
   expected to exit the current method cleanly.

For more information, see [Handle duplicate records](kinesis-record-processor-duplicates.md "kinesis-record-processor-duplicates.md").

## The consumer application is reading at a

slower rate than expected

The most common reasons for read throughput being slower than expected are as
follows:

1. Multiple consumer applications have total reads exceeding the per-shard
   limits. For more information, see [Quotas and limits](service-sizes-and-limits.md "service-sizes-and-limits.md"). In this case, increase the
   number of shards in the Kinesis data stream.
2. The [limit](../../../kinesis/latest/APIReference/API_GetRecords.md#API_GetRecords_RequestSyntax "../../../kinesis/latest/APIReference/API_GetRecords.md#API_GetRecords_RequestSyntax") that specifies the maximum number of
   **GetRecords** per call may have been configured with a low
   value. If you are using the KCL, you may have configured the worker with a low
   value for the `maxRecords` property. In general, we recommend using
   the system defaults for this property.
3. The logic inside your `processRecords` call may be taking longer
   than expected for a number of possible reasons; the logic may be CPU intensive,
   I/O blocking, or bottlenecked on synchronization. To test if this is true, test
   run empty record processors and compare the read throughput. For information
   about how to keep up with the incoming data, see [Use resharding, scaling, and parallel
   processing to change the number of shards](kinesis-record-processor-scaling.md "kinesis-record-processor-scaling.md").

If you have only one consumer application, it is always possible to read at least two
times faster than the put rate. That’s because you can write up to 1,000 records per second for writes, up to a maximum total data write rate of 1 MB per second (including partition keys). Each
open shard can support up to 5 transactions per second for reads, up to a maximum total data read rate of 2 MB per second. Note that each read
(**GetRecords** call) gets a batch of records. The size of the data
returned by **GetRecords** varies depending on the utilization of the
shard. The maximum size of data that **GetRecords** can return is
10 MB. If a call returns that limit, subsequent calls made within the
next 5 seconds throw a `ProvisionedThroughputExceededException`.

## GetRecords returns an empty records array

even when there is data in the stream

Consuming, or getting records is a pull model. Developers are expected to call [GetRecords](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md") in a continuous loop with
no back-offs. Every call to **GetRecords** also returns a
`ShardIterator` value, which must be used in the next iteration of the
loop.

The **GetRecords** operation does not block. Instead, it returns
immediately; with either relevant data records or with an empty `Records`
element. An empty `Records` element is returned under two conditions:

1. There is no more data currently in the shard.
2. There is no data near the part of the shard pointed to by the
   `ShardIterator`.

The latter condition is subtle, but is a necessary design tradeoff to avoid unbounded
seek time (latency) when retrieving records. Thus, the stream-consuming application
should loop and call **GetRecords**, handling empty records as a matter
of course.

In a production scenario, the only time the continuous loop should be exited is when
the `NextShardIterator` value is `NULL`. When
`NextShardIterator` is `NULL`, it means that the current shard
has been closed and the `ShardIterator`value would otherwise point past the
last record. If the consuming application never calls **SplitShard** or
**MergeShards**, the shard remains open and the calls to
**GetRecords** never return a `NextShardIterator` value
that is `NULL`.

If you use the Kinesis Client Library (KCL), the preceding consumption pattern is
abstracted for you. This includes automatic handling of a set of shards that dynamically
change. With the KCL, the developer only supplies the logic to process incoming
records. This is possible because the library makes continuous calls to
**GetRecords** for you.

## The shard iterator expires

unexpectedly

A new shard iterator is returned by every **GetRecords** request (as
`NextShardIterator`), which you then use in the next
**GetRecords** request (as `ShardIterator`). Typically,
this shard iterator does not expire before you use it. However, you may find that shard
iterators expire because you have not called **GetRecords** for more than
5 minutes, or because you've performed a restart of your consumer application.

If the shard iterator expires immediately before you can use it, this might indicate
that the DynamoDB table used by Kinesis does not have enough capacity to store the lease data.
This situation is more likely to happen if you have a large number of shards. To solve
this problem, increase the write capacity assigned to the shard table. For more
information, see [Use a lease table to track
the shards processed by the KCL consumer application](shared-throughput-kcl-consumers.md#shared-throughput-kcl-consumers-leasetable "shared-throughput-kcl-consumers.md#shared-throughput-kcl-consumers-leasetable").

## Consumer record processing is falling

behind

For most use cases, consumer applications are reading the latest data from the stream.
In certain circumstances, consumer reads may fall behind, which may not be desired.
After you identify how far behind your consumers are reading, look at the most common
reasons why consumers fall behind.

Start with the `GetRecords.IteratorAgeMilliseconds` metric, which tracks
the read position across all shards and consumers in the stream. Note that if an
iterator's age passes 50% of the retention period (by
default,
24 hours, configurable up to
365
days), there is risk for data loss due to record expiration. A quick stopgap solution is
to increase the retention period. This stops the loss of important data while you
troubleshoot the issue further. For more information, see [Monitor the Amazon Kinesis Data Streams service with
Amazon CloudWatch](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md").
Next, identify how far behind your consumer application is reading from each shard using
a custom CloudWatch metric emitted by the Kinesis Client Library (KCL),
`MillisBehindLatest`. For more information, see [Monitor the Kinesis Client Library with
Amazon CloudWatch](monitoring-with-kcl.md "monitoring-with-kcl.md").

Here are the most common reasons consumers can fall behind:

- Sudden large increases to `GetRecords.IteratorAgeMilliseconds` or
  `MillisBehindLatest` usually indicate a transient problem, such
  as API operation failures to a downstream application. Investigate these sudden
  increases if either of the metrics consistently display this behavior.
- A gradual increase to these metrics indicates that a consumer is not keeping
  up with the stream because it is not processing records fast enough. The most
  common root causes for this behavior are insufficient physical resources or
  record processing logic that has not scaled with an increase in stream
  throughput. You can verify this behavior by looking at the other custom CloudWatch
  metrics that the KCL emits associated with the `processTask`
  operation, including `RecordProcessor.processRecords.Time`,
  `Success`, and `RecordsProcessed`.
  - If you see an increase in the `processRecords.Time` metric
    that correlates with increased throughput, you should analyze your
    record processing logic to identify why it is not scaling with the
    increased throughput.
  - If you see an increase to the `processRecords.Time` values
    that are not correlated with increased throughput, check to see if you
    are making any blocking calls in the critical path, which are often the
    cause of slowdowns in record processing. An alternative approach is to
    increase your parallelism by increasing the number of shards. Finally,
    confirm that you have an adequate amount of physical resources (memory,
    CPU utilization, among others) on the underlying processing nodes during
    peak demand.

## Unauthorized KMS key permission

error

This error occurs when a consumer application reads from an encrypted stream without
permissions on the AWS KMS key. To assign permissions to an application to access a
KMS key, see [Using Key Policies in AWS
KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") and [Using IAM Policies with
AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md").

## DynamoDbException: The document path provided in

the update expression is invalid for update

When using KCL 3.x with AWS SDK for Java versions 2.27.19 through 2.27.23, you may
encounter the following DynamoDB exception:

"software.amazon.awssdk.services.dynamodb.model.DynamoDbException: The document path
provided in the update expression is invalid for update (Service: DynamoDb, Status Code:
400, Request ID: xxx)"

This error occurs due to a known issue in the AWS SDK for Java that affects the DynamoDB
metadata table managed by KCL 3.x. The issue was introduced in version 2.27.19
and impacts all versions up to 2.27.23. The issue has been resolved in the AWS SDK for Java
version 2.27.24. For optimal performance and stability, we recommend upgrading to
version 2.28.0 or later.

## Troubleshoot other common issues for

consumers

- [Why is Kinesis Data Streams trigger unable to invoke my Lambda
  function?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-lambda-invocation/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-streams-lambda-invocation/")
- [How do I detect and troubleshoot ReadProvisionedThroughputExceeded
  exceptions in Kinesis Data Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-readprovisionedthroughputexceeded/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-readprovisionedthroughputexceeded/")
- [Why am I experiencing high latency issues with Kinesis Data
  Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-latency-issues/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-latency-issues/")
- [Why is my Kinesis data stream returning a 500 Internal Server
  Error?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-500-error/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-500-error/")
- [How do I troubleshoot a blocked or stuck KCL application for Kinesis Data
  Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kcl-kinesis-data-streams/ "https://aws.amazon.com/premiumsupport/knowledge-center/kcl-kinesis-data-streams/")
- [Can I use different Amazon Kinesis Client Library applications with the
  same Amazon DynamoDB table?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-kcl-apps-dynamodb-table/ "https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-kcl-apps-dynamodb-table/")
