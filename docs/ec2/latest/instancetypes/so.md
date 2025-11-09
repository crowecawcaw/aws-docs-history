# Specifications for Amazon EC2 storage optimized instances

Storage optimized instances are designed for workloads that require high, sequential
read and write access to very large data sets on local storage. They are optimized to
deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to
applications.

For information on previous generation instance types of this category, such as I2 instances,
see [Specifications for Amazon EC2 previous generation instances](pg.md "pg.md").

###### Contents

- [Instance families and instance types](#so_sizes "#so_sizes")
- [Instance family summary](#so_summary "#so_summary")
- [Performance specifications](#so_hardware "#so_hardware")
- [Network specifications](#so_network "#so_network")
- [Amazon EBS specifications](#so_storage-ebs "#so_storage-ebs")
- [Instance store specifications](#so_instance-store "#so_instance-store")
- [Security specifications](#so_security "#so_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | -------------- | --------------- | ---------------- | ---------------- | ---------------- | --------------- | --------------- | --------------- | ----------------- | ----------------- |
| D2              | `d2.xlarge`              | `d2.2xlarge`   | `d2.4xlarge`    | `d2.8xlarge`     |
| D3              | `d3.xlarge`              | `d3.2xlarge`   | `d3.4xlarge`    | `d3.8xlarge`     |
| D3en            | `d3en.xlarge`            | `d3en.2xlarge` | `d3en.4xlarge`  | `d3en.6xlarge`   | `d3en.8xlarge`   | `d3en.12xlarge`  |
| H1              | `h1.2xlarge`             | `h1.4xlarge`   | `h1.8xlarge`    | `h1.16xlarge`    |
| I3              | `i3.large`               | `i3.xlarge`    | `i3.2xlarge`    | `i3.4xlarge`     | `i3.8xlarge`     | `i3.16xlarge`    | `i3.metal`      |
| I3en            | `i3en.large`             | `i3en.xlarge`  | `i3en.2xlarge`  | `i3en.3xlarge`   | `i3en.6xlarge`   | `i3en.12xlarge`  | `i3en.24xlarge` | `i3en.metal`    |
| I4g             | `i4g.large`              | `i4g.xlarge`   | `i4g.2xlarge`   | `i4g.4xlarge`    | `i4g.8xlarge`    | `i4g.16xlarge`   |
| I4i             | `i4i.large`              | `i4i.xlarge`   | `i4i.2xlarge`   | `i4i.4xlarge`    | `i4i.8xlarge`    | `i4i.12xlarge`   | `i4i.16xlarge`  | `i4i.24xlarge`  | `i4i.32xlarge`  | `i4i.metal`       |
| I7i             | `i7i.large`              | `i7i.xlarge`   | `i7i.2xlarge`   | `i7i.4xlarge`    | `i7i.8xlarge`    | `i7i.12xlarge`   | `i7i.16xlarge`  | `i7i.24xlarge`  | `i7i.48xlarge`  | `i7i.metal-24xl`  | `i7i.metal-48xl`  |
| I7ie            | `i7ie.large`             | `i7ie.xlarge`  | `i7ie.2xlarge`  | `i7ie.3xlarge`   | `i7ie.6xlarge`   | `i7ie.12xlarge`  | `i7ie.18xlarge` | `i7ie.24xlarge` | `i7ie.48xlarge` | `i7ie.metal-24xl` | `i7ie.metal-48xl` |
| I8g             | `i8g.large`              | `i8g.xlarge`   | `i8g.2xlarge`   | `i8g.4xlarge`    | `i8g.8xlarge`    | `i8g.12xlarge`   | `i8g.16xlarge`  | `i8g.24xlarge`  | `i8g.48xlarge`  | `i8g.metal-24xl`  |
| I8ge            | `i8ge.large`             | `i8ge.xlarge`  | `i8ge.2xlarge`  | `i8ge.3xlarge`   | `i8ge.6xlarge`   | `i8ge.12xlarge`  | `i8ge.18xlarge` | `i8ge.24xlarge` | `i8ge.48xlarge` | `i8ge.metal-24xl` | `i8ge.metal-48xl` |
| Im4gn           | `im4gn.large`            | `im4gn.xlarge` | `im4gn.2xlarge` | `im4gn.4xlarge`  | `im4gn.8xlarge`  | `im4gn.16xlarge` |
| Is4gen          | `is4gen.medium`          | `is4gen.large` | `is4gen.xlarge` | `is4gen.2xlarge` | `is4gen.4xlarge` | `is4gen.8xlarge` |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| D2              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| D3              | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| D3en            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| H1              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| I3              | Xen \*                                                      | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| I3en            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| I4g             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| I4i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| I7i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| I7ie            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| I8g             | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| I8ge            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| Im4gn           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| Is4gen          | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Linux                       |

###### Note

\* `i3.metal` instances are built on the AWS Nitro System.

## Performance specifications

| Instance type   | Memory (GiB) | Processor                 | vCPUs | CPU cores | Threads per core | Accelerators | Accelerator memory |
| --------------- | ------------ | ------------------------- | ----- | --------- | ---------------- | ------------ | ------------------ |
| **D2**          |
| d2.xlarge       | 30.50        | Intel Xeon E52676v3       | 4     | 2         | 2                | ✗ No         | ✗ No               |
| d2.2xlarge      | 61.00        | Intel Xeon E52676v3       | 8     | 4         | 2                | ✗ No         | ✗ No               |
| d2.4xlarge      | 122.00       | Intel Xeon E52676v3       | 16    | 8         | 2                | ✗ No         | ✗ No               |
| d2.8xlarge      | 244.00       | Intel Xeon E52676v3       | 36    | 18        | 2                | ✗ No         | ✗ No               |
| **D3**          |
| d3.xlarge       | 32.00        | Intel Xeon Platinum 8259  | 4     | 2         | 2                | ✗ No         | ✗ No               |
| d3.2xlarge      | 64.00        | Intel Xeon Platinum 8259  | 8     | 4         | 2                | ✗ No         | ✗ No               |
| d3.4xlarge      | 128.00       | Intel Xeon Platinum 8259  | 16    | 8         | 2                | ✗ No         | ✗ No               |
| d3.8xlarge      | 256.00       | Intel Xeon Platinum 8259  | 32    | 16        | 2                | ✗ No         | ✗ No               |
| **D3en**        |
| d3en.xlarge     | 16.00        | Intel Xeon Platinum 8259  | 4     | 2         | 2                | ✗ No         | ✗ No               |
| d3en.2xlarge    | 32.00        | Intel Xeon Platinum 8259  | 8     | 4         | 2                | ✗ No         | ✗ No               |
| d3en.4xlarge    | 64.00        | Intel Xeon Platinum 8259  | 16    | 8         | 2                | ✗ No         | ✗ No               |
| d3en.6xlarge    | 96.00        | Intel Xeon Platinum 8259  | 24    | 12        | 2                | ✗ No         | ✗ No               |
| d3en.8xlarge    | 128.00       | Intel Xeon Platinum 8259  | 32    | 16        | 2                | ✗ No         | ✗ No               |
| d3en.12xlarge   | 192.00       | Intel Xeon Platinum 8259  | 48    | 24        | 2                | ✗ No         | ✗ No               |
| **H1**          |
| h1.2xlarge      | 32.00        | Intel Broadwell E5-2686v4 | 8     | 4         | 2                | ✗ No         | ✗ No               |
| h1.4xlarge      | 64.00        | Intel Broadwell E5-2686v4 | 16    | 8         | 2                | ✗ No         | ✗ No               |
| h1.8xlarge      | 128.00       | Intel Broadwell E5-2686v4 | 32    | 16        | 2                | ✗ No         | ✗ No               |
| h1.16xlarge     | 256.00       | Intel Broadwell E5-2686v4 | 64    | 32        | 2                | ✗ No         | ✗ No               |
| **I3**          |
| i3.large        | 15.25        | Intel Broadwell E5-2686v4 | 2     | 1         | 2                | ✗ No         | ✗ No               |
| i3.xlarge       | 30.50        | Intel Broadwell E5-2686v4 | 4     | 2         | 2                | ✗ No         | ✗ No               |
| i3.2xlarge      | 61.00        | Intel Broadwell E5-2686v4 | 8     | 4         | 2                | ✗ No         | ✗ No               |
| i3.4xlarge      | 122.00       | Intel Broadwell E5-2686v4 | 16    | 8         | 2                | ✗ No         | ✗ No               |
| i3.8xlarge      | 244.00       | Intel Broadwell E5-2686v4 | 32    | 16        | 2                | ✗ No         | ✗ No               |
| i3.16xlarge     | 488.00       | Intel Broadwell E5-2686v4 | 64    | 32        | 2                | ✗ No         | ✗ No               |
| i3.metal        | 512.00       | Intel Broadwell E5-2686v4 | 72    | 36        | 2                | ✗ No         | ✗ No               |
| **I3en**        |
| i3en.large      | 16.00        | Intel Xeon Platinum 8175  | 2     | 1         | 2                | ✗ No         | ✗ No               |
| i3en.xlarge     | 32.00        | Intel Xeon Platinum 8175  | 4     | 2         | 2                | ✗ No         | ✗ No               |
| i3en.2xlarge    | 64.00        | Intel Xeon Platinum 8175  | 8     | 4         | 2                | ✗ No         | ✗ No               |
| i3en.3xlarge    | 96.00        | Intel Xeon Platinum 8175  | 12    | 6         | 2                | ✗ No         | ✗ No               |
| i3en.6xlarge    | 192.00       | Intel Xeon Platinum 8175  | 24    | 12        | 2                | ✗ No         | ✗ No               |
| i3en.12xlarge   | 384.00       | Intel Xeon Platinum 8175  | 48    | 24        | 2                | ✗ No         | ✗ No               |
| i3en.24xlarge   | 768.00       | Intel Xeon Platinum 8175  | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i3en.metal      | 768.00       | Intel Xeon Platinum 8175  | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **I4g**         |
| i4g.large       | 16.00        | AWS Graviton2 Processor   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| i4g.xlarge      | 32.00        | AWS Graviton2 Processor   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| i4g.2xlarge     | 64.00        | AWS Graviton2 Processor   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| i4g.4xlarge     | 128.00       | AWS Graviton2 Processor   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| i4g.8xlarge     | 256.00       | AWS Graviton2 Processor   | 32    | 32        | 1                | ✗ No         | ✗ No               |
| i4g.16xlarge    | 512.00       | AWS Graviton2 Processor   | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **I4i**         |
| i4i.large       | 16.00        | Intel Xeon Ice Lake       | 2     | 1         | 2                | ✗ No         | ✗ No               |
| i4i.xlarge      | 32.00        | Intel Xeon Ice Lake       | 4     | 2         | 2                | ✗ No         | ✗ No               |
| i4i.2xlarge     | 64.00        | Intel Xeon Ice Lake       | 8     | 4         | 2                | ✗ No         | ✗ No               |
| i4i.4xlarge     | 128.00       | Intel Xeon Ice Lake       | 16    | 8         | 2                | ✗ No         | ✗ No               |
| i4i.8xlarge     | 256.00       | Intel Xeon Ice Lake       | 32    | 16        | 2                | ✗ No         | ✗ No               |
| i4i.12xlarge    | 384.00       | Intel Xeon Ice Lake       | 48    | 24        | 2                | ✗ No         | ✗ No               |
| i4i.16xlarge    | 512.00       | Intel Xeon Ice Lake       | 64    | 32        | 2                | ✗ No         | ✗ No               |
| i4i.24xlarge    | 768.00       | Intel Xeon Ice Lake       | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i4i.32xlarge    | 1024.00      | Intel Xeon Ice Lake       | 128   | 64        | 2                | ✗ No         | ✗ No               |
| i4i.metal       | 1024.00      | Intel Xeon Ice Lake       | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **I7i**         |
| i7i.large       | 16.00        | Intel Emerald Rapids      | 2     | 1         | 2                | ✗ No         | ✗ No               |
| i7i.xlarge      | 32.00        | Intel Emerald Rapids      | 4     | 2         | 2                | ✗ No         | ✗ No               |
| i7i.2xlarge     | 64.00        | Intel Emerald Rapids      | 8     | 4         | 2                | ✗ No         | ✗ No               |
| i7i.4xlarge     | 128.00       | Intel Emerald Rapids      | 16    | 8         | 2                | ✗ No         | ✗ No               |
| i7i.8xlarge     | 256.00       | Intel Emerald Rapids      | 32    | 16        | 2                | ✗ No         | ✗ No               |
| i7i.12xlarge    | 384.00       | Intel Emerald Rapids      | 48    | 24        | 2                | ✗ No         | ✗ No               |
| i7i.16xlarge    | 512.00       | Intel Emerald Rapids      | 64    | 32        | 2                | ✗ No         | ✗ No               |
| i7i.24xlarge    | 768.00       | Intel Emerald Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i7i.48xlarge    | 1536.00      | Intel Emerald Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| i7i.metal-24xl  | 768.00       | Intel Emerald Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i7i.metal-48xl  | 1536.00      | Intel Emerald Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **I7ie**        |
| i7ie.large      | 16.00        | Intel Emerald Rapids      | 2     | 1         | 2                | ✗ No         | ✗ No               |
| i7ie.xlarge     | 32.00        | Intel Emerald Rapids      | 4     | 2         | 2                | ✗ No         | ✗ No               |
| i7ie.2xlarge    | 64.00        | Intel Emerald Rapids      | 8     | 4         | 2                | ✗ No         | ✗ No               |
| i7ie.3xlarge    | 96.00        | Intel Emerald Rapids      | 12    | 6         | 2                | ✗ No         | ✗ No               |
| i7ie.6xlarge    | 192.00       | Intel Emerald Rapids      | 24    | 12        | 2                | ✗ No         | ✗ No               |
| i7ie.12xlarge   | 384.00       | Intel Emerald Rapids      | 48    | 24        | 2                | ✗ No         | ✗ No               |
| i7ie.18xlarge   | 576.00       | Intel Emerald Rapids      | 72    | 36        | 2                | ✗ No         | ✗ No               |
| i7ie.24xlarge   | 768.00       | Intel Emerald Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i7ie.48xlarge   | 1536.00      | Intel Emerald Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| i7ie.metal-24xl | 768.00       | Intel Emerald Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| i7ie.metal-48xl | 1536.00      | Intel Emerald Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **I8g**         |
| i8g.large       | 16.00        | AWS Graviton4 Processor   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| i8g.xlarge      | 32.00        | AWS Graviton4 Processor   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| i8g.2xlarge     | 64.00        | AWS Graviton4 Processor   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| i8g.4xlarge     | 128.00       | AWS Graviton4 Processor   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| i8g.8xlarge     | 256.00       | AWS Graviton4 Processor   | 32    | 32        | 1                | ✗ No         | ✗ No               |
| i8g.12xlarge    | 384.00       | AWS Graviton4 Processor   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| i8g.16xlarge    | 512.00       | AWS Graviton4 Processor   | 64    | 64        | 1                | ✗ No         | ✗ No               |
| i8g.24xlarge    | 768.00       | AWS Graviton4 Processor   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| i8g.48xlarge    | 1536.00      | AWS Graviton4 Processor   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| i8g.metal-24xl  | 768.00       | AWS Graviton4 Processor   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| **I8ge**        |
| i8ge.large      | 16.00        | AWS Graviton4 Processor   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| i8ge.xlarge     | 32.00        | AWS Graviton4 Processor   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| i8ge.2xlarge    | 64.00        | AWS Graviton4 Processor   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| i8ge.3xlarge    | 96.00        | AWS Graviton4 Processor   | 12    | 12        | 1                | ✗ No         | ✗ No               |
| i8ge.6xlarge    | 192.00       | AWS Graviton4 Processor   | 24    | 24        | 1                | ✗ No         | ✗ No               |
| i8ge.12xlarge   | 384.00       | AWS Graviton4 Processor   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| i8ge.18xlarge   | 576.00       | AWS Graviton4 Processor   | 72    | 72        | 1                | ✗ No         | ✗ No               |
| i8ge.24xlarge   | 768.00       | AWS Graviton4 Processor   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| i8ge.48xlarge   | 1536.00      | AWS Graviton4 Processor   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| i8ge.metal-24xl | 768.00       | AWS Graviton4 Processor   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| i8ge.metal-48xl | 1536.00      | AWS Graviton4 Processor   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **Im4gn**       |
| im4gn.large     | 8.00         | AWS Graviton2 Processor   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| im4gn.xlarge    | 16.00        | AWS Graviton2 Processor   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| im4gn.2xlarge   | 32.00        | AWS Graviton2 Processor   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| im4gn.4xlarge   | 64.00        | AWS Graviton2 Processor   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| im4gn.8xlarge   | 128.00       | AWS Graviton2 Processor   | 32    | 32        | 1                | ✗ No         | ✗ No               |
| im4gn.16xlarge  | 256.00       | AWS Graviton2 Processor   | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **Is4gen**      |
| is4gen.medium   | 6.00         | AWS Graviton2 Processor   | 1     | 1         | 1                | ✗ No         | ✗ No               |
| is4gen.large    | 12.00        | AWS Graviton2 Processor   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| is4gen.xlarge   | 24.00        | AWS Graviton2 Processor   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| is4gen.2xlarge  | 48.00        | AWS Graviton2 Processor   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| is4gen.4xlarge  | 96.00        | AWS Graviton2 Processor   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| is4gen.8xlarge  | 192.00       | AWS Graviton2 Processor   | 32    | 32        | 1                | ✗ No         | ✗ No               |

## Network specifications

| Instance type     | Baseline / Burst bandwidth (Gbps) | EFA   | ENA    | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| ----------------- | --------------------------------- | ----- | ------ | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **D2**            |
| d2.xlarge         | Moderate                          | ✗ No  | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| d2.2xlarge        | High                              | ✗ No  | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| d2.4xlarge        | High                              | ✗ No  | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| d2.8xlarge        | 10 Gigabit                        | ✗ No  | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **D3**            |
| d3.xlarge 1       | 3.0 / 15.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 3                          | ✓ Yes |
| d3.2xlarge 1      | 6.0 / 15.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 5                          | ✓ Yes |
| d3.4xlarge 1      | 12.5 / 15.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 10                         | ✓ Yes |
| d3.8xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| **D3en**          |
| d3en.xlarge 1     | 6.0 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 3                          | ✓ Yes |
| d3en.2xlarge 1    | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 5                          | ✓ Yes |
| d3en.4xlarge      | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 10                         | ✓ Yes |
| d3en.6xlarge      | 40 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| d3en.8xlarge      | 50 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| d3en.12xlarge     | 75 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 30                         | ✓ Yes |
| **H1**            |
| h1.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| h1.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| h1.8xlarge        | 10 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| h1.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| **I3**            |
| i3.large 1        | 0.75 / 10.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i3.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i3.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i3.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i3.8xlarge        | 10 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i3.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| i3.metal          | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **I3en**          |
| i3en.large 1      | 2.1 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i3en.xlarge 1     | 4.2 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i3en.2xlarge 1    | 8.4 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i3en.3xlarge 1    | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i3en.6xlarge      | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i3en.12xlarge     | 50 Gigabit                        | ✓ Yes | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i3en.24xlarge     | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| i3en.metal        | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **I4g**           |
| i4g.large 1       | 0.781 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i4g.xlarge 1      | 1.875 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i4g.2xlarge 1     | 4.687 / 12.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i4g.4xlarge 1     | 9.375 / 25.0                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i4g.8xlarge       | 18.75 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i4g.16xlarge      | 37.5 Gigabit                      | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **I4i**           |
| i4i.large 1       | 0.781 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i4i.xlarge 1      | 1.875 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i4i.2xlarge 1     | 4.687 / 12.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i4i.4xlarge 1     | 9.375 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i4i.8xlarge       | 18.75 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i4i.12xlarge      | 28.12 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i4i.16xlarge      | 37.5 Gigabit                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i4i.24xlarge      | 56.25 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 30                         | ✓ Yes |
| i4i.32xlarge      | 75 Gigabit                        | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i4i.metal         | 75 Gigabit                        | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **I7i**           |
| i7i.large 1       | 1.171 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i7i.xlarge 1      | 2.343 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i7i.2xlarge 1     | 4.687 / 12.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i7i.4xlarge 1     | 9.375 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i7i.8xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i7i.12xlarge      | 28.12 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i7i.16xlarge      | 37.5 Gigabit                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7i.24xlarge      | 56.25 Gigabit                     | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7i.48xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7i.metal-24xl    | 56.25 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7i.metal-48xl    | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **I7ie**          |
| i7ie.large 1      | 2.083 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i7ie.xlarge 1     | 4.166 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i7ie.2xlarge 1    | 8.333 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i7ie.3xlarge 1    | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i7ie.6xlarge 1    | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i7ie.12xlarge 1   | 25.0 / 50.0                       | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 50                         | ✓ Yes |
| i7ie.18xlarge 1   | 37.5 / 75.0                       | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7ie.24xlarge 1   | 50.0 / 100.0                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7ie.48xlarge     | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7ie.metal-24xl 1 | 50.0 / 100.0                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i7ie.metal-48xl   | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **I8g**           |
| i8g.large 1       | 1.172 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i8g.xlarge 1      | 2.344 / 10.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i8g.2xlarge 1     | 4.688 / 12.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i8g.4xlarge 1     | 9.375 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i8g.8xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i8g.12xlarge      | 28.12 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| i8g.16xlarge      | 37.5 Gigabit                      | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i8g.24xlarge      | 56.25 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i8g.48xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| i8g.metal-24xl    | 56.25 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **I8ge**          |
| i8ge.large 1      | 2.1 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| i8ge.xlarge 1     | 4.2 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i8ge.2xlarge 1    | 8.4 / 25.0                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i8ge.3xlarge 1    | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 6                       | 30                         | ✓ Yes |
| i8ge.6xlarge      | 37.5 Gigabit                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 10                      | 30                         | ✓ Yes |
| i8ge.12xlarge     | 75 Gigabit                        | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| i8ge.18xlarge     | 112.5 Gigabit                     | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| i8ge.24xlarge     | 150 Gigabit                       | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| i8ge.48xlarge     | 180 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| i8ge.metal-24xl   | 150 Gigabit                       | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| i8ge.metal-48xl   | 180 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| **Im4gn**         |
| im4gn.large 1     | 3.125 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| im4gn.xlarge 1    | 6.25 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| im4gn.2xlarge 1   | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| im4gn.4xlarge     | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| im4gn.8xlarge     | 50 Gigabit                        | ✗ No  | ✓ Yes  | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| im4gn.16xlarge    | 100 Gigabit                       | ✓ Yes | ✓ Yes  | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **Is4gen**        |
| is4gen.medium 1   | 1.562 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| is4gen.large 1    | 3.125 / 25.0                      | ✗ No  | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| is4gen.xlarge 1   | 6.25 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| is4gen.2xlarge 1  | 12.5 / 25.0                       | ✗ No  | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| is4gen.4xlarge    | 25 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| is4gen.8xlarge    | 50 Gigabit                        | ✗ No  | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |

###### Note

1 These instances have a baseline bandwidth and can
use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best effort basis.
Other instances types can sustain their maximum performance indefinitely. For more information,
see [instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md").

2 These instances support enhanced networking using the
Intel 82599 VF interface.

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

| Instance type    | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                               |
| ---------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **D2**           |
| d2.xlarge        | 750.00                              | 93.75                                             | 6000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| d2.2xlarge       | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| d2.4xlarge       | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| d2.8xlarge       | 4000.00                             | 500.00                                            | 32000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **D3**           |
| d3.xlarge 1      | 850.00 / 2800.00                    | 106.25 / 350.00                                   | 5000.00 / 15000.00                   | ✓ Yes | Up to 24 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3.2xlarge 1     | 1700.00 / 2800.00                   | 212.50 / 350.00                                   | 10000.00 / 15000.00                  | ✓ Yes | Up to 21 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3.4xlarge       | 2800.00                             | 350.00                                            | 15000.00                             | ✓ Yes | Up to 15 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3.8xlarge       | 5000.00                             | 625.00                                            | 30000.00                             | ✓ Yes | Up to 3 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))      |
| **D3en**         |
| d3en.xlarge 1    | 850.00 / 2800.00                    | 106.25 / 350.00                                   | 5000.00 / 15000.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3en.2xlarge 1   | 1700.00 / 2800.00                   | 212.50 / 350.00                                   | 10000.00 / 15000.00                  | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3en.4xlarge     | 2800.00                             | 350.00                                            | 15000.00                             | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3en.6xlarge     | 4000.00                             | 500.00                                            | 25000.00                             | ✓ Yes | Up to 15 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3en.8xlarge     | 5000.00                             | 625.00                                            | 30000.00                             | ✓ Yes | Up to 11 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| d3en.12xlarge    | 7000.00                             | 875.00                                            | 40000.00                             | ✓ Yes | Up to 3 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))      |
| **H1**           |
| h1.2xlarge       | 1750.00                             | 218.75                                            | 12000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| h1.4xlarge       | 3500.00                             | 437.50                                            | 20000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| h1.8xlarge       | 7000.00                             | 875.00                                            | 40000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| h1.16xlarge      | 14000.00                            | 1750.00                                           | 80000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **I3**           |
| i3.large         | 425.00                              | 53.12                                             | 3000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.xlarge        | 850.00                              | 106.25                                            | 6000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.2xlarge       | 1700.00                             | 212.50                                            | 12000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.4xlarge       | 3500.00                             | 437.50                                            | 16000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.8xlarge       | 7000.00                             | 875.00                                            | 32500.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.16xlarge      | 14000.00                            | 1750.00                                           | 65000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| i3.metal         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **I3en**         |
| i3en.large 1     | 576.00 / 4750.00                    | 72.10 / 593.75                                    | 3000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.xlarge 1    | 1153.00 / 4750.00                   | 144.20 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.2xlarge 1   | 2307.00 / 4750.00                   | 288.39 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.3xlarge 1   | 3800.00 / 4750.00                   | 475.00 / 593.75                                   | 15000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.6xlarge     | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.12xlarge    | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.24xlarge    | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i3en.metal       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **I4g**          |
| i4g.large 1      | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4g.xlarge 1     | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4g.2xlarge 1    | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4g.4xlarge 1    | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4g.8xlarge      | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4g.16xlarge     | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **I4i**          |
| i4i.large 1      | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.xlarge 1     | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.2xlarge 1    | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.4xlarge 1    | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.8xlarge      | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.12xlarge     | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 24 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.16xlarge     | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.24xlarge     | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 21 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.32xlarge     | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| i4i.metal        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **I7i**          |
| i7i.large 1      | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.xlarge 1     | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.2xlarge 1    | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.4xlarge 1    | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.8xlarge      | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.12xlarge     | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.16xlarge     | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.24xlarge     | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.48xlarge     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| i7i.metal-24xl   | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7i.metal-48xl   | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **I7ie**         |
| i7ie.large 1     | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.xlarge 1    | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.2xlarge 1   | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.3xlarge 1   | 3750.00 / 10000.00                  | 468.75 / 1250.00                                  | 15000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.6xlarge 1   | 7500.00 / 10000.00                  | 937.50 / 1250.00                                  | 30000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.12xlarge    | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.18xlarge    | 22500.00                            | 2812.50                                           | 90000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.24xlarge    | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.48xlarge    | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| i7ie.metal-24xl  | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i7ie.metal-48xl  | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **I8g**          |
| i8g.large 1      | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.xlarge 1     | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.2xlarge 1    | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.4xlarge 1    | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.8xlarge      | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.12xlarge     | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.16xlarge     | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.24xlarge     | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8g.48xlarge     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| i8g.metal-24xl   | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **I8ge**         |
| i8ge.large 1     | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.xlarge 1    | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.2xlarge 1   | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.3xlarge 1   | 3750.00 / 10000.00                  | 468.75 / 1250.00                                  | 15000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.6xlarge 1   | 7500.00 / 10000.00                  | 937.50 / 1250.00                                  | 30000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.12xlarge    | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.18xlarge    | 22500.00                            | 2812.50                                           | 90000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.24xlarge    | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.48xlarge    | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| i8ge.metal-24xl  | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| i8ge.metal-48xl  | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Im4gn**        |
| im4gn.large 1    | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| im4gn.xlarge 1   | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| im4gn.2xlarge 1  | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| im4gn.4xlarge    | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| im4gn.8xlarge    | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| im4gn.16xlarge   | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Is4gen**       |
| is4gen.medium 1  | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| is4gen.large 1   | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| is4gen.xlarge 1  | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| is4gen.2xlarge 1 | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| is4gen.4xlarge   | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| is4gen.8xlarge   | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |

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
| **D2**          |
| d2.xlarge       | 3 x 2048 GB            | HDD                 |                                    | ✓ Yes                  |                |
| d2.2xlarge      | 6 x 2048 GB            | HDD                 |                                    | ✓ Yes                  |                |
| d2.4xlarge      | 12 x 2048 GB           | HDD                 |                                    | ✓ Yes                  |                |
| d2.8xlarge      | 24 x 2048 GB           | HDD                 |                                    | ✓ Yes                  |                |
| **D3**          |
| d3.xlarge       | 3 x 1980 GB            | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3.2xlarge      | 6 x 1980 GB            | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3.4xlarge      | 12 x 1980 GB           | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3.8xlarge      | 24 x 1980 GB           | NVMe HDD            |                                    |                        | ✓ Yes          |
| **D3en**        |
| d3en.xlarge     | 2 x 13980 GB           | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3en.2xlarge    | 4 x 13980 GB           | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3en.4xlarge    | 8 x 13980 GB           | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3en.6xlarge    | 12 x 13980 GB          | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3en.8xlarge    | 16 x 13980 GB          | NVMe HDD            |                                    |                        | ✓ Yes          |
| d3en.12xlarge   | 24 x 13980 GB          | NVMe HDD            |                                    |                        | ✓ Yes          |
| **H1**          |
| h1.2xlarge      | 1 x 2000 GB            | HDD                 |                                    | ✓ Yes                  |                |
| h1.4xlarge      | 2 x 2000 GB            | HDD                 |                                    | ✓ Yes                  |                |
| h1.8xlarge      | 4 x 2000 GB            | HDD                 |                                    | ✓ Yes                  |                |
| h1.16xlarge     | 8 x 2000 GB            | HDD                 |                                    | ✓ Yes                  |                |
| **I3**          |
| i3.large        | 1 x 475 GB             | NVMe SSD            | 103,125 / 35,000                   |                        | ✓ Yes          |
| i3.xlarge       | 1 x 950 GB             | NVMe SSD            | 206,250 / 70,000                   |                        | ✓ Yes          |
| i3.2xlarge      | 1 x 1900 GB            | NVMe SSD            | 412,500 / 180,000                  |                        | ✓ Yes          |
| i3.4xlarge      | 2 x 1900 GB            | NVMe SSD            | 825,000 / 360,000                  |                        | ✓ Yes          |
| i3.8xlarge      | 4 x 1900 GB            | NVMe SSD            | 1,650,000 / 720,000                |                        | ✓ Yes          |
| i3.16xlarge     | 8 x 1900 GB            | NVMe SSD            | 3,300,000 / 1,440,000              |                        | ✓ Yes          |
| i3.metal        | 8 x 1900 GB            | NVMe SSD            | 3,300,000 / 1,440,000              |                        | ✓ Yes          |
| **I3en**        |
| i3en.large      | 1 x 1250 GB            | NVMe SSD            | 42,500 / 32,500                    |                        | ✓ Yes          |
| i3en.xlarge     | 1 x 2500 GB            | NVMe SSD            | 85,000 / 65,000                    |                        | ✓ Yes          |
| i3en.2xlarge    | 2 x 2500 GB            | NVMe SSD            | 170,000 / 130,000                  |                        | ✓ Yes          |
| i3en.3xlarge    | 1 x 7500 GB            | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| i3en.6xlarge    | 2 x 7500 GB            | NVMe SSD            | 500,000 / 400,000                  |                        | ✓ Yes          |
| i3en.12xlarge   | 4 x 7500 GB            | NVMe SSD            | 1,000,000 / 800,000                |                        | ✓ Yes          |
| i3en.24xlarge   | 8 x 7500 GB            | NVMe SSD            | 2,000,000 / 1,600,000              |                        | ✓ Yes          |
| i3en.metal      | 8 x 7500 GB            | NVMe SSD            | 2,000,000 / 1,600,000              |                        | ✓ Yes          |
| **I4g**         |
| i4g.large       | 1 x 468 GB             | NVMe SSD            | 31,250 / 25,000                    |                        | ✓ Yes          |
| i4g.xlarge      | 1 x 937 GB             | NVMe SSD            | 62,500 / 50,000                    |                        | ✓ Yes          |
| i4g.2xlarge     | 1 x 1875 GB            | NVMe SSD            | 125,000 / 100,000                  |                        | ✓ Yes          |
| i4g.4xlarge     | 1 x 3750 GB            | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| i4g.8xlarge     | 2 x 3750 GB            | NVMe SSD            | 500,000 / 400,000                  |                        | ✓ Yes          |
| i4g.16xlarge    | 4 x 3750 GB            | NVMe SSD            | 1,000,000 / 800,000                |                        | ✓ Yes          |
| **I4i**         |
| i4i.large       | 1 x 468 GB             | NVMe SSD            | 50,000 / 27,500                    |                        | ✓ Yes          |
| i4i.xlarge      | 1 x 937 GB             | NVMe SSD            | 100,000 / 55,000                   |                        | ✓ Yes          |
| i4i.2xlarge     | 1 x 1875 GB            | NVMe SSD            | 200,000 / 110,000                  |                        | ✓ Yes          |
| i4i.4xlarge     | 1 x 3750 GB            | NVMe SSD            | 400,000 / 220,000                  |                        | ✓ Yes          |
| i4i.8xlarge     | 2 x 3750 GB            | NVMe SSD            | 800,000 / 440,000                  |                        | ✓ Yes          |
| i4i.12xlarge    | 3 x 3750 GB            | NVMe SSD            | 1,200,000 / 660,000                |                        | ✓ Yes          |
| i4i.16xlarge    | 4 x 3750 GB            | NVMe SSD            | 1,600,000 / 880,000                |                        | ✓ Yes          |
| i4i.24xlarge    | 6 x 3750 GB            | NVMe SSD            | 2,400,000 / 1,320,000              |                        | ✓ Yes          |
| i4i.32xlarge    | 8 x 3750 GB            | NVMe SSD            | 3,200,000 / 1,760,000              |                        | ✓ Yes          |
| i4i.metal       | 8 x 3750 GB            | NVMe SSD            | 3,200,000 / 1,760,000              |                        | ✓ Yes          |
| **I7i**         |
| i7i.large       | 1 x 468 GB             | NVMe SSD            | 75,000 / 41,250                    |                        | ✓ Yes          |
| i7i.xlarge      | 1 x 937 GB             | NVMe SSD            | 150,000 / 82,500                   |                        | ✓ Yes          |
| i7i.2xlarge     | 1 x 1875 GB            | NVMe SSD            | 300,000 / 165,000                  |                        | ✓ Yes          |
| i7i.4xlarge     | 1 x 3750 GB            | NVMe SSD            | 600,000 / 330,000                  |                        | ✓ Yes          |
| i7i.8xlarge     | 2 x 3750 GB            | NVMe SSD            | 1,200,000 / 660,000                |                        | ✓ Yes          |
| i7i.12xlarge    | 3 x 3750 GB            | NVMe SSD            | 1,800,000 / 990,000                |                        | ✓ Yes          |
| i7i.16xlarge    | 4 x 3750 GB            | NVMe SSD            | 2,400,000 / 1,320,000              |                        | ✓ Yes          |
| i7i.24xlarge    | 6 x 3750 GB            | NVMe SSD            | 3,600,000 / 1,980,000              |                        | ✓ Yes          |
| i7i.48xlarge    | 12 x 3750 GB           | NVMe SSD            | 7,200,000 / 3,960,000              |                        | ✓ Yes          |
| i7i.metal-24xl  | 6 x 3750 GB            | NVMe SSD            | 3,600,000 / 1,980,000              |                        | ✓ Yes          |
| i7i.metal-48xl  | 12 x 3750 GB           | NVMe SSD            | 7,200,000 / 3,960,000              |                        | ✓ Yes          |
| **I7ie**        |
| i7ie.large      | 1 x 1250 GB            | NVMe SSD            | 54,166 / 43,333                    |                        | ✓ Yes          |
| i7ie.xlarge     | 1 x 2500 GB            | NVMe SSD            | 108,333 / 86,666                   |                        | ✓ Yes          |
| i7ie.2xlarge    | 2 x 2500 GB            | NVMe SSD            | 216,666 / 173,332                  |                        | ✓ Yes          |
| i7ie.3xlarge    | 1 x 7500 GB            | NVMe SSD            | 325,000 / 260,000                  |                        | ✓ Yes          |
| i7ie.6xlarge    | 2 x 7500 GB            | NVMe SSD            | 650,000 / 520,000                  |                        | ✓ Yes          |
| i7ie.12xlarge   | 4 x 7500 GB            | NVMe SSD            | 1,300,000 / 1,040,000              |                        | ✓ Yes          |
| i7ie.18xlarge   | 6 x 7500 GB            | NVMe SSD            | 1,950,000 / 1,560,000              |                        | ✓ Yes          |
| i7ie.24xlarge   | 8 x 7500 GB            | NVMe SSD            | 2,600,000 / 2,080,000              |                        | ✓ Yes          |
| i7ie.48xlarge   | 16 x 7500 GB           | NVMe SSD            | 5,200,000 / 4,160,000              |                        | ✓ Yes          |
| i7ie.metal-24xl | 8 x 7500 GB            | NVMe SSD            | 2,600,000 / 2,080,000              |                        | ✓ Yes          |
| i7ie.metal-48xl | 16 x 7500 GB           | NVMe SSD            | 5,200,000 / 4,160,000              |                        | ✓ Yes          |
| **I8g**         |
| i8g.large       | 1 x 468 GB             | NVMe SSD            | 75,000 / 41,250                    |                        | ✓ Yes          |
| i8g.xlarge      | 1 x 937 GB             | NVMe SSD            | 150,000 / 82,500                   |                        | ✓ Yes          |
| i8g.2xlarge     | 1 x 1875 GB            | NVMe SSD            | 300,000 / 165,000                  |                        | ✓ Yes          |
| i8g.4xlarge     | 1 x 3750 GB            | NVMe SSD            | 600,000 / 330,000                  |                        | ✓ Yes          |
| i8g.8xlarge     | 2 x 3750 GB            | NVMe SSD            | 1,200,000 / 660,000                |                        | ✓ Yes          |
| i8g.12xlarge    | 3 x 3750 GB            | NVMe SSD            | 1,800,000 / 990,000                |                        | ✓ Yes          |
| i8g.16xlarge    | 4 x 3750 GB            | NVMe SSD            | 2,400,000 / 1,320,000              |                        | ✓ Yes          |
| i8g.24xlarge    | 6 x 3750 GB            | NVMe SSD            | 3,600,000 / 1,980,000              |                        | ✓ Yes          |
| i8g.48xlarge    | 12 x 3750 GB           | NVMe SSD            | 7,200,000 / 3,960,000              |                        | ✓ Yes          |
| i8g.metal-24xl  | 6 x 3750 GB            | NVMe SSD            | 3,600,000 / 1,980,000              |                        | ✓ Yes          |
| **I8ge**        |
| i8ge.large      | 1 x 1250 GB            | NVMe SSD            | 54,166 / 43,333                    |                        | ✓ Yes          |
| i8ge.xlarge     | 1 x 2500 GB            | NVMe SSD            | 108,333 / 86,666                   |                        | ✓ Yes          |
| i8ge.2xlarge    | 2 x 2500 GB            | NVMe SSD            | 216,666 / 173,332                  |                        | ✓ Yes          |
| i8ge.3xlarge    | 1 x 7500 GB            | NVMe SSD            | 325,000 / 260,000                  |                        | ✓ Yes          |
| i8ge.6xlarge    | 2 x 7500 GB            | NVMe SSD            | 650,000 / 520,000                  |                        | ✓ Yes          |
| i8ge.12xlarge   | 4 x 7500 GB            | NVMe SSD            | 1,300,000 / 1,040,000              |                        | ✓ Yes          |
| i8ge.18xlarge   | 6 x 7500 GB            | NVMe SSD            | 1,950,000 / 1,560,000              |                        | ✓ Yes          |
| i8ge.24xlarge   | 8 x 7500 GB            | NVMe SSD            | 2,600,000 / 2,080,000              |                        | ✓ Yes          |
| i8ge.48xlarge   | 16 x 7500 GB           | NVMe SSD            | 5,200,000 / 4,160,000              |                        | ✓ Yes          |
| i8ge.metal-24xl | 8 x 7500 GB            | NVMe SSD            | 2,600,000 / 2,080,000              |                        | ✓ Yes          |
| i8ge.metal-48xl | 16 x 7500 GB           | NVMe SSD            | 5,200,000 / 4,160,000              |                        | ✓ Yes          |
| **Im4gn**       |
| im4gn.large     | 1 x 937 GB             | NVMe SSD            | 31,250 / 25,000                    |                        | ✓ Yes          |
| im4gn.xlarge    | 1 x 1875 GB            | NVMe SSD            | 62,500 / 50,000                    |                        | ✓ Yes          |
| im4gn.2xlarge   | 1 x 3750 GB            | NVMe SSD            | 125,000 / 100,000                  |                        | ✓ Yes          |
| im4gn.4xlarge   | 1 x 7500 GB            | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| im4gn.8xlarge   | 2 x 7500 GB            | NVMe SSD            | 500,000 / 400,000                  |                        | ✓ Yes          |
| im4gn.16xlarge  | 4 x 7500 GB            | NVMe SSD            | 1,000,000 / 800,000                |                        | ✓ Yes          |
| **Is4gen**      |
| is4gen.medium   | 1 x 937 GB             | NVMe SSD            | 31,250 / 25,000                    |                        | ✓ Yes          |
| is4gen.large    | 1 x 1875 GB            | NVMe SSD            | 62,500 / 50,000                    |                        | ✓ Yes          |
| is4gen.xlarge   | 1 x 3750 GB            | NVMe SSD            | 125,000 / 100,000                  |                        | ✓ Yes          |
| is4gen.2xlarge  | 1 x 7500 GB            | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| is4gen.4xlarge  | 2 x 7500 GB            | NVMe SSD            | 500,000 / 400,000                  |                        | ✓ Yes          |
| is4gen.8xlarge  | 4 x 7500 GB            | NVMe SSD            | 1,000,000 / 800,000                |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type   | EBS encryption | Instance store encryption | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| --------------- | -------------- | ------------------------- | --------------------- | ----------- | -------- | -------------- |
| **D2**          |
| d2.xlarge       | ✓ Yes          | ✗ No                      | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| d2.2xlarge      | ✓ Yes          | ✗ No                      | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| d2.4xlarge      | ✓ Yes          | ✗ No                      | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| d2.8xlarge      | ✓ Yes          | ✗ No                      | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **D3**          |
| d3.xlarge       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3.2xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3.4xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3.8xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **D3en**        |
| d3en.xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3en.2xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3en.4xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3en.6xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3en.8xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| d3en.12xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **H1**          |
| h1.2xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| h1.4xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| h1.8xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| h1.16xlarge     | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **I3**          |
| i3.large        | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.xlarge       | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.2xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.4xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.8xlarge      | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.16xlarge     | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i3.metal        | ✓ Yes          | ✓ Yes                     | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **I3en**        |
| i3en.large      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| i3en.xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.2xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.3xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.6xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.12xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.24xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i3en.metal      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **I4g**         |
| i4g.large       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| i4g.xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| i4g.2xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| i4g.4xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| i4g.8xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| i4g.16xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **I4i**         |
| i4i.large       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| i4i.xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.2xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.4xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.8xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.12xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.16xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.24xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.32xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i4i.metal       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **I7i**         |
| i7i.large       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| i7i.xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.2xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.4xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.8xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.12xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.16xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.24xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.48xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7i.metal-24xl  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| i7i.metal-48xl  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **I7ie**        |
| i7ie.large      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| i7ie.xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.2xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.3xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.6xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.12xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.18xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.24xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.48xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i7ie.metal-24xl | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| i7ie.metal-48xl | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **I8g**         |
| i8g.large       | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.xlarge      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.2xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.4xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.8xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.12xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.16xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.24xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.48xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8g.metal-24xl  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **I8ge**        |
| i8ge.large      | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.xlarge     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.2xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.3xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.6xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.12xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.18xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.24xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.48xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| i8ge.metal-24xl | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| i8ge.metal-48xl | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Im4gn**       |
| im4gn.large     | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| im4gn.xlarge    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| im4gn.2xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| im4gn.4xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| im4gn.8xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| im4gn.16xlarge  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **Is4gen**      |
| is4gen.medium   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| is4gen.large    | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| is4gen.xlarge   | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| is4gen.2xlarge  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| is4gen.4xlarge  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| is4gen.8xlarge  | ✓ Yes          | ✓ Yes                     | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
