# Storage Configuration for SAP HANA

###### Important

To simplify storage configuration and provide more flexible guidance, we have moved to a memory-based sizing approach for SAP HANA storage. The documentation has been reorganized and is now located in the Environment Setup section to ensure storage layout is part of your build design.

While this document remains available as a reference for existing deployments, we recommend following the new guidance for all new implementations. The new approach provides clearer sizing logic and better control over performance optimization.

See [SAP Hana Environment Setup - Configure Storage (EBS)](storage-configuration-ebs.md "storage-configuration-ebs.md")

SAP HANA stores and processes all or most of its data in memory, and provides protection against data loss by saving the data in persistent storage locations. To achieve optimal performance, the storage solution used for SAP HANA data and log volumes should meet SAP’s storage KPI. AWS has worked with SAP to certify both Amazon EBS General Purpose SSD (`gp2` and `gp3`) and Provisioned IOPS SSD (`io1`, `io2`, and `io2 Block Express`) storage solutions for SAP HANA workloads.

You can use Amazon FSx for NetApp ONTAP, Amazon EBS or Amazon EFS to configure storage for your SAP HANA deployments on AWS. For more information, see [Configure storage](configure-storage.md "configure-storage.md").

`gp2` and `gp3` volumes balance price and performance for a variety of workloads, while `io1`, `io2`, and `io2 Block Express` volumes provide the highest performance for mission-critical applications. From these options, you can choose the best storage solution that meets your performance and cost requirements. We recommend the `io2` or `io2 Block Express` configuration for mission-critical SAP HANA production workloads.

For multi-node deployments, storage volumes for SAP HANA data and logs are provisioned in the master and worker nodes.

In the following configurations, we intentionally kept the same storage configuration for SAP HANA data and log volumes for all R3, certain R4 and R5, and smaller X1e/X2iedn instance types so you can scale up from smaller instances to larger instances without having to reconfigure your storage.

###### Note

The X1, X1e, X2idn, and X2iedn instance types include instance storage but should not be used to persist any SAP HANA related files.

## `gp2` and `gp3` for HANA

gp2 for HANA data

Certified for production use|
**Instance type**
| **Memory (GiB)**
| **vCPUs / logical processors**\* | **General Purpose SSD (gp2) storage with LVM**
| **Total maximum throughput (MiB/s)**
| **Total baseline IOPS**
| **Total burst IOPS**
|
| **u-24tb1.112xlarge**
| 24,576 | 448 | 6 x 4,800 GiB | 1,500 | 86,400 | N/A |
| **u-24tb1.metal**
| 24,576 | 448 | 6 x 4,800 GiB | 1,500 | 86,400 | N/A |
| **u-18tb1.112xlarge**
| 18,432 | 448 | 6 x 3,600 GiB | 1,500 | 64,800 | N/A |
| **u-18tb1.metal**
| 18,432 | 448 | 6 x 3,600 GiB | 1,500 | 64,800 | N/A |
| **u-12tb1.112xlarge**
| 12,288 | 448 | 6 x 2,400 GiB | 1,500 | 43,200 | N/A |
| **u-12tb1.metal**
| 12,288 | 448 | 6 x 2,400 GiB | 1,500 | 43,200 | N/A |
| **u-9tb1.112xlarge**
| 9,216 | 448 | 6 x 1,800 GiB | 1,500 | 32,400 | N/A |
| **u-9tb1.metal**
| 9,216 | 448 | 6 x 1,800 GiB | 1,500 | 32,400 | N/A |
| **u7in-24tb.112xlarge**
| 24,576 | 896 | 6 x 4,800 GiB | 1,500 | 86,400 | N/A |
| **u7in-16tb.112xlarge**
| 16,384 | 896 | 6 x 3,200 GiB | 1,500 | 57,600 | N/A |
| **u7i-12tb.224xlarge**
| 12,288 | 896 | 6 x 2,400 GiB | 1,500 | 43,200 | N/A |
| **u7i-8tb.112xlarge**
| 8,192 | 448 | 6 x 1,600 GiB | 1,500 | 28,800 | N/A |
| **u7i-6tb.112xlarge**
| 6,144 | 448 | 6 x 1,200 GiB | 1,500 | 21,600 | N/A |
| **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 6 x 6,400 GiB | 1,500 | 96,000 | N/A |
| **u-6tb1.112xlarge**
| 6,144 | 448 | 6 x 1,200 GiB | 1,500 | 21,600 | N/A |
| **u-6tb1.56xlarge**
| 6,144 | 224 | 6 x 1,200 GiB | 1,500 | 21,600 | N/A |
| **u-6tb1.metal**
| 6,144 | 448 | 6 x 1,200 GiB | 1,500 | 21,600 | N/A |
| **u-3tb1.56xlarge**
| 3,072 | 224 | 3 x 1,200 GiB | 750 | 10,800 | N/A |
| **x2iedn.32xlarge**
| 4,096 | 128 | 3 x 1,600 GiB | 750 | 14,400 | N/A |
| **x2iedn.24xlarge**
| 3,072 | 96 | 3 x 1,200 GiB | 750 | 10,800 | N/A |
| **x2idn.32xlarge**
| 2,048 | 128 | 3 x 800 GiB | 750 | 7,200 | 9,000 |
| **x2idn.24xlarge**
| 1,536 | 96 | 3 x 600 GiB | 750 | 5,400 | 9,000 |
| **x2idn.16xlarge**
| 1,024 | 64 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **x1e.32xlarge**
| 3,904 | 128 | 3 x 1,600 GiB | 750 | 14,400 | N/A |
| **x1.32xlarge**
| 1,952 | 128 | 3 x 800 GiB | 750 | 7,200 | 9,000 |
| **x1.16xlarge**
| 976 | 64 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r7i.48xlarge**
| 1,536 | 192 | 3 x 600 GiB | 750 | 5,400 | 9,000 |
| **r7i.24xlarge**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r7i.16xlarge**
| 512 | 64 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r7i.12xlarge**
| 384 | 48 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r7i.8xlarge**
| 256 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r6i.32xlarge**
| 1,024 | 128 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r6i.24xlarge**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r6i.16xlarge**
| 512 | 64 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r6i.12xlarge**
| 384 | 48 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r6i.8xlarge**
| 256 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5.24xlarge**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r5.16xlarge**
| 512 | 64 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5.12xlarge**
| 384 | 48 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5.8xlarge**
| 256 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5.metal**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r5b.24xlarge**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r5b.16xlarge**
| 512 | 64 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5b.12xlarge**
| 384 | 48 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5b.8xlarge**
| 256 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5b.metal**
| 768 | 96 | 3 x 400 GiB | 750 | 3,600 | 9,000 |
| **r4.16xlarge**
| 488 | 64 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r4.8xlarge**
| 244 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r3.8xlarge**
| 244 | 32 | 3 x 225 GiB | 750 | 2,025 | 9,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Total baseline IOPS** | **Total burst IOPS** |
| **x2iedn.4xlarge**
| 512 | 16 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **x2iedn.2xlarge**
| 256 | 8 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **x2iedn.xlarge**
| 128 | 4 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **x1e.4xlarge**
| 488 | 16 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **x1e.2xlarge**
| 244 | 8 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **x1e.xlarge**
| 122 | 4 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r7i.4xlarge**
| 128 | 16 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r7i.2xlarge**
| 64 | 8 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r6i.4xlarge**
| 128 | 16 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r6i.2xlarge**
| 64 | 8 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5.4xlarge**
| 128 | 16 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r5.2xlarge**
| 64 | 8 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r5b.4xlarge**
| 128 | 16 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r5b.2xlarge**
| 64 | 8 | 3 x 225 GiB | 750 | 2,025 | 9,000 |
| **r4.4xlarge**
| 122 | 16 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r4.2xlarge**
| 61 | 8 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r3.4xlarge**
| 122 | 16 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 |
| **r3.2xlarge**
| 61 | 8 | 3 x 225 GiB | 750\*\* | 2,025 | 9,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. \*\*\*gp3 based configurations are only supported in production for Nitro based instances, not for Xen based instances as SAP HANA HCMT storage tests may not meet the minimum required KPI for log writes. gp2 for HANA logs Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Total baseline IOPS** | **Total burst IOPS** |
| **u-24tb1.112xlarge**
| 24,576 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-24tb1.metal**
| 24,576 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-18tb1.112xlarge**
| 18,432 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-18tb1.metal**
| 18,432 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-12tb1.112xlarge**
| 12,288 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-12tb1.metal**
| 12,288 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-9tb1.112xlarge**
| 9,216 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-9tb1.metal**
| 9,216 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7in-24tb.112xlarge**
| 24,576 | 896 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7in-16tb.112xlarge**
| 16,384 | 896 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7i-12tb.224xlarge**
| 12,288 | 896 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7i-8tb.112xlarge**
| 8,192 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7i-6tb.112xlarge**
| 6,144 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 2 x 300 GiB | 500 | 1,800 | 6000 |
| **u-6tb1.112xlarge**
| 6,144 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-6tb1.56xlarge**
| 6,144 | 224 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-6tb1.metal**
| 6,144 | 448 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **u-3tb1.56xlarge**
| 3,072 | 224 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x2iedn.32xlarge**
| 4,096 | 128 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x2iedn.24xlarge**
| 3,072 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x2idn.32xlarge**
| 2,048 | 128 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x2idn.24xlarge**
| 1,536 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x2idn.16xlarge**
| 1,024 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x1e.32xlarge**
| 3,904 | 128 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x1.32xlarge**
| 1,952 | 128 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **x1.16xlarge**
| 976 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r7i.48xlarge**
| 1,536 | 192 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r7i.24xlarge**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r7i.16xlarge**
| 512 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r7i.12xlarge**
| 384 | 48 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r7i.8xlarge**
| 256 | 32 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r6i.32xlarge**
| 1,024 | 128 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r6i.24xlarge**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r6i.16xlarge**
| 512 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r6i.12xlarge**
| 384 | 48 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r6i.8xlarge**
| 256 | 32 | 2 x 175 GiB | 500 | 1,050 | 6,000 |
| **r5.24xlarge**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5.16xlarge**
| 512 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5.12xlarge**
| 384 | 48 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5.8xlarge**
| 256 | 32 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5.metal**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5b.24xlarge**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5b.16xlarge**
| 512 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5b.12xlarge**
| 384 | 48 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5b.8xlarge**
| 256 | 32 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r5b.metal**
| 768 | 96 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r4.16xlarge**
| 488 | 64 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r4.8xlarge**
| 244 | 32 | 2 x 300 GiB | 500 | 1,800 | 6,000 |
| **r3.8xlarge**
| 244 | 32 | 2 x 300 GiB | 500 | 1,800 | 6,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors** | **General Purpose SSD (gp2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Total baseline IOPS** | **Total burst IOPS** |
| **x2iedn.4xlarge**
| 512 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **x2iedn.2xlarge**
| 256 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **x2iedn.xlarge**
| 128 | 4 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **x1e.4xlarge**
| 488 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **x1e.2xlarge**
| 244 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **x1e.xlarge**
| 122 | 4 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r7i.4xlarge**
| 128 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r7i.2xlarge**
| 64 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r6i.4xlarge**
| 128 | 16 | 2 x 175 GiB | 500 | 1,050 | 6,000 |
| **r6i.2xlarge**
| 64 | 8 | 2 x 175 GiB | 500 | 1,050 | 6,000 |
| **r5.4xlarge**
| 128 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r5.2xlarge**
| 64 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r5b.4xlarge**
| 128 | 16 | 2 x 175 GiB | 500 | 1,050 | 6,000 |
| **r5b.2xlarge**
| 64 | 8 | 2 x 175 GiB | 500 | 1,050 | 6,000 |
| **r4.4xlarge**
| 122 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r4.2xlarge**
| 61 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r3.4xlarge**
| 122 | 16 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 |
| **r3.2xlarge**
| 61 | 8 | 2 x 175 GiB | 500\*\* | 1,050 | 6,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. \*\*\*gp3 based configurations are only supported in production for Nitro based instances, not for Xen based instances as SAP HANA HCMT storage tests may not meet the minimum required KPI for log writes. gp3 for HANA data Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp3) storage with LVM** | **Configured throughput per volume (MiB/s)** | **Configured IOPS per volume** | **Total throughput (MiB/s)** | **Total IOPS**
| | **u-24tb1.112xlarge**
| 24,576 | 448 | 2 x 14,400 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u-24tb1.metal**
| 24,576 | 448 | 2 x 14,400 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u-18tb1.112xlarge**
| 18,432 | 448 | 2 x 10,800 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u-18tb1.metal**
| 18,432 | 448 | 2 x 10,800 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u-12tb1.112xlarge**
| 12,228 | 448 | 2 x 7,200 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-12tb1.metal**
| 12,228 | 448 | 2 x 7,200 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-9tb1.112xlarge**
| 9,216 | 448 | 2 x 5,400 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-9tb1.metal**
| 9,216 | 448 | 2 x 5,400 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u7in-24tb.112xlarge**
| 24,576 | 896 | 2 x 14,400 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u7in-16tb.112xlarge**
| 16,384 | 896 | 2 x 9,600 GiB | 1,000 | 9,000 | 2,000 | 18,000 |
| **u7i-12tb.224xlarge**
| 12,288 | 896 | 2 x 7,200 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u7i-8tb.112xlarge**
| 8,192 | 448 | 2 x 4,800 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u7i-6tb.112xlarge**
| 6,144 | 448 | 2 x 3,600 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 4 x 9,600 GiB | 1,000 | 6,000 | 4,000 | 24,000 |
| **u-6tb1.112xlarge**
| 6,114 | 448 | 2 x 3,600 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-6tb1.56xlarge**
| 6,114 | 224 | 2 x 3,600 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-6tb1.metal**
| 6,114 | 448 | 2 x 3,600 GiB | 1,000 | 6,000 | 2,000 | 12,000 |
| **u-3tb1.56xlarge**
| 3,072 | 224 | 2 x 1,800 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x2iedn.32xlarge**
| 4,096 | 128 | 2 x 2,400 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x2iedn.24xlarge**
| 3,072 | 96 | 2 x 1,800 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x2idn.32xlarge**
| 2,048 | 128 | 2 x 1,200 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x2idn.24xlarge**
| 1,536 | 96 | 2 x 900 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x2idn.16xlarge**
| 1,024 | 64 | 2 x 600 GiB | 500 | 3,750 | 1,000 | 7,500 |
| **x1e.32xlarge**
| 3,904 | 128 | 2 x 2,400 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x1.32xlarge**
| 1,952 | 128 | 2 x 1,200 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **x1.16xlarge**
| 976 | 64 | 1 x 1,200 GiB | 500 | 7,500 | 500 | 7,500 |
| **r7i.48xlarge**
| 1,536 | 192 | 2 x 900 GiB | 750 | 4,500 | 1,500 | 9,000 |
| **r7i.24xlarge**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r7i.16xlarge**
| 512 | 64 | 1 x 615 GiB | 500 | 7,500 | 500 | 7,500 |
| **r7i.12xlarge**
| 384 | 48 | 1 x 460 GiB | 500 | 7,500 | 500 | 7,500 |
| **r7i.8xlarge**
| 256 | 32 | 1 x 320 GiB | 500 | 7,500 | 500 | 7,500 |
| **r6i.32xlarge**
| 1,024 | 128 | 1 x 1,200 GiB | 500 | 7,500 | 500 | 7,500 |
| **r6i.24xlarge**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r6i.16xlarge**
| 512 | 64 | 1 x 615 GiB | 500 | 7,500 | 500 | 7,500 |
| **r6i.12xlarge**
| 384 | 48 | 1 x 460 GiB | 500 | 7,500 | 500 | 7,500 |
| **r6i.8xlarge**
| 256 | 32 | 1 x 320 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5.24xlarge**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5.16xlarge**
| 512 | 64 | 1 x 615 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5.12xlarge**
| 384 | 48 | 1 x 460 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5.8xlarge**
| 256 | 32 | 1 x 320 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5.metal**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5b.24xlarge**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5b.16xlarge**
| 512 | 64 | 1 x 615 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5b.12xlarge**
| 384 | 48 | 1 x 460 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5b.8xlarge**
| 256 | 32 | 1 x 320 GiB | 500 | 7,500 | 500 | 7,500 |
| **r5b.metal**
| 768 | 96 | 1 x 920 GiB | 500 | 7,500 | 500 | 7,500 |
| **r4.16xlarge**
| 488 | 64 | 1 x 585 GiB | 500 | 7,500 | 500 | 7,500 |
| **r4.8xlarge**
| 244 | 32 | 1 x 300 GiB | 500 | 7,500 | 500 | 7,500 |
| **r3.8xlarge**
| 244 | 32 | 1 x 300 GiB | 500 | 7,500 | 500 | 7,500 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp3) storage with LVM** | **Configured throughput per volume (MiB/s)** | **Configured IOPS per volume** | **Total throughput (MiB/s)** | **Total IOPS** |
| **x2iedn.4xlarge**
| 512 | 16 | 1 x 585 GiB | 125 | 3,000 | 125 | 3,000 |
| **x2iedn.2xlarge**
| 256 | 8 | 1 x 295 GiB | 125 | 3,000 | 125 | 3,000 |
| **x2iedn.xlarge**
| 128 | 4 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.4xlarge**
| 488 | 16 | 1 x 585 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.2xlarge**
| 244 | 8 | 1 x 295 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.xlarge**
| 122 | 4 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r7i.4xlarge**
| 128 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r7i.2xlarge**
| 64 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 |
| **r6i.4xlarge**
| 128 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r6i.2xlarge**
| 64 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5.4xlarge**
| 128 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5.2xlarge**
| 64 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5b.4xlarge**
| 128 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5b.2xlarge**
| 64 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 |
| **r4.4xlarge**
| 122 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r4.2xlarge**
| 61 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 |
| **r3.4xlarge**
| 122 | 16 | 1 x 150 GiB | 125 | 3,000 | 125 | 3,000 |
| **r3.2xlarge**
| 61 | 8 | 1 x 80 GiB | 125 | 3,000 | 125 | 3,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. \*\*\*gp3 based configurations are only supported in production for Nitro based instances, not for Xen based instances as SAP HANA HCMT storage tests may not meet the minimum required KPI for log writes. gp3 for HANA logs Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp3) storage with LVM** | **Configured throughput per volume (MiB/s)** | **Configured IOPS per volume** | **Total throughput (MiB/s)** | **Total IOPS** |
| **u-24tb1.112xlarge**
| 24,576 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-24tb1.metal**
| 24,576 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-18tb1.112xlarge**
| 18,432 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-18tb1.metal**
| 18,432 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-12tb1.112xlarge**
| 12,228 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-12tb1.metal**
| 12,228 | 448 | 1 x 512 GiB | 500 | 3000 | 500 | 3,000 |
| **u-9tb1.112xlarge**
| 9,216 | 448 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **u-9tb1.metal**
| 9,216 | 448 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **u7in-24tb.112xlarge**
| 24,576 | 896 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u7in-16tb.112xlarge**
| 16,384 | 896 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u7i-12tb.224xlarge**
| 12,288 | 896 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u7i-8tb.112xlarge**
| 8,192 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u7i-6tb.112xlarge**
| 6,144 | 448 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 1 x 512 GiB | 500 | 3,000 | 500 | 3,000 |
| **u-6tb1.112xlarge**
| 6,114 | 448 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **u-6tb1.56xlarge**
| 6,114 | 224 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **u-6tb1.metal**
| 6,114 | 448 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **u-3tb1.56xlarge**
| 3,072 | 224 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x2iedn.32xlarge**
| 4,096 | 128 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x2iedn.24xlarge**
| 3,072 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x2idn.32xlarge**
| 2,048 | 128 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x2idn.24xlarge**
| 1,536 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x2idn.16xlarge**
| 1,024 | 64 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x1e.32xlarge**
| 3,904 | 128 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x1.32xlarge**
| 1,952 | 128 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **x1.16xlarge**
| 976 | 64 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r7i.48xlarge**
| 1,536 | 192 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r7i.24xlarge**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r7i.16xlarge**
| 512 | 64 | 1 x 256 GiB | 300 | 3,000 | 300 | 3,000 |
| **r7i.12xlarge**
| 384 | 48 | 1 x 192 GiB | 300 | 3,000 | 300 | 3,000 |
| **r7i.8xlarge**
| 256 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 |
| **r6i.32xlarge**
| 1,024 | 128 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r6i.24xlarge**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r6i.16xlarge**
| 512 | 64 | 1 x 256 GiB | 300 | 3,000 | 300 | 3,000 |
| **r6i.12xlarge**
| 384 | 48 | 1 x 192 GiB | 300 | 3,000 | 300 | 3,000 |
| **r6i.8xlarge**
| 256 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5.24xlarge**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5.16xlarge**
| 512 | 64 | 1 x 256 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5.12xlarge**
| 384 | 48 | 1 x 192 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5.8xlarge**
| 256 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5.metal**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5b.24xlarge**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5b.16xlarge**
| 512 | 64 | 1 x 256 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5b.12xlarge**
| 384 | 48 | 1 x 192 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5b.8xlarge**
| 256 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 |
| **r5b.metal**
| 768 | 96 | 1 x 512 GiB | 300 | 3,000 | 300 | 3,000 |
| **r4.16xlarge**
| 488 | 64 | 1 x 256 GiB | 300 | 3,000 | 300 | 3,000 |
| **r4.8xlarge**
| 244 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 |
| **r3.8xlarge**
| 244 | 32 | 1 x 128 GiB | 300 | 3,000 | 300 | 3,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **General Purpose SSD (gp3) storage with LVM** | **Configured throughput per volume (MiB/s)** | **Configured IOPS per volume** | **Total throughput (MiB/s)** | **Total IOPS** |
| **x2iedn.4xlarge**
| 512 | 16 | 1 x 245 GiB | 125 | 3,000 | 125 | 3,000 |
| **x2iedn.2xlarge**
| 256 | 8 | 1 x 125 GiB | 125 | 3,000 | 125 | 3,000 |
| **x2iedn.xlarge**
| 128 | 4 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.4xlarge**
| 488 | 16 | 1 x 245 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.2xlarge**
| 244 | 8 | 1 x 125 GiB | 125 | 3,000 | 125 | 3,000 |
| **x1e.xlarge**
| 122 | 4 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r7i.4xlarge**
| 128 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r7i.2xlarge**
| 64 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 |
| **r6i.4xlarge**
| 128 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r6i.2xlarge**
| 64 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5.4xlarge**
| 128 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5.2xlarge**
| 64 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5b.4xlarge**
| 128 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r5b.2xlarge**
| 64 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 |
| **r4.4xlarge**
| 122 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r4.2xlarge**
| 61 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 |
| **r3.4xlarge**
| 122 | 16 | 1 x 64 GiB | 125 | 3,000 | 125 | 3,000 |
| **r3.2xlarge**
| 61 | 8 | 1 x 32 GiB | 125 | 3,000 | 125 | 3,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. \*\*\*gp3 based configurations are only supported in production for Nitro based instances, not for Xen based instances as SAP HANA HCMT storage tests may not meet the minimum required KPI for log writes. General Purpose SSD (`gp2`) volumes created or modified after 12/03/2018 have a throughput maximum between 128 MiB/s and 250 MiB/s depending on volume size. Volumes greater than 170 GiB and below 334 GiB deliver a maximum throughput of 250 MiB/s if burst credits are available. Volumes with 334 GiB and above deliver 250 MiB/s, irrespective of burst credits. For details, see [Amazon EBS Volume Types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md") in the AWS documentation. General Purpose SSD `gp3` volumes deliver a consistent baseline of 3,000 IOPS and 125 MiB/s. You can also purchase additional IOPS (up to 16,000) and throughput (up to 1,000 MiB/s). While we recommend you to use the configurations shown in this guide, gp3 volumes provide flexibility to customize SAP HANA’s storage configuration (IOPS and throughput) according to your needs and usage. The **minimum** gp3 configuration required to meet SAP HANA KPIs are the following:
| Storage Area | IOPS | Throughput | | --- | --- | --- |
| **SAP HANA Data** | 7,000 | 425 MiB/s | | **SAP HANA Logs** | 3,000 | 275 MiB/s | ## `io1`, `io2`, and `io2 Block Express` for HANA io1 for HANA data Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **u-24tb1.112xlarge**
| 24,576 | 448 | 6 x 4,800 GiB | 3,000 | 3,000 | 18,000 | | **u-24tb1.metal**
| 24,576 | 448 | 6 x 4,800 GiB | 3,000 | 3,000 | 18,000 | | **u-18tb1.112xlarge**
| 18,432 | 448 | 6 x 3,600 GiB | 3,000 | 3,000 | 18,000 | | **u-18tb1.metal**
| 18,432 | 448 | 6 x 3,600 GiB | 3,000 | 3,000 | 18,000 | | **u-12tb1.112xlarge**
| 12,288 | 448 | 6 x 2,400 GiB | 3,000 | 2,000 | 12,000 | | **u-12tb1.metal**
| 12,288 | 448 | 6 x 2,400 GiB | 3,000 | 2,000 | 12,000 | | **u-9tb1.112xlarge**
| 9,216 | 448 | 6 x 1,800 GiB | 3,000 | 2,000 | 12,000 | | **u-9tb1.metal**
| 9,216 | 448 | 6 x 1,800 GiB | 3,000 | 2,000 | 12,000 | | **u7in-24tb.112xlarge**
| 24,576 | 896 | 6 x 4,800 GiB | 3,000 | 3,000 | 18,000 | | **u7in-16tb.112xlarge**
| 16,384 | 896 | 6 x 3,200 GiB | 3,000 | 3,000 | 18,000 | | **u7i-12tb.224xlarge**
| 12,288 | 896 | 6 x 2,400 GiB | 3,000 | 3,000 | 18,000 | | **u7i-8tb.112xlarge**
| 8,192 | 448 | 6 x 1,600 GiB | 3,000 | 2,000 | 12,000 | | **u7i-6tb.112xlarge**
| 6,144 | 448 | 6 x 1,200 GiB | 3,000 | 2,000 | 12,000 | | **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 6 x 6,400 GiB | 3,000 | 3,000 | 18,000 | | **u-6tb1.112xlarge**
| 6,144 | 448 | 6 x 1,200 GiB | 3,000 | 2,000 | 12,000 | | **u-6tb1.56xlarge**
| 6,144 | 224 | 6 x 1,200 GiB | 3,000 | 2,000 | 12,000 | | **u-6tb1.metal**
| 6,144 | 448 | 6 x 1,200 GiB | 3,000 | 2,000 | 12,000 | | **u-3tb1.56xlarge**
| 3,072 | 224 | 3 x 1,200 GiB | 1,500 | 3,000 | 9,000 | | **x2iedn.32xlarge**
| 4,096 | 128 | 2 x 2,400 GiB | 1,000 | 4,500 | 9,000 | | **x2iedn.24xlarge**
| 3,072 | 96 | 2 x 1,800 GiB | 1,000 | 4,500 | 9,000 | | **x2idn.32xlarge**
| 2,048 | 128 | 2 x 1,200 GiB | 1,000 | 4,500 | 9,000 | | **x2idn.24xlarge**
| 1,536 | 96 | 2 x 900 GiB | 1,000 | 4,500 | 9,000 | | **x2idn.16xlarge**
| 1,024 | 64 | 2 x 600 GiB | 1,000 | 3,750 | 7,500 | | **x1e.32xlarge**
| 3,904 | 128 | 3 x 1,600 GiB | 1,500 | 3,000 | 9,000 | | **x1.32xlarge**
| 1,952 | 128 | 3 x 800 GiB | 1,500 | 3,000 | 9,000 | | **x1.16xlarge**
| 976 | 64 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r7i.48xlarge**
| 1,536 | 192 | 1 x 1,800 GiB | 500 | 7,500 | 7,500 | | **r7i.24xlarge**
| 768 | 96 | 1 x 900 GiB | 500 | 7,500 | 7,500 | | **r7i.16xlarge**
| 512 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r7i.12xlarge**
| 384 | 48 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r7i.8xlarge**
| 256 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r6i.32xlarge**
| 1,024 | 128 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r6i.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r6i.16xlarge**
| 512 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r6i.12xlarge**
| 384 | 48 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r6i.8xlarge**
| 256 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r5.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r5.16xlarge**
| 512 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r5.12xlarge**
| 384 | 48 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r5.8xlarge**
| 256 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r5.metal**
| 768 | 96 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r5b.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r5b.16xlarge**
| 512 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r5b.12xlarge**
| 384 | 48 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r5b.8xlarge**
| 256 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r5b.metal**
| 768 | 96 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r4.16xlarge**
| 488 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r4.8xlarge**
| 244 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r3.8xlarge**
| 244 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x2iedn.4xlarge**
| 512 | 16 | 1 x 600 GiB | 500 | 2,000 | 2,000 | | **x2iedn.2xlarge**
| 256 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **x2iedn.xlarge**
| 128 | 4 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **x1e.4xlarge**
| 488 | 16 | 1 x 600 GiB | 500\*\* | 2,000 | 2,000 | | **x1e.2xlarge**
| 244 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **x1e.xlarge**
| 122 | 4 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r7i.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r7i.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 7,500 | 7,500 | | **r6i.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r6i.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5b.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5b.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r4.4xlarge**
| 122 | 16 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r4.2xlarge**
| 61 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r3.4xlarge**
| 122 | 16 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r3.2xlarge**
| 61 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. io1 for HANA logs Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **u-24tb1.112xlarge**
| 24,576 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-24tb1.metal**
| 24,576 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-18tb1.112xlarge**
| 18,432 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-18tb1.metal**
| 18,432 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-12tb1.112xlarge**
| 12,288 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-12tb1.metal**
| 12,288 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-9tb1.112xlarge**
| 9,216 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-9tb1.metal**
| 9,216 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7in-24tb.112xlarge**
| 24,576 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7in-16tb.112xlarge**
| 16,384 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-12tb.224xlarge**
| 12,288 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-8tb.112xlarge**
| 8,192 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-6tb.112xlarge**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.112xlarge**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.56xlarge**
| 6,144 | 224 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.metal**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-3tb1.56xlarge**
| 3,072 | 224 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2iedn.32xlarge**
| 4,096 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2iedn.24xlarge**
| 3,072 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.32xlarge**
| 2,048 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.24xlarge**
| 1,536 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.16xlarge**
| 1,024 | 64 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x1e.32xlarge**
| 3,904 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x1.32xlarge**
| 1,952 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x1.16xlarge**
| 976 | 64 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.48xlarge**
| 1,536 | 192 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r7i.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r7i.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.32xlarge**
| 1,024 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r6i.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r6i.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.8xlarge**
| 256 | 32 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.metal**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5b.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5b.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.metal**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r4.16xlarge**
| 488 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r4.8xlarge**
| 244 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r3.8xlarge**
| 244 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x2iedn.4xlarge**
| 512 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **x2iedn.2xlarge**
| 256 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **x2iedn.xlarge**
| 128 | 4 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **x1e.4xlarge**
| 488 | 16 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **x1e.2xlarge**
| 244 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **x1e.xlarge**
| 122 | 4 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **r7i.4xlarge**
| 128 | 16 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r7i.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r6i.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r6i.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5b.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5b.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r4.4xlarge**
| 122 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r4.2xlarge**
| 61 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **r3.4xlarge**
| 122 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r3.2xlarge**
| 61 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum achievable throughput when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For more information, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md"). io2 for HANA data Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x1e.32xlarge**
| 3,904 | 128 | 3 x 1,600 GiB | 1,500 | 3,000 | 9,000 | | **x1.32xlarge**
| 1,952 | 128 | 3 x 800 GiB | 1,500 | 3,000 | 9,000 | | **x1.16xlarge**
| 976 | 64 | 1 x 1,200 GiB | 500 | 7,500 | 7,500 | | **r4.16xlarge**
| 488 | 64 | 1 x 600 GiB | 500 | 7,500 | 7,500 | | **r4.8xlarge**
| 244 | 32 | 1 x 300 GiB | 500 | 7,500 | 7,500 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x1e.4xlarge**
| 488 | 16 | 1 x 600 GiB | 500\*\* | 2,000 | 2,000 | | **x1e.2xlarge**
| 244 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **x1e.xlarge**
| 122 | 4 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r4.4xlarge**
| 122 | 16 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r4.2xlarge**
| 61 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r3.4xlarge**
| 122 | 16 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | | **r3.2xlarge**
| 61 | 8 | 1 x 300 GiB | 500\*\* | 2,000 | 2,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. io2 for HANA logs Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x1e.32xlarge**
| 3,904 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x1.32xlarge**
| 1,952 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x1.16xlarge**
| 976 | 64 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r4.16xlarge**
| 488 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r4.8xlarge**
| 244 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x1e.4xlarge**
| 488 | 16 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **x1e.2xlarge**
| 244 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **x1e.xlarge**
| 122 | 4 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **r4.4xlarge**
| 122 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r4.2xlarge**
| 61 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | | **r3.4xlarge**
| 122 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r3.2xlarge**
| 61 | 8 | 1 x 260 GiB | 250\*\* | 1,000 | 1,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum achievable throughput when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For more information, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md"). io2 Block Express for HANA data Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **u-24tb1.112xlarge**
| 24,576 | 448 | 2 x 14,400 GiB | 4,500 | 9,000 | 18,000 | | **u-24tb1.metal**
| 24,576 | 448 | 2 x 14,400 GiB | 4,500 | 9,000 | 18,000 | | **u-18tb1.112xlarge**
| 18,432 | 448 | 2 x 10,800 GiB | 4,500 | 9,000 | 18,000 | | **u-18tb1.metal**
| 18,432 | 448 | 2 x 10,800 GiB | 4,500 | 9,000 | 18,000 | | **u-12tb1.112xlarge**
| 12,288 | 448 | 2 x 7,200 GiB | 3,000 | 6,000 | 12,000 | | **u-12tb1.metal**
| 12,288 | 448 | 2 x 7,200 GiB | 3,000 | 6,000 | 12,000 | | **u-9tb1.112xlarge**
| 9,216 | 448 | 2 x 5,400 GiB | 3,000 | 6,000 | 12,000 | | **u-9tb1.metal**
| 9,216 | 448 | 2 x 5,400 GiB | 3,000 | 6,000 | 12,000 | | **u7in-24tb.112xlarge**
| 24,576 | 896 | 2 x 14,400 GiB | 4,500 | 9,000 | 18,000 | | **u7in-16tb.112xlarge**
| 16,384 | 896 | 2 x 9,600 GiB | 4,500 | 9,000 | 18,000 | | **u7i-12tb.224xlarge**
| 12,288 | 896 | 2 x 7,200 GiB | 3,000 | 6,000 | 12,000 | | **u7i-8tb.112xlarge**
| 8,192 | 448 | 2 x 4,800 GiB | 3,000 | 6,000 | 12,000 | | **u7i-6tb.112xlarge**
| 6,144 | 448 | 2 x 3,600 GiB | 3,000 | 6,000 | 12,000 | | **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 4 x 9,600 GiB | 9,000 | 9,000 | 36,000 | | **u-6tb1.112xlarge**
| 6,144 | 448 | 2 x 3,600 GiB | 3,000 | 6,000 | 12,000 | | **u-6tb1.56xlarge**
| 6,144 | 224 | 2 x 3,600 GiB | 3,000 | 6,000 | 12,000 | | **u-6tb1.metal**
| 6,144 | 448 | 2 x 3,600 GiB | 3,000 | 6,000 | 12,000 | | **u-3tb1.56xlarge**
| 3,072 | 224 | 2 x 1,800 GiB | 2,250 | 4,500 | 9,000 | | **x2iedn.32xlarge**
| 4,096 | 128 | 2 x 2,400 GiB | 2,250 | 4,500 | 9,000 | | **x2iedn.24xlarge**
| 3,072 | 96 | 2 x 1,800 GiB | 2,250 | 4,500 | 9,000 | | **x2idn.32xlarge**
| 2,048 | 128 | 2 x 1,200 GiB | 2,250 | 4,500 | 9,000 | | **x2idn.24xlarge**
| 1,536 | 96 | 2 x 900 GiB | 1,875 | 3,750 | 7,500 | | **x2idn.16xlarge**
| 1,024 | 64 | 2 x 600 GiB | 1,875 | 3,750 | 7,500 | | **r7i.48xlarge**
| 1,536 | 192 | 1 x 1,800 GiB | 1,875 | 7,500 | 7,500 | | **r7i.24xlarge**
| 768 | 96 | 1 x 900 GiB | 1,875 | 7,500 | 7,500 | | **r7i.16xlarge**
| 512 | 64 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r7i.12xlarge**
| 384 | 48 | 1 x 300 GiB | 1,875 | 7,500 | 7,500 | | **r7i.8xlarge**
| 256 | 32 | 1 x 300 GiB | 1,875 | 7,500 | 7,500 | | **r6i.32xlarge**
| 1,024 | 128 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | | **r6i.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | | **r6i.16xlarge**
| 512 | 64 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r6i.12xlarge**
| 384 | 48 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r6i.8xlarge**
| 256 | 32 | 1 x 300 GiB | 1,875 | 7,500 | 7,500 | | **r5.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | | **r5.16xlarge**
| 512 | 64 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r5.12xlarge**
| 384 | 48 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r5.8xlarge**
| 256 | 32 | 1 x 300 GiB | 1,875 | 7,500 | 7,500 | | **r5.metal**
| 768 | 96 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | | **r5b.24xlarge**
| 768 | 96 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | | **r5b.16xlarge**
| 512 | 64 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r5b.12xlarge**
| 384 | 48 | 1 x 600 GiB | 1,875 | 7,500 | 7,500 | | **r5b.8xlarge**
| 256 | 32 | 1 x 300 GiB | 1,875 | 7,500 | 7,500 | | **r5b.metal**
| 768 | 96 | 1 x 1,200 GiB | 1,875 | 7,500 | 7,500 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x2iedn.4xlarge**
| 512 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **x2iedn.2xlarge**
| 256 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **x2iedn.xlarge**
| 128 | 4 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r7i.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r7i.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r6i.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r6i.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5b.4xlarge**
| 128 | 16 | 1 x 300 GiB | 500 | 2,000 | 2,000 | | **r5b.2xlarge**
| 64 | 8 | 1 x 300 GiB | 500 | 2,000 | 2,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. io2 Block Express for HANA logs Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **u-24tb1.112xlarge**
| 24,576 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-24tb1.metal**
| 24,576 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-18tb1.112xlarge**
| 18,432 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-18tb1.metal**
| 18,432 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-12tb1.112xlarge**
| 12,288 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-12tb1.metal**
| 12,288 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-9tb1.112xlarge**
| 9,216 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-9tb1.metal**
| 9,216 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7in-24tb.112xlarge**
| 24,576 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7in-16tb.112xlarge**
| 16,384 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-12tb.224xlarge**
| 12,288 | 896 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-8tb.112xlarge**
| 8,192 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7i-6tb.112xlarge**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.112xlarge**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.56xlarge**
| 6,144 | 224 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-6tb1.metal**
| 6,144 | 448 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **u-3tb1.56xlarge**
| 3,072 | 224 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2iedn.32xlarge**
| 4,096 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2iedn.24xlarge**
| 3,072 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.32xlarge**
| 2,048 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.24xlarge**
| 1,536 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **x2idn.16xlarge**
| 1,024 | 64 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.48xlarge**
| 1,536 | 192 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r7i.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r7i.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r7i.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.32xlarge**
| 1,024 | 128 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r6i.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r6i.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r6i.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5.metal**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5b.24xlarge**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | | **r5b.16xlarge**
| 512 | 64 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.12xlarge**
| 384 | 48 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.8xlarge**
| 256 | 32 | 1 x 260 GiB | 500 | 2,000 | 2,000 | | **r5b.metal**
| 768 | 96 | 1 x 525 GiB | 500 | 2,000 | 2,000 | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Provisioned IOPS SSD (io1/io2) storage with LVM** | **Total maximum throughput (MiB/s)** | **Provisioned IOPS per volume** | **Total provisioned IOPS** | | **x2iedn.4xlarge**
| 512 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **x2iedn.2xlarge**
| 256 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **x2iedn.xlarge**
| 128 | 4 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r7i.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r7i.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r6i.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r6i.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5b.4xlarge**
| 128 | 16 | 1 x 260 GiB | 250 | 1,000 | 1,000 | | **r5b.2xlarge**
| 64 | 8 | 1 x 260 GiB | 250 | 1,000 | 1,000 | <br>• Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core. + This value represents the maximum throughput that could be achieved when striping multiple EBS volumes. Actual throughput depends on the instance type. Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the AWS documentation. ###### Note io2 Block Express volume supports up to 4000 MiB/s throughput per volume with 16,000 IOPS at 256 KiB I/O size or with 64,000 IOPS at 16 KiB I/O size. The maximum throughput value represented in the _Total maximum throughput_ column = Total provisioned IOPS \* 256 KiB I/O. To increase the throughput, increase the provisioned IOPS. ## Root, binaries, shared, and backup volumes In addition to the SAP HANA data and log volumes, we recommend the following storage configuration for root, SAP binaries, and SAP HANA shared and backup volumes: Certified for production use| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Root volume** | **SAP binaries** | **SAP HANA shared**\*\* | **SAP HANA backup**\*\*\* | | **u-24tb1.112xlarge**
| 24,576 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u-24tb1.metal**
| 24,576 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u-18tb1.112xlarge**
| 18,432 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u-18tb1.metal**
| 18,432 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u-12tb1.112xlarge**
| 12,288 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 16,384 GiB | | **u-12tb1.metal**
| 12,288 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 16,384 GiB | | **u-9tb1.112xlarge**
| 9,216 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 16,384 GiB | | **u-9tb1.metal**
| 9,216 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 16,384 GiB | | **u7in-24tb.112xlarge**
| 24,576 | 896 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u7in-16tb.112xlarge**
| 16,384 | 896 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u7i-12tb.112xlarge**
| 12,288 | 896 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 2 x 16,384 GiB | | **u7i-8tb.112xlarge**
| 8,192 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 16,384 GiB | | **u7i-6tb.224xlarge**
| 6,144 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 12,288 GiB | | **u7inh-32tb.480xlarge**
| 32,768 | 1,920 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 3 x 16,384 GiB | | **u-6tb1.112xlarge**
| 6,144 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 12,288 GiB | | **u-6tb1.56xlarge**
| 6,144 | 224 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 12,288 GiB | | **u-6tb1.metal**
| 6,144 | 448 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 12,288 GiB | | **u-3tb1.56xlarge**
| 3,072 | 224 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 6,144 GiB | | **x2iedn.32xlarge**
| 4,096 | 128 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 8,192 GiB | | **x2iedn.24xlarge**
| 3,072 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 6,144 GiB | | **x2idn.32xlarge**
| 2,048 | 128 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 4,096 GiB | | **x2idn.24xlarge**
| 1,536 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 3,096 GiB | | **x2idn.16xlarge**
| 1,024 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **x1e.32xlarge**
| 3,904 | 128 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 8,192 GiB | | **x1.32xlarge**
| 1,952 | 128 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 4,096 GiB | | **x1.16xlarge**
| 976 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r7i.48xlarge**
| 1,536 | 192 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 3,096 GiB | | **r7i.24xlarge**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r7i.16xlarge**
| 512 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r7i.12xlarge**
| 384 | 48 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r7i.8xlarge**
| 256 | 32 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 1,024 GiB | | **r6i.32xlarge**
| 1,024 | 128 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r6i.24xlarge**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r6i.16xlarge**
| 512 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r6i.12xlarge**
| 384 | 48 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r6i.8xlarge**
| 256 | 32 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 1,024 GiB | | **r5.24xlarge**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r5.16xlarge**
| 512 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r5.12xlarge**
| 384 | 48 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r5.8xlarge**
| 256 | 32 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 1,024 GiB | | **r5.metal**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r5b.24xlarge**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r5b.16xlarge**
| 512 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r5b.12xlarge**
| 384 | 48 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r5b.8xlarge**
| 256 | 32 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 1,024 GiB | | **r5b.metal**
| 768 | 96 | 1 x 50 GiB | 1 x 50 GiB | 1 x 1,024 GiB | 1 x 2,048 GiB | | **r4.16xlarge**
| 488 | 64 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **r4.8xlarge**
| 244 | 32 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 1,024 GiB | Supported for nonproduction use only| **Instance type**
| **Memory (GiB)** | **vCPUs / logical processors**\* | **Root volume** | **SAP binaries** | **SAP HANA shared**\*\* | **SAP HANA backup**\*\*\* | | **x2iedn.4xlarge**
| 512 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **x2iedn.2xlarge**
| 256 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **x2iedn.xlarge**
| 128 | 4 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **x1e.4xlarge**
| 488 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 512 GiB | 1 x 1,024 GiB | | **x1e.2xlarge**
| 244 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **x1e.xlarge**
| 122 | 4 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r7i.4xlarge**
| 128 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r7i.2xlarge**
| 64 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r6i.4xlarge**
| 128 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r6i.2xlarge**
| 64 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r5.4xlarge**
| 128 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r5.2xlarge**
| 64 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r5b.4xlarge**
| 128 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r5b.2xlarge**
| 64 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r4.4xlarge**
| 122 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r4.2xlarge**
| 61 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r3.4xlarge**
| 122 | 16 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | | **r3.2xlarge**
| 61 | 8 | 1 x 50 GiB | 1 x 50 GiB | 1 x 300 GiB | 1 x 512 GiB | _\* Each logical processor offered by Amazon EC2 High Memory Instances is a hyperthread on a physical CPU core._ _\*\* In a multi-node architecture, the SAP HANA NFS shared volume is provisioned only once on the master node._ _\*\*\* In a multi-node architecture, the SAP HANA backup volume can be deployed as NFS or Amazon EFS. The size of the SAP HANA NFS backup volume is multiplied by the number of nodes. The SAP HANA backup volume is provisioned only once on the master node, and NFS is mounted on the worker nodes. There is no provision needed for [Amazon EFS](https://aws.amazon.com/efs/features/ "https://aws.amazon.com/efs/features/") as it is built to scale on demand, growing and shrinking automatically as files are added and removed._ ## Backup options For SAP HANA backup, you can choose file-based backup with storage configuration recommended in this guide or [AWS Backint for SAP HANA](https://aws.amazon.com/backint-agent/ "https://aws.amazon.com/backint-agent/") to backup your database on Amazon S3. AWS Backint Agent for SAP HANA is an SAP-certified backup and restore solution for SAP HANA workloads running on Amazon EC2 instances. With AWS Backint for SAP HANA as your backup solution, provisioning additional Amazon EBS storage volumes or Amazon EFS file systems becomes optional. For more details, see [AWS Backint Agent for SAP HANA](https://aws.amazon.com/backint-agent/ "https://aws.amazon.com/backint-agent/"). For Disaster Recovery (DR) purposes, you can also automate the creation of application-consistent EBS snapshots for SAP HANA using Amazon Data Lifecycle Manager and the AWS Systems Manager document for SAP HANA. EBS snapshots make it easy to maintain a copy of your SAP HANA databases in another Region or account. Restoring an entire SAP HANA database from an EBS snapshot can take longer than other backups. However, you can reduce the restore time by enabling the EBS snapshots for [Amazon EBS fast snapshot restore](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md"). We recommend that you use EBS snapshots to supplement your existing backups with AWS Backint Agent, and to use Amazon Data Lifecycle Manager to automate the copying and retention of EBS snapshots in DR Regions as needed. For more information, see [Amazon EBS snapshots for SAP HANA](ebs-sap-hana.md "ebs-sap-hana.md"). For single-node deployment, we recommend using [Amazon EBS](https://aws.amazon.com/ebs/features/ "https://aws.amazon.com/ebs/features/") Throughput Optimized HDD (`st1`) volumes for SAP HANA to perform file-based backup. This volume type provides low-cost magnetic storage designed for large sequential workloads. SAP HANA uses sequential I/O with large blocks to back up the database, so `st1` volumes provide a low-cost, high-performance option for this scenario. To learn more about `st1` volumes, see [Amazon EBS Volume Types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md"). The SAP HANA backup volume size is designed to provide optimal baseline and burst throughput as well as the ability to hold several backup sets. Holding multiple backup sets inthe backup volume makes it easier to recover your database if necessary. You may resize your SAP HANA backup volume after initial setup if needed. To learn more about resizing your Amazon EBS volumes, see [Expanding the Storage Size of an EBS Volume on Linux](../../../AWSEC2/latest/UserGuide/ebs-expand-volume.md "../../../AWSEC2/latest/UserGuide/ebs-expand-volume.md"). For multi-node deployment, we recommend using [Amazon EFS](https://aws.amazon.com/efs/features/ "https://aws.amazon.com/efs/features/") for SAP HANA to perform file-based backup. It can support performance over 10 GB/sec and over 500,000 IOPS. The configurations recommended in this guide are used by [AWS Launch Wizard for SAP](https://aws.amazon.com/launchwizard/ "https://aws.amazon.com/launchwizard/").
