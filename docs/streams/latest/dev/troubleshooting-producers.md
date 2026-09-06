

# Troubleshoot Amazon Kinesis Data Streams producers
<a name="troubleshooting-producers"></a>

**Topics**
+ [My producer application is writing at a slower rate than expected](#producer-writing-at-slower-rate)
+ [I receive an unauthorized KMS master key permission error](#unauthorized-kms-producer)
+ [Troubleshoot other common issues for producers](#misc-troubleshooting-producer)

## My producer application is writing at a slower rate than expected
<a name="producer-writing-at-slower-rate"></a>

**Topics**
+ [Service limits exceeded](#service-limits-exceeded)
+ [I want to optimize my producer](#producer-optimization)
+ [Misuse of `flushSync()` operations](#misuse-tag)

### Service limits exceeded
<a name="service-limits-exceeded"></a>

To find out if service limits are being exceeded, check to see if your producer is throwing throughput exceptions from the service, and validate what API operations are being throttled. Keep in mind that there are different limits based on the call, see [Quotas and limits](service-sizes-and-limits.md). For example, in addition to the shard-level limits for writes and reads that are most commonly known, there are the following stream-level limits:
+ [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html)
+ [DeleteStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeleteStream.html)
+ [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html)
+ [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html)
+ [MergeShards](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_MergeShards.html)
+ [DescribeStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStream.html)
+ [DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html)

The operations `CreateStream`, `DeleteStream`, `ListStreams`, `GetShardIterator`, and `MergeShards` are limited to 5 calls per second. The `DescribeStream` operation is limited to 10 calls per second. The `DescribeStreamSummary` operation is limited to 20 calls per second.

If these calls aren't the issue, make sure you've selected a partition key that allows you to distribute *put* operations evenly across all shards, and that you don't have a particular partition key that's bumping into the service limits when the rest are not. This requires that you measure peak throughput and take into account the number of shards in your stream. For more information about managing streams, see [Create and manage Kinesis data streams](working-with-streams.md).

**Tip**  
Remember to round up to the nearest kilobyte for throughput throttling calculations when using the single-record operation [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html), while the multi-record operation [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html) rounds on the cumulative sum of the records in each call. For example, a `PutRecords` request with 600 records that are 1.1 KB in size will not get throttled. 

### I want to optimize my producer
<a name="producer-optimization"></a>

Before you begin optimizing your producer, complete the following key tasks. First, identify your desired peak throughput in terms of record size and records per second. Next, rule out stream capacity as the limiting factor ([Service limits exceeded](#service-limits-exceeded)). If you've ruled out stream capacity, use the following troubleshooting tips and optimization guidelines for the two common types of producers.

**Large Producer**

A large producer is usually running from an on-premises server or Amazon EC2 instance. Customers who need higher throughput from a large producer typically care about per-record latency. Strategies for dealing with latency include the following: If the customer can micro-batch/buffer records, use the [Amazon Kinesis Producer Library](https://docs.aws.amazon.com/kinesis/latest/dev/developing-producers-with-kpl.html) (which has advanced aggregation logic), the multi-record operation [PutRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html), or aggregate records into a larger file before using the single-record operation [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html). If you are unable to batch/buffer, use multiple threads to write to the Kinesis Data Streams service at the same time. The AWS SDK for Java and other SDKs include async clients that can do this with very little code.

**Small Producer**

A small producer is usually a mobile app, IoT device, or web client. If it’s a mobile app, we recommend using the `PutRecords` operation or the Kinesis Recorder in the AWS Mobile SDKs. For more information, see AWS Mobile SDK for Android Getting Started Guide and AWS Mobile SDK for iOS Getting Started Guide. Mobile apps must handle intermittent connections inherently and need some sort of batch put, such as `PutRecords`. If you are unable to batch for some reason, see the Large Producer information above. If your producer is a browser, the amount of data being generated is typically very small. However, you are putting the *put* operations on the critical path of the application, which we don’t recommend.

### Misuse of `flushSync()` operations
<a name="misuse-tag"></a>

Using `flushSync()` incorrectly can significantly impact write performance. The `flushSync()` operation is designed for shutdown scenarios to make sure that all buffered records are sent before the KPL application terminates. If you implemented this operation after every write operation, it can add substantial extra latency, around 500ms per write. Make sure that you have implemented `flushSync()` only for the application shutdown to avoid unnecessary extra delay in write performance. 

## I receive an unauthorized KMS master key permission error
<a name="unauthorized-kms-producer"></a>

This error occurs when a producer application writes to an encrypted stream without permissions on the KMS master key. To assign permissions to an application to access a KMS key, see [Using Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and [Using IAM Policies with AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html).

## Troubleshoot other common issues for producers
<a name="misc-troubleshooting-producer"></a>
+ [Why is my Kinesis data stream returning a 500 Internal Server Error?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-500-error/)
+ [How do I troubleshoot timeout errors when writing from Flink to Kinesis Data Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-flink-timeout/)
+ [How do I troubleshoot throttling errors in Kinesis Data Streams?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-throttling-errors/)
+ [Why is my Kinesis data stream throttling?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-throttling/)
+ [How can I put data records into a Kinesis data stream using the KPL?](https://aws.amazon.com/premiumsupport/knowledge-center/kinesis-data-stream-kpl/)