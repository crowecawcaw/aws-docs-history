

# Monitoring Amazon EventBridge Scheduler with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

 You can monitor Amazon EventBridge Scheduler using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. EventBridge Scheduler emits a set of metrics for all schedules, and an additional set of metrics for schedules that have an associated dead-letter queue (DLQ). If you [configure a DLQ](configuring-schedule-dlq.md) for your schedule, EventBridge Scheduler publishes additional metrics when your schedule exhausts its retry policy. 

 These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on why a schedule is failing, and troubleshoot underlying issues. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). 

**Best-effort CloudWatch metrics delivery**  
CloudWatch metrics are delivered on a best-effort basis. Most EventBridge Scheduler operations result in a data point being sent to CloudWatch. The completeness and timeliness of metrics are not guaranteed. A data point for a given minute might be delayed before being available through CloudWatch, or it might not be delivered at all. CloudWatch metrics give you an idea of the nature of activity in near-real time. They are not meant to be a complete accounting of all operations.

**Topics**
+ [Terms](#monitoring-cloudwatch-terms)
+ [Dimensions](#monitoring-cloudwatch-dimensions)
+ [Accessing metrics](#monitoring-cloudwatch-view-metrics)
+ [List of metrics](#monitoring-cloudwatch-metrics-list)
+ [EventBridge Scheduler usage metrics](monitoring-cloudwatch-usage-metrics.md)

## Terms
<a name="monitoring-cloudwatch-terms"></a>

**Namespace**  
A namespace is a container for the CloudWatch metrics of an AWS service. For EventBridge Scheduler, the namespace is `AWS/Scheduler`.

**CloudWatch metrics**  
A CloudWatch metric represents a time-ordered set of data points that are specific to CloudWatch. 

**Dimension**  
A dimension is a name/value pair that is part of the identity of a metric. 

**Unit**  
 A statistic has a unit of measure. For EventBridge Scheduler, units include *Count*. 

## Dimensions
<a name="monitoring-cloudwatch-dimensions"></a>

This section describes the CloudWatch dimensions grouping for EventBridge Scheduler metrics in CloudWatch.


| Dimension | Description | 
| --- | --- | 
| ScheduleGroup | The group of schedules for which you want to view metrics using CloudWatch. If you have not created any groups yet, EventBridge Scheduler associates your schedules with the `default` group. | 

## Accessing metrics
<a name="monitoring-cloudwatch-view-metrics"></a>

This section describes how to access performance metrics in CloudWatch for a specific EventBridge Scheduler schedule.

**To view performance metrics for a dimension**

1. Open the [Metrics page](https://console.aws.amazon.com/cloudwatch/home#metricsV2:graph=~()) on the CloudWatch console.

1.  Use the AWS Region selector to choose the Region for your schedule 

1. Choose the **Scheduler** namespace.

1. In the **All metrics** tab, choose a dimension, for example, **Schedule Group Metrics**. To see metrics for all the schedules you've created in your selected Region, choose **Account Metrics**.

1. Choose a CloudWatch metric for a dimension. For example, **InvocationAttemptCount** or **InvocationDroppedCount**, then choose **Graph search**.

1. Choose the **Graphed metrics** tab to view performance statistics for EventBridge Scheduler metrics.

## List of metrics
<a name="monitoring-cloudwatch-metrics-list"></a>

The following tables list the metrics for all EventBridge Scheduler schedules, as well as additional metrics for schedules for which you've configured a DLQ.

### Metrics for all schedules
<a name="monitoring-cloudwatch-metrics-list-schedules"></a>


| Namespace | Metric | Unit | Description | 
| --- | --- | --- | --- | 
| `AWS/Scheduler` | `InvocationAttemptCount` | Count | Emitted for every invocation attempt. Use this metric to check that EventBridge Scheduler is attempting to invoke your schedules, and to see when invocations approach your account quotas. | 
| `AWS/Scheduler` | `TargetErrorCount` | Count | Emitted when the target returns an exception after EventBridge Scheduler calls the target API. Use this to check when delivery to a target fails. | 
| `AWS/Scheduler` | `TargetErrorThrottledCount` | Count | Emitted when target invocation fails due to API throttling by the target. Use this to diagnose delivery failures when the underlying reason is the target API throttling calls made by EventBridge Scheduler | 
| `AWS/Scheduler` | `InvocationThrottleCount` | Count | Emitted when EventBridge Scheduler throttles a target invocation because it exceeds your service quotas set by EventBridge Scheduler. Use this to determine when you have exceeded your invocations throttle limit quota. For more information about service quotas, see [Quotas for Amazon EventBridge Scheduler](scheduler-quotas.md). | 
| `AWS/Scheduler` | `InvocationDroppedCount` | Count | Emitted when EventBridge Scheduler stops attempting to invoke the target after a schedule's retry policy has been exhausted. For more information about retry policies, see [RetryPolicy](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_RetryPolicy.html) in the *EventBridge Scheduler API Reference*. | 

### Metrics for schedules with a DLQ
<a name="monitoring-cloudwatch-metrics-list-dlq"></a>


<table>
<thead>
  <tr><th>Namespace</th><th>Metric</th><th>Unit</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>AWS/Scheduler</code></td><td><code>InvocationsSentToDeadLetterCount</code></td><td>Count</td><td>Emitted for every successful delivery to a schedule's DLQ. Use this to determine when events are sent to a DLQ, then check the event delivered to the schedule's DLQ for additional details that help you determine the cause of the failure.</td></tr>
  <tr><td><code>AWS/Scheduler</code></td><td><code>InvocationsFailedToBeSentToDeadLetterCount</code></td><td>Count</td><td rowspan="2">Emitted when EventBridge Scheduler cannot deliver an event to the DLQ. Use these two metrics to determine the reason why EventBridge Scheduler is unable to send an event to the DLQ, and modify your DLQ configuration to resolve the issue.<br />The following is an example of the <code>InvocationsFailedToBeSentToDeadLetterCount_&lt;error_code&gt;</code> metric when the Amazon SQS queue you specify as a DLQ does not exist: <code>InvocationsFailedToBeSentToDeadLetterCount_AWS.SimpleQueueService.NonExistentQueue</code> </td></tr>
  <tr><td><code>AWS/Scheduler</code></td><td><code>InvocationsFailedToBeSentToDeadLetterCount_&lt;error_code&gt;</code></td><td>Count</td></tr>
  <tr><td><code>AWS/Scheduler</code></td><td><code>InvocationsSentToDeadLetterCount_Truncated_MessageSizeExceeded</code></td><td>Count</td><td>Emitted when the payload of the event sent to the DLQ exceeds the maximum size allowed by Amazon SQS, and EventBridge Scheduler truncates the payload you specify in the <code>Input</code> attribute of a schedule.</td></tr>
</tbody>
</table>
