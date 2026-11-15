

# Search AWS Cloud WAN Flow Logs records
<a name="cwan-search-flow-log-records"></a>

You can search your flow log records that are published to CloudWatch Logs by using the CloudWatch Logs console. You can use [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) to filter flow log records. Flow log records are space delimited.

**To search flow log records using the CloudWatch Logs console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Log groups**. 

1. Select the log group that contains your flow log. A list of log streams for each core network attachment is displayed.

1. Select the individual log stream if you know the core network attachment that you are searching for. Alternatively, choose **Search Log Group** to search the entire log group. This might take some time if there are many core network attachments in your log group, or depending on the time range that you select.

1. For **Filter events**, enter the following string. This assumes that the flow log record uses the [default format](cwan-flow-logs.md#cwan-flow-logs-default).

   ```
   [version, resource_type, account_id, core_network_id, cwan_attachment_id, cwan_pair_attachment_id, src_account_id, dst_account_id, src_vpc_id, dst_vpc_id, src_subnet_id, dst_subnet_id, src_eni, dst_eni, src_az_id, dst_az_id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, log_status, type, tcp_flags, flow_direction, packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, src_region, dst_region, src_segment_name, dst_segment_name, pkt_src_aws_service, pkt_dst_aws_service, network_function_group_attachment_ids, src_attachment_type, dst_attachment_type]
   ```

1. Modify the filter as needed by specifying values for the fields. The following examples filter by specific source IP addresses.

   ```
   [version, resource_type, account_id, core_network_id, cwan_attachment_id, cwan_pair_attachment_id, src_account_id, dst_account_id, src_vpc_id, dst_vpc_id, src_subnet_id, dst_subnet_id, src_eni, dst_eni, src_az_id, dst_az_id, srcaddr=10.0.0.1, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, log_status, type, tcp_flags, flow_direction, packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, src_region, dst_region, src_segment_name, dst_segment_name, pkt_src_aws_service, pkt_dst_aws_service, network_function_group_attachment_ids, src_attachment_type, dst_attachment_type]
   [version, resource_type, account_id, core_network_id, cwan_attachment_id, cwan_pair_attachment_id, src_account_id, dst_account_id, src_vpc_id, dst_vpc_id, src_subnet_id, dst_subnet_id, src_eni, dst_eni, src_az_id, dst_az_id, srcaddr=10.0.2.*, dstaddr, srcport, dstport, protocol, packets, bytes, start, end, log_status, type, tcp_flags, flow_direction, packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, src_region, dst_region, src_segment_name, dst_segment_name, pkt_src_aws_service, pkt_dst_aws_service, network_function_group_attachment_ids, src_attachment_type, dst_attachment_type]
   ```

   The following example filters by core network ID core-network-123abc456bca, destination port, and number of bytes.

   ```
   [version, resource_type, account_id, core_network_id=core-network-123abc456bca, cwan_attachment_id, cwan_pair_attachment_id, src_account_id, dst_account_id, src_vpc_id, dst_vpc_id, src_subnet_id, dst_subnet_id, src_eni, dst_eni, src_az_id, dst_az_id, srcaddr, dstaddr, srcport, dstport = 80 || dstport = 8080, protocol, packets, bytes >= 500, start, end, log_status, type, tcp_flags, flow_direction, packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, src_region, dst_region, src_segment_name, dst_segment_name, pkt_src_aws_service, pkt_dst_aws_service, network_function_group_attachment_ids, src_attachment_type, dst_attachment_type]
   ```