# Specifications for Amazon EC2 accelerated computing instances

Accelerated computing instances use hardware accelerators, or co-processors, to perform functions,
such as floating point number calculations, graphics processing, or data pattern matching, more
efficiently than is possible in software running on CPUs.

For information on previous generation instance types of this category, such as G3 instances,
see [Specifications for Amazon EC2 previous generation instances](pg.md "pg.md").

###### Contents

- [Instance families and instance types](#ac-sizes "#ac-sizes")
- [Instance family summary](#ac_summary "#ac_summary")
- [Performance specifications](#ac_hardware "#ac_hardware")
- [Network specifications](#ac_network "#ac_network")
- [Amazon EBS specifications](#ac_storage-ebs "#ac_storage-ebs")
- [Instance store specifications](#ac_instance-store "#ac_instance-store")
- [Security specifications](#ac_security "#ac_security")

###### Pricing

For pricing information, see [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

## Instance families and instance types

| Instance family | Available instance types |
| --------------- | ------------------------ | --------------- | --------------- | --------------- | --------------- | --------------- | -------------- | -------------- |
| DL1             | `dl1.24xlarge`           |
| DL2q            | `dl2q.24xlarge`          |
| F1              | `f1.2xlarge`             | `f1.4xlarge`    | `f1.16xlarge`   |
| F2              | `f2.6xlarge`             | `f2.12xlarge`   | `f2.48xlarge`   |
| G4ad            | `g4ad.xlarge`            | `g4ad.2xlarge`  | `g4ad.4xlarge`  | `g4ad.8xlarge`  | `g4ad.16xlarge` |
| G4dn            | `g4dn.xlarge`            | `g4dn.2xlarge`  | `g4dn.4xlarge`  | `g4dn.8xlarge`  | `g4dn.12xlarge` | `g4dn.16xlarge` | `g4dn.metal`   |
| G5              | `g5.xlarge`              | `g5.2xlarge`    | `g5.4xlarge`    | `g5.8xlarge`    | `g5.12xlarge`   | `g5.16xlarge`   | `g5.24xlarge`  | `g5.48xlarge`  |
| G5g             | `g5g.xlarge`             | `g5g.2xlarge`   | `g5g.4xlarge`   | `g5g.8xlarge`   | `g5g.16xlarge`  | `g5g.metal`     |
| G6              | `g6.xlarge`              | `g6.2xlarge`    | `g6.4xlarge`    | `g6.8xlarge`    | `g6.12xlarge`   | `g6.16xlarge`   | `g6.24xlarge`  | `g6.48xlarge`  |
| G6e             | `g6e.xlarge`             | `g6e.2xlarge`   | `g6e.4xlarge`   | `g6e.8xlarge`   | `g6e.12xlarge`  | `g6e.16xlarge`  | `g6e.24xlarge` | `g6e.48xlarge` |
| G6f             | `g6f.large`              | `g6f.xlarge`    | `g6f.2xlarge`   | `g6f.4xlarge`   |
| Gr6             | `gr6.4xlarge`            | `gr6.8xlarge`   |
| Gr6f            | `gr6f.4xlarge`           |
| Inf1            | `inf1.xlarge`            | `inf1.2xlarge`  | `inf1.6xlarge`  | `inf1.24xlarge` |
| Inf2            | `inf2.xlarge`            | `inf2.8xlarge`  | `inf2.24xlarge` | `inf2.48xlarge` |
| P3              | `p3.2xlarge`             | `p3.8xlarge`    | `p3.16xlarge`   |
| P3dn            | `p3dn.24xlarge`          |
| P4d             | `p4d.24xlarge`           |
| P4de            | `p4de.24xlarge`          |
| P5              | `p5.4xlarge`             | `p5.48xlarge`   |
| P5e             | `p5e.48xlarge`           |
| P5en            | `p5en.48xlarge`          |
| P6-B200         | `p6-b200.48xlarge`       |
| P6e-GB200       | `p6e-gb200.36xlarge`     |
| Trn1            | `trn1.2xlarge`           | `trn1.32xlarge` |
| Trn1n           | `trn1n.32xlarge`         |
| Trn2            | `trn2.48xlarge`          |
| Trn2u           | `trn2u.48xlarge`         |
| VT1             | `vt1.3xlarge`            | `vt1.6xlarge`   | `vt1.24xlarge`  |

## Instance family summary

| Instance family | Hypervisor                                                  | Processor type (architecture) | Metal instances available | Dedicated Hosts support | Spot support | Hibernation support | Supported operating systems |
| --------------- | ----------------------------------------------------------- | ----------------------------- | ------------------------- | ----------------------- | ------------ | ------------------- | --------------------------- | ------- |
| DL1             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| DL2q            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| F1              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| F2              | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| G4ad            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| G4dn            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| G5              | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| G5g             | [Nitro v2](ec2-nitro-instances.md "ec2-nitro-instances.md") | AWS Graviton (arm64)          | ✓ Yes                     | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| G6              | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| G6e             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| G6f             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| Gr6             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| Gr6f            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| Inf1            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| Inf2            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| P3              | Xen                                                         | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| P3dn            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Windows                     | Linux   |
| P4d             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| P4de            | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| P5              | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Windows (`p5.4xlarge` only) | Linux 1 |
| P5e             | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | AMD (x86_64)                  | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| P5en            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| P6-B200         | [Nitro v6](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| P6e-GB200       | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | NVIDIA Grace (arm64)          | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Linux                       |
| Trn1            | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |
| Trn1n           | [Nitro v4](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| Trn2            | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✓ Yes        | ✗ No                | Linux                       |
| Trn2u           | [Nitro v5](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✗ No                    | ✗ No         | ✗ No                | Linux                       |
| VT1             | [Nitro v3](ec2-nitro-instances.md "ec2-nitro-instances.md") | Intel (x86_64)                | ✗ No                      | ✓ Yes                   | ✓ Yes        | ✗ No                | Linux                       |

###### Note

1 `p5.4xlarge` supports both Windows and
Linux operating systems. `p5.48xlarge` supports Linux operating systems only.

## Performance specifications

| Instance type      | Memory (GiB) | Processor                   | vCPUs | CPU cores | Threads per core | Accelerators                                      | Accelerator memory      |
| ------------------ | ------------ | --------------------------- | ----- | --------- | ---------------- | ------------------------------------------------- | ----------------------- |
| **DL1**            |
| dl1.24xlarge       | 768.00       | Intel Xeon P-8275CL         | 96    | 48        | 2                | 8 x Habana Gaudi HL-205 GPU                       | 256 GiB (8 x 32 GiB)    |
| **DL2q**           |
| dl2q.24xlarge      | 768.00       | Intel Xeon Cascade Lake     | 96    | 48        | 2                | 8 x Qualcomm Qualcomm AI100 inference accelerator | 125 GiB (8 x 15 GiB)    |
| **F1**             |
| f1.2xlarge         | 122.00       | Intel Xeon E5-2686v4        | 8     | 4         | 2                | 1 x Xilinx Virtex UltraScale (VU9P) FPGA          | 64 GiB (1 x 64 GiB)     |
| f1.4xlarge         | 244.00       | Intel Xeon E5-2686v4        | 16    | 8         | 2                | 2 x Xilinx Virtex UltraScale (VU9P) FPGA          | 128 GiB (2 x 64 GiB)    |
| f1.16xlarge        | 976.00       | Intel Xeon E5-2686v4        | 64    | 32        | 2                | 8 x Xilinx Virtex UltraScale (VU9P) FPGA          | 512 GiB (8 x 64 GiB)    |
| **F2**             |
| f2.6xlarge         | 256.00       | AMD EPYC 7R13               | 24    | 12        | 2                | 1 x Xilinx Virtex UltraScale+ (VU47P) FPGA        | 80 GiB (1 x 80 GiB)     |
| f2.12xlarge        | 512.00       | AMD EPYC 7R13               | 48    | 24        | 2                | 2 x Xilinx Virtex UltraScale+ (VU47P) FPGA        | 160 GiB (2 x 80 GiB)    |
| f2.48xlarge        | 2048.00      | AMD EPYC 7R13               | 192   | 96        | 2                | 8 x Xilinx Virtex UltraScale+ (VU47P) FPGA        | 640 GiB (8 x 80 GiB)    |
| **G4ad**           |
| g4ad.xlarge        | 16.00        | 2nd Gen AMD EPYC 7R32       | 4     | 2         | 2                | 1 x AMD Radeon Pro V520 GPU                       | 8 GiB (1 x 8 GiB)       |
| g4ad.2xlarge       | 32.00        | 2nd Gen AMD EPYC 7R32       | 8     | 4         | 2                | 1 x AMD Radeon Pro V520 GPU                       | 8 GiB (1 x 8 GiB)       |
| g4ad.4xlarge       | 64.00        | 2nd Gen AMD EPYC 7R32       | 16    | 8         | 2                | 1 x AMD Radeon Pro V520 GPU                       | 8 GiB (1 x 8 GiB)       |
| g4ad.8xlarge       | 128.00       | 2nd Gen AMD EPYC 7R32       | 32    | 16        | 2                | 2 x AMD Radeon Pro V520 GPU                       | 16 GiB (2 x 8 GiB)      |
| g4ad.16xlarge      | 256.00       | 2nd Gen AMD EPYC 7R32       | 64    | 32        | 2                | 4 x AMD Radeon Pro V520 GPU                       | 32 GiB (4 x 8 GiB)      |
| **G4dn**           |
| g4dn.xlarge        | 16.00        | Intel Xeon P-8259L          | 4     | 2         | 2                | 1 x NVIDIA T4 GPU                                 | 16 GiB (1 x 16 GiB)     |
| g4dn.2xlarge       | 32.00        | Intel Xeon P-8259L          | 8     | 4         | 2                | 1 x NVIDIA T4 GPU                                 | 16 GiB (1 x 16 GiB)     |
| g4dn.4xlarge       | 64.00        | Intel Xeon P-8259L          | 16    | 8         | 2                | 1 x NVIDIA T4 GPU                                 | 16 GiB (1 x 16 GiB)     |
| g4dn.8xlarge       | 128.00       | Intel Xeon P-8259L          | 32    | 16        | 2                | 1 x NVIDIA T4 GPU                                 | 16 GiB (1 x 16 GiB)     |
| g4dn.12xlarge      | 192.00       | Intel Xeon P-8259L          | 48    | 24        | 2                | 4 x NVIDIA T4 GPU                                 | 64 GiB (4 x 16 GiB)     |
| g4dn.16xlarge      | 256.00       | Intel Xeon P-8259L          | 64    | 32        | 2                | 1 x NVIDIA T4 GPU                                 | 16 GiB (1 x 16 GiB)     |
| g4dn.metal         | 384.00       | Intel Xeon P-8259L          | 96    | 48        | 2                | 8 x NVIDIA T4 GPU                                 | 128 GiB (8 x 16 GiB)    |
| **G5**             |
| g5.xlarge          | 16.00        | 2nd Gen AMD EPYC 7R32       | 4     | 2         | 2                | 1 x NVIDIA A10G GPU                               | 22 GiB (1 x 22 GiB)     |
| g5.2xlarge         | 32.00        | 2nd Gen AMD EPYC 7R32       | 8     | 4         | 2                | 1 x NVIDIA A10G GPU                               | 22 GiB (1 x 22 GiB)     |
| g5.4xlarge         | 64.00        | 2nd Gen AMD EPYC 7R32       | 16    | 8         | 2                | 1 x NVIDIA A10G GPU                               | 22 GiB (1 x 22 GiB)     |
| g5.8xlarge         | 128.00       | 2nd Gen AMD EPYC 7R32       | 32    | 16        | 2                | 1 x NVIDIA A10G GPU                               | 22 GiB (1 x 22 GiB)     |
| g5.12xlarge        | 192.00       | 2nd Gen AMD EPYC 7R32       | 48    | 24        | 2                | 4 x NVIDIA A10G GPU                               | 89 GiB (4 x 22 GiB)     |
| g5.16xlarge        | 256.00       | 2nd Gen AMD EPYC 7R32       | 64    | 32        | 2                | 1 x NVIDIA A10G GPU                               | 22 GiB (1 x 22 GiB)     |
| g5.24xlarge        | 384.00       | 2nd Gen AMD EPYC 7R32       | 96    | 48        | 2                | 4 x NVIDIA A10G GPU                               | 89 GiB (4 x 22 GiB)     |
| g5.48xlarge        | 768.00       | 2nd Gen AMD EPYC 7R32       | 192   | 96        | 2                | 8 x NVIDIA A10G GPU                               | 178 GiB (8 x 22 GiB)    |
| **G5g**            |
| g5g.xlarge         | 8.00         | AWS Graviton2 Processor     | 4     | 4         | 1                | 1 x NVIDIA T4g GPU                                | 16 GiB (1 x 16 GiB)     |
| g5g.2xlarge        | 16.00        | AWS Graviton2 Processor     | 8     | 8         | 1                | 1 x NVIDIA T4g GPU                                | 16 GiB (1 x 16 GiB)     |
| g5g.4xlarge        | 32.00        | AWS Graviton2 Processor     | 16    | 16        | 1                | 1 x NVIDIA T4g GPU                                | 16 GiB (1 x 16 GiB)     |
| g5g.8xlarge        | 64.00        | AWS Graviton2 Processor     | 32    | 32        | 1                | 1 x NVIDIA T4g GPU                                | 16 GiB (1 x 16 GiB)     |
| g5g.16xlarge       | 128.00       | AWS Graviton2 Processor     | 64    | 64        | 1                | 2 x NVIDIA T4g GPU                                | 32 GiB (2 x 16 GiB)     |
| g5g.metal          | 128.00       | AWS Graviton2 Processor     | 64    | 64        | 1                | 2 x NVIDIA T4g GPU                                | 32 GiB (2 x 16 GiB)     |
| **G6**             |
| g6.xlarge          | 16.00        | AMD EPYC 7R13               | 4     | 2         | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| g6.2xlarge         | 32.00        | AMD EPYC 7R13               | 8     | 4         | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| g6.4xlarge         | 64.00        | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| g6.8xlarge         | 128.00       | AMD EPYC 7R13               | 32    | 16        | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| g6.12xlarge        | 192.00       | AMD EPYC 7R13               | 48    | 24        | 2                | 4 x NVIDIA L4 GPU                                 | 89 GiB (4 x 22 GiB)     |
| g6.16xlarge        | 256.00       | AMD EPYC 7R13               | 64    | 32        | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| g6.24xlarge        | 384.00       | AMD EPYC 7R13               | 96    | 48        | 2                | 4 x NVIDIA L4 GPU                                 | 89 GiB (4 x 22 GiB)     |
| g6.48xlarge        | 768.00       | AMD EPYC 7R13               | 192   | 96        | 2                | 8 x NVIDIA L4 GPU                                 | 178 GiB (8 x 22 GiB)    |
| **G6e**            |
| g6e.xlarge         | 32.00        | AMD EPYC 7R13               | 4     | 2         | 2                | 1 x NVIDIA L40S GPU                               | 44 GiB (1 x 44 GiB)     |
| g6e.2xlarge        | 64.00        | AMD EPYC 7R13               | 8     | 4         | 2                | 1 x NVIDIA L40S GPU                               | 44 GiB (1 x 44 GiB)     |
| g6e.4xlarge        | 128.00       | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA L40S GPU                               | 44 GiB (1 x 44 GiB)     |
| g6e.8xlarge        | 256.00       | AMD EPYC 7R13               | 32    | 16        | 2                | 1 x NVIDIA L40S GPU                               | 44 GiB (1 x 44 GiB)     |
| g6e.12xlarge       | 384.00       | AMD EPYC 7R13               | 48    | 24        | 2                | 4 x NVIDIA L40S GPU                               | 178 GiB (4 x 44 GiB)    |
| g6e.16xlarge       | 512.00       | AMD EPYC 7R13               | 64    | 32        | 2                | 1 x NVIDIA L40S GPU                               | 44 GiB (1 x 44 GiB)     |
| g6e.24xlarge       | 768.00       | AMD EPYC 7R13               | 96    | 48        | 2                | 4 x NVIDIA L40S GPU                               | 178 GiB (4 x 44 GiB)    |
| g6e.48xlarge       | 1536.00      | AMD EPYC 7R13               | 192   | 96        | 2                | 8 x NVIDIA L40S GPU                               | 357 GiB (8 x 44 GiB)    |
| **G6f**            |
| g6f.large          | 8.00         | AMD EPYC 7R13               | 2     | 1         | 2                | 1 x NVIDIA L4 GPU                                 | 2 GiB (1 x 2 GiB)       |
| g6f.xlarge         | 16.00        | AMD EPYC 7R13               | 4     | 2         | 2                | 1 x NVIDIA L4 GPU                                 | 2 GiB (1 x 2 GiB)       |
| g6f.2xlarge        | 32.00        | AMD EPYC 7R13               | 8     | 4         | 2                | 1 x NVIDIA L4 GPU                                 | 5 GiB (1 x 5 GiB)       |
| g6f.4xlarge        | 64.00        | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA L4 GPU                                 | 11 GiB (1 x 11 GiB)     |
| **Gr6**            |
| gr6.4xlarge        | 128.00       | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| gr6.8xlarge        | 256.00       | AMD EPYC 7R13               | 32    | 16        | 2                | 1 x NVIDIA L4 GPU                                 | 22 GiB (1 x 22 GiB)     |
| **Gr6f**           |
| gr6f.4xlarge       | 128.00       | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA L4 GPU                                 | 11 GiB (1 x 11 GiB)     |
| **Inf1**           |
| inf1.xlarge        | 8.00         | Intel Xeon P-8259L          | 4     | 2         | 2                | 1 x AWS Inferentia inference accelerator          | 8 GiB (1 x 8 GiB)       |
| inf1.2xlarge       | 16.00        | Intel Xeon P-8259L          | 8     | 4         | 2                | 1 x AWS Inferentia inference accelerator          | 8 GiB (1 x 8 GiB)       |
| inf1.6xlarge       | 48.00        | Intel Xeon P-8259L          | 24    | 12        | 2                | 4 x AWS Inferentia inference accelerator          | 32 GiB (4 x 8 GiB)      |
| inf1.24xlarge      | 192.00       | Intel Xeon P-8259L          | 96    | 48        | 2                | 16 x AWS Inferentia inference accelerator         | 128 GiB (16 x 8 GiB)    |
| **Inf2**           |
| inf2.xlarge        | 16.00        | AMD EPYC 7R13               | 4     | 2         | 2                | 1 x AWS Inferentia2 inference accelerator         | 32 GiB (1 x 32 GiB)     |
| inf2.8xlarge       | 128.00       | AMD EPYC 7R13               | 32    | 16        | 2                | 1 x AWS Inferentia2 inference accelerator         | 32 GiB (1 x 32 GiB)     |
| inf2.24xlarge      | 384.00       | AMD EPYC 7R13               | 96    | 48        | 2                | 6 x AWS Inferentia2 inference accelerator         | 192 GiB (6 x 32 GiB)    |
| inf2.48xlarge      | 768.00       | AMD EPYC 7R13               | 192   | 96        | 2                | 12 x AWS Inferentia2 inference accelerator        | 384 GiB (12 x 32 GiB)   |
| **P3**             |
| p3.2xlarge         | 61.00        | Intel Xeon E5-2686 v4       | 8     | 4         | 2                | 1 x NVIDIA V100 GPU                               | 16 GiB (1 x 16 GiB)     |
| p3.8xlarge         | 244.00       | Intel Xeon E5-2686 v4       | 32    | 16        | 2                | 4 x NVIDIA V100 GPU                               | 64 GiB (4 x 16 GiB)     |
| p3.16xlarge        | 488.00       | Intel Xeon E5-2686 v4       | 64    | 32        | 2                | 8 x NVIDIA V100 GPU                               | 128 GiB (8 x 16 GiB)    |
| **P3dn**           |
| p3dn.24xlarge      | 768.00       | Intel Xeon Platinum 8175    | 96    | 48        | 2                | 8 x NVIDIA V100 GPU                               | 256 GiB (8 x 32 GiB)    |
| **P4d**            |
| p4d.24xlarge       | 1152.00      | Intel Xeon Platinum 8175    | 96    | 48        | 2                | 8 x NVIDIA A100 GPU                               | 320 GiB (8 x 40 GiB)    |
| **P4de**           |
| p4de.24xlarge      | 1152.00      | Intel Xeon Platinum 8175    | 96    | 48        | 2                | 8 x NVIDIA A100 GPU                               | 640 GiB (8 x 80 GiB)    |
| **P5**             |
| p5.4xlarge         | 256.00       | AMD EPYC 7R13               | 16    | 8         | 2                | 1 x NVIDIA H100 GPU                               | 80 GiB (1 x 80 GiB)     |
| p5.48xlarge        | 2048.00      | AMD EPYC 7R13               | 192   | 96        | 2                | 8 x NVIDIA H100 GPU                               | 640 GiB (8 x 80 GiB)    |
| **P5e**            |
| p5e.48xlarge       | 2048.00      | AMD EPYC 7R13               | 192   | 96        | 2                | 8 x NVIDIA H200 GPU                               | 1128 GiB (8 x 141 GiB)  |
| **P5en**           |
| p5en.48xlarge      | 2048.00      | Intel Xeon Sapphire Rapids  | 192   | 96        | 2                | 8 x NVIDIA H200 GPU                               | 1128 GiB (8 x 141 GiB)  |
| **P6-B200**        |
| p6-b200.48xlarge   | 2048.00      | Intel Xeon Emerald Rapids   | 192   | 96        | 2                | 8 x NVIDIA B200 GPU                               | 1432 GiB (8 x 179 GiB)  |
| **P6e-GB200**      |
| p6e-gb200.36xlarge | 960.00       | Nvidia Grace CPU            | 144   | 144       | 1                | 4 x NVIDIA B200 GPU                               | 740 GiB (4 x 185 GiB)   |
| **Trn1**           |
| trn1.2xlarge       | 32.00        | Intel Xeon Ice Lake 8375C   | 8     | 4         | 2                | 1 x AWS Trainium accelerators                     | 32 GiB (1 x 32 GiB)     |
| trn1.32xlarge      | 512.00       | Intel Xeon Ice Lake 8375C   | 128   | 64        | 2                | 16 x AWS Trainium accelerators                    | 512 GiB (16 x 32 GiB)   |
| **Trn1n**          |
| trn1n.32xlarge     | 512.00       | Intel Xeon Ice Lake         | 128   | 64        | 2                | 16 x AWS Trainium accelerators                    | 512 GiB (16 x 32 GiB)   |
| **Trn2**           |
| trn2.48xlarge      | 2048.00      | Intel Xeon Sapphire Rapids  | 192   | 96        | 2                | 16 x AWS Trainium2 accelerators                   | 8192 GiB (16 x 512 GiB) |
| **Trn2u**          |
| trn2u.48xlarge     | 2048.00      | Intel Xeon Sapphire Rapids  | 192   | 96        | 2                | ✗ No                                              | ✗ No                    |
| **VT1**            |
| vt1.3xlarge        | 24.00        | Intel Cascade Lake P-8259CL | 12    | 6         | 2                | 1 x Xilinx U30 media accelerator                  | 24 GiB (1 x 24 GiB)     |
| vt1.6xlarge        | 48.00        | Intel Cascade Lake P-8259CL | 24    | 12        | 2                | 2 x Xilinx U30 media accelerator                  | 48 GiB (2 x 24 GiB)     |
| vt1.24xlarge       | 192.00       | Intel Cascade Lake P-8259CL | 96    | 48        | 2                | 8 x Xilinx U30 media accelerator                  | 192 GiB (8 x 24 GiB)    |

## Network specifications

| Instance type      | Baseline / Burst bandwidth (Gbps) | EFA   | ENA   | ENA Express | Network cards | Max. network interfaces | IP addresses per interface | IPv6  |
| ------------------ | --------------------------------- | ----- | ----- | ----------- | ------------- | ----------------------- | -------------------------- | ----- |
| **DL1**            |
| dl1.24xlarge       | 4x 100 Gigabit                    | ✓ Yes | ✓ Yes | ✗ No        | 4             | 60                      | 50                         | ✓ Yes |
| **DL2q**           |
| dl2q.24xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **F1**             |
| f1.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| f1.4xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| f1.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 50                         | ✓ Yes |
| **F2**             |
| f2.6xlarge         | 12.5 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| f2.12xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| f2.48xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **G4ad**           |
| g4ad.xlarge 1      | 2.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| g4ad.2xlarge 1     | 4.167 / 10.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 4                          | ✓ Yes |
| g4ad.4xlarge 1     | 8.333 / 10.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| g4ad.8xlarge       | 15 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g4ad.16xlarge      | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **G4dn**           |
| g4dn.xlarge 1      | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| g4dn.2xlarge 1     | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| g4dn.4xlarge 1     | 20.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 3                       | 10                         | ✓ Yes |
| g4dn.8xlarge       | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g4dn.12xlarge      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g4dn.16xlarge      | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g4dn.metal         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **G5**             |
| g5.xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g5.2xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g5.4xlarge 1       | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g5.8xlarge         | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g5.12xlarge        | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g5.16xlarge        | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g5.24xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g5.48xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 7                       | 50                         | ✓ Yes |
| **G5g**            |
| g5g.xlarge 1       | 1.25 / 10.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g5g.2xlarge 1      | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g5g.4xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g5g.8xlarge        | 12 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g5g.16xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g5g.metal          | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **G6**             |
| g6.xlarge 1        | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6.2xlarge 1       | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6.4xlarge 1       | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g6.8xlarge         | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g6.12xlarge        | 40 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g6.16xlarge        | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g6.24xlarge        | 50 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g6.48xlarge        | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 15                      | 50                         | ✓ Yes |
| **G6e**            |
| g6e.xlarge 1       | 2.5 / 20.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6e.2xlarge 1      | 5.0 / 20.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6e.4xlarge        | 20 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g6e.8xlarge        | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| g6e.12xlarge       | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 1             | 10                      | 30                         | ✓ Yes |
| g6e.16xlarge       | 35 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| g6e.24xlarge       | 200 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 2             | 20                      | 50                         | ✓ Yes |
| g6e.48xlarge       | 400 Gigabit                       | ✓ Yes | ✓ Yes | ✓ Yes       | 4             | 40                      | 50                         | ✓ Yes |
| **G6f**            |
| g6f.large 1        | 1.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 2                       | 10                         | ✓ Yes |
| g6f.xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6f.2xlarge 1      | 5.0 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| g6f.4xlarge 1      | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Gr6**            |
| gr6.4xlarge 1      | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| gr6.8xlarge        | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Gr6f**           |
| gr6f.4xlarge 1     | 10.0 / 25.0                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **Inf1**           |
| inf1.xlarge 1      | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 10                         | ✓ Yes |
| inf1.2xlarge 1     | 5.0 / 25.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 10                         | ✓ Yes |
| inf1.6xlarge       | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| inf1.24xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 11                      | 30                         | ✓ Yes |
| **Inf2**           |
| inf2.xlarge 1      | 2.083 / 15.0                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| inf2.8xlarge 1     | 16.667 / 25.0                     | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| inf2.24xlarge      | 50 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| inf2.48xlarge      | 100 Gigabit                       | ✗ No  | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **P3**             |
| p3.2xlarge 1       | 2.5 / 10.0                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| p3.8xlarge         | 10 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| p3.16xlarge        | 25 Gigabit                        | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| **P3dn**           |
| p3dn.24xlarge      | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |
| **P4d**            |
| p4d.24xlarge       | 4x 100 Gigabit                    | ✓ Yes | ✓ Yes | ✗ No        | 4             | 60                      | 50                         | ✓ Yes |
| **P4de**           |
| p4de.24xlarge      | 4x 100 Gigabit                    | ✓ Yes | ✓ Yes | ✗ No        | 4             | 60                      | 50                         | ✓ Yes |
| **P5**             |
| p5.4xlarge         | 100 Gigabit                       | ✓ Yes | ✓ Yes | ✗ No        | 1             | 4                       | 30                         | ✓ Yes |
| p5.48xlarge        | 3200 Gigabit                      | ✓ Yes | ✓ Yes | ✓ Yes       | 32            | 64                      | 50                         | ✓ Yes |
| **P5e**            |
| p5e.48xlarge       | 3200 Gigabit                      | ✓ Yes | ✓ Yes | ✓ Yes       | 32            | 64                      | 50                         | ✓ Yes |
| **P5en**           |
| p5en.48xlarge      | 3200 Gigabit                      | ✓ Yes | ✓ Yes | ✓ Yes       | 16            | 64                      | 50                         | ✓ Yes |
| **P6-B200**        |
| p6-b200.48xlarge   | 3200 Gigabit                      | ✓ Yes | ✓ Yes | ✓ Yes       | 8             | 32                      | 50                         | ✓ Yes |
| **P6e-GB200**      |
| p6e-gb200.36xlarge | 3200 Gigabit                      | ✓ Yes | ✓ Yes | ✗ No        | 17            | 39                      | 50                         | ✓ Yes |
| **Trn1**           |
| trn1.2xlarge 1     | 3.125 / 12.5                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| trn1.32xlarge      | 8x 100 Gigabit                    | ✓ Yes | ✓ Yes | ✗ No        | 8             | 40                      | 50                         | ✓ Yes |
| **Trn1n**          |
| trn1n.32xlarge     | 16x 100 Gigabit                   | ✓ Yes | ✓ Yes | ✗ No        | 16            | 80                      | 50                         | ✓ Yes |
| **Trn2**           |
| trn2.48xlarge      | 16x 200 Gigabit                   | ✓ Yes | ✓ Yes | ✗ No        | 16            | 32                      | 50                         | ✓ Yes |
| **Trn2u**          |
| trn2u.48xlarge     | 16x 200 Gigabit                   | ✓ Yes | ✓ Yes | ✗ No        | 16            | 32                      | 50                         | ✓ Yes |
| **VT1**            |
| vt1.3xlarge        | 3.12 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 4                       | 15                         | ✓ Yes |
| vt1.6xlarge        | 6.25 Gigabit                      | ✗ No  | ✓ Yes | ✗ No        | 1             | 8                       | 30                         | ✓ Yes |
| vt1.24xlarge       | 25 Gigabit                        | ✓ Yes | ✓ Yes | ✗ No        | 1             | 15                      | 50                         | ✓ Yes |

###### Note

1 These instances have a baseline bandwidth and can
use a network I/O credit mechanism to burst beyond their baseline bandwidth on a best effort basis.
Other instances types can sustain their maximum performance indefinitely. For more information,
see [instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md").

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

| Instance type      | Baseline / Maximum bandwidth (Mbps) | Baseline / Maximum throughput (MB/s, 128 KiB I/O) | Baseline / Maximum IOPS (16 KiB I/O) | NVMe  | EBS volume limit                                                                                                                                               |
| ------------------ | ----------------------------------- | ------------------------------------------------- | ------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DL1**            |
| dl1.24xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 28 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **DL2q**           |
| dl2q.24xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 19 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **F1**             |
| f1.2xlarge         | 1700.00                             | 212.50                                            | 12000.00                             | ✗ No  | Up to 26 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| f1.4xlarge         | 3500.00                             | 437.50                                            | 44000.00                             | ✗ No  | Up to 25 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| f1.16xlarge        | 14000.00                            | 1750.00                                           | 75000.00                             | ✗ No  | Up to 19 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **F2**             |
| f2.6xlarge         | 7500.00                             | 937.50                                            | 30000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| f2.12xlarge        | 15000.00                            | 1875.00                                           | 60000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| f2.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **G4ad**           |
| g4ad.xlarge 1      | 400.00 / 3170.00                    | 50.00 / 396.25                                    | 1700.00 / 13333.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4ad.2xlarge 1     | 800.00 / 3170.00                    | 100.00 / 396.25                                   | 3400.00 / 13333.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4ad.4xlarge 1     | 1580.00 / 3170.00                   | 197.50 / 396.25                                   | 6700.00 / 13333.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4ad.8xlarge       | 3170.00                             | 396.25                                            | 13333.00                             | ✓ Yes | Up to 24 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4ad.16xlarge      | 6300.00                             | 787.50                                            | 26667.00                             | ✓ Yes | Up to 21 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **G4dn**           |
| g4dn.xlarge 1      | 950.00 / 3500.00                    | 118.75 / 437.50                                   | 3000.00 / 20000.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.2xlarge 1     | 1150.00 / 3500.00                   | 143.75 / 437.50                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.4xlarge       | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.8xlarge       | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.12xlarge      | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 22 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.16xlarge      | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g4dn.metal         | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **G5**             |
| g5.xlarge 1        | 700.00 / 3500.00                    | 87.50 / 437.50                                    | 3000.00 / 15000.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.2xlarge 1       | 850.00 / 3500.00                    | 106.25 / 437.50                                   | 3500.00 / 15000.00                   | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.4xlarge         | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.8xlarge         | 16000.00                            | 2000.00                                           | 65000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.12xlarge        | 16000.00                            | 2000.00                                           | 65000.00                             | ✓ Yes | Up to 22 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.16xlarge        | 16000.00                            | 2000.00                                           | 65000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.24xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 22 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5.48xlarge        | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 9 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))      |
| **G5g**            |
| g5g.xlarge 1       | 1188.00 / 4750.00                   | 148.50 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5g.2xlarge 1      | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 12000.00 / 20000.00                  | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5g.4xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5g.8xlarge        | 9500.00                             | 1187.50                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5g.16xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| g5g.metal          | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 31 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **G6**             |
| g6.xlarge 1        | 1000.00 / 5000.00                   | 125.00 / 625.00                                   | 4000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.2xlarge 1       | 2000.00 / 5000.00                   | 250.00 / 625.00                                   | 8000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.4xlarge         | 8000.00                             | 1000.00                                           | 32000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.8xlarge         | 16000.00                            | 2000.00                                           | 64000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.12xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.16xlarge        | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.24xlarge        | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6.48xlarge        | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **G6e**            |
| g6e.xlarge 1       | 1000.00 / 5000.00                   | 125.00 / 625.00                                   | 4000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.2xlarge 1      | 2000.00 / 5000.00                   | 250.00 / 625.00                                   | 8000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.4xlarge        | 8000.00                             | 1000.00                                           | 32000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.8xlarge        | 16000.00                            | 2000.00                                           | 64000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.12xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.16xlarge       | 20000.00                            | 2500.00                                           | 80000.00                             | ✓ Yes | 48 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.24xlarge       | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6e.48xlarge       | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 128 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit")) |
| **G6f**            |
| g6f.large 1        | 936.00 / 5000.00                    | 117.00 / 625.00                                   | 3750.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6f.xlarge 1       | 1000.00 / 5000.00                   | 125.00 / 625.00                                   | 4000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6f.2xlarge 1      | 2000.00 / 5000.00                   | 250.00 / 625.00                                   | 8000.00 / 20000.00                   | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| g6f.4xlarge        | 6000.00                             | 750.00                                            | 24000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Gr6**            |
| gr6.4xlarge        | 8000.00                             | 1000.00                                           | 32000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| gr6.8xlarge        | 16000.00                            | 2000.00                                           | 64000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Gr6f**           |
| gr6f.4xlarge       | 8000.00                             | 1000.00                                           | 32000.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Inf1**           |
| inf1.xlarge 1      | 1190.00 / 4750.00                   | 148.75 / 593.75                                   | 4000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf1.2xlarge 1     | 1190.00 / 4750.00                   | 148.75 / 593.75                                   | 6000.00 / 20000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf1.6xlarge       | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf1.24xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 11 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Inf2**           |
| inf2.xlarge 1      | 1250.00 / 10000.00                  | 156.25 / 1250.00                                  | 6000.00 / 40000.00                   | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf2.8xlarge       | 10000.00                            | 1250.00                                           | 40000.00                             | ✓ Yes | Up to 26 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf2.24xlarge      | 30000.00                            | 3750.00                                           | 120000.00                            | ✓ Yes | Up to 28 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| inf2.48xlarge      | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | Up to 28 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **P3**             |
| p3.2xlarge         | 1750.00                             | 218.75                                            | 10000.00                             | ✗ No  | Up to 26 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| p3.8xlarge         | 7000.00                             | 875.00                                            | 40000.00                             | ✗ No  | Up to 23 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| p3.16xlarge        | 14000.00                            | 1750.00                                           | 80000.00                             | ✗ No  | Up to 19 ([Xen-based limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits "../../../AWSEC2/latest/UserGuide/volume_limits.md#xen-limits"))      |
| **P3dn**           |
| p3dn.24xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 17 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **P4d**            |
| p4d.24xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | 28 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P4de**           |
| p4de.24xlarge      | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | 28 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P5**             |
| p5.4xlarge         | 10000.00                            | 1250.00                                           | 32500.00                             | ✓ Yes | 32 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| p5.48xlarge        | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P5e**            |
| p5e.48xlarge       | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P5en**           |
| p5en.48xlarge      | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P6-B200**        |
| p6-b200.48xlarge   | 100000.00                           | 12500.00                                          | 400000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **P6e-GB200**      |
| p6e-gb200.36xlarge | 60000.00                            | 7500.00                                           | 240000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Trn1**           |
| trn1.2xlarge 1     | 5000.00 / 20000.00                  | 625.00 / 2500.00                                  | 16250.00 / 65000.00                  | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| trn1.32xlarge      | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 28 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Trn1n**          |
| trn1n.32xlarge     | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | Up to 28 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| **Trn2**           |
| trn2.48xlarge      | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **Trn2u**          |
| trn2u.48xlarge     | 80000.00                            | 10000.00                                          | 260000.00                            | ✓ Yes | 64 ([Dedicated limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#dedicated-limit"))  |
| **VT1**            |
| vt1.3xlarge 1      | 2375.00 / 4750.00                   | 296.88 / 593.75                                   | 10000.00 / 20000.00                  | ✓ Yes | Up to 25 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| vt1.6xlarge        | 4750.00                             | 593.75                                            | 20000.00                             | ✓ Yes | Up to 23 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |
| vt1.24xlarge       | 19000.00                            | 2375.00                                           | 80000.00                             | ✓ Yes | Up to 27 ([Shared limit](../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit "../../../AWSEC2/latest/UserGuide/volume_limits.md#shared-limit"))     |

###### Note

1 These instances can support maximum performance for 30 minutes at least once every
24 hours, after which they revert to their baseline performance. Other instances can sustain the maximum performance
indefinitely. If your workload requires sustained maximum performance for longer than 30 minutes, use one of these
instances.

## Instance store specifications

The following table shows the instance store volume configuration for supported instance types,
along with the aggregated IOPS performance with 4,096 byte block size at queue depth saturation.

| Instance type      | Instance store volumes | Instance store type | 100% random read IOPS / Write IOPS | Needs initialization 1 | TRIM support 2 |
| ------------------ | ---------------------- | ------------------- | ---------------------------------- | ---------------------- | -------------- |
| **DL1**            |
| dl1.24xlarge       | 4 x 1000 GB            | NVMe SSD            | 1,000,000 / 800,000                |                        | ✓ Yes          |
| **F1**             |
| f1.2xlarge         | 1 x 470 GB             | NVMe SSD            |                                    |                        | ✓ Yes          |
| f1.4xlarge         | 1 x 940 GB             | NVMe SSD            |                                    |                        | ✓ Yes          |
| f1.16xlarge        | 4 x 940 GB             | NVMe SSD            |                                    |                        | ✓ Yes          |
| **F2**             |
| f2.6xlarge         | 1 x 940 GB             | NVMe SSD            | 400,000 / 125,000                  |                        | ✓ Yes          |
| f2.12xlarge        | 2 x 940 GB             | NVMe SSD            | 800,000 / 250,000                  |                        | ✓ Yes          |
| f2.48xlarge        | 8 x 940 GB             | NVMe SSD            | 3,200,000 / 1,000,000              |                        | ✓ Yes          |
| **G4ad**           |
| g4ad.xlarge        | 1 x 150 GB             | NVMe SSD            | 10,417 / 8,333                     |                        | ✓ Yes          |
| g4ad.2xlarge       | 1 x 300 GB             | NVMe SSD            | 20,833 / 16,667                    |                        | ✓ Yes          |
| g4ad.4xlarge       | 1 x 600 GB             | NVMe SSD            | 41,667 / 33,333                    |                        | ✓ Yes          |
| g4ad.8xlarge       | 1 x 1200 GB            | NVMe SSD            | 83,333 / 66,667                    |                        | ✓ Yes          |
| g4ad.16xlarge      | 2 x 1200 GB            | NVMe SSD            | 166,666 / 133,332                  |                        | ✓ Yes          |
| **G4dn**           |
| g4dn.xlarge        | 1 x 125 GB             | NVMe SSD            | 42,500 / 32,500                    |                        | ✓ Yes          |
| g4dn.2xlarge       | 1 x 225 GB             | NVMe SSD            | 42,500 / 32,500                    |                        | ✓ Yes          |
| g4dn.4xlarge       | 1 x 225 GB             | NVMe SSD            | 85,000 / 65,000                    |                        | ✓ Yes          |
| g4dn.8xlarge       | 1 x 900 GB             | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| g4dn.12xlarge      | 1 x 900 GB             | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| g4dn.16xlarge      | 1 x 900 GB             | NVMe SSD            | 250,000 / 200,000                  |                        | ✓ Yes          |
| g4dn.metal         | 2 x 900 GB             | NVMe SSD            | 500,000 / 400,000                  |                        | ✓ Yes          |
| **G5**             |
| g5.xlarge          | 1 x 250 GB             | NVMe SSD            | 40,625 / 20,313                    |                        | ✓ Yes          |
| g5.2xlarge         | 1 x 450 GB             | NVMe SSD            | 40,625 / 20,313                    |                        | ✓ Yes          |
| g5.4xlarge         | 1 x 600 GB             | NVMe SSD            | 125,000 / 62,500                   |                        | ✓ Yes          |
| g5.8xlarge         | 1 x 900 GB             | NVMe SSD            | 250,000 / 125,000                  |                        | ✓ Yes          |
| g5.12xlarge        | 1 x 3800 GB            | NVMe SSD            | 312,500 / 156,250                  |                        | ✓ Yes          |
| g5.16xlarge        | 1 x 1900 GB            | NVMe SSD            | 250,000 / 125,000                  |                        | ✓ Yes          |
| g5.24xlarge        | 1 x 3800 GB            | NVMe SSD            | 312,500 / 156,250                  |                        | ✓ Yes          |
| g5.48xlarge        | 2 x 3800 GB            | NVMe SSD            | 625,000 / 312,500                  |                        | ✓ Yes          |
| **G6**             |
| g6.xlarge          | 1 x 250 GB             | NVMe SSD            | 40,625 / 20,000                    |                        | ✓ Yes          |
| g6.2xlarge         | 1 x 450 GB             | NVMe SSD            | 40,625 / 20,000                    |                        | ✓ Yes          |
| g6.4xlarge         | 1 x 600 GB             | NVMe SSD            | 125,000 / 40,000                   |                        | ✓ Yes          |
| g6.8xlarge         | 2 x 450 GB             | NVMe SSD            | 250,000 / 80,000                   |                        | ✓ Yes          |
| g6.12xlarge        | 4 x 940 GB             | NVMe SSD            | 312,500 / 125,000                  |                        | ✓ Yes          |
| g6.16xlarge        | 2 x 940 GB             | NVMe SSD            | 250,000 / 80,000                   |                        | ✓ Yes          |
| g6.24xlarge        | 4 x 940 GB             | NVMe SSD            | 312,500 / 156,248                  |                        | ✓ Yes          |
| g6.48xlarge        | 8 x 940 GB             | NVMe SSD            | 625,000 / 312,496                  |                        | ✓ Yes          |
| **G6e**            |
| g6e.xlarge         | 1 x 250 GB             | NVMe SSD            | 40,625 / 20,000                    |                        | ✓ Yes          |
| g6e.2xlarge        | 1 x 450 GB             | NVMe SSD            | 40,625 / 20,000                    |                        | ✓ Yes          |
| g6e.4xlarge        | 1 x 600 GB             | NVMe SSD            | 125,000 / 40,000                   |                        | ✓ Yes          |
| g6e.8xlarge        | 2 x 450 GB             | NVMe SSD            | 250,000 / 80,000                   |                        | ✓ Yes          |
| g6e.12xlarge       | 2 x 1900 GB            | NVMe SSD            | 312,500 / 125,000                  |                        | ✓ Yes          |
| g6e.16xlarge       | 2 x 950 GB             | NVMe SSD            | 250,000 / 80,000                   |                        | ✓ Yes          |
| g6e.24xlarge       | 2 x 1900 GB            | NVMe SSD            | 312,500 / 156,250                  |                        | ✓ Yes          |
| g6e.48xlarge       | 4 x 1900 GB            | NVMe SSD            | 625,000 / 312,500                  |                        | ✓ Yes          |
| **G6f**            |
| g6f.large          | 1 x 100 GB             | NVMe SSD            | 16,250 / 8,000                     |                        | ✓ Yes          |
| g6f.xlarge         | 1 x 100 GB             | NVMe SSD            | 27,100 / 13,333                    |                        | ✓ Yes          |
| g6f.2xlarge        | 1 x 200 GB             | NVMe SSD            | 40,625 / 20,000                    |                        | ✓ Yes          |
| g6f.4xlarge        | 1 x 450 GB             | NVMe SSD            | 125,000 / 40,000                   |                        | ✓ Yes          |
| **Gr6**            |
| gr6.4xlarge        | 1 x 600 GB             | NVMe SSD            | 125,000 / 40,000                   |                        | ✓ Yes          |
| gr6.8xlarge        | 2 x 450 GB             | NVMe SSD            | 250,000 / 80,000                   |                        | ✓ Yes          |
| **Gr6f**           |
| gr6f.4xlarge       | 1 x 450 GB             | NVMe SSD            | 125,000 / 40,000                   |                        | ✓ Yes          |
| **P3dn**           |
| p3dn.24xlarge      | 2 x 900 GB             | NVMe SSD            | 700,000 / 340,000                  |                        | ✓ Yes          |
| **P4d**            |
| p4d.24xlarge       | 8 x 1000 GB            | NVMe SSD            | 2,000,000 / 1,600,000              |                        | ✓ Yes          |
| **P4de**           |
| p4de.24xlarge      | 8 x 1000 GB            | NVMe SSD            | 2,000,000 / 1,600,000              |                        | ✓ Yes          |
| **P5**             |
| p5.4xlarge         | 1 x 3800 GB            | NVMe SSD            | 550,000 / 275,000                  |                        | ✓ Yes          |
| p5.48xlarge        | 8 x 3800 GB            | NVMe SSD            | 4,400,000 / 2,200,000              |                        | ✓ Yes          |
| **P5e**            |
| p5e.48xlarge       | 8 x 3800 GB            | NVMe SSD            | 4,400,000 / 2,200,000              |                        | ✓ Yes          |
| **P5en**           |
| p5en.48xlarge      | 8 x 3800 GB            | NVMe SSD            | 4,400,000 / 2,200,000              |                        | ✓ Yes          |
| **P6-B200**        |
| p6-b200.48xlarge   | 8 x 3800 GB            | NVMe SSD            | 4,400,000 / 2,200,000              |                        | ✓ Yes          |
| **P6e-GB200**      |
| p6e-gb200.36xlarge | 3 x 7500 GB            | NVMe SSD            | 2,550,000 / 2,400,000              |                        | ✓ Yes          |
| **Trn1**           |
| trn1.2xlarge       | 1 x 474 GB             | NVMe SSD            | 107,500 / 45,000                   |                        | ✓ Yes          |
| trn1.32xlarge      | 4 x 1900 GB            | NVMe SSD            | 1,720,000 / 720,000                |                        | ✓ Yes          |
| **Trn1n**          |
| trn1n.32xlarge     | 4 x 1900 GB            | NVMe SSD            | 1,720,000 / 720,000                |                        | ✓ Yes          |
| **Trn2**           |
| trn2.48xlarge      | 4 x 1900 GB            | NVMe SSD            | 1,720,000 / 720,000                |                        | ✓ Yes          |
| **Trn2u**          |
| trn2u.48xlarge     | 4 x 1900 GB            | NVMe SSD            | 1,720,000 / 720,000                |                        | ✓ Yes          |

1 Volumes attached to certain instances suffer a first-write
penalty unless initialized. For more information, see [Optimize disk performance for
instance store volumes](../../../AWSEC2/latest/UserGuide/disk-performance.md "../../../AWSEC2/latest/UserGuide/disk-performance.md").

2 For more information, see [Instance
store volume TRIM support](../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport "../../../AWSEC2/latest/UserGuide/ssd-instance-store.md#InstanceStoreTrimSupport").

## Security specifications

| Instance type      | EBS encryption | Instance store encryption    | Encryption in transit | AMD SEV-SNP | NitroTPM | Nitro Enclaves |
| ------------------ | -------------- | ---------------------------- | --------------------- | ----------- | -------- | -------------- |
| **DL1**            |
| dl1.24xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **DL2q**           |
| dl2q.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **F1**             |
| f1.2xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| f1.4xlarge         | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| f1.16xlarge        | ✓ Yes          | ✓ Yes                        | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **F2**             |
| f2.6xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| f2.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| f2.48xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **G4ad**           |
| g4ad.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| g4ad.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| g4ad.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| g4ad.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| g4ad.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **G4dn**           |
| g4dn.xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.8xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.12xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.16xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g4dn.metal         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **G5**             |
| g5.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.24xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g5.48xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **G5g**            |
| g5g.xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g5g.2xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g5g.4xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g5g.8xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g5g.16xlarge       | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| g5g.metal          | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **G6**             |
| g6.xlarge          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.2xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.8xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.12xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.16xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.24xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6.48xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **G6e**            |
| g6e.xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.2xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.4xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.8xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.12xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.16xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.24xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6e.48xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **G6f**            |
| g6f.large          | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| g6f.xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6f.2xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| g6f.4xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **Gr6**            |
| gr6.4xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| gr6.8xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **Gr6f**           |
| gr6f.4xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **Inf1**           |
| inf1.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf1.2xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf1.6xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf1.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **Inf2**           |
| inf2.xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf2.8xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf2.24xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| inf2.48xlarge      | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **P3**             |
| p3.2xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| p3.8xlarge         | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| p3.16xlarge        | ✓ Yes          | Instance store not supported | ✗ No                  | ✗ No        | ✗ No     | ✗ No           |
| **P3dn**           |
| p3dn.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **P4d**            |
| p4d.24xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **P4de**           |
| p4de.24xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✓ Yes          |
| **P5**             |
| p5.4xlarge         | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| p5.48xlarge        | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **P5e**            |
| p5e.48xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **P5en**           |
| p5en.48xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **P6-B200**        |
| p6-b200.48xlarge   | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✗ No           |
| **P6e-GB200**      |
| p6e-gb200.36xlarge | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Trn1**           |
| trn1.2xlarge       | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| trn1.32xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Trn1n**          |
| trn1n.32xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| **Trn2**           |
| trn2.48xlarge      | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **Trn2u**          |
| trn2u.48xlarge     | ✓ Yes          | ✓ Yes                        | ✓ Yes                 | ✗ No        | ✓ Yes    | ✓ Yes          |
| **VT1**            |
| vt1.3xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| vt1.6xlarge        | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
| vt1.24xlarge       | ✓ Yes          | Instance store not supported | ✓ Yes                 | ✗ No        | ✗ No     | ✗ No           |
