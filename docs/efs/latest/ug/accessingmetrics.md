# Accessing CloudWatch metrics for Amazon EFS

You can view Amazon EFS metrics for CloudWatch in several ways:

- In the Amazon EFS console
- In the CloudWatch console
- Using the CloudWatch CLI
- Using the CloudWatch API

1. Sign in to the AWS Management Console and open the Amazon EFS console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **File systems**.
3. Choose the file system that you want to view CloudWatch metrics for.
4. Choose **Monitoring** to display the **File system
   metrics** page.

The **File system metrics** page displays a default set of CloudWatch
metrics for the file system. Any CloudWatch alarms that you have configured also display with
these metrics. For file systems that use Max I/O performance mode, the default set of
metrics includes Burst Credit balance in place of Percent IO limit. You can override the
default settings using the **Metrics settings** dialog box, accessed by
opening the settings.

###### Note

The Throughput utilization (%) metric is not a CloudWatch metric; it is derived using
CloudWatch metric math. 5. You can adjust the way metrics and alarms are displayed using the controls on the
**File system metric** page, as follows.

    * Toggle the **Display mode** between **Time
     series** or **Single value**.
    * Show or hide any CloudWatch alarms configured for the file system.
    * Choose **See more in CloudWatch** to view the metrics in CloudWatch.
    * Choose **Add to dashboard** to open your CloudWatch dashboard and add
     the displayed metrics.
    * Adjust the metric time window displayed from 1 hour to 1 week.

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. In the navigation pane, choose **Metrics**.
3. Select the **EFS** namespace.
4. (Optional) To view a metric, enter its name in the search field.
5. (Optional) To filter by dimension, select **FileSystemId**.

- Use the [`list-metrics`](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command with the `--namespace "AWS/EFS"`
  namespace. For more information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").
- Call `GetMetricStatistics`. For more information, see
  the [Amazon CloudWatch API Reference](../../../AmazonCloudWatch/latest/APIReference.md "../../../AmazonCloudWatch/latest/APIReference.md").
