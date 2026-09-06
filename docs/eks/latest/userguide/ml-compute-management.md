

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage accelerated compute for AI/ML workloads on Amazon EKS
<a name="ml-compute-management"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section covers how to purchase and provision EC2 accelerated compute instances for AI/ML training and inference workloads with Amazon EKS. Whether you’re training large-scale models, running real-time inference, or deploying generative AI applications, using the right NVIDIA GPU or AWS Trainium capacity is foundational for performance of your workloads.

## Choose from EC2 instance types
<a name="choose-ec2-instances"></a>

See the [Specifications for Amazon EC2 accelerated computing instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html) for details on the available Amazon EC2 accelerated compute instances. These include NVIDIA GPU instances from the P-family and G-family, as well as AWS-designed accelerators Trainium and Inferentia.

## Understand EC2 purchase options
<a name="understand-ec2-purchase-options"></a>

Once you know the accelerated instances that you need for your workloads, the next step is understanding the purchase options available for acquiring these accelerated instance types. AWS offers four compute capacity purchase options: On-Demand Instances, Spot Instances, Capacity Blocks for ML, and On-Demand Capacity Reservations (ODCRs). Each option serves different workload patterns, cost profiles, and availability requirements. The [Amazon EC2 Instance Purchasing Options documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) explains how each option works, its pricing model, and when to use it.
+  **On-Demand Instances**: Pay by the second with no commitment and immediate availability when capacity exists. Best for development, prototyping, unpredictable inference scaling, and any workload that needs immediate compute without interruption risk.
+  **Spot Instances**: Up to 90% savings versus On-Demand by using spare EC2 capacity, with a 2-minute interruption notice. Best for fault-tolerant workloads that checkpoint to durable storage: hyperparameter tuning, distributed training with periodic checkpoints, batch and offline inference, and data preprocessing pipelines.
+  **Capacity Blocks for ML**: Reserve P-family and Trainium instances for a fixed window (24 hours, up to 6 months), booked up to 8 weeks in advance. Use Capacity Blocks for planned large-scale training runs, time-bound fine-tuning experiments, and research projects with known timelines that need predictable access to a GPU cluster.
+  **On-Demand Capacity Reservations (ODCRs)**: Reserve accelerated capacity in a specific Availability Zone without a long-term commitment, billed at standard On-Demand rates whether the capacity is used or not. Best for production inference, SLA-bound services, and business-critical applications where scheduling delays or capacity unavailability are unacceptable. Unlike Capacity Blocks, ODCRs support both P-family and G-family instances.

## Match purchase options to workload requirements
<a name="match-purchase-option-with-workload"></a>

Now that you understand the accelerated instance types and purchase options, the next step is matching the right purchase option to your workload-specific requirements. Workloads with greater flexibility across instance types, regions, and timing qualify for more purchase options and lower pricing.

Base your decision on factors such as:
+ Strategic importance and SLA commitments
+ Demand predictability and scheduling flexibility
+ Willingness to commit to reserved capacity in advance
+ Flexibility across instance types, regions, and timing
+ Tolerance for interruptions versus cost savings

In practice, teams adopt a hybrid approach that combines multiple purchase options to balance cost, availability, and reliability across their workload portfolio. The article [How to Get GPU Capacity on AWS](https://builder.aws.com/content/3B88fT4nDiNkg5Wrya4WV5zroSS/how-to-get-gpu-capacity-on-aws) provides a decision tree, pricing comparisons, and real-world examples for selecting the right purchase option for different types of workloads.

## Verify your EC2 service quotas
<a name="verify-service-quotas"></a>

Before implementing any capacity purchase option on your EKS cluster, verify that your AWS account has sufficient vCPU quota for the GPU instance families you plan to use. Without adequate quotas, Karpenter NodePools, EKS Auto Mode provisioning, and EKS node groups will fail to launch accelerated compute nodes regardless of which purchase option you select.

 AWS enforces separate vCPU quotas per instance family and purchase model. Review the [Amazon EC2 instance type quotas](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-instance-quotas.html) to understand the default quotas for accelerated compute instances.

These quotas are based on vCPU count, not instance count. For example, launching 10 p6-b300.48xlarge instances requires 1,920 vCPUs (10 × 192). Default GPU quotas are often set to 0 for new accounts, so request increases before attempting to deploy instances.

If you encounter quota limitations when creating Capacity Block reservations, launching On-Demand instances, or submitting Spot requests, contact AWS Support or your AWS account team to discuss your requirements and explore options for securing the accelerated compute capacity that best fits your needs.

## Use EC2 purchase options with Amazon EKS
<a name="use-purchase-options"></a>

After selecting an EC2 accelerated compute purchase option, configure your Amazon EKS cluster to use the capacity. Amazon EKS provides three provisioning methods, each with a different balance of control and automation:
+  **Amazon EKS Auto Mode**: AWS-managed compute that automatically provisions, scales, and patches nodes. Uses built-in Karpenter for provisioning and Bottlerocket operating system with NVIDIA drivers and device plugins included. Best when you want managed infrastructure with minimal operational overhead. Supports both static and dynamic capacity provisioning.
+  **Karpenter (self-managed)**: Open source upstream project that you install and operate in your Amazon EKS cluster. Provides the same provisioning model as EKS Auto Mode and you have full control over operating system, AMIs, kernel tuning, and node lifecycle. Best for platform teams with requirements that EKS Auto Mode doesn’t provide out-of-the-box.
+  **Node groups (managed and self-managed)**: Backed by EC2 Auto Scaling Groups (ASG), capacity is defined upfront through an EC2 launch template. Best for platform teams with existing EKS managed or self-managed node groups, and training workloads with predictable sizing with a known, static accelerated compute footprint.

The pages below cover each provisioning option in detail.
+  [Manage compute for AI/ML workloads with EKS Auto Mode and Karpenter](ml-node-pools.md) 
+  [Manage compute for AI/ML workloads on Amazon EKS with node groups](ml-node-groups.md) 

## Mixed strategy: combine purchase options
<a name="purchase-options-mixed-strategy"></a>

It’s common to combine multiple capacity purchase options within a single Amazon EKS cluster. This approach optimizes cost, availability, and reliability simultaneously by routing different workloads to the most appropriate capacity source. Customers implement this hybrid strategy using any of the three EKS compute management approaches (EKS Auto Mode, Karpenter, or Node Groups) or combine them within the same cluster.

EKS Auto Mode and Karpenter always provision reserved capacity (ODCRs and Capacity Blocks) first, followed by Spot or On-Demand. You can couple this instance provisioning priority by scheduling your critical workloads on reserved capacity and your flexible workloads on Spot or On-Demand instances. You control workload routing through Kubernetes-native scheduling primitives: `nodeSelector` targets a specific capacity type, taints and tolerations isolate NVIDIA GPU or AWS Trainium nodes, and `topologySpreadConstraints` distribute workloads across Availability Zones for high availability.

A well-designed Amazon EKS cluster organizes accelerated compute NodePools or node groups into two categories, Reserved and Burst, each aligned to the workload patterns best suited for the capacity strategy. An example is described below.
+  **Reserved Capacity**: A `gpu-reserved` NodePool or node group runs production inference and scheduled large-scale training on reserved capacity (ODCRs and Capacity Blocks) for SLA-bound services and planned compute-intensive jobs. This NodePool or node group serves inference and production workloads: real-time inference endpoints, production model serving, and business-critical applications that require always-on GPU availability with predictable performance. It also supports scheduled compute-intensive jobs: planned distributed training, large-scale fine-tuning experiments, time-bound research projects, and any workload where you know the start time and duration in advance.
+  **Burst Capacity**: A `gpu-burst` NodePool or node group handles experimentation, ad hoc workloads, and batch processing. It uses Spot instances as the primary capacity type with On-Demand fallback. This combination maximizes cost savings for fault-tolerant workloads and ensures capacity when Spot is unavailable. This NodePool or node group serves batch offline inference, data preprocessing pipelines, model evaluation jobs, development and prototyping, unpredictable inference scaling, short-lived debugging sessions, and any workload that implements checkpointing and can handle Spot interruptions or that doesn’t justify a reservation but cannot wait for reserved windows. Workloads on this NodePool or node group implement checkpointing and graceful shutdown to handle node loss within the 2-minute Spot interruption window.

Specify the desired capacity type for workloads using nodeSelector: `karpenter.sh/capacity-type: [spot, on-demand, reserved]`. Weight-based provisioning scales the cluster efficiently across all capacity pools. With this architecture, you can run diverse AI/ML workloads—from experimental notebooks to production inference—within a single Amazon EKS cluster while optimizing cost.