# 1- Key range throughput

exceeded (hot partitions)

Amazon DynamoDB enforces specific throughput limits at the partition level for both table and
global secondary index (GSI). Each partition has a maximum number of read capacity units
(RCUs) and write capacity units (WCUs) per second. When partitions receive concentrated
traffic that exceeds these limits, they experience throttling while other operations may
remain underutilized, creating "hot partitions." DynamoDB's partition-level throttling operates
independently for reads and writes - a partition may throttle reads while writes continue
normally, or vice versa. This throttling can occur even when your table or GSI has
sufficient overall capacity. To learn more about:

- DynamoDB partition limits and effective partition key design addressing hot partition
  prevention, see [Best practices for designing
  and using partition keys effectively in DynamoDB](bp-partition-key-design.md "bp-partition-key-design.md").
- General partition concepts and data distribution, see [Partitions in DynamoDB](HowItWorks.md "HowItWorks.md").
- Additional guidance and real-world scenarios for managing partition keys and
  throughput, see [Additional resources](#key-range-additional-resources "#key-range-additional-resources").
  When individual partitions exceed their throughput limits, DynamoDB returns a
  `KeyRangeThroughputExceeded` throttling reason type in the throttling
  exception. The information identifies that a partition is experiencing high traffic and
  which operation type (read or write) is causing the issue.

## Key range throughput exceeded

mitigation measures

This section provides resolution guidance for partition-level throttling scenarios.
Before using this guide, ensure you have identified the specific throttling reasons from
your application's exception handling, and determined the Amazon Resource Name (ARN) of
the affected resource. For information on retrieving throttling reasons and identifying
throttled resources, see [DynamoDB throttling diagnosis framework](throttling-diagnosing-workflow.md#throttling-diagnosing "throttling-diagnosing-workflow.md#throttling-diagnosing").

Before diving into specific throttling scenarios, first, check if the problem resolves
automatically:

- DynamoDB often adapts to hot partitions through its automatic split-for-heat
  mechanism. If you see throttling events that stop after a short period, your
  table may have already adapted by splitting the hot partition. When partitions
  split, each new partition handles a smaller section of the keyspace, which can
  help distribute the load more evenly. In many cases, no further action is needed
  as DynamoDB has automatically resolved the issue.

For more information about the _split-for-heat
mechanism_, see [Additional resources](#key-range-additional-resources "#key-range-additional-resources").

If the throttling persists, refer to the specific throttling scenarios below for
targeted remediation options:

- [TableReadKeyRangeThroughputExceeded](#throttling-table-read-keyrange "#throttling-table-read-keyrange")
- [TableWriteKeyRangeThroughputExceeded](#throttling-table-write-keyrange "#throttling-table-write-keyrange")
- [IndexReadKeyRangeThroughputExceeded](#throttling-index-read-keyrange "#throttling-index-read-keyrange")
- [IndexWriteKeyRangeThroughputExceeded](#throttling-index-write-keyrange "#throttling-index-write-keyrange")

### TableReadKeyRangeThroughputExceeded

###### When this occurs

The consumption rate of one or more partitions in your DynamoDB table exceeds the
partition's read throughput limit. This throttling occurs regardless of your
table's total provisioned capacity and affects both provisioned and on-demand
tables. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#key-range-exceeded-diagnosis-monitoring "#key-range-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

**For both provisioned and on-demand modes:**

- **Pre-warm capacity:** If throttling
  persists, check if your table is limited by its [Understanding DynamoDB warm throughput](warm-throughput.md "warm-throughput.md") capacity. Use warm throughput or increase
  read provisioned capacity in advance for expected traffic increases.
  Increasing warm throughput improves your table's ability to handle sudden
  traffic spikes before throttling occurs. Over time, if your actual
  throughput consistently approaches the warm throughput levels, DynamoDB may
  split busy partitions based on observed usage patterns.
- **Identify your hot keys:** If the table
  didn't resolve it automatically and your warm throughput is high or raising
  it didn't help, you'll need to identify specific hot keys. Use [Identifying hot keys using CloudWatch
  Contributor Insights](#key-range-identify-hot-keys "#key-range-identify-hot-keys") to determine if any particular
  partition key values are hot. This is a first step to target your mitigation
  efforts effectively. Note that identification may not always be
  straightforward, particularly with rolling hot partitions (where different
  partitions become hot over time) or when throttling is triggered by
  operations like scans. For these complex scenarios, you may need to analyze
  your application's access patterns and correlate them with the timing of
  throttling events.
- **Depending on your use case, consider using
  eventually consistent reads:** Switch from strongly consistent
  to eventually consistent reads, which consume half the RCUs and can
  immediately double your effective read capacity. For best practices on
  implementing eventually consistent reads to reduce read capacity
  consumption, see [DynamoDB read consistency](HowItWorks.md "HowItWorks.md").
- **Improve partition key design:** As a
  long-term solution, consider [Improving partition key
  design](#key-range-improve-partition-key-design "#key-range-improve-partition-key-design") to distribute access
  more evenly across partitions. This approach often provides the most
  comprehensive resolution to hot partition issues by addressing the root
  cause. However, it requires careful planning as it involves significant
  migration challenges.

### TableWriteKeyRangeThroughputExceeded

###### When this occurs

The consumption rate of one or more partitions in your DynamoDB table exceeds the
partition's write throughput limit. This throttling occurs regardless of your
table's total provisioned capacity and affects both provisioned and on-demand
tables. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#key-range-exceeded-diagnosis-monitoring "#key-range-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

**For both provisioned and on-demand modes:**

- **Pre-warm capacity:** If throttling
  persists, check if your table is limited by its [Understanding DynamoDB warm throughput](warm-throughput.md "warm-throughput.md") capacity.
  Use warm throughput or increase write provisioned capacity in advance for
  expected traffic increases. Increasing warm throughput improves your table's
  ability to handle sudden traffic spikes before throttling occurs. Over time,
  if your actual throughput consistently approaches the warm throughput
  levels, DynamoDB may split busy partitions based on observed usage patterns.
- **Identify your hot keys:** If the table
  didn't resolve it automatically and your warm throughput is high or raising
  it didn't help, you'll need to identify specific hot keys. Use [Identifying hot keys using CloudWatch
  Contributor Insights](#key-range-identify-hot-keys "#key-range-identify-hot-keys") to determine if any particular
  partition key values are hot. This is a first step to target your mitigation
  efforts effectively. Consider these common patterns:

      + If you see the same partition key appearing frequently in your
       throttling data, this indicates a concentrated hot key.
      + If you do not see repeated keys but are writing data in an ordered
       way (such as sequential timestamps or scan-based operations that
       follow keyspace order), you likely have rolling hot partitions where
       different keys become hot over time as your writes move through the
       keyspace.

  Note that write throttling can also occur with operations like
  `BatchWriteItem` or transactions that affect multiple items
  simultaneously. When individual items within a `BatchWriteItem`
  request are throttled, DynamoDB does not propagate these throttling errors to
  the application code. Instead, DynamoDB returns information about the
  unprocessed items in the response, which your application must handle by
  retrying those specific items. For transactions, the entire operation fails
  with a `TransactionCanceledException` if any item experiences
  throttling. For these complex scenarios, you may need to analyze your
  application's write patterns and data ingestion workflows, correlate them
  with the timing of throttling events, and implement appropriate retry
  handling strategies.

- **Improve partition key design:** As a
  long-term solution, consider [Improving partition key
  design](#key-range-improve-partition-key-design "#key-range-improve-partition-key-design") to distribute access
  more evenly across partitions. This approach often provides the most
  comprehensive resolution to hot partition issues by addressing the root
  cause. However, it requires careful planning as it involves significant
  migration challenges.

### IndexReadKeyRangeThroughputExceeded

###### When this occurs

The consumption rate of one or more partitions in your DynamoDB GSI exceeds the
partition's read throughput limit. This throttling occurs regardless of your
GSI's total provisioned capacity and affects both provisioned and on-demand
tables. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#key-range-exceeded-diagnosis-monitoring "#key-range-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Pre-warm capacity:** If throttling
  persists, check if your GSI is limited by its [Understanding DynamoDB warm throughput](warm-throughput.md "warm-throughput.md") capacity.
  Use warm throughput or increase read provisioned capacity in advance for
  expected traffic increases. Increasing warm throughput improves your GSI's
  ability to handle sudden traffic spikes before throttling occurs. Over time,
  if your actual throughput consistently approaches the warm throughput
  levels, DynamoDB may split busy partitions based on observed usage patterns.
- **Identify your hot keys:** If the GSI didn't
  resolve it automatically and your warm throughput is high or raising it
  didn't help, you'll need to identify specific hot keys. Use [Identifying hot keys using CloudWatch
  Contributor Insights](#key-range-identify-hot-keys "#key-range-identify-hot-keys") to determine if any particular
  partition key values are hot. This is a first step to target your mitigation
  efforts effectively. Note that for GSIs, the partition key distribution may
  differ significantly from your base table, creating different hot key
  patterns.
- **Redesign GSI partition keys:** Consider
  whether your GSI key design might be creating artificial hot spots (such as
  status flags, date-only keys, or boolean attributes) that concentrate reads
  on a small number of partitions. Consider using composite keys that combine
  the low-cardinality attribute with a high-cardinality attribute (e.g.,
  "ACTIVE#customer123" instead of just "ACTIVE") or apply [Using write sharding to distribute workloads
  evenly in your DynamoDB table](bp-partition-key-sharding.md "bp-partition-key-sharding.md") techniques to the base table items
  that affect GSI distribution to distribute writes across multiple
  partitions. While querying sharded data requires additional application
  logic to aggregate results, this approach prevents throttling by
  distributing access patterns more evenly.

### IndexWriteKeyRangeThroughputExceeded

###### When this occurs

The consumption rate of one or more partitions in your DynamoDB GSI exceeds the
partition's write throughput limit. This throttling occurs regardless of your
GSI's total provisioned capacity and affects both provisioned and on-demand
tables. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#key-range-exceeded-diagnosis-monitoring "#key-range-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Redesign GSI partition key:** Review your
  GSI partition key design to verify it has sufficient cardinality
  (uniqueness) to distribute writes evenly. A common cause of GSI write
  throttling is using low-cardinality attributes as GSI partition keys (such
  as status flags with only a few possible values). Even when your base table
  has well-distributed partition keys, your GSI can still experience hot
  partitions if its partition key concentrates writes to a small number of
  values. For example, if 80% of your items have status="ACTIVE", this creates
  a severe hot partition in a status-based GSI. Consider using composite keys
  that combine the low-cardinality attribute with a high-cardinality attribute
  (e.g., "ACTIVE#customer123" instead of just "ACTIVE") or apply [Using write sharding to distribute workloads
  evenly in your DynamoDB table](bp-partition-key-sharding.md "bp-partition-key-sharding.md") techniques to the base table items
  that affect GSI distribution to distribute writes across multiple
  partitions. While querying sharded data requires additional application
  logic to aggregate results, this approach prevents throttling by
  distributing access patterns more evenly.
- **Pre-warm capacity:**Check if your GSI is
  limited by its [Understanding DynamoDB warm throughput](warm-throughput.md "warm-throughput.md") capacity. Use warm throughput or
  increase read provisioned capacity in advance for expected traffic
  increases. Increasing warm throughput improves your GSI's ability to handle
  sudden traffic spikes before throttling occurs. Over time, if your actual
  throughput consistently approaches the warm throughput levels, DynamoDB may
  split busy partitions based on observed usage patterns.
- **Optimize GSI projections:** Apply [Optimizing GSI
  projections](#key-range-optimize-gsi-projections "#key-range-optimize-gsi-projections") techniques to reduce
  write volume to GSIs. Projecting fewer attributes can significantly reduce
  the write capacity consumed by each GSI update.

## Common diagnosis and

monitoring

When troubleshooting partition-level throttling, several CloudWatch metrics can help
identify hot partitions and confirm the root cause.

###### Essential CloudWatch metrics

Monitor these key metrics to diagnose partition-level throttling:

- **Partition-level throttling events:**
  [`ReadKeyRangeThroughputThrottleEvents`](metrics-dimensions.md#ReadKeyRangeThroughputThrottleEvents "metrics-dimensions.md#ReadKeyRangeThroughputThrottleEvents") and [`WriteKeyRangeThroughputThrottleEvents`](metrics-dimensions.md#WriteKeyRangeThroughputThrottleEvents "metrics-dimensions.md#WriteKeyRangeThroughputThrottleEvents") track when
  individual partitions exceed their throughput limits. [`ReadThrottleEvents`](metrics-dimensions.md#ReadThrottleEvents "metrics-dimensions.md#ReadThrottleEvents") and [`WriteThrottleEvents`](metrics-dimensions.md#WriteThrottleEvents "metrics-dimensions.md#WriteThrottleEvents") track when any read or write
  requests exceed the provisioned capacity.
- **Capacity consumption:**
  [`ConsumedReadCapacityUnits`](metrics-dimensions.md#ConsumedReadCapacityUnits "metrics-dimensions.md#ConsumedReadCapacityUnits") and [`ConsumedWriteCapacityUnits`](metrics-dimensions.md#ConsumedWriteCapacityUnits "metrics-dimensions.md#ConsumedWriteCapacityUnits") show overall usage
  patterns.

## Resolution procedures

### Identifying hot keys using CloudWatch

Contributor Insights

Use this procedure to identify which partition keys are causing throttling.

1. Enable [CloudWatch Contributor
   Insights](contributorinsights_HowItWorks.md "contributorinsights_HowItWorks.md") on your table or GSI to track the most throttled keys.
   Consider keeping CloudWatch Contributor Insights enabled continuously for
   real-time throttling alerts by using the _Throttled
   keys_ mode. This mode focuses exclusively on throttled
   requests by only processing events when throttling occurs. This targeted
   monitoring is a cost effective way to maintain continuous visibility into
   throttling issues.
2. Identify which keys are causing the hot partition issues.
3. (If the full _Accessed and throttled keys
   mode_ is enabled) Analyze the access patterns over time to
   determine if hot keys are consistent or occur during specific
   periods.

### Improving partition key

design

Use this approach when you can modify your table schema to better distribute
traffic across partitions. When possible, this is the most effective long-term
solution for hot partition issues. Ideally, partition key design should be carefully
considered during the initial table design phase.

Partition key redesign represents a fundamental change to your data model that
impacts your entire application ecosystem. Before proceeding with this approach,
carefully consider these significant limitations:

- **Data migration complexity:** Redesigning
  partition keys requires migrating all existing data, which can be
  resource-intensive and time-consuming for large tables.
- **Application code changes:** All application
  code that reads or writes to the table must be updated to use the new key
  structure.
- **Production impact:** Migrating to a new key
  design often requires downtime or complex dual-write strategies during
  transition.

For comprehensive guidance and principles on partition key design, see [Best practices for designing and using partition keys
effectively in DynamoDB](bp-partition-key-design.md "bp-partition-key-design.md") and [Designing partition keys to distribute your
workload in DynamoDB](bp-partition-key-uniform-load.md "bp-partition-key-uniform-load.md").

### Optimizing GSI

projections

Review your application's query patterns to determine exactly which attributes
need to be available when querying the GSI, and limit your projections to just those
attributes. When you update attributes that aren't projected into a GSI, no write
operation occurs on that GSI, reducing write throughput consumption during updates.
This targeted projection strategy optimizes both performance and cost while still
supporting your application's query requirements. Note that projecting fewer
attributes reduces write capacity consumption but may require additional base table
reads.

For more information about efficient projection strategies, see [Best Practices for Using Secondary Indexes in
DynamoDB](bp-indexes-general.md "bp-indexes-general.md").

## Additional resources

The following blog posts provide hands-on examples and practical details for the
concepts covered in this guide:

- For hands-on guidance about scaling DynamoDB and managing hot partitions, see
  [Part 1: Scaling DynamoDB - How partitions, hot keys, and split for heat
  impact performance](https://aws.amazon.com/blogs/database/part-1-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/ "https://aws.amazon.com/blogs/database/part-1-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/").
- For detailed information about how DynamoDB's split-for-heat mechanism works, its
  benefits, and implementation details, see [Part 3: Summary and best practices](https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/ "https://aws.amazon.com/blogs/database/part-3-scaling-dynamodb-how-partitions-hot-keys-and-split-for-heat-impact-performance/").
- For detailed write sharding strategies, see [Using write sharding to distribute workloads
  evenly in your DynamoDB table](bp-partition-key-sharding.md "bp-partition-key-sharding.md").
