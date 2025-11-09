AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Monitoring your automations

_Metrics_ are the fundamental concept in Amazon CloudWatch. A
metric represents a time-ordered set of data points that are published to CloudWatch. Think of
a metric as a variable to monitor and the data points as representing the values of that
variable over time.

Automation is a tool in AWS Systems Manager. Systems Manager publishes metrics about Automation usage to
CloudWatch. This allows you to set alarms based on those metrics.

###### To view Automation metrics in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. Choose **SSM**.
4. On the **Metrics** tab, choose **Usage**,
   and then choose **By AWS Resource**.
5. In the search box near the list of metrics, enter
   **SSM**.

###### To view Automation metrics using the AWS CLI

Open a command prompt, and use the following command.

```
aws cloudwatch list-metrics \
    --namespace "AWS/Usage"
```

## Automation metrics

Systems Manager sends the following Automation metrics to CloudWatch.

| Metric                      | Description                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------- |
| `ConcurrentAutomationUsage` | The number of automations running at the same time in the current<br>AWS account and AWS Region.    |
| `QueuedAutomationUsage`     | The number of automations currently queued that have not started<br>and have a status of `Pending`. |

For more information about working with CloudWatch metrics, see the following topics in
the _Amazon CloudWatch User Guide_:

- [Metrics](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Metric")
- [Using
  Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Using
  Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
