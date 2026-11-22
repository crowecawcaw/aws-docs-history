

# COST04-BP01 Define network and data transfer infrastructure costs

 Data transfer cost depends on the path traffic takes through your network, and shared network components spread those charges across many workloads. Document your network architecture and the transfer pricing that applies to each path so you can attribute cost to the workloads that drive it. 

 **Desired outcome:** 
+  You have documented the network paths your workload uses and the data transfer pricing that applies to each path. 
+  Your shared network components have a defined cost allocation method that attributes charges to the workloads that use them. 
+  You know which network components grow in cost as data transfer volume increases. 

 **Common anti-patterns:** 
+  Teams build network architecture without documenting data transfer paths or the pricing that applies to them. 
+  Organizations deploy shared network services without a mechanism to allocate their cost across teams or workloads. 
+  Cost reviews treat network charges as a single line item, with no visibility into which path or component drives them. 
+  Architecture decisions ignore how transfer cost scales as the workload grows. 

 **Benefits of establishing this best practice:** 
+  Network cost becomes attributable to the workloads that generate it, at both the workload and organization levels. 
+  Shared component charges are distributed fairly instead of landing on a single owning team. 
+  Architecture reviews can compare connectivity options because the cost of each path is documented. 
+  Cost forecasts improve because you know which components scale with data transfer volume. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Traffic that stays inside one Availability Zone over private addresses usually incurs no data transfer charge. Traffic between Availability Zones or Regions carries a per-gigabyte charge in each direction, and traffic that leaves to the internet is priced separately. Map the paths your workload uses and how much each path costs before you try to control network cost. 

 In a multi-account organization, an infrastructure or networking team often owns the shared connectivity layer. Transit gateways, private connectivity circuits, and inspection appliances serve many workloads at once. Without an allocation method, these charges accumulate on the owning account and no workload sees the cost it creates. Decide early how you split shared network cost, whether by data processed, by attachment, or by another metric that maps usage back to the teams that drive it. 

 Some components charge mainly for the data that flows through them, so their cost tracks workload growth. A component that processes egress traffic, a managed address translation service, or a traffic inspection layer bills per gigabyte on top of any hourly rate. A design that looks inexpensive at proof-of-concept volume can become a major line item at production scale. Identify these usage-driven components separately from fixed-rate ones. 

 Each AWS capability that moves data has its own pricing dimensions. Inter-VPC and hybrid connectivity through [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) and [AWS Direct Connect](https://aws.amazon.com/directconnect/) charge for attachments or ports and for data processed. Edge and delivery services such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) can lower egress cost by serving traffic closer to users. Supporting services, including [Amazon Route 53](https://aws.amazon.com/route53/), [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and traffic inspection, also carry charges that grow with request or log volume. Some transfer services use tiered pricing, so the per-gigabyte rate changes with volume. Document the pricing dimension for each capability your workload depends on. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory workload-specific and shared components:** Map the path your workload traffic follows, and mark each component as workload-specific or shared. For shared components, record the owning team and the allocation method you will use to attribute their cost. This inventory is the basis for every pricing decision that follows. 

1.  **Document inter-VPC connectivity:** Identify how your workload reaches resources in other VPCs and [how that traffic is routed](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html). Record the per-attachment and per-gigabyte charges for the connectivity method you choose, such as a transit gateway or VPC peering. 

1.  **Document hybrid and private connectivity:** Determine how your workload reaches on-premises resources and [how traffic is routed to your network](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html). Note the port-hour and data transfer charges for the AWS Direct Connect or VPN connection you use. 

1.  **Document internet-bound connectivity:** Record how outbound and inbound internet traffic is routed, through an internet gateway, a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html), or a load balancer. Capture whether edge services such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/) or [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) serve any of this traffic, and note their transfer pricing. 

1.  **Document supporting network services:** Capture the charges for DNS resolution with [Amazon Route 53](https://aws.amazon.com/route53/), for flow and access logging with [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and for any traffic inspection or firewall layer. These services bill per request, per gigabyte, or per log, so their cost scales with workload activity. 

1.  **Record the pricing dimension and scaling behavior of each component:** For every component in your inventory, note whether it charges a fixed rate, a usage rate, or both, and whether it uses tiered pricing. Flag the components whose cost grows with data transfer volume so they receive priority during modeling and optimization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST04-BP02 Perform data transfer modeling](cost04-bp02.md) 
+  [COST04-BP03 Optimize services to reduce data transfer costs](cost04-bp03.md) 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 
+  [COST06-BP04 Consider using shared resources](cost06-bp04.md) 

 **Related documents:** 
+  [Building a scalable and secure multi-VPC network infrastructure - VPC-to-VPC connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.html) 
+  [Building a scalable and secure multi-VPC network infrastructure - Hybrid connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html) 
+  [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) 
+  [Amazon Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) 
+  [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) 

 **Related services:** 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 