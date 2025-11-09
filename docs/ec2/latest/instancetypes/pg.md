# Specifications for Amazon EC2 previous generation instances

AWS offers previous generation instance types for users who have optimized
their applications around them and have yet to upgrade. We encourage you to use
current generation instance types to get the best performance, but we continue
to support the following previous generation instance types.

###### Contents

- [Instance families and instance types](#pg_sizes "#pg_sizes")
- [Instance family summary](#pg_summary "#pg_summary")
- [Performance specifications](#pg_hardware "#pg_hardware")
- [Network specifications](#pg_network "#pg_network")
- [Amazon EBS specifications](#pg_storage-ebs "#pg_storage-ebs")
- [Instance store specifications](#pg_instance-store "#pg_instance-store")
- [Security specifications](#pg_security "#pg_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | ------------ | ------------- | ------------ | ------------- | ------------- |
| A1              | `a1.medium`              | `a1.large`   | `a1.xlarge`   | `a1.2xlarge` | `a1.4xlarge`  | `a1.metal`    |
| C1              | `c1.medium`              | `c1.xlarge`  |
| C3              | `c3.large`               | `c3.xlarge`  | `c3.2xlarge`  | `c3.4xlarge` | `c3.8xlarge`  |
| C4              | `c4.large`               | `c4.xlarge`  | `c4.2xlarge`  | `c4.4xlarge` | `c4.8xlarge`  |
| G3              | `g3.4xlarge`             | `g3.8xlarge` | `g3.16xlarge` |
| I2              | `i2.xlarge`              | `i2.2xlarge` | `i2.4xlarge`  | `i2.8xlarge` |
| M1              | `m1.small`               | `m1.medium`  | `m1.large`    | `m1.xlarge`  |
| M2              | `m2.xlarge`              | `m2.2xlarge` | `m2.4xlarge`  |
| M3              | `m3.medium`              | `m3.large`   | `m3.xlarge`   | `m3.2xlarge` |
| M4              | `m4.large`               | `m4.xlarge`  | `m4.2xlarge`  | `m4.4xlarge` | `m4.10xlarge` | `m4.16xlarge` |
| P2              | `p2.xlarge`              | `p2.8xlarge` | `p2.16xlarge` |
| R3              | `r3.large`               | `r3.xlarge`  | `r3.2xlarge`  | `r3.4xlarge` | `r3.8xlarge`  |
| R4              | `r4.large`               | `r4.xlarge`  | `r4.2xlarge`  | `r4.4xlarge` | `r4.8xlarge`  | `r4.16xlarge` |
| T1              | `t1.micro`               |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ----- |
| A1              | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| C1              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| C3              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| C4              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| G3              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| I2              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M1              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M2              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |
| M3              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| M4              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| P2              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux |
| R3              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| R4              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✓ Yes               | Windows                     | Linux |
| T1              | Xen                                                         | Intel (i386)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux |

## Performance specifications

| Instance type | Memory (GiB) | Processor                 | vCPUs | CPU cores | Threads per core | Accelerators        | Accelerator memory    |
| ------------- | ------------ | ------------------------- | ----- | --------- | ---------------- | ------------------- | --------------------- |
| **A1**        |
| a1.medium     | 2.00         | AWS Graviton Processor    | 1     | 1         | 1                | ✗ No                | ✗ No                  |
| a1.large      | 4.00         | AWS Graviton Processor    | 2     | 2         | 1                | ✗ No                | ✗ No                  |
| a1.xlarge     | 8.00         | AWS Graviton Processor    | 4     | 4         | 1                | ✗ No                | ✗ No                  |
| a1.2xlarge    | 16.00        | AWS Graviton Processor    | 8     | 8         | 1                | ✗ No                | ✗ No                  |
| a1.4xlarge    | 32.00        | AWS Graviton Processor    | 16    | 16        | 1                | ✗ No                | ✗ No                  |
| a1.metal      | 32.00        | AWS Graviton Processor    | 16    | 16        | 1                | ✗ No                | ✗ No                  |
| **C1**        |
| c1.medium     | 1.70         | Intel Xeon Family         | 2     | 2         | 1                | ✗ No                | ✗ No                  |
| c1.xlarge     | 7.00         | Intel Xeon Family         | 8     | 8         | 1                | ✗ No                | ✗ No                  |
| **C3**        |
| c3.large      | 3.75         | Intel Xeon E5-2680v2      | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| c3.xlarge     | 7.50         | Intel Xeon E5-2680v2      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| c3.2xlarge    | 15.00        | Intel Xeon E5-2680v2      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| c3.4xlarge    | 30.00        | Intel Xeon E5-2680v2      | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| c3.8xlarge    | 60.00        | Intel Xeon E5-2680v2      | 32    | 16        | 2                | ✗ No                | ✗ No                  |
| **C4**        |
| c4.large      | 3.75         | Intel Xeon E5-2666v3      | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| c4.xlarge     | 7.50         | Intel Xeon E5-2666v3      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| c4.2xlarge    | 15.00        | Intel Xeon E5-2666v3      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| c4.4xlarge    | 30.00        | Intel Xeon E5-2666v3      | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| c4.8xlarge    | 60.00        | Intel Xeon E5-2666v3      | 36    | 18        | 2                | ✗ No                | ✗ No                  |
| **G3**        |
| g3.4xlarge    | 122.00       | Intel Xeon E5-2686 v4     | 16    | 8         | 2                | 1 x NVIDIA M60 GPU  | 8 GiB (1 x 8 GiB)     |
| g3.8xlarge    | 244.00       | Intel Xeon E5-2686 v4     | 32    | 16        | 2                | 2 x NVIDIA M60 GPU  | 16 GiB (2 x 8 GiB)    |
| g3.16xlarge   | 488.00       | Intel Xeon E5-2686 v4     | 64    | 32        | 2                | 4 x NVIDIA M60 GPU  | 32 GiB (4 x 8 GiB)    |
| **I2**        |
| i2.xlarge     | 30.50        | Intel Xeon E5-2670v2      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| i2.2xlarge    | 61.00        | Intel Xeon E5-2670v2      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| i2.4xlarge    | 122.00       | Intel Xeon E5-2670v2      | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| i2.8xlarge    | 244.00       | Intel Xeon E5-2670v2      | 32    | 16        | 2                | ✗ No                | ✗ No                  |
| **M1**        |
| m1.small      | 1.70         | Intel Xeon Family         | 1     | 1         | 1                | ✗ No                | ✗ No                  |
| m1.medium     | 3.70         | Intel Xeon Family         | 1     | 1         | 1                | ✗ No                | ✗ No                  |
| m1.large      | 7.50         | Intel Xeon Family         | 2     | 2         | 1                | ✗ No                | ✗ No                  |
| m1.xlarge     | 15.00        | Intel Xeon Family         | 4     | 4         | 1                | ✗ No                | ✗ No                  |
| **M2**        |
| m2.xlarge     | 17.10        | Intel Xeon Family         | 2     | 2         | 1                | ✗ No                | ✗ No                  |
| m2.2xlarge    | 34.20        | Intel Xeon Family         | 4     | 4         | 1                | ✗ No                | ✗ No                  |
| m2.4xlarge    | 68.40        | Intel Xeon Family         | 8     | 8         | 1                | ✗ No                | ✗ No                  |
| **M3**        |
| m3.medium     | 3.75         | Intel Xeon E5-2670v2      | 1     | 1         | 1                | ✗ No                | ✗ No                  |
| m3.large      | 7.50         | Intel Xeon E5-2670v2      | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| m3.xlarge     | 15.00        | Intel Xeon E5-2670v2      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| m3.2xlarge    | 30.00        | Intel Xeon E5-2670v2      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| **M4**        |
| m4.large      | 8.00         | Intel Xeon E5-2676v3      | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| m4.xlarge     | 16.00        | Intel Xeon E5-2676v3      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| m4.2xlarge    | 32.00        | Intel Xeon E5-2676v3      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| m4.4xlarge    | 64.00        | Intel Xeon E5-2676v3      | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| m4.10xlarge   | 160.00       | Intel Xeon E5-2676v3      | 40    | 20        | 2                | ✗ No                | ✗ No                  |
| m4.16xlarge   | 256.00       | Intel Xeon E5-2686v4      | 64    | 32        | 2                | ✗ No                | ✗ No                  |
| **P2**        |
| p2.xlarge     | 61.00        | Intel Xeon E5-2686v4      | 4     | 2         | 2                | 1 x NVIDIA K80 GPU  | 12 GiB (1 x 12 GiB)   |
| p2.8xlarge    | 488.00       | Intel Xeon E5-2686v4      | 32    | 16        | 2                | 8 x NVIDIA K80 GPU  | 96 GiB (8 x 12 GiB)   |
| p2.16xlarge   | 732.00       | Intel Xeon E5-2686 v4     | 64    | 32        | 2                | 16 x NVIDIA K80 GPU | 192 GiB (16 x 12 GiB) |
| **R3**        |
| r3.large      | 15.00        | Intel Xeon E5-2670v2      | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| r3.xlarge     | 30.50        | Intel Xeon E5-2670v2      | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| r3.2xlarge    | 61.00        | Intel Xeon E5-2670v2      | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| r3.4xlarge    | 122.00       | Intel Xeon E5-2670v2      | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| r3.8xlarge    | 244.00       | Intel Xeon E5-2670v2      | 32    | 16        | 2                | ✗ No                | ✗ No                  |
| **R4**        |
| r4.large      | 15.25        | Intel Broadwell E5-2686v4 | 2     | 1         | 2                | ✗ No                | ✗ No                  |
| r4.xlarge     | 30.50        | Intel Broadwell E5-2686v4 | 4     | 2         | 2                | ✗ No                | ✗ No                  |
| r4.2xlarge    | 61.00        | Intel Broadwell E5-2686v4 | 8     | 4         | 2                | ✗ No                | ✗ No                  |
| r4.4xlarge    | 122.00       | Intel Broadwell E5-2686v4 | 16    | 8         | 2                | ✗ No                | ✗ No                  |
| r4.8xlarge    | 244.00       | Intel Broadwell E5-2686v4 | 32    | 16        | 2                | ✗ No                | ✗ No                  |
| r4.16xlarge   | 488.00       | Intel Broadwell E5-2686v4 | 64    | 32        | 2                | ✗ No                | ✗ No                  |
| **T1**        |
| t1.micro      | 0.61         | Intel E5-2650             | 1     | 1         | 1                | ✗ No                | ✗ No                  |

## Network specifications

| Instance type | Baseline / Burst bandwidth (Gbps) | EFA  | ENA    | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| ------------- | --------------------------------- | ---- | ------ | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **A1**        |
| a1.medium 1   | 0.5 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| a1.large 1    | 0.75 / 10.0                       | ✗ No | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| a1.xlarge 1   | 1.25 / 10.0                       | ✗ No | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| a1.2xlarge 1  | 2.5 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| a1.4xlarge 1  | 5.0 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| a1.metal 1    | 5.0 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **C1**        |
| c1.medium     | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 2                       | 6                          | ✗ No  |
| c1.xlarge     | High                              | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 15                         | ✗ No  |
| **C3**        |
| c3.large      | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c3.xlarge     | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c3.2xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c3.4xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c3.8xlarge    | 10 Gigabit                        | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **C4**        |
| c4.large      | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| c4.xlarge     | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c4.2xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| c4.4xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| c4.8xlarge    | 10 Gigabit                        | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **G3**        |
| g3.4xlarge 1  | 5.0 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g3.8xlarge    | 10 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g3.16xlarge   | 25 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **I2**        |
| i2.xlarge     | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i2.2xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| i2.4xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| i2.8xlarge    | 10 Gigabit                        | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **M1**        |
| m1.small      | Low                               | ✗ No | ✗ No   | ✗ No        | 1             | 2                       | 4                          | ✗ No  |
| m1.medium     | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 2                       | 6                          | ✗ No  |
| m1.large      | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 3                       | 10                         | ✗ No  |
| m1.xlarge     | High                              | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 15                         | ✗ No  |
| **M2**        |
| m2.xlarge     | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 15                         | ✗ No  |
| m2.2xlarge    | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 30                         | ✗ No  |
| m2.4xlarge    | High                              | ✗ No | ✗ No   | ✗ No        | 1             | 8                       | 30                         | ✗ No  |
| **M3**        |
| m3.medium     | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 2                       | 6                          | ✗ No  |
| m3.large      | Moderate                          | ✗ No | ✗ No   | ✗ No        | 1             | 3                       | 10                         | ✗ No  |
| m3.xlarge     | High                              | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 15                         | ✗ No  |
| m3.2xlarge    | High                              | ✗ No | ✗ No   | ✗ No        | 1             | 4                       | 30                         | ✗ No  |
| **M4**        |
| m4.large      | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 2                       | 10                         | ✓ Yes |
| m4.xlarge     | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m4.2xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| m4.4xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m4.10xlarge   | 10 Gigabit                        | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| m4.16xlarge   | 25 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **P2**        |
| p2.xlarge     | High                              | ✗ No | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| p2.8xlarge    | 10 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| p2.16xlarge   | 25 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **R3**        |
| r3.large      | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r3.xlarge     | Moderate                          | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r3.2xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r3.4xlarge    | High                              | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r3.8xlarge    | 10 Gigabit                        | ✗ No | ✗ No 2 | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **R4**        |
| r4.large 1    | 0.75 / 10.0                       | ✗ No | ✓ Yes  | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| r4.xlarge 1   | 1.25 / 10.0                       | ✗ No | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r4.2xlarge 1  | 2.5 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| r4.4xlarge 1  | 5.0 / 10.0                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r4.8xlarge    | 10 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| r4.16xlarge   | 25 Gigabit                        | ✗ No | ✓ Yes  | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **T1**        |
| t1.micro      | Very Low                          | ✗ No | ✗ No   | ✗ No        | 1             | 2                       | 2                          | ✗ No  |

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

| Instance type | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                           |
| ------------- | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1**        |
| a1.medium 1   | 300.00 / 3500.00                    | 37.50 / 437.50                                    | 2500.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| a1.large 1    | 525.00 / 3500.00                    | 65.62 / 437.50                                    | 4000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| a1.xlarge 1   | 800.00 / 3500.00                    | 100.00 / 437.50                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| a1.2xlarge 1  | 1750.00 / 3500.00                   | 218.75 / 437.50                                   | 10000.00 / 20000.00                  | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| a1.4xlarge    | 3500.00                             | 437.50                                            | 20000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| a1.metal      | 3500.00                             | 437.50                                            | 20000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit")) |
| **C1**        |
| c1.xlarge     | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **C3**        |
| c3.xlarge     | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c3.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c3.4xlarge    | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **C4**        |
| c4.large      | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c4.xlarge     | 750.00                              | 93.75                                             | 6000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c4.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c4.4xlarge    | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| c4.8xlarge    | 4000.00                             | 500.00                                            | 32000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **G3**        |
| g3.4xlarge    | 3500.00                             | 437.50                                            | 20000.00                             | ✗ No  | Up to 26 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| g3.8xlarge    | 7000.00                             | 875.00                                            | 40000.00                             | ✗ No  | Up to 25 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| g3.16xlarge   | 14000.00                            | 1750.00                                           | 80000.00                             | ✗ No  | Up to 23 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **I2**        |
| i2.xlarge     | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| i2.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| i2.4xlarge    | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **M1**        |
| m1.large      | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m1.xlarge     | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **M2**        |
| m2.2xlarge    | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m2.4xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **M3**        |
| m3.xlarge     | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m3.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **M4**        |
| m4.large      | 450.00                              | 56.25                                             | 3600.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m4.xlarge     | 750.00                              | 93.75                                             | 6000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m4.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m4.4xlarge    | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m4.10xlarge   | 4000.00                             | 500.00                                            | 32000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| m4.16xlarge   | 10000.00                            | 1250.00                                           | 65000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **P2**        |
| p2.xlarge     | 750.00                              | 93.75                                             | 6000.00                              | ✗ No  | Up to 26 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| p2.8xlarge    | 5000.00                             | 625.00                                            | 32500.00                             | ✗ No  | Up to 19 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| p2.16xlarge   | 10000.00                            | 1250.00                                           | 65000.00                             | ✗ No  | Up to 11 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **R3**        |
| r3.xlarge     | 500.00                              | 62.50                                             | 4000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r3.2xlarge    | 1000.00                             | 125.00                                            | 8000.00                              | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r3.4xlarge    | 2000.00                             | 250.00                                            | 16000.00                             | ✗ No  | Up to 39 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **R4**        |
| r4.large      | 425.00                              | 53.12                                             | 3000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r4.xlarge     | 850.00                              | 106.25                                            | 6000.00                              | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r4.2xlarge    | 1700.00                             | 212.50                                            | 12000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r4.4xlarge    | 3500.00                             | 437.50                                            | 18750.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r4.8xlarge    | 7000.00                             | 875.00                                            | 37500.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| r4.16xlarge   | 14000.00                            | 1750.00                                           | 75000.00                             | ✗ No  | Up to 40 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))  |
| **T1**        |

###### Note

1 These instances can support maximum performance for 30 minutes at least once every
24 hours, after which they revert to their baseline performance. Other instances can sustain the maximum performance
indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these
instances.

C1, C3, I2, M1, M2, M3, and R3 instances are not Amazon EBS optimized by default. You can optionally enable [Amazon EBS optimization](../../../AWSEC2/latest/UserGuide/ebs-optimized.md "../../../AWSEC2/latest/UserGuide/ebs-optimized.md") for these instances
during or after launch for an additional hourly fee.

## Instance store specifications

| Instance type | Instance store volumes | Instance store type | 100% random read IOPS / Write IOPS | Needs initialization 1 | TRIM support 2 |
| ------------- | ---------------------- | ------------------- | ---------------------------------- | ---------------------- | -------------- |
| **C1**        |
| c1.medium     | 1 x 350 GB             | HDD                 |                                    | ✓ Yes                  |                |
| c1.xlarge     | 4 x 420 GB             | HDD                 |                                    | ✓ Yes                  |                |
| **C3**        |
| c3.large      | 2 x 16 GB              | SSD                 |                                    | ✓ Yes                  |                |
| c3.xlarge     | 2 x 40 GB              | SSD                 |                                    | ✓ Yes                  |                |
| c3.2xlarge    | 2 x 80 GB              | SSD                 |                                    | ✓ Yes                  |                |
| c3.4xlarge    | 2 x 160 GB             | SSD                 |                                    | ✓ Yes                  |                |
| c3.8xlarge    | 2 x 320 GB             | SSD                 |                                    | ✓ Yes                  |                |
| **I2**        |
| i2.xlarge     | 1 x 800 GB             | SSD                 |                                    | ✓ Yes                  |                |
| i2.2xlarge    | 2 x 800 GB             | SSD                 |                                    | ✓ Yes                  |                |
| i2.4xlarge    | 4 x 800 GB             | SSD                 |                                    | ✓ Yes                  |                |
| i2.8xlarge    | 8 x 800 GB             | SSD                 |                                    | ✓ Yes                  |                |
| **M1**        |
| m1.small      | 1 x 160 GB             | HDD                 |                                    | ✓ Yes                  |                |
| m1.medium     | 1 x 410 GB             | HDD                 |                                    | ✓ Yes                  |                |
| m1.large      | 2 x 420 GB             | HDD                 |                                    | ✓ Yes                  |                |
| m1.xlarge     | 4 x 420 GB             | HDD                 |                                    | ✓ Yes                  |                |
| **M2**        |
| m2.xlarge     | 1 x 420 GB             | HDD                 |                                    | ✓ Yes                  |                |
| m2.2xlarge    | 1 x 850 GB             | HDD                 |                                    | ✓ Yes                  |                |
| m2.4xlarge    | 2 x 840 GB             | HDD                 |                                    | ✓ Yes                  |                |
| **M3**        |
| m3.medium     | 1 x 4 GB               | SSD                 |                                    | ✓ Yes                  |                |
| m3.large      | 1 x 32 GB              | SSD                 |                                    | ✓ Yes                  |                |
| m3.xlarge     | 2 x 40 GB              | SSD                 |                                    | ✓ Yes                  |                |
| m3.2xlarge    | 2 x 80 GB              | SSD                 |                                    | ✓ Yes                  |                |
| **R3**        |
| r3.large      | 1 x 32 GB              | SSD                 |                                    | ✓ Yes                  |                |
| r3.xlarge     | 1 x 80 GB              | SSD                 |                                    | ✓ Yes                  |                |
| r3.2xlarge    | 1 x 160 GB             | SSD                 |                                    | ✓ Yes                  |                |
| r3.4xlarge    | 1 x 320 GB             | SSD                 |                                    | ✓ Yes                  |                |
| r3.8xlarge    | 2 x 320 GB             | SSD                 |                                    | ✓ Yes                  |                |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| ------------- | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **A1**        |
| a1.medium     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| a1.large      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| a1.xlarge     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| a1.2xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| a1.4xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| a1.metal      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C1**        |
| c1.medium     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c1.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C3**        |
| c3.large      | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c3.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c3.2xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c3.4xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c3.8xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **C4**        |
| c4.large      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c4.xlarge     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c4.2xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c4.4xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| c4.8xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **G3**        |
| g3.4xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g3.8xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g3.16xlarge   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **I2**        |
| i2.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i2.2xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i2.4xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| i2.8xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M1**        |
| m1.small      | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m1.medium     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m1.large      | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m1.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M2**        |
| m2.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m2.2xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m2.4xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M3**        |
| m3.medium     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m3.large      | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m3.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m3.2xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **M4**        |
| m4.large      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m4.xlarge     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m4.2xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m4.4xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m4.10xlarge   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| m4.16xlarge   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **P2**        |
| p2.xlarge     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| p2.8xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| p2.16xlarge   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R3**        |
| r3.large      | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r3.xlarge     | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r3.2xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r3.4xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r3.8xlarge    | ✓ Yes          | ✗ No                         | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **R4**        |
| r4.large      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r4.xlarge     | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r4.2xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r4.4xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r4.8xlarge    | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| r4.16xlarge   | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **T1**        |
| t1.micro      | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
