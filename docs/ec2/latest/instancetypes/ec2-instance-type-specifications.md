# Amazon EC2 instance type specifications

Amazon EC2 provides a wide selection of instance types optimized to fit different use cases.
Instance types comprise varying combinations of CPU, memory, storage, and networking capacity
and give you the flexibility to choose the appropriate mix of resources for your applications.
Each instance type includes one or more instance sizes, allowing you to scale your resources
to the requirements of your target workload.

We group EC2 instance into the following categories:

- General purpose – Provide a balance of compute,
  memory, and networking resources. These instances are ideal for applications that use
  these resources in equal proportions, such as web servers and code repositories.

Burstable performance – The T instance family
is also referred to as burstable performance instances. These instances provide a baseline
CPU performance with the ability to burst above the baseline at any time. For more information, see
[Burstable performance instances](../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md")
in the _Amazon EC2 User Guide_.

- Compute optimized – Designed for compute intensive
  applications that benefit from high performance processors. These instances are ideal
  for batch processing workloads, media transcoding, high performance web servers, high
  performance computing (HPC), scientific modeling, dedicated gaming servers, ad server
  engines, and machine learning inference.
- Memory optimized – Designed to deliver fast
  performance for workloads that process large data sets in memory.
- Storage optimized – Designed for workloads that
  require high, sequential read and write access to very large data sets on local storage.
  They are optimized to deliver tens of thousands of low-latency, random I/O operations
  per second (IOPS) to applications.
- Accelerated computing – Use hardware accelerators,
  or co-processors, to perform functions, such as floating point number calculations,
  graphics processing, or data pattern matching, more efficiently than is possible in
  software running on CPUs.
- High-performance computing – Purpose built to offer the best
  price performance for running HPC workloads at scale on AWS. These instances are ideal
  for applications that benefit from high-performance processors, such as large, complex
  simulations and deep learning workloads.
- Previous generation – AWS offers previous
  generation instance types for users who have optimized their applications around them
  and have yet to upgrade. We encourage you to use current generation instance types to
  get the best performance, but we continue to support previous generation instance
  types.
  To determine which instance types meet your requirements, such as supported Regions,
  compute resources, or storage resources, see [Find an Amazon EC2 instance type](../../../AWSEC2/latest/UserGuide/instance-discovery.md "../../../AWSEC2/latest/UserGuide/instance-discovery.md") in the _Amazon EC2 User Guide_.

###### Categories

- [General purpose](gp.md "gp.md")
- [Compute optimized](co.md "co.md")
- [Memory optimized](mo.md "mo.md")
- [Storage optimized](so.md "so.md")
- [Accelerated computing](ac.md "ac.md")
- [High-performance computing](hpc.md "hpc.md")
- [Previous generation](pg.md "pg.md")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").
