

# Architecture selection

 The optimal solution for a particular advertising workload varies, and solutions often combine multiple approaches. Well-Architected advertising workloads use multiple solutions and allow different features to improve performance. Architecture selection decisions directly affect the latency, burst capacity, and unit economics of programmatic advertising systems. Choosing the wrong architecture for geographic affinity, scaling strategy, compute, or AI/ML inference can result in missed bid deadlines, inefficient scaling, and avoidable cost penalties at scale. 


|  ADVPERF01: How do you select and configure your architecture to meet the performance requirements of your advertising workload?  | 
| --- | 
| [ADVPERF01-BP01 Design geographical affinity architecture with external entities (DSPs and SSPs)](advperf01-bp01.md) | 
| [ADVPERF01-BP02 Use appropriate scaling to handle burst traffic with cost considerations](advperf01-bp02.md) | 
| [ADVPERF01-BP03 Design for low latency with appropriate compute, storage, and network considerations](advperf01-bp03.md) | 
| [ADVPERF01-BP04 Evaluate AI/ML-based architecture for optimization](advperf01-bp04.md) | 
| [ADVPERF01-BP05 Benchmark managed and self-hosted services for latency-sensitive bid paths](advperf01-bp05.md) | 

## Capability intent
<a name="advperf01-capability-intent"></a>
+  You have designed geographic affinity routing so that traffic from publishers and demand partners travels the shortest network path, keeping bid round-trip times within the real-time bidding window. 
+  Your architecture scales elastically to absorb burst traffic from flash crowds and high-profile live events without dropped bid requests or latency degradation. 
+  Every layer of your infrastructure (compute, storage, and network) is configured specifically for the low-latency, high-throughput demands of ad serving and bidding workloads. 
+  AI/ML inference is served through a purpose-built, low-latency framework that meets programmatic auction deadlines and integrates with your observability stack. 
+  You have made an evidence-based choice between self-managed open-source software and fully managed AWS services, validated through benchmarking under realistic advertising traffic. 

## Common issues to watch for
<a name="advperf01-common-issues-to-watch-for"></a>
+  Routing traffic between AWS-hosted DSP and SSP partners over the public internet instead of AWS PrivateLink, adding unnecessary latency and network exposure. 
+  Deploying all compute in a single Region regardless of where bid requests originate, forcing cross-continental round trips. 
+  Relying solely on reactive auto scaling without pre-warming load balancers, causing connection drops during sudden traffic bursts before scaling catches up. 
+  Invoking [Amazon Bedrock](https://aws.amazon.com/bedrock/) over public internet endpoints instead of through AWS PrivateLink, adding per-call latency to the critical bid path. 
+  Defaulting to self-managed open-source or fully managed services without benchmarking either option under realistic advertising load. 
+  Hard-coding a specific x86 chipset (AMD or Intel), locking the workload into a single Spot pricing pool and missing cost savings when pricing shifts. 