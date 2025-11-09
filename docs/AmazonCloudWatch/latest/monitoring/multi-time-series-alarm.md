# Create a fleet monitoring alarm using multiple

time series

You can create an alarm that monitors multiple time series across a fleet of resources.
Unlike single-instance alarms that trigger actions on individual instances, fleet monitoring
alarms let you aggregate metrics across multiple resources and trigger based on fleet-wide
conditions.

## Setting up a fleet monitoring alarm

using the AWS Management Console

This example shows how to create an alarm that monitors memory utilization across a
fleet of instances and alerts you when more than two instances exceed a threshold.

###### To create a fleet monitoring alarm

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
   Alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Under **Metrics**, enter a Metrics Insights query:

```
SELECT MAX(mem_used_percent)
FROM "CWAgent"
GROUP BY InstanceId
ORDER BY MAX() DESC
```

6. Choose **Next**.
7. Under **Conditions**, specify the following:
   - For **Threshold type**, choose
     **Static**.
   - For **When metric is**, choose **Greater
     than** and enter `80`.
   - For **Datapoints to alarm**, enter
     `2`.

8. Configure notifications and actions as needed.
9. Add a name and description for your alarm.
10. Choose **Create alarm**.

This alarm differs from single-instance alarms in several ways:

- It monitors multiple time series simultaneously through the use of a metrics query.
  The metrics query is refreshed every time the alarm evaluates, thus your alarm
  automatically adapts as resources are created, paused, or deleted.
- For each contributor that breaches the threshold, the alarm sends a contributor
  state change event, which has a different event type in EventBridge than an alarm state change
  event. The alarm itself also changes state: as soon as at least one contributor is in
  alarm, the alarm also enters the alarm state.
- Some actions however, such as SSM Incident, are triggered at the alarm level. Such
  actions are not repeated when the list of contributors in alarm changes.
  This alarm differs from aggregated metric-query alarms in several ways:

- It monitors time series individually instead of an aggregate, using the `GROUP
BY` clause.
- It follows the level of granularity that you set according to your needs: for
  example, it can alarm on every Amazon EC2 instance (most granular level of Amazon EC2 metrics) or
  per Amazon RDS table (aggregated across various operations on a table), depending on which
  fields you set in the `GROUP BY` clause
- It prioritizes evaluation using the `ORDER BY` clause.
- For each contributor that breaches the threshold, the alarm sends a contributor
  state change event, which has a different event type in EventBridge than an alarm state change
  event. The alarm itself also changes state: as soon as at least one contributor is in
  alarm, the alarm also enters the alarm state.
- Some actions however, such as SSM Incident, are triggered at the alarm level. Such
  actions are not repeated when the list of contributors in alarm changes.
