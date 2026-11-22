

# Optimize over time

 A workload that was cost-efficient at launch drifts as usage patterns shift, business requirements change, and cloud providers release new services and pricing models. This capability covers keeping workloads cost-efficient over time: running structured review cycles, deciding when to modernize aging components, and adopting new capabilities as they become available. 

 Match review frequency to each workload's share of spend. Perform quarterly or bi-annual deep reviews for workloads representing more than roughly 10 percent of cost; review lower-impact workloads annually. 


|  COST09: How do you evaluate new services and optimize over time?  | 
| --- | 
|  [COST09-BP01 Develop a workload review process](cost09-bp01.md)  | 
|  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md)  | 

## Capability intent
<a name="cost09-intent"></a>
+  Workloads are reviewed on a schedule whose frequency and depth match each workload's share of spend, business importance, and the effort needed to change it. 
+  Reviews assess total cost of ownership, including operational, maintenance, and licensing costs, rather than resource cost alone. 
+  New services, features, and pricing models are tracked and evaluated as candidate improvements against the running workload. 
+  Modernization decisions are made deliberately, weighing migration cost against the compounding cost of maintaining aging components. 
+  Adopted changes are validated against security, compliance, regional availability, and performance requirements before rollout. 
+  Identified opportunities enter a prioritized backlog and flow through the normal development cycle, and realized savings feed back to refine future reviews. 

## Common issues to watch for
<a name="cost09-issues"></a>
+  Workloads are reviewed only when costs spike or at annual budget time, so savings surface after the overrun rather than before it. 
+  The same cadence and depth applies to every workload, which wastes review effort on small, stable workloads and under-reviews the ones driving most of the bill. 
+  Reviews count resource cost but ignore operational, maintenance, and licensing costs, so the components where total cost is highest look cheaper than they are. 
+  Modernization is deferred because migration cost is visible today while the cost of staying put is spread over years, until technical obsolescence forces a more expensive change. 
+  Tracking new service and pricing releases is nobody's explicit responsibility, so workloads keep running on costlier options long after cheaper ones ship. 
+  Optimization findings are recorded but never enter a backlog, so reviews produce reports instead of implemented savings. 