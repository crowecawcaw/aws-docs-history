

# ADVCOST03-BP10 Right-size compute with auto-scaling and serverless containers

 RTB traffic follows daily patterns and spikes during major content events. Fixed-capacity infrastructure wastes money during low-traffic periods and drops auctions during spikes. Scalable containers match capacity to demand in near real-time, so you pay less for idle compute during nights and weekends. 

 **Desired outcome:** 
+  RTB compute scales automatically with traffic demand, maintaining optimal utilization (60-70% CPU) without over-provisioning during low-traffic periods or dropping auctions during spikes. 
+  Non-latency-critical workloads (analytics, reporting) use AWS Fargate Spot for 60-90% cost reduction. 

 **Common anti-patterns:** 
+  Provisioning fixed compute capacity sized for peak traffic, so idle resources accrue costs during nights, weekends, and off-peak periods when RTB traffic drops well below daytime peaks. 
+  Scaling reactively based only on CPU utilization without incorporating QPS-based metrics, which lags scaling actions behind sudden traffic spikes and causes dropped auctions before new capacity comes online. 
+  Maintaining fan-out to all demand partners regardless of performance, which sends bid requests to partners with consistently low win rates or slow response times and consumes compute and networking for negligible revenue return. 
+  Using On-Demand EC2 instances for all bidder workloads without evaluating Fargate (serverless containers) for variable traffic or Spot capacity for non-latency-critical supporting tasks like analytics and reporting. 
+  Setting auto-scaling minimum capacity too high out of caution, so excess baseline compute stays online during predictable low-traffic windows rather than trusting scaling policies to respond within acceptable latency budgets when traffic returns. 

 **Benefits of establishing this best practice:** 
+  Reduce idle compute costs during low-traffic periods (nights, weekends). 
+  Reduce the risk of revenue loss from dropped auctions during traffic spikes. 
+  Serverless containers (Fargate) remove EC2 instance management overhead. 
+  Spot capacity provides 60-90% discounts for non-latency-critical workloads. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB traffic peaks during prime-time viewing and drops off overnight. Unlike fixed-capacity or average load infrastructures, automatic scaling matches compute capacity to demand in near real-time and holds a target utilization (typically 60-70% CPU) that leaves headroom for sudden traffic increases. 

 CPU utilization reflects sustained load and works well for gradual traffic changes. QPS (queries per second) reflects instantaneous demand and catches sudden spikes before they saturate CPU. When you scale on whichever threshold breaks first, you get a faster response than either metric gives by itself. Without QPS-based scaling, a sudden surge can queue requests and cause bid timeouts before CPU metrics trigger a scale-out. 

 [AWS Fargate](https://aws.amazon.com/fargate/) removes the operational overhead of managing EC2 instances (patching, AMI updates, and capacity planning) for containerized bidder workloads. For non-latency-critical supporting tasks like bid analytics, log processing, and report generation, [Fargate Spot](https://aws.amazon.com/fargate/pricing/) provides 60-90% cost reduction. These workloads tolerate interruption because they can checkpoint progress and resume. Do not run latency-critical bid processing on Spot. Capacity reclamation during peak auction volume drops bids. 

 Scheduled scaling reduces reliance on reactive scaling for predictable patterns. Pre-scale before known traffic events and scale down overnight. 

 Each bid request fans out to multiple demand partners (adapters), and each adapter consumes compute and network resources. Adapters with consistently low win rates (below 1%) use resources on every auction but return little revenue. Disable them to cut per-request compute. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy bidder containers on ECS Fargate with target tracking:** Configure Application Auto Scaling targeting 65% CPU utilization. Publish custom QPS metrics and include them in scaling decisions. Scale down during overnight hours and pre-scale before known traffic events. 

1.  **Configure dual-metric scaling (CPU \+ QPS):** Scale on whichever threshold is breached first. CPU utilization for sustained load, QPS for sudden spikes. This catches traffic surges before they cause CPU saturation. 

1.  **Deploy analytics and reporting workloads on Fargate Spot:** For bid analytics, log processing, and report generation, use Fargate Spot for 60-90% cost reduction. Implement checkpoint-based processing to handle Spot interruptions. 

1.  **Disable low-yield demand partner adapters:** Analyze win rate per adapter. Disable adapters with less than 1% win rate. They consume compute and networking per auction with minimal revenue return. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP02 Implement Availability Zone affinity across the RTB data path](advcost03-bp02.md) 

 **Related documents:** 
+  [Guidance for Deploying a Prebid Server on AWS](https://aws.amazon.com/solutions/implementations/prebid-server-deployment-on-aws/) 

 **Related services:** 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [AWS Fargate](https://aws.amazon.com/fargate/) 