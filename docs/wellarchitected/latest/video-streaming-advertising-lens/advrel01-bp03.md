

# ADVREL01-BP03 Architect for variable demand
<a name="advrel01-bp03"></a>

 Architect to elastically launch resources for variable demand, including peak events such as flash crowds and thundering herds. Advertising workloads spike during live events, product launches, and seasonal campaigns. Infrastructure must absorb these peaks without degrading bid win rates or dropping ad requests. 

 **Desired outcome:** 
+  Your architecture handles sudden traffic spikes without dropped bid requests or latency degradation. 
+  Historical load statistics inform load testing scenarios so that workload performance under unexpected peaks is validated. 
+  Auto Scaling groups and Elastic Load Balancers meet compute demands and send requests to healthy hosts without manual intervention. 

 **Common anti-patterns:** 
+  Sizing infrastructure for average load rather than peak load, so high-traffic events bring throttling and revenue loss. 
+  Scaling only compute without planning for network, database, and cache capacity, which creates bottlenecks at the layers that did not scale. 
+  No load testing before major advertising events, so capacity limits surface during the event itself. 

 **Benefits of establishing this best practice:** 
+  Peak events are absorbed gracefully without manual capacity operations. 
+  Pre-validated scaling behavior provides confidence before major campaigns. 
+  Proactive capacity planning reduces the risk of both over-provisioning (wasteful) and under-provisioning (revenue-losing). 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Reactive scaling assumes demand rises faster than it can be served but slower than capacity can be added. Advertising traffic violates the second half of that assumption. A live sports event, a stream premiere, or a synchronized campaign launch produces a step change rather than a ramp. Demand arrives in seconds while new compute takes minutes to become useful, and whatever capacity was already running serves the interval between them. Because a bid request that misses its deadline is worth nothing rather than merely late, that interval is pure lost revenue. Arrange elasticity in advance of demand rather than in response to it. 

 You can plan capacity ahead of demand because advertising demand is unusually forecastable. Most of the largest peaks are on a calendar known weeks ahead, because someone scheduled the event and someone bought against it. Historical traffic for a comparable event predicts a peak better than any live signal, because the live signal only exists after the peak has begun. Peaks also vary by channel and geography, so a system serving several channels has several distinct peak shapes. A single global scaling policy fits none of them. 

 Warm capacity costs money, so choosing a peak multiple is a commercial judgment. Test for the scenario in which the revenue at risk during a peak exceeds the cost of holding headroom. State that number explicitly so the trade-off stays reviewable. 

 Testing at a multiple only proves capacity if every layer is included. Compute scales elastically, but network paths, address space, connection tables, and partner-side capacity don't necessarily scale with it. A test that drives one service in isolation finds none of those limits. A compute fleet can scale correctly into a network path that can't carry the traffic, which presents as unexplained latency rather than as a capacity error. 

 At peak, a host can pass a liveness check while returning bids too slowly to win. Verification must exercise the auction path end to end and judge each host against the deadline, not against availability. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish load baseline metrics and historical traffic patterns:** Instrument your advertising platform to publish request volume, bid rate, and latency percentiles as CloudWatch metrics with 1-minute resolution. Analyze at least 90 days of historical data to identify traffic patterns: time-of-day peaks, day-of-week peaks, and event-driven spikes. Document peak multipliers (typical live event peak is 5–10x baseline) for use in capacity planning and load testing. 

1.  **Configure predictive scaling for known advertising calendar events:** Create predictive scaling policies in EC2 Auto Scaling or ECS Application Auto Scaling that are trained on historical RTB traffic data. For known events (Super Bowl, holiday shopping peaks), supplement predictive scaling with scheduled scaling actions that pre-provision capacity 30 minutes before the event. Set scale-in cooldown periods (300 seconds minimum) to avoid premature scale-in during event traffic. 

1.  **Implement load tests at 5x baseline before major events:** Use a load testing framework (Artillery, Locust, or AWS Load Testing solution) to simulate 5x baseline RTB traffic on a staging environment that mirrors production. Validate that: bid response p99 latency remains within SLO, no requests are throttled or dropped, database connection pools don't exhaust, and cache hit rates remain stable. Fix any capacity gaps before the event date. 

1.  **Plan networking capacity alongside compute capacity:** For each Auto Scaling group, calculate the aggregate network bandwidth required at peak (bid request size × peak QPS per instance). Verify that your VPC, load balancer, and NAT Gateway configurations can sustain peak bandwidth without throttling. For high-throughput RTB workloads, consider Enhanced Networking instances (ENA) and NLB Capacity Unit reservation. 

1.  **Configure CloudWatch Synthetics for ongoing availability monitoring:** Deploy CloudWatch Synthetics canaries that send test bid requests through your complete auction pipeline on a 1-minute cadence. Configure the canaries to validate response format, content, and latency against expected thresholds. Use these canaries as the primary availability signal for scaling decisions and as early warning during traffic spikes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL03-BP04 Reserve appropriate capacity of services in the supported regions](advrel03-bp04.md) 
+  [ADVREL03-BP01 Use a full regional deployment for compute resources through Auto Scaling groups and compute container orchestrators](advrel03-bp01.md) 

 **Related documents:** 
+  [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) 
+  [Guidance for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/) 

 **Related services:** 
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 