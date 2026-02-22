# Specifications for Amazon EC2 high-performance computing instances

High-performance computing instances are purpose built to offer the best price performance
for running HPC workloads at scale on AWS. These instances are ideal for applications that
benefit from high-performance processors, such as large, complex simulations and deep learning
workloads.

###### Contents

- [Instance families and instance types](#hpc_sizes "#hpc_sizes")
- [Instance family summary](#hpc_summary "#hpc_summary")
- [Performance specifications](#hpc_hardware "#hpc_hardware")
- [Network specifications](#hpc_network "#hpc_network")
- [Amazon EBS specifications](#hpc_storage-ebs "#hpc_storage-ebs")
- [Instance store specifications](#hpc_instance-store "#hpc_instance-store")
- [Security specifications](#hpc_security "#hpc_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | ---------------- | ---------------- | ---------------- |
| Hpc6a           | `hpc6a.48xlarge`         |
| Hpc6id          | `hpc6id.32xlarge`        |
| Hpc7a           | `hpc7a.12xlarge`         | `hpc7a.24xlarge` | `hpc7a.48xlarge` | `hpc7a.96xlarge` |
| Hpc7g           | `hpc7g.4xlarge`          | `hpc7g.8xlarge`  | `hpc7g.16xlarge` |
| Hpc8a           | `hpc8a.96xlarge`         |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| Hpc6a           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Linux                       |
| Hpc6id          | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Windows                     | Linux |
| Hpc7a           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Windows                     | Linux |
| Hpc7g           | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Linux                       |
| Hpc8a           | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Windows                     | Linux |

## Performance specifications

| Instance type   | Memory (GiB) | Processor                | vCPUs | CPU cores | Threads per core | Accelerators | Accelerator memory |
| --------------- | ------------ | ------------------------ | ----- | --------- | ---------------- | ------------ | ------------------ |
| **Hpc6a**       |
| hpc6a.48xlarge  | 384.00       | AMD EPYC 7R13            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| **Hpc6id**      |
| hpc6id.32xlarge | 1024.00      | Intel Xeon Ice Lake      | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **Hpc7a**       |
| hpc7a.12xlarge  | 768.00       | AMD EPYC 9R14            | 24    | 24        | 1                | ✗ No         | ✗ No               |
| hpc7a.24xlarge  | 768.00       | AMD EPYC 9R14            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| hpc7a.48xlarge  | 768.00       | AMD EPYC 9R14            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| hpc7a.96xlarge  | 768.00       | AMD EPYC 9R14            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **Hpc7g**       |
| hpc7g.4xlarge   | 128.00       | AWS Graviton3E Processor | 16    | 16        | 1                | ✗ No         | ✗ No               |
| hpc7g.8xlarge   | 128.00       | AWS Graviton3E Processor | 32    | 32        | 1                | ✗ No         | ✗ No               |
| hpc7g.16xlarge  | 128.00       | AWS Graviton3E Processor | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **Hpc8a**       |
| hpc8a.96xlarge  | 768.00       | AMD EPYC 9R45            | 192   | 192       | 1                | ✗ No         | ✗ No               |

## Network specifications

| Instance type   | Baseline / Burst bandwidth (Gbps) | EFA   | ENA   | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| --------------- | --------------------------------- | ----- | ----- | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **Hpc6a**       |
| hpc6a.48xlarge  | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 2                       | 50                         | ✓ Yes |
| **Hpc6id**      |
| hpc6id.32xlarge | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 2                       | 50                         | ✓ Yes |
| **Hpc7a**       |
| hpc7a.12xlarge  | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 4                       | 50                         | ✓ Yes |
| hpc7a.24xlarge  | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 4                       | 50                         | ✓ Yes |
| hpc7a.48xlarge  | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 4                       | 50                         | ✓ Yes |
| hpc7a.96xlarge  | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 4                       | 50                         | ✓ Yes |
| **Hpc7g**       |
| hpc7g.4xlarge   | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 50                         | ✓ Yes |
| hpc7g.8xlarge   | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 50                         | ✓ Yes |
| hpc7g.16xlarge  | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 50                         | ✓ Yes |
| **Hpc8a**       |
| hpc8a.96xlarge  | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 2             | 4                       | 50                         | ✓ Yes |

###### Note

For `hpc6id.32xlarge`, you must attach at least 2 ENIs, to separate network
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 170 Gbps.

For `hpc7a.12xlarge`, `hpc7a.24xlarge`, `hpc7a.48xlarge`, `hpc7a.96xlarge`,
you must attach at least 2 ENIs, to separate network cards, to achieve 300 Gbps throughput. Each ENI attached to a network
card can achieve up to 150 Gbps.

## Amazon EBS specifications

The following table indicates which instance types are Amazon EBS optimized by default and which
optionally support it. It also describes their EBS-optimized performance, including dedicated bandwidth to Amazon EBS, the
typical maximum aggregate throughput that can be achieved on that dedicated connection with a streaming read workload
and 128 KiB I/O size, and the maximum IOPS the instance type can support when using a 16 KiB I/O size. Instance types
not listed do not support Amazon EBS optimization.

###### Important

An instance's EBS performance is bounded by the instance's performance limits, or the
aggregated performance of its attached volumes, whichever is smaller. To achieve maximum
EBS performance, an instance must have attached volumes that provide a combined performance
equal to or greater than the maximum instance performance. For example, to achieve
`80,000` IOPS for `r6i.16xlarge`, the instance must have at least
`5` `gp3` volumes provisioned with `16,000` IOPS each
(`5` volumes x `16,000` IOPS = `80,000` IOPS).

We recommend that you choose an EBS–optimized instance type that provides more
dedicated Amazon EBS throughput than your application needs; otherwise, the connection between
Amazon EBS and Amazon EC2 can become a performance bottleneck.

| Instance type     | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                              |
| ----------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hpc6a**         |
| hpc6a.48xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))    |
| **Hpc6id**        |
| hpc6id.32xlarge 1 | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))    |
| **Hpc7a**         |
| hpc7a.12xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | 27 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| hpc7a.24xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | 27 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| hpc7a.48xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | 27 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| hpc7a.96xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | 27 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **Hpc7g**         |
| hpc7g.4xlarge 1   | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))    |
| hpc7g.8xlarge 1   | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))    |
| hpc7g.16xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))    |
| **Hpc8a**         |
| hpc8a.96xlarge 1  | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11000.00                    | ✓ Yes | 27 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |

###### Note

1 These instances can support maximum performance for 30 minutes at least once every
24 hours, after which they revert to their baseline performance. Other instances can sustain the maximum performance
indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these
instances.

## Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

| Instance type   | Instance store volumes | Instance store type | 100% random read IOPS / Write IOPS | Needs initialization 1 | TRIM support 2 |
| --------------- | ---------------------- | ------------------- | ---------------------------------- | ---------------------- | -------------- |
| **Hpc6id**      |
| hpc6id.32xlarge | 4 x 3800 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type   | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| --------------- | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **Hpc6a**       |
| hpc6a.48xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **Hpc6id**      |
| hpc6id.32xlarge | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **Hpc7a**       |
| hpc7a.12xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| hpc7a.24xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| hpc7a.48xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| hpc7a.96xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Hpc7g**       |
| hpc7g.4xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| hpc7g.8xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| hpc7g.16xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Hpc8a**       |
| hpc8a.96xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
