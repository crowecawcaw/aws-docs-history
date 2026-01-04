# Monitor with Amazon CloudWatch

You can monitor physical Direct Connect connections, and virtual interfaces, using CloudWatch.
CloudWatch collects raw data from Direct Connect, and processes it into readable metrics. By
default, CloudWatch provides Direct Connect metric data in 5-minute intervals.
The metric data in every interval is an aggregation of at least two
samples collected during that interval.

For detailed information about CloudWatch, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md"). You can also monitor your
services CloudWatch to see what ones are using resources. For more information, see [AWS
services that publish CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md "../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md").

###### Contents

- [Direct Connect metrics and dimensions](#metrics-dimensions "#metrics-dimensions")
- [View Direct Connect CloudWatch metrics](viewing-metrics.md "viewing-metrics.md")
- [Create alarms to monitor connections](creating-alarms.md "creating-alarms.md")

## Direct Connect metrics and dimensions

Metrics are available for Direct Connect physical connections, and virtual
interfaces.

### Direct Connect Connection

metrics

The following metrics are available from Direct Connect dedicated connections.

| Metric                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ConnectionState`             | The state of the connection.1 indicates **up\*<br>• and 0 indicates **down\*\*.<br>This metric is available for dedicated and hosted<br>connections.<br>NoteThis metric is also available in hosted virtual interface<br>owner accounts in addition to connection owner accounts.<br>Units: There are no units returned for this metric.                                                                                                                                                                                                                                                                                             |
| `ConnectionBpsEgress`         | The bitrate for outbound data from the AWS side of the<br>connection.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default, 1 minute minimum).<br>You can change the default aggregate.<br>This metric might be unavailable for a new connection, or when<br>a device reboots. The metric starts when the connection is used<br>to send or receive traffic.<br>Units: Bits per second                                                                                                                                                                                           |
| `ConnectionBpsIngress`        | The bitrate for inbound data to the AWS side of the<br>connection.<br>This metric might be unavailable for a new connection, or when<br>a device reboots. The metric starts when the connection is used<br>to send or receive traffic.<br>Units: Bits per second                                                                                                                                                                                                                                                                                                                                                                     |
| `ConnectionPpsEgress`         | `<br>The packet rate for outbound data from the AWS side of the<br>connection.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default, 1 minute minimum).<br>You can change the default aggregate.<br>This metric might be unavailable for a new connection, or when<br>a device reboots. The metric starts when the connection is used<br>to send or receive traffic.<br>Units: Packets per second                                                                                                                                                                               |
| `ConnectionPpsIngress`        | The packet rate for inbound data to the AWS side of the<br>connection.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default, 1 minute minimum).<br>You can change the default aggregate.<br>This metric might be unavailable for a new connection, or when<br>a device reboots. The metric starts when the connection is used<br>to send or receive traffic.<br>Units: Packets per second                                                                                                                                                                                       |
| `ConnectionCRCErrorCount`     | This<br>count is no longer in use. Use `ConnectionErrorCount`<br>instead.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `ConnectionErrorCount`        | The total error count for all types of MAC level errors on the<br>AWS device. The total includes cyclic redundancy check (CRC)<br>errors.<br>This metric is the error count that occurred since the last<br>reported datapoint. When there are errors on the interface, the<br>metric reports non-zero values. To get the total count of all<br>errors for the selected interval in CloudWatch, for example, 5<br>minutes, apply the "sum" statistic.<br>The metric value is set to 0 when the errors on the interface<br>stop.<br>NoteThis metric replaces `ConnectionCRCErrorCount`,<br>which is no longer in use.<br>Units: Count |
| `ConnectionLightLevelTx`      | Indicates the health of the fiber connection for outbound<br>(egress) traffic from the AWS side of the connection.<br>There are two dimensions for this metric. For more<br>information, see [Direct Connect available<br>dimensions](#metrics-available-dimensions "#metrics-available-dimensions").<br>Units: dBm                                                                                                                                                                                                                                                                                                                  |
| `ConnectionLightLevelRx`      | Indicates the health of the fiber connection for inbound<br>(ingress) traffic to the AWS side of the connection.<br>There are two dimensions for this metric. For more<br>information, see [Direct Connect available<br>dimensions](#metrics-available-dimensions "#metrics-available-dimensions").<br>Units: dBm                                                                                                                                                                                                                                                                                                                    |
| `ConnectionEncryptionState`   | Indicates the connection encryption status. 1 indicates the connection encryption is<br>`up`, and 0 indicates the connection encryption<br>is `down`. When this metric is applied to a LAG, 1<br>indicates that all connections in the LAG have encryption<br>`up`. 0 indicates at least one LAG connection<br>encryption is `down`.                                                                                                                                                                                                                                                                                                 |
| `ConnectionDiscardsPpsEgress` | The packet discard rate for outbound data from the AWS side of the<br>connection. This metric tracks packets that are dropped due to buffer<br>overflows, interface congestion, or other network conditions.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default, 1 minute minimum).<br>You can change the default aggregate.<br>Units: Packets per second                                                                                                                                                                                                                     |

### Direct Connect virtual

interface metrics

The following metrics are available from Direct Connect virtual interfaces.

| Metric                       | Description                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `VirtualInterfaceBpsEgress`  | The bitrate for outbound data from the AWS side of the<br>virtual interface.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default).<br>Units: Bits per second        |
| `VirtualInterfaceBpsIngress` | The bitrate for inbound data to the AWS side of the virtual<br>interface.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default).<br>Units: Bits per second           |
| `VirtualInterfacePpsEgress`  | The packet rate for outbound data from the AWS side of the<br>virtual interface.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default).<br>Units: Packets per second |
| `VirtualInterfacePpsIngress` | The packet rate for inbound data to the AWS side of the<br>virtual interface.<br>The number reported is the aggregate (average) over the<br>specified time period (5 minutes by default).<br>Units: Packets per second    |

### Direct Connect available

dimensions

You can filter the Direct Connect data using the following dimensions.

| Dimension            | Description                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ConnectionId`       | This dimension is available on the metrics for Direct Connect<br>connection, and virtual interface. This dimension filters the<br>data by the connection.                                  |
| `OpticalLaneNumber`  | This dimension filters the `ConnectionLightLevelTx`<br>data and the `ConnectionLightLevelRx` data, and filters<br>the data by the optical lane number of the Direct Connect<br>connection. |
| `VirtualInterfaceId` | This dimension is available on the metrics for Direct Connect virtual<br>interface, and filters the data by the virtual interface.                                                         |

###### Topics

- [View Direct Connect CloudWatch metrics](viewing-metrics.md "viewing-metrics.md")
- [Create alarms to monitor connections](creating-alarms.md "creating-alarms.md")
