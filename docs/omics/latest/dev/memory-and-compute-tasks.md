# Compute and memory requirements for HealthOmics tasks

HealthOmics runs your private workflow tasks in an omics instance. HealthOmics provides a variety of instance types to
accommodate different types of tasks. Each instance type has a fixed memory and vCPU configuration (and fixed GPU
configuration for accelerated computing instance types). The cost of using an omics instance varies depending on
the instance type. For details, see the [HealthOmics Pricing](https://aws.amazon.com/healthomics/pricing/ "https://aws.amazon.com/healthomics/pricing/")
page.

For tasks in a workflow, you specify the required memory and vCPUs in the workflow definition file. When a
workflow task runs, HealthOmics allocates the smallest omics instance that accommodates the requested memory and vCPUs.
For example, if a task needs 64 GiB of memory and 8 vCPUs, HealthOmics selects `omics.r.2xlarge`.

We recommend that you review the instance types and set your requested vCPUs and memory size to match the
instance that best meets your needs. The task container uses the number of vCPUs and the memory size that you
specify in your workflow definition file, even if the instance type has additional vCPUs and memory.

The following list contains additional information about vCPU and memory allocation:

- Container resource allocations are hard limits. If a task runs out of memory or attempts to use additional vCPUs ,
  the task generates an error log and exits.
- If you don’t specify any compute or memory requirements, HealthOmics selects **omics.c.large** and defaults to a
  configuration with 1 vCPU and 1 GiB of memory.
- The minimum configuration that you can request is 1 vCPU and 1 GiB of memory.
- If you specify vCPUs, memory, or GPUs that exceeds the supported instance types, HealthOmics throws an error
  message and the workflow fails validations
- If you specify fractional units, HealthOmics rounds up to the nearest integer.
- HealthOmics reserves a small amount of memory (5%) for management and logging agents, so the full memory allocation might
  not always be available to the application in the task.
- HealthOmics matches instance types to fit the compute and memory requirements that you specify, and may use a mix of
  hardware generations. For this reason, there can be some minor variances in task run times for the same
  task.
  These topics provide details about the instance types that HealthOmics supports.

###### Topics

- [Standard instance types](#workflow-task-standard-instances "#workflow-task-standard-instances")
- [Compute-optimized instances](#workflow-task-compute-optimized-instances "#workflow-task-compute-optimized-instances")
- [Memory-optimized instances](#workflow-task-memory-optimized-instances "#workflow-task-memory-optimized-instances")
- [Accelerated-computing instances](#workflow-task-accelerated-computing-instances "#workflow-task-accelerated-computing-instances")

###### Note

For standard, compute, and memory optimized instances, increase the instance bandwidth size if the instance requires a higher
throughput. Amazon EC2 instances with fewer than 16 vCPUs (size 4xl and smaller) can experience throughput bursting. For more information
on Amazon EC2 instance throughput, see
[Amazon EC2 available instance bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md#available-instance-bandwidth "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md#available-instance-bandwidth").

## Standard instance types

For standard instance types, the configurations aim for a balance of compute power and memory.

HealthOmics supports the 32xlarge and 48xlarge instances in these regions: US West (Oregon) and US East (N.
Virginia).

| Instance         | Number of vCPUs | Memory  |
| ---------------- | --------------- | ------- |
| omics.m.large    | 2               | 8 GiB   |
| omics.m.xlarge   | 4               | 16 GiB  |
| omics.m.2xlarge  | 8               | 32 GiB  |
| omics.m.4xlarge  | 16              | 64 GiB  |
| omics.m.8xlarge  | 32              | 128 GiB |
| omics.m.12xlarge | 48              | 192 GiB |
| omics.m.16xlarge | 64              | 256 GiB |
| omics.m.24xlarge | 96              | 384 GiB |
| omics.m.32xlarge | 128             | 512 GiB |
| omics.m.48xlarge | 192             | 768 GiB |

## Compute-optimized instances

For compute-optimized instance types, the configurations have more compute power and less memory.

HealthOmics supports the 32xlarge and 48xlarge instances in these regions: US West (Oregon) and US East (N.
Virginia).

| Instance         | Number of vCPUs | Memory  |
| ---------------- | --------------- | ------- |
| omics.c.large    | 2               | 4 GiB   |
| omics.c.xlarge   | 4               | 8 GiB   |
| omics.c.2xlarge  | 8               | 16 GiB  |
| omics.c.4xlarge  | 16              | 32 GiB  |
| omics.c.8xlarge  | 32              | 64 GiB  |
| omics.c.12xlarge | 48              | 96 GiB  |
| omics.c.16xlarge | 64              | 128 GiB |
| omics.c.24xlarge | 96              | 192 GiB |
| omics.c.32xlarge | 128             | 256 GiB |
| omics.c.48xlarge | 192             | 384 GiB |

## Memory-optimized instances

For memory-optimized instance types, the configurations have less compute power and more memory.

HealthOmics supports the 32xlarge and 48xlarge instances in these regions: US West (Oregon) and US East (N.
Virginia).

| Instance         | Number of vCPUs | Memory   |
| ---------------- | --------------- | -------- |
| omics.r.large    | 2               | 16 GiB   |
| omics.r.xlarge   | 4               | 32 GiB   |
| omics.r.2xlarge  | 8               | 64 GiB   |
| omics.r.4xlarge  | 16              | 128 GiB  |
| omics.r.8xlarge  | 32              | 256 GiB  |
| omics.r.12xlarge | 48              | 384 GiB  |
| omics.r.16xlarge | 64              | 512 GiB  |
| omics.r.24xlarge | 96              | 768 GiB  |
| omics.r.32xlarge | 128             | 1024 GiB |
| omics.r.48xlarge | 192             | 1536 GiB |

## Accelerated-computing instances

You can optionally specify GPU resources for each task in a workflow, so that HealthOmics
allocates an accelerated-computing instance for the task. For information on how to specify the GPU information in
the workflow definition file, see [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md").

If you specify a GPU that supports multiple instance types, HealthOmics selects the instance type based on
availability. If both instance types are available, HealthOmics gives preference to the lower cost instance.

G4 instances aren't supported in the Israel (Tel Aviv) Region. G5 instances aren't support in the Asia Pacific (Singapore) Region.

###### Topics

- [G6 and G6e instance types](#workflow-task-accelerated-accelerated-g6 "#workflow-task-accelerated-accelerated-g6")
- [G4 and G5 instances](#workflow-task-accelerated-accelerated-g45 "#workflow-task-accelerated-accelerated-g45")

### G6 and G6e instance types

HealthOmics supports the following G6 accelerated-computing instance configurations. All omics.g6 instances use
Nvidia L4 or Nvidia L4 A10G GPUs.

HealthOmics supports the G6 and G6e instances in these regions: US West (Oregon) and US East (N. Virginia).

| Instance          | Number of vCPUs | Memory  | Number of GPUs | GPU memory |
| ----------------- | --------------- | ------- | -------------- | ---------- |
| omics.g6.xlarge   | 4               | 16 GiB  | 1              | 48 GiB     |
| omics.g6.2xlarge  | 8               | 32 GiB  | 1              | 48 GiB     |
| omics.g6.4xlarge  | 16              | 64 GiB  | 1              | 48 GiB     |
| omics.g6.8xlarge  | 32              | 128 GiB | 1              | 48 GiB     |
| omics.g6.12xlarge | 48              | 192 GiB | 4              | 192 GiB    |
| omics.g6.16xlarge | 64              | 256 GiB | 1              | 48 GiB     |
| omics.g6.24xlarge | 96              | 192 GiB | 4              | 192 GiB    |

All omics.g6e instances use Nvidia L40s GPUs.

| Instance           | Number of vCPUs | Memory  | Number of GPUs | GPU memory |
| ------------------ | --------------- | ------- | -------------- | ---------- |
| omics.g6e.xlarge   | 4               | 32 GiB  | 1              | 24 GiB     |
| omics.g6e.2xlarge  | 8               | 64 GiB  | 1              | 24 GiB     |
| omics.g6e.4xlarge  | 16              | 128 GiB | 1              | 24 GiB     |
| omics.g6e.8xlarge  | 32              | 256 GiB | 1              | 24 GiB     |
| omics.g6e.12xlarge | 48              | 384 GiB | 4              | 96 GiB     |
| omics.g6e.16xlarge | 64              | 512 GiB | 1              | 96 GiB     |
| omics.g6e.24xlarge | 96              | 768 GiB | 4              | 96 GiB     |

### G4 and G5 instances

HealthOmics supports the following G4 and G5 accelerated-computing instance configurations.

All omics.g5 instances use Nvidia L4 A10G, Nvidia Tesla A10G, or Nvidia Tesla T4 A10G GPUs.

| Instance          | Number of vCPUs | Memory  | Number of GPUs | GPU memory |
| ----------------- | --------------- | ------- | -------------- | ---------- |
| omics.g5.xlarge   | 4               | 16 GiB  | 1              | 24 GiB     |
| omics.g5.2xlarge  | 8               | 32 GiB  | 1              | 24 GiB     |
| omics.g5.4xlarge  | 16              | 64 GiB  | 1              | 24 GiB     |
| omics.g5.8xlarge  | 32              | 128 GiB | 1              | 24 GiB     |
| omics.g5.12xlarge | 48              | 192 GiB | 4              | 96 GiB     |
| omics.g5.16xlarge | 64              | 256 GiB | 1              | 24 GiB     |
| omics.g5.24xlarge | 96              | 384 GiB | 4              | 96 GiB     |

All omics.g4dn instances use Nvidia Tesla T4 or Nvidia Tesla T4 A10G GPUs.

| Instance            | Number of vCPUs | Memory  | Number of GPUs | GPU memory |
| ------------------- | --------------- | ------- | -------------- | ---------- |
| omics.g4dn.xlarge   | 4               | 16 GiB  | 1              | 16 GiB     |
| omics.g4dn.2xlarge  | 8               | 32 GiB  | 1              | 16 GiB     |
| omics.g4dn.4xlarge  | 16              | 64 GiB  | 1              | 16 GiB     |
| omics.g4dn.8xlarge  | 32              | 128 GiB | 1              | 16 GiB     |
| omics.g4dn.12xlarge | 48              | 192 GiB | 4              | 64 GiB     |
| omics.g4dn.16xlarge | 64              | 256 GiB | 1              | 24 GiB     |
