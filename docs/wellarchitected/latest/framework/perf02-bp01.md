

# PERF02-BP01 Select the best compute options for your workload

 The compute model you choose determines a workload's performance, cost, and operational effort. Workloads differ in shape: some run constantly, some react to events, some process large batches. Matching the compute model to that shape lets a workload perform well without wasting capacity or operator time. 

 **Desired outcome:** 
+  Your compute choice is driven by measured workload characteristics such as traffic pattern, latency target, execution duration, and state, not by habit or familiarity. 
+  You evaluate more than one compute model against your requirements before committing, and you can explain why you rejected the alternatives. 
+  Your workload uses more than one compute model where that produces a better fit, rather than forcing every component onto a single option. 
+  You reassess your compute choice as new instance families and services become available, and as your workload's demands change. 

 **Common anti-patterns:** 
+  Teams reuse the same compute model they ran on-premises without checking whether a cloud-native option fits better. 
+  Teams over-provision a familiar compute option to meet a scaling need that a different model would meet more precisely. 
+  Teams commit to one instance family or one compute service for every workload to keep management simple. 
+  Teams evaluate compute options once at launch and never revisit the decision as newer generations ship. 
+  Teams weigh performance alone and ignore the operational overhead of patching, scaling, and capacity management. 

 **Benefits of establishing this best practice:** 
+  Workloads run closer to their performance targets because the compute model matches how they actually behave. 
+  Infrastructure cost drops when capacity is matched to demand instead of padded for a poor fit. 
+  Operational effort falls when the compute model absorbs undifferentiated work such as server management. 
+  Teams make faster architectural decisions because they compare options against a known set of workload characteristics. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Each compute model trades control for convenience. Virtual machines give you full control of the operating system and runtime at the cost of managing them. Containers standardize the runtime and packaging while leaving you responsible for the orchestration layer. Serverless functions remove server management entirely but constrain execution time, package size, and startup behavior. Batch services provision and tear down capacity around a queue of jobs. 

 Processing needs, traffic patterns, data access patterns, scaling behavior, and latency targets each push toward a different model. A steady, long-running service with predictable load fits a provisioned instance. An event-driven task that runs briefly and infrequently fits a function, where you pay only for execution and avoid idle capacity. A workload with sharp, short spikes suffers on statically sized infrastructure because you either overpay for peak or fail under it. 

 Lift-and-shift migrations that carry forward a fixed-hardware VM model miss elasticity that would cut cost and improve response under variable load. Standardizing on one instance type for every workload has the opposite effect: capacity sits idle. 

 You don't have to run a workload on one model. A single system can pair provisioned instances for a stateful core, functions for event handling, and a batch service for periodic processing. Mixing models adds operational surface, so weigh that cost. 

 On AWS, each primary compute model maps to its own service. [Amazon EC2](https://docs.aws.amazon.com/ec2/) provides virtual servers with a wide selection of instance families and processor types, including [AWS Graviton](https://aws.amazon.com/ec2/graviton/) processors for better price performance. [Amazon ECS](https://aws.amazon.com/ecs/) and [Amazon EKS](https://aws.amazon.com/eks/) run containers, and [AWS Fargate](https://aws.amazon.com/fargate/) runs them without managing the underlying instances. [AWS Lambda](https://aws.amazon.com/lambda/) runs code in response to events and manages compute for you. [AWS Batch](https://aws.amazon.com/batch/) provisions and scales capacity for large parallel jobs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Characterize your workload:** Document the processing needs, traffic pattern, data access pattern, scaling behavior, state, and latency target for each component. These characteristics are the criteria you will score compute options against, so capture them before you look at any service. 

1.  **Map characteristics to compute models:** Match each component to the model whose trade-offs it can accept. Use the following as a starting point, and review the full set of [AWS compute services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html). 


<table>
<thead>
  <tr><th> AWS service </th><th> Key characteristics </th><th> Common use cases </th></tr>
</thead>
<tbody>
  <tr><td> <a href="https://aws.amazon.com/ec2/">Amazon EC2</a> </td><td> Full OS control, broad selection of instance families, processor types, and accelerators </td><td> Lift-and-shift migrations, monolithic and enterprise applications, hybrid environments </td></tr>
  <tr><td> <a href="https://aws.amazon.com/ecs/">Amazon ECS</a> and <a href="https://aws.amazon.com/eks/">Amazon EKS</a> </td><td> Standardized runtime, portable deployments, scalable orchestration </td><td> Microservices, container-based platforms, hybrid environments </td></tr>
  <tr><td> <a href="https://aws.amazon.com/lambda/">AWS Lambda</a> </td><td> Event-driven, no server management, pay per execution </td><td> Microservices, event and stream processing, scheduled tasks </td></tr>
  <tr><td> <a href="https://aws.amazon.com/batch/">AWS Batch</a> </td><td> Dynamic provisioning across ECS, EKS, and Fargate, with On-Demand or Spot capacity </td><td> High performance computing, model training, large parallel jobs </td></tr>
  <tr><td> <a href="https://aws.amazon.com/lightsail/">Amazon Lightsail</a> </td><td> Preconfigured bundles for small, predictable workloads </td><td> Simple web applications, small websites </td></tr>
</tbody>
</table>


1.  **Compare cost and operational overhead:** For each candidate, estimate the pricing dimension that applies, such as instance hours, request count, or data transfer. Add the operational cost of patching, scaling, and capacity management. A cheaper compute rate can cost more overall once operator time is included. 

1.  **Benchmark in a non-production environment:** Run representative load against the shortlisted options and measure against your latency and throughput targets. Benchmarking surfaces behavior that specification sheets hide, such as cold-start latency or contention under spike. 

1.  **Migrate and validate:** Plan the cutover for the selected option and confirm that live performance metrics match what the benchmark predicted. Validate before decommissioning the previous compute. 

1.  **Reassess on a cadence:** Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for real usage and [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) for recommendations, and revisit the choice as new instance generations and services ship. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 
+  [PERF02-BP05 Use optimized hardware-based compute accelerators](perf02-bp05.md) 
+  [PERF01-BP01 Validate requirements align to business needs](perf01-bp01.md) 

 **Related documents:** 
+  [Compute services in the AWS overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html) 
+  [Cloud compute with AWS](https://aws.amazon.com/products/compute/) 
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) 
+  [Amazon EKS worker nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html) 
+  [Amazon ECS container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity.html) 
+  [AWS Lambda function configuration best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4) 
+  [AWS re:Invent 2023 - What's new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g) 

 **Related examples:** 
+  [Run a serverless Hello World](https://aws.amazon.com/tutorials/run-serverless-code/) 
+  [Amazon EKS workshop](https://www.eksworkshop.com/) 
+  [Efficient and resilient workloads with Amazon EC2 Auto Scaling](https://catalog.us-east-1.prod.workshops.aws/workshops/20c57d32-162e-4ad5-86a6-dff1f8de4b3c/en-US) 
+  [Migrating to AWS Graviton with container services](https://catalog.us-east-1.prod.workshops.aws/workshops/dcab7555-32fc-42d2-97e5-2b7a35cd008f/en-US/) 