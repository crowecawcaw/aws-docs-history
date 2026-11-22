

# Plan for data transfer

 Data transfer is one of the most variable and often underestimated parts of a cloud bill. Data transfer cost depends on where the data movement originates and ends, how often it moves, and which path it takes. Those charges follow architectural choices, so controlling them starts at design time and continues as the workload grows. 

 This capability covers documenting how data moves across services and environments, modeling transfer cost before deployment, and revisiting the design as pricing and usage change. Data transfer is entangled with performance, reliability, and security, so decisions here weigh cost against the resilience and latency that traffic patterns provide. Avoid defaulting to the cheapest path. 


|  COST04: How do you plan for and optimize data transfer costs?  | 
| --- | 
|  [COST04-BP01 Define network and data transfer infrastructure costs](cost04-bp01.md)  | 
|  [COST04-BP02 Perform data transfer modeling](cost04-bp02.md)  | 
|  [COST04-BP03 Optimize services to reduce data transfer costs](cost04-bp03.md)  | 

## Capability intent
<a name="cost04-intent"></a>
+  The network paths a workload uses are documented alongside the transfer pricing that applies to each, so cost can be attributed to the workloads that generate it. 
+  Shared network components carry a defined allocation method, so their charges reach the teams that drive usage rather than resting on a single owner. 
+  Data transfer cost is modeled during design across a range of usage levels, so architectural options are compared on projected cost rather than current spend alone. 
+  Every transfer flow is tied to the business outcome it serves, so flows without a justification can be questioned or removed. 
+  The transfer architecture is reviewed on a regular cadence, and the costliest flows are addressed first as pricing and usage patterns change. 
+  Optimization decisions treat cost as one input alongside performance, reliability, and security, so cutting a charge never quietly weakens the workload. 

## Common issues to watch for
<a name="cost04-issues"></a>
+  Network charges are tracked as a single line item, so no one can see which path or component drives the cost and reviews have nothing to act on. 
+  Shared network services are deployed without an allocation method, so their cost lands on the owning account and no workload sees the charge it creates. 
+  Transfer cost is estimated from current traffic alone, so projections miss growth and tiered pricing and understate the bill the workload reaches at scale. 
+  Flows are built without recording the business outcome they serve, so expensive traffic cannot be questioned because no one can say why it exists. 
+  The transfer architecture is treated as fixed after launch, so it drifts out of alignment as pricing and usage change and misses cheaper options. 
+  Optimization chases the flow that is easiest to change rather than the one that costs the most, so effort produces activity while the largest charges remain. 