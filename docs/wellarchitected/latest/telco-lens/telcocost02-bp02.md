# TELCOCOST02-BP02 Choose the most efficient compute resource

for your Network Function

When implementing cloud-based network functions (CNFs), it is important to benchmark your
applications on different compute types to determine the optimal balance of performance and
cost-efficiency. CNFs have diverse compute requirements, so gravitating to the lowest cost
option may result in poor performance. Older compute architectures and hardware can hamper
efficiency and drive-up expenses over time.

**Desired outcome:**

- Identify the most cost-effective compute resources that meet the performance
  requirements of your cloud-based network functions (CNFs).
- Optimize the balance between cost and performance for your CNF workloads.
- Avoid over-provisioning or under-provisioning of compute resources, which can lead to
  increased costs.

**Common anti-patterns:**

- Selecting compute resources solely based on the lowest cost, without considering
  performance requirements.
- Relying on outdated compute architectures and hardware that are less efficient and
  cost-effective.
- Lack of benchmarking and profiling of CNF workloads on different compute options.

**Benefits of establishing this best practice:**

- Significant cost savings by selecting the most optimal compute resources for your CNFs.
- Improved CNF performance and reliability by matching compute capabilities to workload
  needs.
- Enhanced operational efficiency by right-sizing compute resources to avoid
  over-provisioning.
- Increased agility in responding to changing compute requirements for your CNF
  workloads.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

When implementing cloud-based network functions (CNFs), it is crucial to carefully
evaluate the compute resource options to strike the right balance between cost and
performance. CNFs often have diverse compute requirements, and simply selecting the
lowest-cost compute option may result in poor performance and sub-optimal outcomes.

By benchmarking your CNF applications on different compute types, you can identify the
most efficient resources that meet your performance needs. This may involve evaluating various
AWS compute services, such as Amazon EC2 instances with different processor architectures, memory
configurations, and storage options. Older compute architectures and hardware can also hamper
efficiency and drive-up expenses over time, so it is important to consider the long-term costs
and benefits of your compute choices.

The goal is to optimize the cost-performance tradeoff for your CNF workloads, verifying
you are not over-provisioning or under-provisioning compute resources, which can lead to
increased costs.

### Implementation steps

- Profile the performance and resource utilization characteristics of your
  cloud-based network functions (CNFs).
- Benchmark your CNF applications on a variety of AWS compute instances, including
  different processor architectures, memory configurations, and storage options.
- Analyze the performance and cost data to identify the most efficient compute
  resources that meet your CNF's requirements.
- Consider the long-term implications of your compute choices, evaluating factors
  like energy efficiency, hardware lifecycle, and future performance trends.
- Implement mechanisms to dynamically adjust the compute resources allocated to your
  CNFs based on changing demands and workload characteristics.
- Continuously monitor and optimize your CNF compute resource allocations to verify
  cost-effectiveness while maintaining performance.

## Resources

**Key AWS services:**

- [Amazon EC2](https://aws.amazon.com/pm/ec2/ "https://aws.amazon.com/pm/ec2/")
- [AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/ "https://aws.amazon.com/ec2/graviton/")
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/")
