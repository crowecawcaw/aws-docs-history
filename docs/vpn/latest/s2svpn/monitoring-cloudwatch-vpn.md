# Monitor AWS Site-to-Site VPN tunnels using Amazon CloudWatch

You can monitor VPN tunnels using CloudWatch, which collects and processes raw data from the
VPN service into readable, near real-time metrics. These statistics are recorded for a
period of 15 months, so that you can access historical information and gain a better
perspective on how your web application or service is performing. VPN metric data is
automatically sent to CloudWatch as it becomes available.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

###### Contents

- [VPN metrics and dimensions](#metrics-dimensions-vpn "#metrics-dimensions-vpn")
- [View VPN CloudWatch metrics](viewing-metrics.md "viewing-metrics.md")
- [Create CloudWatch alarms to monitor VPN tunnels](creating-alarms-vpn.md "creating-alarms-vpn.md")

## VPN metrics and dimensions

The following CloudWatch metrics are available for your Site-to-Site VPN connections.

| Metric            | Description                                                                                                                                                                                                                                                                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TunnelState`     | The state of the tunnels. For static VPNs, 0 indicates DOWN<br>and 1 indicates UP. For BGP VPNs, 1 indicates ESTABLISHED and 0<br>is used for all other states. For both types of VPNs, values<br>between 0 and 1 indicate at least one tunnel is not UP.<br>Units: Fractional value between 0 and 1                                                                |
| `TunnelDataIn` †  | The bytes received on the AWS side of the connection through<br>the VPN tunnel from a customer gateway. Each metric data point<br>represents the number of bytes received after the previous data<br>point. Use the Sum statistic to show the total number of bytes<br>received during the period.<br>This metric counts the data after decryption.<br>Units: Bytes |
| `TunnelDataOut` † | The bytes sent from the AWS side of the connection through<br>the VPN tunnel to the customer gateway. Each metric data point<br>represents the number of bytes sent after the previous data<br>point. Use the Sum statistic to show the total number of bytes<br>sent during the period.<br>This metric counts the data before encryption.<br>Units: Bytes          |

† These metrics can report network usage even when the tunnel is down. This is due to
periodic status checks performed on the tunnel, and background ARP and BGP requests.

To filter the metric data, use the following dimensions.

| Dimension         | Description                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------- |
| `VpnId`           | Filters the metric data by the Site-to-Site VPN connection ID.                              |
| `TunnelIpAddress` | Filters the metric data by the IP address of the tunnel for<br>the virtual private gateway. |
