

# Select the correct resource type, size, and number

 Choosing the right resources for a workload is fundamental to cost efficiency in the cloud. This capability covers selecting resource types, sizing each resource to its technical requirements, and running the correct number of resources at the lowest cost. The practice is called right-sizing, and it depends on a workload's characteristics, performance requirements, and usage patterns rather than on peak-load estimates. 

 Right-sizing is both an initial design decision and an ongoing discipline. A resource that fits at launch drifts out of fit as demand cycles, data ages, and usage grows. Revisit the choice as the workload runs. Match right-sizing effort to a workload's cost impact: analyze high-cost resources more deeply than low-cost ones. 


|  COST06: How do you meet cost targets when you select resource type, size, and number?  | 
| --- | 
|  [COST06-BP01 Perform cost modeling](cost06-bp01.md)  | 
|  [COST06-BP02 Select resource type, size, and number based on data](cost06-bp02.md)  | 
|  [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md)  | 
|  [COST06-BP04 Consider using shared resources](cost06-bp04.md)  | 

## Capability intent
<a name="cost06-intent"></a>
+  Resource decisions are grounded in cost models that break a workload down by component and weigh total cost of ownership, not infrastructure charges alone, before a configuration is committed. 
+  Resource type, size, and number are chosen from measured workload characteristics across compute, memory, storage, and network, so capacity matches the constraining dimension rather than a cautious over-estimate. 
+  Capacity tracks demand through feedback loops that read live metrics, so workloads resize and re-tier automatically instead of holding peak capacity at all times. 
+  Common supporting functions run on shared resources where that raises utilization and lowers cost, and the shared spend is allocated back to the teams that consume it. 
+  Right-sizing is treated as a continuous practice reviewed on a cadence, with the depth of analysis matched to how much of the bill each workload drives. 

## Common issues to watch for
<a name="cost06-issues"></a>
+  Resources are sized on intuition rather than data, and because guessing high feels safer than guessing low, workloads run persistently over-provisioned across every instance and every month. 
+  Sizing decisions are made on a single dimension such as CPU, so a memory-bound or network-bound workload lands on the wrong resource family and either underperforms or overpays. 
+  Workloads that could scale are left at fixed capacity, forcing a permanent choice between provisioning for the peak and wasting money in every trough, or provisioning for the average and failing during every spike. 
+  Right-sizing recommendations are generated and then never acted on, so identified savings stay theoretical while the underused resources keep running. 
+  Common functions such as monitoring, backups, and connectivity are rebuilt in every account or workload, multiplying cost for capabilities that rarely need to differ between teams. 
+  Shared resources are provided without allocating their cost, so no team owns the spend and it grows unnoticed. 