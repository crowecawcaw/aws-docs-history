# DynamoDB Metrics and dimensions

When you interact with DynamoDB, it sends metrics and dimensions to CloudWatch.

DynamoDB outputs consumed provisioned throughput for one-minute periods. [Auto scaling](AutoScaling.md "AutoScaling.md") triggers when your consumed capacity breaches
the configured target utilization for two consecutive minutes. CloudWatch alarms might have a
short delay of up to a few minutes before triggering auto scaling. This delay ensures
accurate CloudWatch metric evaluation. If the consumed throughput spikes are more than a minute
apart, auto scaling might not trigger. Similarly, a scale down event can occur when 15
consecutive data points are lower than the target utilization. In either case, after auto
scaling triggers, the [UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") API is
invoked. It then takes several minutes to update the provisioned capacity for the table or
index. During this period, any requests that exceed the previous provisioned capacity of the
tables are throttled.

## Viewing metrics and dimensions

CloudWatch displays the following metrics for DynamoDB:

### DynamoDB metrics

###### Note

Amazon CloudWatch aggregates these metrics at one-minute intervals:

- `ConditionalCheckFailedRequests`
- `ConsumedReadCapacityUnits`
- `ConsumedWriteCapacityUnits`
- `ReadAccountLimitThrottleEvents`
- `ReadKeyRangeThroughputThrottleEvents`
- `ReadMaxOnDemandThroughputThrottleEvents`
- `ReadProvisionedThroughputThrottleEvents`
- `ReadThrottleEvents`
- `ReturnedBytes`
- `ReturnedItemCount`
- `ReturnedRecordsCount`
- `SuccessfulRequestLatency`
- `SystemErrors`
- `TimeToLiveDeletedItemCount`
- `ThrottledRequests`
- `TransactionConflict`
- `UserErrors`
- `WriteAccountLimitThrottleEvents`
- `WriteKeyRangeThroughputThrottleEvents`
- `WriteMaxOnDemandThroughputThrottleEvents`
- `WriteProvisionedThroughputThrottleEvents`
- `WriteThrottleEvents`
  For all other DynamoDB metrics, the aggregation granularity is five
  minutes.

Not all statistics, such as _Average_ or
_Sum_, are applicable for every metric. However, all of these
values are available through the Amazon DynamoDB console, or by using the CloudWatch console,
AWS CLI, or AWS SDKs for all metrics.

In the following list, each metric has a set of valid statistics that are
applicable to that metric.

###### List of Available Metrics

- [AccountMaxReads](#AccountMaxReads "#AccountMaxReads")
- [AccountMaxTableLevelReads](#AccountMaxTableLevelReads "#AccountMaxTableLevelReads")
- [AccountMaxTableLevelWrites](#AccountMaxTableLevelWrites "#AccountMaxTableLevelWrites")
- [AccountMaxWrites](#AccountMaxWrites "#AccountMaxWrites")
- [AccountProvisionedReadCapacityUtilization](#AccountProvisionedReadCapacityUtilization "#AccountProvisionedReadCapacityUtilization")
- [AccountProvisionedWriteCapacityUtilization](#AccountProvisionedWriteCapacityUtilization "#AccountProvisionedWriteCapacityUtilization")
- [AgeOfOldestUnreplicatedRecord](#AgeOfOldestUnreplicatedRecord "#AgeOfOldestUnreplicatedRecord")
- [ConditionalCheckFailedRequests](#ConditionalCheckFailedRequests "#ConditionalCheckFailedRequests")
- [ConsumedChangeDataCaptureUnits](#ConsumedChangeDataCaptureUnits "#ConsumedChangeDataCaptureUnits")
- [ConsumedReadCapacityUnits](#ConsumedReadCapacityUnits "#ConsumedReadCapacityUnits")
- [ConsumedWriteCapacityUnits](#ConsumedWriteCapacityUnits "#ConsumedWriteCapacityUnits")
- [FailedToReplicateRecordCount](#FailedToReplicateRecordCount "#FailedToReplicateRecordCount")
- [MaxProvisionedTableReadCapacityUtilization](#MaxProvisionedTableReadCapacityUtilization "#MaxProvisionedTableReadCapacityUtilization")
- [MaxProvisionedTableWriteCapacityUtilization](#MaxProvisionedTableWriteCapacityUtilization "#MaxProvisionedTableWriteCapacityUtilization")
- [OnDemandMaxReadRequestUnits](#OnDemandMaxReadRequestUnits "#OnDemandMaxReadRequestUnits")
- [OnDemandMaxWriteRequestUnits](#OnDemandMaxWriteRequestUnits "#OnDemandMaxWriteRequestUnits")
- [OnlineIndexConsumedWriteCapacity](#OnlineIndexConsumedWriteCapacity "#OnlineIndexConsumedWriteCapacity")
- [OnlineIndexPercentageProgress](#OnlineIndexPercentageProgress "#OnlineIndexPercentageProgress")
- [OnlineIndexThrottleEvents](#OnlineIndexThrottleEvents "#OnlineIndexThrottleEvents")
- [PendingReplicationCount](#PendingReplicationCount "#PendingReplicationCount")
- [ProvisionedReadCapacityUnits](#ProvisionedReadCapacityUnits "#ProvisionedReadCapacityUnits")
- [ProvisionedWriteCapacityUnits](#ProvisionedWriteCapacityUnits "#ProvisionedWriteCapacityUnits")
- [ReadAccountLimitThrottleEvents](#ReadAccountLimitThrottleEvents "#ReadAccountLimitThrottleEvents")
- [ReadKeyRangeThroughputThrottleEvents](#ReadKeyRangeThroughputThrottleEvents "#ReadKeyRangeThroughputThrottleEvents")
- [ReadMaxOnDemandThroughputThrottleEvents](#ReadMaxOnDemandThroughputThrottleEvents "#ReadMaxOnDemandThroughputThrottleEvents")
- [ReadProvisionedThroughputThrottleEvents](#ReadProvisionedThroughputThrottleEvents "#ReadProvisionedThroughputThrottleEvents")
- [ReadThrottleEvents](#ReadThrottleEvents "#ReadThrottleEvents")
- [ReplicationLatency](#ReplicationLatency "#ReplicationLatency")
- [ReturnedBytes](#ReturnedBytes "#ReturnedBytes")
- [ReturnedItemCount](#ReturnedItemCount "#ReturnedItemCount")
- [ReturnedRecordsCount](#ReturnedRecordsCount "#ReturnedRecordsCount")
- [SuccessfulRequestLatency](#SuccessfulRequestLatency "#SuccessfulRequestLatency")
- [SystemErrors](#SystemErrors "#SystemErrors")
- [TimeToLiveDeletedItemCount](#TimeToLiveDeletedItemCount "#TimeToLiveDeletedItemCount")
- [ThrottledPutRecordCount](#ThrottledPutRecordCount "#ThrottledPutRecordCount")
- [ThrottledRequests](#ThrottledRequests "#ThrottledRequests")
- [TransactionConflict](#TransactionConflict "#TransactionConflict")
- [UserErrors](#UserErrors "#UserErrors")
- [WriteAccountLimitThrottleEvents](#WriteAccountLimitThrottleEvents "#WriteAccountLimitThrottleEvents")
- [WriteKeyRangeThroughputThrottleEvents](#WriteKeyRangeThroughputThrottleEvents "#WriteKeyRangeThroughputThrottleEvents")
- [WriteMaxOnDemandThroughputThrottleEvents](#WriteMaxOnDemandThroughputThrottleEvents "#WriteMaxOnDemandThroughputThrottleEvents")
- [WriteProvisionedThroughputThrottleEvents](#WriteProvisionedThroughputThrottleEvents "#WriteProvisionedThroughputThrottleEvents")
- [WriteThrottleEvents](#WriteThrottleEvents "#WriteThrottleEvents")

#### AccountMaxReads

The maximum number of read capacity units that can be used by an account. This
limit doesn't apply to on-demand tables or global secondary indexes.

Units: `Count`

Valid Statistics:

- `Maximum` – The maximum number of read capacity units
  that can be used by an account.

#### AccountMaxTableLevelReads

The maximum number of read capacity units that can be used by a table or
global secondary index of an account. For on-demand tables, this limit caps the
maximum read request units a table or a global secondary index can use.

Units: `Count`

Valid Statistics:

- `Maximum` – The maximum number of read capacity units
  that can be used by a table or global secondary index of the
  account.

#### AccountMaxTableLevelWrites

The maximum number of write capacity units that can be used by a table or
global secondary index of an account. For on-demand tables, this limit caps the
maximum write request units a table or a global secondary index can use.

Units: `Count`

Valid Statistics:

- `Maximum` – The maximum number of write capacity
  units that can be used by a table or global secondary index of the
  account.

#### AccountMaxWrites

The maximum number of write capacity units that can be used by an account.
This limit doesn't apply to on-demand tables or global secondary indexes.

Units: `Count`

Valid Statistics:

- `Maximum` – The maximum number of write capacity
  units that can be used by an account.

#### AccountProvisionedReadCapacityUtilization

The percentage of provisioned read capacity units utilized by an
account.

Units: `Percent`

Valid Statistics:

- `Maximum` – The maximum percentage of provisioned
  read capacity units utilized by the account.
- `Minimum` – The minimum percentage of provisioned
  read capacity units utilized by the account.
- `Average` – The average percentage of provisioned
  read capacity units utilized by the account. The metric is published for
  five-minute intervals. Therefore, if you rapidly adjust the provisioned
  read capacity units, this statistic might not reflect the true
  average.

#### AccountProvisionedWriteCapacityUtilization

The percentage of provisioned write capacity units utilized by an
account.

Units: `Percent`

Valid Statistics:

- `Maximum` – The maximum percentage of provisioned
  write capacity units utilized by the account.
- `Minimum` – The minimum percentage of provisioned
  write capacity units utilized by the account.
- `Average` – The average percentage of provisioned
  write capacity units utilized by the account. The metric is published
  for five-minute intervals. Therefore, if you rapidly adjust the
  provisioned write capacity units, this statistic might not reflect the
  true average.

#### AgeOfOldestUnreplicatedRecord

The elapsed time since a record yet to be replicated to the Kinesis data stream
first appeared in the DynamoDB table.

Units: `Milliseconds`

Dimensions: `TableName, DelegatedOperation`

Valid Statistics:

- `Maximum`.
- `Minimum`.
- `Average`.

#### ConditionalCheckFailedRequests

The number of failed attempts to perform conditional writes. The
`PutItem`, `UpdateItem`, and `DeleteItem`
operations let you provide a logical condition that must evaluate to true before
the operation can proceed. If this condition evaluates to false,
`ConditionalCheckFailedRequests` is incremented by one.
`ConditionalCheckFailedRequests` is also incremented by one for
PartiQL Update and Delete statements where a logical condition is provided and
that condition evaluates to false.

###### Note

A failed conditional write will result in an HTTP 400 error (Bad Request).
These events are reflected in the
`ConditionalCheckFailedRequests` metric, but not in the
`UserErrors` metric.

Units: `Count`

Dimensions: `TableName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### ConsumedChangeDataCaptureUnits

The number of consumed change data capture units.

Units: `Count`

Dimensions: `TableName, DelegatedOperation`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`

#### ConsumedReadCapacityUnits

The number of read capacity units consumed over the specified time period for
both provisioned and on-demand capacity, so you can track how much of your
throughput is used. You can retrieve the total consumed read capacity for a
table and all of its global secondary indexes, or for a particular global
secondary index. For more information, see [Read/Write Capacity
Mode](ProvisionedThroughputIntro.md "ProvisionedThroughputIntro.md").

The `TableName` dimension returns the
`ConsumedReadCapacityUnits` for the table, but not for any global
secondary indexes. To view `ConsumedReadCapacityUnits` for a global
secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

###### Note

This means that short, intense spikes in capacity consumption lasting
just a second may not be accurately reflected in the CloudWatch graph, potentially
leading to a lower apparent consumption rate for that minute.

Use the `Sum` statistic to calculate the consumed throughput.
For example, get the `Sum` value over a span of one minute, and
divide it by the number of seconds in a minute (60) to calculate the average
`ConsumedReadCapacityUnits` per second. You can compare the
calculated value to the provisioned throughput value that you provide DynamoDB.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The minimum number of read capacity units
  consumed by any individual request to the table or index.
- `Maximum` – The maximum number of read capacity units
  consumed by any individual request to the table or index.
- `Average` – The average per-request read capacity
  consumed.

###### Note

The `Average` value is influenced by periods of
inactivity where the sample value will be zero.

- `Sum` – The total read capacity units consumed. This
  is the most useful statistic for the
  `ConsumedReadCapacityUnits` metric.
- `SampleCount` – represents the frequency at which the
  metric is emitted. Even tables with zero traffic will have the
  `SampleCount` emitted regularly, but the sample values
  will always be zero.

###### Note

The `SampleCount` value is influenced by periods of
inactivity where the sample value will be zero.

#### ConsumedWriteCapacityUnits

The number of write capacity units consumed over the specified time period for
both provisioned and on-demand capacity, so you can track how much of your
throughput is used. You can retrieve the total consumed write capacity for a
table and all of its global secondary indexes, or for a particular global
secondary index. For more information, see [Read/Write Capacity
Mode](ProvisionedThroughputIntro.md "ProvisionedThroughputIntro.md").

The `TableName` dimension returns the
`ConsumedWriteCapacityUnits` for the table, but not for any
global secondary indexes. To view `ConsumedWriteCapacityUnits` for a
global secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

###### Note

Use the `Sum` statistic to calculate the consumed throughput.
For example, get the `Sum` value over a span of one minute, and
divide it by the number of seconds in a minute (60) to calculate the average
`ConsumedWriteCapacityUnits` per second (recognizing that
this average doesn't highlight any large but brief spikes in write activity
that occurred during that minute). You can compare the calculated value to
the provisioned throughput value that you provide DynamoDB.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The minimum number of write capacity
  units consumed by any individual request to the table or index.
- `Maximum` – The maximum number of write capacity
  units consumed by any individual request to the table or index.
- `Average` – The average per-request write capacity
  consumed.

###### Note

The `Average` value is influenced by periods of
inactivity where the sample value will be zero.

- `Sum` – The total write capacity units consumed. This
  is the most useful statistic for the
  `ConsumedWriteCapacityUnits` metric.
- `SampleCount` – represents the frequency at which the
  metric is emitted. Even tables with zero traffic will have the
  `SampleCount` emitted regularly, but the sample values
  will always be zero.

###### Note

The `SampleCount` value is influenced by periods of
inactivity where the sample value will be zero.

#### FailedToReplicateRecordCount

The number of records that DynamoDB failed to replicate to your Kinesis data
stream.

Units: `Count`

Dimensions: `TableName`, `DelegatedOperation`

Valid Statistics:

- `Sum`

#### MaxProvisionedTableReadCapacityUtilization

The percentage of provisioned read capacity utilized by the highest
provisioned read table or global secondary index of an account.

Units: `Percent`

Valid Statistics:

- `Maximum` – The maximum percentage of provisioned
  read capacity units utilized by the highest provisioned read table or
  global secondary index of an account.
- `Minimum` – The minimum percentage of provisioned
  read capacity units utilized by the highest provisioned read table or
  global secondary index of an account.
- `Average` – The average percentage of provisioned
  read capacity units utilized by the highest provisioned read table or
  global secondary index of the account. The metric is published for
  five-minute intervals. Therefore, if you rapidly adjust the provisioned
  read capacity units, this statistic might not reflect the true
  average.

#### MaxProvisionedTableWriteCapacityUtilization

The percentage of provisioned write capacity utilized by the highest
provisioned write table or global secondary index of an account.

Units: `Percent`

Valid Statistics:

- `Maximum` – The maximum percentage of provisioned
  write capacity units utilized by the highest provisioned write table or
  global secondary index of an account.
- `Minimum` – The minimum percentage of provisioned
  write capacity units utilized by the highest provisioned write table or
  global secondary index of an account.
- `Average` – The average percentage of provisioned
  write capacity units utilized by the highest provisioned write table or
  global secondary index of the account. The metric is published for
  five-minute intervals. Therefore, if you rapidly adjust the provisioned
  write capacity units, this statistic might not reflect the true
  average.

#### OnDemandMaxReadRequestUnits

The number of specified on-demand read request units for a table or a global
secondary index.

To view `OnDemandMaxReadRequestUnits` for a table, you must specify
`TableName`. To view `OnDemandMaxReadRequestUnits` for
a global secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units: Count

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The lowest setting for on-demand read
  request units. If you use `UpdateTable` to increase read
  request units, this metric shows the lowest value of on-demand
  `ReadRequestUnits` during this time period.
- `Maximum` – The highest setting for on-demand read
  request units. If you use `UpdateTable` to decrease read
  request units, this metric shows the highest value of on-demand
  `ReadRequestUnits` during this time period.
- `Average` – The average on-demand read request units.
  The `OnDemandMaxReadRequestUnits` metric is published at
  five-minute intervals. Therefore, if you rapidly adjust the on-demand
  read request units, this statistic might not reflect the true
  average.

#### OnDemandMaxWriteRequestUnits

The number of specified on-demand write request units for a table or a global
secondary index.

To view `OnDemandMaxWriteRequestUnits` for a table, you must
specify `TableName`. To view
`OnDemandMaxWriteRequestUnits` for a global secondary index, you
must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The lowest setting for on-demand write
  request units. If you use `UpdateTable` to increase write
  request units, this metric shows the lowest value of on-demand
  `WriteRequestUnits` during this time period.
- `Maximum` – The highest setting for on-demand write
  request units. If you use `UpdateTable` to decrease write
  request units, this metric shows the highest value of on-demand
  `WriteRequestUnits` during this time period.
- `Average` – The average on-demand write request
  units. The `OnDemandMaxWriteRequestUnits` metric is published
  at five-minute intervals. Therefore, if you rapidly adjust the on-demand
  write request units, this statistic might not reflect the true
  average.

#### OnlineIndexConsumedWriteCapacity

The number of write capacity units consumed when adding a new global secondary
index to a table. If the write capacity of the index is too low, incoming write
activity during the backfill phase might be throttled. This can increase the
time it takes to create the index. You should monitor this statistic while the
index is being built to determine whether the write capacity of the index is
underprovisioned.

You can adjust the write capacity of the index using the
`UpdateTable` operation, even while the index is still being
built.

The `ConsumedWriteCapacityUnits` metric for the index doesn't
include the write throughput consumed during index creation.

###### Note

This metric may not be emitted if the new global secondary index’s
backfill phase completes quickly (less than a few minutes), which may occur
if the base table has few or no items to backfill in the index.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### OnlineIndexPercentageProgress

The percentage of completion when a new global secondary index is being added
to a table. DynamoDB must first allocate resources for the new index, and then
backfill attributes from the table into the index. For large tables, this
process might take a long time. You should monitor this statistic to view the
relative progress as DynamoDB builds the index.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### OnlineIndexThrottleEvents

The number of write throttle events that occur when adding a new global
secondary index to a table. These events indicate that the index creation will
take longer to complete, because incoming write activity is exceeding the
provisioned write throughput of the index.

You can adjust the write capacity of the index using the
`UpdateTable` operation, even while the index is still being
built.

The `WriteThrottleEvents` metric for the index doesn't include any
throttle events that occur during index creation.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### PendingReplicationCount

Metric for [Global tables version 2017.11.29 (Legacy)](globaltables.md "globaltables.md")
(global tables only). The number of item updates that are written to one replica
table, but that have not yet been written to another replica in the global
table.

Units: `Count`

Dimensions: `TableName, ReceivingRegion`

Valid Statistics:

- `Average`
- `Sample Count`
- `Sum`

#### ProvisionedReadCapacityUnits

The number of provisioned read capacity units for a table or a global
secondary index. The `TableName` dimension returns the
`ProvisionedReadCapacityUnits` for the table, but not for any
global secondary indexes. To view `ProvisionedReadCapacityUnits` for
a global secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units:`Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The lowest setting for provisioned read
  capacity. If you use `UpdateTable` to increase read capacity,
  this metric shows the lowest value of provisioned
  `ReadCapacityUnits` during this time period.
- `Maximum` – The highest setting for provisioned read
  capacity. If you use `UpdateTable` to decrease read capacity,
  this metric shows the highest value of provisioned
  `ReadCapacityUnits` during this time period.
- `Average` – The average provisioned read capacity.
  The `ProvisionedReadCapacityUnits` metric is published at
  five-minute intervals. Therefore, if you rapidly adjust the provisioned
  read capacity units, this statistic might not reflect the true
  average.

#### ProvisionedWriteCapacityUnits

The number of provisioned write capacity units for a table or a global
secondary index.

The `TableName` dimension returns the
`ProvisionedWriteCapacityUnits` for the table, but not for any
global secondary indexes. To view `ProvisionedWriteCapacityUnits` for
a global secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Minimum` – The lowest setting for provisioned write
  capacity. If you use `UpdateTable` to increase write
  capacity, this metric shows the lowest value of provisioned
  `WriteCapacityUnits` during this time period.
- `Maximum` – The highest setting for provisioned write
  capacity. If you use `UpdateTable` to decrease write
  capacity, this metric shows the highest value of provisioned
  `WriteCapacityUnits` during this time period.
- `Average` – The average provisioned write capacity.
  The `ProvisionedWriteCapacityUnits` metric is published at
  five-minute intervals. Therefore, if you rapidly adjust the provisioned
  write capacity units, this statistic might not reflect the true
  average.

#### ReadAccountLimitThrottleEvents

The number of read requests throttled due to account limits.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### ReadKeyRangeThroughputThrottleEvents

The number of read requests throttled due to partition limits.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### ReadMaxOnDemandThroughputThrottleEvents

The number of read requests throttled due to on-demand maximum
throughput.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### ReadProvisionedThroughputThrottleEvents

The number of read requests throttled due to provisioned throughput
limits.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### ReadThrottleEvents

Requests to DynamoDB that exceed the provisioned read capacity units for a table
or a global secondary index.

A single request can result in multiple events. For example, a
`BatchGetItem` that reads 10 items is processed as 10
`GetItem` events. For each event, `ReadThrottleEvents`
is incremented by one if that event is throttled. The
`ThrottledRequests` metric for the entire
`BatchGetItem` is not incremented unless _all
10_ of the `GetItem` events are throttled.

The `TableName` dimension returns the
`ReadThrottleEvents` for the table, but not for any global
secondary indexes. To view `ReadThrottleEvents` for a global
secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `SampleCount`
- `Sum`

#### ReplicationLatency

(This metric is for DynamoDB global tables.) The elapsed time between an updated
item appearing in the DynamoDB stream for one replica table, and that item
appearing in another replica in the global table.

Units: `Milliseconds`

Dimensions: `TableName, ReceivingRegion`

Valid Statistics:

- `Average`
- `Minimum`
- `Maximum`

#### ReturnedBytes

The number of bytes returned by `GetRecords` operations (Amazon DynamoDB Streams)
during the specified time period.

Units: `Bytes`

Dimensions: `Operation, StreamLabel, TableName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### ReturnedItemCount

The number of items returned by `Query`, `Scan` or
`ExecuteStatement` (select) operations during the specified time
period.

The number of items _returned_ is not necessarily the same
as the number of items that were evaluated. For example, suppose that you
requested a `Scan` on a table or an index that had 100 items, but
specified a `FilterExpression` that narrowed the results so that only
15 items were returned. In this case, the response from `Scan` would
contain a `ScanCount` of 100 and a `Count` of 15 returned
items.

Units: `Count`

Dimensions: `TableName, Operation`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### ReturnedRecordsCount

The number of stream records returned by `GetRecords` operations
(Amazon DynamoDB Streams) during the specified time period.

Units: `Count`

Dimensions: `Operation, StreamLabel, TableName`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`
- `Sum`

#### SuccessfulRequestLatency

The latency of successful requests to DynamoDB or Amazon DynamoDB Streams during the specified
time period. `SuccessfulRequestLatency` can provide two different
kinds of information:

- The elapsed time for successful requests (`Minimum`,
  `Maximum`, `Sum`, `Average`, or
  `Percentile`).
- The number of successful requests (`SampleCount`).

`SuccessfulRequestLatency` reflects activity only within DynamoDB or
Amazon DynamoDB Streams, and doesn't consider network latency or client-side activity.

###### Note

To analyze custom percentile values (such as p99.9), you can manually
enter the desired percentile (e.g., p99.9) in the CloudWatch metric statistic
field. This allows you to evaluate latency distributions beyond the
default percentiles listed in the dropdown.

Units: `Milliseconds`

Dimensions: `TableName, Operation, StreamLabel`

Valid Statistics:

- `Minimum`
- `Maximum`
- `Sum`
- `Average`
- `Percentile`
- `SampleCount`

#### SystemErrors

The requests to DynamoDB or Amazon DynamoDB Streams that generate an HTTP 500 status code during
the specified time period. An HTTP 500 usually indicates an internal service
error.

###### Note

When DynamoDB returns a system error (HTTP 500), most AWS SDKs
automatically perform a configurable number of retries. If the issue
resolves during a retry, your application continues without seeing the
error, and you may notice increased client-side perceived latency. If the
error persists after all retries, it propagates to your application code.

Units: `Count`

Dimensions: `TableName, Operation`

Valid Statistics:

- `Sum`
- `SampleCount`

#### TimeToLiveDeletedItemCount

The number of items deleted by Time to Live (TTL) during the specified time
period. This metric helps you monitor the rate of TTL deletions on your table.

Units: `Count`

Dimensions: TableName

Valid Statistics:

- `Sum`

#### ThrottledPutRecordCount

The number of records that were throttled by your Kinesis data stream due to
insufficient Kinesis Data Streams capacity.

Units: `Count`

Dimensions: TableName, DelegatedOperation

Valid Statistics:

- `Minimum`
- `Maximum`
- `Average`
- `SampleCount`

#### ThrottledRequests

Requests to DynamoDB that exceed the provisioned throughput limits on a resource
(such as a table or an index).

`ThrottledRequests` is incremented by one if any event within a
request exceeds a provisioned throughput limit. For example, if you update an
item in a table with global secondary indexes, there are multiple events—a
write to the table, and a write to each index. If one or more of these events
are throttled, then `ThrottledRequests` is incremented by one.

###### Note

In a batch request (`BatchGetItem` or
`BatchWriteItem`), `ThrottledRequests` is
incremented only if _every_ request in the batch is
throttled.

If any individual request within the batch is throttled, one of the
following metrics is incremented:

- `ReadThrottleEvents` – For a throttled
  `GetItem` event within
  `BatchGetItem`.
- `WriteThrottleEvents` – For a throttled
  `PutItem` or `DeleteItem` event within
  `BatchWriteItem`.

To gain insight into which event is throttling a request, compare
`ThrottledRequests` with the `ReadThrottleEvents` and
`WriteThrottleEvents` for the table and its indexes.

###### Note

A throttled request will result in an HTTP 400 status code. All such
events are reflected in the `ThrottledRequests` metric, but not
in the `UserErrors` metric.

Units: `Count`

Dimensions: `TableName, Operation`

Valid Statistics:

- `Sum`
- `SampleCount`

#### TransactionConflict

Rejected item-level requests due to transactional conflicts between concurrent
requests on the same items. For more information, see [Transaction Conflict Handling in DynamoDB](transaction-apis.md#transaction-conflict-handling "transaction-apis.md#transaction-conflict-handling").

Units: `Count`

Dimensions: `TableName`

Valid Statistics:

- `Sum` – The number of rejected item-level requests
  due to transaction conflicts.

###### Note

If multiple item-level requests within a call to
`TransactWriteItems` or `TransactGetItems`
were rejected, `Sum` is incremented by one for each
item-level `Put`, `Update`,
`Delete`, or `Get` request.

- `SampleCount` – The number of rejected requests due
  to transaction conflicts.

###### Note

If multiple item-level requests within a call to
`TransactWriteItems` or `TransactGetItems`
are rejected, `SampleCount` is only incremented by
one.

- `Min` – The minimum number of rejected item-level
  requests within a call to `TransactWriteItems`,
  `TransactGetItems`, `PutItem`,
  `UpdateItem`, or `DeleteItem`.
- `Max` – The maximum number of rejected item-level
  requests within a call to `TransactWriteItems`,
  `TransactGetItems`, `PutItem`,
  `UpdateItem`, or `DeleteItem`.
- `Average` – The average number of rejected item-level
  requests within a call to `TransactWriteItems`,
  `TransactGetItems`, `PutItem`,
  `UpdateItem`, or `DeleteItem`.

#### UserErrors

Requests to DynamoDB or Amazon DynamoDB Streams that generate an HTTP 400 status code during the
specified time period. An HTTP 400 usually indicates a client-side error, such
as an invalid combination of parameters, an attempt to update a nonexistent
table, or an incorrect request signature.

Some examples of exceptions that will log metrics related to
`UserErrors` would be:

- `ResourceNotFoundException`
- `ValidationException`
- `TransactionConflict`

All such events are reflected in the `UserErrors` metric, except
for the following:

- _ProvisionedThroughputExceededException_ –
  See the `ThrottledRequests` metric in this section.
- _ConditionalCheckFailedException_ – See the
  `ConditionalCheckFailedRequests` metric in this
  section.

`UserErrors` represents the aggregate of HTTP 400 errors for DynamoDB
or Amazon DynamoDB Streams requests for the current AWS Region and the current AWS
account.

Units: `Count`

Valid Statistics:

- `Sum`
- `SampleCount`

#### WriteAccountLimitThrottleEvents

The number of write requests throttled due to account limits.

Units: `Count`

Dimensions: `TableName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### WriteKeyRangeThroughputThrottleEvents

The number of write requests throttled due to partition limits.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### WriteMaxOnDemandThroughputThrottleEvents

The number of write requests throttled due to on-demand maximum
throughput.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### WriteProvisionedThroughputThrottleEvents

The number of write requests throttled due to provisioned throughput
limits.

Units: `Count`

Dimensions: `TableName`,
`GlobalSecondaryIndexName`

Valid Statistics:

- `Sum` – Total number of throttled events.
- `SampleCount` – Number of throttling
  occurrences.
- `Minimum` – Minimum number of throttled events in any
  given sample.
- `Maximum` – Maximum number of throttled events in any
  given sample.

#### WriteThrottleEvents

Requests to DynamoDB that exceed the provisioned write capacity units for a table
or a global secondary index.

A single request can result in multiple events. For example, a
`PutItem` request on a table with three global secondary indexes
would result in four events—the table write, and each of the three index
writes. For each event, the `WriteThrottleEvents` metric is
incremented by one if that event is throttled. For single `PutItem`
requests, if any of the events are throttled, `ThrottledRequests` is
also incremented by one. For `BatchWriteItem`, the
`ThrottledRequests` metric for the entire
`BatchWriteItem` is not incremented unless all of the individual
`PutItem` or `DeleteItem` events are throttled.

The `TableName` dimension returns the
`WriteThrottleEvents` for the table, but not for any global
secondary indexes. To view `WriteThrottleEvents` for a global
secondary index, you must specify both `TableName` and
`GlobalSecondaryIndexName`.

Units: `Count`

Dimensions: `TableName, GlobalSecondaryIndexName`

Valid Statistics:

- `Sum`
- `SampleCount`

### Usage metrics

Usage metrics in CloudWatch allow you to proactively manage usage by visualizing metrics
in the CloudWatch console, creating custom dashboards, detecting changes in activity with
CloudWatch anomaly detection, and configuring alarms that alert you when usage approaches
a threshold.

DynamoDB also integrates these usage metrics with Service Quotas. You can use CloudWatch to
manage your account's use of your service quotas. For more information, see [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md")

###### List of Available Usage

Metrics

- [AccountProvisionedWriteCapacityUnits](#w2aac39c15c13b7c11b9 "#w2aac39c15c13b7c11b9")
- [AccountProvisionedReadCapacityUnits](#w2aac39c15c13b7c11c11 "#w2aac39c15c13b7c11c11")
- [TableCount](#w2aac39c15c13b7c11c13 "#w2aac39c15c13b7c11c13")

#### AccountProvisionedWriteCapacityUnits

The sum of write capacity units provisioned for all tables and global
secondary indexes of an account.

Units: `Count`

Valid Statistics:

- `Minimum` – The lowest number of provisioned write capacity
  units during a time period.
- `Maximum` – The highest number of provisioned write
  capacity units during a time period.
- `Average` - The average number provisioned write capacity
  units account during a time period.

This metric is published at five-minute intervals. Therefore, if you rapidly
adjust the provisioned write capacity units, this statistic might not reflect
the true average.

#### AccountProvisionedReadCapacityUnits

The sum of read capacity units provisioned for all tables and global secondary
indexes of an account.

Units: `Count`

Valid Statistics:

- `Minimum` – The lowest number of provisioned read capacity
  units during a time period.
- `Maximum` – The highest number of provisioned read capacity
  units during a time period.
- `Average` - The average number provisioned read capacity
  units account during a time period.

This metric is published at five-minute intervals. Therefore, if you rapidly
adjust the provisioned read capacity units, this statistic might not reflect the
true average.

#### TableCount

The number of active tables of an account.

Units: `Count`

Valid Statistics:

- `Minimum` – The lowest number of tables during a time
  period.
- `Maximum` – The highest number of tables during a time
  period.
- `Average` - The average number tables during a time period.

## Understanding metrics and

dimensions for DynamoDB

The metrics for DynamoDB are qualified by the values for the account, table name, global
secondary index name, or operation. You can use the CloudWatch console to retrieve DynamoDB data
along any of the dimensions in the table below.

###### List of Available Dimensions

- [DelegatedOperation](#w2aac39c15c13b9b7 "#w2aac39c15c13b9b7")
- [GlobalSecondaryIndexName](#w2aac39c15c13b9b9 "#w2aac39c15c13b9b9")
- [Operation](#w2aac39c15c13b9c11 "#w2aac39c15c13b9c11")
- [OperationType](#w2aac39c15c13b9c13 "#w2aac39c15c13b9c13")
- [Verb](#w2aac39c15c13b9c15 "#w2aac39c15c13b9c15")
- [ReceivingRegion](#w2aac39c15c13b9c17 "#w2aac39c15c13b9c17")
- [StreamLabel](#w2aac39c15c13b9c19 "#w2aac39c15c13b9c19")
- [TableName](#w2aac39c15c13b9c21 "#w2aac39c15c13b9c21")

### DelegatedOperation

This dimension limits the data to operations DynamoDB performs on your behalf. The
following operations are captured:

- Change data capture for Kinesis Data Streams.

### GlobalSecondaryIndexName

This dimension limits the data to a global secondary index on a table. If you
specify `GlobalSecondaryIndexName`, you must also specify
`TableName`.

### Operation

This dimension limits the data to one of the following DynamoDB operations:

- `PutItem`
- `DeleteItem`
- `UpdateItem`
- `GetItem`
- `BatchGetItem`
- `Scan`
- `Query`
- `BatchWriteItem`
- `TransactWriteItems`
- `TransactGetItems`
- `ExecuteTransaction`
- `BatchExecuteStatement`
- `ExecuteStatement`

In addition, you can limit the data to the following Amazon DynamoDB Streams operation:

- `GetRecords`

### OperationType

This dimension limits the data to one of the following operation types:

- `Read`
- `Write`

This dimension is emitted for `ExecuteTransaction` and
`BatchExecuteStatement` requests.

### Verb

This dimension limits the data to one of the following DynamoDB PartiQL verbs:

- Insert: `PartiQLInsert`
- Select: `PartiQLSelect`
- Update: `PartiQLUpdate`
- Delete: `PartiQLDelete`

This dimension is emitted for the `ExecuteStatement` operation.

### ReceivingRegion

This dimension limits the data to a particular AWS region. It is used with
metrics originating from replica tables within a DynamoDB global table.

### StreamLabel

This dimension limits the data to a specific stream label. It is used with metrics
originating from Amazon DynamoDB Streams `GetRecords` operations.

### TableName

This dimension limits the data to a specific table. This value can be any table
name in the current region and the current AWS account.
