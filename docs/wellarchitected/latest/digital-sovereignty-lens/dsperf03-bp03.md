# DSPERF03-BP03 Design networks that can operate independently of

foreign interference

In highly regulated industries, establishing network independence
from foreign interference is crucial for maintaining data
sovereignty, regulatory adherence, and operational resilience.

Organizations should design robust, autonomous network architectures
that minimize external exposure and protect sensitive data. This
improves business continuity during connectivity disruptions. It
also blocks unauthorized access that could lead to compliance
violations or operational disruptions.

**Desired outcome:** Network
architecture is self-contained and resilient, enforcing data
sovereignty while maintaining operational capabilities with minimal
external risks.

**Common anti-patterns:**

- Over-reliance on foreign CDNs, DNS providers, and third-party
  services without consideration of disruptions.
- Routing traffic containing sensitive data through
  foreign-controlled infrastructure without proper isolation or
  redundancy.
- Weak access controls and overly permissive security groups that
  don't properly distinguish or restrict foreign network sources
  or destinations.
- Insufficient monitoring, logging, and encryption of network
  traffic, particularly for identifying foreign interference
  attempts.
- Storing or transferring sensitive data through unapproved
  regions without proper encryption or compliance validation.

**Benefits of establishing this best
practice:**

- Control over network traffic flows while meeting domestic
  security requirements and data residency regulations.
- Strengthened security posture through network isolation and
  comprehensive visibility into potential interference.
- Reduced dependencies on foreign infrastructure while maintaining
  business operations during international disruptions.
- Traffic is routed through approved regions and services while
  isolating critical workloads from public networks.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design a multi-layered, independent network architecture using AWS
services.

Key implementation elements:

- Deploy localized DNS resolution and redundant connectivity
  paths aligned with compliance requirements
- Implement strict network segmentation to isolate critical
  workloads from untrusted traffic
- Configure comprehensive traffic inspection and monitoring to
  detect interferences
- Establish private connections using AWS Direct Connect and VPC
  peering
- Default to using private connections to avoid internet-based
  routing where possible

### Implementation steps

1. Configure DNS and network foundation using
   [Amazon Route 53](../../../Route%C2%A053/latest/DeveloperGuide/Welcome.md "../../../Route%C2%A053/latest/DeveloperGuide/Welcome.md") with private hosted zones, health checks,
   and failover routing. Design
   [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") architecture with separate security zones and
   data-sensitivity-based isolation for workload separation.
2. Implement connectivity and traffic management using
   [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") with redundant connections and private
   VIFs. Configure
   [VPC
   Peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"), and deploy
   [AWS Network Firewall](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md") for stateful inspection and custom
   traffic filtering rules.
3. Configure security controls and access management using
   [security
   groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md"),
   [network
   ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md"),
   [AWS WAF (Web Application Firewall)](../../../waf/latest/developerguide/waf-chapter.md "../../../waf/latest/developerguide/waf-chapter.md"), and
   [AWS Shield](../../../waf/latest/developerguide/shield-chapter.md "../../../waf/latest/developerguide/shield-chapter.md") for comprehensive protection.
4. Deploy transit architecture and private connectivity using
   [AWS Transit Gateway](../../../vpc/latest/tgw/what-is-transit-gateway.md "../../../vpc/latest/tgw/what-is-transit-gateway.md") with route tables and security
   domains for cross-region connectivity. Set up
   [AWS PrivateLink](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md") with service endpoints and interface
   endpoints for secure private access.
5. Implement network monitoring and threat detection using
   [VPC
   Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"),
   [Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"), and
   [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"). Configure
   [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") and
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") for automated threat detection and
   security insights.
6. Establish compliance and operational excellence using
   [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") rules for compliance monitoring and automated
   remediation.
7. Maintain comprehensive documentation including network
   diagrams, disaster recovery procedures, and continuous
   performance monitoring with security alerts and health
   checks.

## Resources

**Related best practices:**

- [PERF04-BP06
  Choose your workload's location based on network
  requirements](../performance-efficiency-pillar/perf_networking_choose_workload_location_network_requirements.md "../performance-efficiency-pillar/perf_networking_choose_workload_location_network_requirements.md")
- [DRHCOPS03-BP03
  Build redundant network connectivity](../data-residency-hybrid-cloud-services-lens/drhcops03-bp03.md "../data-residency-hybrid-cloud-services-lens/drhcops03-bp03.md")
- [ADVPERF01-BP01
  Design geographical affinity architecture with external
  entities (DSPs and SSPs)](../video-streaming-advertising-lens/advperf01-bp01.md "../video-streaming-advertising-lens/advperf01-bp01.md")

**Related documents:**

- [Network
  ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md")
- [Security
  Groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md")
- [VPC
  Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md")

**Related videos:**

- [Inside
  AWS Networking: Building a Secure, Reliable, and
  High-Performance Global Infrastructure](https://aws.amazon.com/awstv/watch/c37546e1558/ "https://aws.amazon.com/awstv/watch/c37546e1558/")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/")
- [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Direct Connect](https://aws.amazon.com/directconnect/ "https://aws.amazon.com/directconnect/")
- [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/")
- [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/")
- [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [AWS Shield](https://aws.amazon.com/shield/ "https://aws.amazon.com/shield/")
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/ "https://aws.amazon.com/transit-gateway/")
- [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/")
- [VPC
  Peering](https://aws.amazon.com/vpc/features/vpc-peering/ "https://aws.amazon.com/vpc/features/vpc-peering/")
