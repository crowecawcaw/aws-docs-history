

# Process AWS Cloud WAN Flow Logs records in Amazon CloudWatch Logs

You can work with flow log records as you would with any other log events collected by CloudWatch Logs. For more information about monitoring log data and metric filters, see [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) in the *Amazon CloudWatch User Guide*.

## Example: Create a CloudWatch metric filter and alarm for a flow log
<a name="cwan-flow-logs-cw-alarm-example"></a>

In this example, you have a flow log for `core-network-123abc456bca`. You want to create an alarm that alerts you if any traffic on the core network is dropped because of a blackhole route within a 1-hour time period. First, you must create a metric filter that matches the pattern of the traffic for which to create the alarm. Then, you can create an alarm for the metric filter.

**To create a metric filter for blackhole-dropped traffic and create an alarm for the filter**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Log groups**.

1. Select the checkbox for the log group, and then choose **Actions**, **Create metric filter**.

1. For **Filter Pattern**, enter the following.

   ```
   [version, resource_type, account_id, core_network_id="core-network-123abc456bca", cwan_attachment_id, cwan_pair_attachment_id, src_account_id, dst_account_id, src_vpc_id, dst_vpc_id, src_subnet_id, dst_subnet_id, src_eni, dst_eni, src_az_id, dst_az_id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, log_status, type, tcp_flags, flow_direction, packets_lost_no_route, packets_lost_blackhole > 0, packets_lost_mtu_exceeded, packets_lost_ttl_expired, src_region, dst_region, src_segment_name, dst_segment_name, pkt_src_aws_service, pkt_dst_aws_service, network_function_group_attachment_ids, src_attachment_type, dst_attachment_type]
   ```

1. For **Select log data to test**, select the log stream for one of your core network attachments. (Optional) To view the lines of log data that match the filter pattern, choose **Test pattern**. When you're ready, choose **Next**.

1. Enter a filter name, metric namespace, and metric name. Set the metric value to **1**. When you're done, choose **Next** and then choose **Create metric filter**.

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose the namespace for the metric filter that you created.

   It can take a few minutes for a new metric to display in the console.

1. Select the metric name that you created, and then choose **Select metric**.

1. Configure the alarm as follows, and then choose **Next**:
   + For **Statistic**, choose **Sum**. This ensure that you capture the total number of data points for the specified time period.
   + For **Period**, choose **1 hour**.
   + For **Whenever**, choose **Greater/Equal** and enter **1** for the threshold.
   + For **Additional configuration**, **Datapoints to alarm**, leave the default of **1**.

1. For **Notification**, select an existing SNS topic, or choose **Create new topic** to create a new one. Choose **Next**.

1. Enter a name and description for the alarm and choose **Next**.

1. When you are done configuring the alarm, choose **Create alarm**.