# SAP HANA EBS Storage Reference

###### Important

These values serve as a starting point. For guidance on how to size and configure storage for your specific workload, including calculations and striping considerations, refer to [Calculate Requirements](hana-storage-config-ebs.md "hana-storage-config-ebs.md").

###### Topics

- [Certified Instances - General](#general "#general")
- [Certified Instances - High Memory](#_certified_instances_high_memory "#_certified_instances_high_memory")
- [Suitable for Non-Production Use](#_suitable_for_non_production_use "#_suitable_for_non_production_use")

## Certified Instances - General

For systems with less than 2 TiB of memory storage can typically be configured using standard Amazon EBS volumes. gp3 volumes usually balance price and performance for a variety of workloads, while io2 volumes should be considered when higher durability is required or to improve startup and EBS snapshot restore times.

Sample layouts are provided for the following memory configurations:

Memory sizes: [256 GiB](#mem-256 "#mem-256"), [384 GiB](#mem-384 "#mem-384"), [488 GiB](#mem-512 "#mem-512"), [512 GiB](#mem-512 "#mem-512"), [768 GiB](#mem-768 "#mem-768"), [976 GiB](#mem-1024 "#mem-1024"), [1024 GiB](#mem-1024 "#mem-1024"), [1536 GiB](#mem-1536 "#mem-1536"), [2 TiB](#mem-2tb "#mem-2tb")

### 256 GiB Memory Systems

Applicable Instance Types: **r8i.8xlarge**, **r7i.8xlarge**, **r6i.8xlarge**, **r5.8xlarge**, **r5b.8xlarge**, **x2iedn.2xlarge**, **r4.8xlarge**, **r3.8xlarge1**, **x1e.2xlarge1**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 300               | 7,300       | 500                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 100               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 256               | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

1 Xen instance types. We suggest migrating to a Nitro instance type.

### 384 GiB Memory Systems

Applicable Instance Types: **r8i.12xlarge**, **r7i.12xlarge**, **r6i.12xlarge**, **r5.12xlarge**, **r5b.12xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 500               | 7,400       | 500                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 200               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 384               | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 488 GiB / 512 GiB Memory Systems

Applicable Instance Types: **r8i.16xlarge**, **r7i.16xlarge**, **r6i.16xlarge**, **r5.16xlarge**, **r5b.16xlarge**, **x2iedn.4xlarge**, **r4.16xlarge**, **x1e.4xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 600               | 7,400       | 500                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 300               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 512               | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 768 GiB Memory Systems

Applicable Instance Types: **r8i.24xlarge**, **r7i.24xlarge**, **r6i.24xlarge**, **r5.24xlarge**, **r5.metal**, **r5b.24xlarge**, **r5b.metal**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 900               | 7,500       | 625                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 400               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 768               | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 976 GiB / 1024 GiB Memory Systems

Applicable Instance Types: **x2idn.16xlarge**, **r6i.32xlarge**, **x1.16xlarge1**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 1,200             | 7,700       | 625                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

1 Xen instance types. We suggest migrating to a Nitro instance type.

### 1,536 GiB Memory Systems

Applicable Instance Types: **r8i.48xlarge**, **x2idn.24xlarge**, **r7i.48xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 1,800             | 7,900       | 750                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 2 TiB Memory Systems

Applicable Instance Types: **x2idn.32xlarge**, **x1.32xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 2,500             | 8,100       | 875                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

## Certified Instances - High Memory

Storage configuration for high memory systems requires careful planning to meet increased I/O demands. Multiple EBS volumes in striped configurations and/or io2 may be required to meet the higher IOPs and throughput demands, particularly for data volumes. As with smaller systems, durability, startup and snapshot restore times should also be considered.

Sample layouts are provided for the following memory configurations:

Memory sizes: [3 TiB](#mem-3tb "#mem-3tb"), [4 TiB](#mem-4tb "#mem-4tb"), [6 TiB](#mem-6tb "#mem-6tb"), [8 TiB](#mem-8tb "#mem-8tb"), [9 TiB](#mem-9tb "#mem-9tb"), [12 TiB](#mem-12tb "#mem-12tb"), [16 TiB](#mem-16tb "#mem-16tb"), [18 TiB](#mem-18tb "#mem-18tb"), [24 TiB](#mem-24tb "#mem-24tb"), [32 TiB](#mem-32tb "#mem-32tb")

### 3 TiB Memory Systems

Applicable Instance Types: **r8i.96xlarge**, **x2iedn.24xlarge**, **u-3tb1.56xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                  | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| HANA Data            | 3,700             | 8,600       | 1,125                    | gp3/io2            | • **gp3**: 2 x 1,650 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 4,300 IOPS, 625 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required                                                                                                                          |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                       | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                       | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 4 TiB Memory Systems

Applicable Instance Types: **x2iedn.32xlarge**, **x1e.32xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                  | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| HANA Data            | 4,900             | 9,000       | 1,250                    | gp3/io2            | • **gp3**: 2 x 2,450 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 4,500 IOPS, 625 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required                                                                                                                          |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                       | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                       | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 6 TiB Memory Systems

Applicable Instance Types: **u-6tb1.112xlarge**, **u-6tb1.56xlarge**, **u-6tb1.metal**, **u7i-6tb.112xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                  | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                       |                                                                                                                                        |
| HANA Data            | 7,300             | 10,000      | 1,625                    | gp3/io2            | • **gp3**: 2 x 3,650 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 5,000 IOPS, 875 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required                                                                                                                          |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                       | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                       | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 8 TiB Memory Systems

Applicable Instance Types: **u7i-8tb.112xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                    | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| HANA Data            | 9,800             | 10,900      | 2,000                    | gp3/io2            | • **gp3**: 2 x 4,900 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 5,500 IOPS, 1,000 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required                                                                                                                            |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                         | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                         | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 9 TiB Memory Systems

Applicable Instance Types: **u-9tb1.112xlarge**, **u-9tb1.metal**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                    | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| HANA Data            | 11,100            | 11,300      | 2,000                    | gp3/io2            | • **gp3**: 2 x 5,550 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 5,700 IOPS, 1,000 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 300                      | gp3/io2            | Not Required                                                                                                                            |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                         | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                         | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 12 TiB Memory Systems

Applicable Instance Types: **u-12tb1.112xlarge**, **u-12tb1.metal**, **u7i-12tb.224xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                    | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| HANA Data            | 14,700            | 12,700      | 2,000                    | gp3/io2            | • **gp3**: 2 x 7,350 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 6,400 IOPS, 1,000 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 500                      | gp3/io2            | Not Required                                                                                                                            |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                         | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                         | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 16 TiB Memory Systems

Applicable Instance Types: **u7in-16tb.112xlarge**, **u7in-16tb.224xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                    | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                         |                                                                                                                                        |
| HANA Data            | 19,700            | 14,600      | 2,000                    | gp3/io2            | • **gp3**: 2 x 9,850 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 7,300 IOPS, 1,000 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 500                      | gp3/io2            | Not Required                                                                                                                            |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                         | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                         | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 18 TiB Memory Systems

Applicable Instance Types: **u-18tb1.112xlarge**, **u-18tb1.metal**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration                                                                                                                     | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                                                                                                                                          |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                                                                                                                                          |                                                                                                                                        |
| HANA Data            | 22,100            | 15,500      | 2,000                    | gp3/io2            | • **gp3**: 2 x 11,050 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 7,800 IOPS, 1,000 MB/s Throughput<br>• **io2**: Not Required |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 500                      | gp3/io2            | Not Required                                                                                                                             |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                |                                                                                                                                          | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                                                                                                                                          | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 24 TiB Memory Systems

Applicable Instance Types: **u7in-24tb.224xlarge**, **u-24tb1.metal**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type        | Stripe Configuration                                                                                                                                                                           | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                |                                                                                                                                        |
| HANA Data            | 29,500            | 18,300      | 2,000                    | gp3/io2 (io2 recommended) | • **gp3**: 3 x 10,000 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 6,100 IOPS, 625 MB/s Throughput<br>• **io2**: Not required, but consider striping for backup and start parallelism | Throughput target can be met with 2 stripes for gp3, 3 recommended to reduce volume size.                                              |
| HANA Log             | 500               | 3,000       | 500                      | gp3/io2                   | Not Required                                                                                                                                                                                   |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs                   |                                                                                                                                                                                                | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

### 32 TiB Memory Systems

Applicable Instance Types: **u7inh-32tb.480xlarge**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type        | Stripe Configuration                                                                                                                                                                                             | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                                  |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                                  |                                                                                                                                        |
| HANA Data            | 39,300            | 21,900      | 4,000                    | gp3/io2 (io2 recommended) | • **gp3**: 4 x 9,900 GiB Filesystems. LVM Stripe Size 256 KB. Per Volume - 5,100 IOPS, 1000 MB/s Throughput<br>• **io2**: 3 x 13,100 GiB. LVM Stripe Size 256 KB. Per Volume - 7,300 IOPS, 1,375 MB/s Throughput |                                                                                                                                        |
| HANA Log             | 500               | 3,000       | 500                      | gp3/io2                   | Not Required                                                                                                                                                                                                     |                                                                                                                                        |
| HANA Shared          | 1,024             | 3,000       | 125                      | gp3                       |                                                                                                                                                                                                                  | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs                   |                                                                                                                                                                                                                  | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

## Suitable for Non-Production Use

While not SAP-certified, these configurations are suitable for small non-production environments where cost optimization is a priority. Storage targets listed represent minimum requirements and can be increased to improve performance or meet SAP storage KPIs.

Sample layouts are provided for the following memory configurations:

Memory sizes: [64 GiB](#mem-64 "#mem-64"), [128 GiB](#mem-128 "#mem-128")

### 64 GiB Memory Systems

Applicable Instance Types: **r8i.2xlarge**, **r7i.2xlarge**, **r6i.2xlarge**, **r5.2xlarge**, **r5b.2xlarge**, **r4.2xlarge1**, **r3.2xlarge1**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 100               | 3,000       | 125                      | gp3                | Not required         |                                                                                                                                        |
| HANA Log             | 50                | 3,000       | 125                      | gp3                | Not required         |                                                                                                                                        |
| HANA Shared          | 64                | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

1 Xen instance types. We suggest migrating to a Nitro instance type.

### 128 GiB Memory Systems

Applicable Instance Types: **r8i.4xlarge**, **x2iedn.xlarge**, **r7i.4xlarge**, **r6i.4xlarge**, **r5.4xlarge**, **r5b.4xlarge**, **x1e.xlarge**, **r4.4xlarge1**, **r3.4xlarge1**

Suggested Storage Configuration:

| System Configuration | Target Size (GiB) | Target IOPS | Target Throughput (MB/s) | Target Volume Type | Stripe Configuration | Comments                                                                                                                               |
| -------------------- | ----------------- | ----------- | ------------------------ | ------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Root/OS              | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| SAP Binaries         | 50                | 3,000       | 125                      | gp3                |                      |                                                                                                                                        |
| HANA Data            | 200               | 7,300       | 500                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Log             | 100               | 3,000       | 300                      | gp3/io2            | Not Required         |                                                                                                                                        |
| HANA Shared          | 128               | 3,000       | 125                      | gp3                |                      | For scale out, review formula or use EFS                                                                                               |
| HANA Backup          | -                 | -           | -                        | st1/efs            |                      | Optional and Workload Dependent. Review [HANA Backup](hana-storage-config-ebs.md#hana_backup "hana-storage-config-ebs.md#hana_backup") |

1 Xen instance types. We suggest migrating to a Nitro instance type.
