

# ADVREL05-BP03 Deploy partner-facing bid gateways in multiple AWS Regions

 A single-Region gateway deployment means all bid traffic terminates in one Region. If that Region becomes unavailable, your exchange partners can't reach your gateways and bid connectivity is lost. To survive a Regional failure, deploy RTB Fabric gateways in at least two Regions. 

 **Desired outcome:** 
+  RTB Fabric gateways are deployed in at least two AWS Regions, selected to minimize round-trip latency to exchange partners. 
+  Exchange partners can route to either Region through an agreed failover architecture, with no manual reconfiguration required at failover time. 
+  Each Region has independent Service Quota allocations and sufficient IPv4 capacity to absorb the other Region's full traffic during failover. 

 **Common anti-patterns:** 
+  Terminating all bid traffic in a single Region, so a regional outage severs partner connectivity entirely. 
+  Choosing a failover architecture without coordinating with exchange partners, so partners can't actually route to the secondary Region during an event. 
+  Configuration drift between Regions because gateway environments are built by hand instead of infrastructure as code. 
+  Secondary-Region subnets sized only for steady-state share, which causes IPv4 exhaustion when that Region must absorb full failover traffic. 

 **Benefits of establishing this best practice:** 
+  Bid connectivity survives a full regional outage through gateways in the surviving Region. 
+  A pre-agreed partner failover pattern enables predictable, low-friction regional failover. 
+  Infrastructure as code keeps the Regions identical, limiting drift that would undermine failover. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Regional resilience and zonal resilience address different failures. Spreading gateways across zones protects against losing part of one Region, but does nothing when the entire Region becomes unreachable to your partners. A second Region gives partner traffic another endpoint to reach. This practice addresses how an exchange partner actually reaches the other Region when the first Region is gone. 

 Failover patterns differ by who performs the work: the partner, an infrastructure layer, or DNS resolution. Choose the pattern your exchange partners can support, considering the required failover speed and where you want operational responsibility to reside. 

 Manually configured gateway environments drift apart, and unnoticed differences surface during a failover you can't test on demand. Describe both Regions as code to keep them identical. 

 Quotas and capacity are also per-Region. A limit raised in one Region does nothing for another, and the second Region can reach a limit the first never approached. Address capacity has the same problem: a normally-sized Region can't absorb the other Region's full traffic during a failover without headroom provisioned ahead of time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy gateways in at least two Regions:** Deploy RTB Fabric gateways in ≥2 AWS Regions, selecting Regions that minimize round-trip latency to your exchange partners. 

1.  **Choose and agree a partner failover architecture:** Register gateway endpoints in both Regions with your exchange partners, selecting the appropriate pattern:- **Option A - Partner-Managed Failover:** Partners register static endpoints in both Regions (for example, gateway-us-east-1.example.com and gateway-us-west-2.example.com) and build their own client-side health-check and failover logic, giving maximum partner control at the cost of higher integration complexity. 
+  **Option B - AWS Global Accelerator with static anycast IPs:** Provision Global Accelerator in front of your regional gateways to provide static anycast IPs that automatically route to healthy endpoints based on health checks, letting partners use the static IPs without their own failover logic for sub-second failover with simplified integration, which incurs additional cost (a fixed \~$0.025/hour accelerator fee, public IPv4 address charges for the two static IPs, and premium data transfer) but removes DNS caching delays. 
+  **Option C - Route 53 health-checked DNS:** Create a Route 53 hosted zone with health checks on regional gateways, so partners use a single DNS name (for example, gateway.example.com) that resolves to healthy Regions based on routing policy. This is most cost-effective but introduces DNS TTL-dependent failover delays of approximately 70 seconds at the most aggressive configuration (fast health checks, threshold of 1, 60-second TTL) and commonly 2 or more minutes in practice because resolvers and clients cache DNS beyond the stated TTL, and it requires partners to use DNS names rather than static IPs. 

1.  **Coordinate with partners in advance:** Confirm partners can support your chosen failover architecture, understand endpoint registration requirements, and configure their systems to route to either Region based on the selected pattern. 

1.  **Limit configuration drift with infrastructure as code:** Maintain identical VPC, subnet, and security group configurations across Regions using CloudFormation StackSets or Terraform workspaces. 

1.  **Allocate per-Region quotas and capacity:** Each Region has independent Service Quota allocations. Request Multi-AZ gateway quotas in every active Region separately. Provision sufficient IPv4 subnet capacity in each Region to support full gateway scaling without IP exhaustion, even if one Region must absorb traffic from the other during failover. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements](advrel03-bp02.md) 
+  [ADVREL05-BP01 Deploy partner-facing bid gateways across multiple Availability Zones](advrel05-bp01.md) 

 **Related documents:** 
+  [AWS RTB Fabric - Setting Up](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/setting-up-aws-rtb-service.html) 
+  [AWS RTB Fabric - Service Quotas](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/rtb-fabric-quotas.html) 
+  [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 