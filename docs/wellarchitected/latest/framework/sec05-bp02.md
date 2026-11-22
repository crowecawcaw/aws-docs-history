

# SEC05-BP02 Control traffic flow within your network layers

 Within each network layer, segment traffic so that you permit only the flows required by your workload. Start with traffic between your environment and the internet or other external systems, then control the flows between internal components. Apply least privilege to network paths to limit how far an incident can spread. 

 **Desired outcome:** 
+  You permit only the flows your components need to reach their clients, their dependencies, and each other. 
+  Your controls cover both ingress and egress at network boundaries and within each layer. 
+  Your design accounts for public compared to private paths, data classification, regional requirements, and protocol choices. 
+  You favor point-to-point connections over broad network peering wherever practical. 

 **Common anti-patterns:** 
+  Teams control traffic only at the perimeter of a network layer and leave internal flows unrestricted. 
+  Teams assume that any traffic already inside a layer is authenticated and authorized. 
+  Teams apply controls to ingress traffic or egress traffic, but not both. 
+  Teams rely on network controls alone to authenticate and authorize traffic. 

 **Benefits of establishing this best practice:** 
+  Restricting internal flows reduces the risk of unauthorized movement between components. 
+  Fine-grained controls add a layer of authorization on top of application and identity controls. 
+  Limiting reachable paths narrows the scope of impact when an incident occurs. 
+  Explicit, documented flows make anomalies easier to detect and investigate. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Network layers set the outer boundaries around groups of components. Traffic control is what you do inside and between those boundaries to enforce least privilege on individual flows. A boundary alone does not stop lateral movement. If every component in a layer can reach every other, unauthorized access to one component gives access to all of them. Controlling flows closes those paths so that a component can reach only what it requires. 

 Inventory the flows your workload needs, such as which party initiates each connection, which ports and protocols they use, and which layers they cross. Capture these requirements at the boundaries and within each layer, and choose protocols that meet your protection needs, such as HTTPS instead of HTTP. Without this inventory, you can't write precise rules, and broad allowances undermine segmentation. 

 Combine controls at different network levels for defense in depth. *Security groups* are a strong default because they attach to resources with an elastic network interface. Examples include Amazon EC2 instances, Amazon ECS tasks, Amazon EKS pods, and Amazon RDS databases. A security group can reference another security group by its identifier, so rules stay stable as resources come and go. Security groups filter both inbound and outbound traffic. Route tables and network ACLs complement them at the subnet level. 

 Cross-VPC connectivity is a design choice with cost and blast-radius consequences. VPC peering and [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) route between the full IP ranges of the connected networks, which exposes more than a single flow often requires. When a workload needs only specific components to communicate across VPCs, a point-to-point connection with [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) exposes just the producer service to the consumer without peering the networks. PrivateLink adds data processing and load balancing costs in return for that tighter exposure. 

 Controlling which domains your resources can reach is a separate concern from controlling component-to-component flows. Depending on the DHCP configuration of your VPC, use the [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) to allow or deny traffic based on domain lists associated with your VPC. When you need inspection deeper than domain filtering, [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) evaluates individual packets with stateless or stateful rules. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) filters inbound web traffic to your public endpoints (for more detail, see SEC05-BP03). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory required data flows:** Identify the connections your components need, recording the initiating party, ports, protocols, and the layers each flow crosses. Use this inventory as the basis for every rule you write. 

1.  **Apply layered controls for ingress and egress:** Use security groups and route tables to permit only the inventoried flows, covering both inbound and outbound directions. Reference security groups by identifier where possible so rules remain stable as resources change. 

1.  **Use point-to-point connectivity for cross-VPC flows:** Where only specific components must communicate across VPCs, use [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) instead of peering the full networks. Designate the producer and consumer, deploy a compatible load balancer for the producer, turn on PrivateLink, and accept the consumer connection request. 

1.  **Add firewalls for domain and packet control:** Use the [Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html), [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html), and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) for fine-grained control over traffic in, out, and across your VPCs. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC05-BP01 Create network layers](sec05-bp01.md) 
+  [SEC05-BP03 Implement inspection-based protection](sec05-bp03.md) 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 
+  [REL03-BP01 Choose how to segment your workload](rel03-bp01.md) 

 **Related documents:** 
+  [Security best practices for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) 
+  [Guidance for Network Security on AWS](https://docs.aws.amazon.com/solutions/network-security-on-aws/) 
+  [Secure your VPC's outbound network traffic in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-outbound-network-traffic/introduction.html) 
+  [Enhanced security with DMZ architecture using Amazon VPC Block Public Access](https://aws.amazon.com/blogs/networking-and-content-delivery/enhanced-security-with-dmz-architecture-using-amazon-vpc-block-public-access/) 

 **Related videos:** 
+  [How do I configure and manage Amazon VPC security groups and network ACLs?](https://www.youtube.com/watch?v=z5VhZ8lva6A) 
+  [AWS re:Inforce 2025 - AWS Network Firewall: Latest features and deployment options (NIS201-NEW)](https://www.youtube.com/watch?v=nauTd9uOtsU) 
+  [AWS re:Invent 2025 - A day in the life of an AWS WAF administrator (NET317)](https://www.youtube.com/watch?v=E_xm8W_BEFk) 

 **Related tools:** 
+  [AWS WAF](https://aws.amazon.com/waf/) 
+  [AWS Network Firewall](https://aws.amazon.com/network-firewall/) 
+  [Amazon Route 53 Resolver DNS Firewall](https://aws.amazon.com/route53/resolver-dns-firewall/) 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 