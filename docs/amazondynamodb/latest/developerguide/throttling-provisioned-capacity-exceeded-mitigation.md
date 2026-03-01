# 2- Provisioned throughput exceeded

Provisioned capacity throttling occurs when your application's consumption rate exceeds
the read or write capacity units (RCUs/WCUs) configured for your tables or global secondary
indexes. While DynamoDB provides burst capacity to handle occasional traffic spikes, sustained
requests beyond your provisioned limits result in throttling. When this happens, DynamoDB
returns a `ProvisionedThroughputExceeded` throttling reason type in the
throttling exception. The reason identifies whether the issue is with read or write
operations and whether it affects the base table or a global secondary index.

Throttling can occur regardless of whether Auto Scaling is enabled. Auto Scaling adapts to
increases in consumption, but it does not respond instantly and it is constrained by the
maximum capacity limits you configure. This means throttling can still occur during sudden
traffic spikes or when consumption exceeds your maximum Auto Scaling limits.

## Provisioned throughput exceeded mitigation measures

This section provides resolution guidance for provisioned capacity throttling
scenarios. Before using this guide, ensure you have identified the specific throttling
reason from your application's exception handling, and determined the Amazon Resource
Name (ARN) of the affected resource. For information on retrieving throttling reasons
and identifying throttled resources, see [DynamoDB throttling diagnosis framework](throttling-diagnosing-workflow.md#throttling-diagnosing "throttling-diagnosing-workflow.md#throttling-diagnosing").

Before diving into specific throttling scenarios, first consider if the throttling is
actually a problem that needs resolution:

- Occasional throttling is normal and expected in well-optimized DynamoDB
  applications. Throttling simply means you're consuming 100% of what you've
  provisioned. If your application handles throttling gracefully with retries and
  your overall performance meets requirements, the throttling may not require
  immediate action.
- However, if throttling is causing unacceptable client-side latency, degrading
  user experience, or preventing critical operations from completing in a timely
  manner, then proceed with the mitigation options below.

When you need to address throttling issues, first determine if your throttling is
caused by:

- **Temporary traffic spikes:** Short-duration
  increases in traffic that exceed your provisioned capacity but aren't sustained.
  These require different strategies than continuous high traffic.
- **Continuous high traffic:** Sustained workloads
  that consistently exceed your provisioned capacity.

For traffic spikes, consider the strategies from the _Handle
traffic spikes with Amazon DynamoDB provisioned capacity_ blog in [Additional resources](#throttling-additional-resources "#throttling-additional-resources").

For continuous high traffic, consider the capacity adjustment options below:

- [TableReadProvisionedThroughputExceeded](#throttling-table-read-provisioned "#throttling-table-read-provisioned")
- [TableWriteProvisionedThroughputExceeded](#throttling-table-write-provisioned "#throttling-table-write-provisioned")
- [IndexReadProvisionedThroughputExceeded](#throttling-index-read-provisioned "#throttling-index-read-provisioned")
- [IndexWriteProvisionedThroughputExceeded](#throttling-index-write-provisioned "#throttling-index-write-provisioned")

### TableReadProvisionedThroughputExceeded

###### When this occurs

Your application's read consumption rate exceeds the [provisioned read capacity units](../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-ReadCapacityUnits "../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-ReadCapacityUnits") (RCUs) configured for your table.
You can monitor the CloudWatch metrics in [Common diagnosis and monitoring](#provisioned-capacity-exceeded-diagnosis-monitoring "#provisioned-capacity-exceeded-diagnosis-monitoring") to analyze
your throttling event.

###### Resolution approach

Consider these strategies to resolve read capacity throttling:

- **Switch to on-demand capacity mode:**
  Consider [switching your table to
  on-demand](#procedure-switch-ondemand "#procedure-switch-ondemand") if you experience frequent throttling from traffic
  spikes. On-demand eliminates provisioning concerns and automatically scales
  with your workload.
- **If staying with provisioned mode and Auto Scaling is
  not enabled:**
  - Consider [increasing the table read capacity.](#provisioned-capacity-exceeded-increase-table-throughput "#provisioned-capacity-exceeded-increase-table-throughput")
  - [Enable
    Auto Scaling for read capacity](#provisioned-capacity-configure-autoscaling "#provisioned-capacity-configure-autoscaling") on your table.

- **If Auto Scaling is enabled (default for tables
  created in the console):**
  - [Optimize your table's read Auto Scaling
    parameters](#provisioned-capacity-optimize-autoscaling-settings "#provisioned-capacity-optimize-autoscaling-settings").

### TableWriteProvisionedThroughputExceeded

###### When this occurs

Your application's write consumption rate exceeds the [provisioned write capacity units](../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-WriteCapacityUnits "../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-WriteCapacityUnits") (WCUs) configured for your table.
You can monitor the CloudWatch metrics in [Common diagnosis and monitoring](#provisioned-capacity-exceeded-diagnosis-monitoring "#provisioned-capacity-exceeded-diagnosis-monitoring") to analyze
your throttling event.

###### Resolution approach

Consider these strategies to resolve write capacity throttling:

- **Switch to on-demand capacity mode:**
  Consider [switching your table to
  on-demand](#procedure-switch-ondemand "#procedure-switch-ondemand") if you experience frequent throttling from traffic
  spikes. On-demand eliminates provisioning concerns and automatically scales
  with your workload.
- **If staying with provisioned mode and Auto Scaling is
  not enabled:**
  - Consider [increasing the table write capacity](#provisioned-capacity-exceeded-increase-table-throughput "#provisioned-capacity-exceeded-increase-table-throughput").
  - [Enable
    Auto Scaling for write capacity](#provisioned-capacity-configure-autoscaling "#provisioned-capacity-configure-autoscaling") on your table.

- **If Auto Scaling is enabled (default for tables
  created in the console):**
  - [Optimize your table's write Auto Scaling
    parameters](#provisioned-capacity-optimize-autoscaling-settings "#provisioned-capacity-optimize-autoscaling-settings").

### IndexReadProvisionedThroughputExceeded

###### When this occurs

Read consumption on a Global Secondary Index (GSI) exceeds the GSI's [provisioned read capacity units](../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-ReadCapacityUnits "../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-ReadCapacityUnits") (RCUs). You can monitor the CloudWatch
metrics in [Common diagnosis and monitoring](#provisioned-capacity-exceeded-diagnosis-monitoring "#provisioned-capacity-exceeded-diagnosis-monitoring")
to analyze your throttling event.

###### Resolution approach

Consider these strategies to resolve GSI read capacity throttling:

- **Switch to on-demand capacity mode:**
  Consider [switching the base table
  to on-demand](#procedure-switch-ondemand "#procedure-switch-ondemand") if you experience frequent throttling from traffic
  spikes. On-demand eliminates provisioning concerns and automatically scales
  with your workload.
- **If staying with provisioned mode and Auto Scaling is
  not enabled:**
  - Consider [increasing the GSI read capacity](#provisioned-capacity-exceeded-increase-index-throughput "#provisioned-capacity-exceeded-increase-index-throughput").
  - [Enable
    Auto Scaling for read capacity](#provisioned-capacity-configure-autoscaling "#provisioned-capacity-configure-autoscaling") on your GSI.

- **If Auto Scaling is enabled (default for tables
  created in the console):**
  - [Optimize your GSI's read Auto Scaling parameters](#provisioned-capacity-optimize-autoscaling-settings "#provisioned-capacity-optimize-autoscaling-settings").

### IndexWriteProvisionedThroughputExceeded

###### When this occurs

Updates to items in the base table trigger writes to a GSI that exceed the
[GSI's provisioned write capacity](../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-WriteCapacityUnits "../APIReference/API_ProvisionedThroughput.md#DDB-Type-ProvisionedThroughput-WriteCapacityUnits"). This causes [back-pressure throttling](gsi-throttling.md "gsi-throttling.md") on base table
writes. You can monitor the CloudWatch metrics in [Common diagnosis and monitoring](#provisioned-capacity-exceeded-diagnosis-monitoring "#provisioned-capacity-exceeded-diagnosis-monitoring") to analyze
your throttling event.

###### Resolution approach

Consider these strategies to resolve GSI write capacity throttling:

- **Switch to on-demand capacity mode:**
  Consider [switching the base table
  to on-demand](#procedure-switch-ondemand "#procedure-switch-ondemand") if you experience frequent throttling from traffic
  spikes. On-demand eliminates provisioning concerns and automatically scales
  with your workload.
- **If staying with provisioned mode and Auto Scaling is
  not enabled:**
  - Consider [increasing the GSI write capacity](#provisioned-capacity-exceeded-increase-index-throughput "#provisioned-capacity-exceeded-increase-index-throughput").
  - [Enable
    Auto Scaling for write capacity](#provisioned-capacity-configure-autoscaling "#provisioned-capacity-configure-autoscaling") on your GSI.

- **If Auto Scaling is enabled (default for tables
  created in the console):**
  - [Optimize your GSI's write Auto Scaling
    parameters](#provisioned-capacity-optimize-autoscaling-settings "#provisioned-capacity-optimize-autoscaling-settings").

## Common diagnosis and monitoring

When troubleshooting throughput errors, several CloudWatch metrics can help identify the
root cause.

###### Essential CloudWatch metrics

Monitor these key metrics to diagnose provisioned capacity throttling:

- **Throttling events:**
  [`ReadProvisionedThroughputThrottleEvents`](metrics-dimensions.md#ReadProvisionedThroughputThrottleEvents "metrics-dimensions.md#ReadProvisionedThroughputThrottleEvents") and [`WriteProvisionedThroughputThrottleEvents`](metrics-dimensions.md#WriteProvisionedThroughputThrottleEvents "metrics-dimensions.md#WriteProvisionedThroughputThrottleEvents") track
  when requests are throttled for this reason.[`ReadThrottleEvents`](metrics-dimensions.md#ReadThrottleEvents "metrics-dimensions.md#ReadThrottleEvents") and [`WriteThrottleEvents`](metrics-dimensions.md#WriteThrottleEvents "metrics-dimensions.md#WriteThrottleEvents") track when any read or write
  requests exceed the provisioned capacity.
- **Capacity consumption:**
  [`ConsumedReadCapacityUnits`](metrics-dimensions.md#ConsumedReadCapacityUnits "metrics-dimensions.md#ConsumedReadCapacityUnits") and [`ConsumedWriteCapacityUnits`](metrics-dimensions.md#ConsumedWriteCapacityUnits "metrics-dimensions.md#ConsumedWriteCapacityUnits") show actual
  usage.
- **Provisioned capacity:**
  [`ProvisionedReadCapacityUnits`](metrics-dimensions.md#ProvisionedReadCapacityUnits "metrics-dimensions.md#ProvisionedReadCapacityUnits") and [`ProvisionedWriteCapacityUnits`](metrics-dimensions.md#ProvisionedWriteCapacityUnits "metrics-dimensions.md#ProvisionedWriteCapacityUnits") show configured
  limits.

## Resolution procedures

### Increasing table throughput capacity

Use this procedure when Auto Scaling is not enabled and you need immediate
capacity increase.

1. Update your table's provisioned capacity using the DynamoDB console, AWS CLI,
   or SDK:
   - **For read capacity:** Increase the
     [`ReadCapacityUnits`](../APIReference/API_ProvisionedThroughput.md "../APIReference/API_ProvisionedThroughput.md") parameter, which
     specifies the maximum number of strongly consistent reads consumed
     per second before DynamoDB throttles requests.
   - **For write capacity:** Increase the
     [`WriteCapacityUnits`](../APIReference/API_ProvisionedThroughput.md "../APIReference/API_ProvisionedThroughput.md") parameter, which
     specifies the maximum number of writes consumed per second before
     DynamoDB throttles requests.

2. Verify that your new capacity settings don't exceed the [per-table throughput quotas](ServiceQuotas.md "ServiceQuotas.md") and that your
   total account consumption remains below the [per-account throughput quotas](ServiceQuotas.md "ServiceQuotas.md") for your Region. If you're
   approaching these limits, consider [switching to on-demand capacity mode](#procedure-switch-ondemand "#procedure-switch-ondemand") instead.

### Configuring table Auto Scaling to adjust the read or write capacity of your table or GSI

Configure DynamoDB [Auto Scaling](AutoScaling.md "AutoScaling.md") to automatically
adjust read or write capacity based on traffic patterns. You can configure Auto
Scaling independently for both tables and GSIs, with separate controls for read and
write capacity units.

1. Enable Auto Scaling for read capacity, write capacity, or both on your
   table or GSI.
2. Set a target utilization percentage with headroom for traffic
   spikes.

###### Note

Lower target utilization increases costs and scaling frequency.
Targets below 40% may cause over-provisioning. Monitor usage patterns
and costs to balance performance and efficiency. 3. Set capacity boundaries:

    * **Minimum RCUs/WCUs:** Maintains
     sufficient capacity during low-traffic periods.
    * **Maximum RCUs/WCUs:** Accommodates
     peak traffic demands and protects against runaway scaling
     events.

For guidance on configuring and managing DynamoDB Auto Scaling, see [Managing throughput capacity automatically with DynamoDB Auto
Scaling](AutoScaling.md "AutoScaling.md").

###### Note

Auto Scaling typically takes several minutes to respond to traffic changes.
For sudden traffic spikes, your table's burst capacity provides immediate
protection while Auto Scaling adjusts. Configure target utilization with
adequate headroom to allow time for scaling operations and to preserve burst
capacity for unexpected demand.

### Optimizing your table's or index's read or write Auto Scaling settings

Use this procedure when [Auto Scaling](AutoScaling.md "AutoScaling.md") is enabled
but throttling still occurs. You can tune Auto Scaling independently for both tables
and global secondary indexes (GSIs), with separate controls for read and write
capacity units.

- **Adjust target utilization:** Consider
  lowering the target utilization for your table or GSIs to trigger scaling
  earlier before throttling occurs. Ensure that you monitor your traffic after
  making these adjustments. See [Configuring table Auto Scaling to adjust the read or write capacity of your table or GSI](#provisioned-capacity-configure-autoscaling "#provisioned-capacity-configure-autoscaling") for more
  information about capacity consumption and cost implications.
- **Review capacity boundaries:** Ensure your
  minimum and maximum capacity settings align with your actual workload
  patterns.

### Switching to on-demand capacity mode

For general information about switching capacity modes, see [Considerations when switching capacity modes in DynamoDB](bp-switching-capacity-modes.md "bp-switching-capacity-modes.md"). Refer to the Service Quotas to learn
about specific [constraints
when switching mode](troubleshooting-throttling-diagnostics.md "troubleshooting-throttling-diagnostics.md").

### Increasing GSI throughput capacity

Use this procedure when Auto Scaling is not enabled on your GSI or you need
immediate capacity increase.

1. Update the GSI's provisioned capacity using the DynamoDB console, AWS CLI, or
   SDK:
   - **For read capacity:** Increase the
     [`ReadCapacityUnits`](../APIReference/API_GlobalSecondaryIndexUpdate.md "../APIReference/API_GlobalSecondaryIndexUpdate.md") parameter for the
     specific GSI, which specifies the maximum number of reads the GSI
     can consume per second before DynamoDB throttles requests. Note that
     GSIs only support eventually consistent reads.
   - **For write capacity:** Increase the
     [`WriteCapacityUnits`](../APIReference/API_GlobalSecondaryIndexUpdate.md "../APIReference/API_GlobalSecondaryIndexUpdate.md") parameter for the
     specific GSI, which specifies the maximum number of writes the GSI
     can consume per second before DynamoDB throttles requests.

2. Ensure that the GSI's provisioned throughput capacity remains within the
   [per-account and per-table throughput
   quotas](ServiceQuotas.md "ServiceQuotas.md").

## Additional resources

- For detailed information about handling traffic spikes in DynamoDB provisioned
  capacity tables, including various strategies from utilizing Auto Scaling and
  burst capacity to strategic throttle management, see [Handle traffic spikes with Amazon DynamoDB provisioned capacity](https://aws.amazon.com/blogs//database/handle-traffic-spikes-with-amazon-dynamodb-provisioned-capacity/ "https://aws.amazon.com/blogs//database/handle-traffic-spikes-with-amazon-dynamodb-provisioned-capacity/").
- For information about how to use a cron expression to schedule a scaling
  policy, see [Optimize costs by scheduling provisioned capacity for DynamoDB](https://aws.amazon.com/blogs/database/optimize-costs-by-scheduling-provisioned-capacity-for-amazon-dynamodb/ "https://aws.amazon.com/blogs/database/optimize-costs-by-scheduling-provisioned-capacity-for-amazon-dynamodb/").
- For hands-on information about monitoring and analyzing throughput utilization
  patterns for your DynamoDB tables in provisioned capacity mode, see [How to evaluate throughput utilization for Amazon DynamoDB tables in provisioned
  mode](https://aws.amazon.com/blogs/database/how-to-evaluate-throughput-utilization-for-amazon-dynamodb-tables-in-provisioned-mode/ "https://aws.amazon.com/blogs/database/how-to-evaluate-throughput-utilization-for-amazon-dynamodb-tables-in-provisioned-mode/").
