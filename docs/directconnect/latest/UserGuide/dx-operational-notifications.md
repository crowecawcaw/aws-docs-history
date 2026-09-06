

# Direct Connect operational event notifications
<a name="dx-operational-notifications"></a>

Direct Connect continuously monitors your connections for operational events that may affect your connectivity. When Direct Connect detects an operational event, it sends notifications through [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) to inform you of the event.

Direct Connect monitors for packet loss in the following connectivity segments:
+ **To your Region** – Packet loss on the path between your Direct Connect location and its associated AWS Region.
+ **Between Regions** – Packet loss on the inter-Region path when you use a [Direct Connect gateway](direct-connect-gateways.md) to route traffic across AWS Regions.

Direct Connect targets sending an initial notification to the affected account within the following timeframes:


| Connectivity segment | Target notification time | 
| --- | --- | 
| To your Region | Within 5 minutes of detection | 
| Between Regions | Within 15 minutes of detection | 

**Note**  
Notification timing begins when the packet loss event is detected by Direct Connect monitoring systems. Some events may require additional time for detection, scope assessment, and notification delivery.

## What to expect in a notification
<a name="operational-notifications-content"></a>

When Direct Connect detects packet loss affecting your connections, you receive notifications through AWS Health in the following sequence:

1. **Initial notification** – Indicates that Direct Connect has detected packet loss affecting your connection(s). Includes the impacted Direct Connect location and the start time of the event.

1. **Update notifications** – Indicates that the previously reported event is still ongoing.

1. **Resolution notification** – Indicates that the event has been resolved and connectivity has been restored.

Each notification includes the Direct Connect location where the event was detected, the start time of the event, and the current status (open, update, or resolved).

## Recommended actions
<a name="operational-notifications-actions"></a>

When you receive an operational event notification, take the following actions:
+ **Verify your traffic** – Check whether your applications are experiencing connectivity issues consistent with the notification.
+ **Monitor your CloudWatch metrics** – Review your [CloudWatch metrics for Direct Connect](monitoring-cloudwatch.md) to assess impact. `ConnectionState` indicates whether your connection is up, `ConnectionBpsEgress` and `ConnectionBpsIngress` show throughput changes, and `ConnectionPpsEgress` and `ConnectionPpsIngress` show packet rate changes that may indicate loss.
+ **Check Network Synthetic Monitor** – If you have configured [Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html), review your packet loss and latency metrics for additional context. Direct Connect operational event notifications and Network Synthetic Monitor metrics may not always correlate.
+ **Rely on redundant connections** – If you have configured your deployment for [Maximum resiliency](resiliency_toolkit.md#maximum_resiliency), traffic should automatically route to healthy connections during an event.

If you are monitoring for packet loss on your Direct Connect connections and do not receive an AWS Health notification within the expected timeframe, the packet loss may be occurring outside of the AWS network. Check your on-premises router, cross-connect, or contact your colocation provider or network service provider for further investigation. If the issue persists after troubleshooting with those parties, contact [AWS Support](https://console.aws.amazon.com/support/) for additional assistance.

## Integrating with AWS Health
<a name="operational-notifications-health-integration"></a>

To receive and act on Direct Connect operational event notifications, you can use the following AWS Health features:
+ **Health Dashboard** – View active and recent events in the [Health Dashboard](https://health.aws.amazon.com/health/home) in the AWS Management Console.
+ **Amazon EventBridge** – Create rules to route AWS Health events to targets such as Amazon SNS topics, Lambda functions, or other AWS services for automated alerting or remediation. For more information, see [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html).
+ **AWS Health API** – Programmatically query for events affecting your resources. For more information, see the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/).

Direct Connect operational event notifications are generated for packet loss events detected within AWS network infrastructure and apply to dedicated and hosted connections that are part of the Direct Connect service. Events occurring on partner networks, colocation provider infrastructure, or customer on-premises equipment are not covered by these notifications.

## Related resources
<a name="operational-notifications-related"></a>
+ [Direct Connect maintenance](dx-maintenance.md)
+ [Monitoring and visibility with Direct Connect](monitoring-overview.md)
+ [AWS Direct Connect Resiliency Toolkit](resiliency_toolkit.md)
+ [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html)