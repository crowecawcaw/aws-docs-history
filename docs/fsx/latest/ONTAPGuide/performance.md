

# Amazon FSx for NetApp ONTAP performance

Following is an overview of Amazon FSx for NetApp ONTAP file system performance, with a discussion of the available performance and throughput options and useful performance tips.

**Topics**
+ [How performance is measured for FSx for ONTAP file systems](#perf-overview)
+ [Performance details](#performance-details-fsxw)
+ [Impact of deployment type on performance](#deployment-type-performance)
+ [Impact of storage capacity on performance](#storage-capacity-and-performance)
+ [Impact of throughput capacity on performance](#impact-throughput-cap-performance)
+ [Availability by AWS Region](#perf-region-availability)
+ [Example: storage capacity and throughput capacity](#throughput-example-ontap)

## How performance is measured for FSx for ONTAP file systems
<a name="perf-overview"></a>

File system performance is measured by its latency, throughput, and I/O operations per second (IOPS).

### Latency
<a name="latency-fsxW"></a>

Amazon FSx for NetApp ONTAP provides sub-millisecond file operation latencies with solid state drive (SSD) storage, and tens of milliseconds of latency for capacity pool storage. Above that, Amazon FSx has two layers of read caching on each file server—NVMe (non-volatile memory express) drives and in-memory—to provide even lower latencies when you access your most frequently-read data.

### Throughput and IOPS
<a name="throughput-and-iops-fsxw"></a>

Each Amazon FSx file system provides up to tens of GBps of throughput and millions of IOPS. The specific amount of throughput and IOPS that your workload can drive on your file system depends on the total throughput capacity and storage capacity configuration of your file system, along with the nature of your workload, including the size of the active working set.

### SMB Multichannel and NFS nconnect support
<a name="single-client-performance"></a>

With Amazon FSx, you can configure SMB Multichannel to provide multiple connections between ONTAP and clients in a single SMB session. SMB Multichannel uses multiple network connections between the client and server simultaneously to aggregate network bandwidth for maximal utilization. For information on using the NetApp ONTAP CLI to configure SMB Multichannel, see [Configuring SMB Multichannel for performance and redundancy](https://docs.netapp.com/us-en/ontap/smb-admin/configure-multichannel-performance-task.html).

NFS clients can use the `nconnect` mount option to have multiple TCP connections (up to 16) associated with a single NFS mount. Such an NFS client multiplexes file operations onto multiple TCP connections in a round-robin fashion and thus obtains higher throughput from the available network bandwidth. NFSv3 and NFSv4.1\+ support `nconnect`. [ Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) describes the full duplex 5 Gbps per network flow bandwidth limit. You can overcome this limit by using multiple network flows with `nconnect` or SMB multichannel. See your NFS client documentation to confirm whether `nconnect` is supported in your client version. For more information about NetApp ONTAP support for `nconnect`, see [ONTAP support for NFSv4.1](https://docs.netapp.com/us-en/ontap/nfs-admin/ontap-support-nfsv41-concept.html).

#### Jumbo frames
<a name="jumbo-frames"></a>

To achieve the maximum read or write throughput, we recommend enabling jumbo frames on all network interfaces in the data path to your Amazon FSx file system, including your client EC2 instances. The default maximum transmission unit (MTU) setting for network interfaces on your FSx for ONTAP file system is 9,001 bytes.

## Performance details
<a name="performance-details-fsxw"></a>

To understand the Amazon FSx for NetApp ONTAP performance model in detail, you can examine the architectural components of an Amazon FSx file system. Your client compute instances, whether they exist in AWS or on-premises, access your file system through one or multiple elastic network interfaces (ENI). These network interfaces reside in the Amazon VPC that you associate with your file system. Behind each file system ENI is a NetApp ONTAP file server that is serving data over the network to the clients accessing the file system. Amazon FSx provides a fast in-memory cache and NVMe cache on each file server to enhance performance for the most frequently accessed data. Attached to each file server are the SSD disks hosting your file system data.

These components are illustrated in the following diagram.

![FSx for ONTAP architecture.](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/images/fsx-ontap-performance.png)


Corresponding with these architectural components–network interface, in-memory cache, NVMe cache, and storage volumes–are the primary performance characteristics of an Amazon FSx for NetApp ONTAP file system that determine the overall throughput and IOPS performance.
+ Network I/O performance: throughput/IOPS of requests between the clients and the file server (in aggregate)
+ In-memory and NVMe cache size on the file server: size of active working set that can be accommodated for caching
+ Disk I/O performance: throughput/IOPS of requests between the file server and the storage disks

There are two factors that determine these performance characteristics for your file system: the total amount of SSD IOPS and throughput capacity that you configure for it. The first two performance characteristics – network I/O performance and in-memory and NVMe cache size – are solely determined by throughput capacity, while the third one – disk I/O performance – is determined by a combination of throughput capacity and SSD IOPS.

File-based workloads are typically spiky, characterized by short, intense periods of high I/O with plenty of idle time between bursts. To support spiky workloads, in addition to the baseline speeds that a file system can sustain 24/7, Amazon FSx provides the capability to burst to higher speeds for periods of time for both network I/O and disk I/O operations. Amazon FSx uses a network I/O credit mechanism to allocate throughput and IOPS based on average utilization — file systems accrue credits when their throughput and IOPS usage is below their baseline limits, and can use these credits when they perform I/O operations. 

**Note**  
For iSCSI and NVMe/TCP SAN protocols, sequential read client operations can achieve up to the file system's maximum network I/O burst or baseline throughput.

Write operations use twice as much network bandwidth as read operations. A write operation has to be replicated on the secondary file server, so a single write operation results in twice the amount of network throughput.

## Impact of deployment type on performance
<a name="deployment-type-performance"></a>

You can create Single-AZ and Multi-AZ file systems with FSx for ONTAP. First-generation Single-AZ file systems and all Multi-AZ file systems are powered by one high-availability (HA) pair. Second- and third-generation Single-AZ file systems are powered by up to 12 HA pairs. For more information, see [Managing high-availability (HA) pairs](HA-pairs.md).

The following table shows the maximum throughput capacity that file systems can scale up to, per HA pair and per file system, by generation and deployment type.


<table>
<thead>
  <tr><th></th><th></th><th colspan="2">Maximum per HA pair (MBps)</th><th></th><th colspan="2">Maximum per file system (MBps)</th></tr>
  <tr><th>Generation</th><th>Deployment type</th><th>Read throughput</th><th>Write throughput</th><th>Maximum HA pairs</th><th>Read throughput</th><th>Write throughput</th></tr>
</thead>
<tbody>
  <tr><td rowspan="2"><b>Third-generation</b></td><td>Single-AZ</td><td rowspan="2">18,432</td><td rowspan="2">4,500</td><td>12</td><td>221,184</td><td>54,000</td></tr>
  <tr><td>Multi-AZ</td><td>1</td><td>18,432</td><td>4,500</td></tr>
  <tr><td rowspan="2"><b>Second-generation</b></td><td>Single-AZ</td><td rowspan="2">6,144</td><td rowspan="2">2,048</td><td>12</td><td>73,728</td><td>24,576</td></tr>
  <tr><td>Multi-AZ</td><td>1</td><td>6,144</td><td>2,048</td></tr>
  <tr><td rowspan="2"><b>First-generation</b></td><td>Single-AZ</td><td rowspan="2">4,0961, 2</td><td>1,0001</td><td>1</td><td>4,0961, 2</td><td>1,0001</td></tr>
  <tr><td>Multi-AZ</td><td>1,8001</td><td>1</td><td>4,0961, 2</td><td>1,8001</td></tr>
</tbody>
</table>


**Note**  
1 Varies by AWS Region. See [Availability by AWS Region](#perf-region-availability).  
2 To provision 4 GBps of throughput capacity, your file system must be configured with a minimum of 5,120 GiB of SSD storage capacity and 160,000 SSD IOPS.

## Impact of storage capacity on performance
<a name="storage-capacity-and-performance"></a>

The maximum disk throughput and IOPS levels your file system can achieve is the lower of:
+ the disk performance level provided by your file servers, based on the throughput capacity you select for your file system
+ the disk performance level provided by the number of SSD IOPS you provision for your file system

By default, your file system's SSD storage provides up to the following levels of disk throughput and IOPS:
+ Disk throughput (MBps per TiB of storage): 768
+ Disk IOPS (IOPs per TiB of storage): 3,072

**Note**  
When decreasing SSD storage capacity on a second-generation or third-generation file system, most workloads experience minimal performance impact. However, write-heavy workloads might experience a temporary performance degradation. You might also experience brief I/O pauses (up to 60 seconds) as client access is redirected to new disks.  
To minimize performance impact, ensure that ongoing workloads don't consistently consume more than 50% CPU, 50% disk throughput, or 50% SSD IOPS before initiating an SSD decrease operation. For more information about decreasing SSD storage capacity, see [When to decrease SSD storage capacity](storage-capacity-and-IOPS.md#when-to-decrease-ssd-storage-capacity).

## Impact of throughput capacity on performance
<a name="impact-throughput-cap-performance"></a>

Every Amazon FSx file system has a throughput capacity that you configure when the file system is created. Your file system's throughput capacity determines the level of network I/O performance, or the speed at which each of the file servers that are hosting your file system can serve file data over the network to clients accessing it. Higher levels of throughput capacity come with more memory and non-volatile memory express (NVMe) storage for caching data on each file server, and higher levels of disk I/O performance supported by each file server.

You can optionally provision a higher level of SSD IOPS when creating your file system. The maximum level of SSD IOPS that your file system can achieve is also dictated by your file system's throughput capacity, even when provisioning additional SSD IOPS.

The following tables show the full set of specifications for throughput capacity, along with baseline and burst levels, and amount of memory for caching on the file server. Choose a deployment type, then find the table for your file system's generation.

------
#### [ Single-AZ file systems ]

**Third-generation file systems**

These performance specifications apply to third-generation Single-AZ file systems, per HA pair.


**Performance specifications for third-generation Single-AZ file systems**  

| FSx throughput capacity per HA pair (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 384\*\* | 521 | 2,500 |  Hundreds of thousands baseline  | 16 | – | 384 | 3,125 | 15,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 768\*\* | 1,042 | 3,333 | 32 | – | 768 | 3,125 | 30,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,536 | 2,083 | 4,167 | 64 | 918 | 1,536 | 3,125 | 60,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 3,072 | 4,167 | – | 128 | 1,868 | 3,072 | – | 120,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 6,144 | 8,333 | – | 256 | 3,768 | 6,144 | – | 240,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 12,288 | 16,667 | – | 512 | 7,536 | 12,288 | – | 480,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 18,432 | 25,000 | – | 768 | 11,304 | 18,432 | – | 720,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

**Second-generation file systems**

These performance specifications apply to second-generation Single-AZ file systems, per HA pair.


**Performance specifications for second-generation Single-AZ file systems**  

| FSx throughput capacity per HA pair (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 384\*\* | 781 | 3,750 |  Hundreds of thousands baseline  | 16 | – | 384 | 3,125 | 12,500 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 768\*\* | 1,563 | 5,000 | 32 | – | 768 | 3,125 | 25,000 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,536 | 3,125 | 6,250 | 64 | 918 | 1,536 | 3,125 | 50,000 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 3,072 | 6,250 | – | 128 | 1,868 | 3,072 | – | 100,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 6,144 | 12,500 | – | 256 | 3,736 | 6,144 | – | 200,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

**Note**  
\*\* Second-generation and third-generation Single-AZ file systems support 384 and 768 MBps throughput capacities, but only with one HA pair. To add HA pairs, your file system must be configured with at least 1,536 MBps of throughput capacity per HA pair.

**First-generation file systems**

These performance specifications apply to first-generation Single-AZ file systems.


**Performance specifications for first-generation Single-AZ file systems in US East (Ohio), US East (N. Virginia), US West (Oregon), and Europe (Ireland) (file systems created after November 28, 2022)**  

| FSx throughput capacity (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 128 | 188 | 1,500 |  Tens of thousands baseline  | 16 | – | 128 | 1,250 | 6,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 256 | 375 | 1,500 | 32 | – | 256 | 1,250 | 12,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 512 | 750 | 1,500 |  Hundreds of thousands baseline  | 64 | – | 512 | 1,250 | 20,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,024 | 1,500 | – | 128 | – | 1,024 | 1,250 | 40,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 2,048 | 3,125 | – | 256 | 3,800 | 2,048 | – | 80,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 4,096 | 6,250 | – | 512 | 7,600 | 4,096 | – | 160,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |


**Performance specifications for first-generation Single-AZ file systems in [All other AWS Regions where FSx for ONTAP is available](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)**  

| FSx throughput capacity (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 128 | 150 | 1,250 |  Tens of thousands baseline  | 16 | – | 128 | 600 | 6,000 | 18,750 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 256 | 300 | 1,250 | 32 | – | 256 | 600 | 12,000 | 18,750 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 512 | 625 | 1,250 |  Hundreds of thousands baseline  | 64 | – | 512 | – | 18,750 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,024 | 1,500 | – | 128 | – | 1,024 | – | 40,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 2,048 | 3,125 | – | 256 | 3,600 | 2,048 | – | 80,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

------
#### [ Multi-AZ file systems ]

**Third-generation file systems**

These performance specifications apply to third-generation Multi-AZ file systems, per HA pair.


**Performance specifications for third-generation Multi-AZ file systems**  

| FSx throughput capacity per HA pair (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 384 | 521 | 2,500 |  Hundreds of thousands baseline  | 16 | 205 | 384 | 3,125 | 15,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 768 | 1,042 | 3,333 | 32 | 442 | 768 | 3,125 | 30,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,536 | 2,083 | 4,167 | 64 | 918 | 1,536 | 3,125 | 60,000 | 120,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 3,072 | 4,167 | – | 128 | 1,868 | 3,072 | – | 120,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 6,144 | 8,333 | – | 256 | 3,736 | 6,144 | – | 240,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 12,288 | 16,667 | – | 512 | 7,536 | 12,288 | – | 480,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 18,432 | 25,000 | – | 768 | 11,304 | 18,432 | – | 720,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

**Second-generation file systems**

These performance specifications apply to second-generation Multi-AZ file systems, per HA pair.


**Performance specifications for second-generation Multi-AZ file systems**  

| FSx throughput capacity per HA pair (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 384 | 781 | 3,750 |  Hundreds of thousands baseline  | 16 | 205 | 384 | 3,125 | 12,500 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 768 | 1,563 | 5,000 | 32 | 442 | 768 | 3,125 | 25,000 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,536 | 3,125 | 6,250 | 64 | 918 | 1,536 | 3,125 | 50,000 | 100,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 3,072 | 6,250 | – | 128 | 1,868 | 3,072 | – | 100,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 6,144 | 12,500 | – | 256 | 3,736 | 6,144 | – | 200,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

**First-generation file systems**

These performance specifications apply to first-generation Multi-AZ file systems.


**Performance specifications for first-generation Multi-AZ file systems in US East (Ohio), US East (N. Virginia), US West (Oregon), and Europe (Ireland) (file systems created after November 28, 2022)**  

| FSx throughput capacity (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 128 | 188 | 1,500 |  Tens of thousands baseline  | 16 | 205 | 128 | 1,250 | 6,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 256 | 375 | 1,500 | 32 | 442 | 256 | 1,250 | 12,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 512 | 750 | 1,500 |  Hundreds of thousands baseline  | 64 | 918 | 512 | 1,250 | 20,000 | 40,000 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,024 | 1,500 | – | 128 | 1,868 | 1,024 | 1,250 | 40,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 2,048 | 3,125 | – | 256 | 3,736 | 2,048 | – | 80,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 4,096 | 6,250 | – | 512 | 7,472 | 4,096 | – | 160,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |


**Performance specifications for first-generation Multi-AZ file systems in [All other AWS Regions where FSx for ONTAP is available](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)**  

| FSx throughput capacity (MBps) | Network throughput capacity (MBps) | Network IOPS | In-memory caching (GB) | NVMe caching (GB) | Disk throughput (MBps) | SSD drive IOPS \* | 
| --- |--- |--- |--- |--- |--- |--- |
|  ****  |  **Baseline**  |  **Burst**  |  ****  |  ****  |  ****  |  **Baseline**  |  **Burst**  |  **Baseline**  |  **Burst**  | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 128 | 150 | 1,250 |  Tens of thousands baseline  | 16 | 118 | 128 | 600 | 6,000 | 18,750 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 256 | 300 | 1,250 | 32 | 268 | 256 | 600 | 12,000 | 18,750 | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 512 | 625 | 1,250 |  Hundreds of thousands baseline  | 64 | 536 | 512 | – | 18,750 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |--- |
| 1,024 | 1,500 | – | 128 | 1,736 | 1,024 | – | 40,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |
| 2,048 | 3,125 | – | 256 | 3,472 | 2,048 | – | 80,000 | – | 
| --- |--- |--- |--- |--- |--- |--- |--- |--- |

------

\* Your SSD IOPS are only used when you access data that is not cached in your file server's in-memory cache or NVMe cache.

**Note**  
For second- and third-generation file systems (Single-AZ 2, Multi-AZ 2, Single-AZ 3, and Multi-AZ 3), using an NVMe cache can result in your workload achieving less total throughput for high-throughput or large I/O workloads. If you have a throughput-bound workload, we recommend disabling the NVMe cache. For more information, see [Managing the NVMe cache](nvme-cache.md).

## Availability by AWS Region
<a name="perf-region-availability"></a>

The following table shows the AWS Regions where each generation of FSx for ONTAP file systems is available.


**FSx for ONTAP file system generations by AWS Region**  

| AWS Region | First generation | Second generation | Third generation | 
| --- | --- | --- | --- | 
| US East (N. Virginia) | ✓\* | ✓ | ✓ | 
| US East (Ohio) | ✓\* | ✓ | ✓ | 
| US West (N. California) | ✓ | ✓ |  | 
| US West (Oregon) | ✓\* | ✓ | ✓ | 
| AWS GovCloud (US-East) | ✓ |  |  | 
| AWS GovCloud (US-West) | ✓ | ✓ |  | 
| Africa (Cape Town) | ✓ |  |  | 
| Asia Pacific (Hong Kong) | ✓ |  |  | 
| Asia Pacific (Tokyo) | ✓ | ✓ | ✓ | 
| Asia Pacific (Seoul) | ✓ | ✓ |  | 
| Asia Pacific (Osaka) | ✓ |  |  | 
| Asia Pacific (Mumbai) | ✓ | ✓ |  | 
| Asia Pacific (Hyderabad) | ✓ | ✓ |  | 
| Asia Pacific (Singapore) | ✓ | ✓ |  | 
| Asia Pacific (Sydney) | ✓ | ✓ |  | 
| Asia Pacific (Jakarta) | ✓ |  |  | 
| Asia Pacific (Melbourne) | ✓ |  |  | 
| Asia Pacific (Malaysia) | ✓ |  |  | 
| Asia Pacific (New Zealand) | ✓ |  |  | 
| Asia Pacific (Taipei) | ✓ |  |  | 
| Asia Pacific (Thailand) | ✓ |  |  | 
| Canada (Central) | ✓ | ✓ |  | 
| Canada West (Calgary) | ✓ |  |  | 
| Europe (Frankfurt) | ✓ | ✓ |  | 
| Europe (Zurich) | ✓ | ✓ |  | 
| Europe (Stockholm) | ✓ | ✓ |  | 
| Europe (Milan) | ✓ |  |  | 
| Europe (Spain) | ✓ | ✓ | ✓ | 
| Europe (Ireland) | ✓\* | ✓ | ✓ | 
| Europe (London) | ✓ | ✓ |  | 
| Europe (Paris) | ✓ |  |  | 
| Israel (Tel Aviv) | ✓ |  |  | 
| Mexico (Central) | ✓ |  |  | 
| Middle East (UAE) | ✓ |  |  | 
| Middle East (Bahrain) | ✓ |  |  | 
| South America (São Paulo) | ✓ | ✓ |  | 

\* In these AWS Regions, first-generation file systems created after November 28, 2022 scale up to 4,096 MBps of read throughput and 1,000 MBps (Single-AZ) or 1,800 MBps (Multi-AZ) of write throughput. In all other AWS Regions, first-generation file systems scale up to 2,048 MBps of read throughput and 750 MBps (Single-AZ) or 1,300 MBps (Multi-AZ) of write throughput.

## Example: storage capacity and throughput capacity
<a name="throughput-example-ontap"></a>

The following example illustrates how storage capacity and throughput capacity impact file system performance. 

A first-generation file system that is configured with 2 TiB of SSD storage capacity and 512 MBps of throughput capacity has the following throughput levels:
+ Network throughput – 625 MBps baseline and 1,250 MBps burst (see throughput capacity table)
+ Disk throughput – 512 MBps baseline and 600 MBps burst.

Your workload accessing the file system will therefore be able to drive up to 625 MBps baseline and 1,250 MBps burst throughput for file operations performed on actively accessed data cached in the file server in-memory cache and NVMe cache.