

# Search flow log records
<a name="search-flow-log-records-cwl"></a>

You can search your flow log records that are published to CloudWatch Logs using the CloudWatch Logs console. You can use [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) to filter flow log records. Flow log records are space delimited.

**To search flow log records using the CloudWatch Logs console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, **Log groups**.

1. Select the log group that contains your flow log, and then select the log stream, if you know the network interface that you are searching for. Alternatively, choose **Search log group**. This might take some time if there are many network interfaces in your log group, or depending on the time range that you select.

1. Under **Filter events**, enter the string below. This assumes that the flow log record uses the [default format](flow-log-records.md#flow-logs-default).

   ```
   [version, accountid, interfaceid, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, logstatus]
   ```

1. Modify the filter as needed by specifying values for the fields. The following examples filter by specific source IP addresses.

   ```
   [version, accountid, interfaceid, srcaddr = 10.0.0.1, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, logstatus]
   [version, accountid, interfaceid, srcaddr = 10.0.2.*, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, action, logstatus]
   ```

   The following examples filter by destination port, the number of bytes, and whether the traffic was rejected.

   ```
   [version, accountid, interfaceid, srcaddr, dstaddr, srcport, dstport = 80 || dstport = 8080, protocol, packets, bytes, start, end, action, logstatus]
   [version, accountid, interfaceid, srcaddr, dstaddr, srcport, dstport = 80 || dstport = 8080, protocol, packets, bytes >= 400, start, end, action = REJECT, logstatus]
   ```