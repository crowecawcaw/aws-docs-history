# Change data capture with Amazon DynamoDB

Many applications benefit from capturing changes to items stored in a DynamoDB table, at the
point in time when such changes occur. The following are some example use cases:

- A popular mobile app modifies data in a DynamoDB table, at the rate of thousands of
  updates per second. Another application captures and stores data about these
  updates, providing near-real-time usage metrics for the mobile app.
- A financial application modifies stock market data in a DynamoDB table. Different
  applications running in parallel track these changes in real time, compute
  value-at-risk, and automatically rebalance portfolios based on stock price
  movements.
- Sensors in transportation vehicles and industrial equipment send data to a
  DynamoDB table. Different applications monitor performance and send messaging alerts
  when a problem is detected, predict any potential defects by applying machine
  learning algorithms, and compress and archive data to Amazon Simple Storage Service
  (Amazon S3).
- An application automatically sends notifications to the mobile devices of all
  friends in a group as soon as one friend uploads a new picture.
- A new customer adds data to a DynamoDB table. This event invokes another application
  that sends a welcome email to the new customer.
  DynamoDB supports streaming of item-level change data capture records in near-real time.
  You can build applications that consume these streams and take action based on the
  contents.

###### Note

Adding tags to DynamoDB Streams and using [attribute-based access control (ABAC)](access-control-resource-based.md "access-control-resource-based.md") with DynamoDB Streams aren't supported.

The following video will give you an introductory look at the change data capture
concept.

###### Topics

- [Streaming options for change data capture](#streamsmain.choose "#streamsmain.choose")
- [Using Kinesis Data Streams to capture changes to DynamoDB](kds.md "kds.md")
- [Change data capture for DynamoDB Streams](Streams.md "Streams.md")

## Streaming options for change data capture

DynamoDB offers two streaming models for change data capture: Kinesis Data Streams for
DynamoDB and DynamoDB Streams.

To help you choose the right solution for your application, the following table
summarizes the features of each streaming model.

| Properties                               | Kinesis Data Streams for DynamoDB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | DynamoDB Streams                                                                                                                                |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Data retention**                       | Up to [1 year](../../../streams/latest/dev/kinesis-extended-retention.md "../../../streams/latest/dev/kinesis-extended-retention.md").                                                                                                                                                                                                                                                                                                                                                                                                           | 24 hours.                                                                                                                                       |
| **Kinesis Client Library (KCL) support** | Supports [KCL versions 1.X, 2.X, and 3.X](../../../streams/latest/dev/custom-kcl-consumers.md "../../../streams/latest/dev/custom-kcl-consumers.md").                                                                                                                                                                                                                                                                                                                                                                                            | Supports [KCL versions 1.X and 2.X](../../../streams/latest/dev/custom-kcl-consumers.md "../../../streams/latest/dev/custom-kcl-consumers.md"). |
| **Number of consumers**                  | Up to [5 simultaneous](../../../streams/latest/dev/service-sizes-and-limits.md "../../../streams/latest/dev/service-sizes-and-limits.md") consumers per shard, or up to 20 simultaneous consumers per shard with [enhanced fan-out](../../../streams/latest/dev/enhanced-consumers.md "../../../streams/latest/dev/enhanced-consumers.md").                                                                                                                                                                                                      | Up to [2 simultaneous](Limits.md#limits-dynamodb-streams "Limits.md#limits-dynamodb-streams") consumers per shard.                              |
| **Throughput quotas**                    | Unlimited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Subject to throughput [quotas](Limits.md#limits-dynamodb-streams "Limits.md#limits-dynamodb-streams") by DynamoDB table and AWS Region.         |
| **Record delivery model**                | Pull model over HTTP using [GetRecords](../../../kinesis/latest/APIReference/API_GetRecords.md "../../../kinesis/latest/APIReference/API_GetRecords.md") and with [enhanced fan-out](../../../streams/latest/dev/enhanced-consumers.md "../../../streams/latest/dev/enhanced-consumers.md"), Kinesis Data Streams pushes the records over HTTP/2 by using [SubscribeToShard](../../../kinesis/latest/APIReference/API_SubscribeToShard.md "../../../kinesis/latest/APIReference/API_SubscribeToShard.md").                                       | Pull model over HTTP using [GetRecords](../APIReference/API_streams_GetRecords.md "../APIReference/API_streams_GetRecords.md").                 |
| **Ordering of records**                  | The timestamp attribute on each stream record can be used to identify the actual order in which changes occurred in the DynamoDB table.                                                                                                                                                                                                                                                                                                                                                                                                          | For each item that is modified in a DynamoDB table, the stream records appear in the same sequence as the actual modifications to the item.     |
| **Duplicate records**                    | Duplicate records might occasionally appear in the stream.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No duplicate records appear in the stream.                                                                                                      |
| **Stream processing options**            | Process stream records using [AWS Lambda](../../../lambda/latest/dg/with-kinesis.md "../../../lambda/latest/dg/with-kinesis.md"), [Amazon Managed Service for Apache Flink](../../../kinesisanalytics/latest/dev/what-is.md "../../../kinesisanalytics/latest/dev/what-is.md"), [Kinesis data firehose](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md") , or [AWS Glue streaming ETL](../../../glue/latest/dg/add-job-streaming.md "../../../glue/latest/dg/add-job-streaming.md"). | Process stream records using [AWS Lambda](Streams.md "Streams.md") or [DynamoDB Streams Kinesis adapter](Streams.md "Streams.md").              |
| **Durability level**                     | [Availability zones](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") to provide automatic failover without interruption.                                                                                                                                                                                                                                                                                                                                                                                                      | [Availability zones](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md") to provide automatic failover without interruption.     | You can enable both streaming models on the same DynamoDB table. The following video talks more about the differences between the two options. |
