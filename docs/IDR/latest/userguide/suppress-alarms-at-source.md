# Suppress alarms at the alarm source

Specify which alarms engage with Incident Detection and Response and when they do so by suppressing alarms at the alarm source.

###### Topics

- [Use a metric math function to suppress a CloudWatch alarm](#suppress-alarms-at-source-cw "#suppress-alarms-at-source-cw")
- [Remove a metric math function to un-suppress a CloudWatch alarm](#suppress-alarms-metric-math-unsuppress "#suppress-alarms-metric-math-unsuppress")
- [Example metric math functions and associated use cases](#suppress-alarms-example-functions "#suppress-alarms-example-functions")
- [Suppress alarms from a third party APM](#suppress-alarms-third-party-apm "#suppress-alarms-third-party-apm")

## Use a metric math function to suppress a CloudWatch alarm

To suppress Incident Detection and Response monitoring of Amazon CloudWatch alarms, use a [metric math function](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md") to stop CloudWatch alarms from entering the `ALARM` state during a designated window.

###### Note

Disabling **Alarm actions** on a CloudWatch alarm doesn’t suppress monitoring of your alarms by Incident Detection and Response. Alarm state changes are ingested through Amazon EventBridge, not through CloudWatch alarm actions.

To use a metric math function to suppress a CloudWatch alarm, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Alarms**, and then locate the alarm that you want to add the metric math function to.
3. In the metric math section, choose **Edit**.
4. Choose **Add math**, **Start with empty expression**.
5. Enter your math expression, then choose **Apply**.
6. Deselect the existing metric that the alarm monitored.
7. Select the expression that you just created, and then choose **Select metric**.
8. Choose **Skip to Preview and create**.
9. Review your changes to make sure that your metric math function is applied as expected, and then choose **Update alarm**.

For a step by step example of suppressing a CloudWatch alarm with a metric math function, see [Tutorial: Use a metric math function to suppress an alarm](suppress-alarms-tutorial-suppress.md "suppress-alarms-tutorial-suppress.md").

For more information on syntax and available functions, see [Metric math syntax and functions](../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#metric-math-syntax "../../../AmazonCloudWatch/latest/monitoring/using-metric-math.md#metric-math-syntax") in the _Amazon CloudWatch User Guide_.

## Remove a metric math function to un-suppress a CloudWatch alarm

Un-suppress a CloudWatch alarm by removing the metric math function. To remove a metric math function from an alarm, complete the following steps:

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Alarms**, and then locate the alarm or alarms that you want to remove the metric math expression from.
3. In the metric math section, choose **Edit**.
4. To remove the metric from the alarm, choose **Edit** on the metric, and then choose the **x** button next to the metric math expression.
5. Select the original metric, then choose **Select metric**.
6. Choose **Skip to Preview and create**.
7. Review your changes to make sure that your metric math function is applied as expected, then choose **Update alarm**.

## Example metric math functions and associated use cases

The following table contains metric math function examples, along with associated use cases and an explanation of each metric component.

| Metric math function                                          | Use case                                                                                                           | Explanation                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IF((DAY(m1) == 2 && HOUR(m1) >= 1 && HOUR(m1) < 3), 0, m1)`  | Suppress alarm between 1:00 to 3:00 AM UTC every Tuesday by replacing real data points with 0 during this window.  | <br>• **DAY(m1) == 2**: Ensures it's Tuesday (Monday = 1, Sunday = 7). <br>• **HOUR(m1) >= 1 && HOUR(m1) > 3**: Specifies the time range from 1 AM to 3 AM UTC. <br>• **IF(condition, value_if_true, value_if_false)**:If the conditions are true, then replace the metric value with 0. Otherwise, return the original value (m1) |
| `IF((HOUR(m1) >= 23                                           |                                                                                                                    | HOUR(m1) < 4), 0, m1)`                                                                                                                                                                                                                                                                                                             | Suppress alarm between 11:00 PM to 4:00 AM UTC, daily by replacing real data points with 0 during this window.                                                                                                                                                                                                    | <br>• **HOUR(m1) >= 23**: Captures the hours starting at 23:00 UTC. <br>• **HOUR(m1) < 4**: Captures the hours up to (but not including) 04:00 UTC. <br>• \*\*                                                                           |     | **: Logical OR ensures the condition applies across two ranges—late-night hours and early-morning hours. <br>• **IF(condition, value_if_true, value_if_false)\*\*: Returns 0 during the specified time range. Retains the original metric value m1 outside that range.   |
|                                                               | `IF((HOUR(m1) >= 11 && HOUR(m1) < 13), 0, m1)`                                                                     | Suppress alarm between 11:00 AM to 1:00 PM UTC daily by replacing real data points with 0 during this window.                                                                                                                                                                                                                      | <br>• **HOUR(m1) >= 11 && HOUR(m1) < 13**: Captures the time range from 11:00 to 13:00 UTC. <br>• **IF(condition, value_if_true, value_if_false)**: If the condition is true (for example, the time is between 11:00 and 13:00 UTC), return 0, If the condition is false, retain the original metric value (m1).  |
| `IF((DAY(m1) == 2 && HOUR(m1) >= 1 && HOUR(m1) < 3), 99, m1)` | Suppress alarm between 1:00 to 3:00 AM UTC every Tuesday by replacing real data points with 99 during this window. | <br>• **DAY(m1) == 2:**: Ensures it's Tuesday (Monday = 1, Sunday = 7). <br>• **HOUR(m1) >= 1 && HOUR(m1) < 3**: Specifies the time range from 1 AM to 3 AM UTC. <br>• **IF(condition, value_if_true, value_if_false)**: If the conditions are true, replace the metric value with 99. Otherwise, return the original value (m1).  |
| `IF((HOUR(m1) >= 23                                           |                                                                                                                    | HOUR(m1) < 4), 100, m1)`                                                                                                                                                                                                                                                                                                           | Suppress alarm between 11:00 PM to 4:00 AM UTC, daily by replacing real data points with 100 during this window.                                                                                                                                                                                                  | <br>• **HOUR(m1) >= 23**: Captures the hours starting at 23:00 UTC. <br>• **HOUR(m1) < 4**: Captures the hours up to (but not including) 04:00 UTC. <br>• \*\*                                                                           |     | **: Logical OR ensures the condition applies across two ranges—late-night hours and early-morning hours. <br>• **IF(condition, value_if_true, value_if_false)\*\*: Returns 100 during the specified time range. Retains the original metric value m1 outside that range. |
|                                                               | `IF((HOUR(m1) >= 11 && HOUR(m1) < 13), 99, m1)`                                                                    | Suppress alarm between 11:00 AM to 1:00 PM UTC daily by replacing real data points with 99 during this window.                                                                                                                                                                                                                     | <br>• **HOUR(m1) >= 11 && HOUR(m1) < 13**: Captures the time range from 11:00 to 13:00 UTC. <br>• **IF(condition, value_if_true, value_if_false)**: If the condition is true (for example, the time is between 11:00 and 13:00 UTC), return 99. If the condition is false, retain the original metric value (m1). | ## Suppress alarms from a third party APM Refer to your third party APM vendor’s documentation for instructions on how to suppress alarms. Examples of third party APM vendors are New Relic, Splunk, Dynatrace, Datadog, and SumoLogic. |
