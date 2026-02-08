# HNOPS03-BP01 Monitor hybrid networking components

Monitoring solutions serve as an essential tool to provide
visibility across your hybrid network infrastructure. It enables
collection, visualization, and analysis of metrics from network
connectivity components like virtual private networks, dedicated
connections, and network transit hubs, allowing teams to set alarms
for performance thresholds and detect anomalies before they impact
connectivity.

**Desired outcome:**

- Quickly identified and address performance issues, security
  anomalies, and connectivity problems
- Improved network reliability, optimized resource utilization,
  and enhanced operational efficiency.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Get real-time visibility into network performance, enabling
  quick detection and resolution of issues.
- Customizable alerts and automated responses to predefined
  conditions.
- Support capacity planning and resource optimization by providing
  historical data and trends.

## Implementation guidance:

- Identify critical hybrid networking components that require
  monitoring. Determine key metrics and thresholds relevant to
  each component.
- Configure dashboards, alarms, and automated actions using
  services such as Amazon CloudWatch
- Integrate automated notification and remediation to alarms
  using services such as Amazon SNS and AWS Lambda

## Resources

- [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [Metrics
  and events in Amazon VPC Transit Gateways](../../../vpc/latest/tgw/transit-gateway-monitoring.md "../../../vpc/latest/tgw/transit-gateway-monitoring.md")
- [AWS Direct Connect Monitoring](../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md "../../../directconnect/latest/UserGuide/monitoring-cloudwatch.md")
- [Monitor
  hybrid connectivity with Amazon CloudWatch Network Synthetic
  Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/ "https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/")
- [AWS Cloud WAN events and metrics](../../../network-manager/latest/cloudwan/cloudwan-events-metrics.md "../../../network-manager/latest/cloudwan/cloudwan-events-metrics.md")
- [Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md")
- [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
