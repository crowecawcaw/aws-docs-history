# Calculate EBS Storage Requirements for SAP HANA

## Overview

This guide provides storage configuration recommendations for SAP HANA workloads running on Amazon EC2. Learn how to configure Amazon EBS volumes to meet SAP’s storage key performance indicators (KPIs).

SAP HANA stores and processes its data primarily in memory, and provides protection against data loss by saving the data to persistent storage locations. To achieve optimal performance, the storage solution used for SAP HANA data and log volumes should meet SAP’s storage KPI requirements. AWS has worked with SAP to certify both Amazon EBS General Purpose SSD (gp2 and gp3) and Provisioned IOPS SSD (io1, io2 Block Express) storage solutions for SAP HANA workloads.

## New Amazon EBS Storage Guidelines for SAP HANA

This document introduces a memory-based formula approach for storage sizing, replacing previous instance-specific recommendations. This change enables customers to better understand storage configuration logic and maintain greater control over performance optimization decisions.

The new guidance focuses on gp3 and io2 Block Express volumes as the current standard recommendation for all new deployments. While gp2 and io1 volumes remain supported for existing deployments, we recommend gp3 for new implementations due to its predictable performance and cost-effectiveness, with io2 Block Express as the upgrade path for systems requiring additional performance.

###### Note

If your SAP HANA system was deployed using previous guidance, including the use of Launch Wizard, it is not necessary to change the configuration. Existing configurations based on previous recommendations continue to meet the necessary requirements.

## Testing with SAP HANA Hardware and Cloud Measurement Tools

AWS has ensured that the storage configuration guidelines meet the Key Performance Indicators (KPIs) for running SAP HANA. However, for workloads with high performance requirements or those that deviate from the standard recommendation, we strongly recommended validating the performance of your storage configuration with SAP HANA Hardware and Cloud Measurement Tools.

See:

- SAP Note: [2493172 - SAP HANA Hardware and Cloud Measurement Tools](https://me.sap.com/notes/2493172 "https://me.sap.com/notes/2493172")
- SAP Documentation: [SAP HANA Hardware and Cloud Measurement Tools](https://help.sap.com/viewer/product/HANA_HW_CLOUD_TOOLS/latest/en-US "https://help.sap.com/viewer/product/HANA_HW_CLOUD_TOOLS/latest/en-US")

## EBS Storage Volume Configurations

This section provides the formulas and methodology for calculating SAP HANA storage requirements. The calculations factor in memory size and workload characteristics to determine appropriate volume sizing and performance configuration. Adjust these baseline recommendations based on your specific workload requirements and growth projections.

Refer to [SAP HANA EBS Storage Reference](hana-storage-config-reference-layout.md "hana-storage-config-reference-layout.md") for calculated requirements based on available memory.

###### Topics

- [Root and SAP Binary Volumes](#root_and_sap "#root_and_sap")
- [HANA Data Volume](#hana_data "#hana_data")
- [HANA Log Volume](#hana_log "#hana_log")
- [HANA Shared Volume](#hana_shared "#hana_shared")
- [HANA Backup Volume (Optional)](#hana_backup "#hana_backup")
- [When to Stripe Volumes](#_when_to_stripe_volumes "#_when_to_stripe_volumes")

###### Important

Some EC2 Instances Types may include [instance storage](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md"), this storage is ephemeral and must not be used for SAP HANA files. Configure Amazon EBS volumes for all SAP HANA storage requirements.

### Root and SAP Binary Volumes

The root volume contains operating system files, configuration, and logs. The sizing recommendation is suitable for most SAP HANA deployments and sizes, but may vary based on your AMI strategy and non-SAP software requirements. Consider using a separate volume for the `/tmp` filesystem in high-usage environments.

The SAP binaries volume (`default /usr/sap/<SID>/`) contains common SAP executables and binaries.

###### Storage Type

Use gp3 volumes for root storage. The baseline performance characteristics meet operating system requirements.

**Size Calculation**

```
root_and_sap_volume_size = 50 GiB
```

**IOPS Formula**

```
root_and_sap_iops_target = 3000 (fixed)
```

**Throughput Formula**

```
root_and_sap_throughput_target = 125 MB/s (fixed)
```

###### Example

_ANY Memory System Root Volume:_

- Size = 50 GiB
- IOPS = 3000
- Throughput = 125 MB/s

### HANA Data Volume

The Storage\DATA filesystem (default `/hana/data`) stores the persistent copy of the SAP HANA in-memory database. While SAP HANA operates with data in-memory, this volume ensures data durability through regular savepoints. The storage must handle mixed workload patterns including random reads and writes during normal operation, and sequential patterns during savepoints, with consistently low latency to maintain database performance.

###### Size Calculation

The data volume size requirements are derived from system memory size. While actual storage requirements depend on your specific workload, compression ratios, and growth projections, use the following calculation as a baseline. Consult SAP sizing tools for precise calculations.

- SAP Documentation: [SAP Benchmark Sizing](https://www.sap.com/about/benchmark/sizing.html "https://www.sap.com/about/benchmark/sizing.html")

```
data_volume_size = MROUND(memory_size * 1.2, 100)

Where:
- Size factor = 1.2
- Rounding factor = 100
```

###### Note

While SAP has updated their size factor recommendation from 1.2 to 1.5 to accomodate operational requirement, AWS maintains the 1.2 factor as the baseline for initial deployments. This is a cost-effective approach that leverages the dynamic scaling capabilities of EBS volumes, allowing you to expand storage capacity online as your needs grow. You can easily increase volume size without service interruption when additional space is required.

###### Storage Type Selection

- Use gp3 with custom IOPS/throughput up to volume limits
- Consider io2 Block Express when requiring consistent sub-millisecond latency
- For Xen based instances, use gp2 (striped) or io2 Block Express since gp3 may not meet the SAP HANA storage latency KPI for log writes.

**IOPS Formula**

```
data_iops_target = MROUND(7200 + (0.45 * memory_size), 100)

Where:
- Base IOPS = 7200
- IOPS factor = 0.45 per GiB of memory
- Rounding factor = 100
```

- Large instances may require multiple volumes to achieve the specified data_iops_target. Refer to the striping guidelines below.
- The minimum IOPS required to meet SAP HANA KPIs for Data is 7000.

**Throughput Formula**

```
data_throughput_target = MIN(MROUND(450 + (0.2 * memory_size), 125), 2000)

Where:
- Base throughput = 450 MB/s
- Throughput factor = 0.2 MB/s per GiB of memory
- Maximum throughput = 2000 MB/s (see exception)
- Rounding factor = 125
```

- For large instances using gp3 volumes, a single volume might not achieve the required `data_throughput_target`. For more information about using multiple volumes, see [When to Stripe Volumes](#_when_to_stripe_volumes "#_when_to_stripe_volumes").
- SAP’s minimum throughput requirement for HANA data volumes is 400 MB/s. The base throughput value of 450 MB/s in our formula ensures this SAP KPI is met with additional headroom for optimal performance.
- Every instance type has its own Amazon EBS throughput maximum. For details, see [Amazon EBS-Optimized Instances](../../../AWSEC2/latest/UserGuide/ebs-optimized.md "../../../AWSEC2/latest/UserGuide/ebs-optimized.md") in the AWS documentation.
- Exception: For instances of 32 TB and larger (currently instance type u7inh-32tb.480xlarge), we recommend provisioning 4000 MB/s of throughput or higher. For all other instance sizes, if you need more than 2000 MB/s of throughput, you can adjust the maximum throughput value in the formula accordingly.

###### Volume Striping

Implement volume striping when you need to meet specific technical limits, performance requirements, or operational demands. Refer to the [When to Stripe Volumes](#_when_to_stripe_volumes "#_when_to_stripe_volumes") for detailed guidance on when striping is appropriate.

For gp3 volumes, throughput is typically the first limit you’ll encounter. For io2 Block Express volumes, throughput is calculated as IOPS × I/O size. SAP HANA workloads typically use 256 KiB I/O operations - at this size, a single io2 Block Express volume can achieve 4,000 MB/s throughput with 16,000 IOPS. Given these capabilities, volume striping is not required for most HANA deployments on io2 Block Express. If higher throughput is needed, you can adjust the provisioned IOPS accordingly.

If implementing striping for data volumes, use a 256 KB stripe size to optimize for data operations.

###### Examples

_512 GiB Memory System HANA Data Volume:_

- Storage Type Selection = GP3
- Size = MROUND((512 GiB \* 1.2),100) = 600 GiB
- IOPS = MROUND(7,200 + (0.45 \* 512), 100) = 7,460 IOPS
- Throughput = MIN(MROUND(450 + (0.2 \* 512), 125), 2,000) = 500 MB/s
- Striping = Not required.

_4 TiB Memory System HANA Data Volume:_

- Storage Type Selection = GP3
- Size = MROUND((4,096 GiB \* 1.2),100) = 4,900 GiB
- IOPS = MROUND(7,200 + (0.45 \* 4096), 100) = 9,000 IOPS
- Throughput = MIN(MROUND(450 + (0.2 \* 4,096), 125), 2000) = 1250 MB/s
- Striping = Required for throughput. Consider 2 x 2,450 GiB Filesystems, 4500 IOPS, 625 MB/s Throughput

### HANA Log Volume

The Storage\LOG filesystem (default `/hana/log`) stores the redo log files that ensure data durability and consistency. This filesystem handles write-intensive workloads with high-frequency, small, sequential writes. Because log writes directly impact database response time and transaction performance, storage volumes require consistent sub-millisecond latency.

###### Size Calculation

The log volume size requirements are derived from system memory size. Modifications can be made based on transaction volume and log backup frequency.

```
log_volume_size = MROUND((memory_size * 0.5),100)

Where:
- Minimum Size = 50 GiB
- Maximum Size = 500 GiB
- Rounding factor = 100
```

###### Storage Type Selection

- Use gp3 with custom IOPS/throughput up to volume limits
- Consider io2 Block Express when requiring consistent sub-millisecond latency
- For Xen based instances, use gp2 (striped) or io2 Block Express since gp3 may not meet the SAP HANA storage latency KPI for log writes.

**IOPS Formula**

```
log_iops_target = 3000

Where:
- Base IOPS = 3000
```

- The minimum IOPS required to meet SAP HANA KPIs for Data is 3000.

**Throughput Formula**

```
log_throughput_target = MIN(MROUND(300 + (0.015 * memory_size), 300), 500)

Where:
- Base throughput = 300 MB/s
- Throughput factor = 0.015 MB/s per GiB of memory
- Maximum throughput = 500 MB/s
- Rounding factor = 300
```

- SAP’s minimum throughput requirement for HANA log volumes is 250 MB/s. The base throughput value of 300 MB/s and the rounding factor in our formula ensures this value remains static with changing sizes and that the SAP KPI is met with additional headroom for optimal performance.

###### Volume Striping

For log volumes, striping is generally not required to achieve the `log_throughput_target` when using gp3 or io2 Block Express volumes. Single volumes typically provide sufficient performance for log operations.

If implementing striping for log volumes, use a 64 KB stripe size to optimize for sequential write patterns typical of log operations. Refer to the [When to Stripe Volumes](#_when_to_stripe_volumes "#_when_to_stripe_volumes") section to understand where striping is required in order to achieve the throughput, IOPS or performance targets.

###### Examples

_512 GiB Memory System HANA Log Volume:_

- Storage Type Selection = GP3
- Size = MROUND512 GiB \* 0.5),100 = 300 GiB (within 500 GiB maximum)
- IOPS = 3000
- Throughput = MIN(MROUND(300 + (0.015 \* 512), 300), 500) = 300 MB/s
- Striping = Not required.

### HANA Shared Volume

The HANA Shared filesystem (default `/hana/shared`) contains SAP HANA installation files, trace files, and shared configuration files.

###### Note

This file system must be accessible to all nodes in scale-out deployments.

###### Size Calculation

For single-node deployments:

```
shared_volume_size = MIN(memory_size, 1024)

Where:
- memory_size is system memory in GiB
- 1024 represents 1 TiB maximum
```

For scale-out deployments:

For scale-out SAP HANA systems, the /hana/shared filesystem requires disk space equal to one worker node’s memory for every four worker nodes in the deployment.

```
shared_volume_size = worker_node_memory * CEILING(number_of_worker_nodes/4)

Where:
- worker_node_memory is the memory size of a single worker node in GiB
- number_of_worker_nodes is the total number of worker nodes
- CEILING rounds up to the nearest whole number
```

**Examples for scale-out deployments**

|                    |                 |             |               |
| ------------------ | --------------- | ----------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Worker Node Memory | Number of Nodes | Calculation | Required Size |
| 2 TiB              | 1-4 nodes       | 2048 \* 1   | 2 TiB         |
| 2 TiB              | 5-8 nodes       | 2048 \* 2   | 4 TiB         |
| 2 TiB              | 9-11 nodes      | 2048 \* 3   | 6 TiB         |
| 2 TiB              | 12-15 nodes     | 2048 \* 4   | 8 TiB         | ###### Storage Type Selection <br>• GP3 provides the required performance characteristics for scale-up deployments <br>• Amazon EFS is a viable option for both scale-up and scale-out deployments, providing shared access across all nodes with the required performance characteristics. For scale-out configurations, see [Configure Storage (EFS)](configure-nfs-for-scale-out-workloads.md "configure-nfs-for-scale-out-workloads.md") **IOPS Formula** `shared_iops_target = 3000 Where: <br>• Base IOPS = 3000 (fixed)` **Throughput Formula** `shared_throughput_target = 125 Where: <br>• Base throughput = 125 MB/s (fixed)` ###### Examples _512 GiB Memory System HANA Shared Volume:_ <br>• Size = 512 GiB <br>• IOPS = 3000 <br>• Throughput = 125 MB/s ### HANA Backup Volume (Optional) The `/backup` filesystem provides local storage for SAP HANA file-based backups, including data and log backups. While local filesystem backups can be useful for non-critical systems or as a secondary backup option, they present several challenges in production environments: <br>• An additional sync step is required to move backups to durable storage like Amazon S3 <br>• The recovery point objectives may be impacted if there is a disk or hardware failure <br>• Careful management of local storage capacity is required via housekeeping and monitoring <br>• In scale-out, volume needs to be accessible across all nodes ###### Important AWS recommends using [AWS Backup for SAP HANA](aws-backint-agent-backup.md "aws-backint-agent-backup.md") or the [AWS Backint Agent](aws-backint-agent-backup.md "aws-backint-agent-backup.md") instead of file-based backups. These solutions provide direct backup to durable storage and simplify backup management. ###### Size Calculation The size of the backup volume is very dependent on the usage of the system. The following should be used as an initial baseline, but adapted post deployment depending on backup size, volume of change, retention of local copies and contingency. `backup_volume_size = memory_size * 3 Where: <br>• memory_size is system memory in GiB` ###### Storage Type Selection <br>• For single-node deployment, we recommend using Amazon EBS Throughput Optimized HDD (st1) volumes for SAP HANA to perform file-based backup. This volume type provides low-cost magnetic storage designed for large sequential workloads. SAP HANA uses sequential I/O with large blocks to back up the database, so st1 volumes provide a low-cost, high-performance option for this scenario. To learn more about st1 volumes, see [Amazon EBS Volume Types](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md"). <br>• For multi-node deployment, we recommend using Amazon EFS for SAP HANA to perform file-based backup. It can support performance over 10 GB/sec and over 500,000 IOPS. **IOPS Formula** `backup_iops_target = n/a` ###### Note ST1 Baseline is 500 IOPs but this is not configurable. Backup operations typically depend more on throughput than IOPS performance. ###### Throughput Formula For ST1 volumes, use this formula as a starting point to determine the number of volumes needed for backup throughput. Adjust the final volume count based on your actual backup window requirements and performance monitoring data. `backup_volumes_for_throughput = CEILING(memory_size/6000) * 500 Where: <br>• memory_size is system memory in GiB <br>• 6000 represents the GiB threshold for striping <br>• 500 is maximum throughput MB/s per st1 volume <br>• Result indicates number of volumes needed for throughput` **Examples for scale-out deployments** |
|                    |                 |             |               | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | --- | ---       |
| Worker Node Memory | Volumes         | Throughput  |               | 4 TiB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 1   | 500 MB/s  |
| 12 TiB             | 2               | 1000 MB/s   |               | 24 TiB                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 4   | 2000 MB/s | ### When to Stripe Volumes Linux Logical Volume Management (LVM) striping distributes data across multiple EBS volumes to increase I/O performance. The striped volumes act as a single logical volume, with reads and writes distributed across all volumes in the stripe set. Implement storage volume striping in the following scenarios: Technical Limits <br>• Throughput requirements exceed single volume maximum (1,000 MB/s for gp3, 4,000 MB/s for io2 Block Express). + For io2 Block Express volumes, throughput is calculated as IOPS × I/O size. SAP HANA workloads typically use 256 KiB I/O operations - at this size, a single io2 Block Express volume can achieve 4,000 MB/s throughput with 16,000 IOPS. Given these capabilities, volume striping is not required for most HANA deployments on io2 Block Express. If higher throughput is needed, you can adjust the provisioned IOPS accordingly. <br>• IOPS requirements exceed single volume maximum (16,000 for gp3, 256,000 for io2 Block Express) <br>• Volume size requirements exceed single volume maximum (16 TiB for gp3, 64 TiB for io2 Block Express) Operational Requirements <br>• Large data loads or backups that need to complete within specific time windows <br>• Systems with memory sizes > 4 TiB where data operations exceed acceptable durations <br>• High-throughput analytical workloads requiring sustained parallel I/O <br>• Expected growth that will exceed single-volume limits ###### Important Before implementing striping, first consider using higher performance EBS volume types or adjusting the IOPS and throughput settings within single-volume limits. Striping requires volumes of the same type and size, and balanced I/O patterns to be effective. |
