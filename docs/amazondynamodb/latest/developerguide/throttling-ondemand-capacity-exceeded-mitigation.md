# 4- On-demand maximum

throughput exceeded

When you configure an [on-demand](on-demand-capacity-mode.md "on-demand-capacity-mode.md") table or
GSI, you can optionally set a maximum throughput limit ([`MaxReadRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits") and [`MaxWriteRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits")) at the table or index level to prevent
runaway costs or protect downstream systems from being overwhelmed. For more information
about maximum throughput, see [DynamoDB maximum throughput
for on-demand tables](on-demand-capacity-mode-max-throughput.md "on-demand-capacity-mode-max-throughput.md").

When your read or write consumption exceeds these self-imposed limits, additional
requests that would exceed the limit receive quick throttle responses. DynamoDB returns
exceptions with a `MaxOnDemandThroughputExceeded` throttling reason type,
indicating which resource has reached its throughput boundary.

## On-demand maximum throughput

exceeded throttling

This section provides resolution guidance for on-demand maximum throughput exceeded
throttling scenarios. Before using this guide, ensure you have identified the specific
throttling reasons from your application's exception handling, and determined the Amazon
Resource Name (ARN) of the affected resource. For information on retrieving throttling
reasons and identifying throttled resources, see [DynamoDB throttling diagnosis framework](throttling-diagnosing-workflow.md#throttling-diagnosing "throttling-diagnosing-workflow.md#throttling-diagnosing").

Before diving into specific throttling scenarios, first consider whether action is
actually needed:

- **Evaluate your maximum throughput settings:**
  These limits were intentionally configured to control costs or protect
  downstream systems. If you're receiving
  `MaxOnDemandThroughputExceeded` throttling events, your limits
  are working as designed. Consider whether increasing these limits aligns with
  your original cost control or system protection goals.
- **Assess application impact:** Determine if the
  throttling is actually causing problems for your applications or users. If your
  applications handle retries effectively and meets their performance requirements
  despite occasional throttling, maintaining your current limits might be the
  appropriate choice.
- **Review traffic patterns:** Analyze whether the
  throttling represents an expected traffic pattern or an unusual spike. For
  predictable, recurring traffic patterns that consistently exceed your limits,
  adjusting the maximum throughput settings might be warranted. For temporary
  spikes, implementing better request distribution strategies might be more
  appropriate than raising limits.

If after consideration you determine that your maximum throughput settings need
adjustment, refer to the specific throttling scenarios below for targeted remediation
options:

- [TableReadMaxOnDemandThroughputExceeded](#throttling-diagnostic-table-read-max-ondemand "#throttling-diagnostic-table-read-max-ondemand")
- [TableWriteMaxOnDemandThroughputExceeded](#throttling-diagnostic-table-write-max-ondemand "#throttling-diagnostic-table-write-max-ondemand")
- [IndexReadMaxOnDemandThroughputExceeded](#throttling-diagnostic-index-read-max-ondemand "#throttling-diagnostic-index-read-max-ondemand")
- [IndexWriteMaxOnDemandThroughputExceeded](#throttling-diagnostic-index-write-max-ondemand "#throttling-diagnostic-index-write-max-ondemand")

### TableReadMaxOnDemandThroughputExceeded

###### When this occurs

Your on-demand table has exceeded its configured maximum read throughput
capacity. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#ondemand-capacity-exceeded-diagnosis-monitoring "#ondemand-capacity-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Increase maximum throughput limit:** Use
  the [DynamoDB console](https://console.aws.amazon.com/dynamodb "https://console.aws.amazon.com/dynamodb"), [AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI"), or the DynamoDB `UpdateTable` API to increase the [`MaxReadRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits") value for the affected
  table, then monitor and adjust. This allows your table to handle higher read
  throughput before throttling occurs.
- **Remove the maximum limit:** Set
  `MaxReadRequestUnits` to `-1` to remove the
  ceiling, allowing scaling based on demand up to your account-level
  throughput quotas. This removes your custom limit but still maintains
  AWS's account-level safeguards. However, it's important to monitor
  spending closely after removing this limit, as your table can now consume
  significantly more capacity before hitting the account-level quotas.

### TableWriteMaxOnDemandThroughputExceeded

###### When this occurs

Your on-demand table has exceeded its configured maximum write throughput
capacity. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#ondemand-capacity-exceeded-diagnosis-monitoring "#ondemand-capacity-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Increase maximum throughput limit:** Use
  the [DynamoDB console](https://console.aws.amazon.com/dynamodb "https://console.aws.amazon.com/dynamodb"), [AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI"), or the DynamoDB `UpdateTable` API to increase the [`MaxWriteRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits") value for the affected
  table, then monitor and adjust.
- **Remove the maximum limit:** Set
  `MaxWriteRequestUnits` to `-1` to remove the
  ceiling, allowing scaling based on demand up to your account-level
  throughput quotas. This removes your custom limit but still maintains
  AWS's account-level safeguards. However, it's important to monitor
  spending closely after removing this limit, as your table can now consume
  significantly more capacity before hitting the account-level quotas.

### IndexReadMaxOnDemandThroughputExceeded

###### When this occurs

Read requests to a GSI in on-demand mode have exceeded the GSI's configured
maximum read throughput capacity. You can monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#ondemand-capacity-exceeded-diagnosis-monitoring "#ondemand-capacity-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Increase GSI maximum throughput limit:**
  Use the [DynamoDB console](https://console.aws.amazon.com/dynamodb "https://console.aws.amazon.com/dynamodb"), [AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI"), or the DynamoDB `UpdateTable` API to increase the [`MaxReadRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxReadRequestUnits") value for the affected
  GSI, then monitor and adjust.
- **Remove the GSI maximum limit:** Set
  `MaxReadRequestUnits` to `-1` for the GSI to
  remove the ceiling, allowing scaling based on demand up to your
  account-level throughput quotas. This removes your custom limit but still
  maintains AWS's account-level safeguards. However, it's important to
  monitor spending closely after removing this limit.

### IndexWriteMaxOnDemandThroughputExceeded

###### When this occurs

Updates to items in the base table trigger writes to a GSI in on-demand mode
that exceed the GSI's configured maximum write throughput capacity, causing
[back-pressure throttling](gsi-throttling.md "gsi-throttling.md"). You can
monitor the CloudWatch metrics in [Common diagnosis and
monitoring](#ondemand-capacity-exceeded-diagnosis-monitoring "#ondemand-capacity-exceeded-diagnosis-monitoring") to analyze your
throttling event.

###### Remediation options

Consider these steps to address your throttling events:

- **Increase GSI maximum throughput limit:**
  Use the [DynamoDB console](https://console.aws.amazon.com/dynamodb "https://console.aws.amazon.com/dynamodb"), [AWS CLI](AccessingDynamoDB.md#Tools.CLI "AccessingDynamoDB.md#Tools.CLI"), or the DynamoDB `UpdateTable` API to increase the [`MaxWriteRequestUnits`](../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits "../APIReference/API_OnDemandThroughput.md#DDB-Type-OnDemandThroughput-MaxWriteRequestUnits") value for the affected
  GSI, then monitor and adjust.
- **Remove the GSI maximum limit:** Set
  `MaxWriteRequestUnits` to `-1` for the GSI to
  remove the ceiling, allowing scaling based on demand up to your
  account-level throughput quotas. This removes your custom limit but still
  maintains AWS's account-level safeguards. However, it's important to
  monitor spending closely after removing this limit.

## Common diagnosis and

monitoring

When troubleshooting on-demand maximum throughput exceeded throttling events, several
CloudWatch metrics can help identify the root cause and scaling patterns.

###### Essential CloudWatch metrics

Monitor these key metrics to diagnose on-demand maximum throughput exceeded
throttling:

- **Maximum throughput throttling events:**
  [`ReadMaxOnDemandThroughputThrottleEvents`](metrics-dimensions.md#ReadMaxOnDemandThroughputThrottleEvents "metrics-dimensions.md#ReadMaxOnDemandThroughputThrottleEvents") and [`WriteMaxOnDemandThroughputThrottleEvents`](metrics-dimensions.md#WriteMaxOnDemandThroughputThrottleEvents "metrics-dimensions.md#WriteMaxOnDemandThroughputThrottleEvents") track
  when requests are throttled due to exceeding maximum limits. [`ReadThrottleEvents`](metrics-dimensions.md#ReadThrottleEvents "metrics-dimensions.md#ReadThrottleEvents") and [`WriteThrottleEvents`](metrics-dimensions.md#WriteThrottleEvents "metrics-dimensions.md#WriteThrottleEvents") track when any read or write
  requests exceed the provisioned capacity.
- **Current maximum throughput configured for a table or
  global secondary index:**
  [`OnDemandMaxReadRequestUnits`](metrics-dimensions.md#OnDemandMaxReadRequestUnits "metrics-dimensions.md#OnDemandMaxReadRequestUnits") and [`OnDemandMaxWriteRequestUnits`](metrics-dimensions.md#OnDemandMaxWriteRequestUnits "metrics-dimensions.md#OnDemandMaxWriteRequestUnits") show the current
  maximum capacity limits.
- **Actual capacity consumption:**
  [`ConsumedReadCapacityUnits`](metrics-dimensions.md#ConsumedReadCapacityUnits "metrics-dimensions.md#ConsumedReadCapacityUnits") and [`ConsumedWriteCapacityUnits`](metrics-dimensions.md#ConsumedWriteCapacityUnits "metrics-dimensions.md#ConsumedWriteCapacityUnits") show actual usage
  patterns.

###### Analysis approach

Follow these steps to confirm on-demand maximum throughput exceeded
diagnosis:

1. Compare consumed capacity to maximum capacity limits - check if consumption
   consistently approaches or exceeds maximum limits.
2. Review throttling event frequency and timing to identify patterns. Look for
   sudden increases in consumed capacity that coincides with your throttling
   event.
3. Use [CloudWatch Contributor
   Insights](contributorinsights_HowItWorks.md "contributorinsights_HowItWorks.md") to identify which items or partition keys consume the most
   capacity.
