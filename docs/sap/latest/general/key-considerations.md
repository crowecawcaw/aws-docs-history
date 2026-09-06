

# Network, storage, and compute
<a name="key-considerations"></a>

This section provides information about configuring network, storage, and compute for staging and target environments to achieve disaster recovery goals for your SAP workloads on AWS with Elastic Disaster Recovery.

**Topics**
+ [Network](#key-considerations-network)
+ [Storage](#key-considerations-storage)
+ [Compute](#key-considerations-compute)

## Network
<a name="key-considerations-network"></a>

Your network architecture and configuration used for disaster recovery can play a significant role in supporting an effective RTO and RPO SLA. You must consider network design and redirecting traffic to recovery instance when disaster recovery is triggered.

The following are the four steps to design network for disaster recovery.
+  [Connecting the source and target network](#step-connection) 
+  [Defining the staging and recovery subnets](#step-subnets) 
+  [Configuring the network security settings](#step-security) 
+  [SAP end user and integration traffic](#step-user) 

### Connecting the source and target network
<a name="step-connection"></a>

The first step is to choose and configure the network connection method from the source network to the replication servers. You can choose between private or public. For more information, see [Data routing and throttling](https://docs.aws.amazon.com/drs/latest/userguide/data-routing.html).

Regardless of the method, transferred data is always encrypted in transit. The default method is public, where data is routed over the internet to a public network interface on the replication servers. In the private method, the data is replicated over a private network. A private network selection depends on the disaster recovery scenario in use.
+  [AWS In-Region disaster recovery](scenarios.md#same-region) – Private networks are generally between VPCs, using either Amazon VPC peering or AWS Transit Gateway for connectivity. We recommend using a different AWS account, and separate Amazon VPC for disaster recovery. For more information, see [What is Amazon VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) and [What is a transit gateway?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).
+  [AWS Cross-Region disaster recovery](scenarios.md#different-regions) – We recommend using the fully redundant AWS network backbone that connects different AWS Regions together. Amazon VPC peering and AWS Transit Gateway enable connectivity between Regions. For more details, see [Introduction to Network Transformation on AWS](https://aws.amazon.com/blogs/networking-and-content-delivery/introduction-to-network-transformation-on-aws-part-1/).
+  [Outside of AWS to AWS disaster recovery](scenarios.md#other-aws) – In this scenario, your physical network between your source network and AWS are provided through various telecommunications or internet services providers (ISP). The following solutions are available on AWS.
  +  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
  +  [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/) 
  + SD-WAN available on [AWS marketplace](https://aws.amazon.com/marketplace) 

   AWS Direct Connect is commonly used by SAP on AWS customers. It provides more predictable performance against service level agreement (SLA) based targets such as throughput, jitter, and latency, versus VPN or SD-WAN based solutions. You can work with [AWS Direct Connect Delivery Partners](https://aws.amazon.com/directconnect/partners/) for guidance on which options are the best fit for your environment.

### Defining the staging and recovery subnets
<a name="step-subnets"></a>

One subnet is recommended to host the replication servers, called the *staging area subnet*. Additional subnets, called the recovery subnets, are necessary as the target of your disaster recovery action. For scenarios where the source network is on AWS, consider how your subnets should be allocated based on your selected AWS account strategy and landing zone. Often this may mean that the staging area subnets should be in a different Amazon VPC than your source servers. For a simplified environment, this may just use different subnets in the same Amazon VPC. This would mean reduced isolation between your production and non-production disaster recovery environments. For more information, see [AWS Well-Architected Framework : Best Practice 5.3](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-3.html).

Ultimately, the number and design of these subnets should follow similar concepts as your source environment. For more information, see [Network diagrams](https://docs.aws.amazon.com/drs/latest/userguide/Network-diagrams.html).

For [AWS In-Region disaster recovery](scenarios.md#same-region) scenario, we recommend hosting the staging area subnet in a different Availability Zone than the recovery subnets. This design enables an additional redundancy for disaster recovery. The launched recovery instances are protected by a staging area in a separate Availability Zone. This follows the design principle of using multiple Availability Zones to maintain resiliency.

### Configuring the network security settings
<a name="step-security"></a>

Ensure that the required network security settings are configured. This includes enabling access through a number of ports in your on-premises firewall, network security devices, security groups, or network access control lists (network ACL), and possibly other tasks depending on the location of your source environment. For more information, see [Replication network requirements](https://docs.aws.amazon.com/drs/latest/userguide/preparing-environments.html).

### SAP end user and integration traffic
<a name="step-user"></a>

The following are some of the factors that affect how the end user and integration related network traffic can affect your RTO and RPO.
+ DNS propagation time for clients to identify and resolve to new IP
+ Delays in network components (if any used) to reroute traffic, such as global or local load balancers, including AWS Application Load Balancers, AWS Global Accelerator, or Amazon Route 53 Public Data Plane

For more information, see [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html).

## Storage
<a name="key-considerations-storage"></a>

 AWS Elastic Disaster Recovery is designed to evaluate and define the optimal Amazon EBS volume settings for your staging environment based on the source server performance. A default performance setting is used for drill and recovery servers. These volumes are sized to match the capacity needs of the source systems. You must review these settings with the specific requirements of your SAP workloads. This ensures an efficient and disaster recovery SLA compliant environment. These different server types have different requirements, and methods of managing storage.

**Topics**
+ [Replication servers](#servers-storage)
+ [Drill and recovery instances](#instances-storage)
+ [Point in time recovery](#recovery-storage)

### Replication servers
<a name="servers-storage"></a>

The staging area requires storage to support ongoing replication from source machines. These Amazon EBS volumes are usually low-cost, hard disk drive (HDD) type storage volumes. However, if the replicated disk write throughput is high, the default Replication server settings dynamically change to a higher performance, solid state drive (SSD) storage type. The default Amazon EBS volume type setting – **Auto volume type selection** for replication servers, is the recommended setting for SAP workloads. It automatically chooses the high-performing, cost-efficient Amazon EBS volumes for your workload requirements.

You have the option to increase the performance of the staging area by selecting solid state drives (SSD). This can help SAP workloads, such as bursty or consistently high transaction rate databases which have a high rate of create, update, and/or delete operations that must be applied to its storage. For such workloads, we recommend monitoring Amazon CloudWatch metrics and check for any persistent or increasing delays. You can use the following CloudWatch metrics for Elastic Disaster Recovery.
+  **LagDuration** – the age of the latest consistent snapshot, in seconds
+  **Backlog** – the amount of data yet to be synced, in bytes

If Amazon EBS metrics on the replication server also indicate performance issues, you can change Amazon EBS volume type. See the following resources to learn more.
+  [Amazon EBS volume performance on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html) 
+  [Volumes](https://docs.aws.amazon.com/drs/latest/userguide/volumes-drs.html) 
+  [Disk settings](https://docs.aws.amazon.com/drs/latest/userguide/disk-settings.html) 

### Drill and recovery instances
<a name="instances-storage"></a>

SAP workloads require at least the `gp3` volume type for 90% or more of the use cases, including SAP applications and databases (SAP HANA and any other). If you have a higher per-volume IOPS requirement of more than 16,000 IOPS, or per-volume throughput requirement greater than 1,000 MiB/s, consider `io2` or `io2 Block Express` volumes.

When you launch drill or recovery instances, Elastic Disaster Recovery creates Amazon EBS storage volumes based on the types defined in the launch template. For more information, see [Amazon EC2 launch template](https://docs.aws.amazon.com/drs/latest/userguide/ec2-launch.html). The launch template is automatically generated by Elastic Disaster Recovery, with default values for storage performance, using general purpose SSD (volumes sized to match the source system capacity requirements). Review the launch template to confirm that your workload’s storage requirements are being met by the default allocations of the launch template.

You can modify the launch template for a different volume type or performance setting. Before modifying, confirm that your target Amazon EC2 instance type supports higher storage. For more details, see [Supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#ebs-optimization-support). For SAP HANA databases, see [Storage configuration](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-storage-config.html). Define the modified version as the default launch template for your server once your changes are applied to the template. We do not recommend adding or removing Amazon EBS volumes in the template when using it with Elastic Disaster Recovery.

For servers that require loading larger amounts of data before they become active, such as database servers, you can configure higher performance settings and types of storage in the launch template. For example, if your server is configured with `gp3` storage, then defining more provisioned throughput and IOPS for your storage, and/or using a higher performance scaling storage such as `io2 Block Express` (with a supported Amazon EC2 instance type), can reduce the time it takes for your drill or recovery instance to handle the expected workload quantity. Once your drill or recovery instance is fully online, you can change revert your storage settings. For more information, see [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html). You can increase the volume size, change the volume type, or adjust the performance of your Amazon EBS volumes, without detaching the volume or restarting the instance.

### Point in time recovery
<a name="recovery-storage"></a>

 AWS Elastic Disaster Recovery uses Amazon EBS snapshots to give Point in Time (PiT) recovery options that can be used during a drill or recovery. Amazon EBS snapshots of the staging are volumes are continuously taken to provide recovery points of latest (sub-second RPO), 10-minute increments for the first hour, in one hour increments for 24 hours. A daily PiT is retained for the amount of days specified in your Point in Time (PiT) policy. You can specify between 1 to 365 days, with 7 days being the default. For more information, see [Understanding Point In Time states](https://docs.aws.amazon.com/drs/latest/userguide/failback-overview.html#point-in-time-faq).

## Compute
<a name="key-considerations-compute"></a>

You must choose an Amazon EC2 instance type for both the replication server and the recovery server.

**Topics**
+ [Replication servers](#servers-compute)
+ [Drill and recovery instances](#instances-compute)
+ [Source server](#source-servers-compute)

### Replication servers
<a name="servers-compute"></a>

The replication server is normally smaller than the source system. `t3.small` is the default instance type, and it can replicate up to 15 volumes. You can use a shared replication server between SAP application servers, or other servers with low change rates.

If you have a workload that is bursty or has consistently high transaction rate databases, with a high rate of create, update, and/or delete operations that must be applied to its storage, you may require different configurations for the staging area. If you see lag in the replication for your workload, change the default replication server to a different instance family. For example, General Purpose Amazon EC2 instance family or use a dedicated replication server. This change can impact cost. For more information, see [Replication server configuration](https://docs.aws.amazon.com/drs/latest/userguide/replication-server-settings.html).

### Drill and recovery instances
<a name="instances-compute"></a>

For recovery instances, configure the Amazon EC2 launch template settings to match AWS target instances with source. See the following resources for a list of SAP certified instances.
+  [SAP NetWeaver certified instances](https://docs.aws.amazon.com/sap/latest/general/sap-netweaver-aws-ec2.html) 
+  [SAP HANA certified instances](https://docs.aws.amazon.com/sap/latest/general/sap-hana-aws-ec2.html) 

The following are some of the compute-related factors impacting the RTO of your disaster recovery solutions.
+ Server startup time
+ SAP running on Microsoft Windows Server operating system
+ Large SAP HANA database that takes more than 10 minutes to start up
+ SAP application(s) installed on the server, and their startup times
+ Mismatch in the source and target server and storage configurations – configuring a lesser compute power or storage performance at the target side increases the RTO

You must consider application startup times as a factor in recovery. We recommend choosing an Amazon EC2 instance type and storage configuration that provides an effective startup time. This helps your optimize the RTO for your disaster recovery solutions. Also, performing a disaster recovery test or drill enables you to measure the RTO based on your operating system and database.

SAP systems can run on a variety of operating systems, infrastructure platforms, and processor instruction sets. If your source servers is on-premises or with another cloud provider, it must be compatible with Amazon EC2 and Elastic Disaster Recovery. The source server must have a 64-bit based operating system built for the x86 system architecture. Various x86 based CPUs are available on AWS, being used on source servers, especially if the servers are old models. Using an SAP sizing-based approach to map the source system to an Amazon EC2 instance type is recommended. To learn more, see SAP’s [Sizing](https://www.sap.com/about/benchmark.html) information.

### Source server
<a name="source-servers-compute"></a>

While the system requirements for the Replication Agent are relatively low, consider the constraints on the source server for CPU, memory, network, storage, and other resources that can impact the performance of your disaster recovery solution. Size the source server based on these factors. For more information, see [Source server requirements](https://docs.aws.amazon.com/drs/latest/userguide/installation-requiremets.html#general-requirements2).