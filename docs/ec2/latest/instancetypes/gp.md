# Specifications for Amazon EC2 general purpose instances

General purpose instances provide a balance of compute, memory, and networking resources.
These instances are ideal for applications that use these resources in equal proportions,
such as web servers and code repositories.

For information on previous generation instance types of this category, such as M4 instances,
see [Specifications for Amazon EC2 previous generation instances](pg.md "pg.md").

###### Contents

- [Instance families and instance types](#gp_sizes "#gp_sizes")
- [Instance family summary](#gp_summary "#gp_summary")
- [Performance specifications](#gp_hardware "#gp_hardware")
- [Network specifications](#gp_network "#gp_network")
- [Amazon EBS specifications](#gp_storage-ebs "#gp_storage-ebs")
- [Instance store specifications](#gp_instance-store "#gp_instance-store")
- [Security specifications](#gp_security "#gp_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | ----------------- | ------------------ | ------------------ | ------------------ | ------------------- | ------------------- | ------------------ | ------------------ | ---------------- | ----------------- | ----------------- | ----------------- |
| M5              | `m5.large`               | `m5.xlarge`       | `m5.2xlarge`       | `m5.4xlarge`       | `m5.8xlarge`       | `m5.12xlarge`       | `m5.16xlarge`       | `m5.24xlarge`      | `m5.metal`         |
| M5a             | `m5a.large`              | `m5a.xlarge`      | `m5a.2xlarge`      | `m5a.4xlarge`      | `m5a.8xlarge`      | `m5a.12xlarge`      | `m5a.16xlarge`      | `m5a.24xlarge`     |
| M5ad            | `m5ad.large`             | `m5ad.xlarge`     | `m5ad.2xlarge`     | `m5ad.4xlarge`     | `m5ad.8xlarge`     | `m5ad.12xlarge`     | `m5ad.16xlarge`     | `m5ad.24xlarge`    |
| M5d             | `m5d.large`              | `m5d.xlarge`      | `m5d.2xlarge`      | `m5d.4xlarge`      | `m5d.8xlarge`      | `m5d.12xlarge`      | `m5d.16xlarge`      | `m5d.24xlarge`     | `m5d.metal`        |
| M5dn            | `m5dn.large`             | `m5dn.xlarge`     | `m5dn.2xlarge`     | `m5dn.4xlarge`     | `m5dn.8xlarge`     | `m5dn.12xlarge`     | `m5dn.16xlarge`     | `m5dn.24xlarge`    | `m5dn.metal`       |
| M5n             | `m5n.large`              | `m5n.xlarge`      | `m5n.2xlarge`      | `m5n.4xlarge`      | `m5n.8xlarge`      | `m5n.12xlarge`      | `m5n.16xlarge`      | `m5n.24xlarge`     | `m5n.metal`        |
| M5zn            | `m5zn.large`             | `m5zn.xlarge`     | `m5zn.2xlarge`     | `m5zn.3xlarge`     | `m5zn.6xlarge`     | `m5zn.12xlarge`     | `m5zn.metal`        |
| M6a             | `m6a.large`              | `m6a.xlarge`      | `m6a.2xlarge`      | `m6a.4xlarge`      | `m6a.8xlarge`      | `m6a.12xlarge`      | `m6a.16xlarge`      | `m6a.24xlarge`     | `m6a.32xlarge`     | `m6a.48xlarge`   | `m6a.metal`       |
| M6g             | `m6g.medium`             | `m6g.large`       | `m6g.xlarge`       | `m6g.2xlarge`      | `m6g.4xlarge`      | `m6g.8xlarge`       | `m6g.12xlarge`      | `m6g.16xlarge`     | `m6g.metal`        |
| M6gd            | `m6gd.medium`            | `m6gd.large`      | `m6gd.xlarge`      | `m6gd.2xlarge`     | `m6gd.4xlarge`     | `m6gd.8xlarge`      | `m6gd.12xlarge`     | `m6gd.16xlarge`    | `m6gd.metal`       |
| M6i             | `m6i.large`              | `m6i.xlarge`      | `m6i.2xlarge`      | `m6i.4xlarge`      | `m6i.8xlarge`      | `m6i.12xlarge`      | `m6i.16xlarge`      | `m6i.24xlarge`     | `m6i.32xlarge`     | `m6i.metal`      |
| M6id            | `m6id.large`             | `m6id.xlarge`     | `m6id.2xlarge`     | `m6id.4xlarge`     | `m6id.8xlarge`     | `m6id.12xlarge`     | `m6id.16xlarge`     | `m6id.24xlarge`    | `m6id.32xlarge`    | `m6id.metal`     |
| M6idn           | `m6idn.large`            | `m6idn.xlarge`    | `m6idn.2xlarge`    | `m6idn.4xlarge`    | `m6idn.8xlarge`    | `m6idn.12xlarge`    | `m6idn.16xlarge`    | `m6idn.24xlarge`   | `m6idn.32xlarge`   | `m6idn.metal`    |
| M6in            | `m6in.large`             | `m6in.xlarge`     | `m6in.2xlarge`     | `m6in.4xlarge`     | `m6in.8xlarge`     | `m6in.12xlarge`     | `m6in.16xlarge`     | `m6in.24xlarge`    | `m6in.32xlarge`    | `m6in.metal`     |
| M7a             | `m7a.medium`             | `m7a.large`       | `m7a.xlarge`       | `m7a.2xlarge`      | `m7a.4xlarge`      | `m7a.8xlarge`       | `m7a.12xlarge`      | `m7a.16xlarge`     | `m7a.24xlarge`     | `m7a.32xlarge`   | `m7a.48xlarge`    | `m7a.metal-48xl`  |
| M7g             | `m7g.medium`             | `m7g.large`       | `m7g.xlarge`       | `m7g.2xlarge`      | `m7g.4xlarge`      | `m7g.8xlarge`       | `m7g.12xlarge`      | `m7g.16xlarge`     | `m7g.metal`        |
| M7gd            | `m7gd.medium`            | `m7gd.large`      | `m7gd.xlarge`      | `m7gd.2xlarge`     | `m7gd.4xlarge`     | `m7gd.8xlarge`      | `m7gd.12xlarge`     | `m7gd.16xlarge`    | `m7gd.metal`       |
| M7i             | `m7i.large`              | `m7i.xlarge`      | `m7i.2xlarge`      | `m7i.4xlarge`      | `m7i.8xlarge`      | `m7i.12xlarge`      | `m7i.16xlarge`      | `m7i.24xlarge`     | `m7i.48xlarge`     | `m7i.metal-24xl` | `m7i.metal-48xl`  |
| M7i-flex        | `m7i-flex.large`         | `m7i-flex.xlarge` | `m7i-flex.2xlarge` | `m7i-flex.4xlarge` | `m7i-flex.8xlarge` | `m7i-flex.12xlarge` | `m7i-flex.16xlarge` |
| M8a             | `m8a.medium`             | `m8a.large`       | `m8a.xlarge`       | `m8a.2xlarge`      | `m8a.4xlarge`      | `m8a.8xlarge`       | `m8a.12xlarge`      | `m8a.16xlarge`     | `m8a.24xlarge`     | `m8a.48xlarge`   | `m8a.metal-24xl`  | `m8a.metal-48xl`  |
| M8azn           | `m8azn.medium`           | `m8azn.large`     | `m8azn.xlarge`     | `m8azn.3xlarge`    | `m8azn.6xlarge`    | `m8azn.12xlarge`    | `m8azn.24xlarge`    | `m8azn.metal-12xl` | `m8azn.metal-24xl` |
| M8g             | `m8g.medium`             | `m8g.large`       | `m8g.xlarge`       | `m8g.2xlarge`      | `m8g.4xlarge`      | `m8g.8xlarge`       | `m8g.12xlarge`      | `m8g.16xlarge`     | `m8g.24xlarge`     | `m8g.48xlarge`   | `m8g.metal-24xl`  | `m8g.metal-48xl`  |
| M8gb            | `m8gb.medium`            | `m8gb.large`      | `m8gb.xlarge`      | `m8gb.2xlarge`     | `m8gb.4xlarge`     | `m8gb.8xlarge`      | `m8gb.12xlarge`     | `m8gb.16xlarge`    | `m8gb.24xlarge`    | `m8gb.48xlarge`  |
| M8gd            | `m8gd.medium`            | `m8gd.large`      | `m8gd.xlarge`      | `m8gd.2xlarge`     | `m8gd.4xlarge`     | `m8gd.8xlarge`      | `m8gd.12xlarge`     | `m8gd.16xlarge`    | `m8gd.24xlarge`    | `m8gd.48xlarge`  | `m8gd.metal-24xl` | `m8gd.metal-48xl` |
| M8gn            | `m8gn.medium`            | `m8gn.large`      | `m8gn.xlarge`      | `m8gn.2xlarge`     | `m8gn.4xlarge`     | `m8gn.8xlarge`      | `m8gn.12xlarge`     | `m8gn.16xlarge`    | `m8gn.24xlarge`    | `m8gn.48xlarge`  |
| M8i             | `m8i.large`              | `m8i.xlarge`      | `m8i.2xlarge`      | `m8i.4xlarge`      | `m8i.8xlarge`      | `m8i.12xlarge`      | `m8i.16xlarge`      | `m8i.24xlarge`     | `m8i.32xlarge`     | `m8i.48xlarge`   | `m8i.96xlarge`    | `m8i.metal-48xl`  | `m8i.metal-96xl`  |
| M8id            | `m8id.large`             | `m8id.xlarge`     | `m8id.2xlarge`     | `m8id.4xlarge`     | `m8id.8xlarge`     | `m8id.12xlarge`     | `m8id.16xlarge`     | `m8id.24xlarge`    | `m8id.32xlarge`    | `m8id.48xlarge`  | `m8id.96xlarge`   | `m8id.metal-48xl` | `m8id.metal-96xl` |
| M8i-flex        | `m8i-flex.large`         | `m8i-flex.xlarge` | `m8i-flex.2xlarge` | `m8i-flex.4xlarge` | `m8i-flex.8xlarge` | `m8i-flex.12xlarge` | `m8i-flex.16xlarge` |
| Mac1            | `mac1.metal`             |
| Mac2            | `mac2.metal`             |
| Mac2-m1ultra    | `mac2-m1ultra.metal`     |
| Mac2-m2         | `mac2-m2.metal`          |
| Mac2-m2pro      | `mac2-m2pro.metal`       |
| Mac-m4          | `mac-m4.metal`           |
| Mac-m4pro       | `mac-m4pro.metal`        |
| T2              | `t2.nano`                | `t2.micro`        | `t2.small`         | `t2.medium`        | `t2.large`         | `t2.xlarge`         | `t2.2xlarge`        |
| T3              | `t3.nano`                | `t3.micro`        | `t3.small`         | `t3.medium`        | `t3.large`         | `t3.xlarge`         | `t3.2xlarge`        |
| T3a             | `t3a.nano`               | `t3a.micro`       | `t3a.small`        | `t3a.medium`       | `t3a.large`        | `t3a.xlarge`        | `t3a.2xlarge`       |
| T4g             | `t4g.nano`               | `t4g.micro`       | `t4g.small`        | `t4g.medium`       | `t4g.large`        | `t4g.xlarge`        | `t4g.2xlarge`       |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| M5              | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M5a             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M5ad            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M5d             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M5dn            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M5n             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M5zn            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M6a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M6g             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M6gd            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M6i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M6id            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M6idn           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M6in            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M7a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M7g             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M7gd            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M7i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M7i-flex        | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M8a             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M8azn           | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M8g             | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M8gb            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M8gd            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M8gn            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| M8i             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M8id            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M8i-flex        | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| Mac1            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64_mac)            | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac2            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac2-m1ultra    | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac2-m2         | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac2-m2pro      | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac-m4          | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| Mac-m4pro       | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Apple (arm64_mac)             | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| T2              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| T3              | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| T3a             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| T4g             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Linux                       |

## Performance specifications

| Instance type      | Memory (GiB) | Processor                       | vCPUs | CPU cores | Threads per core | Accelerators | Accelerator memory |
| ------------------ | ------------ | ------------------------------- | ----- | --------- | ---------------- | ------------ | ------------------ |
| **M5**             |
| m5.large           | 8.00         | Intel Xeon Platinum 8175        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5.xlarge          | 16.00        | Intel Xeon Platinum 8175        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5.2xlarge         | 32.00        | Intel Xeon Platinum 8175        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5.4xlarge         | 64.00        | Intel Xeon Platinum 8175        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5.8xlarge         | 128.00       | Intel Xeon Platinum 8175        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5.12xlarge        | 192.00       | Intel Xeon Platinum 8175        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5.16xlarge        | 256.00       | Intel Xeon Platinum 8175        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5.24xlarge        | 384.00       | Intel Xeon Platinum 8175        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m5.metal           | 384.00       | Intel Xeon Platinum 8175        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5a**            |
| m5a.large          | 8.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5a.xlarge         | 16.00        | AMD EPYC 7571                   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5a.2xlarge        | 32.00        | AMD EPYC 7571                   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5a.4xlarge        | 64.00        | AMD EPYC 7571                   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5a.8xlarge        | 128.00       | AMD EPYC 7571                   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5a.12xlarge       | 192.00       | AMD EPYC 7571                   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5a.16xlarge       | 256.00       | AMD EPYC 7571                   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5a.24xlarge       | 384.00       | AMD EPYC 7571                   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5ad**           |
| m5ad.large         | 8.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5ad.xlarge        | 16.00        | AMD EPYC 7571                   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5ad.2xlarge       | 32.00        | AMD EPYC 7571                   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5ad.4xlarge       | 64.00        | AMD EPYC 7571                   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5ad.8xlarge       | 128.00       | AMD EPYC 7571                   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5ad.12xlarge      | 192.00       | AMD EPYC 7571                   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5ad.16xlarge      | 256.00       | AMD EPYC 7571                   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5ad.24xlarge      | 384.00       | AMD EPYC 7571                   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5d**            |
| m5d.large          | 8.00         | Intel Xeon Platinum 8175        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5d.xlarge         | 16.00        | Intel Xeon Platinum 8175        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5d.2xlarge        | 32.00        | Intel Xeon Platinum 8175        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5d.4xlarge        | 64.00        | Intel Xeon Platinum 8175        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5d.8xlarge        | 128.00       | Intel Xeon Platinum 8175        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5d.12xlarge       | 192.00       | Intel Xeon Platinum 8175        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5d.16xlarge       | 256.00       | Intel Xeon Platinum 8175        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5d.24xlarge       | 384.00       | Intel Xeon Platinum 8175        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m5d.metal          | 384.00       | Intel Xeon Platinum 8175        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5dn**           |
| m5dn.large         | 8.00         | Intel Xeon Platinum 8259        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5dn.xlarge        | 16.00        | Intel Xeon Platinum 8259        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5dn.2xlarge       | 32.00        | Intel Xeon Platinum 8259        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5dn.4xlarge       | 64.00        | Intel Xeon Platinum 8259        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5dn.8xlarge       | 128.00       | Intel Xeon Platinum 8259        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5dn.12xlarge      | 192.00       | Intel Xeon Platinum 8259        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5dn.16xlarge      | 256.00       | Intel Xeon Platinum 8259        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5dn.24xlarge      | 384.00       | Intel Xeon Platinum 8259        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m5dn.metal         | 384.00       | Intel Xeon Platinum 8259        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5n**            |
| m5n.large          | 8.00         | Intel Xeon Platinum 8259        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5n.xlarge         | 16.00        | Intel Xeon Platinum 8259        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5n.2xlarge        | 32.00        | Intel Xeon Platinum 8259        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5n.4xlarge        | 64.00        | Intel Xeon Platinum 8259        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m5n.8xlarge        | 128.00       | Intel Xeon Platinum 8259        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m5n.12xlarge       | 192.00       | Intel Xeon Platinum 8259        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5n.16xlarge       | 256.00       | Intel Xeon Platinum 8259        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m5n.24xlarge       | 384.00       | Intel Xeon Platinum 8259        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m5n.metal          | 384.00       | Intel Xeon Platinum 8259        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **M5zn**           |
| m5zn.large         | 8.00         | Intel Xeon Platinum 8252        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m5zn.xlarge        | 16.00        | Intel Xeon Platinum 8252        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m5zn.2xlarge       | 32.00        | Intel Xeon Platinum 8252        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m5zn.3xlarge       | 48.00        | Intel Xeon Platinum 8252        | 12    | 6         | 2                | ✗ No         | ✗ No               |
| m5zn.6xlarge       | 96.00        | Intel Xeon Platinum 8252        | 24    | 12        | 2                | ✗ No         | ✗ No               |
| m5zn.12xlarge      | 192.00       | Intel Xeon Platinum 8252        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m5zn.metal         | 192.00       | Intel Xeon Platinum 8252        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| **M6a**            |
| m6a.large          | 8.00         | AMD EPYC 7R13                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m6a.xlarge         | 16.00        | AMD EPYC 7R13                   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m6a.2xlarge        | 32.00        | AMD EPYC 7R13                   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m6a.4xlarge        | 64.00        | AMD EPYC 7R13                   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m6a.8xlarge        | 128.00       | AMD EPYC 7R13                   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m6a.12xlarge       | 192.00       | AMD EPYC 7R13                   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m6a.16xlarge       | 256.00       | AMD EPYC 7R13                   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m6a.24xlarge       | 384.00       | AMD EPYC 7R13                   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m6a.32xlarge       | 512.00       | AMD EPYC 7R13                   | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m6a.48xlarge       | 768.00       | AMD EPYC 7R13                   | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m6a.metal          | 768.00       | AMD EPYC 7R13                   | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **M6g**            |
| m6g.medium         | 4.00         | AWS Graviton2 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m6g.large          | 8.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m6g.xlarge         | 16.00        | AWS Graviton2 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m6g.2xlarge        | 32.00        | AWS Graviton2 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m6g.4xlarge        | 64.00        | AWS Graviton2 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m6g.8xlarge        | 128.00       | AWS Graviton2 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m6g.12xlarge       | 192.00       | AWS Graviton2 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m6g.16xlarge       | 256.00       | AWS Graviton2 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m6g.metal          | 256.00       | AWS Graviton2 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **M6gd**           |
| m6gd.medium        | 4.00         | AWS Graviton2 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m6gd.large         | 8.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m6gd.xlarge        | 16.00        | AWS Graviton2 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m6gd.2xlarge       | 32.00        | AWS Graviton2 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m6gd.4xlarge       | 64.00        | AWS Graviton2 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m6gd.8xlarge       | 128.00       | AWS Graviton2 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m6gd.12xlarge      | 192.00       | AWS Graviton2 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m6gd.16xlarge      | 256.00       | AWS Graviton2 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m6gd.metal         | 256.00       | AWS Graviton2 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **M6i**            |
| m6i.large          | 8.00         | Intel Xeon Ice Lake             | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m6i.xlarge         | 16.00        | Intel Xeon Ice Lake             | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m6i.2xlarge        | 32.00        | Intel Xeon Ice Lake             | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m6i.4xlarge        | 64.00        | Intel Xeon Ice Lake             | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m6i.8xlarge        | 128.00       | Intel Xeon Ice Lake             | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m6i.12xlarge       | 192.00       | Intel Xeon Ice Lake             | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m6i.16xlarge       | 256.00       | Intel Xeon Ice Lake             | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m6i.24xlarge       | 384.00       | Intel Xeon Ice Lake             | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m6i.32xlarge       | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m6i.metal          | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **M6id**           |
| m6id.large         | 8.00         | Intel Xeon Ice Lake             | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m6id.xlarge        | 16.00        | Intel Xeon Ice Lake             | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m6id.2xlarge       | 32.00        | Intel Xeon Ice Lake             | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m6id.4xlarge       | 64.00        | Intel Xeon Ice Lake             | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m6id.8xlarge       | 128.00       | Intel Xeon Ice Lake             | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m6id.12xlarge      | 192.00       | Intel Xeon Ice Lake             | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m6id.16xlarge      | 256.00       | Intel Xeon Ice Lake             | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m6id.24xlarge      | 384.00       | Intel Xeon Ice Lake             | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m6id.32xlarge      | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m6id.metal         | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **M6idn**          |
| m6idn.large        | 8.00         | Intel Xeon Ice Lake             | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m6idn.xlarge       | 16.00        | Intel Xeon Ice Lake             | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m6idn.2xlarge      | 32.00        | Intel Xeon Ice Lake             | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m6idn.4xlarge      | 64.00        | Intel Xeon Ice Lake             | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m6idn.8xlarge      | 128.00       | Intel Xeon Ice Lake             | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m6idn.12xlarge     | 192.00       | Intel Xeon Ice Lake             | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m6idn.16xlarge     | 256.00       | Intel Xeon Ice Lake             | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m6idn.24xlarge     | 384.00       | Intel Xeon Ice Lake             | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m6idn.32xlarge     | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m6idn.metal        | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **M6in**           |
| m6in.large         | 8.00         | Intel Xeon Ice Lake             | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m6in.xlarge        | 16.00        | Intel Xeon Ice Lake             | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m6in.2xlarge       | 32.00        | Intel Xeon Ice Lake             | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m6in.4xlarge       | 64.00        | Intel Xeon Ice Lake             | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m6in.8xlarge       | 128.00       | Intel Xeon Ice Lake             | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m6in.12xlarge      | 192.00       | Intel Xeon Ice Lake             | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m6in.16xlarge      | 256.00       | Intel Xeon Ice Lake             | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m6in.24xlarge      | 384.00       | Intel Xeon Ice Lake             | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m6in.32xlarge      | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m6in.metal         | 512.00       | Intel Xeon Ice Lake             | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **M7a**            |
| m7a.medium         | 4.00         | AMD EPYC 9R14                   | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m7a.large          | 8.00         | AMD EPYC 9R14                   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m7a.xlarge         | 16.00        | AMD EPYC 9R14                   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m7a.2xlarge        | 32.00        | AMD EPYC 9R14                   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m7a.4xlarge        | 64.00        | AMD EPYC 9R14                   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m7a.8xlarge        | 128.00       | AMD EPYC 9R14                   | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m7a.12xlarge       | 192.00       | AMD EPYC 9R14                   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m7a.16xlarge       | 256.00       | AMD EPYC 9R14                   | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m7a.24xlarge       | 384.00       | AMD EPYC 9R14                   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m7a.32xlarge       | 512.00       | AMD EPYC 9R14                   | 128   | 128       | 1                | ✗ No         | ✗ No               |
| m7a.48xlarge       | 768.00       | AMD EPYC 9R14                   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| m7a.metal-48xl     | 768.00       | AMD EPYC 9R14                   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M7g**            |
| m7g.medium         | 4.00         | AWS Graviton3 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m7g.large          | 8.00         | AWS Graviton3 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m7g.xlarge         | 16.00        | AWS Graviton3 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m7g.2xlarge        | 32.00        | AWS Graviton3 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m7g.4xlarge        | 64.00        | AWS Graviton3 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m7g.8xlarge        | 128.00       | AWS Graviton3 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m7g.12xlarge       | 192.00       | AWS Graviton3 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m7g.16xlarge       | 256.00       | AWS Graviton3 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m7g.metal          | 256.00       | AWS Graviton3 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **M7gd**           |
| m7gd.medium        | 4.00         | AWS Graviton3 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m7gd.large         | 8.00         | AWS Graviton3 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m7gd.xlarge        | 16.00        | AWS Graviton3 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m7gd.2xlarge       | 32.00        | AWS Graviton3 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m7gd.4xlarge       | 64.00        | AWS Graviton3 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m7gd.8xlarge       | 128.00       | AWS Graviton3 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m7gd.12xlarge      | 192.00       | AWS Graviton3 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m7gd.16xlarge      | 256.00       | AWS Graviton3 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m7gd.metal         | 256.00       | AWS Graviton3 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **M7i**            |
| m7i.large          | 8.00         | Intel Xeon Sapphire Rapids      | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m7i.xlarge         | 16.00        | Intel Xeon Sapphire Rapids      | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m7i.2xlarge        | 32.00        | Intel Xeon Sapphire Rapids      | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m7i.4xlarge        | 64.00        | Intel Xeon Sapphire Rapids      | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m7i.8xlarge        | 128.00       | Intel Xeon Sapphire Rapids      | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m7i.12xlarge       | 192.00       | Intel Xeon Sapphire Rapids      | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m7i.16xlarge       | 256.00       | Intel Xeon Sapphire Rapids      | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m7i.24xlarge       | 384.00       | Intel Xeon Sapphire Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m7i.48xlarge       | 768.00       | Intel Xeon Sapphire Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m7i.metal-24xl     | 384.00       | Intel Xeon Sapphire Rapids      | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m7i.metal-48xl     | 768.00       | Intel Xeon Sapphire Rapids      | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **M7i-flex**       |
| m7i-flex.large     | 8.00         | Intel Xeon Sapphire Rapids      | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m7i-flex.xlarge    | 16.00        | Intel Xeon Sapphire Rapids      | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m7i-flex.2xlarge   | 32.00        | Intel Xeon Sapphire Rapids      | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m7i-flex.4xlarge   | 64.00        | Intel Xeon Sapphire Rapids      | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m7i-flex.8xlarge   | 128.00       | Intel Xeon Sapphire Rapids      | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m7i-flex.12xlarge  | 192.00       | Intel Xeon Sapphire Rapids      | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m7i-flex.16xlarge  | 256.00       | Intel Xeon Sapphire Rapids      | 64    | 32        | 2                | ✗ No         | ✗ No               |
| **M8a**            |
| m8a.medium         | 4.00         | AMD EPYC 9R45                   | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8a.large          | 8.00         | AMD EPYC 9R45                   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8a.xlarge         | 16.00        | AMD EPYC 9R45                   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8a.2xlarge        | 32.00        | AMD EPYC 9R45                   | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m8a.4xlarge        | 64.00        | AMD EPYC 9R45                   | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m8a.8xlarge        | 128.00       | AMD EPYC 9R45                   | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m8a.12xlarge       | 192.00       | AMD EPYC 9R45                   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8a.16xlarge       | 256.00       | AMD EPYC 9R45                   | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m8a.24xlarge       | 384.00       | AMD EPYC 9R45                   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8a.48xlarge       | 768.00       | AMD EPYC 9R45                   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| m8a.metal-24xl     | 384.00       | AMD EPYC 9R45                   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8a.metal-48xl     | 768.00       | AMD EPYC 9R45                   | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M8azn**          |
| m8azn.medium       | 4.00         | AMD EPYC 9R05                   | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8azn.large        | 8.00         | AMD EPYC 9R05                   | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8azn.xlarge       | 16.00        | AMD EPYC 9R05                   | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8azn.3xlarge      | 48.00        | AMD EPYC 9R05                   | 12    | 12        | 1                | ✗ No         | ✗ No               |
| m8azn.6xlarge      | 96.00        | AMD EPYC 9R05                   | 24    | 24        | 1                | ✗ No         | ✗ No               |
| m8azn.12xlarge     | 192.00       | AMD EPYC 9R05                   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8azn.24xlarge     | 384.00       | AMD EPYC 9R05                   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8azn.metal-12xl   | 192.00       | AMD EPYC 9R05                   | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8azn.metal-24xl   | 384.00       | AMD EPYC 9R05                   | 96    | 96        | 1                | ✗ No         | ✗ No               |
| **M8g**            |
| m8g.medium         | 4.00         | AWS Graviton4 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8g.large          | 8.00         | AWS Graviton4 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8g.xlarge         | 16.00        | AWS Graviton4 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8g.2xlarge        | 32.00        | AWS Graviton4 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m8g.4xlarge        | 64.00        | AWS Graviton4 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m8g.8xlarge        | 128.00       | AWS Graviton4 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m8g.12xlarge       | 192.00       | AWS Graviton4 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8g.16xlarge       | 256.00       | AWS Graviton4 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m8g.24xlarge       | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8g.48xlarge       | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| m8g.metal-24xl     | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8g.metal-48xl     | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M8gb**           |
| m8gb.medium        | 4.00         | AWS Graviton4 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8gb.large         | 8.00         | AWS Graviton4 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8gb.xlarge        | 16.00        | AWS Graviton4 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8gb.2xlarge       | 32.00        | AWS Graviton4 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m8gb.4xlarge       | 64.00        | AWS Graviton4 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m8gb.8xlarge       | 128.00       | AWS Graviton4 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m8gb.12xlarge      | 192.00       | AWS Graviton4 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8gb.16xlarge      | 256.00       | AWS Graviton4 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m8gb.24xlarge      | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8gb.48xlarge      | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M8gd**           |
| m8gd.medium        | 4.00         | AWS Graviton4 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8gd.large         | 8.00         | AWS Graviton4 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8gd.xlarge        | 16.00        | AWS Graviton4 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8gd.2xlarge       | 32.00        | AWS Graviton4 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m8gd.4xlarge       | 64.00        | AWS Graviton4 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m8gd.8xlarge       | 128.00       | AWS Graviton4 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m8gd.12xlarge      | 192.00       | AWS Graviton4 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8gd.16xlarge      | 256.00       | AWS Graviton4 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m8gd.24xlarge      | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8gd.48xlarge      | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| m8gd.metal-24xl    | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8gd.metal-48xl    | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M8gn**           |
| m8gn.medium        | 4.00         | AWS Graviton4 Processor         | 1     | 1         | 1                | ✗ No         | ✗ No               |
| m8gn.large         | 8.00         | AWS Graviton4 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| m8gn.xlarge        | 16.00        | AWS Graviton4 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| m8gn.2xlarge       | 32.00        | AWS Graviton4 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |
| m8gn.4xlarge       | 64.00        | AWS Graviton4 Processor         | 16    | 16        | 1                | ✗ No         | ✗ No               |
| m8gn.8xlarge       | 128.00       | AWS Graviton4 Processor         | 32    | 32        | 1                | ✗ No         | ✗ No               |
| m8gn.12xlarge      | 192.00       | AWS Graviton4 Processor         | 48    | 48        | 1                | ✗ No         | ✗ No               |
| m8gn.16xlarge      | 256.00       | AWS Graviton4 Processor         | 64    | 64        | 1                | ✗ No         | ✗ No               |
| m8gn.24xlarge      | 384.00       | AWS Graviton4 Processor         | 96    | 96        | 1                | ✗ No         | ✗ No               |
| m8gn.48xlarge      | 768.00       | AWS Graviton4 Processor         | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **M8i**            |
| m8i.large          | 8.00         | Intel Xeon Granite Rapids       | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m8i.xlarge         | 16.00        | Intel Xeon Granite Rapids       | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m8i.2xlarge        | 32.00        | Intel Xeon Granite Rapids       | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m8i.4xlarge        | 64.00        | Intel Xeon Granite Rapids       | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m8i.8xlarge        | 128.00       | Intel Xeon Granite Rapids       | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m8i.12xlarge       | 192.00       | Intel Xeon Granite Rapids       | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m8i.16xlarge       | 256.00       | Intel Xeon Granite Rapids       | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m8i.24xlarge       | 384.00       | Intel Xeon Granite Rapids       | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m8i.32xlarge       | 512.00       | Intel Xeon Granite Rapids       | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m8i.48xlarge       | 768.00       | Intel Xeon Granite Rapids       | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m8i.96xlarge       | 1536.00      | Intel Xeon Granite Rapids       | 384   | 192       | 2                | ✗ No         | ✗ No               |
| m8i.metal-48xl     | 768.00       | Intel Xeon Granite Rapids       | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m8i.metal-96xl     | 1536.00      | Intel Xeon Granite Rapids       | 384   | 192       | 2                | ✗ No         | ✗ No               |
| **M8id**           |
| m8id.large         | 8.00         | Intel Xeon Granite Rapids       | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m8id.xlarge        | 16.00        | Intel Xeon Granite Rapids       | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m8id.2xlarge       | 32.00        | Intel Xeon Granite Rapids       | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m8id.4xlarge       | 64.00        | Intel Xeon Granite Rapids       | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m8id.8xlarge       | 128.00       | Intel Xeon Granite Rapids       | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m8id.12xlarge      | 192.00       | Intel Xeon Granite Rapids       | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m8id.16xlarge      | 256.00       | Intel Xeon Granite Rapids       | 64    | 32        | 2                | ✗ No         | ✗ No               |
| m8id.24xlarge      | 384.00       | Intel Xeon Granite Rapids       | 96    | 48        | 2                | ✗ No         | ✗ No               |
| m8id.32xlarge      | 512.00       | Intel Xeon Granite Rapids       | 128   | 64        | 2                | ✗ No         | ✗ No               |
| m8id.48xlarge      | 768.00       | Intel Xeon Granite Rapids       | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m8id.96xlarge      | 1536.00      | Intel Xeon Granite Rapids       | 384   | 192       | 2                | ✗ No         | ✗ No               |
| m8id.metal-48xl    | 768.00       | Intel Xeon Granite Rapids       | 192   | 96        | 2                | ✗ No         | ✗ No               |
| m8id.metal-96xl    | 1536.00      | Intel Xeon Granite Rapids       | 384   | 192       | 2                | ✗ No         | ✗ No               |
| **M8i-flex**       |
| m8i-flex.large     | 8.00         | Intel Xeon Granite Rapids       | 2     | 1         | 2                | ✗ No         | ✗ No               |
| m8i-flex.xlarge    | 16.00        | Intel Xeon Granite Rapids       | 4     | 2         | 2                | ✗ No         | ✗ No               |
| m8i-flex.2xlarge   | 32.00        | Intel Xeon Granite Rapids       | 8     | 4         | 2                | ✗ No         | ✗ No               |
| m8i-flex.4xlarge   | 64.00        | Intel Xeon Granite Rapids       | 16    | 8         | 2                | ✗ No         | ✗ No               |
| m8i-flex.8xlarge   | 128.00       | Intel Xeon Granite Rapids       | 32    | 16        | 2                | ✗ No         | ✗ No               |
| m8i-flex.12xlarge  | 192.00       | Intel Xeon Granite Rapids       | 48    | 24        | 2                | ✗ No         | ✗ No               |
| m8i-flex.16xlarge  | 256.00       | Intel Xeon Granite Rapids       | 64    | 32        | 2                | ✗ No         | ✗ No               |
| **Mac1**           |
| mac1.metal         | 32.00        | Intel Core i7-8700B             | 12    | 6         | 2                | ✗ No         | ✗ No               |
| **Mac2**           |
| mac2.metal         | 16.00        | Apple M1 chip with 8-core CPU   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| **Mac2-m1ultra**   |
| mac2-m1ultra.metal | 128.00       | Apple M1 Ultra with 20‑core CPU | 20    | 20        | 1                | ✗ No         | ✗ No               |
| **Mac2-m2**        |
| mac2-m2.metal      | 24.00        | Apple M2 with 8‑core CPU        | 8     | 8         | 1                | ✗ No         | ✗ No               |
| **Mac2-m2pro**     |
| mac2-m2pro.metal   | 32.00        | Apple M2 Pro with 12‑core CPU   | 12    | 12        | 1                | ✗ No         | ✗ No               |
| **Mac-m4**         |
| mac-m4.metal       | 24.00        | Apple M4 with 10‑core CPU       | 10    | 10        | 1                | ✗ No         | ✗ No               |
| **Mac-m4pro**      |
| mac-m4pro.metal    | 48.00        | Apple M4 with 12‑core CPU       | 14    | 14        | 1                | ✗ No         | ✗ No               |
| **T2**             |
| t2.nano 1          | 0.50         | Intel Xeon Family               | 1     | 1         | 1                | ✗ No         | ✗ No               |
| t2.micro 1         | 1.00         | Intel Xeon Family               | 1     | 1         | 1                | ✗ No         | ✗ No               |
| t2.small 1         | 2.00         | Intel Xeon Family               | 1     | 1         | 1                | ✗ No         | ✗ No               |
| t2.medium 1        | 4.00         | Intel Broadwell E5-2686v4       | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t2.large 1         | 8.00         | Intel Broadwell E5-2686v4       | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t2.xlarge 1        | 16.00        | Intel Broadwell E5-2686v4       | 4     | 4         | 1                | ✗ No         | ✗ No               |
| t2.2xlarge 1       | 32.00        | Intel Broadwell E5-2686v4       | 8     | 8         | 1                | ✗ No         | ✗ No               |
| **T3**             |
| t3.nano 1          | 0.50         | Intel Skylake P-8175            | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3.micro 1         | 1.00         | Intel Skylake P-8175            | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3.small 1         | 2.00         | Intel Skylake P-8175            | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3.medium 1        | 4.00         | Intel Skylake P-8175            | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3.large 1         | 8.00         | Intel Skylake P-8175            | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3.xlarge 1        | 16.00        | Intel Skylake P-8175            | 4     | 2         | 2                | ✗ No         | ✗ No               |
| t3.2xlarge 1       | 32.00        | Intel Skylake P-8175            | 8     | 4         | 2                | ✗ No         | ✗ No               |
| **T3a**            |
| t3a.nano 1         | 0.50         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3a.micro 1        | 1.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3a.small 1        | 2.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3a.medium 1       | 4.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3a.large 1        | 8.00         | AMD EPYC 7571                   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| t3a.xlarge 1       | 16.00        | AMD EPYC 7571                   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| t3a.2xlarge 1      | 32.00        | AMD EPYC 7571                   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| **T4g**            |
| t4g.nano 1         | 0.50         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t4g.micro 1        | 1.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t4g.small 1        | 2.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t4g.medium 1       | 4.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t4g.large 1        | 8.00         | AWS Graviton2 Processor         | 2     | 2         | 1                | ✗ No         | ✗ No               |
| t4g.xlarge 1       | 16.00        | AWS Graviton2 Processor         | 4     | 4         | 1                | ✗ No         | ✗ No               |
| t4g.2xlarge 1      | 32.00        | AWS Graviton2 Processor         | 8     | 8         | 1                | ✗ No         | ✗ No               |

###### Note

1 These are burstable instance types that provide a baseline CPU
performance with the ability to burst beyond their baseline at any time using CPU credits. For
more information, see [Burstable performance instances](../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md "../../../AWSEC2/latest/UserGuide/burstable-performance-instances.md").

## Network specifications

###### Note

M8a, M8g, M8gd, M8i, M8id, M8i-flex instance types support configurable bandwidth weightings.
With these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
instance types. For the supported configurable weightings, see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").

| Instance type       | Baseline / Burst bandwidth (Gbps) | EFA   | ENA   | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| ------------------- | --------------------------------- | ----- | ----- | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **M5**              |
| m5.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5.8xlarge          | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5.12xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5.16xlarge         | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5.24xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5a**             |
| m5a.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5a.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5a.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5a.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5a.8xlarge 1       | 7.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5a.12xlarge        | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5a.16xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5a.24xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5ad**            |
| m5ad.large 1        | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5ad.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5ad.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5ad.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5ad.8xlarge 1      | 7.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5ad.12xlarge       | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5ad.16xlarge       | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5ad.24xlarge       | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5d**             |
| m5d.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5d.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5d.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5d.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5d.8xlarge         | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5d.12xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5d.16xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5d.24xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5d.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5dn**            |
| m5dn.large 1        | 2.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5dn.xlarge 1       | 4.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5dn.2xlarge 1      | 8.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5dn.4xlarge 1      | 16.25 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5dn.8xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5dn.12xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5dn.16xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5dn.24xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5dn.metal          | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5n**             |
| m5n.large 1         | 2.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5n.xlarge 1        | 4.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5n.2xlarge 1       | 8.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5n.4xlarge 1       | 16.25 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5n.8xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5n.12xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5n.16xlarge        | 75 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5n.24xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5n.metal           | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M5zn**            |
| m5zn.large 1        | 3.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m5zn.xlarge 1       | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5zn.2xlarge 1      | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m5zn.3xlarge 1      | 15.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5zn.6xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m5zn.12xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m5zn.metal          | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M6a**             |
| m6a.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6a.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6a.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6a.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6a.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6a.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6a.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6a.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6a.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6a.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6a.metal           | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M6g**             |
| m6g.medium 1        | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m6g.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6g.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6g.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6g.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6g.8xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6g.12xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6g.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m6g.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M6gd**            |
| m6gd.medium 1       | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m6gd.large 1        | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6gd.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6gd.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6gd.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6gd.8xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6gd.12xlarge       | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6gd.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| m6gd.metal          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M6i**             |
| m6i.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6i.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6i.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6i.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6i.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6i.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6i.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6i.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6i.32xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6i.metal           | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M6id**            |
| m6id.large 1        | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6id.xlarge 1       | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6id.2xlarge 1      | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6id.4xlarge 1      | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6id.8xlarge        | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6id.12xlarge       | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6id.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6id.24xlarge       | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6id.32xlarge       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6id.metal          | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M6idn**           |
| m6idn.large 1       | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6idn.xlarge 1      | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6idn.2xlarge 1     | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6idn.4xlarge 1     | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6idn.8xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6idn.12xlarge      | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6idn.16xlarge      | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6idn.24xlarge      | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6idn.32xlarge      | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| m6idn.metal         | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **M6in**            |
| m6in.large 1        | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m6in.xlarge 1       | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6in.2xlarge 1      | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m6in.4xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m6in.8xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6in.12xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m6in.16xlarge       | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6in.24xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m6in.32xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| m6in.metal          | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **M7a**             |
| m7a.medium 1        | 0.39 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m7a.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m7a.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7a.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7a.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7a.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7a.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m7a.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7a.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7a.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7a.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7a.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M7g**             |
| m7g.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m7g.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m7g.xlarge 1        | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7g.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7g.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7g.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7g.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m7g.16xlarge        | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7g.metal           | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M7gd**            |
| m7gd.medium 1       | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m7gd.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m7gd.xlarge 1       | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7gd.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7gd.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7gd.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7gd.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m7gd.16xlarge       | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7gd.metal          | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M7i**             |
| m7i.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m7i.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7i.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7i.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7i.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7i.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m7i.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7i.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7i.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7i.metal-24xl      | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m7i.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M7i-flex**        |
| m7i-flex.large 1    | 0.39 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m7i-flex.xlarge 1   | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7i-flex.2xlarge 1  | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m7i-flex.4xlarge 1  | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7i-flex.8xlarge 1  | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7i-flex.12xlarge 1 | 9.375 / 18.75                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m7i-flex.16xlarge 1 | 12.5 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **M8a**             |
| m8a.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m8a.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| m8a.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| m8a.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 40                         | ✓ Yes |
| m8a.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| m8a.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 40                         | ✓ Yes |
| m8a.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 64                         | ✓ Yes |
| m8a.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8a.24xlarge        | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8a.48xlarge        | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8a.metal-24xl      | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8a.metal-48xl      | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **M8azn**           |
| m8azn.medium 1      | 2.08 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 4                          | ✓ Yes |
| m8azn.large 1       | 4.17 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| m8azn.xlarge 1      | 8.33 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| m8azn.3xlarge 1     | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| m8azn.6xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| m8azn.12xlarge      | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8azn.24xlarge      | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8azn.metal-12xl    | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8azn.metal-24xl    | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| **M8g**             |
| m8g.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m8g.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m8g.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8g.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8g.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8g.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8g.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m8g.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8g.24xlarge        | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8g.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8g.metal-24xl      | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8g.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M8gb**            |
| m8gb.medium 1       | 2.083 / 16.666                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m8gb.large 1        | 4.166 / 20.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m8gb.xlarge 1       | 8.333 / 26.666                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gb.2xlarge 1      | 16.666 / 33.333                   | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gb.4xlarge        | 33.33 Gigabit                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8gb.8xlarge        | 66.66 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| m8gb.12xlarge       | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| m8gb.16xlarge       | 133.33 Gigabit                    | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| m8gb.24xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| m8gb.48xlarge       | 400 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| **M8gd**            |
| m8gd.medium 1       | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m8gd.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m8gd.xlarge 1       | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gd.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gd.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8gd.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8gd.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| m8gd.16xlarge       | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8gd.24xlarge       | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8gd.48xlarge       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8gd.metal-24xl     | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| m8gd.metal-48xl     | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **M8gn**            |
| m8gn.medium 1       | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| m8gn.large 1        | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| m8gn.xlarge 1       | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gn.2xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m8gn.4xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m8gn.8xlarge        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| m8gn.12xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| m8gn.16xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| m8gn.24xlarge       | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| m8gn.48xlarge       | 600 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| **M8i**             |
| m8i.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| m8i.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8i.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8i.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| m8i.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| m8i.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| m8i.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| m8i.24xlarge        | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8i.32xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8i.48xlarge        | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8i.96xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8i.metal-48xl      | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8i.metal-96xl      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **M8id**            |
| m8id.large 1        | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| m8id.xlarge 1       | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8id.2xlarge 1      | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8id.4xlarge 1      | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| m8id.8xlarge        | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| m8id.12xlarge       | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| m8id.16xlarge       | 30 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| m8id.24xlarge       | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| m8id.32xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8id.48xlarge       | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8id.96xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8id.metal-48xl     | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| m8id.metal-96xl     | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **M8i-flex**        |
| m8i-flex.large 1    | 0.468 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| m8i-flex.xlarge 1   | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8i-flex.2xlarge 1  | 1.875 / 15.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| m8i-flex.4xlarge 1  | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| m8i-flex.8xlarge 1  | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| m8i-flex.12xlarge 1 | 11.25 / 22.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| m8i-flex.16xlarge 1 | 15.0 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| **Mac1**            |
| mac1.metal          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac2**            |
| mac2.metal          | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac2-m1ultra**    |
| mac2-m1ultra.metal  | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac2-m2**         |
| mac2-m2.metal       | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac2-m2pro**      |
| mac2-m2pro.metal    | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac-m4**          |
| mac-m4.metal        | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Mac-m4pro**       |
| mac-m4pro.metal     | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **T2**              |
| t2.nano             | Low to Moderate                   | ✗ No  | ✗ No  | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t2.micro            | Low to Moderate                   | ✗ No  | ✗ No  | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t2.small            | Low to Moderate                   | ✗ No  | ✗ No  | ✗ No        | 1             | 3                       | 4                          | ✓ Yes |
| t2.medium           | Low to Moderate                   | ✗ No  | ✗ No  | ✗ No        | 1             | 3                       | 6                          | ✓ Yes |
| t2.large            | Low to Moderate                   | ✗ No  | ✗ No  | ✗ No        | 1             | 3                       | 12                         | ✓ Yes |
| t2.xlarge           | Moderate                          | ✗ No  | ✗ No  | ✗ No        | 1             | 3                       | 15                         | ✓ Yes |
| t2.2xlarge          | Moderate                          | ✗ No  | ✗ No  | ✗ No        | 1             | 3                       | 15                         | ✓ Yes |
| **T3**              |
| t3.nano 1           | 0.032 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t3.micro 1          | 0.064 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t3.small 1          | 0.128 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 4                          | ✓ Yes |
| t3.medium 1         | 0.256 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 6                          | ✓ Yes |
| t3.large 1          | 0.512 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 12                         | ✓ Yes |
| t3.xlarge 1         | 1.024 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| t3.2xlarge 1        | 2.048 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| **T3a**             |
| t3a.nano 1          | 0.032 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t3a.micro 1         | 0.064 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t3a.small 1         | 0.128 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| t3a.medium 1        | 0.256 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 6                          | ✓ Yes |
| t3a.large 1         | 0.512 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 12                         | ✓ Yes |
| t3a.xlarge 1        | 1.024 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| t3a.2xlarge 1       | 2.048 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| **T4g**             |
| t4g.nano 1          | 0.032 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t4g.micro 1         | 0.064 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 2                          | ✓ Yes |
| t4g.small 1         | 0.128 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 4                          | ✓ Yes |
| t4g.medium 1        | 0.256 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 6                          | ✓ Yes |
| t4g.large 1         | 0.512 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 12                         | ✓ Yes |
| t4g.xlarge 1        | 1.024 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| t4g.2xlarge 1       | 2.048 / 5.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |

###### Note

1 These instances have a baseline bandwidth and can
use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best effort basis.
Other instances types can sustain their maximum performance indefinitely. For more information,
see [instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md").

For `m6in.32xlarge`, `m6in.metal`, `m6idn.32xlarge`, `m6idn.metal`, you must attach at least 2 ENIs, to separate network
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 170 Gbps.

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

M8a, M8g, M8gd, M8i, M8id, M8i-flex instance types support configurable bandwidth weightings.
With these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
instance types. For the supported configurable weightings, see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").

| Instance type       | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                               |
| ------------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **M5**              |
| m5.large 1          | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.xlarge 1         | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.2xlarge 1        | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.4xlarge          | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.8xlarge          | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.12xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.16xlarge         | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.24xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5a**             |
| m5a.large 1         | 650.00 / 2880.00                    | 81.25 / 360.00                                    | 3600.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.xlarge 1        | 1085.00 / 2880.00                   | 135.62 / 360.00                                   | 6000.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.2xlarge 1       | 1580.00 / 2880.00                   | 197.50 / 360.00                                   | 8333.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.4xlarge         | 2880.00                             | 360.00                                            | 16000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.8xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.12xlarge        | 6780.00                             | 847.50                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.16xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5a.24xlarge        | 13750.00                            | 1718.75                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5ad**            |
| m5ad.large 1        | 650.00 / 2880.00                    | 81.25 / 360.00                                    | 3600.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.xlarge 1       | 1085.00 / 2880.00                   | 135.62 / 360.00                                   | 6000.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.2xlarge 1      | 1580.00 / 2880.00                   | 197.50 / 360.00                                   | 8333.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.4xlarge        | 2880.00                             | 360.00                                            | 16000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.8xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.12xlarge       | 6780.00                             | 847.50                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.16xlarge       | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5ad.24xlarge       | 13750.00                            | 1718.75                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5d**             |
| m5d.large 1         | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.xlarge 1        | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.2xlarge 1       | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.4xlarge         | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.8xlarge         | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.12xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.16xlarge        | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.24xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5d.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5dn**            |
| m5dn.large 1        | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.xlarge 1       | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.2xlarge 1      | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.4xlarge        | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.8xlarge        | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.12xlarge       | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.16xlarge       | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.24xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5dn.metal          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5n**             |
| m5n.large 1         | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.xlarge 1        | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.2xlarge 1       | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.4xlarge         | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.8xlarge         | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.12xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.16xlarge        | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.24xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5n.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M5zn**            |
| m5zn.large 1        | 800.00 / 3170.00                    | 100.00 / 396.25                                   | 3333.00 / 13333.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.xlarge 1       | 1564.00 / 3170.00                   | 195.50 / 396.25                                   | 6667.00 / 13333.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.2xlarge        | 3170.00                             | 396.25                                            | 13333.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.3xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.6xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.12xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m5zn.metal          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6a**             |
| m6a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6a.metal           | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6g**             |
| m6g.medium 1        | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.large 1         | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.xlarge 1        | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.2xlarge 1       | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.8xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.12xlarge        | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.16xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6g.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6gd**            |
| m6gd.medium 1       | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.large 1        | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.xlarge 1       | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.2xlarge 1      | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.4xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.8xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.12xlarge       | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.16xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6gd.metal          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6i**             |
| m6i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6i.metal           | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6id**            |
| m6id.large 1        | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.32xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6id.metal          | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6idn**           |
| m6idn.large 1       | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 6250.00 / 100000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.xlarge 1      | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 12500.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.2xlarge 1     | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 25000.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.4xlarge 1     | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 50000.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.8xlarge       | 25000.00                            | 3125.00                                           | 100000.00                            | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.12xlarge      | 37500.00                            | 4687.50                                           | 150000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.16xlarge      | 50000.00                            | 6250.00                                           | 200000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.24xlarge      | 75000.00                            | 9375.00                                           | 300000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.32xlarge      | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6idn.metal         | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M6in**            |
| m6in.large 1        | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 6250.00 / 100000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.xlarge 1       | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 12500.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.2xlarge 1      | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 25000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.4xlarge 1      | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 50000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.8xlarge        | 25000.00                            | 3125.00                                           | 100000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.12xlarge       | 37500.00                            | 4687.50                                           | 150000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.16xlarge       | 50000.00                            | 6250.00                                           | 200000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.24xlarge       | 75000.00                            | 9375.00                                           | 300000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.32xlarge       | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m6in.metal          | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M7a**             |
| m7a.medium 1        | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7a.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m7a.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M7g**             |
| m7g.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7g.metal           | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M7gd**            |
| m7gd.medium 1       | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.large 1        | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| m7gd.metal          | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **M7i**             |
| m7i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m7i.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M7i-flex**        |
| m7i-flex.large 1    | 312.00 / 10000.00                   | 39.06 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.xlarge 1   | 625.00 / 10000.00                   | 78.12 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.2xlarge 1  | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.4xlarge 1  | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.8xlarge 1  | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.12xlarge 1 | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m7i-flex.16xlarge 1 | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 40000.00 / 80000.00                  | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8a**             |
| m8a.medium 1        | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8a.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8a.metal-48xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8azn**           |
| m8azn.medium 1      | 625.00 / 15000.00                   | 78.12 / 1875.00                                   | 2500.00 / 60000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.large 1       | 1250.00 / 15000.00                  | 156.25 / 1875.00                                  | 5000.00 / 60000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.xlarge 1      | 2500.00 / 15000.00                  | 312.50 / 1875.00                                  | 10000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.3xlarge 1     | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.6xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.12xlarge      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.24xlarge      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8azn.metal-12xl    | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8azn.metal-24xl    | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8g**             |
| m8g.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8g.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8g.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8gb**            |
| m8gb.medium 1       | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 7500.00 / 120000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.large 1        | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 15000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.xlarge 1       | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 30000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.2xlarge 1      | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 60000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.4xlarge        | 25000.00                            | 3125.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.8xlarge        | 50000.00                            | 6250.00                                           | 240000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.12xlarge       | 75000.00                            | 9375.00                                           | 360000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.16xlarge       | 100000.00                           | 12500.00                                          | 480000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.24xlarge       | 150000.00                           | 18750.00                                          | 720000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gb.48xlarge       | 300000.00                           | 37500.00                                          | 1440000.00                           | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **M8gd**            |
| m8gd.medium 1       | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.large 1        | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.48xlarge       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8gd.metal-24xl     | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gd.metal-48xl     | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8gn**            |
| m8gn.medium 1       | 760.00 / 10000.00                   | 95.00 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.large 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.2xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.4xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.8xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.12xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.16xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.24xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8gn.48xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8i**             |
| m8i.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8i.96xlarge        | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8i.metal-48xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i.metal-96xl      | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8id**            |
| m8id.large 1        | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.xlarge 1       | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.2xlarge 1      | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.4xlarge 1      | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.8xlarge        | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.12xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.32xlarge       | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.48xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8id.96xlarge       | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| m8id.metal-48xl     | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8id.metal-96xl     | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **M8i-flex**        |
| m8i-flex.large 1    | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.xlarge 1   | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.2xlarge 1  | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.4xlarge 1  | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.8xlarge 1  | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.12xlarge 1 | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| m8i-flex.16xlarge 1 | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 40000.00 / 80000.00                  | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Mac1**            |
| mac1.metal          | 14000.00                            | 1750.00                                           | 80000.00                             | ✓ Yes | Up to 16 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac2**            |
| mac2.metal          | 10000.00                            | 1250.00                                           | 55000.00                             | ✓ Yes | Up to 10 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac2-m1ultra**    |
| mac2-m1ultra.metal  | 10000.00                            | 1250.00                                           | 55000.00                             | ✓ Yes | Up to 10 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac2-m2**         |
| mac2-m2.metal       | 8000.00                             | 1000.00                                           | 55000.00                             | ✓ Yes | Up to 10 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac2-m2pro**      |
| mac2-m2pro.metal    | 8000.00                             | 1000.00                                           | 55000.00                             | ✓ Yes | Up to 10 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac-m4**          |
| mac-m4.metal        | 8000.00                             | 1000.00                                           | 55000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Mac-m4pro**       |
| mac-m4pro.metal     | 8000.00                             | 1000.00                                           | 55000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **T2**              |
| **T3**              |
| t3.nano 1           | 43.00 / 2085.00                     | 5.38 / 260.62                                     | 250.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.micro 1          | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.small 1          | 174.00 / 2085.00                    | 21.75 / 260.62                                    | 1000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.medium 1         | 347.00 / 2085.00                    | 43.38 / 260.62                                    | 2000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.large 1          | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.xlarge 1         | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3.2xlarge 1        | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **T3a**             |
| t3a.nano 1          | 45.00 / 2085.00                     | 5.62 / 260.62                                     | 250.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.micro 1         | 90.00 / 2085.00                     | 11.25 / 260.62                                    | 500.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.small 1         | 175.00 / 2085.00                    | 21.88 / 260.62                                    | 1000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.medium 1        | 350.00 / 2085.00                    | 43.75 / 260.62                                    | 2000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.large 1         | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.xlarge 1        | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t3a.2xlarge 1       | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **T4g**             |
| t4g.nano 1          | 43.00 / 2085.00                     | 5.38 / 260.62                                     | 250.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.micro 1         | 87.00 / 2085.00                     | 10.88 / 260.62                                    | 500.00 / 11800.00                    | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.small 1         | 174.00 / 2085.00                    | 21.75 / 260.62                                    | 1000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.medium 1        | 347.00 / 2085.00                    | 43.38 / 260.62                                    | 2000.00 / 11800.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.large 1         | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.xlarge 1        | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| t4g.2xlarge 1       | 695.00 / 2780.00                    | 86.88 / 347.50                                    | 4000.00 / 15700.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |

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
| **M5ad**        |
| m5ad.large      | 1 x 75 GB              | NVMe SSD            | 30,000 / 15,000                    |                        | ✓ Yes          |
| m5ad.xlarge     | 1 x 150 GB             | NVMe SSD            | 59,000 / 29,000                    |                        | ✓ Yes          |
| m5ad.2xlarge    | 1 x 300 GB             | NVMe SSD            | 117,000 / 57,000                   |                        | ✓ Yes          |
| m5ad.4xlarge    | 2 x 300 GB             | NVMe SSD            | 234,000 / 114,000                  |                        | ✓ Yes          |
| m5ad.8xlarge    | 2 x 600 GB             | NVMe SSD            | 466,666 / 233,334                  |                        | ✓ Yes          |
| m5ad.12xlarge   | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| m5ad.16xlarge   | 4 x 600 GB             | NVMe SSD            | 933,332 / 466,668                  |                        | ✓ Yes          |
| m5ad.24xlarge   | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| **M5d**         |
| m5d.large       | 1 x 75 GB              | NVMe SSD            | 30,000 / 15,000                    |                        | ✓ Yes          |
| m5d.xlarge      | 1 x 150 GB             | NVMe SSD            | 59,000 / 29,000                    |                        | ✓ Yes          |
| m5d.2xlarge     | 1 x 300 GB             | NVMe SSD            | 117,000 / 57,000                   |                        | ✓ Yes          |
| m5d.4xlarge     | 2 x 300 GB             | NVMe SSD            | 234,000 / 114,000                  |                        | ✓ Yes          |
| m5d.8xlarge     | 2 x 600 GB             | NVMe SSD            | 466,666 / 233,334                  |                        | ✓ Yes          |
| m5d.12xlarge    | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| m5d.16xlarge    | 4 x 600 GB             | NVMe SSD            | 933,332 / 466,668                  |                        | ✓ Yes          |
| m5d.24xlarge    | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| m5d.metal       | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| **M5dn**        |
| m5dn.large      | 1 x 75 GB              | NVMe SSD            | 29,000 / 14,500                    |                        | ✓ Yes          |
| m5dn.xlarge     | 1 x 150 GB             | NVMe SSD            | 58,000 / 29,000                    |                        | ✓ Yes          |
| m5dn.2xlarge    | 1 x 300 GB             | NVMe SSD            | 116,000 / 58,000                   |                        | ✓ Yes          |
| m5dn.4xlarge    | 2 x 300 GB             | NVMe SSD            | 232,000 / 116,000                  |                        | ✓ Yes          |
| m5dn.8xlarge    | 2 x 600 GB             | NVMe SSD            | 464,000 / 232,000                  |                        | ✓ Yes          |
| m5dn.12xlarge   | 2 x 900 GB             | NVMe SSD            | 700,000 / 350,000                  |                        | ✓ Yes          |
| m5dn.16xlarge   | 4 x 600 GB             | NVMe SSD            | 930,000 / 465,000                  |                        | ✓ Yes          |
| m5dn.24xlarge   | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 700,000                |                        | ✓ Yes          |
| m5dn.metal      | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 700,000                |                        | ✓ Yes          |
| **M6gd**        |
| m6gd.medium     | 1 x 59 GB              | NVMe SSD            | 13,438 / 5,625                     |                        | ✓ Yes          |
| m6gd.large      | 1 x 118 GB             | NVMe SSD            | 26,875 / 11,250                    |                        | ✓ Yes          |
| m6gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 53,750 / 22,500                    |                        | ✓ Yes          |
| m6gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| m6gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 215,000 / 90,000                   |                        | ✓ Yes          |
| m6gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| m6gd.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| m6gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| m6gd.metal      | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **M6id**        |
| m6id.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| m6id.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| m6id.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| m6id.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| m6id.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| m6id.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| m6id.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| m6id.24xlarge   | 4 x 1425 GB            | NVMe SSD            | 1,609,996 / 805,000                |                        | ✓ Yes          |
| m6id.32xlarge   | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| m6id.metal      | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **M6idn**       |
| m6idn.large     | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| m6idn.xlarge    | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| m6idn.2xlarge   | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| m6idn.4xlarge   | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| m6idn.8xlarge   | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| m6idn.12xlarge  | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| m6idn.16xlarge  | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| m6idn.24xlarge  | 4 x 1425 GB            | NVMe SSD            | 1,609,996 / 805,000                |                        | ✓ Yes          |
| m6idn.32xlarge  | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| m6idn.metal     | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **M7gd**        |
| m7gd.medium     | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| m7gd.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| m7gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| m7gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| m7gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| m7gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| m7gd.12xlarge   | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| m7gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| m7gd.metal      | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| **M8gd**        |
| m8gd.medium     | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| m8gd.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| m8gd.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| m8gd.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| m8gd.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| m8gd.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| m8gd.12xlarge   | 3 x 950 GB             | NVMe SSD            | 804,999 / 402,501                  |                        | ✓ Yes          |
| m8gd.16xlarge   | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| m8gd.24xlarge   | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| m8gd.48xlarge   | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| m8gd.metal-24xl | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| m8gd.metal-48xl | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| **M8id**        |
| m8id.large      | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| m8id.xlarge     | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| m8id.2xlarge    | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| m8id.4xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| m8id.8xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| m8id.12xlarge   | 1 x 2850 GB            | NVMe SSD            | 804,999 / 402,501                  |                        | ✓ Yes          |
| m8id.16xlarge   | 1 x 3800 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| m8id.24xlarge   | 2 x 2850 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| m8id.32xlarge   | 2 x 3800 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| m8id.48xlarge   | 3 x 3800 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| m8id.96xlarge   | 6 x 3800 GB            | NVMe SSD            | 6,439,992 / 3,220,008              |                        | ✓ Yes          |
| m8id.metal-48xl | 3 x 3800 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| m8id.metal-96xl | 6 x 3800 GB            | NVMe SSD            | 6,439,992 / 3,220,008              |                        | ✓ Yes          |
| **Mac-m4**      |
| mac-m4.metal    | 1 x 1900 GB            | NVMe SSD            | 550,000 / 275,000                  |                        | ✓ Yes          |
| **Mac-m4pro**   |
| mac-m4pro.metal | 1 x 1900 GB            | NVMe SSD            | 550,000 / 275,000                  |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type      | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| ------------------ | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **M5**             |
| m5.large           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m5.xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.2xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.4xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.8xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.12xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.16xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.24xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5.metal           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M5a**            |
| m5a.large          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m5a.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.4xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.8xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.12xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.16xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5a.24xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| **M5ad**           |
| m5ad.large         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m5ad.xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.2xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.4xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.8xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.12xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.16xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5ad.24xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| **M5d**            |
| m5d.large          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m5d.xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.2xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.4xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.8xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.12xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.16xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.24xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5d.metal          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M5dn**           |
| m5dn.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m5dn.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5dn.metal         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M5n**            |
| m5n.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m5n.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5n.metal          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M5zn**           |
| m5zn.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m5zn.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5zn.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5zn.3xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5zn.6xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5zn.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m5zn.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M6a**            |
| m6a.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✗ No           |
| m6a.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| m6a.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| m6a.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| m6a.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| m6a.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6a.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6a.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6a.32xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6a.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6a.metal          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M6g**            |
| m6g.medium         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m6g.large          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.4xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.8xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.12xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.16xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6g.metal          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M6gd**           |
| m6gd.medium        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| m6gd.large         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.2xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.4xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.8xlarge       | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.12xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.16xlarge      | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6gd.metal         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M6i**            |
| m6i.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m6i.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.32xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6i.metal          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M6id**           |
| m6id.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m6id.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.32xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6id.metal         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M6idn**          |
| m6idn.large        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m6idn.xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.2xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.4xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.8xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.12xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.16xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.24xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.32xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6idn.metal        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M6in**           |
| m6in.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m6in.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.32xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m6in.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M7a**            |
| m7a.medium         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7a.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7a.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.32xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7a.metal-48xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M7g**            |
| m7g.medium         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7g.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7g.metal          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M7gd**           |
| m7gd.medium        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7gd.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7gd.metal         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M7i**            |
| m7i.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m7i.metal-24xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m7i.metal-48xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M7i-flex**       |
| m7i-flex.large     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.2xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.4xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.8xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.12xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m7i-flex.16xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **M8a**            |
| m8a.medium         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8a.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8a.metal-24xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8a.metal-48xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8azn**          |
| m8azn.medium       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8azn.large        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.3xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.6xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.12xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.24xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8azn.metal-12xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8azn.metal-24xl   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8g**            |
| m8g.medium         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8g.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8g.metal-24xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8g.metal-48xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8gb**           |
| m8gb.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8gb.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gb.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **M8gd**           |
| m8gd.medium        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8gd.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.48xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gd.metal-24xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8gd.metal-48xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8gn**           |
| m8gn.medium        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8gn.large         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.16xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8gn.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **M8i**            |
| m8i.large          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i.xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.2xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.4xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.8xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.12xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.16xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.32xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.48xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.96xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8i.metal-48xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8i.metal-96xl     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8id**           |
| m8id.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8id.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.32xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.48xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.96xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| m8id.metal-48xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| m8id.metal-96xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **M8i-flex**       |
| m8i-flex.large     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.2xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.4xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.8xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.12xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| m8i-flex.16xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **Mac1**           |
| mac1.metal         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **Mac2**           |
| mac2.metal         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **Mac2-m1ultra**   |
| mac2-m1ultra.metal | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **Mac2-m2**        |
| mac2-m2.metal      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **Mac2-m2pro**     |
| mac2-m2pro.metal   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **Mac-m4**         |
| mac-m4.metal       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Mac-m4pro**      |
| mac-m4pro.metal    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **T2**             |
| t2.nano            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.micro           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.small           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.medium          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.large           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| t2.2xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **T3**             |
| t3.nano            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.micro           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.small           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.medium          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.large           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3.2xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| **T3a**            |
| t3a.nano           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.micro          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.small          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.medium         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.large          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t3a.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| **T4g**            |
| t4g.nano           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.micro          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.small          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.medium         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.large          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| t4g.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
