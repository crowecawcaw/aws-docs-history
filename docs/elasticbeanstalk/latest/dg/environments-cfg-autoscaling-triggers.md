# Amazon EC2 Auto Scaling triggers for your Elastic Beanstalk environment

The Amazon EC2 Auto Scaling group in your Elastic Beanstalk environment uses two Amazon CloudWatch alarms to trigger scaling operations. The default triggers scale when the average outbound
network traffic from each instance is higher than 6 MB or lower than 2 MB over a period of five minutes. To use Amazon EC2 Auto Scaling effectively, configure triggers
that are appropriate for your application, instance type, and service requirements. You can scale based on several statistics including latency, disk I/O,
CPU utilization, and request count.

For more information about CloudWatch metrics and alarms, see [Amazon CloudWatch Concepts](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md") in the
_Amazon CloudWatch User Guide_.

## Configuring Amazon EC2 Auto Scaling triggers

You can configure the triggers that adjust the number of instances in your environment's Amazon EC2 Auto Scaling group in the Elastic Beanstalk console.

###### To configure triggers in the Elastic Beanstalk console

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Capacity** configuration category, choose **Edit**.
5. In the **Scaling triggers** section, configure the following settings:
   - **Metric** – Metric used for your Amazon EC2 Auto Scaling trigger.
   - **Statistic** – Statistic calculation the trigger should use, such as `Average`.
   - **Unit** – Unit for the trigger metric, such as **Bytes**.
   - **Period** – Specifies how frequently Amazon CloudWatch measures the metrics for your trigger.
   - **Breach duration** – Amount of time, in minutes, a metric can be outside of the upper and lower thresholds before
     triggering a scaling operation.
   - **Upper threshold** – If the metric exceeds this number for the breach duration, a scaling operation is triggered.
   - **Scale up increment** – The number of Amazon EC2 instances to add when performing a scaling activity.
   - **Lower threshold** – If the metric falls below this number for the breach duration, a scaling operation is triggered.
   - **Scale down increment** – The number of Amazon EC2 instances to remove when performing a scaling activity.

6. To save the changes choose **Apply** at the bottom of the page.

## The aws:autoscaling:trigger namespace

Elastic Beanstalk provides [configuration options](command-options.md "command-options.md") for Amazon EC2 Auto Scaling settings in the [aws:autoscaling:trigger](command-options-general.md#command-options-general-autoscalingtrigger "command-options-general.md#command-options-general-autoscalingtrigger") namespace. Settings in this namespace are organized by
the resource that they apply to.

```
option_settings:
  AWSEBAutoScalingScaleDownPolicy.aws:autoscaling:trigger:
    LowerBreachScaleIncrement: '-1'
  AWSEBAutoScalingScaleUpPolicy.aws:autoscaling:trigger:
    UpperBreachScaleIncrement: '1'
  AWSEBCloudwatchAlarmHigh.aws:autoscaling:trigger:
    UpperThreshold: '6000000'
  AWSEBCloudwatchAlarmLow.aws:autoscaling:trigger:
    BreachDuration: '5'
    EvaluationPeriods: '1'
    LowerThreshold: '2000000'
    MeasureName: NetworkOut
    Period: '5'
    Statistic: Average
    Unit: Bytes
```
