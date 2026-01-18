# Supported configurations

The following rules and limitations are applicable for deploying SAP HANA on AWS with Amazon FSx for NetApp ONTAP.

- FSx for ONTAP file systems for SAP HANA data and log volumes are only supported for single Availability Zone deployment.
- Amazon EC2 instances where you plan to deploy your SAP HANA workload and FSx for ONTAP file systems must be in the same subnet.
- Use separate storage virtual machines (SVM) for SAP HANA data and log volumes at no additional cost. This ensures that your I/O traffic flows through different IP addresses and TCP sessions.
- For SAP HANA scale-out with standby node, the `basepath_shared` must be set to _Yes_. You can locate it in the _Persistence_ section of the `global.ini` file.
- SAP HANA on FSx for ONTAP is only supported with the NFSv4.1 protocol. SAP HANA volumes must be created and mounted using the NFSv4.1 protocol.
- SAP HANA on FSx for ONTAP is only supported on the following operating systems:
  - Red Hat Enterprise Linux 8.4 and above
  - SUSE Linux Enterprise Server 15 SP2 and above

- `/hana/data` and `/hana/log` must have their own FSx for ONTAP volumes. `/hana/shared`, and `/usr/sap` can share a volume.

## Supported Amazon EC2 instance types

Amazon FSx for NetApp ONTAP is certified by SAP for scale-up and scale-out (OLTP/OLAP) SAP HANA workloads in a single Availability Zone setup. You can use Amazon FSx for NetApp ONTAP as the primary storage for SAP HANA data, log, binary, and shared volumes. For a complete list of supported Amazon EC2 instances for SAP HANA, see [SAP HANA certified instances](../general/sap-hana-aws-ec2.md "../general/sap-hana-aws-ec2.md").

## Sizing

You can configure the throughput capacity of FSx for ONTAP when you create a new file system by scaling up to 4 GB/s of read throughput and 1000 MB/s of write throughput in a single Availability Zone deployment. For more information, see [Amazon FSx for NetApp ONTAP performance](../../../fsx/latest/ONTAPGuide/performance.md "../../../fsx/latest/ONTAPGuide/performance.md").

###### Topics

- [SAP KPIs](#sizing-sap-kpi "#sizing-sap-kpi")
- [Minimum requirement](#sizing-min-req "#sizing-min-req")
- [Higher throughput](#sizing-high-throughput "#sizing-high-throughput")

### SAP KPIs

**SAP requires the following KPIs for SAP HANA volumes.**

|                 | Read                                                                  | Write    |
| --------------- | --------------------------------------------------------------------- | -------- |
| Data            | 400 MB/s                                                              | 250 MB/s |
| Log             | 250 MB/s                                                              | 250 MB/s |
| Latency for log | Less than 1 millisecond write latency with 4K and 16K block sized I/O |

### Minimum requirement

You must provision FSx for ONTAP volumes with sufficient capacity and performance, based on the requirements of your SAP HANA workload. To meet the storage KPIs for SAP HANA, you need a throughput capacity of at least **1,024 MB/s**. Lower throughput may be acceptable for non-production systems.

Sharing a file system between multiple SAP HANA nodes is supported when the file system meets the requirements of all SAP HANA nodes. When sharing a file system, you can use the quality of service feature for consistent performance and reduced interference between competing workloads. For more information, see [Using Quality of Service in Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-quality-of-service-in-amazon-fsx-for-netapp-ontap/ "https://aws.amazon.com/blogs/storage/using-quality-of-service-in-amazon-fsx-for-netapp-ontap/").

### Higher throughput

If you require higher throughput, you can do one of the following:

- Create separate data and log volumes on different FSx for ONTAP file systems.
- Create additional data volume partitions across multiple FSx for ONTAP file systems.

To learn more about FSx for ONTAP performance, see [Performance details](../../../fsx/latest/ONTAPGuide/performance.md#performance-details-fsxw "../../../fsx/latest/ONTAPGuide/performance.md#performance-details-fsxw").

## SAP HANA parameters

Set the following SAP HANA database parameters in the `global.ini` file.

```
 [fileio]
max_parallel_io_requests=128
async_read_submit=on
async_write_submit_active=on
async_write_submit_blocks=all
```

Use the following SQL commands to set these parameters on `SYSTEM` level.

```
 ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('fileio', 'max_parallel_io_requests') = '128' WITH RECONFIGURE;
ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('fileio', 'async_read_submit') = 'on' WITH RECONFIGURE;
ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('fileio', 'async_write_submit_active') = 'on' WITH RECONFIGURE;
ALTER SYSTEM ALTER CONFIGURATION ('global.ini', 'SYSTEM') SET ('fileio', 'async_write_submit_blocks') = 'all' WITH RECONFIGURE;
```
