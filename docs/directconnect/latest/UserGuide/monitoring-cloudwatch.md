

# Monitor with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor physical Direct Connect connections, and virtual interfaces, using CloudWatch. CloudWatch collects raw data from Direct Connect, and processes it into readable metrics. By default, CloudWatch provides Direct Connect metric data in 5-minute intervals. The metric data in every interval is an aggregation of at least two samples collected during that interval. 

For detailed information about CloudWatch, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). You can also monitor your services CloudWatch to see what ones are using resources. For more information, see [AWS services that publish CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html).

**Topics**
+ [Direct Connect metrics and dimensions](#metrics-dimensions)
+ [View Direct Connect CloudWatch metrics](viewing-metrics.md)
+ [Create alarms to monitor connections](creating-alarms.md)

## Direct Connect metrics and dimensions
<a name="metrics-dimensions"></a>

Metrics are available for Direct Connect physical connections, and virtual interfaces.

### Direct Connect Connection metrics
<a name="connection-metrics-dimensions"></a>

The following metrics are available from Direct Connect dedicated connections. 


| Metric | Description | 
| --- | --- | 
| `ConnectionState` | The state of the connection.1 indicates **up** and 0 indicates **down**.<br />This metric is available for dedicated and hosted connections.This metric is also available in hosted virtual interface owner accounts in addition to connection owner accounts.<br />Units: There are no units returned for this metric. | 
| `ConnectionBpsEgress` | The bitrate for outbound data from the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Bits per second | 
| `ConnectionBpsIngress` | The bitrate for inbound data to the AWS side of the connection.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Bits per second | 
| `ConnectionPpsEgress` | ` The packet rate for outbound data from the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Packets per second | 
| `ConnectionPpsIngress` | The packet rate for inbound data to the AWS side of the connection.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />This metric might be unavailable for a new connection, or when a device reboots. The metric starts when the connection is used to send or receive traffic.<br />Units: Packets per second | 
| `ConnectionCRCErrorCount` | This count is no longer in use. Use `ConnectionErrorCount` instead. | 
| `ConnectionErrorCount` | The total error count for all types of MAC level errors recorded by the AWS device. The total includes cyclic redundancy check (CRC) errors. The root cause of these errors can be on either the customer side or the AWS side.<br />This metric is the error count that occurred since the last reported datapoint. When there are errors on the interface, the metric reports non-zero values. To get the total count of all errors for the selected interval in CloudWatch, for example, 5 minutes, apply the "sum" statistic. <br />The metric value is set to 0 when the errors on the interface stop. This metric replaces `ConnectionCRCErrorCount`, which is no longer in use. <br />Units: Count | 
| ConnectionLightLevelTx | Indicates the health of the fiber connection for outbound (egress) traffic from the AWS side of the connection.<br />There are two dimensions for this metric. For more information, see [Direct Connect available dimensions](#metrics-available-dimensions).<br />Units: dBm | 
| `ConnectionLightLevelRx` | Indicates the health of the fiber connection for inbound (ingress) traffic to the AWS side of the connection.<br />There are two dimensions for this metric. For more information, see [Direct Connect available dimensions](#metrics-available-dimensions).<br />Units: dBm | 
| ConnectionEncryptionState | Indicates the connection encryption status. 1 indicates the connection encryption is `up`, and 0 indicates the connection encryption is `down`. When this metric is applied to a LAG, 1 indicates that all connections in the LAG have encryption `up`. 0 indicates at least one LAG connection encryption is `down`. | 
| ConnectionDiscardsPpsEgress | The packet discard rate for outbound data from the AWS side of the connection. This metric tracks packets that are dropped due to buffer overflows, interface congestion, or other network conditions.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default, 1 minute minimum). You can change the default aggregate.<br />Units: Packets per second | 

### Direct Connect virtual interface metrics
<a name="virtual-interfaces-metrics-dimensions"></a>

The following metrics are available from Direct Connect virtual interfaces. 


| Metric | Description | 
| --- | --- | 
| `VirtualInterfaceBpsEgress` | The bitrate for outbound data from the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Bits per second | 
| `VirtualInterfaceBpsIngress` | The bitrate for inbound data to the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Bits per second | 
| `VirtualInterfacePpsEgress` | The packet rate for outbound data from the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Packets per second | 
| `VirtualInterfacePpsIngress` | The packet rate for inbound data to the AWS side of the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Packets per second | 
| `VirtualInterfaceBgpStatus` | The state of the BGP peering session for the virtual interface. 1 indicates **up** and 0 indicates **down**.<br />Units: There are no units returned for this metric. | 
| `VirtualInterfaceBgpPrefixesAccepted` | The number of BGP prefixes accepted from the BGP peer on the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Count | 
| `VirtualInterfaceBgpPrefixesAdvertised` | The number of BGP prefixes advertised to the BGP peer on the virtual interface.<br />The number reported is the aggregate (average) over the specified time period (5 minutes by default). <br />Units: Count | 

### Direct Connect available dimensions
<a name="metrics-available-dimensions"></a>

You can filter the Direct Connect data using the following dimensions.


| Dimension | Description | 
| --- | --- | 
| `ConnectionId` | This dimension is available on the metrics for Direct Connect connection, and virtual interface. This dimension filters the data by the connection. | 
| OpticalLaneNumber | This dimension filters the ConnectionLightLevelTx data and the ConnectionLightLevelRx data, and filters the data by the optical lane number of the Direct Connect connection. | 
| VirtualInterfaceId | This dimension is available on the metrics for Direct Connect virtual interface, and filters the data by the virtual interface. | 
| IpAddressFamily | This dimension is available on the BGP metrics for Direct Connect virtual interfaces (VirtualInterfaceBgpStatus, VirtualInterfaceBgpPrefixesAccepted, VirtualInterfaceBgpPrefixesAdvertised). This dimension filters the data by IP address family. Valid values are ipv4 and ipv6. | 

**Topics**
+ [Direct Connect metrics and dimensions](#metrics-dimensions)
+ [View Direct Connect CloudWatch metrics](viewing-metrics.md)
+ [Create alarms to monitor connections](creating-alarms.md)