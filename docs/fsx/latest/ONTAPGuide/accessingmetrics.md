

# Accessing CloudWatch metrics
<a name="accessingmetrics"></a>

You can see Amazon CloudWatch metrics for Amazon FSx in the following ways:
+ The Amazon FSx console
+ The Amazon CloudWatch console
+ The AWS Command Line Interface (AWS CLI) for CloudWatch
+ The CloudWatch API

The following procedure explains how to view your file system's CloudWatch metrics with the Amazon FSx console. 

**To view CloudWatch metrics for your file system using the Amazon FSx console**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **File systems**, then choose the file system whose metrics you want to view.

1. On the **Summary** page, choose **Monitoring & performance** from the second panel to view graphs for your file system's metrics. 

There are four tabs on the **Monitoring & performance** panel. 
+ Choose **Summary** (the default tab) to display any active warnings, CloudWatch alarms, and graphs for **File system activity**. 
+ Choose **Storage** to view storage capacity and utilization metrics. 
+ Choose **Performance** to view file server and storage performance metrics. 
+ Choose **CloudWatch alarms** to view graphs of any alarms configured for your file system. 

The following procedure explains how to view your volume's CloudWatch metrics with the Amazon FSx console

**To view CloudWatch metrics for your volume using the Amazon FSx console**

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. In the left navigation pane, choose **Volumes**, then choose the volume whose metrics you want to view.

1. On the **Summary** page, choose **Monitoring** (the default tab) from the second panel to view graphs for your volume's metrics. 

The following procedure explains how to view your file system's CloudWatch metrics with the Amazon CloudWatch console. 

**To view metrics using the Amazon CloudWatch console**

1. On the **Summary** page of your file system, choose **Monitoring & performance** from the second panel to view graphs for your file system's metrics. 

1. Choose **View in metrics** from the actions menu in the upper right of the graph that you want to view in the Amazon CloudWatch console. This opens the **Metrics** page in the Amazon CloudWatch console. 

The following procedure explains how to add FSx for ONTAP file system metrics to a dashboard in the Amazon CloudWatch console. 

**To add metrics to a Amazon CloudWatch console**

1. Choose the set of metrics (**Summary**, **Storage**, or **Performance**) in the **Monitoring & performance** panel of the Amazon FSx console. 

1. Choose **Add to dashboard** in the upper right hand of the panel. This opens the Amazon CloudWatch console. 

1. Select an existing CloudWatch dashboard from the list, or create a new dashboard. For more information, see [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) in the *Amazon CloudWatch User Guide*. 

The following procedure explains how to access your file system's metrics with the AWS CLI. 

**To access metrics from the AWS CLI**
+ Use the CloudWatch [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) CLI command with the `--namespace "AWS/FSx"` parameter. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

The following procedure explains how to access your file system's metrics with the CloudWatch API. 

**To access metrics from the CloudWatch API**
+ Call the [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) API operation. For more information, see the [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/). 