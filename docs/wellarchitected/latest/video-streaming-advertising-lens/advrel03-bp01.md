

# ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators
<a name="advrel03-bp01"></a>

 Deploy compute resources across multiple Availability Zones and Regions to improve application resilience. Implement zone-aware architectures to optimize performance and manage costs, and focus on intra-AZ communication and load balancing configurations. 

 **Desired outcome:** 
+  Compute resources are distributed across multiple Availability Zones behind zone-aware load balancers. 
+  Availability Zone-level failures trigger automatic traffic redistribution without manual intervention. 
+  Zone-aware load balancing minimizes cross-AZ data transfer costs for intra-cluster communication. 

 **Common anti-patterns:** 
+  Distributing compute across Availability Zones but using default cross-zone load balancing settings, which routes all traffic evenly across Availability Zones and adds unnecessary cross-AZ transfer costs for stateful advertising services. 
+  Not implementing pod anti-affinity rules in EKS, so all replicas of a critical bidding service can end up in a single Availability Zone. 

 **Benefits of establishing this best practice:** 
+  Availability Zone-level failures are absorbed automatically without dropped bids. 
+  Cross-AZ data transfer costs are minimized through zone-aware communication. 
+  Capacity scales horizontally across Availability Zones to absorb uneven load distribution. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 An exchange gives a bidder roughly 100 milliseconds end to end. Network transit to and from the exchange consumes part of that, so the decisioning logic often has single-digit milliseconds to spend. Multi-AZ design for that bid path answers a different question than it does for a typical web application. 

 Every cross-AZ hop inside the path adds roughly a millisecond one way at best. AWS Availability Zone latency guidance puts the median at about 1.5 milliseconds one way. A path that crosses zone boundaries several times can spend single-digit milliseconds on network transit alone. That amount is negligible for a management console and meaningful for an auction. 

 AWS bills cross-AZ data transfer per gigabyte in each direction. Without Availability Zone affinity, a bidder handling billions of requests per day crosses Availability Zone boundaries billions of times. A design decision that is invisible at normal traffic levels becomes one of the larger infrastructure costs at RTB scale. 

 Place complete, independently functional bidding capacity in every zone. The loss of a zone then removes only a fraction of the fleet. Each request enters a zone, is answered in that zone, and leaves. Availability Zone affinity in load balancing enforces that path. Spreading an individual request across zones buys no additional resilience, because whole replicas already exist elsewhere. It also pays the latency and transfer cost on every auction. 

 Services behind an ALB, such as campaign management consoles, reporting APIs, or creative upload endpoints, have no auction clock and orders of magnitude less volume. The affinity rule is scoped to deadline-bound, high-volume traffic, so it inverts for these services. Uneven load is the primary risk for them. 

 Turning cross-zone off makes each load balancer node serve only the targets in its own zone. Unequal target counts after a scale-in event then translate into unequal per-target load. At low request volume, the statistical variance across a small number of requests concentrates that load further. Turning it off also invalidates any target stickiness on the group, which ALB doesn't support when cross-zone load balancing is off. For those workloads, even distribution across all healthy targets matters more than keeping traffic zone-local, so cross-zone load balancing stays on. 

 Carry that distinction into the steps. An auction deadline and per-request economics call for keeping traffic in-zone, and utilization smoothness on modest traffic calls for spreading it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Auto Scaling groups to span at least 3 Availability Zones:** Create Auto Scaling groups with subnets in all Availability Zones within your deployment region. Set AvailabilityZoneRebalancing to Enabled to redistribute instances after Availability Zone recovery. Configure minimum healthy percentage (85%) so that the fleet remains operational during rolling updates or Availability Zone failures. 

1.  **Implement EKS pod anti-affinity for critical bidding services:** Add podAntiAffinity rules with topologyKey: topology.kubernetes.io/zone to all critical advertising service deployments. Use preferredDuringSchedulingIgnoredDuringExecution for standard services and requiredDuringSchedulingIgnoredDuringExecution for the most critical Tier 1 auction services to guarantee Availability Zone distribution. 

1.  **Configure zone-aware load balancing:** For NLB serving RTB bid traffic, disable cross-zone load balancing to keep traffic within each Availability Zone and avoid cross-AZ data transfer charges. Configure NLB with one IP per Availability Zone and use Route 53 latency-based routing or Availability Zone DNS to route clients to the NLB endpoint in their Availability Zone. Verify Availability Zone traffic distribution using CloudWatch metrics per target group. 

1.  **Deploy Karpenter with zone-balanced node provisioning:** Configure Karpenter NodePool with requirements specifying all Availability Zones in the Region. Set consolidationPolicy: WhenUnderutilized for batch workloads and consolidationPolicy: WhenEmpty for latency-sensitive bidding workloads to avoid consolidation during active campaigns. 

1.  **Validate Availability Zone failure recovery through FIS experiments:** Create an FIS experiment that terminates all EC2 instances in one Availability Zone simultaneously. Verify that Auto Scaling replaces instances in the remaining Availability Zones within the configured RTO. Monitor bid response latency and error rate during the experiment to confirm that the Availability Zone failure doesn't cause SLO violations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP03 Architect for variable demand](advrel01-bp03.md) 
+  [ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions](advrel03-bp04.md) 

 **Related documents:** 
+  [Distribute instances across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html) 
+  [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) 

 **Related services:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [Amazon EKS](https://aws.amazon.com/eks/) 