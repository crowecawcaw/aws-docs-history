

# Trust, safety, and privacy workload efficiency

 Privacy collaboration, fraud detection, and content moderation are the data-intensive trust-and-safety workloads that run alongside advertising delivery. Each analyzes large volumes of impression, click, content, or partner data on an ongoing basis, so each carries a resource and carbon footprint that grows with advertising activity. The sustainability levers are shared across all three: scale compute to actual demand rather than provisioning for peak, run ongoing work on energy-efficient processors, defer and batch work that has no real-time requirement, and analyze data where it resides to avoid moving it across Regions. 


|  ADVSUS05: How do you minimize the resource and carbon impact of privacy-collaboration, fraud-detection, and content-moderation workloads?  | 
| --- | 
| [ADVSUS05-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability](advsus05-bp01.md) | 
| [ADVSUS05-BP02 Optimize fraud detection systems for resource efficiency](advsus05-bp02.md) | 
| [ADVSUS05-BP03 Optimize content moderation systems for sustainable operation](advsus05-bp03.md) | 

## Capability intent
<a name="advsus05-capability-intent"></a>
+  Privacy collaboration, fraud detection, and content moderation run on right-sized, energy-efficient compute that scales with actual demand rather than remaining provisioned for peak. 
+  Machine learning inference and other continual processing run on purpose-built, high-efficiency hardware selected for performance per watt. 
+  Work without a real-time latency requirement is separated from latency-sensitive paths, then batched and scheduled to raise utilization and match periods of lower grid carbon intensity. 
+  Data is analyzed where it resides and aggregated close to its source, limiting cross-Region movement of large impression, click, and media datasets. 
+  Signal, audit, and result data is stored on tiers matched to its access pattern and retained only as long as compliance, security, or model accuracy requires. 

## Common issues to watch for
<a name="advsus05-common-issues-to-watch-for"></a>
+  Running privacy, fraud, or moderation workloads continuously on persistent, over-provisioned instances regardless of actual demand. 
+  Processing every event or asset at full fidelity and in real time when intelligent sampling or batching would meet the same business and risk requirement. 
+  Defaulting to general-purpose x86 compute without evaluating energy-efficient, purpose-built processor options for matching, detection, and inference. 
+  Centralizing analysis in a single Region and moving large volumes of impression, click, or media data across Regions, or copying partner datasets rather than analyzing them where they reside. 
+  Retaining raw signals, results, and audit trails indefinitely on a single high-performance storage tier with no lifecycle or deletion policy. 