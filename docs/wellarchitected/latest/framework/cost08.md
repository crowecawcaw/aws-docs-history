

# Manage demand and supply resources

 Cloud spend follows provisioned capacity, so any gap between provisioned and consumed capacity is waste. Matching supply to demand closes that gap: it holds performance when demand rises and releases capacity when demand falls, so you no longer pay for peak-sized capacity around the clock. This capability covers the practices that align resources with real need, starting with how demand behaves over a full business cycle. 

 Demand rarely arrives at a steady rate, and the right response depends on its shape. Predictable, time-based patterns call for a different approach than sharp, variable spikes. When you can smooth demand at the edge through buffering or throttling, capacity tracks average demand instead of peak. When you cannot, provisioning must adjust to demand automatically. The best practices under this capability describe how to analyze demand, smooth it, and supply resources to meet what remains. 


|  COST08: How do you plan for and supply resources to match demand?  | 
| --- | 
|  [COST08-BP01 Perform an analysis on the workload demand](cost08-bp01.md)  | 
|  [COST08-BP02 Implement a buffer or throttle to manage demand](cost08-bp02.md)  | 
|  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md)  | 

## Capability intent
<a name="cost08-intent"></a>
+  Demand is understood across a full business cycle, including seasonal and periodic peaks, and analysis effort concentrates on the high-value workloads whose demand varies most. 
+  Provisioning decisions start from measured demand against required response times, so performance targets are met without persistent overprovisioning. 
+  Incoming request rates are smoothed with buffering or throttling, so short spikes run on capacity sized closer to average demand rather than forcing capacity sized for peak. 
+  Capacity adjusts to demand automatically, with predictable patterns met by scheduled or predictive provisioning and variable demand met by reactive scaling. 
+  Idle capacity is released when demand subsides, and non-production environments do not run at full capacity outside the hours they are used. 

## Common issues to watch for
<a name="cost08-issues"></a>
+  Capacity is provisioned for peak demand and runs continuously, so cost reflects the peak while most of that capacity sits idle between peaks. 
+  Demand is sampled over a window too short to capture seasonal peaks, so provisioning misses predictable spikes and teams compensate with permanent headroom. 
+  Deep analysis goes to stable, low-cost workloads while high-value workloads with sharp swings are left unexamined, so the effort returns little and the largest savings go unclaimed. 
+  Buffering or throttling is applied uniformly across all traffic, ignoring differing client and workload priorities, so important requests are delayed alongside low-priority ones. 
+  Reactive scaling is used for demand that is predictable by time, so capacity arrives after the peak has already degraded performance. 
+  Non-production environments run at full capacity outside working hours because no one owns stopping them, which adds cost with no corresponding use. 