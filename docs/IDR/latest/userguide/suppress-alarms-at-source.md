

# Suppress alarms at the alarm source
<a name="suppress-alarms-at-source"></a>

Specify which alarms engage with Incident Detection and Response and when they do so by suppressing alarms at the alarm source.

**Topics**
+ [Use a metric math function to suppress a CloudWatch alarm](#suppress-alarms-at-source-cw)
+ [Remove a metric math function to un-suppress a CloudWatch alarm](#suppress-alarms-metric-math-unsuppress)
+ [Example metric math functions and associated use cases](#suppress-alarms-example-functions)
+ [Suppress alarms from a third party APM](#suppress-alarms-third-party-apm)

## Use a metric math function to suppress a CloudWatch alarm
<a name="suppress-alarms-at-source-cw"></a>

To suppress Incident Detection and Response monitoring of Amazon CloudWatch alarms, use a [metric math function](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) to stop CloudWatch alarms from entering the `ALARM` state during a designated window.

**Note**  
Disabling **Alarm actions** on a CloudWatch alarm doesn’t suppress monitoring of your alarms by Incident Detection and Response. Alarm state changes are ingested through Amazon EventBridge, not through CloudWatch alarm actions.

To use a metric math function to suppress a CloudWatch alarm, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Alarms**, and then locate the alarm that you want to add the metric math function to.

1. Choose **Actions**, then select **Edit** to change the alarm.

1. Choose **Edit metric** to modify the metric for the alarm.

1. Choose **Add math**, **Start with empty expression**.

1. Enter your math expression, then choose **Apply**.

1. Deselect the existing metric that the alarm monitored.

1. Select the expression that you just created, and then choose **Select metric**.

1. Choose **Skip to Preview and create**.

1. Review your changes to make sure that your metric math function is applied as expected, and then choose **Update alarm**.

For a step by step example of suppressing a CloudWatch alarm with a metric math function, see [Tutorial: Use a metric math function to suppress an alarm](suppress-alarms-tutorial-suppress.md).

For more information on syntax and available functions, see [Metric math syntax and functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User Guide*. 

## Remove a metric math function to un-suppress a CloudWatch alarm
<a name="suppress-alarms-metric-math-unsuppress"></a>

Un-suppress a CloudWatch alarm by removing the metric math function. To remove a metric math function from an alarm, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Alarms**, and then locate the alarm or alarms that you want to remove the metric math expression from.

1. In the metric math section, choose **Edit**.

1. To remove the metric from the alarm, choose **Edit** on the metric, and then choose the **x** button next to the metric math expression.

1. Select the original metric, then choose **Select metric**.

1. Choose **Skip to Preview and create**. 

1. Review your changes to make sure that your metric math function is applied as expected, then choose **Update alarm**.

## Example metric math functions and associated use cases
<a name="suppress-alarms-example-functions"></a>

The following table contains metric math function examples, along with associated use cases and an explanation of each metric component.


| Metric math function | Use case | Explanation | 
| --- | --- | --- | 
| `IF((DAY(m1) == 2 && HOUR(m1) >= 1 && HOUR(m1) < 3), 0, m1)` | Suppress alarm between 1:00 to 3:00 AM UTC every Tuesday by replacing real data points with 0 during this window.  |  + **DAY(m1) == 2**: Ensures it's Tuesday (Monday = 1, Sunday = 7).<br />+ **HOUR(m1) >= 1 && HOUR(m1) < 3**: Specifies the time range from 1 AM to 3 AM UTC.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**:If the conditions are true, then replace the metric value with 0. Otherwise, return the original value (m1)  | 
| `IF((HOUR(m1) >= 23 \|\| HOUR(m1) < 4), 0, m1)` | Suppress alarm between 11:00 PM to 4:00 AM UTC, daily by replacing real data points with 0 during this window.  |  + **HOUR(m1) >= 23**: Captures the hours starting at 23:00 UTC.<br />+ **HOUR(m1) < 4**: Captures the hours up to (but not including) 04:00 UTC.<br />+ **\|\|**: Logical OR ensures the condition applies across two ranges—late-night hours and early-morning hours.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**: Returns 0 during the specified time range. Retains the original metric value m1 outside that range.  | 
| `IF((HOUR(m1) >= 11 && HOUR(m1) < 13), 0, m1) ` | Suppress alarm between 11:00 AM to 1:00 PM UTC daily by replacing real data points with 0 during this window. |  + **HOUR(m1) >= 11 && HOUR(m1) < 13**: Captures the time range from 11:00 to 13:00 UTC.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**: If the condition is true (for example, the time is between 11:00 and 13:00 UTC), return 0, If the condition is false, retain the original metric value (m1).  | 
| `IF((DAY(m1) == 2 && HOUR(m1) >= 1 && HOUR(m1) < 3), 99, m1)` | Suppress alarm between 1:00 to 3:00 AM UTC every Tuesday by replacing real data points with 99 during this window. |  + **DAY(m1) == 2:**: Ensures it's Tuesday (Monday = 1, Sunday = 7).<br />+ **HOUR(m1) >= 1 && HOUR(m1) < 3**: Specifies the time range from 1 AM to 3 AM UTC.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**: If the conditions are true, replace the metric value with 99. Otherwise, return the original value (m1).  | 
| `IF((HOUR(m1) >= 23 \|\| HOUR(m1) < 4), 100, m1)` | Suppress alarm between 11:00 PM to 4:00 AM UTC, daily by replacing real data points with 100 during this window.  |  + **HOUR(m1) >= 23**: Captures the hours starting at 23:00 UTC.<br />+ **HOUR(m1) < 4**: Captures the hours up to (but not including) 04:00 UTC.<br />+ **\|\|**: Logical OR ensures the condition applies across two ranges—late-night hours and early-morning hours.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**: Returns 100 during the specified time range. Retains the original metric value m1 outside that range.  | 
| `IF((HOUR(m1) >= 11 && HOUR(m1) < 13), 99, m1) ` | Suppress alarm between 11:00 AM to 1:00 PM UTC daily by replacing real data points with 99 during this window.  |  + **HOUR(m1) >= 11 && HOUR(m1) < 13**: Captures the time range from 11:00 to 13:00 UTC.<br />+ **IF(condition, value\_if\_true, value\_if\_false)**: If the condition is true (for example, the time is between 11:00 and 13:00 UTC), return 99. If the condition is false, retain the original metric value (m1).  | 

## Suppress alarms from a third party APM
<a name="suppress-alarms-third-party-apm"></a>

Refer to your third party APM vendor’s documentation for instructions on how to suppress alarms. Examples of third party APM vendors are New Relic, Splunk, Dynatrace, Datadog, and SumoLogic.