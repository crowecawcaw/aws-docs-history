

# SUS03-BP04 Use purpose-built, energy efficient hardware tailored to your workload

 Software optimizations have diminishing returns when the underlying hardware isn't matched to the workload. AWS offers managed service features and [Amazon EC2](https://aws.amazon.com/ec2/) instance types to tailor the underlying hardware involved to the processing needs of a workload. For example, you can select several types of CPU architecture, purpose-built silicon for machine learning, instance storage options, or network adapter features. By selecting the right features for your workload, you can optimize the use of resources and energy and lower your environmental impact for workloads that are compute, storage, or network-bound while simultaneously improving performance and reducing costs. 

 **Desired outcome:** 
+  You run workloads on hardware suited to their specific needs, achieving higher energy and resource efficiency. 

 **Common anti-patterns:** 
+  Using only one processor architecture for all workloads, or not considering the processor architecture in instance selection decisions. 
+  Not considering accelerators for specialized workloads such as machine learning training and inference. 
+  Not monitoring usage patterns of different components to understand their utilization. 
+  Not re-evaluating hardware choices as new, more energy-efficient options become available. 

 **Benefits of establishing this best practice:** 
+  Matching hardware to the workload's dominant constraint (such as storage) means less over-provisioning of other resources (such as memory and compute). Less hardware demand results in lower associated Scope 3 emissions, from raw material extraction to end-of-life treatment. 
+  The choice of instance types that offload specific functions to dedicated hardware (such as the AWS Nitro System) results in better performance and fewer general-purpose CPU resources required to do the same. 
+  Validating the compatibility with other CPU or AI accelerator architectures broadens the choice and availability of instance types to run a workload. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Different workloads have different computational requirements. By matching each workload component with its ideal hardware architecture, you can reduce resource and energy consumption while improving performance and cost. Using purpose-built hardware effectively requires understanding your workload's constraints, testing compatibility, and developing a migration strategy for existing workloads. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Assess your workload's profile and specific needs: 
   +  Check the system requirements of your software stack for support of different CPU and GPU architectures. [AWS Graviton](https://aws.amazon.com/ec2/graviton/) based EC2 instances use up to 60% less energy for the same performance than comparable Amazon EC2 instances. You can [select the instruction set architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) for [AWS Lambda](https://aws.amazon.com/lambda/). 
   +  Identify energy-efficient hardware options in the AWS managed services you use, such as AWS Graviton-based instances for [Amazon RDS](https://aws.amazon.com/rds/), [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon ElastiCache](https://aws.amazon.com/elasticache/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), and [Amazon Redshift](https://aws.amazon.com/redshift/). These managed services shift the responsibility of running the workloads on AWS Graviton processors to AWS service teams. 
   +  Analyze the characteristics of your application (for instance, if they are CPU, network, or storage-bound with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics). 
   +  Identify specialized tasks such as machine learning inference or training, graphics rendering, or video transcoding that could benefit from purpose-built accelerators. 
   +  Evaluate containerization and virtualization layers that introduce a performance overhead. Consider benefits and trade-offs by reducing the level of abstractions in your hardware and software stack. 

1.  Select appropriate purpose-built silicon for compute-intensive tasks: 
   +  For AI training and inference workloads, consider [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/) and [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/) based instances, as well as NVIDIA GPU-powered EC2 instances. Optimize training and inference using the [AWS Neuron SDK](https://aws.amazon.com/ai/machine-learning/neuron/). 
   +  For graphics and general-purpose computing, consider NVIDIA GPUs and AMD GPUs. 
   +  For specialized computational needs, investigate Amazon EC2 F2 FPGA instances, which can be reprogrammed for specific algorithms. 

1.  Optimize networking and storage efficiency: 
   +  Use [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/), and [enhanced networking capabilities](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html) on supported instance types for higher bandwidth, lower latency, and lower CPU utilization. 
   +  Evaluate [storage options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html) for storage-intensive workloads. Consider instances with instance storage for storage-bound workloads. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 

 **Related documents:** 
+  [Specifications for Amazon EC2 accelerated computing instances](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html) 
+  [Instance Type Explorer](https://aws.amazon.com/ec2/instance-explorer/) 
+  [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/) 
+  [Get started quickly and easily using AWS Graviton](https://aws.amazon.com/ec2/graviton/fast-start/) 
+  [AWS Graviton Getting Started Guide](https://github.com/aws/aws-graviton-getting-started) 
+  [Migrating AWS Lambda functions to Arm-based AWS Graviton2 processors](https://aws.amazon.com/blogs/compute/migrating-aws-lambda-functions-to-arm-based-aws-graviton2-processors/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Deep Dive into the AWS Nitro System (CMP316)](https://www.youtube.com/watch?v=cD1mNQ9YbeA) 
+  [AWS re:Invent 2025 - AWS Graviton: The best price performance for your AWS workloads (CMP307)](https://www.youtube.com/watch?v=3Gt-30Fm38U) 

 **Related examples:** 
+  [Guidance for Optimizing Deep Learning Workloads for Sustainability on AWS](https://docs.aws.amazon.com/solutions/optimizing-deep-learning-workloads-for-sustainability-on-aws/) 
+  [Migrating Amazon Relational Database Service Databases to Graviton](https://catalog.workshops.aws/well-architected-sustainability/en-US/4-hardware-and-services/migrate-rds-to-graviton) 