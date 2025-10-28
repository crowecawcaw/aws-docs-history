# Monitor NAT gateways with Amazon CloudWatch

You can monitor your NAT gateway using CloudWatch, which collects information from your NAT
gateway and creates readable, near real-time metrics. You can use this information to
monitor and troubleshoot your NAT gateway. These metrics give you visibility into the health
and performance of your NAT gateway, enabling you to closely monitor its operation and
quickly troubleshoot any issues.

The NAT gateway metrics collected by CloudWatch include data points such as bytes
processed, packet counts, connection counts, and error rates. This enables you to thoroughly
understand the traffic flowing through your NAT gateway and identify any anomalies or
bottlenecks. CloudWatch delivers this metric data at 1-minute intervals, giving you a
granular, up-to-the-minute view of your NAT gateway's behavior.

Additionally, CloudWatch retains this NAT gateway metric data for an extended period of 15
months, enabling you to analyze trends and patterns over time. You can use this historical
data for capacity planning, performance optimization, and understanding the long-term
evolution of your NAT gateway usage.

To leverage these powerful monitoring capabilities, you can create custom CloudWatch
dashboards and alarms tailored to your specific needs. For example, you could set up alerts
to notify you whenever your NAT gateway's outbound data transfer exceeds a certain
threshold, allowing you to proactively address potential bandwidth constraints.

For more information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Contents

- [NAT gateway metrics and dimensions](metrics-dimensions-nat-gateway.md "metrics-dimensions-nat-gateway.md")
- [View NAT gateway CloudWatch metrics](viewing-metrics.md "viewing-metrics.md")
- [Create CloudWatch alarms to monitor a NAT gateway](creating-alarms-nat-gateway.md "creating-alarms-nat-gateway.md")
