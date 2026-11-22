

# ADVREL09-BP01 Deploy Prebid Server across multiple Availability Zones with health-checked load balancing

 A single-AZ Prebid Server deployment means an Availability Zone impairment removes all server-side header bidding capability for the publisher. Deploy Prebid Server instances distributed across at least two Availability Zones behind a load balancer with active health checks. 

 **Desired outcome:** 
+  Prebid Server instances are distributed across at least two Availability Zones behind a load balancer with active health checks. 
+  An Availability Zone-level failure results in automatic traffic redistribution to healthy instances in remaining Availability Zone within the health check detection window (approximately 20 seconds). 
+  Auto-scaling maintains consistent auction latency during traffic spikes, protecting publisher yield during peak monetization hours. 

 **Common anti-patterns:** 
+  Deploying all Prebid Server instances in a single Availability Zone without redundancy. 
+  Health checks that only validate HTTP 200 (container alive) rather than auction engine responsiveness. 
+  No Auto Scaling: manual capacity management can't respond to peak ad hours or Availability Zone failover scenarios. 

 **Benefits of establishing this best practice:** 
+  Multi-AZ deployment with active health checks helps publisher header bidding availability survive Availability Zone-level impairments. 
+  Auto-scaling maintains consistent auction latency during traffic spikes, protecting publisher yield during peak monetization hours. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publisher header bidding is on the critical path of every ad impression. Each second of Prebid Server unavailability translates to lost revenue through unfilled inventory or fallback to less competitive waterfall auctions. A Prebid Server process can be listening on its port and passing a basic liveness probe while failing every auction it attempts. Connections to downstream demand-side platforms may time out, the local bid-cache may be stale, or thread-pool exhaustion may cause requests to queue without returning a bid response. Health checks must probe actual auction capability. 

 Set health-check thresholds tight enough to remove failing instances before they absorb bid requests without producing auctions, while allowing enough tolerance for transient latency spikes during peak programmatic traffic. Bursts of high-compute video-format bid requests can briefly push response times past a tight threshold without indicating a persistent fault. 

 When an instance is marked unhealthy, in-flight auctions continue, so bid requests are already with demand partners and responses are arriving. Set deregistration delay long enough for those auctions to complete without discarding bids that already consumed demand-partner quota, and short enough that the load balancer stops routing new requests to a declining instance. Under bursty ad traffic, letting an overloaded instance self-heal once the spike passes is often faster than terminating and replacing it. Fresh instances must warm bid-adapter connections and repopulate caches before they compete effectively in auctions. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Prebid Server on ECS or EKS across at least 2 Availability Zones:** Configure task/pod anti-affinity rules so that replicas are distributed across Availability Zones. Use ECS Service auto scaling or EKS HPA/Karpenter based on CPU utilization (target 60%) and bid request queue depth. 

1.  **Configure ALB health checks that validate auction engine responsiveness:** Set health check endpoint to a lightweight auction validation endpoint (not just a TCP/HTTP liveness check). Configure 10-second intervals with an unhealthy threshold of 2 consecutive failures. Set deregistration delay to 30 seconds for fast drain of unhealthy targets. 

1.  **Enable cross-zone load balancing and set deregistration delay:** Enable cross-zone load balancing to distribute bid requests evenly across Availability Zones. Configure the 30-second deregistration delay to allow in-flight auctions to complete before removing an instance from rotation. 

1.  **Configure Route 53 health checks for Multi-Region failover:** For publishers with Multi-Region Prebid presence, configure Route 53 health checks on the ALB endpoint for secondary-region failover when the primary Prebid Server becomes completely unavailable. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures](advrel01-bp01.md) 
+  [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) 

 **Related documents:** 
+  [Distribute instances across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html) 
+  [Application Load Balancer health checks](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) 

 **Related services:** 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [Amazon EKS](https://aws.amazon.com/eks/) 
+  [Elastic Load Balancing (ALB)](https://aws.amazon.com/elasticloadbalancing/) 