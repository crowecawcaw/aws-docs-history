# Monitor your global network with

Amazon CloudWatch metrics

You can monitor AWS Global Networks for Transit Gateways using Amazon CloudWatch, which collects raw data and processes it into
readable, near-real-time metrics. These statistics are kept for 15 months, so that you
can access historical information and gain a better perspective on how your web
application or service is performing. You can also set alarms that watch for certain
thresholds, and send notifications or take actions when those thresholds are met. For
more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

You can view CloudWatch metrics in your global network for your registered transited
gateways, your associated Site-to-Site VPN connections, and your on-premises resources. You can
view metrics per transit gateway and per transit gateway attachment, per global
network.

For more information about the supported metrics, see the following topics:

- [CloudWatch metrics
  for your transit gateways](../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md "../../../vpc/latest/tgw/transit-gateway-cloudwatch-metrics.md")
- [Monitor VPN
  tunnels using Amazon CloudWatch](../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md "../../../vpn/latest/s2svpn/monitoring-cloudwatch-vpn.md")
- [View CloudWatch metrics for on-premises resources](cw-metrics-on-premises.md "cw-metrics-on-premises.md")
  For examples of creating alarms, see [Creating Amazon CloudWatch Alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the
  _Amazon CloudWatch User Guide_.
