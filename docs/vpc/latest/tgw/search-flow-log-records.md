# Search AWS Transit Gateway Flow Logs records

You can search your flow log records that are published to CloudWatch Logs by using the
CloudWatch Logs console. You can use [metric filters](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md") to filter flow log records. Flow log records are space
delimited.

###### To search flow log records using the CloudWatch Logs console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, and then choose
   **Log groups**.
3. Select the log group that contains your flow log. A list of log streams
   for each transit gateway is displayed.
4. Select the individual log stream if you know the transit gateway that you are
   searching for. Alternatively, choose **Search Log Group**
   to search the entire log group. This might take some time if there are many
   transit gateways in your log group, or depending on the time range that you
   select.
5. For **Filter events**, enter the following string. This
   assumes that the flow log record uses the [default format](tgw-flow-logs.md#flow-logs-default "tgw-flow-logs.md#flow-logs-default").

```
[version, resource_type, account_id,tgw_id, tgw_attachment_id, tgw_src_vpc_account_id, tgw_dst_vpc_account_id, tgw_src_vpc_id, tgw_dst_vpc_id, tgw_src_subnet_id, tgw_dst_subnet_id, tgw_src_eni, tgw_dst_eni, tgw_src_az_id, tgw_dst_az_id, tgw_pair_attachment_id, srcaddr, dstaddr, srcport, dstport, protocol, packets, bytes,start,end, log_status, type,packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, tcp_flags,region, flow_direction, pkt_src_aws_service, pkt_dst_aws_service]
```

6. Modify the filter as needed by specifying values for the fields. The
   following examples filter by specific source IP addresses.

```
[version, resource_type, account_id,tgw_id, tgw_attachment_id, tgw_src_vpc_account_id, tgw_dst_vpc_account_id, tgw_src_vpc_id, tgw_dst_vpc_id, tgw_src_subnet_id, tgw_dst_subnet_id, tgw_src_eni, tgw_dst_eni, tgw_src_az_id, tgw_dst_az_id, tgw_pair_attachment_id, srcaddr= 10.0.0.1, dstaddr, srcport, dstport, protocol, packets, bytes,start,end, log_status, type,packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, tcp_flags,region, flow_direction, pkt_src_aws_service, pkt_dst_aws_service]
[version, resource_type, account_id,tgw_id, tgw_attachment_id, tgw_src_vpc_account_id, tgw_dst_vpc_account_id, tgw_src_vpc_id, tgw_dst_vpc_id, tgw_src_subnet_id, tgw_dst_subnet_id, tgw_src_eni, tgw_dst_eni, tgw_src_az_id, tgw_dst_az_id, tgw_pair_attachment_id, srcaddr= 10.0.2.*, dstaddr, srcport, dstport, protocol, packets, bytes,start,end, log_status, type,packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, tcp_flags,region, flow_direction, pkt_src_aws_service, pkt_dst_aws_service]
```

The following example filters by transit gateway ID tgw-123abc456bca, destination
port, and number of bytes.

```
[version, resource_type, account_id,tgw_id=tgw-123abc456bca, tgw_attachment_id, tgw_src_vpc_account_id, tgw_dst_vpc_account_id, tgw_src_vpc_id, tgw_dst_vpc_id, tgw_src_subnet_id, tgw_dst_subnet_id, tgw_src_eni, tgw_dst_eni, tgw_src_az_id, tgw_dst_az_id, tgw_pair_attachment_id, srcaddr, dstaddr, srcport, dstport = 80 || dstport = 8080, protocol, packets, bytes >= 500,start,end, log_status, type,packets_lost_no_route, packets_lost_blackhole, packets_lost_mtu_exceeded, packets_lost_ttl_expired, tcp_flags,region, flow_direction, pkt_src_aws_service, pkt_dst_aws_service]
```
