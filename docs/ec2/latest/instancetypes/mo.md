# Specifications for Amazon EC2 memory optimized instances

###### End of sale notice

The **U-9tb1**, **U-12tb1**,
**U-18tb1**, and **U-24tb1** instance
types are no longer available for new instance launches. If your workload requires a high-memory
instance, we recommend that you use a U7i instance type instead.

Memory optimized instances are designed to deliver fast performance for workloads
that process large data sets in memory.

For information on previous generation instance types of this category, such as R4 instances,
see [Specifications for Amazon EC2 previous generation instances](pg.md "pg.md").

###### Contents

- [Instance families and instance types](#mo_sizes "#mo_sizes")
- [Instance family summary](#mo_summary "#mo_summary")
- [Performance specifications](#mo_hardware "#mo_hardware")
- [Network specifications](#mo_network "#mo_network")
- [Amazon EBS specifications](#mo_storage-ebs "#mo_storage-ebs")
- [Instance store specifications](#mo_instance-store "#mo_instance-store")
- [Security specifications](#mo_security "#mo_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | ------------------ | ------------------ | ------------------ | ------------------ | ------------------- | ------------------- | ------------------- | ----------------- | ----------------- | ----------------- | ----------------- | ---------------- |
| R5              | `r5.large`               | `r5.xlarge`        | `r5.2xlarge`       | `r5.4xlarge`       | `r5.8xlarge`       | `r5.12xlarge`       | `r5.16xlarge`       | `r5.24xlarge`       | `r5.metal`        |
| R5a             | `r5a.large`              | `r5a.xlarge`       | `r5a.2xlarge`      | `r5a.4xlarge`      | `r5a.8xlarge`      | `r5a.12xlarge`      | `r5a.16xlarge`      | `r5a.24xlarge`      |
| R5ad            | `r5ad.large`             | `r5ad.xlarge`      | `r5ad.2xlarge`     | `r5ad.4xlarge`     | `r5ad.8xlarge`     | `r5ad.12xlarge`     | `r5ad.16xlarge`     | `r5ad.24xlarge`     |
| R5b             | `r5b.large`              | `r5b.xlarge`       | `r5b.2xlarge`      | `r5b.4xlarge`      | `r5b.8xlarge`      | `r5b.12xlarge`      | `r5b.16xlarge`      | `r5b.24xlarge`      | `r5b.metal`       |
| R5d             | `r5d.large`              | `r5d.xlarge`       | `r5d.2xlarge`      | `r5d.4xlarge`      | `r5d.8xlarge`      | `r5d.12xlarge`      | `r5d.16xlarge`      | `r5d.24xlarge`      | `r5d.metal`       |
| R5dn            | `r5dn.large`             | `r5dn.xlarge`      | `r5dn.2xlarge`     | `r5dn.4xlarge`     | `r5dn.8xlarge`     | `r5dn.12xlarge`     | `r5dn.16xlarge`     | `r5dn.24xlarge`     | `r5dn.metal`      |
| R5n             | `r5n.large`              | `r5n.xlarge`       | `r5n.2xlarge`      | `r5n.4xlarge`      | `r5n.8xlarge`      | `r5n.12xlarge`      | `r5n.16xlarge`      | `r5n.24xlarge`      | `r5n.metal`       |
| R6a             | `r6a.large`              | `r6a.xlarge`       | `r6a.2xlarge`      | `r6a.4xlarge`      | `r6a.8xlarge`      | `r6a.12xlarge`      | `r6a.16xlarge`      | `r6a.24xlarge`      | `r6a.32xlarge`    | `r6a.48xlarge`    | `r6a.metal`       |
| R6g             | `r6g.medium`             | `r6g.large`        | `r6g.xlarge`       | `r6g.2xlarge`      | `r6g.4xlarge`      | `r6g.8xlarge`       | `r6g.12xlarge`      | `r6g.16xlarge`      | `r6g.metal`       |
| R6gd            | `r6gd.medium`            | `r6gd.large`       | `r6gd.xlarge`      | `r6gd.2xlarge`     | `r6gd.4xlarge`     | `r6gd.8xlarge`      | `r6gd.12xlarge`     | `r6gd.16xlarge`     | `r6gd.metal`      |
| R6i             | `r6i.large`              | `r6i.xlarge`       | `r6i.2xlarge`      | `r6i.4xlarge`      | `r6i.8xlarge`      | `r6i.12xlarge`      | `r6i.16xlarge`      | `r6i.24xlarge`      | `r6i.32xlarge`    | `r6i.metal`       |
| R6id            | `r6id.large`             | `r6id.xlarge`      | `r6id.2xlarge`     | `r6id.4xlarge`     | `r6id.8xlarge`     | `r6id.12xlarge`     | `r6id.16xlarge`     | `r6id.24xlarge`     | `r6id.32xlarge`   | `r6id.metal`      |
| R6idn           | `r6idn.large`            | `r6idn.xlarge`     | `r6idn.2xlarge`    | `r6idn.4xlarge`    | `r6idn.8xlarge`    | `r6idn.12xlarge`    | `r6idn.16xlarge`    | `r6idn.24xlarge`    | `r6idn.32xlarge`  | `r6idn.metal`     |
| R6in            | `r6in.large`             | `r6in.xlarge`      | `r6in.2xlarge`     | `r6in.4xlarge`     | `r6in.8xlarge`     | `r6in.12xlarge`     | `r6in.16xlarge`     | `r6in.24xlarge`     | `r6in.32xlarge`   | `r6in.metal`      |
| R7a             | `r7a.medium`             | `r7a.large`        | `r7a.xlarge`       | `r7a.2xlarge`      | `r7a.4xlarge`      | `r7a.8xlarge`       | `r7a.12xlarge`      | `r7a.16xlarge`      | `r7a.24xlarge`    | `r7a.32xlarge`    | `r7a.48xlarge`    | `r7a.metal-48xl`  |
| R7g             | `r7g.medium`             | `r7g.large`        | `r7g.xlarge`       | `r7g.2xlarge`      | `r7g.4xlarge`      | `r7g.8xlarge`       | `r7g.12xlarge`      | `r7g.16xlarge`      | `r7g.metal`       |
| R7gd            | `r7gd.medium`            | `r7gd.large`       | `r7gd.xlarge`      | `r7gd.2xlarge`     | `r7gd.4xlarge`     | `r7gd.8xlarge`      | `r7gd.12xlarge`     | `r7gd.16xlarge`     | `r7gd.metal`      |
| R7i             | `r7i.large`              | `r7i.xlarge`       | `r7i.2xlarge`      | `r7i.4xlarge`      | `r7i.8xlarge`      | `r7i.12xlarge`      | `r7i.16xlarge`      | `r7i.24xlarge`      | `r7i.48xlarge`    | `r7i.metal-24xl`  | `r7i.metal-48xl`  |
| R7iz            | `r7iz.large`             | `r7iz.xlarge`      | `r7iz.2xlarge`     | `r7iz.4xlarge`     | `r7iz.8xlarge`     | `r7iz.12xlarge`     | `r7iz.16xlarge`     | `r7iz.32xlarge`     | `r7iz.metal-16xl` | `r7iz.metal-32xl` |
| R8a             | `r8a.medium`             | `r8a.large`        | `r8a.xlarge`       | `r8a.2xlarge`      | `r8a.4xlarge`      | `r8a.8xlarge`       | `r8a.12xlarge`      | `r8a.16xlarge`      | `r8a.24xlarge`    | `r8a.48xlarge`    | `r8a.metal-24xl`  | `r8a.metal-48xl`  |
| R8g             | `r8g.medium`             | `r8g.large`        | `r8g.xlarge`       | `r8g.2xlarge`      | `r8g.4xlarge`      | `r8g.8xlarge`       | `r8g.12xlarge`      | `r8g.16xlarge`      | `r8g.24xlarge`    | `r8g.48xlarge`    | `r8g.metal-24xl`  | `r8g.metal-48xl`  |
| R8gb            | `r8gb.medium`            | `r8gb.large`       | `r8gb.xlarge`      | `r8gb.2xlarge`     | `r8gb.4xlarge`     | `r8gb.8xlarge`      | `r8gb.12xlarge`     | `r8gb.16xlarge`     | `r8gb.24xlarge`   | `r8gb.metal-24xl` |
| R8gd            | `r8gd.medium`            | `r8gd.large`       | `r8gd.xlarge`      | `r8gd.2xlarge`     | `r8gd.4xlarge`     | `r8gd.8xlarge`      | `r8gd.12xlarge`     | `r8gd.16xlarge`     | `r8gd.24xlarge`   | `r8gd.48xlarge`   | `r8gd.metal-24xl` | `r8gd.metal-48xl` |
| R8gn            | `r8gn.medium`            | `r8gn.large`       | `r8gn.xlarge`      | `r8gn.2xlarge`     | `r8gn.4xlarge`     | `r8gn.8xlarge`      | `r8gn.12xlarge`     | `r8gn.16xlarge`     | `r8gn.24xlarge`   | `r8gn.48xlarge`   | `r8gn.metal-24xl` | `r8gn.metal-48xl` |
| R8i             | `r8i.large`              | `r8i.xlarge`       | `r8i.2xlarge`      | `r8i.4xlarge`      | `r8i.8xlarge`      | `r8i.12xlarge`      | `r8i.16xlarge`      | `r8i.24xlarge`      | `r8i.32xlarge`    | `r8i.48xlarge`    | `r8i.96xlarge`    | `r8i.metal-48xl`  | `r8i.metal-96xl` |
| R8i-flex        | `r8i-flex.large`         | `r8i-flex.xlarge`  | `r8i-flex.2xlarge` | `r8i-flex.4xlarge` | `r8i-flex.8xlarge` | `r8i-flex.12xlarge` | `r8i-flex.16xlarge` |
| U-3tb1          | `u-3tb1.56xlarge`        |
| U-6tb1          | `u-6tb1.56xlarge`        | `u-6tb1.112xlarge` | `u-6tb1.metal`     |
| U-9tb1          | `u-9tb1.112xlarge`       | `u-9tb1.metal`     |
| U-12tb1         | `u-12tb1.112xlarge`      | `u-12tb1.metal`    |
| U-18tb1         | `u-18tb1.112xlarge`      | `u-18tb1.metal`    |
| U-24tb1         | `u-24tb1.112xlarge`      | `u-24tb1.metal`    |
| U7i-6tb         | `u7i-6tb.112xlarge`      |
| U7i-8tb         | `u7i-8tb.112xlarge`      |
| U7i-12tb        | `u7i-12tb.224xlarge`     |
| U7in-16tb       | `u7in-16tb.224xlarge`    |
| U7in-24tb       | `u7in-24tb.224xlarge`    |
| U7in-32tb       | `u7in-32tb.224xlarge`    |
| U7inh-32tb      | `u7inh-32tb.480xlarge`   |
| X1              | `x1.16xlarge`            | `x1.32xlarge`      |
| X1e             | `x1e.xlarge`             | `x1e.2xlarge`      | `x1e.4xlarge`      | `x1e.8xlarge`      | `x1e.16xlarge`     | `x1e.32xlarge`      |
| X2gd            | `x2gd.medium`            | `x2gd.large`       | `x2gd.xlarge`      | `x2gd.2xlarge`     | `x2gd.4xlarge`     | `x2gd.8xlarge`      | `x2gd.12xlarge`     | `x2gd.16xlarge`     | `x2gd.metal`      |
| X2idn           | `x2idn.16xlarge`         | `x2idn.24xlarge`   | `x2idn.32xlarge`   | `x2idn.metal`      |
| X2iedn          | `x2iedn.xlarge`          | `x2iedn.2xlarge`   | `x2iedn.4xlarge`   | `x2iedn.8xlarge`   | `x2iedn.16xlarge`  | `x2iedn.24xlarge`   | `x2iedn.32xlarge`   | `x2iedn.metal`      |
| X2iezn          | `x2iezn.2xlarge`         | `x2iezn.4xlarge`   | `x2iezn.6xlarge`   | `x2iezn.8xlarge`   | `x2iezn.12xlarge`  | `x2iezn.metal`      |
| X8g             | `x8g.medium`             | `x8g.large`        | `x8g.xlarge`       | `x8g.2xlarge`      | `x8g.4xlarge`      | `x8g.8xlarge`       | `x8g.12xlarge`      | `x8g.16xlarge`      | `x8g.24xlarge`    | `x8g.48xlarge`    | `x8g.metal-24xl`  | `x8g.metal-48xl`  |
| X8aedz          | `x8aedz.large`           | `x8aedz.xlarge`    | `x8aedz.3xlarge`   | `x8aedz.6xlarge`   | `x8aedz.12xlarge`  | `x8aedz.24xlarge`   | `x8aedz.metal-12xl` | `x8aedz.metal-24xl` |
| z1d             | `z1d.large`              | `z1d.xlarge`       | `z1d.2xlarge`      | `z1d.3xlarge`      | `z1d.6xlarge`      | `z1d.12xlarge`      | `z1d.metal`         |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| R5              | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R5a             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R5ad            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R5b             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R5d             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R5dn            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R5n             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R6a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R6g             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R6gd            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R6i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R6id            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R6idn           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R6in            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R7a             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R7g             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R7gd            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R7i             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R7iz            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R8a             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R8g             | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R8gb            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R8gd            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R8gn            | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| R8i             | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R8i-flex        | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| U-3tb1          | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Windows                     | Linux |
| U-6tb1          | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U-9tb1          | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U-12tb1         | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U-18tb1         | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U-24tb1         | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7i-6tb         | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7i-8tb         | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7i-12tb        | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7in-16tb       | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7in-24tb       | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7in-32tb       | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Windows                     | Linux |
| U7inh-32tb      | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✗ No         | ✗ No                | Linux                       |
| X1              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| X1e             | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| X2gd            | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Linux                       |
| X2idn           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| X2iedn          | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| X2iezn          | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| X8g             | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| X8aedz          | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| z1d             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |

## Performance specifications

| Instance type        | Memory (GiB) | Processor                  | vCPUs | CPU cores | Threads per core | Accelerators | Accelerator memory |
| -------------------- | ------------ | -------------------------- | ----- | --------- | ---------------- | ------------ | ------------------ |
| **R5**               |
| r5.large             | 16.00        | Intel Xeon Platinum 8175   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5.xlarge            | 32.00        | Intel Xeon Platinum 8175   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5.2xlarge           | 64.00        | Intel Xeon Platinum 8175   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5.4xlarge           | 128.00       | Intel Xeon Platinum 8175   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5.8xlarge           | 256.00       | Intel Xeon Platinum 8175   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5.12xlarge          | 384.00       | Intel Xeon Platinum 8175   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5.16xlarge          | 512.00       | Intel Xeon Platinum 8175   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5.24xlarge          | 768.00       | Intel Xeon Platinum 8175   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r5.metal             | 768.00       | Intel Xeon Platinum 8175   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5a**              |
| r5a.large            | 16.00        | AMD EPYC 7571              | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5a.xlarge           | 32.00        | AMD EPYC 7571              | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5a.2xlarge          | 64.00        | AMD EPYC 7571              | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5a.4xlarge          | 128.00       | AMD EPYC 7571              | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5a.8xlarge          | 256.00       | AMD EPYC 7571              | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5a.12xlarge         | 384.00       | AMD EPYC 7571              | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5a.16xlarge         | 512.00       | AMD EPYC 7571              | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5a.24xlarge         | 768.00       | AMD EPYC 7571              | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5ad**             |
| r5ad.large           | 16.00        | AMD EPYC 7571              | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5ad.xlarge          | 32.00        | AMD EPYC 7571              | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5ad.2xlarge         | 64.00        | AMD EPYC 7571              | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5ad.4xlarge         | 128.00       | AMD EPYC 7571              | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5ad.8xlarge         | 256.00       | AMD EPYC 7571              | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5ad.12xlarge        | 384.00       | AMD EPYC 7571              | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5ad.16xlarge        | 512.00       | AMD EPYC 7571              | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5ad.24xlarge        | 768.00       | AMD EPYC 7571              | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5b**              |
| r5b.large            | 16.00        | Intel Xeon Platinum 8259   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5b.xlarge           | 32.00        | Intel Xeon Platinum 8259   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5b.2xlarge          | 64.00        | Intel Xeon Platinum 8259   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5b.4xlarge          | 128.00       | Intel Xeon Platinum 8259   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5b.8xlarge          | 256.00       | Intel Xeon Platinum 8259   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5b.12xlarge         | 384.00       | Intel Xeon Platinum 8259   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5b.16xlarge         | 512.00       | Intel Xeon Platinum 8259   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5b.24xlarge         | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r5b.metal            | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5d**              |
| r5d.large            | 16.00        | Intel Xeon Platinum 8175   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5d.xlarge           | 32.00        | Intel Xeon Platinum 8175   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5d.2xlarge          | 64.00        | Intel Xeon Platinum 8175   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5d.4xlarge          | 128.00       | Intel Xeon Platinum 8175   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5d.8xlarge          | 256.00       | Intel Xeon Platinum 8175   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5d.12xlarge         | 384.00       | Intel Xeon Platinum 8175   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5d.16xlarge         | 512.00       | Intel Xeon Platinum 8175   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5d.24xlarge         | 768.00       | Intel Xeon Platinum 8175   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r5d.metal            | 768.00       | Intel Xeon Platinum 8175   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5dn**             |
| r5dn.large           | 16.00        | Intel Xeon Platinum 8259   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5dn.xlarge          | 32.00        | Intel Xeon Platinum 8259   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5dn.2xlarge         | 64.00        | Intel Xeon Platinum 8259   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5dn.4xlarge         | 128.00       | Intel Xeon Platinum 8259   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5dn.8xlarge         | 256.00       | Intel Xeon Platinum 8259   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5dn.12xlarge        | 384.00       | Intel Xeon Platinum 8259   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5dn.16xlarge        | 512.00       | Intel Xeon Platinum 8259   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5dn.24xlarge        | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r5dn.metal           | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R5n**              |
| r5n.large            | 16.00        | Intel Xeon Platinum 8259   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r5n.xlarge           | 32.00        | Intel Xeon Platinum 8259   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r5n.2xlarge          | 64.00        | Intel Xeon Platinum 8259   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r5n.4xlarge          | 128.00       | Intel Xeon Platinum 8259   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r5n.8xlarge          | 256.00       | Intel Xeon Platinum 8259   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r5n.12xlarge         | 384.00       | Intel Xeon Platinum 8259   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r5n.16xlarge         | 512.00       | Intel Xeon Platinum 8259   | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r5n.24xlarge         | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r5n.metal            | 768.00       | Intel Xeon Platinum 8259   | 96    | 48        | 2                | ✗ No         | ✗ No               |
| **R6a**              |
| r6a.large            | 16.00        | AMD EPYC 7R13              | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r6a.xlarge           | 32.00        | AMD EPYC 7R13              | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r6a.2xlarge          | 64.00        | AMD EPYC 7R13              | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r6a.4xlarge          | 128.00       | AMD EPYC 7R13              | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r6a.8xlarge          | 256.00       | AMD EPYC 7R13              | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r6a.12xlarge         | 384.00       | AMD EPYC 7R13              | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r6a.16xlarge         | 512.00       | AMD EPYC 7R13              | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r6a.24xlarge         | 768.00       | AMD EPYC 7R13              | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r6a.32xlarge         | 1024.00      | AMD EPYC 7R13              | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r6a.48xlarge         | 1536.00      | AMD EPYC 7R13              | 192   | 96        | 2                | ✗ No         | ✗ No               |
| r6a.metal            | 1536.00      | AMD EPYC 7R13              | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **R6g**              |
| r6g.medium           | 8.00         | AWS Graviton2 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r6g.large            | 16.00        | AWS Graviton2 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r6g.xlarge           | 32.00        | AWS Graviton2 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r6g.2xlarge          | 64.00        | AWS Graviton2 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r6g.4xlarge          | 128.00       | AWS Graviton2 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r6g.8xlarge          | 256.00       | AWS Graviton2 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r6g.12xlarge         | 384.00       | AWS Graviton2 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r6g.16xlarge         | 512.00       | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r6g.metal            | 512.00       | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **R6gd**             |
| r6gd.medium          | 8.00         | AWS Graviton2 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r6gd.large           | 16.00        | AWS Graviton2 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r6gd.xlarge          | 32.00        | AWS Graviton2 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r6gd.2xlarge         | 64.00        | AWS Graviton2 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r6gd.4xlarge         | 128.00       | AWS Graviton2 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r6gd.8xlarge         | 256.00       | AWS Graviton2 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r6gd.12xlarge        | 384.00       | AWS Graviton2 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r6gd.16xlarge        | 512.00       | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r6gd.metal           | 512.00       | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **R6i**              |
| r6i.large            | 16.00        | Intel Xeon Ice Lake        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r6i.xlarge           | 32.00        | Intel Xeon Ice Lake        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r6i.2xlarge          | 64.00        | Intel Xeon Ice Lake        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r6i.4xlarge          | 128.00       | Intel Xeon Ice Lake        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r6i.8xlarge          | 256.00       | Intel Xeon Ice Lake        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r6i.12xlarge         | 384.00       | Intel Xeon Ice Lake        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r6i.16xlarge         | 512.00       | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r6i.24xlarge         | 768.00       | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r6i.32xlarge         | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r6i.metal            | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **R6id**             |
| r6id.large           | 16.00        | Intel Xeon Ice Lake        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r6id.xlarge          | 32.00        | Intel Xeon Ice Lake        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r6id.2xlarge         | 64.00        | Intel Xeon Ice Lake        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r6id.4xlarge         | 128.00       | Intel Xeon Ice Lake        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r6id.8xlarge         | 256.00       | Intel Xeon Ice Lake        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r6id.12xlarge        | 384.00       | Intel Xeon Ice Lake        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r6id.16xlarge        | 512.00       | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r6id.24xlarge        | 768.00       | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r6id.32xlarge        | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r6id.metal           | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **R6idn**            |
| r6idn.large          | 16.00        | Intel Xeon Ice Lake        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r6idn.xlarge         | 32.00        | Intel Xeon Ice Lake        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r6idn.2xlarge        | 64.00        | Intel Xeon Ice Lake        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r6idn.4xlarge        | 128.00       | Intel Xeon Ice Lake        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r6idn.8xlarge        | 256.00       | Intel Xeon Ice Lake        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r6idn.12xlarge       | 384.00       | Intel Xeon Ice Lake        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r6idn.16xlarge       | 512.00       | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r6idn.24xlarge       | 768.00       | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r6idn.32xlarge       | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r6idn.metal          | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **R6in**             |
| r6in.large           | 16.00        | Intel Xeon Ice Lake        | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r6in.xlarge          | 32.00        | Intel Xeon Ice Lake        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r6in.2xlarge         | 64.00        | Intel Xeon Ice Lake        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r6in.4xlarge         | 128.00       | Intel Xeon Ice Lake        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r6in.8xlarge         | 256.00       | Intel Xeon Ice Lake        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r6in.12xlarge        | 384.00       | Intel Xeon Ice Lake        | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r6in.16xlarge        | 512.00       | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r6in.24xlarge        | 768.00       | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r6in.32xlarge        | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r6in.metal           | 1024.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **R7a**              |
| r7a.medium           | 8.00         | AMD EPYC 9R14              | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r7a.large            | 16.00        | AMD EPYC 9R14              | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r7a.xlarge           | 32.00        | AMD EPYC 9R14              | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r7a.2xlarge          | 64.00        | AMD EPYC 9R14              | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r7a.4xlarge          | 128.00       | AMD EPYC 9R14              | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r7a.8xlarge          | 256.00       | AMD EPYC 9R14              | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r7a.12xlarge         | 384.00       | AMD EPYC 9R14              | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r7a.16xlarge         | 512.00       | AMD EPYC 9R14              | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r7a.24xlarge         | 768.00       | AMD EPYC 9R14              | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r7a.32xlarge         | 1024.00      | AMD EPYC 9R14              | 128   | 128       | 1                | ✗ No         | ✗ No               |
| r7a.48xlarge         | 1536.00      | AMD EPYC 9R14              | 192   | 192       | 1                | ✗ No         | ✗ No               |
| r7a.metal-48xl       | 1536.00      | AMD EPYC 9R14              | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **R7g**              |
| r7g.medium           | 8.00         | AWS Graviton3 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r7g.large            | 16.00        | AWS Graviton3 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r7g.xlarge           | 32.00        | AWS Graviton3 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r7g.2xlarge          | 64.00        | AWS Graviton3 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r7g.4xlarge          | 128.00       | AWS Graviton3 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r7g.8xlarge          | 256.00       | AWS Graviton3 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r7g.12xlarge         | 384.00       | AWS Graviton3 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r7g.16xlarge         | 512.00       | AWS Graviton3 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r7g.metal            | 512.00       | AWS Graviton3 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **R7gd**             |
| r7gd.medium          | 8.00         | AWS Graviton3 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r7gd.large           | 16.00        | AWS Graviton3 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r7gd.xlarge          | 32.00        | AWS Graviton3 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r7gd.2xlarge         | 64.00        | AWS Graviton3 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r7gd.4xlarge         | 128.00       | AWS Graviton3 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r7gd.8xlarge         | 256.00       | AWS Graviton3 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r7gd.12xlarge        | 384.00       | AWS Graviton3 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r7gd.16xlarge        | 512.00       | AWS Graviton3 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r7gd.metal           | 512.00       | AWS Graviton3 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **R7i**              |
| r7i.large            | 16.00        | Intel Xeon Sapphire Rapids | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r7i.xlarge           | 32.00        | Intel Xeon Sapphire Rapids | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r7i.2xlarge          | 64.00        | Intel Xeon Sapphire Rapids | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r7i.4xlarge          | 128.00       | Intel Xeon Sapphire Rapids | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r7i.8xlarge          | 256.00       | Intel Xeon Sapphire Rapids | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r7i.12xlarge         | 384.00       | Intel Xeon Sapphire Rapids | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r7i.16xlarge         | 512.00       | Intel Xeon Sapphire Rapids | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r7i.24xlarge         | 768.00       | Intel Xeon Sapphire Rapids | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r7i.48xlarge         | 1536.00      | Intel Xeon Sapphire Rapids | 192   | 96        | 2                | ✗ No         | ✗ No               |
| r7i.metal-24xl       | 768.00       | Intel Xeon Sapphire Rapids | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r7i.metal-48xl       | 1536.00      | Intel Xeon Sapphire Rapids | 192   | 96        | 2                | ✗ No         | ✗ No               |
| **R7iz**             |
| r7iz.large           | 16.00        | Intel Xeon Sapphire Rapids | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r7iz.xlarge          | 32.00        | Intel Xeon Sapphire Rapids | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r7iz.2xlarge         | 64.00        | Intel Xeon Sapphire Rapids | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r7iz.4xlarge         | 128.00       | Intel Xeon Sapphire Rapids | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r7iz.8xlarge         | 256.00       | Intel Xeon Sapphire Rapids | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r7iz.12xlarge        | 384.00       | Intel Xeon Sapphire Rapids | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r7iz.16xlarge        | 512.00       | Intel Xeon Sapphire Rapids | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r7iz.32xlarge        | 1024.00      | Intel Xeon Sapphire Rapids | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r7iz.metal-16xl      | 512.00       | Intel Xeon Sapphire Rapids | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r7iz.metal-32xl      | 1024.00      | Intel Xeon Sapphire Rapids | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **R8a**              |
| r8a.medium           | 8.00         | AMD EPYC 9R45              | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r8a.large            | 16.00        | AMD EPYC 9R45              | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r8a.xlarge           | 32.00        | AMD EPYC 9R45              | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r8a.2xlarge          | 64.00        | AMD EPYC 9R45              | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r8a.4xlarge          | 128.00       | AMD EPYC 9R45              | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r8a.8xlarge          | 256.00       | AMD EPYC 9R45              | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r8a.12xlarge         | 384.00       | AMD EPYC 9R45              | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r8a.16xlarge         | 512.00       | AMD EPYC 9R45              | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r8a.24xlarge         | 768.00       | AMD EPYC 9R45              | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8a.48xlarge         | 1536.00      | AMD EPYC 9R45              | 192   | 192       | 1                | ✗ No         | ✗ No               |
| r8a.metal-24xl       | 768.00       | AMD EPYC 9R45              | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8a.metal-48xl       | 1536.00      | AMD EPYC 9R45              | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **R8g**              |
| r8g.medium           | 8.00         | AWS Graviton4 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r8g.large            | 16.00        | AWS Graviton4 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r8g.xlarge           | 32.00        | AWS Graviton4 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r8g.2xlarge          | 64.00        | AWS Graviton4 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r8g.4xlarge          | 128.00       | AWS Graviton4 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r8g.8xlarge          | 256.00       | AWS Graviton4 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r8g.12xlarge         | 384.00       | AWS Graviton4 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r8g.16xlarge         | 512.00       | AWS Graviton4 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r8g.24xlarge         | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8g.48xlarge         | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| r8g.metal-24xl       | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8g.metal-48xl       | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **R8gb**             |
| r8gb.medium          | 8.00         | AWS Graviton4 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r8gb.large           | 16.00        | AWS Graviton4 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r8gb.xlarge          | 32.00        | AWS Graviton4 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r8gb.2xlarge         | 64.00        | AWS Graviton4 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r8gb.4xlarge         | 128.00       | AWS Graviton4 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r8gb.8xlarge         | 256.00       | AWS Graviton4 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r8gb.12xlarge        | 384.00       | AWS Graviton4 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r8gb.16xlarge        | 512.00       | AWS Graviton4 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r8gb.24xlarge        | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8gb.metal-24xl      | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| **R8gd**             |
| r8gd.medium          | 8.00         | AWS Graviton4 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r8gd.large           | 16.00        | AWS Graviton4 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r8gd.xlarge          | 32.00        | AWS Graviton4 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r8gd.2xlarge         | 64.00        | AWS Graviton4 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r8gd.4xlarge         | 128.00       | AWS Graviton4 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r8gd.8xlarge         | 256.00       | AWS Graviton4 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r8gd.12xlarge        | 384.00       | AWS Graviton4 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r8gd.16xlarge        | 512.00       | AWS Graviton4 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r8gd.24xlarge        | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8gd.48xlarge        | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| r8gd.metal-24xl      | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8gd.metal-48xl      | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **R8gn**             |
| r8gn.medium          | 8.00         | AWS Graviton4 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| r8gn.large           | 16.00        | AWS Graviton4 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| r8gn.xlarge          | 32.00        | AWS Graviton4 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| r8gn.2xlarge         | 64.00        | AWS Graviton4 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| r8gn.4xlarge         | 128.00       | AWS Graviton4 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| r8gn.8xlarge         | 256.00       | AWS Graviton4 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| r8gn.12xlarge        | 384.00       | AWS Graviton4 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| r8gn.16xlarge        | 512.00       | AWS Graviton4 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| r8gn.24xlarge        | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8gn.48xlarge        | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| r8gn.metal-24xl      | 768.00       | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| r8gn.metal-48xl      | 1536.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **R8i**              |
| r8i.large            | 16.00        | Intel Xeon Granite Rapids  | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r8i.xlarge           | 32.00        | Intel Xeon Granite Rapids  | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r8i.2xlarge          | 64.00        | Intel Xeon Granite Rapids  | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r8i.4xlarge          | 128.00       | Intel Xeon Granite Rapids  | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r8i.8xlarge          | 256.00       | Intel Xeon Granite Rapids  | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r8i.12xlarge         | 384.00       | Intel Xeon Granite Rapids  | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r8i.16xlarge         | 512.00       | Intel Xeon Granite Rapids  | 64    | 32        | 2                | ✗ No         | ✗ No               |
| r8i.24xlarge         | 768.00       | Intel Xeon Granite Rapids  | 96    | 48        | 2                | ✗ No         | ✗ No               |
| r8i.32xlarge         | 1024.00      | Intel Xeon Granite Rapids  | 128   | 64        | 2                | ✗ No         | ✗ No               |
| r8i.48xlarge         | 1536.00      | Intel Xeon Granite Rapids  | 192   | 96        | 2                | ✗ No         | ✗ No               |
| r8i.96xlarge         | 3072.00      | Intel Xeon Granite Rapids  | 384   | 192       | 2                | ✗ No         | ✗ No               |
| r8i.metal-48xl       | 1536.00      | Intel Xeon Granite Rapids  | 192   | 96        | 2                | ✗ No         | ✗ No               |
| r8i.metal-96xl       | 3072.00      | Intel Xeon Granite Rapids  | 384   | 192       | 2                | ✗ No         | ✗ No               |
| **R8i-flex**         |
| r8i-flex.large       | 16.00        | Intel Xeon Granite Rapids  | 2     | 1         | 2                | ✗ No         | ✗ No               |
| r8i-flex.xlarge      | 32.00        | Intel Xeon Granite Rapids  | 4     | 2         | 2                | ✗ No         | ✗ No               |
| r8i-flex.2xlarge     | 64.00        | Intel Xeon Granite Rapids  | 8     | 4         | 2                | ✗ No         | ✗ No               |
| r8i-flex.4xlarge     | 128.00       | Intel Xeon Granite Rapids  | 16    | 8         | 2                | ✗ No         | ✗ No               |
| r8i-flex.8xlarge     | 256.00       | Intel Xeon Granite Rapids  | 32    | 16        | 2                | ✗ No         | ✗ No               |
| r8i-flex.12xlarge    | 384.00       | Intel Xeon Granite Rapids  | 48    | 24        | 2                | ✗ No         | ✗ No               |
| r8i-flex.16xlarge    | 512.00       | Intel Xeon Granite Rapids  | 64    | 32        | 2                | ✗ No         | ✗ No               |
| **U-3tb1**           |
| u-3tb1.56xlarge      | 3072.00      | Intel Xeon Platinum 8176M  | 224   | 112       | 2                | ✗ No         | ✗ No               |
| **U-6tb1**           |
| u-6tb1.56xlarge      | 6144.00      | Intel Xeon Platinum 8176M  | 224   | 224       | 1                | ✗ No         | ✗ No               |
| u-6tb1.112xlarge     | 6144.00      | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| u-6tb1.metal         | 6144.00      | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U-9tb1**           |
| u-9tb1.112xlarge     | 9216.00      | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| u-9tb1.metal         | 9216.00      | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U-12tb1**          |
| u-12tb1.112xlarge    | 12288.00     | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| u-12tb1.metal        | 12288.00     | Intel Xeon Platinum 8176M  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U-18tb1**          |
| u-18tb1.112xlarge    | 18432.00     | Intel Xeon Platinum 8280L  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| u-18tb1.metal        | 18432.00     | Intel Xeon Platinum 8280L  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U-24tb1**          |
| u-24tb1.112xlarge    | 24576.00     | Intel Xeon Platinum 8280L  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| u-24tb1.metal        | 24576.00     | Intel Xeon Platinum 8280L  | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U7i-6tb**          |
| u7i-6tb.112xlarge    | 6144.00      | Intel Xeon Sapphire Rapids | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U7i-8tb**          |
| u7i-8tb.112xlarge    | 8192.00      | Intel Xeon Sapphire Rapids | 448   | 224       | 2                | ✗ No         | ✗ No               |
| **U7i-12tb**         |
| u7i-12tb.224xlarge   | 12288.00     | Intel Xeon Sapphire Rapids | 896   | 448       | 2                | ✗ No         | ✗ No               |
| **U7in-16tb**        |
| u7in-16tb.224xlarge  | 16384.00     | Intel Xeon Sapphire Rapids | 896   | 448       | 2                | ✗ No         | ✗ No               |
| **U7in-24tb**        |
| u7in-24tb.224xlarge  | 24576.00     | Intel Xeon Sapphire Rapids | 896   | 448       | 2                | ✗ No         | ✗ No               |
| **U7in-32tb**        |
| u7in-32tb.224xlarge  | 32768.00     | Intel Xeon Sapphire Rapids | 896   | 448       | 2                | ✗ No         | ✗ No               |
| **U7inh-32tb**       |
| u7inh-32tb.480xlarge | 32768.00     | Intel Xeon Sapphire Rapids | 1920  | 960       | 2                | ✗ No         | ✗ No               |
| **X1**               |
| x1.16xlarge          | 976.00       | Intel Xeon E7 8880 v3      | 64    | 32        | 2                | ✗ No         | ✗ No               |
| x1.32xlarge          | 1952.00      | Intel Xeon E7 8880 v3      | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **X1e**              |
| x1e.xlarge           | 122.00       | Intel Haswell E7 8880v3    | 4     | 2         | 2                | ✗ No         | ✗ No               |
| x1e.2xlarge          | 244.00       | Intel Haswell E7 8880v3    | 8     | 4         | 2                | ✗ No         | ✗ No               |
| x1e.4xlarge          | 488.00       | Intel Haswell E7 8880v3    | 16    | 8         | 2                | ✗ No         | ✗ No               |
| x1e.8xlarge          | 976.00       | Intel Haswell E7 8880v3    | 32    | 16        | 2                | ✗ No         | ✗ No               |
| x1e.16xlarge         | 1952.00      | Intel Haswell E7 8880v3    | 64    | 32        | 2                | ✗ No         | ✗ No               |
| x1e.32xlarge         | 3904.00      | Intel Haswell E7 8880v3    | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **X2gd**             |
| x2gd.medium          | 16.00        | AWS Graviton2 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| x2gd.large           | 32.00        | AWS Graviton2 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| x2gd.xlarge          | 64.00        | AWS Graviton2 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| x2gd.2xlarge         | 128.00       | AWS Graviton2 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| x2gd.4xlarge         | 256.00       | AWS Graviton2 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| x2gd.8xlarge         | 512.00       | AWS Graviton2 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| x2gd.12xlarge        | 768.00       | AWS Graviton2 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| x2gd.16xlarge        | 1024.00      | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| x2gd.metal           | 1024.00      | AWS Graviton2 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| **X2idn**            |
| x2idn.16xlarge       | 1024.00      | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| x2idn.24xlarge       | 1536.00      | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| x2idn.32xlarge       | 2048.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| x2idn.metal          | 2048.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **X2iedn**           |
| x2iedn.xlarge        | 128.00       | Intel Xeon Ice Lake        | 4     | 2         | 2                | ✗ No         | ✗ No               |
| x2iedn.2xlarge       | 256.00       | Intel Xeon Ice Lake        | 8     | 4         | 2                | ✗ No         | ✗ No               |
| x2iedn.4xlarge       | 512.00       | Intel Xeon Ice Lake        | 16    | 8         | 2                | ✗ No         | ✗ No               |
| x2iedn.8xlarge       | 1024.00      | Intel Xeon Ice Lake        | 32    | 16        | 2                | ✗ No         | ✗ No               |
| x2iedn.16xlarge      | 2048.00      | Intel Xeon Ice Lake        | 64    | 32        | 2                | ✗ No         | ✗ No               |
| x2iedn.24xlarge      | 3072.00      | Intel Xeon Ice Lake        | 96    | 48        | 2                | ✗ No         | ✗ No               |
| x2iedn.32xlarge      | 4096.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| x2iedn.metal         | 4096.00      | Intel Xeon Ice Lake        | 128   | 64        | 2                | ✗ No         | ✗ No               |
| **X2iezn**           |
| x2iezn.2xlarge       | 256.00       | Intel Xeon Platinum 8252   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| x2iezn.4xlarge       | 512.00       | Intel Xeon Platinum 8252   | 16    | 8         | 2                | ✗ No         | ✗ No               |
| x2iezn.6xlarge       | 768.00       | Intel Xeon Platinum 8252   | 24    | 12        | 2                | ✗ No         | ✗ No               |
| x2iezn.8xlarge       | 1024.00      | Intel Xeon Platinum 8252   | 32    | 16        | 2                | ✗ No         | ✗ No               |
| x2iezn.12xlarge      | 1536.00      | Intel Xeon Platinum 8252   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| x2iezn.metal         | 1536.00      | Intel Xeon Platinum 8252   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| **X8g**              |
| x8g.medium           | 16.00        | AWS Graviton4 Processor    | 1     | 1         | 1                | ✗ No         | ✗ No               |
| x8g.large            | 32.00        | AWS Graviton4 Processor    | 2     | 2         | 1                | ✗ No         | ✗ No               |
| x8g.xlarge           | 64.00        | AWS Graviton4 Processor    | 4     | 4         | 1                | ✗ No         | ✗ No               |
| x8g.2xlarge          | 128.00       | AWS Graviton4 Processor    | 8     | 8         | 1                | ✗ No         | ✗ No               |
| x8g.4xlarge          | 256.00       | AWS Graviton4 Processor    | 16    | 16        | 1                | ✗ No         | ✗ No               |
| x8g.8xlarge          | 512.00       | AWS Graviton4 Processor    | 32    | 32        | 1                | ✗ No         | ✗ No               |
| x8g.12xlarge         | 768.00       | AWS Graviton4 Processor    | 48    | 48        | 1                | ✗ No         | ✗ No               |
| x8g.16xlarge         | 1024.00      | AWS Graviton4 Processor    | 64    | 64        | 1                | ✗ No         | ✗ No               |
| x8g.24xlarge         | 1536.00      | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| x8g.48xlarge         | 3072.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| x8g.metal-24xl       | 1536.00      | AWS Graviton4 Processor    | 96    | 96        | 1                | ✗ No         | ✗ No               |
| x8g.metal-48xl       | 3072.00      | AWS Graviton4 Processor    | 192   | 192       | 1                | ✗ No         | ✗ No               |
| **X8aedz**           |
| x8aedz.large         | 64.00        | AMD EPYC 9R05              | 2     | 2         | 1                | ✗ No         | ✗ No               |
| x8aedz.xlarge        | 128.00       | AMD EPYC 9R05              | 4     | 4         | 1                | ✗ No         | ✗ No               |
| x8aedz.3xlarge       | 384.00       | AMD EPYC 9R05              | 12    | 12        | 1                | ✗ No         | ✗ No               |
| x8aedz.6xlarge       | 768.00       | AMD EPYC 9R05              | 24    | 24        | 1                | ✗ No         | ✗ No               |
| x8aedz.12xlarge      | 1536.00      | AMD EPYC 9R05              | 48    | 48        | 1                | ✗ No         | ✗ No               |
| x8aedz.24xlarge      | 3072.00      | AMD EPYC 9R05              | 96    | 96        | 1                | ✗ No         | ✗ No               |
| x8aedz.metal-12xl    | 1536.00      | AMD EPYC 9R05              | 48    | 48        | 1                | ✗ No         | ✗ No               |
| x8aedz.metal-24xl    | 3072.00      | AMD EPYC 9R05              | 96    | 96        | 1                | ✗ No         | ✗ No               |
| **z1d**              |
| z1d.large            | 16.00        | Intel Xeon Platinum 8151   | 2     | 1         | 2                | ✗ No         | ✗ No               |
| z1d.xlarge           | 32.00        | Intel Xeon Platinum 8151   | 4     | 2         | 2                | ✗ No         | ✗ No               |
| z1d.2xlarge          | 64.00        | Intel Xeon Platinum 8151   | 8     | 4         | 2                | ✗ No         | ✗ No               |
| z1d.3xlarge          | 96.00        | Intel Xeon Platinum 8151   | 12    | 6         | 2                | ✗ No         | ✗ No               |
| z1d.6xlarge          | 192.00       | Intel Xeon Platinum 8151   | 24    | 12        | 2                | ✗ No         | ✗ No               |
| z1d.12xlarge         | 384.00       | Intel Xeon Platinum 8151   | 48    | 24        | 2                | ✗ No         | ✗ No               |
| z1d.metal            | 384.00       | Intel Xeon Platinum 8151   | 48    | 24        | 2                | ✗ No         | ✗ No               |

## Network specifications

###### Note

R8a, R8g, R8gd, R8i, R8i-flex, X8g, X8aedz instance types support configurable bandwidth weightings.
With these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
instance types. For the supported configurable weightings, see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").

| Instance type        | Baseline / Burst bandwidth (Gbps) | EFA   | ENA   | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| -------------------- | --------------------------------- | ----- | ----- | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **R5**               |
| r5.large 1           | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5.xlarge 1          | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5.2xlarge 1         | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5.4xlarge 1         | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5.8xlarge           | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5.12xlarge          | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5.16xlarge          | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5.24xlarge          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5.metal             | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5a**              |
| r5a.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5a.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5a.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5a.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5a.8xlarge 1        | 7.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5a.12xlarge         | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5a.16xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5a.24xlarge         | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5ad**             |
| r5ad.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5ad.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5ad.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5ad.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5ad.8xlarge 1       | 7.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5ad.12xlarge        | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5ad.16xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5ad.24xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5b**              |
| r5b.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5b.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5b.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5b.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5b.8xlarge          | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5b.12xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5b.16xlarge         | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5b.24xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5b.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5d**              |
| r5d.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5d.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5d.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5d.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5d.8xlarge          | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5d.12xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5d.16xlarge         | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5d.24xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5d.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5dn**             |
| r5dn.large 1         | 2.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5dn.xlarge 1        | 4.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5dn.2xlarge 1       | 8.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5dn.4xlarge 1       | 16.25 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5dn.8xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5dn.12xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5dn.16xlarge        | 75 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5dn.24xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5dn.metal           | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R5n**              |
| r5n.large 1          | 2.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r5n.xlarge 1         | 4.1 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5n.2xlarge 1        | 8.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r5n.4xlarge 1        | 16.25 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5n.8xlarge          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5n.12xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r5n.16xlarge         | 75 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5n.24xlarge         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r5n.metal            | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R6a**              |
| r6a.large 1          | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6a.xlarge 1         | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6a.2xlarge 1        | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6a.4xlarge 1        | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6a.8xlarge          | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6a.12xlarge         | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6a.16xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6a.24xlarge         | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6a.32xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6a.48xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6a.metal            | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R6g**              |
| r6g.medium 1         | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r6g.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6g.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6g.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6g.4xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6g.8xlarge          | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6g.12xlarge         | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6g.16xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r6g.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R6gd**             |
| r6gd.medium 1        | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r6gd.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6gd.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6gd.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6gd.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6gd.8xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6gd.12xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6gd.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| r6gd.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **R6i**              |
| r6i.large 1          | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6i.xlarge 1         | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6i.2xlarge 1        | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6i.4xlarge 1        | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6i.8xlarge          | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6i.12xlarge         | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6i.16xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6i.24xlarge         | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6i.32xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6i.metal            | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R6id**             |
| r6id.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6id.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6id.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6id.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6id.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6id.12xlarge        | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6id.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6id.24xlarge        | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6id.32xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6id.metal           | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R6idn**            |
| r6idn.large 1        | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6idn.xlarge 1       | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6idn.2xlarge 1      | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6idn.4xlarge 1      | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6idn.8xlarge        | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6idn.12xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6idn.16xlarge       | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6idn.24xlarge       | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6idn.32xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| r6idn.metal          | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **R6in**             |
| r6in.large 1         | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r6in.xlarge 1        | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6in.2xlarge 1       | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r6in.4xlarge 1       | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r6in.8xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6in.12xlarge        | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r6in.16xlarge        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6in.24xlarge        | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r6in.32xlarge        | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| r6in.metal           | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **R7a**              |
| r7a.medium 1         | 0.39 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r7a.large 1          | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r7a.xlarge 1         | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7a.2xlarge 1        | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7a.4xlarge 1        | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7a.8xlarge          | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7a.12xlarge         | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7a.16xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7a.24xlarge         | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7a.32xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7a.48xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7a.metal-48xl       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R7g**              |
| r7g.medium 1         | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r7g.large 1          | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r7g.xlarge 1         | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7g.2xlarge 1        | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7g.4xlarge 1        | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7g.8xlarge          | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7g.12xlarge         | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7g.16xlarge         | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7g.metal            | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R7gd**             |
| r7gd.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r7gd.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r7gd.xlarge 1        | 1.876 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7gd.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7gd.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7gd.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7gd.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7gd.16xlarge        | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7gd.metal           | 30 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R7i**              |
| r7i.large 1          | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r7i.xlarge 1         | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7i.2xlarge 1        | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7i.4xlarge 1        | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7i.8xlarge          | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7i.12xlarge         | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7i.16xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7i.24xlarge         | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7i.48xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7i.metal-24xl       | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7i.metal-48xl       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R7iz**             |
| r7iz.large 1         | 0.781 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r7iz.xlarge 1        | 1.562 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7iz.2xlarge 1       | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r7iz.4xlarge 1       | 6.25 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r7iz.8xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7iz.12xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r7iz.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7iz.32xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7iz.metal-16xl      | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r7iz.metal-32xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R8a**              |
| r8a.medium 1         | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r8a.large 1          | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| r8a.xlarge 1         | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| r8a.2xlarge 1        | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 40                         | ✓ Yes |
| r8a.4xlarge 1        | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| r8a.8xlarge          | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 40                         | ✓ Yes |
| r8a.12xlarge         | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 64                         | ✓ Yes |
| r8a.16xlarge         | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| r8a.24xlarge         | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| r8a.48xlarge         | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| r8a.metal-24xl       | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| r8a.metal-48xl       | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **R8g**              |
| r8g.medium 1         | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r8g.large 1          | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r8g.xlarge 1         | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8g.2xlarge 1        | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8g.4xlarge 1        | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8g.8xlarge          | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8g.12xlarge         | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r8g.16xlarge         | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8g.24xlarge         | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8g.48xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8g.metal-24xl       | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8g.metal-48xl       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R8gb**             |
| r8gb.medium 1        | 2.083 / 16.667                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r8gb.large 1         | 4.166 / 20.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r8gb.xlarge 1        | 8.333 / 26.667                    | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gb.2xlarge 1       | 16.666 / 33.333                   | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gb.4xlarge         | 33.33 Gigabit                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8gb.8xlarge         | 66.66 Gigabit                     | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| r8gb.12xlarge        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| r8gb.16xlarge        | 133.33 Gigabit                    | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| r8gb.24xlarge        | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| r8gb.metal-24xl      | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| **R8gd**             |
| r8gd.medium 1        | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r8gd.large 1         | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r8gd.xlarge 1        | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gd.2xlarge 1       | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gd.4xlarge 1       | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8gd.8xlarge         | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8gd.12xlarge        | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| r8gd.16xlarge        | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8gd.24xlarge        | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8gd.48xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8gd.metal-24xl      | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| r8gd.metal-48xl      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **R8gn**             |
| r8gn.medium 1        | 3.125 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| r8gn.large 1         | 6.25 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r8gn.xlarge 1        | 12.5 / 40.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gn.2xlarge 1       | 25.0 / 50.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r8gn.4xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r8gn.8xlarge         | 100 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| r8gn.12xlarge        | 150 Gigabit                       | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 12                      | 30                         | ✓ Yes |
| r8gn.16xlarge        | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 50                         | ✓ Yes |
| r8gn.24xlarge        | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| r8gn.48xlarge        | 600 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| r8gn.metal-24xl      | 300 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 50                         | ✓ Yes |
| r8gn.metal-48xl      | 600 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 24                      | 50                         | ✓ Yes |
| **R8i**              |
| r8i.large 1          | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| r8i.xlarge 1         | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| r8i.2xlarge 1        | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| r8i.4xlarge 1        | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| r8i.8xlarge          | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| r8i.12xlarge         | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| r8i.16xlarge         | 30 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| r8i.24xlarge         | 40 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| r8i.32xlarge         | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| r8i.48xlarge         | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| r8i.96xlarge         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| r8i.metal-48xl       | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| r8i.metal-96xl       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 24                      | 64                         | ✓ Yes |
| **R8i-flex**         |
| r8i-flex.large 1     | 0.468 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 20                         | ✓ Yes |
| r8i-flex.xlarge 1    | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| r8i-flex.2xlarge 1   | 1.875 / 15.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| r8i-flex.4xlarge 1   | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| r8i-flex.8xlarge 1   | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 10                      | 50                         | ✓ Yes |
| r8i-flex.12xlarge 1  | 11.25 / 22.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 12                      | 50                         | ✓ Yes |
| r8i-flex.16xlarge 1  | 15.0 / 30.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| **U-3tb1**           |
| u-3tb1.56xlarge      | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **U-6tb1**           |
| u-6tb1.56xlarge      | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-6tb1.112xlarge     | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-6tb1.metal         | 100                               | ✗ No  | ✓ Yes | ✗ No        | 1             | 5                       | 30                         | ✓ Yes |
| **U-9tb1**           |
| u-9tb1.112xlarge     | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-9tb1.metal         | 100                               | ✗ No  | ✓ Yes | ✗ No        | 1             | 5                       | 30                         | ✓ Yes |
| **U-12tb1**          |
| u-12tb1.112xlarge    | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-12tb1.metal        | 100                               | ✗ No  | ✓ Yes | ✗ No        | 1             | 5                       | 30                         | ✓ Yes |
| **U-18tb1**          |
| u-18tb1.112xlarge    | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-18tb1.metal        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **U-24tb1**          |
| u-24tb1.112xlarge    | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| u-24tb1.metal        | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **U7i-6tb**          |
| u7i-6tb.112xlarge    | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **U7i-8tb**          |
| u7i-8tb.112xlarge    | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **U7i-12tb**         |
| u7i-12tb.224xlarge   | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **U7in-16tb**        |
| u7in-16tb.224xlarge  | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **U7in-24tb**        |
| u7in-24tb.224xlarge  | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **U7in-32tb**        |
| u7in-32tb.224xlarge  | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **U7inh-32tb**       |
| u7inh-32tb.480xlarge | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 16                      | 50                         | ✓ Yes |
| **X1**               |
| x1.16xlarge          | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x1.32xlarge          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **X1e**              |
| x1e.xlarge 1         | 0.625 / 10.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| x1e.2xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x1e.4xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x1e.8xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x1e.16xlarge         | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x1e.32xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **X2gd**             |
| x2gd.medium 1        | 0.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| x2gd.large 1         | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| x2gd.xlarge 1        | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x2gd.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x2gd.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2gd.8xlarge         | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2gd.12xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2gd.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| x2gd.metal           | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **X2idn**            |
| x2idn.16xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2idn.24xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2idn.32xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2idn.metal          | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **X2iedn**           |
| x2iedn.xlarge 1      | 1.875 / 25.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x2iedn.2xlarge 1     | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x2iedn.4xlarge 1     | 12.5 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2iedn.8xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| x2iedn.16xlarge      | 50 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2iedn.24xlarge      | 75 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2iedn.32xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x2iedn.metal         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **X2iezn**           |
| x2iezn.2xlarge 1     | 12.5 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x2iezn.4xlarge 1     | 15.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2iezn.6xlarge       | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2iezn.8xlarge       | 75 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x2iezn.12xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| x2iezn.metal         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **X8g**              |
| x8g.medium 1         | 0.52 / 12.5                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| x8g.large 1          | 0.937 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| x8g.xlarge 1         | 1.875 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x8g.2xlarge 1        | 3.75 / 15.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| x8g.4xlarge 1        | 7.5 / 15.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x8g.8xlarge          | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| x8g.12xlarge         | 22.5 Gigabit                      | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 8                       | 30                         | ✓ Yes |
| x8g.16xlarge         | 30 Gigabit                        | ✗ No  | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x8g.24xlarge         | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x8g.48xlarge         | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x8g.metal-24xl       | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| x8g.metal-48xl       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **X8aedz**           |
| x8aedz.large 1       | 1.562 / 18.75                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| x8aedz.xlarge 1      | 3.125 / 18.75                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 20                         | ✓ Yes |
| x8aedz.3xlarge 1     | 9.375 / 18.75                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| x8aedz.6xlarge       | 18.75 Gigabit                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 40                         | ✓ Yes |
| x8aedz.12xlarge      | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| x8aedz.24xlarge      | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| x8aedz.metal-12xl    | 37.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 16                      | 64                         | ✓ Yes |
| x8aedz.metal-24xl    | 75 Gigabit                        | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 16                      | 64                         | ✓ Yes |
| **z1d**              |
| z1d.large 1          | 0.75 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| z1d.xlarge 1         | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| z1d.2xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| z1d.3xlarge 1        | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| z1d.6xlarge          | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| z1d.12xlarge         | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| z1d.metal            | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |

###### Note

1 These instances have a baseline bandwidth and can
use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best effort basis.
Other instances types can sustain their maximum performance indefinitely. For more information,
see [instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md").

For `r6in.32xlarge`, `r6in.metal`, `r6idn.32xlarge`, `r6idn.metal`, you must attach at least 2 ENIs, to separate network
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 170 Gbps.

For `u7in-16tb.224xlarge`, `u7in-24tb.224xlarge`, `u7in-32tb.224xlarge`, `u7inh-32tb.480xlarge`, you must attach at least 2 ENIs, to separate network
cards, to achieve 200 Gbps throughput. Each ENI attached to a network card can achieve up to 100 Gbps.

For `r8gn.48xlarge`, `r8gn.metal-48xl`, you must attach at least 2 ENIs, to separate network
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

- R8a, R8g, R8gd, R8i, R8i-flex, X8g, X8aedz virtualized instance types support configurable bandwidth weightings.
  With these instance types, you can optimize an instance's bandwidth for either networking performance
  or Amazon EBS performance. The following table shows the default networking bandwidth performance for these
  instance types. Bare metal instance types are not supported. For the supported configurable weightings,
  see [Configurable bandwidth weighting preferences](../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md "../../../AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md").
- For maximum IOPS performance with U7i instances, we recommend that you use io2 BlockExpress
  volumes.

| Instance type        | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                               |
| -------------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **R5**               |
| r5.large 1           | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.xlarge 1          | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.2xlarge 1         | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.4xlarge           | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.8xlarge           | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.12xlarge          | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.16xlarge          | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.24xlarge          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5.metal             | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5a**              |
| r5a.large 1          | 650.00 / 2880.00                    | 81.25 / 360.00                                    | 3600.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.xlarge 1         | 1085.00 / 2880.00                   | 135.62 / 360.00                                   | 6000.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.2xlarge 1        | 1580.00 / 2880.00                   | 197.50 / 360.00                                   | 8333.00 / 16000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.4xlarge          | 2880.00                             | 360.00                                            | 16000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.8xlarge          | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.12xlarge         | 6780.00                             | 847.50                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.16xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5a.24xlarge         | 13570.00                            | 1696.25                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5ad**             |
| r5ad.large 1         | 650.00 / 2880.00                    | 81.25 / 360.00                                    | 3600.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.xlarge 1        | 1085.00 / 2880.00                   | 135.62 / 360.00                                   | 6000.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.2xlarge 1       | 1580.00 / 2880.00                   | 197.50 / 360.00                                   | 8333.00 / 16000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.4xlarge         | 2880.00                             | 360.00                                            | 16000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.8xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.12xlarge        | 6780.00                             | 847.50                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.16xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5ad.24xlarge        | 13570.00                            | 1696.25                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5b**              |
| r5b.large 1          | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5417.00 / 43333.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.xlarge 1         | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10833.00 / 43333.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.2xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 21667.00 / 43333.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.4xlarge          | 10000.00                            | 1250.00                                           | 43333.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.8xlarge          | 20000.00                            | 2500.00                                           | 86667.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.12xlarge         | 30000.00                            | 3750.00                                           | 130000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.16xlarge         | 40000.00                            | 5000.00                                           | 173333.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.24xlarge         | 60000.00                            | 7500.00                                           | 260000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5b.metal            | 60000.00                            | 7500.00                                           | 260000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5d**              |
| r5d.large 1          | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.xlarge 1         | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.2xlarge 1        | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.4xlarge          | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.8xlarge          | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.12xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.16xlarge         | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.24xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5d.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5dn**             |
| r5dn.large 1         | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.xlarge 1        | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.2xlarge 1       | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.4xlarge         | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.8xlarge         | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.12xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.16xlarge        | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.24xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5dn.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R5n**              |
| r5n.large 1          | 650.00 / 4750.00                    | 81.25 / 593.75                                    | 3600.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.xlarge 1         | 1150.00 / 4750.00                   | 143.75 / 593.75                                   | 6000.00 / 18750.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.2xlarge 1        | 2300.00 / 4750.00                   | 287.50 / 593.75                                   | 12000.00 / 18750.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.4xlarge          | 4750.00                             | 593.75                                            | 18750.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.8xlarge          | 6800.00                             | 850.00                                            | 30000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.12xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.16xlarge         | 13600.00                            | 1700.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.24xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r5n.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6a**              |
| r6a.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.32xlarge         | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.48xlarge         | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6a.metal            | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6g**              |
| r6g.medium 1         | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.large 1          | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.xlarge 1         | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.2xlarge 1        | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.4xlarge          | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.8xlarge          | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.12xlarge         | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.16xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6g.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6gd**             |
| r6gd.medium 1        | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.large 1         | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.xlarge 1        | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.2xlarge 1       | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.8xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.12xlarge        | 14250.00                            | 1781.25                                           | 50000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.16xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6gd.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6i**              |
| r6i.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.32xlarge         | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6i.metal            | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6id**             |
| r6id.large 1         | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6id.metal           | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6idn**            |
| r6idn.large 1        | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 6250.00 / 100000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.xlarge 1       | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 12500.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.2xlarge 1      | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 25000.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.4xlarge 1      | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 50000.00 / 100000.00                 | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.8xlarge        | 25000.00                            | 3125.00                                           | 100000.00                            | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.12xlarge       | 37500.00                            | 4687.50                                           | 150000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.16xlarge       | 50000.00                            | 6250.00                                           | 200000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.24xlarge       | 75000.00                            | 9375.00                                           | 300000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.32xlarge       | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6idn.metal          | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R6in**             |
| r6in.large 1         | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 6250.00 / 100000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.xlarge 1        | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 12500.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.2xlarge 1       | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 25000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.4xlarge 1       | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 50000.00 / 100000.00                 | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.8xlarge         | 25000.00                            | 3125.00                                           | 100000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.12xlarge        | 37500.00                            | 4687.50                                           | 150000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.16xlarge        | 50000.00                            | 6250.00                                           | 200000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.24xlarge        | 75000.00                            | 9375.00                                           | 300000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.32xlarge        | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r6in.metal           | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R7a**              |
| r7a.medium 1         | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.32xlarge         | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7a.48xlarge         | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r7a.metal-48xl       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R7g**              |
| r7g.medium 1         | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.large 1          | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7g.metal            | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R7gd**             |
| r7gd.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| r7gd.metal           | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **R7i**              |
| r7i.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.48xlarge         | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r7i.metal-24xl       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7i.metal-48xl       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R7iz**             |
| r7iz.large 1         | 792.00 / 10000.00                   | 99.00 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.xlarge 1        | 1584.00 / 10000.00                  | 198.00 / 1250.00                                  | 6667.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.2xlarge 1       | 3168.00 / 10000.00                  | 396.00 / 1250.00                                  | 13333.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.12xlarge        | 19000.00                            | 2375.00                                           | 76000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.32xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.metal-16xl      | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r7iz.metal-32xl      | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8a**              |
| r8a.medium 1         | 325.00 / 10000.00                   | 40.62 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.48xlarge         | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r8a.metal-24xl       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8a.metal-48xl       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8g**              |
| r8g.medium 1         | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.large 1          | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.48xlarge         | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r8g.metal-24xl       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8g.metal-48xl       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8gb**             |
| r8gb.medium 1        | 1562.00 / 25000.00                  | 195.31 / 3125.00                                  | 7500.00 / 120000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.large 1         | 3125.00 / 25000.00                  | 390.62 / 3125.00                                  | 15000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.xlarge 1        | 6250.00 / 25000.00                  | 781.25 / 3125.00                                  | 30000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.2xlarge 1       | 12500.00 / 25000.00                 | 1562.50 / 3125.00                                 | 60000.00 / 120000.00                 | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.4xlarge         | 25000.00                            | 3125.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.8xlarge         | 50000.00                            | 6250.00                                           | 240000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.12xlarge        | 75000.00                            | 9375.00                                           | 360000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.16xlarge        | 100000.00                           | 12500.00                                          | 480000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.24xlarge        | 150000.00                           | 18750.00                                          | 720000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gb.metal-24xl      | 150000.00                           | 18750.00                                          | 720000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8gd**             |
| r8gd.medium 1        | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.large 1         | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.xlarge 1        | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.2xlarge 1       | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.4xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.8xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.48xlarge        | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r8gd.metal-24xl      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gd.metal-48xl      | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8gn**             |
| r8gn.medium 1        | 760.00 / 10000.00                   | 95.00 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.large 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 5000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 10000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.2xlarge 1       | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.4xlarge         | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.8xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.12xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.16xlarge        | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.24xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.metal-24xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8gn.metal-48xl      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8i**              |
| r8i.large 1          | 650.00 / 10000.00                   | 81.25 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.32xlarge         | 40000.00                            | 5000.00                                           | 160000.00                            | ✓ Yes | 88 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.48xlarge         | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r8i.96xlarge         | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| r8i.metal-48xl       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i.metal-96xl       | 80000.00                            | 10000.00                                          | 480000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **R8i-flex**         |
| r8i-flex.large 1     | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.xlarge 1    | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.2xlarge 1   | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.4xlarge 1   | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.8xlarge 1   | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.12xlarge 1  | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| r8i-flex.16xlarge 1  | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 40000.00 / 80000.00                  | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **U-3tb1**           |
| u-3tb1.56xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U-6tb1**           |
| u-6tb1.56xlarge      | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-6tb1.112xlarge     | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-6tb1.metal         | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U-9tb1**           |
| u-9tb1.112xlarge     | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-9tb1.metal         | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U-12tb1**          |
| u-12tb1.112xlarge    | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-12tb1.metal        | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U-18tb1**          |
| u-18tb1.112xlarge    | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-18tb1.metal        | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U-24tb1**          |
| u-24tb1.112xlarge    | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| u-24tb1.metal        | 38000.00                            | 4750.00                                           | 160000.00                            | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **U7i-6tb**          |
| u7i-6tb.112xlarge    | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7i-8tb**          |
| u7i-8tb.112xlarge    | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7i-12tb**         |
| u7i-12tb.224xlarge   | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7in-16tb**        |
| u7in-16tb.224xlarge  | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7in-24tb**        |
| u7in-24tb.224xlarge  | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7in-32tb**        |
| u7in-32tb.224xlarge  | 100000.00                           | 12500.00                                          | 560000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **U7inh-32tb**       |
| u7inh-32tb.480xlarge | 160000.00                           | 20000.00                                          | 840000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **X1**               |
| x1.16xlarge          | 7000.00                             | 875.00                                            | 40000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1.32xlarge          | 14000.00                            | 1750.00                                           | 80000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **X1e**              |
| x1e.xlarge           | 500.00                              | 62.50                                             | 3700.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1e.2xlarge          | 1000.00                             | 125.00                                            | 7400.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1e.4xlarge          | 1750.00                             | 218.75                                            | 10000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1e.8xlarge          | 3500.00                             | 437.50                                            | 20000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1e.16xlarge         | 7000.00                             | 875.00                                            | 40000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| x1e.32xlarge         | 14000.00                            | 1750.00                                           | 80000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **X2gd**             |
| x2gd.medium 1        | 315.00 / 4750.00                    | 39.38 / 593.75                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.large 1         | 630.00 / 4750.00                    | 78.75 / 593.75                                    | 3600.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.xlarge 1        | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.2xlarge 1       | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.8xlarge         | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.12xlarge        | 14250.00                            | 1781.25                                           | 60000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.16xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2gd.metal           | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **X2idn**            |
| x2idn.16xlarge       | 40000.00                            | 5000.00                                           | 173333.00                            | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2idn.24xlarge       | 60000.00                            | 7500.00                                           | 260000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2idn.32xlarge       | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2idn.metal          | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **X2iedn**           |
| x2iedn.xlarge 1      | 2500.00 / 20000.00                  | 312.50 / 2500.00                                  | 8125.00 / 65000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.2xlarge 1     | 5000.00 / 20000.00                  | 625.00 / 2500.00                                  | 16250.00 / 65000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.4xlarge 1     | 10000.00 / 20000.00                 | 1250.00 / 2500.00                                 | 32500.00 / 65000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.8xlarge       | 20000.00                            | 2500.00                                           | 65000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.16xlarge      | 40000.00                            | 5000.00                                           | 130000.00                            | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.24xlarge      | 60000.00                            | 7500.00                                           | 195000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.32xlarge      | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iedn.metal         | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **X2iezn**           |
| x2iezn.2xlarge       | 3170.00                             | 396.25                                            | 13333.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iezn.4xlarge       | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iezn.6xlarge       | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iezn.8xlarge       | 12000.00                            | 1500.00                                           | 55000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iezn.12xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| x2iezn.metal         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **X8g**              |
| x8g.medium 1         | 315.00 / 10000.00                   | 39.38 / 1250.00                                   | 2500.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.large 1          | 630.00 / 10000.00                   | 78.75 / 1250.00                                   | 3600.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.xlarge 1         | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.2xlarge 1        | 2500.00 / 10000.00                  | 312.50 / 1250.00                                  | 12000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.4xlarge 1        | 5000.00 / 10000.00                  | 625.00 / 1250.00                                  | 20000.00 / 40000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.8xlarge          | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.12xlarge         | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.16xlarge         | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.24xlarge         | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.48xlarge         | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| x8g.metal-24xl       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 39 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8g.metal-48xl       | 40000.00                            | 5000.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **X8aedz**           |
| x8aedz.large 1       | 1250.00 / 15000.00                  | 156.25 / 1875.00                                  | 5000.00 / 60000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.xlarge 1      | 2500.00 / 15000.00                  | 312.50 / 1875.00                                  | 10000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.3xlarge 1     | 7500.00 / 15000.00                  | 937.50 / 1875.00                                  | 30000.00 / 60000.00                  | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.6xlarge       | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.12xlarge      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.24xlarge      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| x8aedz.metal-12xl    | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| x8aedz.metal-24xl    | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 79 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **z1d**              |
| z1d.large 1          | 800.00 / 3170.00                    | 100.00 / 396.25                                   | 3333.00 / 13333.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.xlarge 1         | 1580.00 / 3170.00                   | 197.50 / 396.25                                   | 6667.00 / 13333.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.2xlarge          | 3170.00                             | 396.25                                            | 13333.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.3xlarge          | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.6xlarge          | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.12xlarge         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| z1d.metal            | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |

###### Note

1 These instances can support maximum performance for 30 minutes at least once every
24 hours, after which they revert to their baseline performance. Other instances can sustain the maximum performance
indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these
instances.

## Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

| Instance type     | Instance store volumes | Instance store type | 100% random read IOPS / Write IOPS | Needs initialization 1 | TRIM support 2 |
| ----------------- | ---------------------- | ------------------- | ---------------------------------- | ---------------------- | -------------- |
| **R5ad**          |
| r5ad.large        | 1 x 75 GB              | NVMe SSD            | 30,000 / 15,000                    |                        | ✓ Yes          |
| r5ad.xlarge       | 1 x 150 GB             | NVMe SSD            | 59,000 / 29,000                    |                        | ✓ Yes          |
| r5ad.2xlarge      | 1 x 300 GB             | NVMe SSD            | 117,000 / 57,000                   |                        | ✓ Yes          |
| r5ad.4xlarge      | 2 x 300 GB             | NVMe SSD            | 234,000 / 114,000                  |                        | ✓ Yes          |
| r5ad.8xlarge      | 2 x 600 GB             | NVMe SSD            | 466,666 / 233,334                  |                        | ✓ Yes          |
| r5ad.12xlarge     | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| r5ad.16xlarge     | 4 x 600 GB             | NVMe SSD            | 933,332 / 466,668                  |                        | ✓ Yes          |
| r5ad.24xlarge     | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| **R5d**           |
| r5d.large         | 1 x 75 GB              | NVMe SSD            | 30,000 / 15,000                    |                        | ✓ Yes          |
| r5d.xlarge        | 1 x 150 GB             | NVMe SSD            | 59,000 / 29,000                    |                        | ✓ Yes          |
| r5d.2xlarge       | 1 x 300 GB             | NVMe SSD            | 117,000 / 57,000                   |                        | ✓ Yes          |
| r5d.4xlarge       | 2 x 300 GB             | NVMe SSD            | 234,000 / 114,000                  |                        | ✓ Yes          |
| r5d.8xlarge       | 2 x 600 GB             | NVMe SSD            | 466,666 / 233,334                  |                        | ✓ Yes          |
| r5d.12xlarge      | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| r5d.16xlarge      | 4 x 600 GB             | NVMe SSD            | 933,332 / 466,668                  |                        | ✓ Yes          |
| r5d.24xlarge      | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| r5d.metal         | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 680,000                |                        | ✓ Yes          |
| **R5dn**          |
| r5dn.large        | 1 x 75 GB              | NVMe SSD            | 29,000 / 14,500                    |                        | ✓ Yes          |
| r5dn.xlarge       | 1 x 150 GB             | NVMe SSD            | 58,000 / 29,000                    |                        | ✓ Yes          |
| r5dn.2xlarge      | 1 x 300 GB             | NVMe SSD            | 116,000 / 58,000                   |                        | ✓ Yes          |
| r5dn.4xlarge      | 2 x 300 GB             | NVMe SSD            | 232,000 / 116,000                  |                        | ✓ Yes          |
| r5dn.8xlarge      | 2 x 600 GB             | NVMe SSD            | 464,000 / 232,000                  |                        | ✓ Yes          |
| r5dn.12xlarge     | 2 x 900 GB             | NVMe SSD            | 700,000 / 350,000                  |                        | ✓ Yes          |
| r5dn.16xlarge     | 4 x 600 GB             | NVMe SSD            | 930,000 / 465,000                  |                        | ✓ Yes          |
| r5dn.24xlarge     | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 700,000                |                        | ✓ Yes          |
| r5dn.metal        | 4 x 900 GB             | NVMe SSD            | 1,400,000 / 700,000                |                        | ✓ Yes          |
| **R6gd**          |
| r6gd.medium       | 1 x 59 GB              | NVMe SSD            | 13,438 / 5,625                     |                        | ✓ Yes          |
| r6gd.large        | 1 x 118 GB             | NVMe SSD            | 26,875 / 11,250                    |                        | ✓ Yes          |
| r6gd.xlarge       | 1 x 237 GB             | NVMe SSD            | 53,750 / 22,500                    |                        | ✓ Yes          |
| r6gd.2xlarge      | 1 x 474 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| r6gd.4xlarge      | 1 x 950 GB             | NVMe SSD            | 215,000 / 90,000                   |                        | ✓ Yes          |
| r6gd.8xlarge      | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| r6gd.12xlarge     | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| r6gd.16xlarge     | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| r6gd.metal        | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **R6id**          |
| r6id.large        | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| r6id.xlarge       | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| r6id.2xlarge      | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| r6id.4xlarge      | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| r6id.8xlarge      | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| r6id.12xlarge     | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| r6id.16xlarge     | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| r6id.24xlarge     | 4 x 1425 GB            | NVMe SSD            | 1,609,996 / 805,000                |                        | ✓ Yes          |
| r6id.32xlarge     | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| r6id.metal        | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **R6idn**         |
| r6idn.large       | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| r6idn.xlarge      | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| r6idn.2xlarge     | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| r6idn.4xlarge     | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| r6idn.8xlarge     | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| r6idn.12xlarge    | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| r6idn.16xlarge    | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| r6idn.24xlarge    | 4 x 1425 GB            | NVMe SSD            | 1,609,996 / 805,000                |                        | ✓ Yes          |
| r6idn.32xlarge    | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| r6idn.metal       | 4 x 1900 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **R7gd**          |
| r7gd.medium       | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| r7gd.large        | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| r7gd.xlarge       | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| r7gd.2xlarge      | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| r7gd.4xlarge      | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| r7gd.8xlarge      | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| r7gd.12xlarge     | 2 x 1425 GB            | NVMe SSD            | 804,998 / 402,500                  |                        | ✓ Yes          |
| r7gd.16xlarge     | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| r7gd.metal        | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| **R8gd**          |
| r8gd.medium       | 1 x 59 GB              | NVMe SSD            | 16,771 / 8,385                     |                        | ✓ Yes          |
| r8gd.large        | 1 x 118 GB             | NVMe SSD            | 33,542 / 16,771                    |                        | ✓ Yes          |
| r8gd.xlarge       | 1 x 237 GB             | NVMe SSD            | 67,083 / 33,542                    |                        | ✓ Yes          |
| r8gd.2xlarge      | 1 x 474 GB             | NVMe SSD            | 134,167 / 67,084                   |                        | ✓ Yes          |
| r8gd.4xlarge      | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| r8gd.8xlarge      | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| r8gd.12xlarge     | 3 x 950 GB             | NVMe SSD            | 804,999 / 402,501                  |                        | ✓ Yes          |
| r8gd.16xlarge     | 2 x 1900 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| r8gd.24xlarge     | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| r8gd.48xlarge     | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| r8gd.metal-24xl   | 3 x 1900 GB            | NVMe SSD            | 1,609,998 / 805,002                |                        | ✓ Yes          |
| r8gd.metal-48xl   | 6 x 1900 GB            | NVMe SSD            | 3,219,996 / 1,610,004              |                        | ✓ Yes          |
| **X1**            |
| x1.16xlarge       | 1 x 1920 GB            | SSD                 |                                    | ✓ Yes                  |                |
| x1.32xlarge       | 2 x 1920 GB            | SSD                 |                                    | ✓ Yes                  |                |
| **X1e**           |
| x1e.xlarge        | 1 x 120 GB             | SSD                 |                                    | ✓ Yes                  |                |
| x1e.2xlarge       | 1 x 240 GB             | SSD                 |                                    | ✓ Yes                  |                |
| x1e.4xlarge       | 1 x 480 GB             | SSD                 |                                    | ✓ Yes                  |                |
| x1e.8xlarge       | 1 x 960 GB             | SSD                 |                                    | ✓ Yes                  |                |
| x1e.16xlarge      | 1 x 1920 GB            | SSD                 |                                    | ✓ Yes                  |                |
| x1e.32xlarge      | 2 x 1920 GB            | SSD                 |                                    | ✓ Yes                  |                |
| **X2gd**          |
| x2gd.medium       | 1 x 59 GB              | NVMe SSD            | 13,438 / 5,625                     |                        | ✓ Yes          |
| x2gd.large        | 1 x 118 GB             | NVMe SSD            | 26,875 / 11,250                    |                        | ✓ Yes          |
| x2gd.xlarge       | 1 x 237 GB             | NVMe SSD            | 53,750 / 22,500                    |                        | ✓ Yes          |
| x2gd.2xlarge      | 1 x 475 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| x2gd.4xlarge      | 1 x 950 GB             | NVMe SSD            | 215,000 / 90,000                   |                        | ✓ Yes          |
| x2gd.8xlarge      | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| x2gd.12xlarge     | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| x2gd.16xlarge     | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| x2gd.metal        | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **X2idn**         |
| x2idn.16xlarge    | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| x2idn.24xlarge    | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| x2idn.32xlarge    | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| x2idn.metal       | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **X2iedn**        |
| x2iedn.xlarge     | 1 x 118 GB             | NVMe SSD            | 26,875 / 11,250                    |                        | ✓ Yes          |
| x2iedn.2xlarge    | 1 x 237 GB             | NVMe SSD            | 53,750 / 22,500                    |                        | ✓ Yes          |
| x2iedn.4xlarge    | 1 x 475 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| x2iedn.8xlarge    | 1 x 950 GB             | NVMe SSD            | 215,000 / 90,000                   |                        | ✓ Yes          |
| x2iedn.16xlarge   | 1 x 1900 GB            | NVMe SSD            | 430,000 / 180,000                  |                        | ✓ Yes          |
| x2iedn.24xlarge   | 2 x 1425 GB            | NVMe SSD            | 645,000 / 270,000                  |                        | ✓ Yes          |
| x2iedn.32xlarge   | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| x2iedn.metal      | 2 x 1900 GB            | NVMe SSD            | 860,000 / 360,000                  |                        | ✓ Yes          |
| **X8aedz**        |
| x8aedz.large      | 1 x 158 GB             | NVMe SSD            | 44,722 / 22,361                    |                        | ✓ Yes          |
| x8aedz.xlarge     | 1 x 316 GB             | NVMe SSD            | 89,444 / 44,722                    |                        | ✓ Yes          |
| x8aedz.3xlarge    | 1 x 950 GB             | NVMe SSD            | 268,333 / 134,167                  |                        | ✓ Yes          |
| x8aedz.6xlarge    | 1 x 1900 GB            | NVMe SSD            | 536,666 / 268,334                  |                        | ✓ Yes          |
| x8aedz.12xlarge   | 1 x 3800 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| x8aedz.24xlarge   | 2 x 3800 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| x8aedz.metal-12xl | 1 x 3800 GB            | NVMe SSD            | 1,073,332 / 536,668                |                        | ✓ Yes          |
| x8aedz.metal-24xl | 2 x 3800 GB            | NVMe SSD            | 2,146,664 / 1,073,336              |                        | ✓ Yes          |
| **z1d**           |
| z1d.large         | 1 x 75 GB              | NVMe SSD            | 30,000 / 15,000                    |                        | ✓ Yes          |
| z1d.xlarge        | 1 x 150 GB             | NVMe SSD            | 59,000 / 29,000                    |                        | ✓ Yes          |
| z1d.2xlarge       | 1 x 300 GB             | NVMe SSD            | 117,000 / 57,000                   |                        | ✓ Yes          |
| z1d.3xlarge       | 1 x 450 GB             | NVMe SSD            | 175,000 / 75,000                   |                        | ✓ Yes          |
| z1d.6xlarge       | 1 x 900 GB             | NVMe SSD            | 350,000 / 170,000                  |                        | ✓ Yes          |
| z1d.12xlarge      | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| z1d.metal         | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type        | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| -------------------- | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **R5**               |
| r5.large             | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r5.xlarge            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.2xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.4xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.8xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.12xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.16xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.24xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5.metal             | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R5a**              |
| r5a.large            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r5a.xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.2xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.4xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.8xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.12xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.16xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5a.24xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| **R5ad**             |
| r5ad.large           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r5ad.xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.2xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.4xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.8xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.12xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.16xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5ad.24xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| **R5b**              |
| r5b.large            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r5b.xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.2xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.4xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.8xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.12xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.16xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.24xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5b.metal            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R5d**              |
| r5d.large            | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r5d.xlarge           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.2xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.4xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.8xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.12xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.16xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.24xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5d.metal            | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R5dn**             |
| r5dn.large           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r5dn.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.24xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5dn.metal           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R5n**              |
| r5n.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r5n.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r5n.metal            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R6a**              |
| r6a.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✗ No           |
| r6a.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| r6a.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| r6a.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✓ Yes       | ✓ Yes    | ✓ Yes          |
| r6a.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.32xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6a.metal            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R6g**              |
| r6g.medium           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r6g.large            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.xlarge           | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.2xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.4xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.8xlarge          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.12xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.16xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6g.metal            | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R6gd**             |
| r6gd.medium          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| r6gd.large           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.2xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.4xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.8xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.12xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.16xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6gd.metal           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R6i**              |
| r6i.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r6i.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.32xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6i.metal            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R6id**             |
| r6id.large           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r6id.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.24xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.32xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6id.metal           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R6idn**            |
| r6idn.large          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r6idn.xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.2xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.4xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.8xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.12xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.16xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.24xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.32xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6idn.metal          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R6in**             |
| r6in.large           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r6in.xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.2xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.4xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.8xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.12xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.16xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.24xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.32xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r6in.metal           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R7a**              |
| r7a.medium           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7a.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7a.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.32xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7a.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R7g**              |
| r7g.medium           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7g.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7g.metal            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R7gd**             |
| r7gd.medium          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7gd.large           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7gd.metal           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R7i**              |
| r7i.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7i.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7i.metal-24xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r7i.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R7iz**             |
| r7iz.large           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r7iz.xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.2xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.4xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.8xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.12xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.16xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.32xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r7iz.metal-16xl      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r7iz.metal-32xl      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8a**              |
| r8a.medium           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8a.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8a.metal-24xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r8a.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8g**              |
| r8g.medium           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8g.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8g.metal-24xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r8g.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8gb**             |
| r8gb.medium          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8gb.large           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.2xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.4xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.8xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.12xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.16xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.24xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gb.metal-24xl      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8gd**             |
| r8gd.medium          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8gd.large           | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.24xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.48xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gd.metal-24xl      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r8gd.metal-48xl      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8gn**             |
| r8gn.medium          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8gn.large           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.2xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.4xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.8xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.12xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.16xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.24xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.48xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8gn.metal-24xl      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r8gn.metal-48xl      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8i**              |
| r8i.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.32xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.96xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| r8i.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| r8i.metal-96xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **R8i-flex**         |
| r8i-flex.large       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.2xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.4xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.8xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.12xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| r8i-flex.16xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U-3tb1**           |
| u-3tb1.56xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U-6tb1**           |
| u-6tb1.56xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-6tb1.112xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-6tb1.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U-9tb1**           |
| u-9tb1.112xlarge     | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-9tb1.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U-12tb1**          |
| u-12tb1.112xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-12tb1.metal        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U-18tb1**          |
| u-18tb1.112xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-18tb1.metal        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U-24tb1**          |
| u-24tb1.112xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| u-24tb1.metal        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **U7i-6tb**          |
| u7i-6tb.112xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7i-8tb**          |
| u7i-8tb.112xlarge    | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7i-12tb**         |
| u7i-12tb.224xlarge   | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7in-16tb**        |
| u7in-16tb.224xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7in-24tb**        |
| u7in-24tb.224xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7in-32tb**        |
| u7in-32tb.224xlarge  | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **U7inh-32tb**       |
| u7inh-32tb.480xlarge | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **X1**               |
| x1.16xlarge          | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1.32xlarge          | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **X1e**              |
| x1e.xlarge           | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1e.2xlarge          | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1e.4xlarge          | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1e.8xlarge          | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1e.16xlarge         | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x1e.32xlarge         | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **X2gd**             |
| x2gd.medium          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| x2gd.large           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.2xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.4xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.8xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.12xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.16xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✓ Yes          |
| x2gd.metal           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **X2idn**            |
| x2idn.16xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2idn.24xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2idn.32xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2idn.metal          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **X2iedn**           |
| x2iedn.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.32xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iedn.metal         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **X2iezn**           |
| x2iezn.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iezn.4xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iezn.6xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iezn.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iezn.12xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x2iezn.metal         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **X8g**              |
| x8g.medium           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| x8g.large            | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.xlarge           | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.2xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.4xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.8xlarge          | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.12xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.16xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.24xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.48xlarge         | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8g.metal-24xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| x8g.metal-48xl       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **X8aedz**           |
| x8aedz.large         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.3xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.6xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| x8aedz.metal-12xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| x8aedz.metal-24xl    | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **z1d**              |
| z1d.large            | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✗ No           |
| z1d.xlarge           | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| z1d.2xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| z1d.3xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| z1d.6xlarge          | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| z1d.12xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✓ Yes    | ✓ Yes          |
| z1d.metal            | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
