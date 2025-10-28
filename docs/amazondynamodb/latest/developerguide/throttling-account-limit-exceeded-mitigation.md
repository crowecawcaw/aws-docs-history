# 3- Account limits

exceeded

On-demand tables do not have provisioned capacity levels to manage, but DynamoDB enforces
account-level throughput limits to prevent runaway execution and ensure fair resource usage
across all customers. These per-table account limits serve as adjustable safeguards, set for
each account and Region combination. When your read or write consumption rate exceeds these
limits, DynamoDB returns an `AccountLimitExceeded` throttling reason type in the
throttling exception. The default per-table account limits automatically apply when tables
do not have custom maximum throughput settings configured. You can optionally configure
maximum throughput settings for finer cost control and predictability, or request quota
increases through the [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md") console if your application
requirements exceed the default limits.

## Account limit exceeded mitigation

measures

This section provides resolution guidance for account limit throttling scenarios.
Before using this guide, ensure you have identified the specific throttling reasons from
your application's exception handling, and determined the Amazon Resource Name (ARN) of
the affected resource. For information on retrieving throttling reasons and identifying
throttled resources, see [DynamoDB throttling diagnosis framework](throttling-diagnosing-workflow.md#throttling-diagnosing "throttling-diagnosing-workflow.md#throttling-diagnosing").

Before diving into specific throttling scenarios, first determine if action is
actually needed:

- **Evaluate performance impact:** Check if your
  application is still meeting its performance requirements despite the
  throttling. Many applications operate successfully at or near account limits,
  particularly during bulk operations or data migrations.
- **Review throttling patterns:** If throttling is
  intermittent and your application handles retries effectively, the current
  limits may be sufficient for your workload.

If your application performs acceptably even when occasionally hitting account limits,
you might choose to simply monitor the situation rather than implementing immediate
changes.

If you determine that throttling is causing unacceptable performance issues or
reliability concerns, select a specific throttling reason below to find recommended
mitigation options:

- [TableReadAccountLimitExceeded](#throttling-table-read-account-limit "#throttling-table-read-account-limit")
- [TableWriteAccountLimitExceeded](#throttling-table-write-account-limit "#throttling-table-write-account-limit")
- [IndexReadAccountLimitExceeded](#throttling-index-read-account-limit "#throttling-index-read-account-limit")
- [IndexWriteAccountLimitExceeded](#throttling-index-write-account-limit "#throttling-index-write-account-limit")

### TableReadAccountLimitExceeded

###### When this occurs

Your table's read consumption has exceeded the account-level per-table read
throughput quota for your Region. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#account-limit-exceeded-diagnosis-monitoring "#account-limit-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Resolution approach

Use the following steps to resolve this throttling:

- **Request quota increases:**

Request an increase to the per-table read throughput limit (Quota code
L-CF0CBE56). For detailed steps on how to submit the request, see [Requesting per-table
quota increases](#account-limit-request-per-table-quota "#account-limit-request-per-table-quota").

### TableWriteAccountLimitExceeded

###### When this occurs

Your table's write consumption has exceeded the account-level per-table write
throughput quota for your Region. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#account-limit-exceeded-diagnosis-monitoring "#account-limit-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Resolution approach

Use the following steps to resolve this throttling:

- **Request quota increases:** Request an
  increase to the per-table write throughput limit (Quota code L-AB614373).
  For detailed steps on how to submit the request, see [Requesting per-table
  quota increases](#account-limit-request-per-table-quota "#account-limit-request-per-table-quota").

### IndexReadAccountLimitExceeded

###### When this occurs

The read operations directed at a Global Secondary Index (GSI) consume more
throughput than your account's per-table read quota allows in your current AWS
Region. The account-level per-table read throughput quota applies collectively
to a table and all its GSIs combined. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#account-limit-exceeded-diagnosis-monitoring "#account-limit-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Resolution approach

Choose the appropriate resolution based on your account's capacity
distribution:

- **Request quota increases:** Request an
  increase to the per-table read throughput limit (Quota code L-CF0CBE56). For
  detailed steps on how to submit the request, see [Requesting per-table
  quota increases](#account-limit-request-per-table-quota "#account-limit-request-per-table-quota").
- **Optimize GSI usage:**
  [Review GSI design and
  query patterns](#account-limit-optimize-gsi-projections "#account-limit-optimize-gsi-projections") to reduce unnecessary read capacity
  consumption.

### IndexWriteAccountLimitExceeded

###### When this occurs

Write operations to your base table generate corresponding updates to a GSI
that collectively exceed the account-level per-table write throughput quota for
your AWS Region. Every write to a base table item that contains attributes
indexed by a GSI trigger a corresponding write operation to that GSI. These
combined write operations count toward your per-table write throughput quota.
You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#account-limit-exceeded-diagnosis-monitoring "#account-limit-exceeded-diagnosis-monitoring") to analyze the
patterns and timing of these throttling events and identify which operations are
causing the excessive GSI write activity.

###### Resolution approach

Choose the appropriate resolution based on your account's capacity
distribution:

- **Request quota increases:** Request an
  increase to the [per-table write throughput limit](#account-limit-request-per-table-quota "#account-limit-request-per-table-quota") (Quota code L-AB614373) to
  accommodate higher GSI write traffic from base table operations. The
  per-table write throughput quota applies to the entire table, including all
  of its GSIs. For detailed steps on how to submit the request, see [Requesting per-table
  quota increases](#account-limit-request-per-table-quota "#account-limit-request-per-table-quota").
- **Optimize GSI projections:**
  [Review GSI
  projections and design](#account-limit-optimize-gsi-projections "#account-limit-optimize-gsi-projections") to reduce write volume to GSIs.

## Common diagnosis and

monitoring

When troubleshooting account limit exceeded throttling events, several CloudWatch metrics
can help identify whether you're hitting per-table or account-wide limits and understand
your capacity distribution patterns.

###### Essential CloudWatch metrics

Monitor these key metrics to diagnose account limit throttling:

- **Account limit throttling events:**
  [`ReadAccountLimitThrottleEvents`](metrics-dimensions.md#ReadAccountLimitThrottleEvents "metrics-dimensions.md#ReadAccountLimitThrottleEvents") and [`WriteAccountLimitThrottleEvents`](metrics-dimensions.md#WriteAccountLimitThrottleEvents "metrics-dimensions.md#WriteAccountLimitThrottleEvents") track when
  requests are throttled due to account-level limits. [`ReadThrottleEvents`](metrics-dimensions.md#ReadThrottleEvents "metrics-dimensions.md#ReadThrottleEvents") and [`WriteThrottleEvents`](metrics-dimensions.md#WriteThrottleEvents "metrics-dimensions.md#WriteThrottleEvents") track when any read or write
  requests exceed the provisioned capacity.
- **Capacity consumption by resource:**
  [`ConsumedReadCapacityUnits`](metrics-dimensions.md#ConsumedReadCapacityUnits "metrics-dimensions.md#ConsumedReadCapacityUnits") and [`ConsumedWriteCapacityUnits`](metrics-dimensions.md#ConsumedWriteCapacityUnits "metrics-dimensions.md#ConsumedWriteCapacityUnits") for each table and GSI
  show individual resource usage.
- **Account-wide consumption:** Use CloudWatch metric
  math expressions to sum consumed capacity across all tables and GSIs to monitor
  total account usage.

## Resolution

procedures

### Requesting per-table quota

increases

If your applications need to operate beyond the current per-table throughput
limits, you should submit a quota increase request using the procedure below. Each
DynamoDB table in your AWS account (together with all its associated GSIs) is subject
to these throughput quotas within a specific Region. These quotas represent the
maximum read or write capacity that any individual table and its GSIs can
collectively consume, and they apply independently to each table rather than as an
aggregate across all tables in your account.

Optionally, you can also set lower limits on a per-table or per-GSI basis by
configuring their maximum on-demand throughput settings.

1. Identify the specific quota that needs to be increased:
   - **Per-table read throughput limit**
     (Quota code L-CF0CBE56): Default 40,000 RCUs per table
   - **Per-table write throughput limit**
     (Quota code L-AB614373): Default 40,000 WCUs per table

2. Use the [AWS Service Quotas
   console](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") to request an increase:
   - Navigate to the DynamoDB service in Service Quotas
   - Find the appropriate quota using the quota code
   - Request an increase based on your projected peak usage

3. Provide justification for the increase, including:
   - Current usage patterns and peak traffic requirements
   - Business justification for the increased capacity
   - Timeline for when the increased capacity is needed

###### Note

Quota increases typically take 24-48 hours to process. Plan your requests
accordingly and consider temporary mitigation strategies while waiting for
approval.

### Optimizing GSI projections

and design

Optimize your Global Secondary Index (GSI) projections and design to reduce
capacity consumption and improve performance.

###### Selective projection strategies

If your queries only need to access a few attributes, projecting only those
attributes reduces the amount of data written to the GSI when base table items
change. For details on projection types, see [Projections for Global Secondary Indexes](GSI.md#GSI.Projections "GSI.md#GSI.Projections").

1. Analyze query patterns: Review your application's query patterns to
   identify which attributes are actually accessed through the GSI.
2. Use selective projections: Only project attributes that are actually
   needed in queries to reduce write volume.
3. Consider `KEYS_ONLY`: If your queries only need the key
   attributes, use `KEYS_ONLY` projection to minimize write
   volume.
4. Balance read vs. write trade-offs: Projecting fewer attributes reduces
   write capacity consumption but may require additional base table
   reads.

###### Sparse GSI implementation

Sparse GSIs contain only items that have the indexed attribute, rather than
all items from your base table. This reduces partition density and improves
performance when you frequently query specific subsets of data.

1. Design GSIs that only include items with specific attribute values.
2. Implement conditional indexing by only setting the GSI partition key
   attribute on items that should be indexed.
3. Use composite keys in sparse GSIs (e.g., status#timestamp) to further
   distribute traffic within the subset of indexed items.

For more information about implementing these strategies, see [Best Practices for Using Secondary Indexes in DynamoDB](bp-indexes.md "bp-indexes.md").
