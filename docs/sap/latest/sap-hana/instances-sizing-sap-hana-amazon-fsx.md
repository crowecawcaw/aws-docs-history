

# Supported configurations
<a name="instances-sizing-sap-hana-amazon-fsx"></a>

The following rules and limitations are applicable for deploying SAP HANA on AWS with Amazon FSx for NetApp ONTAP.
+ FSx for ONTAP file systems for SAP HANA data and log volumes are only supported for single Availability Zone deployment.
+ Amazon EC2 instances where you plan to deploy your SAP HANA workload and FSx for ONTAP file systems must be in the same subnet.
+ Use separate storage virtual machines (SVM) for SAP HANA data and log volumes at no additional cost. This ensures that your I/O traffic flows through different IP addresses and TCP sessions.
+ For SAP HANA scale-out with standby node, the `basepath_shared` must be set to *Yes*. You can locate it in the *Persistence* section of the `global.ini` file.
+ SAP HANA on FSx for ONTAP is only supported with the NFSv4.1 protocol. SAP HANA volumes must be created and mounted using the NFSv4.1 protocol.
+ SAP HANA on FSx for ONTAP is only supported on the following operating systems:
  + Red Hat Enterprise Linux 8.4 and above
  + SUSE Linux Enterprise Server 15 SP2 and above
+  `/hana/data` and `/hana/log` must have their own FSx for ONTAP volumes. `/hana/shared`, and `/usr/sap` can share a volume.

## Supported Amazon EC2 instance types
<a name="instance-types-sap-hana-amazon-fsx"></a>

Amazon FSx for NetApp ONTAP is certified by SAP for scale-up and scale-out (OLTP/OLAP) SAP HANA workloads in a single Availability Zone setup. You can use Amazon FSx for NetApp ONTAP as the primary storage for SAP HANA data, log, binary, and shared volumes. For a complete list of supported Amazon EC2 instances for SAP HANA, see [SAP HANA certified instances](https://docs.aws.amazon.com/sap/latest/general/sap-hana-aws-ec2.html).

## Sizing
<a name="sizing-sap-hana-amazon-fsx"></a>

You can configure the throughput capacity of FSx for ONTAP when you create a new file system by scaling up to 4 GB/s of read throughput and 1000 MB/s of write throughput in a single Availability Zone deployment. For more information, see [Amazon FSx for NetApp ONTAP performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html).

**Topics**
+ [SAP KPIs](#sizing-sap-kpi)
+ [Minimum requirement](#sizing-min-req)
+ [Higher throughput](#sizing-high-throughput)

### SAP KPIs
<a name="sizing-sap-kpi"></a>

 **SAP requires the following KPIs for SAP HANA volumes.** 


<table>
<thead>
  <tr><th></th><th>Read</th><th>Write</th></tr>
</thead>
<tbody>
  <tr><td>Data</td><td>400 MB/s</td><td>250 MB/s</td></tr>
  <tr><td>Log</td><td>250 MB/s</td><td>250 MB/s</td></tr>
  <tr><td>Latency for log</td><td colspan="2">Less than 1 millisecond write latency with 4K and 16K block sized I/O</td></tr>
</tbody>
</table>


### Minimum requirement
<a name="sizing-min-req"></a>

You must provision FSx for ONTAP volumes with sufficient capacity and performance, based on the requirements of your SAP HANA workload. To meet the storage KPIs for SAP HANA, you need a throughput capacity of at least **1,024 MB/s**. Lower throughput may be acceptable for non-production systems.

Sharing a file system between multiple SAP HANA nodes is supported when the file system meets the requirements of all SAP HANA nodes. When sharing a file system, you can use the quality of service feature for consistent performance and reduced interference between competing workloads. For more information, see [Using Quality of Service in Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/using-quality-of-service-in-amazon-fsx-for-netapp-ontap/).

### Higher throughput
<a name="sizing-high-throughput"></a>

If you require higher throughput, you can do one of the following:
+ Create separate data and log volumes on different FSx for ONTAP file systems.
+ Create additional data volume partitions across multiple FSx for ONTAP file systems.

To learn more about FSx for ONTAP performance, see [Performance details](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html#performance-details-fsxw).

## SAP HANA parameters
<a name="sap-hana-amazon-fsx"></a>

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