

# SMOPS03-BP01 Implement thorough capacity planning for high-viewership events
<a name="smops03-bp01"></a>

Large-scale streaming events require thorough capacity planning across all components of the streaming workflow to maintain reliable delivery during peak viewership. This planning must account for potential viewership patterns, regional distribution, and engagement behaviors.

**Desired outcome:**
+ Sufficient capacity across all streaming workflow components to handle peak viewership without quality degradation or service disruption.

**Benefits of establishing this best practice:**
+ Reliable streaming during high-profile events
+ Prevention of quality degradation during viewership spikes
+ Optimized resource allocation and cost management
+ Enhanced viewer satisfaction during peak events

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Capacity planning across all components of the streaming workflow allows each layer to handle peak viewership without becoming a bottleneck.

For ingest and encoding capacity, calculating required encoder capacity based on expected stream count and quality levels, provisioning redundant encoders in multiple availability zones, and implementing N\+K redundancy (where N is the number of required encoders and K is additional backup capacity) for live events provides resilience. Reserved capacity for critical encoders during high-profile events further reduces risk.

Origin and packaging capacity planning involves calculating expected request rates based on segment duration and viewer count, accounting for manifest request frequency from players, provisioning sufficient capacity to handle peak request rates, and implementing auto-scaling with pre-warming for packaging services.

Content delivery network (CDN) capacity requires working with CDN providers to secure sufficient capacity, requesting capacity reservations for major events, distributing load across multiple CDNs when possible, and configuring appropriate cache settings to maximize offload.

API and authentication services must be scaled to handle peak login rates, with token caching strategies, appropriately scaled API gateways and backend services, and rate limiting to protect critical services.

### Implementation steps
<a name="implementation-steps"></a>

1. **Gather historical data from:** Gather historical data from similar events to inform capacity estimates and identify patterns.

1. **Create viewership forecasts:** Create viewership forecasts with peak estimates that account for regional distribution and engagement behaviors.

1. **Calculate capacity requirements for:** Calculate capacity requirements for each component based on forecasted peak demand with appropriate safety margins.

1. **Implement capacity reservations:** Implement capacity reservations where needed so that resources are available during the event.

1. **Design and test auto-scaling:** Design and test auto-scaling configurations to handle demand fluctuations during the event.

1. **Conduct load testing:** Conduct load testing to validate capacity plans against realistic traffic patterns and peak scenarios.

1. **Create capacity monitoring dashboards:** Create capacity monitoring dashboards to provide real-time visibility into resource utilization during the event.

1. **Establish escalation procedures:** Establish escalation procedures for capacity issues to enable rapid response if thresholds are exceeded.

## Resources
<a name="resources"></a>

**Related documents**
+ [Requesting service limit increases on AWS](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)

**Related services**
+ [AWS Elemental MediaLive](https://aws.amazon.com/medialive/)
+ [AWS Elemental MediaPackage](https://aws.amazon.com/mediapackage/)
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)