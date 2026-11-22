

# FND07-BP01 Define your network and connectivity strategy and centralized resources

 An enterprise network and connectivity strategy defines network topology, connectivity patterns, and centralized network services. Standard approaches for internet access, external access, network segmentation, and service access create secure communication between workloads, consistent connectivity to on-premises resources, and predictable access to shared services. With these standards in place, workload teams can move quickly and stay within enterprise security and operational boundaries. 

 **Desired outcome:** 
+  Your organization has a well-documented enterprise network architecture with clear patterns and standards for workload teams, including guidance on VPC design, IP management, subnet structuring, and scalable routing. 
+  You have established standardized approaches for network connectivity covering hybrid, internet, cross-account, and service-to-service paths. 
+  Your centralized network services and shared resources are consumable through automated provisioning, with documented processes for connectivity requests and exception handling. 
+  Your workload teams have access to self-service tools, infrastructure-as-code modules, and documentation to implement networking consistently with enterprise standards. 
+  Your network strategy accommodates workload growth and continues to provide availability and performance as the environment scales. 

 **Common anti-patterns:** 
+  Creating monolithic network architectures that lack segmentation and flexibility for different workload requirements. 
+  Relying on manual, non-scalable processes for network provisioning and IP address management, including overlapping IP ranges across VPCs, on-premises networks, and other cloud providers. 
+  Implementing distributed internet access without consistent security controls, monitoring, or inspection capabilities. 
+  Creating bottlenecks by requiring central team involvement for routine network changes and access requests, with no self-service tooling for workload teams. 
+  Failing to plan CIDR blocks and IP address space for growth, leading to sizing issues, conflicts, and painful renumbering. 
+  Overlooking hybrid connectivity requirements and lacking clear processes for reviewing and updating network standards as requirements evolve. 

 **Benefits of establishing this best practice:** 
+  Clear patterns and automated provisioning reduce manual overhead and accelerate delivery for workload teams. 
+  A well-designed topology supports consistent connectivity, high availability, and effective disaster recovery across Regions and accounts. 
+  Standardized patterns and centralized services reduce duplication and make efficient use of resources. 
+  A cohesive network architecture grows with the organization, accommodating new workloads without major redesigns. 
+  Fine-grained access controls and segmentation limit resource-to-resource communication to what is necessary, reducing the impact scope of misconfigurations and unintended access. 
+  Multiple layers of network controls and standardized security patterns create overlapping defenses that protect against a variety of threats. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In your network strategy, centralizing requires careful attention to make the network cohesive. Centralize the parts of your network where duplication is expensive or dangerous (such as connectivity hubs, inspection points, DNS, and IP address management), and standardize the patterns workload teams use to build their own networks. 

 An [Amazon Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) is a logically isolated network inside an AWS account, and organizations typically end up with many VPCs because accounts are the strongest isolation boundary AWS provides. Each workload, environment, or business unit often has its own account with its own VPCs. Multiply that across Regions and the result is a network of tens or hundreds of VPCs that still need predictable connectivity to each other, to on-premises networks, to partner networks, and to the internet. 

 The core decision is between distributed and centralized approaches to how VPCs and accounts are connected. A distributed approach gives workload teams autonomy but tends to produce inconsistent security postures and duplicated services. A centralized hub-and-spoke model using [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) trades some team autonomy for consistent routing, centralized inspection, and lower troubleshooting overhead. How VPCs are organized (by business unit, environment, or application) determines scope of impact, cost allocation, and the complexity of the routing layer above them. 

 [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) provides dedicated bandwidth and predictable latency for heavy or sensitive traffic. [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) is faster to set up and often fits smaller environments or a backup path. For any given workload, aspects such as bandwidth, latency, cost, route propagation, filtering, Network Address Translation (NAT) handling, monitoring, and disaster recovery determine the right fit. Most mature environments use both in layered combinations. 

 As an alternative to Transit Gateway, especially for multi-Region environments, consider [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/). Cloud WAN is a policy-driven networking service with built-in automation and network segmentation that supports centralized inspection models and multi-Region traffic management with less configuration overhead. 

 Prefer a centralized egress model. Route traffic through an inspection VPC fronted by [AWS Network Firewall](https://aws.amazon.com/network-firewall/) or a third-party appliance. From this single set of choke points, apply policy, logging, and threat inspection uniformly. A distributed model keeps traffic closer to each workload. This improves performance and reduces single points of failure, but multiplies the places where security controls must stay consistent. Choose distributed only when these gains outweigh the consistency cost. 

 For service connectivity (how workloads reach AWS service APIs, shared services, and third-party SaaS), use private paths through [AWS PrivateLink](https://aws.amazon.com/privatelink/) and [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) rather than the public internet. Standard patterns for service exposure and consumption reduce per-team design work and keep cross-account access predictable. 

 IP address management is where network strategies most often break under growth. Growth is consistently underestimated, acquisitions reshape the address plan in ways that are hard to undo, and private network connections to partners or other cloud providers often fail at the IP planning stage. [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) provides centralized allocation, automated tracking, and overlap prevention. Pair it with a Classless Inter-Domain Routing (CIDR) allocation strategy. Reserve capacity for future Regions, new business units, and hybrid connectivity to reduce the risk of later renumbering. Network access controls (security groups, network ACLs) must align with the segmentation strategy. Deliver them as reusable patterns rather than built manually per workload. 

 The network foundation pays off only when workload teams can consume it efficiently. That means published patterns, infrastructure-as-code modules, automated provisioning, clear exception processes, and regular reviews as requirements evolve. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define your network segmentation strategy:** Determine VPC organization patterns (by business unit, environment, and application). Establish VPC CIDR ranges, subnet patterns, and network layers (public, private with internet access, private isolated). Define network naming and tagging standards. 

1.  **Establish a network connectivity hub:** If a centralized network strategy is the right fit, use [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) as a central connectivity point. Define routing controls and traffic flow patterns. Create a process for adding new VPC attachments. 

1.  **Implement hybrid connectivity:** Evaluate [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) against [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html). Use redundant connections for high availability with backup paths. Plan bandwidth and capacity so your connectivity option meets organizational needs. 

1.  **Define your internet connectivity strategy:** Decide whether to use centralized or distributed internet access. Use inspection VPCs if you plan to use a centralized model. For distributed models, standardize on [NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) with per-Availability Zone (AZ) redundancy so a single zone failure does not take internet egress offline. Plan for scaling and high availability of internet access. 

1.  **Establish service connectivity controls:** Use private connectivity for AWS services through [AWS PrivateLink](https://aws.amazon.com/privatelink/) and [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html), and define a strategy for external service access. 

1.  **Understand VPC and subnet CIDR constraints:** Before allocating address space, become familiar with the limits that shape what is possible. The first four IP addresses and the last IP address in each subnet CIDR block are reserved. The initial VPC CIDR block cannot be changed or deleted, but you can add more non-overlapping CIDR blocks. Subnet IPv4 CIDRs cannot be changed, but IPv6 CIDRs can. The largest VPC CIDR block is a /16 (65,536 addresses), and the smallest is a /28 (16 addresses). See [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) and [subnet sizing](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html) for the full set of constraints. 

1.  **Plan private IP address ranges:** Follow [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) guidelines for private address space in each VPC and reserve IP space for more than one VPC per Region. Within a VPC, reserve space for multiple subnets across multiple Availability Zones, and leave unused CIDR block space for future expansion. Plan IP space for transient [Amazon EC2](https://aws.amazon.com/ec2/) fleets ([Spot Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon Redshift](https://aws.amazon.com/redshift/)) and Kubernetes clusters such as [Amazon EKS](https://aws.amazon.com/eks/), where each pod is assigned a routable address from the VPC CIDR block by default. Check other connected networks (VPCs, on-premises, other cloud providers) to make sure that private IP ranges do not overlap across any networks that must communicate, because overlaps cause routing ambiguity that is hard to unwind later. 

1.  **Deploy IP address management and codify your CIDR allocation strategy:** With the constraints understood and ranges planned, deploy [Amazon VPC IP Address Manager (IPAM)](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) or an equivalent system as the authoritative source for allocation. Codify the allocation strategy from the previous step, including reserves for future Regions, business units, and hybrid connectivity, as IPAM pools. Establish a process for requesting IP ranges and automate CIDR assignments to plan for growth. 

1.  **Discover existing IP usage and resolve overlaps:** For environments that already have VPCs in place before IPAM is deployed, use [IPAM resource discovery](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with-view.html) or service API operations to capture current CIDR consumption, identify overlapping ranges, and calculate spare capacity. For overlapping ranges that need to communicate, use techniques such as [private NAT Gateway](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/private-nat-gateway.html) or [AWS PrivateLink](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/aws-privatelink.html) so traffic can reach its destination without renumbering networks. 

1.  **Create network security controls:** Define standard [security group](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) patterns for common workload archetypes (web tier, app tier, database tier) and publish them as reusable infrastructure-as-code modules. Establish [network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) standards for subnet-level controls, and define how centralized traffic flow controls (such as inspection through [AWS Network Firewall](https://aws.amazon.com/network-firewall/)) integrate with workload-level controls. Document how to combine these layers to achieve defense in depth without duplicating enforcement. 

1.  **Publish network architecture documentation and review processes:** Publish a pattern library covering the common VPC layouts, connectivity models, and security patterns teams are expected to use. Define feedback, review, and exception-handling processes so workload teams can request changes without blocking, and review the standards on a regular cadence as requirements evolve. Use a shared documentation system or internal portal to keep patterns, [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or [AWS CDK](https://aws.amazon.com/cdk/) modules, and guidance findable. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND07-BP02 Implement centralized network protection controls](fnd07-bp02.md) 
+  [FND07-BP03 Establish centralized DNS management](fnd07-bp03.md) 
+  [FND04-BP05 Establish service quota management](fnd04-bp05.md) 
+  [FND04-BP07 Establish cross-Region replication and failover capabilities](fnd04-bp07.md) 
+  [SEC05-BP01 Create network layers](sec05-bp01.md) 
+  [SEC05-BP02 Control traffic flow within your network layers](sec05-bp02.md) 

 **Related documents:** 
+  [Network Connectivity capability](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-connectivity-capability.html) 
+  [Network designing and planning](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/network-designing-and-planning.html) 
+  [AWS Well-Architected Framework - Security Pillar - Protecting networks](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec05.html) 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) 
+  [Amazon Virtual Private Cloud Connectivity Options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) 
+  [Addressing private IPv4 exhaustion with AWS Cloud WAN service insertion](https://aws.amazon.com/blogs/networking-and-content-delivery/addressing-private-ipv4-exhaustion-with-aws-cloud-wan-service-insertion/) 
+  [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) 
+  [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) 
+  [IPv6 on AWS](https://aws.amazon.com/vpc/ipv6/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - Design well-architected networks on AWS (NET202)](https://www.youtube.com/watch?v=Pd5p-fzwsLA) 
+  [AWS re:Invent 2023 - Ready for what's next? Designing networks for growth and flexibility (NET310)](https://www.youtube.com/watch?v=FkWOhTZSfdA) 
+  [AWS re:Invent 2024 - Amazon VPC: Advanced design and what's new (NET301)](https://www.youtube.com/watch?v=7qaSfmnFiI0) 
+  [AWS re:Invent 2023 - AWS networking foundations (NTA307)](https://www.youtube.com/watch?v=8nNurTFy-h4) 