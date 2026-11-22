

# Compute and hardware

 The compute a workload runs on sets the ceiling for its performance, its cost, and the operational effort it demands. The right choice depends on how the workload actually behaves: how traffic arrives, how long work runs, how much state it holds, and how sharply demand changes. A compute choice made from habit rather than evidence leaves performance on the table, and it is expensive to unwind once it reaches production. 

 This capability covers how an organization selects compute to fit the workload, measures how that compute performs, and keeps it matched to demand over time. It spans choosing the compute model and hardware for each component, collecting the metrics that show where resources work hard or sit idle, right-sizing and scaling to track real load, and offloading suitable work to specialized accelerators. 


|  PERF02: How do you select and use compute resources to meet performance requirements?  | 
| --- | 
|  [PERF02-BP01 Select the best compute options for your workload](perf02-bp01.md)  | 
|  [PERF02-BP02 Collect compute-related metrics](perf02-bp02.md)  | 
|  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md)  | 
|  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md)  | 
|  [PERF02-BP05 Use optimized hardware-based compute accelerators](perf02-bp05.md)  | 

## Capability intent
<a name="perf02-intent"></a>
+  Each workload component runs on the compute model whose trade-offs fit how it behaves, and more than one model is used where that produces a better fit. 
+  Compute decisions rest on measured workload characteristics and continuous metrics, covering both resource utilization and application behavior, rather than on habit or familiarity. 
+  Provisioned capacity matches real demand, so neither idle over-provisioning nor performance-limiting under-provisioning persists. 
+  Capacity adjusts automatically as load changes, holding performance through peaks without paying for peak capacity around the clock. 
+  Work that benefits from parallel hardware runs on accelerators that stay busy and are released when idle, while CPU-appropriate work stays on general-purpose compute. 
+  Compute choices, sizing, and scaling policies are revisited as demand shifts and newer options ship, so the workload stays efficient over time. 

## Common issues to watch for
<a name="perf02-issues"></a>
+  Compute is chosen by habit or carried over from on-premises, so workloads miss cloud-native options that would fit their traffic pattern and cost less. 
+  A single instance family or compute service is standardized across every workload for management simplicity, forcing components onto configurations that do not fit and blocking newer, better-value generations. 
+  Only default metrics are collected, so in-guest signals such as memory and workload-specific signals such as queue depth stay invisible until they cause a disruption. 
+  Capacity is sized once and left alone, so over-provisioned resources waste spend while under-provisioned ones degrade the customer experience. 
+  Scaling reacts to a metric that does not track real load, or is tested only for scale-out, so capacity oscillates, never releases, or drops in-flight work when it scales in. 
+  Accelerated hardware runs without benchmarking or utilization monitoring, so expensive capacity sits idle or handles work a general-purpose processor would process more efficiently. 