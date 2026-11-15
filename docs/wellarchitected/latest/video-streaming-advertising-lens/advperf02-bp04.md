

# ADVPERF02-BP04 Use a specialized instance family and features
<a name="advperf02-bp04"></a>

 For advertising workloads, use specialized instance families: compute-optimized for ad serving and bidding, storage-optimized for in-memory databases, ML training accelerators for model training, ML inference accelerators for inference, and hardware-isolated enclaves for processing sensitive audience data. Each purpose-built instance family delivers better performance per dollar than general-purpose alternatives for its target workload type. 

 **Desired outcome:** 
+  Each component of your advertising stack runs on an EC2 instance family purpose-built for its workload type (compute, storage, ML training, inference, or sensitive data processing). 
+  Instance selection is deliberate and workload-driven, not based on general-purpose defaults. 
+  Purpose-built accelerators (Trainium, Inferentia) are used for deep learning training and inference in preference to GPU instances where the cost-performance ratio is better. 
+  [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) are used for workloads that process PII or sensitive audience data requiring cryptographic isolation. 

 **Common anti-patterns:** 
+  Running all advertising workload components on general-purpose instances (M-series) regardless of their actual resource profile, which leaves performance and cost efficiency gains on the table compared to purpose-built families. 
+  Using GPU-based instances for deep learning training and inference workloads without evaluating AWS-designed accelerators (Trainium, Inferentia), which are optimized specifically for these use cases at lower cost. 
+  Placing ad serving and bid evaluation components in the same instance pool as analytics and reporting workloads, where batch workloads become noisy neighbors to latency-sensitive traffic. 

 **Benefits of establishing this best practice:** 
+  Purpose-built instance families deliver better performance per dollar for specific workload types than general-purpose alternatives. 
+  For latency-sensitive advertising workloads, the right instance family can be a meaningful competitive advantage. Faster bid evaluation directly improves win rates. 
+  Trainium instances deliver up to 50% cost savings over comparable GPU instances for model training, making ongoing model retraining economically viable at advertising scale. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Bid evaluation on memory-optimized instances wastes memory capacity. User profile databases on compute-optimized instances bottleneck on storage I/O before they saturate CPU. The wrong instance family wastes spend, and for latency-sensitive layers it degrades bid win rates. 

 Bid evaluation is pure compute, where clock speed matters more than memory capacity. User profile databases are storage I/O bound, and network-attached EBS adds a round-trip that NVMe-backed Instance Store avoids. ML training is throughput-bound and latency-tolerant, so use purpose-built accelerators. ML inference is latency-sensitive and typically runs smaller, optimized models that can run on dedicated accelerator hardware or on Graviton CPUs. 

 Inference can run on dedicated Inferentia instances or embedded in the bid evaluation process on Graviton NEON SIMD. Inferentia delivers higher throughput and lower per-inference cost at scale. For models small enough to run in-process within your auction deadline, embed inference on Graviton to avoid the network hop between the bidder and the inference endpoint. Benchmark both paths against your auction deadline. 

 Trainium has moved to Trn2 (powered by Trainium2 chips), which delivers 4x faster throughput and 4x more memory bandwidth than Trn1. Larger audience models and bid price prediction models benefit from the additional memory capacity Trn2 provides. The Storage Optimized family has moved to I8g (Graviton4, 3rd-gen Nitro SSDs), which Aerospike has benchmarked for ad tech workloads. ISV-validated benchmark guidance now applies to I8g, not I4i. Evaluate the current generation before committing to a configuration. 

 Nitro Enclaves support multi-party data collaboration where neither party can be trusted with the other's raw data. Audience matching between a publisher and an advertiser, or identity resolution using hashed PII, requires cryptographic proof that only the approved algorithm processed the data. Attestation supplies that proof and distinguishes an enclave from standard access control. AWS KMS key policies can require decryption only when the enclave presents a measurement (PCR hash) matching a known-good code image, which becomes verifiable. 

 Instance selection also affects Spot availability. The C and I series pools are in high demand in ad tech, so Spot interruption rates run higher than in less contested pools. Run Compute Optimized workloads with both Intel (C7i) and Graviton (C9g or C8g) variants in the same diversified fleet. This expands the Spot pool and reduces interruption risk without changing the resource profile. Configure fleet diversification explicitly. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Use Compute Optimized instances (C series) for ad serving, bidding, and analytics:** Deploy bid request handling, auction logic, creative serving, and distributed analytics on C7i (Intel) or C9g/C8g (Graviton5/Graviton4) instances. C9g (Graviton5) delivers up to 25% higher performance per vCPU than C8g and is available in US East (N. Virginia and Ohio), US West (Oregon), and Europe (Frankfurt) at launch, with additional Regions following. Benchmark both Intel and Graviton variants against your bid evaluation workload to determine which provides better price-performance for your specific access patterns, and use cluster placement groups to minimize inter-instance latency for components that communicate frequently. 

1.  **Use Storage Optimized instances (I series) for real-time database workloads:** Deploy Aerospike or similar NVMe-dependent real-time databases on I8g instances (Graviton4, 3rd-gen Nitro SSDs), which Aerospike has benchmarked specifically for ad tech workloads showing up to 6x throughput improvement over previous generations. I8g delivers up to 65% better real-time storage performance per TB and 60% lower latency variability compared to I4g. For Intel-specific requirements, I4i remains valid. Verify that the application is configured to use the locally attached NVMe storage directly rather than routing to EBS, and monitor NVMe utilization rather than EBS metrics for performance visibility. 

1.  **Use AWS Trainium instances for deep learning model training:** For advertising ML workloads (bid price prediction models, audience models, CTR prediction), evaluate Trn2 instances (Trainium2) as the primary training infrastructure. Trn2 is the current generation, 4x faster with 4x more memory bandwidth than Trn1, and 30–40% better price-performance than GPU-based P5e and P5en instances. Install the AWS Neuron SDK and compile your model using torch-neuronx or tensorflow-neuronx. Run a comparative benchmark between Trn2 and your current GPU-based training setup to measure training throughput and cost per training run. 

1.  **Use AWS Inferentia instances for model inference:** For real-time model inference at advertising scale, evaluate Inf2 instances. Compile models to the Neuron instruction set using the AWS Neuron compiler. For embedded inference in the bid evaluation path, benchmark Inf2 inference latency against your auction deadline budget and compare to Graviton CPU inference as an alternative for smaller models. 

1.  **Use AWS Nitro Enclaves for sensitive advertising data processing:** For workloads that handle PII (user hashed emails, device IDs), private model weights, or cross-party audience matching data, enable Nitro Enclaves on the parent EC2 instance. Package your sensitive computation as an enclave image. Use AWS KMS attestation-based key policies so that decryption keys are only released to enclaves running approved code (identified by PCR hash values). This provides cryptographic proof to all parties that only the approved algorithm processed their data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable](advperf02-bp01.md) 
+  [ADVPERF02-BP05 Evaluate ARM architecture for performance considerations](advperf02-bp05.md) 

 **Related documents:** 
+  [Amazon EC2 Trn2 instances are generally available](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-ec2-trn2-instances-available) 
+  [Boost AdTech Performance with AWS Graviton4: Aerospike I8g benchmark](https://aerospike.com/blog/aws-graviton4-adtech-performance/) 
+  [Introducing Unified ID 2.0 Private Operator Services on AWS Using Nitro Enclaves](https://aws.amazon.com/blogs/industries/introducing-unified-id-2-0-private-operator-services-on-aws-using-nitro-enclaves/) 

 **Related services:** 
+  [Amazon EC2 Compute Optimized instances (C9g)](https://aws.amazon.com/ec2/instance-types/c9g/) 
+  [Amazon EC2 Storage Optimized instances (I8g)](https://aws.amazon.com/ec2/instance-types/i8g/) 
+  [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/) 
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) 
+  [AWS Nitro Enclaves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) 