

# FND07-BP02 Implement centralized network protection controls

 Centralized network protection controls apply consistent traffic filtering, inspection, threat prevention, and security monitoring across an organization's network. Standard controls at strategic inspection points detect and prevent threats, meet compliance requirements, and protect workloads from network-based attacks without each team rebuilding the same controls. 

 **Desired outcome:** 
+  You have centralized network protection controls providing consistent traffic filtering, inspection, and threat prevention across all environments. 
+  You have automated mechanisms that enforce network security policies regardless of workload deployment location, covering internet ingress and egress, east-west traffic (between workloads inside the network), and shared services communication. 
+  You apply protection controls at strategic inspection points so that traffic between networks is filtered and inspected according to defined policy before it reaches workloads. 
+  Security teams efficiently maintain controls while providing workload teams with self-service capabilities and automated tooling. 

 **Common anti-patterns:** 
+  Using overly permissive or overly complex traffic filtering rules, with poor documentation and no regular review of allowed traffic patterns. 
+  Applying inconsistent security controls across accounts and environments, leading to security gaps and increased management overhead. 
+  Relying on perimeter-based protection while ignoring east-west (inter-VPC and intra-VPC) traffic inspection. 
+  Depending on manual security processes that do not scale and lack a structured exception review for legitimate business needs. 
+  Deploying controls without detailed logging and monitoring, reducing visibility into security events and anomalous traffic. 
+  Applying protection controls unevenly across inspection points, leaving gaps where traffic bypasses filtering and inspection. 

 **Benefits of establishing this best practice:** 
+  Centralized policy definition and enforcement reduce duplicated rule sets and make protection controls more straightforward to monitor, troubleshoot, and evolve. 
+  Layered controls at centralized inspection points create multiple security barriers against both external and internal threats. 
+  Centralized controls verify that all traffic is filtered and inspected according to defined policy, making security part of the infrastructure rather than an add-on. 
+  Central routing and access controls confine communication to approved and inspected pathways. 
+  Centralized telemetry of network traffic and security events supports monitoring, threat detection, and incident response. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Centralized network protection controls build on an existing connectivity foundation. With a hub-and-spoke topology in place (either using [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) or [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) in a dedicated Network Services account), you can place protection controls at strategic inspection points that all traffic flows through, as shown in Figure 1. This gives security teams predictable places to enforce policy, collect telemetry, and respond to incidents. <a name="fnd07-bp02-fig1"></a>

![Network diagram of a hub-and-spoke topology where spoke VPCs connect through a central hub that hosts shared protection and inspection controls.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/hub-and-spoke.png)

*Hub-and-spoke network with centralized protection controls*


 Routing is a security control. Route tables enforce least privilege at the network layer by providing paths only between networks that must communicate. Omit routes between workloads that have no interdependency (for example, between two unrelated business unit VPCs) to close lateral movement paths before any firewall rule runs. 

 [AWS Network Firewall](https://aws.amazon.com/network-firewall/) provides stateful filtering and deep packet inspection with protocol, port, domain, URL, and custom rule filtering. It inspects north-south traffic (entering or leaving the network) as well as east-west traffic (moving between workloads inside the network). Deploy Network Firewall in a dedicated inspection VPC attached to the hub. This lets firewall capacity scale independently of Transit Gateway capacity and keeps the inspection path off the critical data plane. [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) extends these controls across accounts by managing policies centrally. The [centralized network security patterns](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html) in the multi-VPC network infrastructure whitepaper cover alternative inspection models. 

 Complement network-layer inspection with application-layer controls. [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) catches threats at name resolution, [AWS WAF](https://aws.amazon.com/waf/) filters HTTP traffic at web application entry points, and [AWS Shield Advanced](https://aws.amazon.com/shield/) defends against distributed denial of service (DDoS) attacks at the edge. This strategy forms an overlapping defense, an improvement over any single control. 

 [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) aggregates security findings, [Amazon Security Lake](https://aws.amazon.com/security-lake/) supports longer-term storage and analytics, and [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) plus [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) provide the audit trails needed for investigation. Without this telemetry, centralized controls still enforce policy but security teams cannot see how they perform. Use [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to verify network paths between resources and [AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) to identify unintended network access, so security teams can confirm segmentation and least-privilege networking. [AWS Shield Network Security Director](https://aws.amazon.com/shield/) discovers compute, networking, and network security resources across the organization and evaluates their configurations against AWS best practices and threat intelligence. Enable it through an [AWS Organizations Network Security Director policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html) to give a delegated administrator centralized visibility into findings and remediation recommendations. Accounts that join the organization inherit coverage automatically. 

 Review policies regularly, run structured exception processes, and automate enforcement to keep controls consistent as threats and workloads evolve. The [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) provides deeper guidance on secure network architecture and account structure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Confirm the connectivity hub is in place:** Centralized protection assumes a hub-and-spoke foundation, either using [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) or [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) in a dedicated Network Services account with VPC attachments and hybrid connections (see [Figure 1](#fnd07-bp02-fig1)). Protection controls are applied on top of this foundation, so verify the hub, its attachments, and hybrid paths exist before continuing. 

1.  **Use routing to enforce segmentation:** Define how traffic flows between connected VPCs and external connections using [Transit Gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html) or [Cloud WAN network policies](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policies-json.html). Provide routes only between networks that must communicate, and leave out routes between networks that must remain isolated. This applies least privilege at the network layer before any firewall rule runs. 

1.  **Define security requirements and trust boundaries:** Document the allowed traffic patterns, regulatory requirements, and data sensitivity classifications that shape your filtering policies. Map data sensitivity levels to network segments and define explicit security zones and trust boundaries. These requirements drive the rules deployed in later steps. 

1.  **Select an inspection model:** Compare centralized and distributed inspection using the [centralized network security patterns](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-network-security-for-vpc-to-vpc-and-on-premises-to-vpc-traffic.html) in the multi-VPC network infrastructure whitepaper. Weigh capacity needs, high availability, multi-Region protection, and hybrid traffic patterns. Pick inspection points that can cover north-south and east-west flows and that match the team's operational capacity. 

1.  **Implement network layer protection:** Deploy [AWS Network Firewall](https://aws.amazon.com/network-firewall/) with base traffic filtering policies, and add protocol, port, domain, and URL filtering rules aligned with the requirements defined earlier. Use [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) to define policy hierarchy and inheritance across accounts, configure automatic enforcement, and set up non-compliance detection and remediation. Establish firewall policy management processes covering change management with justification, exception approvals, and a recurring rule review (at least quarterly) to remove stale rules, tighten overly permissive ones, and add coverage for new threats. 

1.  **Implement DNS-level protection:** Deploy [Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) and define a domain filtering strategy with allow lists, deny lists, and rule groups that reflect your security requirements. Associate rule groups with the appropriate VPCs, enable [DNS query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs.html), and configure alerting for blocked domains. Set up a feedback and update process so rules stay current as applications and threats evolve. 

1.  **Deploy application layer protection:** Deploy [AWS WAF](https://aws.amazon.com/waf/) in front of your web-facing services and configure [managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html) for common attack patterns, along with custom rules for application-specific requirements. Use additional rule sets from [AWS WAF partners in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security/waf-managed-rules) where specialized protections are needed. 

1.  **Turn on DDoS protection for critical resources:** Enable [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) to protect critical resources that require advanced DDoS defense, all-day access to the AWS Shield Response Team, and cost protection for scaling-related charges incurred during an attack. 

1.  **Centralize security telemetry:** Enable [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) across accounts and route findings into [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) for aggregation. Use [Amazon Security Lake](https://aws.amazon.com/security-lake/) for longer-term security data storage and advanced analytics. Configure alerting on policy violations and anomalous traffic patterns so the signal from centralized controls reaches the right responders. 

1.  **Validate and continuously verify network security posture:** Use [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to test connectivity paths and confirm segmentation controls are working as designed. Use [AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) to find unintended network access and verify that least-privilege networking is maintained as the environment evolves. Enable [AWS Shield Network Security Director](https://aws.amazon.com/shield/) through an [AWS Organizations Network Security Director policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html) to give a delegated administrator centralized visibility into network topology and security findings across member accounts, with automatic coverage for accounts that join the organization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md) 
+  [FND07-BP03 Establish centralized DNS management](fnd07-bp03.md) 
+  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md) 
+  [FND05-BP07 Implement threat detection mechanisms](fnd05-bp07.md) 

 **Related documents:** 
+  [Network Connectivity capability](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-connectivity-capability.html) 
+  [Network designing and planning](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-designing-and-planning.html) 
+  [How to automate rule management for AWS Network Firewall](https://aws.amazon.com/blogs/security/how-to-automate-rule-management-for-aws-network-firewall/) 
+  [Discover the benefits of AWS WAF advanced rate-based rules](https://aws.amazon.com/blogs/security/discover-the-benefits-of-aws-waf-advanced-rate-based-rules/) 
+  [What is Amazon VPC Transit Gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) 
+  [Amazon VPC Transit Gateway design best practices](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html) 
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) 
+  [AWS Security Reference Architecture - Network Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html) 
+  [What is VPC Reachability Analyzer?](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) 
+  [Getting started with AWS Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Design well-architected networks on AWS (NET202)](https://www.youtube.com/watch?v=Pd5p-fzwsLA) 
+  [AWS re:Inforce 2023 - Policy and Suricata compatible rule creation for AWS Network Firewall (NIS308)](https://www.youtube.com/watch?v=67pVOv3lPlk) 
+  [AWS re:Invent 2023 - Automating AWS WAF: Pioneering future security (SEC206)](https://www.youtube.com/watch?v=GqAh2EfMqPU) 

 **Related examples:** 
+  [Migration to AWS Cloud WAN multi-Region inspection using service insertion](https://aws.amazon.com/blogs/networking-and-content-delivery/migration-to-aws-cloud-wan-multi-region-inspection-using-service-insertion/) 
+  [Guidance for Building your Enterprise WAN on AWS](https://docs.aws.amazon.com/solutions/building-your-enterprise-wan-on-aws/) 

 **Related workshops:** 
+  [AWS Networking Workshop](https://catalog.workshops.aws/networking/en-US) 