

# Monitor capacity fulfillment
<a name="capacity-manager-fulfillment"></a>

Capacity fulfillment metrics answer two questions about your Amazon EC2 capacity: how much of your requested capacity Amazon EC2 fulfills, and whether that capacity lands on your preferred instance types and Availability Zones. Capacity Manager organizes the metrics into two groups: fulfillment metrics and the instance type and Availability Zone breakdown. Both are available in the Capacity fulfillment tab of the Amazon EC2 Capacity Manager console and through the get-capacity-manager-metric-data API. Together, they help you analyze your capacity flexibility, so you can see where it is paying off and where to add more.

**Note**  
Capacity fulfillment metrics are available only to AWS Support customers on the [Unified Operations plan](https://docs.aws.amazon.com/awssupport/latest/user/unified-operations-intro.html).

Start at the organization level for a summary, then use dimensions such as tag, account, or Region to drill into the specific workloads where you need to act. Capacity fulfillment metrics are available through get-capacity-manager-metric-data with a minimum period of one hour.

**How to read the two groups together**

Capacity is measured at two levels, and you read them in order. **Request-level fulfillment** (the top level) answers the first question: how much of the requested capacity does Amazon EC2 fulfill? A request can be flexible across multiple instance type and Availability Zone combinations, where a combination is a single instance type in a single Availability Zone. A flexible request is fulfilled if any of those combinations delivers. For example, suppose you have a request that is flexible across ten combinations. It doesn't matter whether Amazon EC2 fulfills the capacity on the first instance type or the tenth. The request still counts as 100% fulfilled. A high request-level fulfillment rate is exactly what you want to see: it means your flexibility is working.

**Per-combination fulfillment** (the second level) takes each option within a flexible request into account, measuring how each individual instance type and Availability Zone combination performed. These rates are often lower than the request-level rate, because they don't include the benefit of a fallback (an alternate instance type and Availability Zone combination that Amazon EC2 uses when your preferred option isn't available).

Start with the request-level metrics to confirm that your requested capacity is being fulfilled. If it is, your flexibility is doing its job. Then use the per-combination metrics for optimization — to see where your capacity is landing and decide whether to reserve capacity or adjust your instance type choices.

**Topics**
+ [Fulfillment metrics](capacity-manager-fulfillment-metrics.md)
+ [Instance type and Availability Zone breakdown](capacity-manager-pool-breakdown.md)