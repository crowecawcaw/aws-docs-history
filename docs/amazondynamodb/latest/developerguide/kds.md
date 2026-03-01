# Using Kinesis Data Streams to capture changes to DynamoDB

You can use Amazon Kinesis Data Streams to capture changes to Amazon DynamoDB.

Kinesis Data Streams captures item-level modifications in any DynamoDB table and replicates them to a [Kinesis data
stream](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md"). Your applications can access this stream and view item-level changes in
near-real time. You can continuously capture and store terabytes of data per hour. You can
take advantage of longer data retention time—and with enhanced fan-out capability,
you can simultaneously reach two or more downstream applications. Other benefits include
additional audit and security transparency.

Kinesis Data Streams also gives you access to [Amazon Data Firehose](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md") and [Amazon Managed Service for Apache Flink](../../../kinesisanalytics/latest/dev/what-is.md "../../../kinesisanalytics/latest/dev/what-is.md").
These services can help you build applications that power real-time dashboards, generate
alerts, implement dynamic pricing and advertising, and implement sophisticated data
analytics and machine learning algorithms.

###### Note

Using Kinesis data streams for DynamoDB is subject to both [Kinesis Data Streams pricing](https://aws.amazon.com/kinesis/data-streams/pricing/ "https://aws.amazon.com/kinesis/data-streams/pricing/") for
the data stream and [DynamoDB
pricing](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/") for the source table.

To enable Kinesis streaming on a DynamoDB table using the console, AWS CLI, or Java SDK, see
[Getting started with Kinesis Data Streams for Amazon DynamoDB](kds_gettingstarted.md "kds_gettingstarted.md").

###### Topics

- [How Kinesis Data Streams works with DynamoDB](#kds_howitworks "#kds_howitworks")
- [Getting started with Kinesis Data Streams for Amazon DynamoDB](kds_gettingstarted.md "kds_gettingstarted.md")
- [Using shards and metrics with DynamoDB Streams and Kinesis Data Streams](kds_using-shards-and-metrics.md "kds_using-shards-and-metrics.md")
- [Using IAM policies for Amazon Kinesis Data Streams and Amazon DynamoDB](kds_iam.md "kds_iam.md")

## How Kinesis Data Streams works with DynamoDB

When a Kinesis data stream is enabled for a DynamoDB table, the table sends out a data record
that captures any changes to that table’s data. This data record includes:

- The specific time any item was recently created, updated, or deleted
- That item’s primary key
- A snapshot of the record before the modification
- A snapshot of the record after the modification

These data records are captured and published in near-real time. After they are written to
the Kinesis data stream, they can be read just like any other record.
You
can use the Kinesis Client Library, use AWS Lambda, call the Kinesis Data Streams API, and use other connected
services. For more information, see [Reading Data from Amazon Kinesis Data Streams](../../../streams/latest/dev/building-consumers.md "../../../streams/latest/dev/building-consumers.md") in
the Amazon Kinesis Data Streams Developer Guide.

These changes to data are also captured asynchronously. Kinesis has no performance impact on
a table that it’s streaming from. The stream records stored in your Kinesis data stream are
also encrypted at rest. For more information, see [Data Protection in
Amazon Kinesis Data Streams](../../../streams/latest/dev/server-side-encryption.md "../../../streams/latest/dev/server-side-encryption.md").

The Kinesis data stream records might appear in a different order than when the item changes occurred. The same item notifications might also appear more than once in the stream. You can check the `ApproximateCreationDateTime` attribute to identify the order that the item modifications occurred in, and to identify duplicate records.

When you enable a Kinesis data stream as a streaming destination of a DynamoDB table, you can configure the precision of `ApproximateCreationDateTime` values in either milliseconds or microseconds. By default, `ApproximateCreationDateTime` indicates the time of the change in milliseconds. Additionally, you can change this value on an active streaming destination. After such an update, stream records written to Kinesis will have `ApproximateCreationDateTime` values of the desired precision.

Binary values written to DynamoDB must be encoded in [base64-encoded format](HowItWorks.md "HowItWorks.md") . However, when
data records are written to a Kinesis data stream, these encoded binary values are encoded
with base64-encoding a second time. When reading these records from a Kinesis data stream,
in order to retrieve the raw binary values, applications must decode these values
twice.

DynamoDB charges for using Kinesis Data Streams in change data capture units. 1 KB of change per single item
counts as one change data capture unit. The KB of change in each item is calculated by the
larger of the “before” and “after” images of the item written to the stream, using the same
logic as [capacity unit consumption for write operations](read-write-operations.md#write-operation-consumption "read-write-operations.md#write-operation-consumption"). Similar to how DynamoDB [on-demand](capacity-mode.md#capacity-mode-on-demand "capacity-mode.md#capacity-mode-on-demand") mode works, you don't need to provision capacity throughput for
change data capture units.

### Turning on a Kinesis data stream for your DynamoDB table

You can enable or disable streaming to Kinesis from your existing DynamoDB table by using
the AWS Management Console, the AWS SDK, or the AWS Command Line Interface (AWS CLI).

- You can only stream data from DynamoDB to Kinesis Data Streams in the same AWS account and
  AWS Region as your table.
- You can only stream data from a DynamoDB table to one Kinesis data stream.

### Making changes to a Kinesis Data Streams destination on your DynamoDB table

By default, all Kinesis data stream records include an `ApproximateCreationDateTime` attribute. This attribute represents a timestamp in milliseconds of the approximate time when each record was created. You can change the precision of these values by using the [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis"), the SDK or the AWS CLI
