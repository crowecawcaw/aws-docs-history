# MIDAREL01-BP02 Scale network architecture for manufacturing operations

In manufacturing environments, network reliability is crucial as disruptions can directly
impact production, quality, and safety. A reliable network architecture must provide
continuous operations even during component failures, maintenance windows, or unexpected
spikes in industrial data traffic. Implementing redundant connections, proper network
segmentation, and automated failover mechanisms helps maintain operational continuity across
the manufacturing floor.

**Desired outcome:** A resilient network infrastructure that
supports manufacturing operations without disruption, creating a continuous data flow between
manufacturing equipment and edge devices, with appropriate redundancy and failover
capabilities.

**Benefits of establishing this best practice:**

- Minimizes production downtime due to network failures
- Provides consistent data collection from production equipment
- Maintains operational integrity during maintenance or failures
- Supports scaling production capacity without compromising reliability
- Enables real-time decision making through dependable data transmission

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish redundant connectivity with automatic failover capabilities to improve the
continuity of your network operations. Implement multiple network paths to help prevent
single points of failure, with automated routing to alternative connections during
disruptions.

Consider implementing redundant connections using services like AWS Direct Connect and
AWS Site-to-Site VPN with AWS Transit Gateway to enable automatic failover and routing
capabilities across multiple network paths.

Design network segmentation that isolates critical manufacturing zones (production,
quality control, and maintenance) while maintaining appropriate communication paths.
Implement security boundaries that help protect sensitive manufacturing operations without
impeding necessary data flows.

Consider using Amazon VPC with multiple subnets and AWS Transit Gateway to create
isolated network zones while maintaining controlled communication paths. Network ACLs and
security groups can provide additional security boundaries for manufacturing-specific
requirements.

Deploy comprehensive network monitoring that tracks performance metrics, sets up alerts
for latency or throughput issues, and creates dashboards specific to manufacturing network
requirements. Include proactive monitoring of network health and automated notification
systems for potential issues.

Consider implementing monitoring using services like Amazon CloudWatch and AWS Network
Manager to track network health metrics and create automated alerts. Amazon EventBridge can
help orchestrate automated responses to network events.

Configure automated recovery procedures when network anomalies are detected in
manufacturing environments. Implement self-healing capabilities that can automatically
reroute traffic or fail over to backup systems without manual intervention.

Consider using AWS Systems Manager Automation with Amazon Route 53 health checks to
automatically detect and respond to network issues. Use AWS Lambda to implement custom
recovery logic based on your manufacturing requirements.

## Key AWS services

- AWS Direct Connect
- AWS Site-to-Site VPN
- AWS Transit Gateway
- Amazon VPC
- AWS Network Manager
- Amazon CloudWatch
- AWS Lambda
- AWS Auto Scaling

## Resources

[Building a Scalable and Secure Multi-VPC AWS Network
Infrastructure](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.md")

[AWS Direct Connect Resiliency
Recommendations](../../../directconnect/latest/UserGuide/resiliency_recommendation.md "../../../directconnect/latest/UserGuide/resiliency_recommendation.md")

[Monitoring Network Health with Network
Manager](https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/ "https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/")

[AWS Transit Gateway Network Manager for Industrial
IoT](https://pages.awscloud.com/Introduction-to-AWS-Transit-Gateway-Network-Manager_2019_1214-NET_OD.html?cr=%7Bcreative%7D&kw=%7Bkeyword%7D "https://pages.awscloud.com/Introduction-to-AWS-Transit-Gateway-Network-Manager_2019_1214-NET_OD.html?cr=%7Bcreative%7D&kw=%7Bkeyword%7D")
