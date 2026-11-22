

# Compute and hardware

 The optimal compute choice for a particular workload can vary based on application design, usage patterns, and configuration settings. Advertising architectures use different compute choices for various components (ad serving, bidding, data processing, and AI agent orchestration) and allow different features to improve performance. Selecting the right compute for each advertising workload component is a prerequisite for meeting sub-millisecond to single-digit-millisecond latency targets at scale. 


|  ADVPERF02: How do you select and configure compute resources to meet the performance requirements of your advertising workload?  | 
| --- | 
| [ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable](advperf02-bp01.md) | 
| [ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization](advperf02-bp02.md) | 
| [ADVPERF02-BP03 Consider low-latency node provisioning tools to improve startup and scaling time](advperf02-bp03.md) | 
| [ADVPERF02-BP04 Use a specialized instance family and features](advperf02-bp04.md) | 
| [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md) | 
| [ADVPERF02-BP06 Use a managed serverless runtime for AI agent compute](advperf02-bp06.md) | 

## Capability intent
<a name="advperf02-capability-intent"></a>
+  You have evaluated ISV-certified EC2 instance types and selected compute based on published benchmark results rather than defaults for advertising-specific software (Aerospike, Databricks). 
+  Your advertising workloads run in containers on [Amazon EKS](https://aws.amazon.com/eks/) or ECS with auto scaling policies that respond faster than traditional VM-based deployments. 
+  Low-latency scaling tools (Karpenter, KEDA) provision nodes and pods quickly enough to absorb sudden traffic spikes from advertising events. 
+  Purpose-built instance families (Compute Optimized, Storage Optimized, Trainium, Inferentia, and Nitro Enclaves) are used for the workload types they are designed for. 
+  ARM architecture (AWS Graviton) has been evaluated against x86 alternatives, and eligible workloads have been migrated to Graviton with validated benchmarks. 
+  AI agent workloads use [Amazon Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/) to remove undifferentiated infrastructure management for session routing, scaling, and lifecycle. 

## Common issues to watch for
<a name="advperf02-common-issues-to-watch-for"></a>
+  Running all advertising workload components on general-purpose instances regardless of their actual resource profile, leaving performance improvements and cost savings unrealized. 
+  Deploying ISV software (Aerospike, Databricks) using the same instance types and configurations carried over from on-premises environments, without validating whether those choices are optimal on AWS infrastructure. 
+  Keeping monolithic application architectures that force the entire workload to scale as a single unit, even when only one component (the bid request handler or audience lookup service) is under load. 
+  Relying on traditional Kubernetes Cluster Autoscaler with standard Auto Scaling group warm-up times, introducing node provisioning delays that cause pods to queue during traffic bursts. 
+  Managing AI agent infrastructure manually (provisioning ECS tasks, building custom session routing, scaling logic) when AgentCore Runtime handles these concerns automatically. 