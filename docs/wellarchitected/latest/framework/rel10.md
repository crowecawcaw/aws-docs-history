

# Use fault isolation to protect your workload

 Everything fails eventually, from a single disk to the power and network feeding an entire site. A failure that reaches every part of a workload takes the whole workload down with it. Fault isolation limits the impact of a component or system failure to a defined boundary, so components outside that boundary keep working. Running a workload across several isolation boundaries turns a single point of failure into a contained event that most requests never notice. 

 This capability covers how an organization uses fault isolation to keep a failure from spreading: deploying compute and data across multiple isolated locations, automating recovery for the components that cannot leave a single location, and partitioning a workload into independent cells so one fault reaches only a fraction of the requests. 


|  REL10: How do you use fault isolation to protect your workload?  | 
| --- | 
|  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md)  | 
|  [REL10-BP02 Automate recovery for components constrained to a single location](rel10-bp02.md)  | 
|  [REL10-BP03 Use bulkhead architectures to limit scope of impact](rel10-bp03.md)  | 

## Capability intent
<a name="rel10-intent"></a>
+  Production workloads run across at least two isolated locations, so a failure in one location does not end availability everywhere. 
+  The location strategy matches the workload's resilience requirements, rather than defaulting to the most complex option. 
+  Components that must stay in a single location have an automated, tested rebuild path that meets their recovery time and recovery point objectives. 
+  Workloads that need containment beyond location boundaries are partitioned into independent cells that share no state. 
+  Cell size is bounded and treated as a reliability control, and the workload grows by adding cells rather than by enlarging existing ones. 
+  Traffic redirects to healthy locations and cells automatically when one becomes impaired. 

## Common issues to watch for
<a name="rel10-issues"></a>
+  A production workload runs in a single Availability Zone, so the loss of that zone ends availability. 
+  Teams reach for a multi-Region architecture when a multi-AZ design meets the requirements, and take on cost and complexity for no gain. 
+  A component in one Region calls a component in another Region during normal operation, which couples the two and lets a failure cascade between them. 
+  Deployments and data drift out of sync between locations, so the surviving location cannot actually take over. 
+  A single-location component has no automated rebuild, and its recovery time stays unknown until an incident exposes it. 
+  Cells grow without an upper bound or share state, so the fault domain widens and the isolation the architecture promised erodes. 