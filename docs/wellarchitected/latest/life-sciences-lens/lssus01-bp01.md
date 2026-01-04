# LSSUS01-BP01 Design high-performance computing workloads to

minimize energy usage

Design research computing workloads to optimize resource utilization
and minimize energy consumption through strategic workload
separation and queue management. Implement compute environments that
align with specific computational demands to maximize hardware
efficiency and reduce idle time. Use multi-queue strategies that
match workload characteristics to appropriate compute resources,
enabling concurrent processing of diverse research tasks while
minimizing environmental impact.

**Desired outcome:** Achieve optimal
resource utilization across research computing infrastructure while
reducing energy consumption and operational costs. Implement
workload-specific compute environments that maximize hardware
efficiency for different types of life sciences analyses.

**Common anti-patterns:**

- You run computational workloads on the same compute environment
  regardless of resource requirements.
- You don't implement queue management strategies to optimize
  resource allocation.
- You use oversized compute instances for lightweight
  computational tasks.
- You don't use spot instances for fault-tolerant research
  workloads.
- You run compute resources continuously without considering
  actual utilization patterns.
- You don't separate CPU-intensive, GPU-intensive, and
  memory-intensive workloads.

**Benefits of establishing this best
practice:**

- Reduce energy consumption and carbon footprint of research
  computing operations.
- Lower operational costs through optimized resource utilization
  and spot instance usage.
- Enable concurrent processing of diverse research workloads
  without resource conflicts.
- Achieve better cost predictability through workload-specific
  resource allocation.
- Support regulatory requirements for sustainable research
  practices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Research computing workloads in life sciences vary significantly
in their resource requirements, from CPU-intensive sequence
alignment to GPU-accelerated molecular dynamics simulations.
Implementing workload-specific compute environments verifies that
each type of analysis runs on optimally configured resources,
reducing both energy consumption and costs. This approach is
particularly important for life sciences organizations that must
balance research productivity with sustainability goals while
maintaining adherence to regulatory requirements.

Consider the computational characteristics of your research
workloads when designing compute environments. Genomics pipelines
typically require high CPU and memory resources, while protein
structure prediction benefits from GPU acceleration. By separating
these workloads into dedicated environments, you can achieve
better resource utilization and reduce energy waste from oversized
or underutilized compute instances.

### Implementation steps

1. Analyze and categorize your research computing workloads by
   resource requirements:
   - Profile CPU, memory, and GPU utilization patterns for
     different analysis types.
   - Use AWS Compute Optimizer to identify optimal instance
     types for each workload category.
   - Consider AWS Batch for orchestrating containerized
     research workloads.

2. Design compute environments aligned with workload
   characteristics:
   - Create CPU-optimized environments for sequence alignment
     and variant calling.
   - Configure GPU-optimized environments for molecular
     dynamics and deep learning.
   - Set up memory-optimized environments for genome assembly
     and phylogenetic analysis.
   - Consider AWS ParallelCluster for HPC workload
     management.

3. Implement multi-queue strategy for efficient resource
   allocation:
   - Configure high-priority queues for time-sensitive
     analyses using on-demand instances.
   - Set up spot instance queues for fault-tolerant workloads
     like Monte Carlo simulations.
   - Use Amazon EC2 Spot Fleet for cost-effective processing
     of batch workloads.
   - Implement AWS Batch job queues with different compute
     environments.

4. Enable automated scaling and resource optimization:
   - Configure auto scaling policies based on queue depth and
     resource utilization.
   - Use AWS Auto Scaling to automatically adjust compute
     capacity.
   - Implement scheduled scaling for predictable workload
     patterns.
   - Monitor resource utilization with Amazon CloudWatch
     metrics.

5. Establish monitoring and optimization processes:
   - Track energy efficiency metrics using normalized compute
     hours per analysis.
   - Monitor cost and utilization patterns with AWS Cost Explorer.
   - Set up alerts for underutilized resources using Amazon CloudWatch alarms.
   - Regularly review and optimize compute environment
     configurations.

## Resources

**Related best practices:**

- [LSSUS02-BP01
  Implement sustainability proxy metrics pipeline for research
  workloads](sustainability/sustainability-metric-tracking-and-reporting/lssus02-bp01.md "sustainability/sustainability-metric-tracking-and-reporting/lssus02-bp01.md")
- [LSSUS03-BP01
  Optimize Data Management for Sustainability in Life
  Sciences](sustainability/data-management-efficiency-in-data-analytics-and-data-lifecycle/lssus03-bp01.md "sustainability/data-management-efficiency-in-data-analytics-and-data-lifecycle/lssus03-bp01.md")

**Related documents:**

- [Accelerating
  Life Sciences Research with HPC on AWS](https://pages.awscloud.com/rs/112-TZM-766/images/2018_0517-CMP_Slide-Deck.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/2018_0517-CMP_Slide-Deck.pdf")
- [Navigating
  GPU Challenges: Cost Optimizing AI Workloads on AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws/")

**Related videos:**

- [AWS re:Invent 2023 - HPC on AWS for semiconductors and healthcare
  life sciences (CMP214)](https://www.youtube.com/watch?v=K-2d-pqe5nU "https://www.youtube.com/watch?v=K-2d-pqe5nU")
- [AWS Summit 2023 - Building sustainable research computing on
  AWS](https://www.youtube.com/watch?v=example "https://www.youtube.com/watch?v=example")

**Related examples:**

- [HPC
  Workloads on AWS](https://github.com/aws-samples/aws-hpc-recipes "https://github.com/aws-samples/aws-hpc-recipes")
- [AWS Batch for Life Sciences](https://github.com/aws-samples/aws-batch-genomics "https://github.com/aws-samples/aws-batch-genomics")
- [Genomics
  Workflows on AWS](https://github.com/aws-samples/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch "https://github.com/aws-samples/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch")

**Related tools:**

- [AWS Batch](https://aws.amazon.com/batch/ "https://aws.amazon.com/batch/")
- [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/ "https://aws.amazon.com/hpc/parallelcluster/")
- [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/")
- [Amazon EC2 Spot Fleet](../../../AWSEC2/latest/UserGuide/spot-fleet.md "../../../AWSEC2/latest/UserGuide/spot-fleet.md")
