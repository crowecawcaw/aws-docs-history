# Throughput modes

Amazon SageMaker Feature Store provides two pricing models to choose from: on-demand (`On-demand`) and
provisioned (`Provisioned`) throughput modes. `On-demand` works best for
less predictable traffic, while `Provisioned` works best for consistent and
predictable traffic.

You have the option to switch between `On-demand` and `Provisioned`
throughput modes for a given feature group, to accommodate periods in which application traffic
patterns are changing or less predictable. You can only update your feature group throughput
mode to `On-demand` once in a 24 hour period. The throughput mode can be updated
programmatically using the [UpdateFeatureGroup](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md") API
or through the console UI. For more information about using the console, see [Using Amazon SageMaker Feature Store in the console](feature-store-use-with-studio.md "feature-store-use-with-studio.md").

You can use the `Provisioned` throughput mode with offline-only feature groups or
feature groups with the `Standard` storage type. For other storage configurations,
the `On-demand` throughput mode is used. For information about the online and offline
storage configurations, see [Online store](feature-store-storage-configurations-online-store.md "feature-store-storage-configurations-online-store.md") and [Offline
store](feature-store-storage-configurations-offline-store.md "feature-store-storage-configurations-offline-store.md"), respectively.

For more details about pricing, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

###### Topics

- [On-demand throughput mode](#feature-store-throughput-mode-on-demand "#feature-store-throughput-mode-on-demand")
- [Provisioned throughput
  mode](#feature-store-throughput-mode-provisioned "#feature-store-throughput-mode-provisioned")
- [Throughput mode metrics](#feature-store-throughput-mode-metrics "#feature-store-throughput-mode-metrics")
- [Throughput mode limits](#feature-store-throughput-mode-limits "#feature-store-throughput-mode-limits")

## On-demand throughput mode

The `On-demand` (default) throughput mode works best when you are using feature
groups with unknown workload, unpredictable application traffic, and you cannot forecast the
capacity requirements.

The `On-demand` mode charges you for the reads and writes that your application
performs on your feature groups. You do not need to specify how much read and write throughput
you expect your application to perform because Feature Store instantly accommodates your workloads as
they ramp up or down. You pay only for what you use, which is measured in
`ReadRequestsUnits` and `WriteRequestsUnits`.

You can enable the `On-demand` throughput mode using the [CreateFeatureGroup](../APIReference/API_CreateFeatureGroup.md "../APIReference/API_CreateFeatureGroup.md") or [UpdateFeatureGroup](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md")
APIs or through the console UI. For more information about using the console UI, see [Using Amazon SageMaker Feature Store in the console](feature-store-use-with-studio.md "feature-store-use-with-studio.md").

###### Important

You can only update your feature group throughput mode to `On-demand` once in
a 24 hour period.

## Provisioned throughput

mode

The `Provisioned` throughput mode works best when you are using feature groups
with predictable workloads and you can forecast the capacity requirements to control costs.
This can make it more cost effective for certain workloads where you can anticipate throughput
requirements in advance.

When you set a feature group to `Provisioned` mode, you specify capacity units
which are the maximum amount of capacity that an application can consume from a feature group.
If your application exceeds this `Provisioned` throughput capacity, it is subject
to request throttling.

The following includes information about the read and write capacity units.

- Retrieving a single record of up to 4 KB using the `GetRecord` API will
  consume _at least_ 1 RCU (read capacity unit). Retrieving
  larger payloads may take more. The total number of read capacity units required depends on
  the item size, including a small per record metadata added by the Feature Store service.
- A single write request with a payload of 1 KB using the `PutRecord` API
  will consume _at least_ 1 WCU (write capacity unit), with
  fractional payloads rounded up to nearest KB. It may consume more depending on the event
  time, deletion status of the record, and time to live (TTL) status. For more information
  about TTL, see [Time to live (TTL) duration for records](feature-store-time-to-live.md "feature-store-time-to-live.md").

###### Important

When setting your capacity units please consider the following:

- You will be charged for the read and write capacities you provision for your feature
  group, even if you do not fully utilize the `Provisioned` capacity.
- If you set a read or write capacity too low, your requests may experience
  throttling.
- In some cases, records may consume an extra capacity unit due to record level
  metadata that is added by the Feature Store service to enable various features.
- Retrieving only a subset of features using `GetRecord` or
  `BatchGetRecord` APIs will still consume RCU corresponding to the entire
  record.
- For write capacity, you should provision 2x the recent peak capacity to avoid
  throttling when performing backfills or bulk ingestion that may result in a large number
  of historical record writes. This is because writing historical records consumes
  additional write capacity.
- Feature Store does not currently support auto scaling for `Provisioned` mode.

You can enable the `On-demand` throughput mode using the [CreateFeatureGroup](../APIReference/API_CreateFeatureGroup.md "../APIReference/API_CreateFeatureGroup.md") or [UpdateFeatureGroup](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md")
APIs or through the console UI. For more information about using the console UI, see [Using Amazon SageMaker Feature Store in the console](feature-store-use-with-studio.md "feature-store-use-with-studio.md").

The following describes how you can increase or decrease the RCU and WCU throughput for
your feature groups when `Provisioned` mode is enabled.

**Increasing provisioned throughput**

You can increase RCU or WCU as often as needed using the [UpdateFeatureGroup](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md")
API or the console UI.

**Decreasing provisioned throughput**

You can decrease RCU and WCU (or both) for feature groups using [UpdateFeatureGroup](../APIReference/API_UpdateFeatureGroup.md "../APIReference/API_UpdateFeatureGroup.md") API or the console UI.

There is a default quota on the number of `Provisioned` capacity decreases you
can perform on your feature group per day. A day is defined according to Universal Time
Coordinated (UTC). On a given day, you can start by performing up to four decreases within one
hour as long as you have not performed any other decreases yet during that day. Subsequently,
you can perform one additional decrease per hour as long as there were no decreases in the
preceding hour. This effectively brings the maximum number of decreases in a day to 27 times
(4 decreases in the first hour, and 1 decrease for each of the subsequent 1-hour windows in a
day).

## Throughput mode metrics

A feature group in `On-demand` mode will emit
`ConsumedReadRequestsUnits` and `ConsumedWriteRequestsUnits` metrics.
A feature group in `Provisioned` mode will emit
`ConsumedReadCapacityUnits` and `ConsumedWriteCapacityUnits` metrics.
For more information about Feature Store metrics, see [Amazon SageMaker Feature Store metrics](monitoring-cloudwatch.md#cloudwatch-metrics-feature-store "monitoring-cloudwatch.md#cloudwatch-metrics-feature-store").

## Throughput mode limits

Each AWS account has default service quotas or limits that are applied to help ensure
availability and manage billing risks. For information about the default quotas and limits,
see [Quotas, naming rules and data types](feature-store-quotas.md "feature-store-quotas.md").

In some cases, these limits may be lower than what is stated in the documentation. If you
need higher limits, you can submit a request for an increase. It's a good idea to do so before
reaching current limits to avoid interruptions to your work. For information about service
quotas and how to request a quota increase, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").
