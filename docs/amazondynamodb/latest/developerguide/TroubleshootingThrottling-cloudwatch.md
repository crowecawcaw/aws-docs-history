# CloudWatch throttling metrics

This page provides a comprehensive guide to CloudWatch metrics specifically designed to help you
identify, diagnose, and resolve throttling issues in your DynamoDB tables and indexes.

**General throttling metrics**

- `ThrottledRequests`
  - Incremented by one when any event within a request is
    throttled, regardless of how many individual events within that
    request are throttled. For example, when updating an item in a
    table with Global Secondary Indexes (GSIs), multiple events
    occur: a write operation to the base table and a write operation
    to each index. If any of these individual events are throttled,
    the `ThrottledRequests` metric is only incremented
    once.

  This behavior is important to understand when monitoring and
  troubleshooting DynamoDB performance, as it may mask the true
  extent of throttling. For more comprehensive insights, compare
  the `ThrottledRequests` metric with the specific
  event-level metrics like `ReadThrottleEvents`,
  `WriteThrottleEvents`, and targeted metrics such
  as `ReadKeyRangeThroughputThrottleEvents` for
  example. The complete list of these cause-specific metrics is
  available in this page. Each metric corresponds to particular
  throttling reasons that are captured within the throttling
  exception. For guidance on retrieving and interpreting these
  reasons during throttling events, see the [Diagnosing throttling](throttling-diagnosing-workflow.md "throttling-diagnosing-workflow.md") section which
  provides instructions for identifying and resolving the root
  causes of throttling issues.

- `ReadThrottleEvents`
  - Watch for requests that exceed the provisioned RCU for a table
    or GSI.

- `WriteThrottleEvents`
  - Watch for requests that exceed the provisioned WCU for a table
    or GSI.

**Detailed throttling metrics by cause**

**On-Demand throughput throttling**

- `ReadMaxOnDemandThroughputThrottleEvents`
  - Number of read requests throttled due to on-demand maximum
    throughput.

- `WriteMaxOnDemandThroughputThrottleEvents`
  - Number of write requests throttled due to on-demand maximum
    throughput.

**Account-Level throttling**

- `ReadAccountLimitThrottleEvents`
  - Number of read requests throttled due to account
    limits.

- `WriteAccountLimitThrottleEvents`
  - Number of write requests throttled due to account
    limits.

**Partition-Level throttling**

- `ReadKeyRangeThroughputThrottleEvents`
  - Number of read requests throttled due to partition
    limits.

- `WriteKeyRangeThroughputThrottleEvents`
  - Number of write requests throttled due to partition
    limits.

**Capacity analysis metrics**

- `OnlineIndexConsumedWriteCapacity`
  - When you add a new GSI to an existing table, DynamoDB performs a
    backfill operation that copies data from the base table to the
    new index. This process consumes write capacity units. The
    `OnlineIndexConsumedWriteCapacity` metric tracks
    this specific consumption.

  This consumption is separate from and additional to the
  regular write operations tracked by
  `ConsumedWriteCapacityUnits`. The regular
  `ConsumedWriteCapacityUnits` metric for a GSI
  does not include the write capacity consumed during the initial
  index creation process.

- `ProvisionedReadCapacityUnits` and
  `ProvisionedWriteCapacityUnits`
  - View how many provisioned read or write capacity units were
    consumed over the specified time period, for a table or a
    specified global secondary index.
  - Note that the `TableName` dimension returns
    `ProvisionedReadCapacityUnits` for the table only
    by default. To view the number of provisioned read or write
    capacity units for a global secondary index, you must specify
    both `TableName` and
    `GlobalSecondaryIndexName`.

- `ConsumedReadCapacityUnits` and
  `ConsumedWriteCapacityUnits`
  - View how many read or write capacity units were consumed over
    the specified time period.
    `ConsumedWriteCapacityUnits` does not include the
    write capacity consumed during the initial index creation
    process.

For more information on DynamoDB CloudWatch metrics, see [DynamoDB Metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").
