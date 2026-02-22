# Specifications for Amazon EC2 compute optimized instances

Compute optimized instances are designed for compute intensive applications that benefit
from high performance processors. These instances are ideal for batch processing workloads,
media transcoding, high performance web servers, high performance computing (HPC), scientific
modeling, dedicated gaming servers, ad server engines, and machine learning inference.

For information on previous generation instance types of this category, such as C4 instances,
see [Specifications for Amazon EC2 previous generation instances](pg.md "pg.md").

###### Contents

- [Instance families and instance types](#co_sizes "#co_sizes")
- [Instance family summary](#co_summary "#co_summary")
- [Performance specifications](#co_hardware "#co_hardware")
- [Network specifications](#co_network "#co_network")
- [Amazon EBS specifications](#co_storage-ebs "#co_storage-ebs")
- [Instance store specifications](#co_instance-store "#co_instance-store")
- [Security specifications](#co_security "#co_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | ----------------- | ------------------ | ------------------ | ------------------ | ------------------- | ------------------- | --------------- | --------------- | ---------------- | ----------------- | ----------------- | ----------------- |
| C5              | `c5.large`               | `c5.xlarge`       | `c5.2xlarge`       | `c5.4xlarge`       | `c5.9xlarge`       | `c5.12xlarge`       | `c5.18xlarge`       | `c5.24xlarge`   | `c5.metal`      |
| C5a             | `c5a.large`              | `c5a.xlarge`      | `c5a.2xlarge`      | `c5a.4xlarge`      | `c5a.8xlarge`      | `c5a.12xlarge`      | `c5a.16xlarge`      | `c5a.24xlarge`  |
| C5ad            | `c5ad.large`             | `c5ad.xlarge`     | `c5ad.2xlarge`     | `c5ad.4xlarge`     | `c5ad.8xlarge`     | `c5ad.12xlarge`     | `c5ad.16xlarge`     | `c5ad.24xlarge` |
| C5d             | `c5d.large`              | `c5d.xlarge`      | `c5d.2xlarge`      | `c5d.4xlarge`      | `c5d.9xlarge`      | `c5d.12xlarge`      | `c5d.18xlarge`      | `c5d.24xlarge`  | `c5d.metal`     |
| C5n             | `c5n.large`              | `c5n.xlarge`      | `c5n.2xlarge`      | `c5n.4xlarge`      | `c5n.9xlarge`      | `c5n.18xlarge`      | `c5n.metal`         |
| C6a             | `c6a.large`              | `c6a.xlarge`      | `c6a.2xlarge`      | `c6a.4xlarge`      | `c6a.8xlarge`      | `c6a.12xlarge`      | `c6a.16xlarge`      | `c6a.24xlarge`  | `c6a.32xlarge`  | `c6a.48xlarge`   | `c6a.metal`       |
| C6g             | `c6g.medium`             | `c6g.large`       | `c6g.xlarge`       | `c6g.2xlarge`      | `c6g.4xlarge`      | `c6g.8xlarge`       | `c6g.12xlarge`      | `c6g.16xlarge`  | `c6g.metal`     |
| C6gd            | `c6gd.medium`            | `c6gd.large`      | `c6gd.xlarge`      | `c6gd.2xlarge`     | `c6gd.4xlarge`     | `c6gd.8xlarge`      | `c6gd.12xlarge`     | `c6gd.16xlarge` | `c6gd.metal`    |
| C6gn            | `c6gn.medium`            | `c6gn.large`      | `c6gn.xlarge`      | `c6gn.2xlarge`     | `c6gn.4xlarge`     | `c6gn.8xlarge`      | `c6gn.12xlarge`     | `c6gn.16xlarge` |
| C6i             | `c6i.large`              | `c6i.xlarge`      | `c6i.2xlarge`      | `c6i.4xlarge`      | `c6i.8xlarge`      | `c6i.12xlarge`      | `c6i.16xlarge`      | `c6i.24xlarge`  | `c6i.32xlarge`  | `c6i.metal`      |
| C6id            | `c6id.large`             | `c6id.xlarge`     | `c6id.2xlarge`     | `c6id.4xlarge`     | `c6id.8xlarge`     | `c6id.12xlarge`     | `c6id.16xlarge`     | `c6id.24xlarge` | `c6id.32xlarge` | `c6id.metal`     |
| C6in            | `c6in.large`             | `c6in.xlarge`     | `c6in.2xlarge`     | `c6in.4xlarge`     | `c6in.8xlarge`     | `c6in.12xlarge`     | `c6in.16xlarge`     | `c6in.24xlarge` | `c6in.32xlarge` | `c6in.metal`     |
| C7a             | `c7a.medium`             | `c7a.large`       | `c7a.xlarge`       | `c7a.2xlarge`      | `c7a.4xlarge`      | `c7a.8xlarge`       | `c7a.12xlarge`      | `c7a.16xlarge`  | `c7a.24xlarge`  | `c7a.32xlarge`   | `c7a.48xlarge`    | `c7a.metal-48xl`  |
| C7g             | `c7g.medium`             | `c7g.large`       | `c7g.xlarge`       | `c7g.2xlarge`      | `c7g.4xlarge`      | `c7g.8xlarge`       | `c7g.12xlarge`      | `c7g.16xlarge`  | `c7g.metal`     |
| C7gd            | `c7gd.medium`            | `c7gd.large`      | `c7gd.xlarge`      | `c7gd.2xlarge`     | `c7gd.4xlarge`     | `c7gd.8xlarge`      | `c7gd.12xlarge`     | `c7gd.16xlarge` | `c7gd.metal`    |
| C7gn            | `c7gn.medium`            | `c7gn.large`      | `c7gn.xlarge`      | `c7gn.2xlarge`     | `c7gn.4xlarge`     | `c7gn.8xlarge`      | `c7gn.12xlarge`     | `c7gn.16xlarge` | `c7gn.metal`    |
| C7i             | `c7i.large`              | `c7i.xlarge`      | `c7i.2xlarge`      | `c7i.4xlarge`      | `c7i.8xlarge`      | `c7i.12xlarge`      | `c7i.16xlarge`      | `c7i.24xlarge`  | `c7i.48xlarge`  | `c7i.metal-24xl` | `c7i.metal-48xl`  |
| C7i-flex        | `c7i-flex.large`         | `c7i-flex.xlarge` | `c7i-flex.2xlarge` | `c7i-flex.4xlarge` | `c7i-flex.8xlarge` | `c7i-flex.12xlarge` | `c7i-flex.16xlarge` |
| C8a             | `c8a.medium`             | `c8a.large`       | `c8a.xlarge`       | `c8a.2xlarge`      | `c8a.4xlarge`      | `c8a.8xlarge`       | `c8a.12xlarge`      | `c8a.16xlarge`  | `c8a.24xlarge`  | `c8a.48xlarge`   | `c8a.metal-24xl`  | `c8a.metal-48xl`  |
| C8g             | `c8g.medium`             | `c8g.large`       | `c8g.xlarge`       | `c8g.2xlarge`      | `c8g.4xlarge`      | `c8g.8xlarge`       | `c8g.12xlarge`      | `c8g.16xlarge`  | `c8g.24xlarge`  | `c8g.48xlarge`   | `c8g.metal-24xl`  | `c8g.metal-48xl`  |
| C8gb            | `c8gb.medium`            | `c8gb.large`      | `c8gb.xlarge`      | `c8gb.2xlarge`     | `c8gb.4xlarge`     | `c8gb.8xlarge`      | `c8gb.12xlarge`     | `c8gb.16xlarge` | `c8gb.24xlarge` | `c8gb.48xlarge`  | `c8gb.metal-24xl` | `c8gb.metal-48xl` |
| C8gd            | `c8gd.medium`            | `c8gd.large`      | `c8gd.xlarge`      | `c8gd.2xlarge`     | `c8gd.4xlarge`     | `c8gd.8xlarge`      | `c8gd.12xlarge`     | `c8gd.16xlarge` | `c8gd.24xlarge` | `c8gd.48xlarge`  | `c8gd.metal-24xl` | `c8gd.metal-48xl` |
| C8gn            | `c8gn.medium`            | `c8gn.large`      | `c8gn.xlarge`      | `c8gn.2xlarge`     | `c8gn.4xlarge`     | `c8gn.8xlarge`      | `c8gn.12xlarge`     | `c8gn.16xlarge` | `c8gn.24xlarge` | `c8gn.48xlarge`  | `c8gn.metal-24xl` | `c8gn.metal-48xl` |
| C8i             | `c8i.large`              | `c8i.xlarge`      | `c8i.2xlarge`      | `c8i.4xlarge`      | `c8i.8xlarge`      | `c8i.12xlarge`      | `c8i.16xlarge`      | `c8i.24xlarge`  | `c8i.32xlarge`  | `c8i.48xlarge`   | `c8i.96xlarge`    | `c8i.metal-48xl`  | `c8i.metal-96xl`  |
| C8id            | `c8id.large`             | `c8id.xlarge`     | `c8id.2xlarge`     | `c8id.4xlarge`     | `c8id.8xlarge`     | `c8id.12xlarge`     | `c8id.16xlarge`     | `c8id.24xlarge` | `c8id.32xlarge` | `c8id.48xlarge`  | `c8id.96xlarge`   | `c8id.metal-48xl` | `c8id.metal-96xl` |
| C8i-flex        | `c8i-flex.large`         | `c8i-flex.xlarge` | `c8i-flex.2xlarge` | `c8i-flex.4xlarge` | `c8i-flex.8xlarge` | `c8i-flex.12xlarge` | `c8i-flex.16xlarge` |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| C5              | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C5a             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| C5ad            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| C5d             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C5n             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| C6a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C6g             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C6gd            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C6gn            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C6i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C6id            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C6in            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C7a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C7g             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C7gd            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C7gn            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C7i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C7i-flex        | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C8a             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C8g             | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C8gb            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C8gd            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C8gn            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| C8i             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C8id            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| C8i-flex        | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |

## Performance specifications

| Instance type     | Memory (GiB) | Processor                          | vCPUs | CPU cores | Threads per core | Accelerators | Accelerator memory |
| ----------------- | ------------ | ---------------------------------- | ----- | --------- | ---------------- | ------------ | ------------------ |
| **C5**            |
| c5.large          | 4.00         | Intel Xeon Platinum 8124M          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c5.xlarge         | 8.00         | Intel Xeon Platinum 8124M          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c5.2xlarge        | 16.00        | Intel Xeon Platinum 8124M          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c5.4xlarge        | 32.00        | Intel Xeon Platinum 8124M          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c5.9xlarge        | 72.00        | Intel Xeon Platinum 8124M          | 36    | 18        | 2                | ✗ No         | ✗ No               |
| c5.12xlarge       | 96.00        | 2nd Gen Intel Xeon Platinum 8275CL | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c5.18xlarge       | 144.00       | Intel Xeon Platinum 8124M          | 72    | 36        | 2                | ✗ No         | ✗ No               |
| c5.24xlarge       | 192.00       | 2nd Gen Intel Xeon Platinum 8275CL | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c5.metal          | 192.00       | 2nd Gen Intel Xeon Platinum 8275CL | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **C5a**           |
| c5a.large         | 4.00         | 2nd Gen AMD EPYC 7R32              | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c5a.xlarge        | 8.00         | 2nd Gen AMD EPYC 7R32              | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c5a.2xlarge       | 16.00        | 2nd Gen AMD EPYC 7R32              | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c5a.4xlarge       | 32.00        | 2nd Gen AMD EPYC 7R32              | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c5a.8xlarge       | 64.00        | 2nd Gen AMD EPYC 7R32              | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c5a.12xlarge      | 96.00        | 2nd Gen AMD EPYC 7R32              | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c5a.16xlarge      | 128.00       | 2nd Gen AMD EPYC 7R32              | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c5a.24xlarge      | 192.00       | 2nd Gen AMD EPYC 7R32              | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **C5ad**          |
| c5ad.large        | 4.00         | 2nd Gen AMD EPYC 7R32              | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c5ad.xlarge       | 8.00         | 2nd Gen AMD EPYC 7R32              | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c5ad.2xlarge      | 16.00        | 2nd Gen AMD EPYC 7R32              | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c5ad.4xlarge      | 32.00        | 2nd Gen AMD EPYC 7R32              | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c5ad.8xlarge      | 64.00        | 2nd Gen AMD EPYC 7R32              | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c5ad.12xlarge     | 96.00        | 2nd Gen AMD EPYC 7R32              | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c5ad.16xlarge     | 128.00       | 2nd Gen AMD EPYC 7R32              | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c5ad.24xlarge     | 192.00       | 2nd Gen AMD EPYC 7R32              | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **C5d**           |
| c5d.large         | 4.00         | Intel Xeon Platinum 8124M          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c5d.xlarge        | 8.00         | Intel Xeon Platinum 8124M          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c5d.2xlarge       | 16.00        | Intel Xeon Platinum 8124M          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c5d.4xlarge       | 32.00        | Intel Xeon Platinum 8124M          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c5d.9xlarge       | 72.00        | Intel Xeon Platinum 8124M          | 36    | 18        | 2                | ✗ No         | ✗ No               |
| c5d.12xlarge      | 96.00        | 2nd Gen Intel Xeon Platinum 8275CL | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c5d.18xlarge      | 144.00       | Intel Xeon Platinum 8124M          | 72    | 36        | 2                | ✗ No         | ✗ No               |
| c5d.24xlarge      | 192.00       | 2nd Gen Intel Xeon Platinum 8275CL | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c5d.metal         | 192.00       | 2nd Gen Intel Xeon Platinum 8275CL | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **C5n**           |
| c5n.large         | 5.25         | Intel Xeon Platinum 8124M          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c5n.xlarge        | 10.50        | Intel Xeon Platinum 8124M          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c5n.2xlarge       | 21.00        | Intel Xeon Platinum 8124M          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c5n.4xlarge       | 42.00        | Intel Xeon Platinum 8124M          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c5n.9xlarge       | 96.00        | Intel Xeon Platinum 8124M          | 36    | 18        | 2                | ✗ No         | ✗ No               |
| c5n.18xlarge      | 192.00       | Intel Xeon Platinum 8124M          | 72    | 36        | 2                | ✗ No         | ✗ No               |
| c5n.metal         | 192.00       | Intel Xeon Platinum 8124M          | 72    | 36        | 2                | ✗ No         | ✗ No               |
| **C6a**           |
| c6a.large         | 4.00         | AMD EPYC 7R13                      | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c6a.xlarge        | 8.00         | AMD EPYC 7R13                      | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c6a.2xlarge       | 16.00        | AMD EPYC 7R13                      | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c6a.4xlarge       | 32.00        | AMD EPYC 7R13                      | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c6a.8xlarge       | 64.00        | AMD EPYC 7R13                      | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c6a.12xlarge      | 96.00        | AMD EPYC 7R13                      | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c6a.16xlarge      | 128.00       | AMD EPYC 7R13                      | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c6a.24xlarge      | 192.00       | AMD EPYC 7R13                      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c6a.32xlarge      | 256.00       | AMD EPYC 7R13                      | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c6a.48xlarge      | 384.00       | AMD EPYC 7R13                      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c6a.metal         | 384.00       | AMD EPYC 7R13                      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **C6g**           |
| c6g.medium        | 2.00         | AWS Graviton2 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c6g.large         | 4.00         | AWS Graviton2 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c6g.xlarge        | 8.00         | AWS Graviton2 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c6g.2xlarge       | 16.00        | AWS Graviton2 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c6g.4xlarge       | 32.00        | AWS Graviton2 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c6g.8xlarge       | 64.00        | AWS Graviton2 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c6g.12xlarge      | 96.00        | AWS Graviton2 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c6g.16xlarge      | 128.00       | AWS Graviton2 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c6g.metal         | 128.00       | AWS Graviton2 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C6gd**          |
| c6gd.medium       | 2.00         | AWS Graviton2 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c6gd.large        | 4.00         | AWS Graviton2 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c6gd.xlarge       | 8.00         | AWS Graviton2 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c6gd.2xlarge      | 16.00        | AWS Graviton2 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c6gd.4xlarge      | 32.00        | AWS Graviton2 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c6gd.8xlarge      | 64.00        | AWS Graviton2 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c6gd.12xlarge     | 96.00        | AWS Graviton2 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c6gd.16xlarge     | 128.00       | AWS Graviton2 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c6gd.metal        | 128.00       | AWS Graviton2 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C6gn**          |
| c6gn.medium       | 2.00         | AWS Graviton2 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c6gn.large        | 4.00         | AWS Graviton2 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c6gn.xlarge       | 8.00         | AWS Graviton2 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c6gn.2xlarge      | 16.00        | AWS Graviton2 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c6gn.4xlarge      | 32.00        | AWS Graviton2 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c6gn.8xlarge      | 64.00        | AWS Graviton2 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c6gn.12xlarge     | 96.00        | AWS Graviton2 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c6gn.16xlarge     | 128.00       | AWS Graviton2 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C6i**           |
| c6i.large         | 4.00         | Intel Xeon Ice Lake                | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c6i.xlarge        | 8.00         | Intel Xeon Ice Lake                | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c6i.2xlarge       | 16.00        | Intel Xeon Ice Lake                | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c6i.4xlarge       | 32.00        | Intel Xeon Ice Lake                | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c6i.8xlarge       | 64.00        | Intel Xeon Ice Lake                | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c6i.12xlarge      | 96.00        | Intel Xeon Ice Lake                | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c6i.16xlarge      | 128.00       | Intel Xeon Ice Lake                | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c6i.24xlarge      | 192.00       | Intel Xeon Ice Lake                | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c6i.32xlarge      | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c6i.metal         | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **C6id**          |
| c6id.large        | 4.00         | Intel Xeon Ice Lake                | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c6id.xlarge       | 8.00         | Intel Xeon Ice Lake                | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c6id.2xlarge      | 16.00        | Intel Xeon Ice Lake                | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c6id.4xlarge      | 32.00        | Intel Xeon Ice Lake                | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c6id.8xlarge      | 64.00        | Intel Xeon Ice Lake                | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c6id.12xlarge     | 96.00        | Intel Xeon Ice Lake                | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c6id.16xlarge     | 128.00       | Intel Xeon Ice Lake                | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c6id.24xlarge     | 192.00       | Intel Xeon Ice Lake                | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c6id.32xlarge     | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c6id.metal        | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **C6in**          |
| c6in.large        | 4.00         | Intel Xeon Ice Lake                | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c6in.xlarge       | 8.00         | Intel Xeon Ice Lake                | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c6in.2xlarge      | 16.00        | Intel Xeon Ice Lake                | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c6in.4xlarge      | 32.00        | Intel Xeon Ice Lake                | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c6in.8xlarge      | 64.00        | Intel Xeon Ice Lake                | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c6in.12xlarge     | 96.00        | Intel Xeon Ice Lake                | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c6in.16xlarge     | 128.00       | Intel Xeon Ice Lake                | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c6in.24xlarge     | 192.00       | Intel Xeon Ice Lake                | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c6in.32xlarge     | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c6in.metal        | 256.00       | Intel Xeon Ice Lake                | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **C7a**           |
| c7a.medium        | 2.00         | AMD EPYC 9R14                      | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c7a.large         | 4.00         | AMD EPYC 9R14                      | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c7a.xlarge        | 8.00         | AMD EPYC 9R14                      | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c7a.2xlarge       | 16.00        | AMD EPYC 9R14                      | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c7a.4xlarge       | 32.00        | AMD EPYC 9R14                      | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c7a.8xlarge       | 64.00        | AMD EPYC 9R14                      | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c7a.12xlarge      | 96.00        | AMD EPYC 9R14                      | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c7a.16xlarge      | 128.00       | AMD EPYC 9R14                      | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c7a.24xlarge      | 192.00       | AMD EPYC 9R14                      | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c7a.32xlarge      | 256.00       | AMD EPYC 9R14                      | 128   | 128       | 1                | ✗ No         | ✗ No               |
| c7a.48xlarge      | 384.00       | AMD EPYC 9R14                      | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c7a.metal-48xl    | 384.00       | AMD EPYC 9R14                      | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C7g**           |
| c7g.medium        | 2.00         | AWS Graviton3 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c7g.large         | 4.00         | AWS Graviton3 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c7g.xlarge        | 8.00         | AWS Graviton3 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c7g.2xlarge       | 16.00        | AWS Graviton3 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c7g.4xlarge       | 32.00        | AWS Graviton3 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c7g.8xlarge       | 64.00        | AWS Graviton3 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c7g.12xlarge      | 96.00        | AWS Graviton3 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c7g.16xlarge      | 128.00       | AWS Graviton3 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c7g.metal         | 128.00       | AWS Graviton3 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C7gd**          |
| c7gd.medium       | 2.00         | AWS Graviton3 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c7gd.large        | 4.00         | AWS Graviton3 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c7gd.xlarge       | 8.00         | AWS Graviton3 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c7gd.2xlarge      | 16.00        | AWS Graviton3 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c7gd.4xlarge      | 32.00        | AWS Graviton3 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c7gd.8xlarge      | 64.00        | AWS Graviton3 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c7gd.12xlarge     | 96.00        | AWS Graviton3 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c7gd.16xlarge     | 128.00       | AWS Graviton3 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c7gd.metal        | 128.00       | AWS Graviton3 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C7gn**          |
| c7gn.medium       | 2.00         | AWS Graviton3E Processor           | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c7gn.large        | 4.00         | AWS Graviton3E Processor           | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c7gn.xlarge       | 8.00         | AWS Graviton3E Processor           | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c7gn.2xlarge      | 16.00        | AWS Graviton3E Processor           | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c7gn.4xlarge      | 32.00        | AWS Graviton3E Processor           | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c7gn.8xlarge      | 64.00        | AWS Graviton3E Processor           | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c7gn.12xlarge     | 96.00        | AWS Graviton3E Processor           | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c7gn.16xlarge     | 128.00       | AWS Graviton3E Processor           | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c7gn.metal        | 128.00       | AWS Graviton3E Processor           | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **C7i**           |
| c7i.large         | 4.00         | Intel Xeon Sapphire Rapids         | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c7i.xlarge        | 8.00         | Intel Xeon Sapphire Rapids         | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c7i.2xlarge       | 16.00        | Intel Xeon Sapphire Rapids         | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c7i.4xlarge       | 32.00        | Intel Xeon Sapphire Rapids         | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c7i.8xlarge       | 64.00        | Intel Xeon Sapphire Rapids         | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c7i.12xlarge      | 96.00        | Intel Xeon Sapphire Rapids         | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c7i.16xlarge      | 128.00       | Intel Xeon Sapphire Rapids         | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c7i.24xlarge      | 192.00       | Intel Xeon Sapphire Rapids         | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c7i.48xlarge      | 384.00       | Intel Xeon Sapphire Rapids         | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c7i.metal-24xl    | 192.00       | Intel Xeon Sapphire Rapids         | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c7i.metal-48xl    | 384.00       | Intel Xeon Sapphire Rapids         | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **C7i-flex**      |
| c7i-flex.large    | 4.00         | Intel Xeon Sapphire Rapids         | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c7i-flex.xlarge   | 8.00         | Intel Xeon Sapphire Rapids         | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c7i-flex.2xlarge  | 16.00        | Intel Xeon Sapphire Rapids         | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c7i-flex.4xlarge  | 32.00        | Intel Xeon Sapphire Rapids         | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c7i-flex.8xlarge  | 64.00        | Intel Xeon Sapphire Rapids         | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c7i-flex.12xlarge | 96.00        | Intel Xeon Sapphire Rapids         | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c7i-flex.16xlarge | 128.00       | Intel Xeon Sapphire Rapids         | 64    | 32        | 2                | ✗ No         | ✗ No               |
| **C8a**           |
| c8a.medium        | 2.00         | AMD EPYC 9R45                      | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c8a.large         | 4.00         | AMD EPYC 9R45                      | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c8a.xlarge        | 8.00         | AMD EPYC 9R45                      | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c8a.2xlarge       | 16.00        | AMD EPYC 9R45                      | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c8a.4xlarge       | 32.00        | AMD EPYC 9R45                      | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c8a.8xlarge       | 64.00        | AMD EPYC 9R45                      | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c8a.12xlarge      | 96.00        | AMD EPYC 9R45                      | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c8a.16xlarge      | 128.00       | AMD EPYC 9R45                      | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c8a.24xlarge      | 192.00       | AMD EPYC 9R45                      | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8a.48xlarge      | 384.00       | AMD EPYC 9R45                      | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c8a.metal-24xl    | 192.00       | AMD EPYC 9R45                      | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8a.metal-48xl    | 384.00       | AMD EPYC 9R45                      | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C8g**           |
| c8g.medium        | 2.00         | AWS Graviton4 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c8g.large         | 4.00         | AWS Graviton4 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c8g.xlarge        | 8.00         | AWS Graviton4 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c8g.2xlarge       | 16.00        | AWS Graviton4 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c8g.4xlarge       | 32.00        | AWS Graviton4 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c8g.8xlarge       | 64.00        | AWS Graviton4 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c8g.12xlarge      | 96.00        | AWS Graviton4 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c8g.16xlarge      | 128.00       | AWS Graviton4 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c8g.24xlarge      | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8g.48xlarge      | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c8g.metal-24xl    | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8g.metal-48xl    | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C8gb**          |
| c8gb.medium       | 2.00         | AWS Graviton4 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c8gb.large        | 4.00         | AWS Graviton4 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c8gb.xlarge       | 8.00         | AWS Graviton4 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c8gb.2xlarge      | 16.00        | AWS Graviton4 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c8gb.4xlarge      | 32.00        | AWS Graviton4 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c8gb.8xlarge      | 64.00        | AWS Graviton4 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c8gb.12xlarge     | 96.00        | AWS Graviton4 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c8gb.16xlarge     | 128.00       | AWS Graviton4 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c8gb.24xlarge     | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gb.48xlarge     | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c8gb.metal-24xl   | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gb.metal-48xl   | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C8gd**          |
| c8gd.medium       | 2.00         | AWS Graviton4 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c8gd.large        | 4.00         | AWS Graviton4 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c8gd.xlarge       | 8.00         | AWS Graviton4 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c8gd.2xlarge      | 16.00        | AWS Graviton4 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c8gd.4xlarge      | 32.00        | AWS Graviton4 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c8gd.8xlarge      | 64.00        | AWS Graviton4 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c8gd.12xlarge     | 96.00        | AWS Graviton4 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c8gd.16xlarge     | 128.00       | AWS Graviton4 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c8gd.24xlarge     | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gd.48xlarge     | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c8gd.metal-24xl   | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gd.metal-48xl   | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C8gn**          |
| c8gn.medium       | 2.00         | AWS Graviton4 Processor            | 1     | 1         | 1                | ✗ No         | ✗ No               |
| c8gn.large        | 4.00         | AWS Graviton4 Processor            | 2     | 2         | 1                | ✗ No         | ✗ No               |
| c8gn.xlarge       | 8.00         | AWS Graviton4 Processor            | 4     | 4         | 1                | ✗ No         | ✗ No               |
| c8gn.2xlarge      | 16.00        | AWS Graviton4 Processor            | 8     | 8         | 1                | ✗ No         | ✗ No               |
| c8gn.4xlarge      | 32.00        | AWS Graviton4 Processor            | 16    | 16        | 1                | ✗ No         | ✗ No               |
| c8gn.8xlarge      | 64.00        | AWS Graviton4 Processor            | 32    | 32        | 1                | ✗ No         | ✗ No               |
| c8gn.12xlarge     | 96.00        | AWS Graviton4 Processor            | 48    | 48        | 1                | ✗ No         | ✗ No               |
| c8gn.16xlarge     | 128.00       | AWS Graviton4 Processor            | 64    | 64        | 1                | ✗ No         | ✗ No               |
| c8gn.24xlarge     | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gn.48xlarge     | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| c8gn.metal-24xl   | 192.00       | AWS Graviton4 Processor            | 96    | 96        | 1                | ✗ No         | ✗ No               |
| c8gn.metal-48xl   | 384.00       | AWS Graviton4 Processor            | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **C8i**           |
| c8i.large         | 4.00         | Intel Xeon Granite Rapids          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c8i.xlarge        | 8.00         | Intel Xeon Granite Rapids          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c8i.2xlarge       | 16.00        | Intel Xeon Granite Rapids          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c8i.4xlarge       | 32.00        | Intel Xeon Granite Rapids          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c8i.8xlarge       | 64.00        | Intel Xeon Granite Rapids          | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c8i.12xlarge      | 96.00        | Intel Xeon Granite Rapids          | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c8i.16xlarge      | 128.00       | Intel Xeon Granite Rapids          | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c8i.24xlarge      | 192.00       | Intel Xeon Granite Rapids          | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c8i.32xlarge      | 256.00       | Intel Xeon Granite Rapids          | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c8i.48xlarge      | 384.00       | Intel Xeon Granite Rapids          | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c8i.96xlarge      | 768.00       | Intel Xeon Granite Rapids          | 384   | 192       | 2                | ✗ No         | ✗ No               |
| c8i.metal-48xl    | 384.00       | Intel Xeon Granite Rapids          | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c8i.metal-96xl    | 768.00       | Intel Xeon Granite Rapids          | 384   | 192       | 2                | ✗ No         | ✗ No               |
| **C8id**          |
| c8id.large        | 4.00         | Intel Xeon Granite Rapids          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c8id.xlarge       | 8.00         | Intel Xeon Granite Rapids          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c8id.2xlarge      | 16.00        | Intel Xeon Granite Rapids          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c8id.4xlarge      | 32.00        | Intel Xeon Granite Rapids          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c8id.8xlarge      | 64.00        | Intel Xeon Granite Rapids          | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c8id.12xlarge     | 96.00        | Intel Xeon Granite Rapids          | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c8id.16xlarge     | 128.00       | Intel Xeon Granite Rapids          | 64    | 32        | 2                | ✗ No         | ✗ No               |
| c8id.24xlarge     | 192.00       | Intel Xeon Granite Rapids          | 96    | 48        | 2                | ✗ No         | ✗ No               |
| c8id.32xlarge     | 256.00       | Intel Xeon Granite Rapids          | 128   | 64        | 2                | ✗ No         | ✗ No               |
| c8id.48xlarge     | 384.00       | Intel Xeon Granite Rapids          | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c8id.96xlarge     | 768.00       | Intel Xeon Granite Rapids          | 384   | 192       | 2                | ✗ No         | ✗ No               |
| c8id.metal-48xl   | 384.00       | Intel Xeon Granite Rapids          | 192   | 96        | 2                | ✗ No         | ✗ No               |
| c8id.metal-96xl   | 768.00       | Intel Xeon Granite Rapids          | 384   | 192       | 2                | ✗ No         | ✗ No               |
| **C8i-flex**      |
| c8i-flex.large    | 4.00         | Intel Xeon Granite Rapids          | 2     | 1         | 2                | ✗ No         | ✗ No               |
| c8i-flex.xlarge   | 8.00         | Intel Xeon Granite Rapids          | 4     | 2         | 2                | ✗ No         | ✗ No               |
| c8i-flex.2xlarge  | 16.00        | Intel Xeon Granite Rapids          | 8     | 4         | 2                | ✗ No         | ✗ No               |
| c8i-flex.4xlarge  | 32.00        | Intel Xeon Granite Rapids          | 16    | 8         | 2                | ✗ No         | ✗ No               |
| c8i-flex.8xlarge  | 64.00        | Intel Xeon Granite Rapids          | 32    | 16        | 2                | ✗ No         | ✗ No               |
| c8i-flex.12xlarge | 96.00        | Intel Xeon Granite Rapids          | 48    | 24        | 2                | ✗ No         | ✗ No               |
| c8i-flex.16xlarge | 128.00       | Intel Xeon Granite Rapids          | 64    | 32        | 2                | ✗ No         | ✗ No               |

## Network specifications

###### Note

C8a, C8g, C8gd, C8i, C8id, C8i-flex instance types support configurable bandwidth weightings.
With these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
instance types. For the supported configurable weightings, see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").

| Instance type       | Baseline / Burst bandwidth (Gbps) | EFA   | ENA   | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| ------------------- | --------------------------------- | ----- | ----- | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **C5**              |
| c5.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c5.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5.9xlarge          | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5.12xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5.18xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5.24xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C5a**             |
| c5a.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c5a.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5a.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5a.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5a.8xlarge         | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5a.12xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5a.16xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5a.24xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C5ad**            |
| c5ad.large 1        | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c5ad.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5ad.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5ad.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5ad.8xlarge        | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5ad.12xlarge       | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5ad.16xlarge       | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5ad.24xlarge       | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C5d**             |
| c5d.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c5d.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5d.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5d.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5d.9xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5d.12xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5d.18xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5d.24xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5d.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C5n**             |
| c5n.large 1         | 3.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c5n.xlarge 1        | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5n.2xlarge 1       | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c5n.4xlarge 1       | 15.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5n.9xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c5n.18xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c5n.metal           | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C6a**             |
| c6a.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6a.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6a.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6a.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6a.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6a.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6a.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6a.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6a.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6a.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6a.metal           | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C6g**             |
| c6g.medium 1        | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c6g.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6g.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6g.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6g.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6g.8xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6g.12xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6g.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c6g.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C6gd**            |
| c6gd.medium 1       | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c6gd.large 1        | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6gd.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6gd.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6gd.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6gd.8xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6gd.12xlarge       | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6gd.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| c6gd.metal          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C6gn**            |
| c6gn.medium 1       | 1.6 / 16.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c6gn.large 1        | 3.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6gn.xlarge 1       | 6.3 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6gn.2xlarge 1      | 12.5 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6gn.4xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6gn.8xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6gn.12xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6gn.16xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C6i**             |
| c6i.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6i.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6i.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6i.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6i.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6i.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6i.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6i.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6i.32xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6i.metal           | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C6id**            |
| c6id.large 1        | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6id.xlarge 1       | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6id.2xlarge 1      | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6id.4xlarge 1      | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6id.8xlarge        | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6id.12xlarge       | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6id.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6id.24xlarge       | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6id.32xlarge       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6id.metal          | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C6in**            |
| c6in.large 1        | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c6in.xlarge 1       | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6in.2xlarge 1      | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c6in.4xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c6in.8xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6in.12xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c6in.16xlarge       | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6in.24xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c6in.32xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| c6in.metal          | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **C7a**             |
| c7a.medium 1        | 0.39 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c7a.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7a.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7a.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7a.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7a.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7a.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7a.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7a.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7a.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7a.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7a.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C7g**             |
| c7g.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c7g.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7g.xlarge 1        | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7g.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7g.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7g.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7g.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7g.16xlarge        | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7g.metal           | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C7gd**            |
| c7gd.medium 1       | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c7gd.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7gd.xlarge 1       | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7gd.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7gd.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7gd.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7gd.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7gd.16xlarge       | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7gd.metal          | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C7gn**            |
| c7gn.medium 1       | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c7gn.large 1        | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7gn.xlarge 1       | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7gn.2xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7gn.4xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7gn.8xlarge        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7gn.12xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7gn.16xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7gn.metal          | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C7i**             |
| c7i.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7i.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7i.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7i.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7i.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7i.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c7i.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7i.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7i.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7i.metal-24xl      | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c7i.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C7i-flex**        |
| c7i-flex.large 1    | 0.39 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c7i-flex.xlarge 1   | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7i-flex.2xlarge 1  | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c7i-flex.4xlarge 1  | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7i-flex.8xlarge 1  | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7i-flex.12xlarge 1 | 9.375 / 18.75                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c7i-flex.16xlarge 1 | 12.5 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **C8a**             |
| c8a.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c8a.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| c8a.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| c8a.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 40                         | ✓ Yes |
| c8a.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| c8a.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 40                         | ✓ Yes |
| c8a.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 64                         | ✓ Yes |
| c8a.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| c8a.24xlarge        | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| c8a.48xlarge        | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8a.metal-24xl      | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| c8a.metal-48xl      | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **C8g**             |
| c8g.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c8g.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c8g.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8g.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8g.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8g.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8g.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c8g.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8g.24xlarge        | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8g.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8g.metal-24xl      | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8g.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C8gb**            |
| c8gb.medium 1       | 2.083 / 16.666                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c8gb.large 1        | 4.166 / 20.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c8gb.xlarge 1       | 8.333 / 26.666                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gb.2xlarge 1      | 16.666 / 33.333                   | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gb.4xlarge        | 33.33 Gigabit                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8gb.8xlarge        | 66.66 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| c8gb.12xlarge       | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| c8gb.16xlarge       | 133.33 Gigabit                    | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| c8gb.24xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| c8gb.48xlarge       | 400 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| c8gb.metal-24xl     | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| c8gb.metal-48xl     | 400 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| **C8gd**            |
| c8gd.medium 1       | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c8gd.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c8gd.xlarge 1       | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gd.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gd.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8gd.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8gd.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| c8gd.16xlarge       | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8gd.24xlarge       | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8gd.48xlarge       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8gd.metal-24xl     | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| c8gd.metal-48xl     | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **C8gn**            |
| c8gn.medium 1       | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| c8gn.large 1        | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c8gn.xlarge 1       | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gn.2xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c8gn.4xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c8gn.8xlarge        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| c8gn.12xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| c8gn.16xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| c8gn.24xlarge       | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| c8gn.48xlarge       | 600 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| c8gn.metal-24xl     | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| c8gn.metal-48xl     | 600 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| **C8i**             |
| c8i.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| c8i.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8i.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8i.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| c8i.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| c8i.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| c8i.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| c8i.24xlarge        | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| c8i.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8i.48xlarge        | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8i.96xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8i.metal-48xl      | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8i.metal-96xl      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **C8id**            |
| c8id.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| c8id.xlarge 1       | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8id.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8id.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| c8id.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| c8id.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| c8id.16xlarge       | 30 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| c8id.24xlarge       | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| c8id.32xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8id.48xlarge       | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8id.96xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8id.metal-48xl     | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| c8id.metal-96xl     | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **C8i-flex**        |
| c8i-flex.large 1    | 0.468 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| c8i-flex.xlarge 1   | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8i-flex.2xlarge 1  | 1.875 / 15.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| c8i-flex.4xlarge 1  | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| c8i-flex.8xlarge 1  | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| c8i-flex.12xlarge 1 | 11.25 / 22.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| c8i-flex.16xlarge 1 | 15.0 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |

###### Note

1 These instances have a baseline bandwidth and can
use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best effort basis.
Other instances types can sustain their maximum performance indefinitely. For more information,
see [instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md").

For `c6in.32xlarge`, `c6in.metal`, you must attach at least 2 ENIs, to separate network
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 170 Gbps.

For `c8gn.48xlarge`, `c8gn.metal-48xl`, you must attach at least 2 ENIs, to separate network
cards, to achieve 600 Gbps throughput. Each ENI attached to a network card can achieve up to 300 Gbps.

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

###### Note

C8a, C8g, C8gd, C8i, C8id, C8i-flex instance types support configurable bandwidth weightings.
With these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
instance types. For the supported configurable weightings, see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").

| Instance type       | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                               |
| ------------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **C5**              |
| c5.large 1          | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 4000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.xlarge 1         | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.2xlarge 1        | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 10000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.4xlarge          | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.9xlarge          | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.12xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.18xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.24xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C5a**             |
| c5a.large 1         | 200.00 / 3170.00                    | 25.00 / 396.25                                    | 800.00 / 13300.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.xlarge 1        | 400.00 / 3170.00                    | 50.00 / 396.25                                    | 1600.00 / 13300.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.2xlarge 1       | 800.00 / 3170.00                    | 100.00 / 396.25                                   | 3200.00 / 13300.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.4xlarge 1       | 1580.00 / 3170.00                   | 197.50 / 396.25                                   | 6600.00 / 13300.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.8xlarge         | 3170.00                             | 396.25                                            | 13300.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.12xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.16xlarge        | 6300.00                             | 787.50                                            | 26700.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5a.24xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C5ad**            |
| c5ad.large 1        | 200.00 / 3170.00                    | 25.00 / 396.25                                    | 800.00 / 13300.00                    | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.xlarge 1       | 400.00 / 3170.00                    | 50.00 / 396.25                                    | 1600.00 / 13300.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.2xlarge 1      | 800.00 / 3170.00                    | 100.00 / 396.25                                   | 3200.00 / 13300.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.4xlarge 1      | 1580.00 / 3170.00                   | 197.50 / 396.25                                   | 6600.00 / 13300.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.8xlarge        | 3170.00                             | 396.25                                            | 13300.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.12xlarge       | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.16xlarge       | 6300.00                             | 787.50                                            | 26700.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5ad.24xlarge       | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C5d**             |
| c5d.large 1         | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 4000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.xlarge 1        | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.2xlarge 1       | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 10000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.9xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.12xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.18xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.24xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5d.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C5n**             |
| c5n.large 1         | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 4000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.xlarge 1        | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.2xlarge 1       | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 10000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.9xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.18xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c5n.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6a**             |
| c6a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6a.metal           | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6g**             |
| c6g.medium 1        | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.large 1         | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.xlarge 1        | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.2xlarge 1       | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.8xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.12xlarge        | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.16xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6g.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6gd**            |
| c6gd.medium 1       | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.large 1        | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.xlarge 1       | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.2xlarge 1      | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.4xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.8xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.12xlarge       | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.16xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gd.metal          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6gn**            |
| c6gn.medium 1       | 760.00 / 9500.00                    | 95.00 / 1187.50                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.large 1        | 1235.00 / 9500.00                   | 154.38 / 1187.50                                  | 5000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.xlarge 1       | 2375.00 / 9500.00                   | 296.88 / 1187.50                                  | 10000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.2xlarge 1      | 4750.00 / 9500.00                   | 593.75 / 1187.50                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.4xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.8xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.12xlarge       | 28500.00                            | 3562.50                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6gn.16xlarge       | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6i**             |
| c6i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6i.metal           | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6id**            |
| c6id.large 1        | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.32xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6id.metal          | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C6in**            |
| c6in.large 1        | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 6250.00 / 100000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.xlarge 1       | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 12500.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.2xlarge 1      | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 25000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.4xlarge 1      | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 50000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.8xlarge        | 25000.00                            | 3125.00                                           | 100000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.12xlarge       | 37500.00                            | 4687.50                                           | 150000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.16xlarge       | 50000.00                            | 6250.00                                           | 200000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.24xlarge       | 75000.00                            | 9375.00                                           | 300000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.32xlarge       | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c6in.metal          | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C7a**             |
| c7a.medium 1        | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7a.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c7a.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C7g**             |
| c7g.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7g.metal           | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C7gd**            |
| c7gd.medium 1       | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.large 1        | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gd.metal          | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C7gn**            |
| c7gn.medium 1       | 521.00 / 10000.00                   | 65.12 / 1250.00                                   | 2083.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.large 1        | 1042.00 / 10000.00                  | 130.25 / 1250.00                                  | 4167.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.xlarge 1       | 2083.00 / 10000.00                  | 260.38 / 1250.00                                  | 8333.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.2xlarge 1      | 4167.00 / 10000.00                  | 520.88 / 1250.00                                  | 16667.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.4xlarge 1      | 8333.00 / 10000.00                  | 1041.62 / 1250.00                                 | 33333.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.8xlarge 1      | 16667.00 / 20000.00                 | 2083.38 / 2500.00                                 | 66667.00 / 80000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.12xlarge 1     | 25000.00 / 30000.00                 | 3125.00 / 3750.00                                 | 100000.00 / 120000.00                | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.16xlarge 1     | 33333.00 / 40000.00                 | 4166.62 / 5000.00                                 | 133333.00 / 160000.00                | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| c7gn.metal 1        | 33333.00 / 40000.00                 | 4166.62 / 5000.00                                 | 133333.00 / 160000.00                | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **C7i**             |
| c7i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c7i.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C7i-flex**        |
| c7i-flex.large 1    | 312.00 / 10000.00                   | 39.06 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.xlarge 1   | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.2xlarge 1  | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.4xlarge 1  | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.8xlarge 1  | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.12xlarge 1 | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c7i-flex.16xlarge 1 | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 40000.00 / 80000.00                  | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8a**             |
| c8a.medium 1        | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8a.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8a.metal-48xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8g**             |
| c8g.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8g.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8g.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8gb**            |
| c8gb.medium 1       | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 7500.00 / 120000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.large 1        | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 15000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.xlarge 1       | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 30000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.2xlarge 1      | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 60000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.4xlarge        | 25000.00                            | 3125.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.8xlarge        | 50000.00                            | 6250.00                                           | 240000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.12xlarge       | 75000.00                            | 9375.00                                           | 360000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.16xlarge       | 100000.00                           | 12500.00                                          | 480000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.24xlarge       | 150000.00                           | 18750.00                                          | 720000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.48xlarge       | 300000.00                           | 37500.00                                          | 1440000.00                           | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8gb.metal-24xl     | 150000.00                           | 18750.00                                          | 720000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gb.metal-48xl     | 300000.00                           | 37500.00                                          | 1440000.00                           | ✓ Yes | 78 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8gd**            |
| c8gd.medium 1       | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.large 1        | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.48xlarge       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8gd.metal-24xl     | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gd.metal-48xl     | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8gn**            |
| c8gn.medium 1       | 760.00 / 10000.00                   | 95.00 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.large 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.2xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.4xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.8xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.12xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.16xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.24xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.48xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.metal-24xl     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8gn.metal-48xl     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8i**             |
| c8i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8i.96xlarge        | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8i.metal-48xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i.metal-96xl      | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8id**            |
| c8id.large 1        | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.32xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.48xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8id.96xlarge       | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| c8id.metal-48xl     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8id.metal-96xl     | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **C8i-flex**        |
| c8i-flex.large 1    | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.xlarge 1   | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.2xlarge 1  | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.4xlarge 1  | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.8xlarge 1  | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.12xlarge 1 | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| c8i-flex.16xlarge 1 | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 40000.00 / 80000.00                  | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |

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
| **C5ad**        |
| c5ad.large      | 1 x 75 GB              | NVMe SSD            | 16,283 / 7,105                     |                        | ✓ Yes          |
| c5ad.xlarge     | 1 x 150 GB             | NVMe SSD            | 32,566 / 14,211                    |                        | ✓ Yes          |
| c5ad.2xlarge    | 1 x 300 GB             | NVMe SSD            | 65,132 / 28,421                    |                        | ✓ Yes          |
| c5ad.4xlarge    | 2 x 300 GB             | NVMe SSD            | 130,262 / 56,842                   |                        | ✓ Yes          |
| c5ad.8xlarge    | 2 x 600 GB             | NVMe SSD            | 260,526 / 113,684                  |                        | ✓ Yes          |
| c5ad.12xlarge   | 2 x 900 GB             | NVMe SSD            | 412,500 / 180,000                  |                        | ✓ Yes          |
| c5ad.16xlarge   | 2 x 1200 GB            | NVMe SSD            | 521,052 / 227,368                  |                        | ✓ Yes          |
| c5ad.24xlarge   | 2 x 1900 GB            | NVMe SSD            | 825,000 / 360,000                  |                        | ✓ Yes          |
| **C5d**         |
| c5d.large       | 1 x 50 GB              | NVMe SSD            | 20,000 / 9,000                     |                        | ✓ Yes          |
| c5d.xlarge      | 1 x 100 GB             | NVMe SSD            | 40,000 / 18,000                    |                        | ✓ Yes          |
| c5d.2xlarge     | 1 x 200 GB             | NVMe SSD            | 80,000 / 37,000                    |                        | ✓ Yes          |
| c5d.4xlarge     | 1 x 400 GB             | NVMe SSD            | 175,000 / 75,000                   |                        | ✓ Yes          |
| c5d.9xlarge     | 1 x 900 GB             | NVMe SSD            | 350,000 / 170,000                  |                        | ✓ Yes          |
| c5d.12xlarge    | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| c5d.18xlarge    | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| c5d.24xlarge    | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| c5d.metal       | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| **C6gd**        |
| c6gd.medium     | 1 x 59 GB              | NVMe SSD            | 13,438 / 5,625                     |                        | ✓ Yes          |
| c6gd.large      | 1 x 118 GB             | NVMe SSD            | 26,875 / 11,250                    |                        | ✓ Yes          |
| c6gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 53,750 / 22,500                    |                        | ✓ Yes          |
| c6gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| c6gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 215,000 / 90,000                   |                        | ✓ Yes          |
| c6gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| c6gd.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| c6gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| c6gd.metal      | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **C6id**        |
| c6id.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| c6id.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| c6id.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| c6id.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| c6id.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| c6id.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| c6id.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| c6id.24xlarge   | 4 x 1425 GB            | NVMe SSD            | 1,609,996 / 805,000                |                        | ✓ Yes          |
| c6id.32xlarge   | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| c6id.metal      | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **C7gd**        |
| c7gd.medium     | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| c7gd.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| c7gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| c7gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| c7gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| c7gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| c7gd.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| c7gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| c7gd.metal      | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| **C8gd**        |
| c8gd.medium     | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| c8gd.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| c8gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| c8gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| c8gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| c8gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| c8gd.12xlarge   | 3 x 950 GB             | NVMe SSD            | 804,999 / 402,501                  |                        | ✓ Yes          |
| c8gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| c8gd.24xlarge   | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| c8gd.48xlarge   | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| c8gd.metal-24xl | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| c8gd.metal-48xl | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| **C8id**        |
| c8id.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| c8id.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| c8id.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| c8id.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| c8id.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| c8id.12xlarge   | 1 x 2850 GB            | NVMe SSD            | 804,999 / 402,501                  |                        | ✓ Yes          |
| c8id.16xlarge   | 1 x 3800 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| c8id.24xlarge   | 2 x 2850 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| c8id.32xlarge   | 2 x 3800 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| c8id.48xlarge   | 3 x 3800 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| c8id.96xlarge   | 6 x 3800 GB            | NVMe SSD            | 6,439,992 / 3,220,008              |                        | ✓ Yes          |
| c8id.metal-48xl | 3 x 3800 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| c8id.metal-96xl | 6 x 3800 GB            | NVMe SSD            | 6,439,992 / 3,220,008              |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type     | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| ----------------- | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **C5**            |
| c5.large          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| c5.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.4xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.9xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.12xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.18xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.24xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5.metal          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C5a**           |
| c5a.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c5a.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5a.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **C5ad**          |
| c5ad.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c5ad.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5ad.24xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **C5d**           |
| c5d.large         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| c5d.xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.2xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.4xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.9xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.12xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.18xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.24xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5d.metal         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C5n**           |
| c5n.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c5n.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5n.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5n.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5n.9xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5n.18xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c5n.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C6a**           |
| c6a.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✗ No           |
| c6a.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| c6a.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6a.32xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6a.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6a.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C6g**           |
| c6g.medium        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| c6g.large         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.2xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.4xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.8xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.12xlarge      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.16xlarge      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6g.metal         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C6gd**          |
| c6gd.medium       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| c6gd.large        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.2xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.4xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.8xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.12xlarge     | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.16xlarge     | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gd.metal        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C6gn**          |
| c6gn.medium       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c6gn.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.2xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.4xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.8xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6gn.16xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **C6i**           |
| c6i.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c6i.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.32xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6i.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C6id**          |
| c6id.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c6id.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.24xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.32xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6id.metal        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C6in**          |
| c6in.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c6in.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.2xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.4xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.8xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.16xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.24xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.32xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c6in.metal        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7a**           |
| c7a.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7a.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7a.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.32xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7a.metal-48xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7g**           |
| c7g.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7g.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7g.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7gd**          |
| c7gd.medium       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gd.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7gd.metal        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7gn**          |
| c7gn.medium       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.2xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.4xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.8xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.16xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7gn.metal        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7i**           |
| c7i.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c7i.metal-24xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c7i.metal-48xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C7i-flex**      |
| c7i-flex.large    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.2xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.4xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.8xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.12xlarge | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c7i-flex.16xlarge | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **C8a**           |
| c8a.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8a.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8a.metal-24xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8a.metal-48xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8g**           |
| c8g.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8g.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8g.metal-24xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8g.metal-48xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8gb**          |
| c8gb.medium       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8gb.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.2xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.4xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.8xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.16xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.24xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.48xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gb.metal-24xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8gb.metal-48xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8gd**          |
| c8gd.medium       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8gd.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.24xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.48xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gd.metal-24xl   | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8gd.metal-48xl   | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8gn**          |
| c8gn.medium       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8gn.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.2xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.4xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.8xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.16xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.24xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.48xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8gn.metal-24xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8gn.metal-48xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8i**           |
| c8i.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.32xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.96xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8i.metal-48xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8i.metal-96xl    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8id**          |
| c8id.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8id.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.24xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.32xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.48xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.96xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| c8id.metal-48xl   | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| c8id.metal-96xl   | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **C8i-flex**      |
| c8i-flex.large    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.2xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.4xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.8xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.12xlarge | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| c8i-flex.16xlarge | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
