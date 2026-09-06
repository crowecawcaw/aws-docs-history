

# Process flow log records in CloudWatch Logs
<a name="process-records-cwl"></a>

You can process flow log records as you would with any other log events collected by CloudWatch Logs. For more information about monitoring log data and metric filters, see [Creating metrics from log events using filter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch Logs User Guide*.

## Example: Create a CloudWatch metric filter and alarm for a flow log
<a name="flow-logs-cw-alarm-example"></a>

In this example, you have a flow log for `eni-1a2b3c4d`. You want to create an alarm that alerts you if there have been 10 or more rejected attempts to connect to your instance over TCP port 22 (SSH) within a 1-hour time period. First, you must create a metric filter that matches the pattern of the traffic for which to create the alarm. Then, you can create an alarm for the metric filter.

**To create a metric filter for rejected SSH traffic and create an alarm for the filter**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Log groups**.

1. Select the check box for the log group, and then choose **Actions**, **Create metric filter**.

1. For **Filter pattern**, enter the following string.

   ```
   [version, account, eni, source, destination, srcport, destport="22", protocol="6", packets, bytes, windowstart, windowend, action="REJECT", flowlogstatus]
   ```

1. For **Select log data to test**, select the log stream for your network interface. (Optional) To view the lines of log data that match the filter pattern, choose **Test pattern**.

1. When you're ready, choose **Next**.

1. Enter a filter name, metric namespace, and metric name. Set the metric value to 1. When you're done, choose **Next** and then choose **Create metric filter**.

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Select the metric name that you created and then choose **Select metric**.

1. Configure the alarm as follows, and then choose **Next**:
   + For **Statistic**, choose **Sum**. This ensure that you capture the total number of data points for the specified time period.
   + For **Period**, choose **1 hour**.
   + For **Whenever TimeSinceLastActive is...**, choose **Greater/Equal** and enter 10 for the threshold.
   + For **Additional configuration**, **Datapoints to alarm**, leave the default of 1.

1. Choose **Next**.

1. For **Notification**, select an existing SNS topic or choose **Create new topic** to create a new one. Choose **Next**.

1. Enter a name and description for the alarm and choose **Next**.

1. When you are done previewing the alarm, choose **Create alarm**.