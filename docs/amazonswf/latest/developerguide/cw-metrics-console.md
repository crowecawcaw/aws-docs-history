# Viewing Amazon SWF Metrics for CloudWatch using the AWS Management Console

Amazon CloudWatch provides a number of viewable metrics for Amazon SWF workflows and activities. You can view the metrics and
set alarms for your Amazon SWF workflow executions using the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
_You must be logged in to the console to proceed_.

For a description of each of the available metrics, see [Amazon SWF Metrics for CloudWatch](cw-metrics.md "cw-metrics.md").

###### Topics

- [Viewing Metrics](#cw-metrics-console-viewing "#cw-metrics-console-viewing")
- [Setting Alarms](#cw-metrics-console-set-alarm "#cw-metrics-console-set-alarm")

## Viewing Metrics

###### To view your metrics for Amazon SWF

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, under **Metrics**, choose **SWF**.

![Dashboard interface showing Alarms, Billing, Metrics, and SWF options with Metric Summary.](images/cw_console.png)

If you have run any workflow executions recently, you will see two lists of metrics presented:
**Workflow Type Metrics** and **Activity Type Metrics**.

![Table showing Workflow Type Metrics and Activity Type Metrics with columns for names and versions.](images/cw_workflow_metrics.png)

###### Note

Initially you might only see the **Workflow Type Metrics**; **Activity Type
Metrics** are presented in the same view, but you may need to scroll down to see them.

Up to 50 of the most recent metrics will be shown at a time, divided among workflow and activity
metrics.

You can use the interactive headings above each column in the list to sort your metrics using any of the
provided dimensions. For workflows, the dimensions are **Domain**, **WorkflowTypeName**, **WorkflowTypeVersion**, and **Metric Name**. For activities, the dimensions are **Domain**, **ActivityTypeName**, **ActivityTypeVersion**, and **Metric Name**.

The various types of metrics are described in [Amazon SWF Metrics for CloudWatch](cw-metrics.md "cw-metrics.md").

You can view graphs for metrics by choosing the boxes next to the metric row in the list, and change the graph
parameters using the **Time Range** controls to the right of the graph view.

![Workflow metrics dashboard showing failed workflows for Cron and FileProcessing domains.](images/cw_graph.png)

For details about any point on the graph, place your cursor over the graph point. A detail of the point's
dimensions will be shown.

![Workflow details showing value, time, metric, and other parameters for a completed task.](images/cw_graph_detail.png)

For more information about working with CloudWatch metrics, see [Viewing,
Graphing, and Publishing Metrics](../../../AmazonCloudWatch/latest/DeveloperGuide/working_with_metrics.md "../../../AmazonCloudWatch/latest/DeveloperGuide/working_with_metrics.md") in the _Amazon CloudWatch User Guide_.

## Setting Alarms

You can use CloudWatch alarms to perform actions such as notifying you when an alarm threshold is reached. For
example, you can set an alarm to send a notification to an SNS topic or to send an email when the `WorkflowsFailed` metric rises above a certain threshold.

###### To set an alarm on any of your metrics

1. Choose a single metric by choosing its box.
2. To the right of the graph, in the **Tools** controls, choose **Create
   Alarm**.
3. On the **Define Alarm** screen, enter the alarm threshold value, period parameters, and
   actions to take.

![Alarm Threshold configuration interface with fields for name, description, conditions, and notification actions.](images/cw_define_alarm.png)

For more information about setting and using CloudWatch alarms, see [Creating Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/DeveloperGuide/AlarmThatSendsEmail.md") in the
_Amazon CloudWatch User Guide_.
