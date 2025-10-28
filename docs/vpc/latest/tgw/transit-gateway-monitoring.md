# Metrics and events in AWS Transit Gateway

You can use the following features to monitor your transit gateways, analyze traffic patterns,
and troubleshoot issues with your transit gateways.

**CloudWatch metrics**

You can use Amazon CloudWatch to retrieve statistics about data points for your transit gateways
as an ordered set of time series data, known as _metrics_.
You can use these metrics to verify that your system is performing as expected.
For more information, see [CloudWatch metrics in AWS Transit Gateway](transit-gateway-cloudwatch-metrics.md "transit-gateway-cloudwatch-metrics.md").

**Transit Gateway Flow Logs**

You can use Transit Gateway Flow Logs to capture detailed information about
the network traffic on your transit gateways. For more information, see [Transit Gateway Flow Logs](tgw-flow-logs.md "tgw-flow-logs.md").

**VPC Flow Logs**

You can use VPC Flow Logs to capture detailed information about the traffic going to
and from the VPCs that are attached to your transit gateways. For more information, see
[VPC Flow Logs](../userguide/flow-logs.md "../userguide/flow-logs.md") in the
_Amazon VPC User Guide_.

**CloudTrail logs**

You can use AWS CloudTrail to capture detailed information about the calls made to the transit gateway
API and store them as log files in Amazon S3. You can use these CloudTrail logs to determine which
calls were made, the source IP address where the call came from, who made the call, when the
call was made, and so on. For more information, see [CloudTrail logs](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

**CloudWatch Events using Network Manager**

You can use AWS Network Manager to forward events to CloudWatch, and then route those
events to target functions or streams. Network Manager generates events for topology
changes, routing updates, and status updates, all of which can be used to alert
you to changes in your transit gateways. For more information, see [Monitoring your
global network with CloudWatch Events](../../../network-manager/latest/tgwnm/monitoring-events.md "../../../network-manager/latest/tgwnm/monitoring-events.md") in the _AWS Global
Networks for Transit Gateways User Guide_.
