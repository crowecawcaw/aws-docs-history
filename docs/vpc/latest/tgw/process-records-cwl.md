# Process AWS Transit Gateway Flow Logs records in

Amazon CloudWatch Logs

You can work with flow log records as you would with any other log events
collected by CloudWatch Logs. For more information about monitoring log data and metric
filters, see [Creating metrics
from log events using filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md") in the _Amazon CloudWatch User Guide_.

## Example: Create a CloudWatch metric

filter and alarm for a flow log

In this example, you have a flow log for `tgw-123abc456bca`. You
want to create an alarm that alerts you if there have been 10 or more rejected
attempts to connect to your instance over TCP port 22 (SSH) within a 1-hour time
period. First, you must create a metric filter that matches the pattern of the
traffic for which to create the alarm. Then, you can create an alarm for the
metric filter.

###### To create a metric filter for rejected SSH traffic and create an alarm

for the filter

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**,
   **Log groups**.
3. Select the checkbox for the log group, and then choose
   **Actions**, **Create metric
   filter**.
4. For **Filter Pattern**, enter the following.

```
[version, resource_type, account_id,tgw_id="tgw-123abc456bca”, tgw_attachment_id, tgw_src_vpc_account_id, tgw_dst_vpc_account_id, tgw_src_vpc_id, tgw_dst_vpc_id, tgw_src_subnet_id, tgw_dst_subnet_id, tgw_src_eni, tgw_dst_eni, tgw_src_az_id, tgw_dst_az_id, tgw_pair_attachment_id, srcaddr= "10.0.0.1", dstaddr, srcport=“80”, dstport, protocol=“6”, packets, bytes,start,end, log_status, type,packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, tcp_flags,region, flow_direction, pkt_src_aws_service, pkt_dst_aws_service]
```

5. For **Select log data to test**, select the log
   stream for your transit gateway. (Optional) To view the lines of log data that
   match the filter pattern, choose **Test pattern**. When
   you're ready, choose **Next**.
6. Enter a filter name, metric namespace, and metric name. Set the metric
   value to `1`. When you're done, choose
   **Next** and then choose **Create metric
   filter**.
7. In the navigation pane, choose **Alarms**,
   **All alarms**.
8. Choose **Create alarm**.
9. Choose the namespace for the metric filter that you created.

It can take a few minutes for a new metric to display in the
console. 10. Select the metric name that you created, and then choose
**Select metric**. 11. Configure the alarm as follows, and then choose
**Next**:

    * For **Statistic**, choose
     **Sum**. This ensure that you capture the
     total number of data points for the specified time
     period.
    * For **Period**, choose **1
     hour**.
    * For **Whenever**, choose
     **Greater/Equal** and enter
     `10` for the threshold.
    * For **Additional configuration**,
     **Datapoints to alarm**, leave the default
     of `1`.

12. For **Notification**, select an existing SNS topic,
    or choose **Create new topic** to create a new one.
    Choose **Next**.
13. Enter a name and description for the alarm and choose
    **Next**.
14. When you are done configuring the alarm, choose **Create
    alarm**.
