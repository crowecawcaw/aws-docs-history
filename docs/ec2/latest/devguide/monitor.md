

# Monitor Amazon EC2 API requests using Amazon CloudWatch
<a name="monitor"></a>

You can monitor Amazon EC2 API requests using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These metrics provide a simple way to track the usage and outcomes of the Amazon EC2 API operations over time. This information gives you a better perspective on how your web applications are performing, and enables you to identify and diagnose a variety of issues. You can also set alarms that watch for certain thresholds, and send notifications or take specific actions when those thresholds are met.

For more information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Important**  
Amazon EC2 API metrics is an opt-in feature. You must request access to this feature. For more information, see [Enable Amazon EC2 API metrics](#enable-ec2-api-metrics).

**Topics**
+ [Enable Amazon EC2 API metrics](#enable-ec2-api-metrics)
+ [Amazon EC2 API metrics and dimensions](#monitor-metrics_dimensions)
+ [Metric data retention](#monitor-retention)
+ [Monitoring requests made on your behalf](#throttling-metrics)
+ [Billing](#monitor-billing)
+ [Working with Amazon CloudWatch](#monitor-using)

## Enable Amazon EC2 API metrics
<a name="enable-ec2-api-metrics"></a>

Use the following procedure to request access to this feature for your AWS account.

**To request access to this feature**

1. Open [AWS Support Center](https://console.aws.amazon.com/support/home#/).

1. Choose **Create case**.

1. Choose **Account and billing**.

1. For **Service**, choose **General Info and Getting Started**.

1. For **Category**, choose **Using AWS & Services**.

1. Choose **Next step: Additional information**.

1. For **Subject**, enter **Request access to Amazon EC2 API metrics**.

1. For **Description**, enter **Please grant my account access to Amazon EC2 API metrics. Related page: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/monitor.html**. Also include the Region where you need access.

1. Choose **Next step: Solve now or contact us**.

1. On the **Contact us** tab, choose your preferred contact language and method of contact.

1. Choose **Submit**.

## Amazon EC2 API metrics and dimensions
<a name="monitor-metrics_dimensions"></a>

### Metrics
<a name="monitor-metrics"></a>

The Amazon EC2 API metrics are contained in the `AWS/EC2/API` namespace. The following tables list the metrics available for Amazon EC2 API requests.


| Metric | Description | 
| --- | --- | 
| `ClientErrors` | The number of failed API requests caused by client errors.<br />These errors are usually caused by something the client did, such as specifying an incorrect or invalid parameter in the request, or using an action or resource on behalf of a user that does not have permission to use the action or resource.<br />Unit: Count | 
| `RequestLimitExceeded` | The number of times the maximum request rate permitted by the Amazon EC2 APIs has been exceeded for your account.<br />Amazon EC2 API requests are throttled to help maintain the performance of the service. If your requests have been throttled, you get the `Client.RequestLimitExceeded` error.<br />Unit: Count | 
| `AwsTriggeredRequestLimitExceeded` | The number of failed API requests caused by throttling which AWS has applied due to an operational issue.<br />When this throttling occurs, you receive a `Client.RequestLimitExceeded` error with a message indicating that your request has been throttled due to an AWS operational issue. This throttling is temporary and resolves automatically once the operational issue is addressed. Implement exponential backoff and retry logic to handle these temporary throttles gracefully.<br />Unit: Count | 
| `ServerErrors` | The number of failed API requests caused by internal server errors.<br />These errors are usually caused by an AWS server-side error, exception, or failure.<br />Unit: Count | 
| `SuccessfulCalls` | The number of successful API requests.<br />Unit: Count | 

### Dimensions
<a name="monitor-dimensions"></a>

The Amazon EC2 metric data can be filtered across all EC2 API actions. For more information about dimensions, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).

## Metric data retention
<a name="monitor-retention"></a>

Amazon EC2 API metrics are sent to CloudWatch at 1-minute intervals. CloudWatch retains metric data as follows:
+ Data points with a period of 60 seconds (1 minute) are available for 15 days.
+ Data points with a period of 300 seconds (5 minutes) are available for 63 days.
+ Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).

## Monitoring requests made on your behalf
<a name="throttling-metrics"></a>

API requests made by AWS services on your behalf, such as requests made by service-linked roles, do not count toward your API throttling limits and they do not send metrics to Amazon CloudWatch for your account. These requests cannot be monitored using CloudWatch.

API requests made on your behalf by third-party service providers do count toward your API throttling limits and they do send metrics to Amazon CloudWatch for your account. These requests can be monitored using CloudWatch.

## Billing
<a name="monitor-billing"></a>

Standard CloudWatch pricing and charges apply. No additional charges are applied for using the Amazon EC2 API metrics. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Working with Amazon CloudWatch
<a name="monitor-using"></a>

**Contents**
+ [Viewing CloudWatch metrics](#monitor-using-viewing)
+ [Creating CloudWatch alarms](#monitor-creating)

### Viewing CloudWatch metrics
<a name="monitor-using-viewing"></a>

Use the following procedure to view the Amazon EC2 API metrics.

**Prerequisite**  
You must enable access to Amazon EC2 API metrics for your account. For more information, see [Enable Amazon EC2 API metrics](#enable-ec2-api-metrics).

**To view the Amazon EC2 API metrics using the console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, chose **Metrics**, **All metrics**.

1. On the **Browse** tab, under **Metrics**, select the desired Region to view metrics.

1. Choose the **EC2** metric namespace.

1. To view the metrics, select the metric dimension, such as **Per-Instance Metrics**.
**Note**  
Metrics are hidden after two weeks of inactivity. If they receive no new data points in the past two weeks, they no longer appear in the console, won't show up when you type their metric name or dimension names in the console search box, and are not returned by the [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) AWS CLI command. To retrieve these metrics, use the [get-metric-data]() or [get-metric-statistics]() commands.

**To view Amazon EC2 API metrics using the command line**

Use one of the following commands:
+ [list-metrics](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) (AWS CLI)

  ```
  aws cloudwatch list-metrics --namespace "AWS/EC2/API"
  ```
+ [Get-CWMetricList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-CWMetricList.html) (AWS Tools for Windows PowerShell)

  ```
  Get-CWMetricList -Namespace "AWS/EC2/API"
  ```

### Creating CloudWatch alarms
<a name="monitor-creating"></a>

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period that you specify. It sends a notification to an SNS topic based on the value of the metric relative to a given threshold over a number of time periods.

For example, you can create an alarm that monitors the number of DescribeInstances API requests that fail due to server-side errors. The following alarm sends an email notification when the number of DescribeInstances API request failures reach a threshold of 10 server-side errors during a 5-minute period.

**Prerequisite**  
You must enable access to the Amazon EC2 API metrics for your account. For more information, see [Enable Amazon EC2 API metrics](#enable-ec2-api-metrics).

**To create an alarm for Amazon EC2 DescribeInstances API request server errors**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose **Select metric**, and the specify the following:

   1. Choose **EC2/API**.

   1. Choose **Per-Action Metrics**.

   1. Select the check box next to **DescribeInstances** that is in the same row as the **ServerErrors** metric name.

   1. Choose **Select metric**.

1. The **Specify metric and conditions** page appears, showing a graph and other information about the metric and statistic that you selected.

   1. Under **Metric**, specify the following:

      1. For **Statistic**, choose **Sum**.

      1. For **Period**, verify that **5 minutes** is selected.

   1. Under **Conditions**, specify the following:

      1. For **Threshold type**, choose **Static**.

      1. For **Whenever ServerErrors is**, choose **Greater/Equal** **>=**.

      1. For **than...**, enter **10**.

   1. Choose **Next**.

1. The **Configure actions** page appears.

   1. Under **Notification**, specify the following:

     1. For **Alam state trigger**, choose **In alarm**.

     1. For **Select an SNS topic**, choose **Select an existing SNS topic** or **Create new topic**, and complete the required fields for the notification.

     1. Choose **Next**.

1. The **Add name and description** page appears. 

   1. For **Alarm name**, enter a name for your alarm. The name must contain only ASCII characters.

   1. For **Alarm description**, enter an optional description for your alarm.

   1. Choose **Next**.

1. The **Preview and create** page appears. Verify that the information is correct, and then choose **Create alarm**.

For more information, see [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.