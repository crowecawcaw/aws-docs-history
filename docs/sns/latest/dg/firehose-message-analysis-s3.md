# Analyzing Amazon SNS messages stored in Amazon S3 using

Athena

This page explains how to analyze Amazon SNS messages that are sent through delivery
streams to Amazon Simple Storage Service (Amazon S3) destinations.

###### To analyze SNS messages sent through Firehose delivery streams to Amazon S3

destinations

1. Configure your Amazon S3 resources. For instructions, see [Creating a bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the
   _Amazon Simple Storage Service User Guide_ and [Working with Amazon S3 Buckets](../../../AmazonS3/latest/userguide/UsingBucket.md "../../../AmazonS3/latest/userguide/UsingBucket.md") in the
   _Amazon Simple Storage Service User Guide_.
2. Configure your delivery stream. For instructions, see [Choose Amazon S3 for
   Your Destination](../../../firehose/latest/dev/create-destination.md#create-destination-s3 "../../../firehose/latest/dev/create-destination.md#create-destination-s3") in the _Amazon Data Firehose Developer Guide_.
3. Use [Amazon Athena](https://console.aws.amazon.com/athena "https://console.aws.amazon.com/athena") to query the Amazon S3 objects
   using standard SQL. For more information, see [Getting Started](../../../athena/latest/ug/getting-started.md "../../../athena/latest/ug/getting-started.md") in the
   _Amazon Athena User Guide_.

## Example query

For this example query, assume the following:

- Messages are stored in the `notifications` table in the
  `default` schema.
- The `notifications` table includes a `timestamp` column
  with a type of `string`.

The following query returns all SNS messages received in the specified date
range:

```
SELECT *
FROM default.notifications
WHERE from_iso8601_timestamp(timestamp) BETWEEN TIMESTAMP '2020-12-01 00:00:00' AND TIMESTAMP '2020-12-02 00:00:00';
```
