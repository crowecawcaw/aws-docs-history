

# COST06-BP02 Select resource type, size, and number based on data

 Base the type, size, and number of resources on evidence of the workload's compute, memory, throughput, and storage demands. Draw that evidence from a prior version of the workload, vendor documentation, published benchmarks, or a cost model. 

 **Desired outcome:** 
+  You size resources from measured or documented workload characteristics rather than estimates. 
+  Your sizing decisions account for multiple dimensions, including compute, memory, storage, and network, not a single dimension. 
+  You match workloads to purpose-built resource types when the workload profile justifies them. 
+  Your resource selections trace back to a named data source that another engineer can review. 

 **Common anti-patterns:** 
+  Allocating resources from unsubstantiated estimates. 
+  Sizing on a single characteristic, such as CPU, while ignoring memory, storage, or network. 
+  Choosing the largest available resource to avoid any risk of under-provisioning. 
+  Reusing a resource type from an unrelated workload because it is familiar. 

 **Benefits of establishing this best practice:** 
+  Workloads perform well under load without paying for capacity they do not use. 
+  Sizing decisions are defensible because they rest on documented evidence. 
+  Purpose-built resource types deliver better price performance than general-purpose equivalents for the workloads that fit them. 
+  Multi-dimensional analysis helps prevent a single overlooked requirement from causing a bottleneck. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A workload's profile spans compute, memory, storage, throughput, and network demands. Match resources to that profile without excess. The profile is rarely obvious before the workload runs, so without data, sizing tends toward the largest option. 

 Sizing on one visible dimension, such as high CPU, can miss the dimension that actually constrains the workload, such as memory. Resource families each target a different bottleneck: general purpose, compute optimized, memory optimized, storage optimized, and accelerated. To select the family, first identify the constraining dimension by evaluating all dimensions together. 

 The strongest evidence comes from a prior version of the workload, whether on-premises or in another environment, because it reflects real behavior. Without one, vendor documentation and published benchmarks provide a starting point. A cost model from earlier analysis maps expected usage to specific resource dimensions. With weaker sources, choose more conservatively and validate against real measurements sooner. 

 Many processor and instance types target specific workload shapes, such as machine learning training, high-throughput storage, or particular instruction sets. They deliver better price performance than general-purpose resources for those workloads. The cost is reduced flexibility, a purpose-built resource that no longer matches the workload is harder to repurpose. Prefer specialized options for stable, well-understood profiles. Keep general purpose when the profile is uncertain or changing. 

 Serverless and managed components expose fewer sizing knobs, and those knobs still drive cost. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-memory.html) cost scales with allocated memory. Test to find the best cost-performance setting. If a prior version of the function is already running, [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/supported-resources.html) recommends a memory size, narrowing the range to test. [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (Arm) processors lower cost for the same work on Lambda, AWS Fargate, and many instance families where your runtime supports Arm. 

 This best practice covers initial resource selection from data. To keep resources correctly sized as demand changes, see [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md). For each resource family's characteristics and use cases, see the [Amazon EC2 instance types documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Gather workload system requirements:** Document the workload's technical profile, including operating system, CPU and GPU core counts, system memory, storage type and capacity, network bandwidth, and any required processor type. Record the source for each figure so reviewers can judge its reliability. 

1.  **Identify the constraining dimension:** Analyze the requirements together to find which dimension limits the workload, rather than reacting to the most visible one. Use this to select the resource family, such as general purpose, compute optimized, memory optimized, storage optimized, or accelerated computing. 

1.  **Select type and size from data:** Use your cost model and workload data to choose a specific type and size within the family, setting virtual CPU count, memory, local and [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) storage, and network performance to match the required data transfer rate. Estimate the number of resources needed for the anticipated load. 

1.  **Prefer purpose-built resources for stable profiles:** When a [purpose-built processor or instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-types-processors) matches a well-understood workload, select it over a general-purpose equivalent for better price performance. Keep general purpose where the profile is uncertain or likely to change. 

1.  **Validate against cost and performance:** Confirm the selection against the cost model and, where possible, a benchmark under predicted load. Adjust the type, size, or number if measured behavior differs from the source data. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 
+  [COST06-BP03 Select resource type, size, and number automatically based on metrics](cost06-bp03.md) 
+  [COST05-BP03 Analyze the total cost of ownership of each component](cost05-bp03.md) 

 **Related documents:** 
+  [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) 
+  [Amazon EC2 processor types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-types-processors) 
+  [Optimizing your cost with rightsizing recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) 
+  [Amazon CloudWatch features](https://aws.amazon.com/cloudwatch/features/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - How well do you know EC2? (CMP356)](https://www.youtube.com/watch?v=sc_3hfucTnY) 
+  [How to use AWS Compute Optimizers new features](https://www.youtube.com/watch?v=jH0qCvMP7ms) 

 **Related examples:** 
+  [Choosing an AWS compute service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-compute-service.html) 
+  [Choosing an AWS storage service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/choosing-aws-storage-service.html) 
+  [Choosing an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/databases-on-aws-how-to-choose.html) 

 **Related workshops:** 
+  [CFM TIPs: Amazon EC2 compute playbook](https://catalog.workshops.aws/awscff/en-US/playbooks/compute/ec2) 