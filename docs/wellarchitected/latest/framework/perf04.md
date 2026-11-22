

# Networking and content delivery

 The network sits between every part of a distributed workload, so network decisions shape the latency, throughput, and reliability that users experience. The right networking solution depends on what the workload is sensitive to: latency, bandwidth, throughput, and jitter each pull the design in a different direction. Physical distance between users, data, and resources sets a floor on latency that no tuning removes, though edge locations and careful placement can offset it. 

 In the cloud, networking is software-defined, so topology, connectivity, routing, and inspection points can change without touching hardware. That flexibility is an advantage only when configuration follows measured requirements rather than assumptions carried over from fixed, on-premises networks. 

 This capability covers how to design, configure, and operate networking and content delivery for performance: understanding how the network affects the workload, evaluating the features and connectivity options available, distributing traffic, choosing protocols, placing resources close to users and data, and tuning the configuration from telemetry. 


|  PERF04: How do you select and configure networking to meet performance requirements?  | 
| --- | 
|  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md)  | 
|  [PERF04-BP02 Evaluate available networking features](perf04-bp02.md)  | 
|  [PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload](perf04-bp03.md)  | 
|  [PERF04-BP04 Use load balancing to distribute traffic across multiple resources](perf04-bp04.md)  | 
|  [PERF04-BP05 Choose network protocols to improve performance](perf04-bp05.md)  | 
|  [PERF04-BP06 Choose your workload's location based on network requirements](perf04-bp06.md)  | 
|  [PERF04-BP07 Optimize network configuration based on metrics](perf04-bp07.md)  | 

## Capability intent
<a name="perf04-intent"></a>
+  Network requirements, including latency, bandwidth, throughput, jitter, protocols, and traffic patterns, are documented per workload and inform the design from the start rather than being diagnosed after slowdowns appear. 
+  Networking features and connectivity options are chosen against measured requirements, and each adopted feature earns its place through tested improvement rather than reputation. 
+  Traffic is distributed across multiple resources so the workload scales with demand and tolerates the loss of any single resource, with connection-level work such as encryption termination moved off backends where it helps. 
+  Protocols match each communication's reliability, latency, and throughput needs instead of defaulting to a single protocol everywhere. 
+  Resources sit close to the users and data that depend on them, and edge caching and acceleration shorten the path for a globally distributed audience. 
+  Network configuration follows from telemetry collected across every layer, so teams separate network causes from application causes and tune to real traffic rather than overprovisioning. 

## Common issues to watch for
<a name="perf04-issues"></a>
+  On-premises assumptions are imported wholesale, so traffic is routed back through a central data center or funneled through a single firewall, recreating bottlenecks and paying in latency for traffic that never needed to leave the cloud. 
+  Features are turned on by reputation instead of measurement, so effort and cost go to options that address no real bottleneck while the actual constraint, often a per-flow bandwidth limit, goes untouched. 
+  A VPN is chosen because it stands up quickly, and its variable throughput and jitter fail to meet the workload's needs once real traffic arrives, with no redundant path planned for when a single connection fails. 
+  Workloads are exposed without load balancing, or generic connection-level balancing forces every node to terminate encryption, wasting backend capacity that could serve requests. 
+  A single protocol is used everywhere regardless of communication pattern, so reliability overhead slows real-time paths and encryption is added to latency-sensitive traffic without measuring its cost. 
+  Resources are placed near the team rather than the users, and a global audience is served from one location without edge caching or acceleration, leaving distant users with latency that placement could have prevented. 
+  Network performance is tested only from a location next to the deployment, so a workload that looks fast to the team is slow for half its audience, and overprovisioning hides the real bottleneck. 