# Understanding Global Secondary Index (GSI) write

throttling and back pressure in DynamoDB

GSI back-pressure throttling represents one of the most complex throttling scenarios
in DynamoDB because it creates an indirect relationship between write operations and
throttling—your application writes to a base table but experiences throttling due to
capacity constraints on one or several indexes.

## Understanding GSI back-pressure

throttling

When you write to a DynamoDB table, any global secondary indexes (GSIs) on that table
are updated asynchronously using an eventually consistent model. If a GSI doesn't
have sufficient capacity to handle these updates, DynamoDB throttles writes to the base
table to maintain data consistency. This is called _GSI
back-pressure_. For more information about how GSIs work, see [Global Secondary Indexes in DynamoDB](GSI.md "GSI.md").

Unlike direct table throttling where the resource being accessed is also the
resource causing throttling, GSI back-pressure creates a dependency between the base
table and its indexes. Even if your base table has ample capacity, writes will be
throttled if any associated GSI cannot handle the update volume. This relationship
is particularly important to understand because partition-level constraints apply
independently to both the base table and each GSI—each has its own partition
structure and corresponding throughput limits.

GSI partitioning is based on the GSI's partition key, which is often different
from the base table's partition key. Even if your base table access is perfectly
distributed across partitions, your GSI updates might still concentrate on specific
partitions, creating hot spots in the GSI. For general best practices on partition
key design for both tables and GSIs, see [DynamoDB partition key design](bp-partition-key-design.md "bp-partition-key-design.md").

For example, if your base table uses `customerId` as a partition key
(evenly distributed) but your GSI uses `status` as a partition key (with
limited possible values like "active", "pending", "closed"), updates to items with
popular status values can create GSI hot partitions even when base table access is
balanced. This creates a particularly challenging scenario where your application
might experience throttling due to GSI hot partitions even though both the base
table and GSI have sufficient overall capacity and the base table's access pattern
appears well-distributed.

Even though the throttling exception points to the GSI (via
`ResourceArn`), the actual operation being throttled is the write to
the base table. This can be confusing because your application is writing to the
base table but receiving an exception about the GSI.

## Types of GSI throttling

GSI back-pressure throttling manifests through different exception types depending
on the specific capacity constraint:

- **GSI provisioned capacity exceeded:** Occurs
  when the GSI lacks sufficient write capacity units to handle updates from
  base table operations. This produces a
  `ProvisionedThroughputExceededException` with the reason
  [IndexWriteProvisionedThroughputExceeded](throttling-provisioned-capacity-exceeded-mitigation.md#throttling-index-write-provisioned "throttling-provisioned-capacity-exceeded-mitigation.md#throttling-index-write-provisioned"), and
  the `ResourceArn` points directly to the specific GSI
  experiencing capacity constraints.
- **GSI on-demand maximum throughput
  exceeded:** Occurs when GSI write operations surpass configured
  maximum limits on on-demand tables. This produces a
  `ThrottlingException` with the reason [IndexWriteMaxOnDemandThroughputExceeded](throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-index-write-max-ondemand "throttling-ondemand-capacity-exceeded-mitigation.md#throttling-diagnostic-index-write-max-ondemand"),
  identifying the specific GSI with configured throughput restrictions.
- **GSI partition limits exceeded:** Happens
  when individual GSI partitions exceed their throughput limits (hot
  partitions), even if overall GSI capacity appears sufficient. This generates
  a `ThrottlingException` with the reason [IndexWriteKeyRangeThroughputExceeded](throttling-key-range-limit-exceeded-mitigation.md#throttling-index-write-keyrange "throttling-key-range-limit-exceeded-mitigation.md#throttling-index-write-keyrange"),
  indicating hot partition issues on the specific GSI identified in the
  `ResourceArn`. This is particularly important because GSI
  partition distribution may differ significantly from the base table's
  partition distribution, creating hot spots in the GSI even when base table
  access is evenly distributed.
- **GSI account limits exceeded:** Triggers
  when write operations to a specific GSI exceed the per-table (or any
  individual GSI within that table) regional throughput boundaries set at the
  account level. DynamoDB returns a `ThrottlingException` with the
  reason [IndexWriteAccountLimitExceeded](throttling-account-limit-exceeded-mitigation.md#throttling-index-write-account-limit "throttling-account-limit-exceeded-mitigation.md#throttling-index-write-account-limit"), pointing to the
  GSI that pushed its usage beyond account limits. This throttling occurs
  independently for each GSI that surpasses the limit. For information about
  per-table, per-account,regional, service quotas, see [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").
