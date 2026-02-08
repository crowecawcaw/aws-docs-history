# MSFTCOST03-BP06 Evaluate Optimize CPU feature

Optimize CPUs for Amazon EC2 Instances provides customers greater
control of your EC2 instances on two fronts. First, you can specify
a custom number of vCPUs to save on vCPU-based licensing costs (such
as SQL Server). Second, you can disable multithreading for workloads
that perform well with single-threaded CPUs, like certain
high-performance computing (HPC) applications. Reducing the number
of vCPUs or disabling multithreading offers fewer cores to your SQL
Server workload on EC2 without affecting the other compute resources
available to the machine (such as RAM and storage), and most of the
time without compromising the workload performance. This feature is
available for both Bring Your Own License (BYOL) and License
Included (LI) deployments.

**Desired outcome:** By evaluating
and implementing CPU optimization for Amazon EC2 instances, we aim
to reduce vCPU-based licensing costs for SQL Server while
maintaining workload performance. This will be achieved by
specifying custom vCPU counts and, where appropriate, disabling
multithreading. The outcome will be a more cost-effective
utilization of resources, particularly for SQL Server workloads,
without compromising on performance or available compute resources
such as RAM and storage.

**Common anti-patterns:**

- Over-provisioning vCPUs: Organizations often provision EC2
  instances with more vCPUs than necessary for their SQL Server
  workloads, believing that more is better. This leads to
  unnecessarily high licensing costs for vCPU-based software like
  SQL Server, without providing any tangible performance benefits.
  The excess vCPUs remain unused while still incurring licensing
  fees.
- Ignoring multithreading optimization: Many teams leave
  multithreading enabled by default for all workloads, including
  those that do not benefit from it (such as certain HPC
  applications or single-threaded workloads). This can result in
  suboptimal performance for these specific workloads and
  potentially higher licensing costs, as some software is licensed
  per logical processor rather than physical core.

**Benefits of establishing this best
practice:**

- Reduced SQL Server licensing costs through optimized vCPU
  allocation and core usage, resulting in direct cost savings.
- Better workload performance by matching CPU configurations to
  specific needs, especially for single-threaded applications and
  HPC workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start by analyzing your SQL Server workload performance and
resource utilization. Use AWS tools like CloudWatch to gather
metrics. Identify instances where you can reduce vCPU count
without impacting performance. Set instances with custom vCPU
counts to match your licensing. Test disabling multithreading for
workloads that benefit from single-threaded performance. Monitor
performance closely after changes to ensure workload efficiency is
maintained. Regularly review and adjust your configurations as
workload demands evolve.

### Implementation steps

1. Analyze current SQL Server workload performance and resource
   utilization using AWS CloudWatch and other monitoring tools.
2. Set EC2 instances with custom vCPU counts that align with
   your SQL Server licensing and workload requirements.
3. Test and implement multithreading disablement for workloads
   that perform better with single-threaded CPUs, monitoring
   performance before and after the change.

## Resources

**Related documents:**

- [CPU
  options for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md "../../../AWSEC2/latest/UserGuide/instance-optimize-cpu.md")
- [Optimize
  CPUs for License-Included instances](../../../AWSEC2/latest/UserGuide/optimize-cpu.md "../../../AWSEC2/latest/UserGuide/optimize-cpu.md")
- [Optimize
  CPU best practices for SQL Server workloads](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpu-best-practices-for-sql-server-workloads/ "https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpu-best-practices-for-sql-server-workloads/")
- [Optimize
  CPUs best practices for SQL Server workloads –
  continued](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/ "https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/")
