# DynamoDB metadata tables and load balancing in

KCL

KCL manages metadata such as leases and CPU utilization metrics from workers.
KCL tracks these metadata using DynamoDB tables. For each Amazon Kinesis Data Streams application,
KCL creates three DynamoDB tables to manage the metadata: lease table, worker
metrics table, and coordinator state table.

###### Note

KCL 3.x introduced two new metadata tables: _worker
metrics_ and _coordinator state_ tables.

###### Important

You must add proper permissions for KCL applications to create and
manage metadata tables in DynamoDB. For details, see [IAM permissions required for KCL
consumer applications](kcl-iam-permissions.md "kcl-iam-permissions.md").

KCL consumer application does not automatically remove these three DynamoDB
metadata tables. Make sure that you remove these DynamoDB metadata tables created by
KCL consumer application when you decommission your consumer application to
prevent unnecessary cost.

## Lease

table

A lease table is a unique Amazon DynamoDB table used to track the shards being leased
and processed by the schedulers of the KCL consumer application. Each
KCL consumer application creates its own lease table. KCL uses the
name of the consumer application for the name of the lease table by default. You can
set a custom table name using configuration. KCL also creates a [global secondary index](../../../amazondynamodb/latest/developerguide/GSI.md "../../../amazondynamodb/latest/developerguide/GSI.md") on the lease table with the partition key of
leaseOwner for an efficient lease discovery. Global secondary index mirrors the
leaseKey attribute from the base lease table. If the lease table for your
KCL consumer application does not exist when the application starts up, one
of the workers creates the lease table for your application.

You can view the lease table using the [Amazon DynamoDB console](../../../amazondynamodb/latest/developerguide/ConsoleDynamoDB.md "../../../amazondynamodb/latest/developerguide/ConsoleDynamoDB.md") while the
consumer application is running.

###### Important

- Each KCL consumer application name must be unique to prevent
  a duplicated lease table name.
- Your account is charged for the costs associated with the DynamoDB table,
  in addition to the costs associated with Kinesis Data Streams itself.

Each row in the lease table represents a shard that is being processed by the
schedulers of your consumer application. Key fields include the following:

- **leaseKey:** For single-stream processing,
  this is the shard ID. For multi-stream processing with KCL, it's
  structured as
  `account-id:StreamName:streamCreationTimestamp:ShardId`.
  leaseKey is the partition key of the lease table. For more information about
  multi-stream processing, see [Multi-stream processing with KCL](kcl-multi-stream.md "kcl-multi-stream.md") .
- **checkpoint:** The most recent checkpoint
  sequence number for the shard.
- **checkpointSubSequenceNumber:** When using
  the Kinesis Producer Library's aggregation feature, this is an extension to
  **checkpoint** that tracks individual user
  records within the Kinesis record.
- **leaseCounter:** Used for checking if a
  worker is currently processing the lease actively. leaseCounter increases if
  the lease ownership is transferred to another worker.
- **leaseOwner:** The current worker that is
  holding this lease.
- **ownerSwitchesSinceCheckpoint:** How many
  times this lease has changed workers since the last checkpoint.
- **parentShardId:** ID of this shard's parent.
  Makes sure that the parent shard is fully processed before processing starts
  on the child shards, maintaining the correct record processing order.
- **childShardId:** List of child shard IDs
  resulting from this shard's split or merge. Used to track shard lineage and
  manage processing order during resharding operations.
- **startingHashKey:** The lower bound of the
  hash key range for this shard.
- **endingHashKey:** The upper bound of the
  hash key range for this shard.

If you use multi-stream processing with KCL, you see the following two
additional fields in the lease table. For more information, see [Multi-stream processing with KCL](kcl-multi-stream.md "kcl-multi-stream.md") .

- **shardID:** The ID of the shard.
- **streamName:** The identifier of the data stream
  in the following format:
  `account-id:StreamName:streamCreationTimestamp`.

## Worker metrics

table

Worker metrics table is a unique Amazon DynamoDB table for each KCL application
and is used to record CPU utilization metrics from each worker. These metrics will
be used by KCL to perform efficient lease assignments to result in balanced resource
utilization across workers. KCL uses
`KCLApplicationName-WorkerMetricStats` for the name of the worker
metrics table by default.

## Coordinator state table

A coordinator state table is a unique Amazon DynamoDB table for each KCL
application and is used to store internal state information for workers. For
example, the coordinator state table stores data regarding the leader election or
metadata associated with the in-place migration from KCL 2.x to
KCL 3.x. KCL uses `KCLApplicationName-CoordinatorState`
for the name of the coordinator state table by default.

## DynamoDB capacity mode for metadata tables created

by KCL

By default, the Kinesis Client Library (KCL) creates DynamoDB metadata tables
such as lease table, worker metrics table, and coordinator state table using the
[on-demand capacity mode](../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md "../../../amazondynamodb/latest/developerguide/on-demand-capacity-mode.md"). This mode automatically scales read and write
capacity to accommodate traffic without requiring capacity planning. We strongly
recommend you to keep the capacity mode as on-demand mode for more efficient
operation of these metadata tables.

If you decide to switch the lease table to [provisioned capacity mode](../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md "../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md"), follow these best practices:

- Analyze usage patterns:
  - Monitor your application's read and write patterns and usages
    (RCU, WCU) using Amazon CloudWatch metrics.
  - Understand peak and average throughput requirements.

- Calculate the required capacity:
  - Estimate read capacity units (RCUs) and write capacity units
    (WCUs) based on your analysis.
  - Consider factors like the number of shards, checkpoint frequency,
    and worker count.

- Implement auto scaling:
  - Use [DynamoDB auto scaling](../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md#ddb-autoscaling "../../../amazondynamodb/latest/developerguide/provisioned-capacity-mode.md#ddb-autoscaling") to automatically adjust provisioned
    capacity and set appropriate minimum and maximum capacity limits.
  - DynamoDB auto scaling will help to avoid your KCL metadata
    table from hitting the capacity limit and getting throttled.

- Regular monitoring and optimization:
  - Continuously monitor CloudWatch metrics for
    `ThrottledRequests`.
  - Adjust capacity as your workload changes over time.

If you experience a `ProvisionedThroughputExceededException` in
metadata DynamoDB tables for your KCL consumer application, you must increase
the provisioned throughput capacity of the DynamoDB table. If you set a certain level
of read capacity units (RCU) and write capacity units (WCU) when you first create
your consumer application, it might not be sufficient as your usage grows. For
example, if your KCL consumer application does frequent checkpointing or
operates on a stream with many shards, you might need more capacity units. For
information about provisioned throughput in DynamoDB, see [DynamoDB throughput capacity](../../../amazondynamodb/latest/developerguide/capacity-mode.md "../../../amazondynamodb/latest/developerguide/capacity-mode.md") and [updating a table](../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.UpdateTable "../../../amazondynamodb/latest/developerguide/WorkingWithTables.md#WorkingWithTables.Basics.UpdateTable") in the Amazon DynamoDB Developer Guide.

## How KCL assigns leases to workers and

balances the load

KCL continuously gathers and monitors CPU utilization metrics from
compute hosts running the workers to ensure even workload distribution. These CPU
utilization metrics are stored in the worker metrics table in DynamoDB. If KCL
detects that some workers are showing higher CPU utilization rates compared to
others, it will reassign leases among workers to lower the load on highly used
workers. The goal is to balance the workload more evenly across the consumer
application fleet, preventing any single worker from becoming overloaded. As
KCL distributes CPU utilization across the consumer application fleet, you
can right-size your consumer application fleet capacity by choosing the right number
of workers or use auto scaling to efficiently manage the computing capacity to
achieve lower cost.

###### Important

KCL can collect CPU utilization metrics from workers only if certain
prerequisites are met. For details, see [Prerequisites](develop-kcl-consumers-java.md#develop-kcl-consumers-java-prerequisites "develop-kcl-consumers-java.md#develop-kcl-consumers-java-prerequisites"). If KCL
cannot collect CPU utilization metrics from workers, KCL will fall back
to using throughput per worker to assign leases and balance the load across
workers in the fleet. KCL will monitor the throughput that each worker
receives at a given time and reassign leases to make sure that each worker gets
a similar total throughput level from its assigned leases.
