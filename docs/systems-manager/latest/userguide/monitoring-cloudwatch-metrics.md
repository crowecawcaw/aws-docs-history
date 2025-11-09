AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Monitoring Run Command metrics using

Amazon CloudWatch

_Metrics_ are the fundamental concept in Amazon CloudWatch. A
metric represents a time-ordered set of data points that are published to CloudWatch. Think of
a metric as a variable to monitor, and the data points as representing the values of
that variable over time.

AWS Systems Manager publishes metrics about the status of Run Command commands to CloudWatch, allowing
you to set alarms based on those metrics. Run Command is a tool in AWS Systems Manager. These
statistics are recorded for an extended period so you can access historical information
and gain a better perspective on the success rate of commands run in your AWS account.

The terminal status values for commands for which you can track metrics include
`Success`, `Failed`, and `Delivery Timed Out`. For
example, for an SSM Command document set to run every hour, you can configure an alarm
to notify you when a status of `Success` isn't reported for any of those
hours. For more information about command status values, see [Understanding command statuses](monitor-commands.md "monitor-commands.md").

###### To view metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. In the **Alarms by AWS service** area, for
   **Services**, choose
   **SSM-Run Command**.

###### To view metrics using the AWS CLI

Open a command prompt, and use the following command.

```
aws cloudwatch list-metrics --namespace "AWS/SSM-RunCommand"
```

To list all available metrics, use the following command.

```
aws cloudwatch list-metrics
```

## Systems Manager Run Command metrics and

dimensions

Systems Manager sends Run Command command metrics to CloudWatch one time every minute.

Systems Manager sends the following command metrics to CloudWatch.

###### Note

These metrics use `Count` as the unit, so `Sum` and
`SampleCount` are the most useful statistics.

| Metric                     | Description                                                                    |
| -------------------------- | ------------------------------------------------------------------------------ |
| `CommandsDeliveryTimedOut` | The number of commands that have a terminal status of<br>`Delivery Timed Out`. |
| `CommandsFailed`           | The number of commands that have a terminal status of<br>`Failed`.             |
| `CommandsSucceeded`        | The number of commands that have a terminal status of<br>`Success`.            |

For more information about working with CloudWatch metrics, see the following topics in
the _Amazon CloudWatch User Guide_:

- [Metrics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric")
- [Using
  Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Using
  Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
