# Amazon SWF Metrics for CloudWatch

Amazon SWF now provides metrics for CloudWatch that you can use to track your workflows and activities
and set alarms on threshold values that you choose. You can view metrics using the AWS Management Console.
For more information, see [Viewing Amazon SWF Metrics for CloudWatch using the AWS Management Console](cw-metrics-console.md "cw-metrics-console.md").

###### Topics

- [Reporting Units for Amazon SWF Metrics](#swf-reporting-units "#swf-reporting-units")
- [API and Decision Event Metrics](#swf-throttling-metrics "#swf-throttling-metrics")
- [Amazon SWF Metrics](#cloudwatch-swf-metrics "#cloudwatch-swf-metrics")
- [Amazon SWF non-ASCII resource names and CloudWatch
  dimensions](#cloudwatch-swf-non-ascii "#cloudwatch-swf-non-ascii")

## Reporting Units for Amazon SWF Metrics

### Metrics that Report a Time

Interval

Some of the Amazon SWF metrics for CloudWatch are _time intervals_, always measured in
milliseconds. The CloudWatch unit is reported as `Time`. These metrics generally
correspond to stages of your workflow execution for which you can set workflow and activity
timeouts, and have similar names.

For example, the `DecisionTaskStartToCloseTime` metric measures the time it
took for the decision task to complete after it began executing, which is the same time
period for which you can set a `DecisionTaskStartToCloseTimeout` value.

For a diagram of each of these workflow stages and to learn when they occur over the
workflow and activity lifecycles, see [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md") .

### Metrics that Report a Count

Some of the Amazon SWF metrics for CloudWatch report results as a _count_. For
example, `WorkflowsCanceled`, records a result as either _one_
or _zero_, indicating whether or not the workflow was canceled. A value
of zero doesn't indicate that the metric was not reported, only that the condition described
by the metric did not occur.

Some of the Amazon SWF metrics for CloudWatch that report a `Count` in CloudWatch are a
_count per second_. For instance, `ProvisionedRefillRate`,
which is reported as a `Count` in CloudWatch, represents a _rate_ of
the `Count` of requests per second.

For count metrics, minimum and maximum will always be either zero or one, but average
will be a value ranging from zero to one.

## API and Decision Event Metrics

You can monitor both API and Decision events in CloudWatch to provide insight into your usage
and capacity. See [deciders](swf-dev-actors.md#swf-dev-actors-deciders "swf-dev-actors.md#swf-dev-actors-deciders") in the [Basic workflow concepts in Amazon SWF](swf-dg-basic.md "swf-dg-basic.md") section, and the [Decision](../apireference/API_Decision.md "../apireference/API_Decision.md") topic in the [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md").

You can also monitor these limits to alarm when you are approaching your Amazon SWF throttling
limits. See [Amazon SWF throttling quotas](swf-dg-limits.md#swf-throttling-limits "swf-dg-limits.md#swf-throttling-limits") for
a description of these limits and their default settings. These limits are designed to prevent
incorrect workflows from consuming excessive system resources. To request an increase to your
limits see: [Requesting a quota increase](swf-dg-limits.md#swf-dg-limits-how-to-increase "swf-dg-limits.md#swf-dg-limits-how-to-increase").

As a best practice, you should configure CloudWatch alarms at around 60% of your API or decision
events capacity. This will allow you to either adjust your workflow, or request a service
limit increase, before Amazon SWF throttling is enabled. Depending on the [burstiness](https://en.wikipedia.org/wiki/Burstiness "https://en.wikipedia.org/wiki/Burstiness") of your calls, you can
configure different alarms to notify when you are approaching your service limits:

- If your traffic has significant spikes, set an alarm at 60% of your
  `ProvisionedBucketSize` limits.
- If your calls have a relatively steady rate, set an alarm at 60% of your
  `ProvisionedRefillRate` limit for your related API and decision events.

## Amazon SWF Metrics

The following metrics are available for Amazon SWF:

| Metric                                    | Description                                                                                                                                                                                                                                                                     |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------- |
| `DecisionTaskScheduleToStartTime`         | The time interval, in milliseconds, between the time that the decision task was scheduled and when it was picked up by a worker and started. CloudWatch Units: `Time` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Average, Minimum, Maximum` |
| `DecisionTaskStartToCloseTime`            | The time interval, in milliseconds, between the time that the decision task was started and when it closed. CloudWatch Units: `Time` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Average, Minimum, Maximum`                                  |
| `DecisionTasksCompleted`                  | The count of decision tasks that have been completed. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                             |
| `PendingTasks`                            | The count of pending tasks in a 1 minute interval for a specific Task List. CloudWatch Units: `Count` Dimensions: `Domain, TaskListName` Valid statistics: `Sum`                                                                                                                |
| `StartedDecisionTasksTimedOutOnClose`     | The count of decision tasks that started but timed out on closing. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                |
| `WorkflowStartToCloseTime`                | The time, in milliseconds, between the time the workflow started and when it closed. CloudWatch Units: `Time` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Average, Minimum, Maximum`                                                         |
| `WorkflowsCanceled`                       | The count of workflows that were canceled. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                                        |
| `WorkflowsCompleted`                      | The count of workflows that completed. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                                            |
| `WorkflowsContinuedAsNew`                 | The count of workflows that continued as new. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                                     |
| `WorkflowsFailed`                         | The count of workflows that failed. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                                               |
| `WorkflowsTerminated`                     | The count of workflows that were terminated. CloudWatch Units: `Count` Dimensions: `Cause, Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                               |
| `WorkflowsTimedOut`                       | The count of workflows that timed out, for any reason. CloudWatch Units: `Count` Dimensions: `Domain, WorkflowTypeName, WorkflowTypeVersion` Valid statistics: `Sum`                                                                                                            |
| `ActivityTaskScheduleToCloseTime`         | The time interval, in milliseconds, between the time when the activity was scheduled and when it closed. CloudWatch Units: `Time` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Average, Minimum, Maximum`                                     |
| `ActivityTaskScheduleToStartTime`         | The time interval, in milliseconds, between the time when the activity task was scheduled and when it started. CloudWatch Units: `Time` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Average, Minimum, Maximum`                               |
| `ActivityTaskStartToCloseTime`            | The time interval, in milliseconds, between the time when the activity task started and when it closed. CloudWatch Units: `Time` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Average, Minimum, Maximum`                                      |
| `ActivityTasksCanceled`                   | The count of activity tasks that were canceled. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                                                   |
| `ActivityTasksCompleted`                  | The count of activity tasks that completed. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                                                       |
| `ActivityTasksFailed`                     | The count of activity tasks that failed. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                                                          |
| `ScheduledActivityTasksTimedOutOnClose`   | The count of activity tasks that were scheduled but timed out on close. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                           |
| `ScheduledActivityTasksTimedOutOnStart`   | The count of activity tasks that were scheduled but timed out on start. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                           |
| `StartedActivityTasksTimedOutOnClose`     | The count of activity tasks that were started but timed out on close. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                                             |
| `StartedActivityTasksTimedOutOnHeartbeat` | The count of activity tasks that were started but timed out due to a heartbeat timeout. CloudWatch Units: `Count` Dimensions: `Domain, ActivityTypeName, ActivityTypeVersion` Valid statistics: `Sum`                                                                           |
| `ThrottledEvents`                         | The count of requests that have been throttled. CloudWatch Units: `Count` Dimensions: `APIName, DecisionName, ThrottlingScope` Valid statistics: `Sum`                                                                                                                          |
| `ProvisionedBucketSize`                   | The count of available requests per second. Dimensions: `APIName, DecisionName` Valid statistics: `Minimum`                                                                                                                                                                     |
| `ConsumedCapacity`                        | The count of requests per second. CloudWatch Units: `Count` Dimensions: `APIName, DecisionName` Valid statistics: `Sum`                                                                                                                                                         |
| `ConsumedLimit`                           | The amount of general limit that has been consumed. Dimensions: `GeneralLimitType`                                                                                                                                                                                              |
| `ProvisionedRefillRate`                   | The count of requests per second that are allowed into the bucket. Dimensions: `APIName, DecisionName` Valid statistics: `Minimum`                                                                                                                                              |
| `ProvisionedLimit`                        | The amount of general limit that is provisioned to the account. Dimensions: `GeneralLimitType`                                                                                                                                                                                  |
| Dimension                                 | Description                                                                                                                                                                                                                                                                     |
| ---                                       | ---                                                                                                                                                                                                                                                                             |
| `Domain`                                  | Filters data to the Amazon SWF domain that the workflow or activity is running in.                                                                                                                                                                                              |
| `ActivityTypeName`                        | Filters data to the name of the activity type.                                                                                                                                                                                                                                  |
| `ActivityTypeVersion`                     | Filters data to the version of the activity type.                                                                                                                                                                                                                               |
| `WorkflowTypeName`                        | Filters data to the name of the workflow type for this workflow execution.                                                                                                                                                                                                      |
| `WorkflowTypeVersion`                     | Filters data to the version of the workflow type for this workflow execution.                                                                                                                                                                                                   |
| `APIName`                                 | Filters data to an API of the specified API name.                                                                                                                                                                                                                               |
| `DecisionName`                            | Filters data to the specified Decision name.                                                                                                                                                                                                                                    |
| `TaskListName`                            | Filters data to the specified Task List name.                                                                                                                                                                                                                                   |
| `TaskListClassification`                  | Filters data to the classification of the task list. Value is "D" for Decision Task Lists and "A" for Activity Task Lists.                                                                                                                                                      |
| `ThrottlingScope`                         | Filters data to the specified throttling scope. Value is "Account" when exceeding account-level quota, or "Workflow" when exceeding workflow-level quota.                                                                                                                       | ## Amazon SWF non-ASCII resource names and CloudWatch dimensions Amazon SWF allows non-ASCII characters in resource names such as TaskList and DomainName. However, the dimension values of CloudWatch metrics can only contain printable ASCII characters. To ensure that Amazon SWF uses dimension values that are compatible with [CloudWatch requirements](../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md "../../../AmazonCloudWatch/latest/APIReference/API_Dimension.md"), Amazon SWF resource names that do not meet these requirements are converted and will have a checksum appended as follows: <br>• Any non-ASCII character is replaced with `?`. <br>• The input string or converted string will, if necessary, be truncated. This ensures that when the checksum is appended, the new string length will not exceed the CloudWatch maximum. <br>• Because any non-ASCII characters are converted to `?`, some CloudWatch metric dimension values that were different before conversion may appear to be the same after conversion. To help differentiate between them, an underscore (`_`) followed by the first 16 characters of the SHA256 checksum of the original resource name is appended to the resource name. Conversion examples: <br>• `test àpple` would be converted to `test ?pple_82cc5b8e3a771d12` <br>• `àòà` would be converted to `???_2fec5edbb2c05c22`. <br>• The TaskList names `àpplé` and `âpplè` would both be converted to `?ppl?`, and would be identical. Appending the checksum returns distinct values, `?ppl?_f39a36df9d85a69d` and `?ppl?_da3efb4f11dd0f7f`. ###### Tip You can generate your own SHA256 checksum. For example, to use the `shasum` command line tool: \*\*echo -n "<the original resource name>" | shasum -a 256 | cut -c1-16\*\* |
