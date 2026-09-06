

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Replication template reference
<a name="replication-server-settings"></a>

Replication servers are lightweight Amazon EC2 instances that are used to replicate data between your source servers and AWS. Replication servers are automatically launched and terminated as needed. You can modify the behavior of the replication servers by modifying the settings for a single source server or multiple source servers. Alternatively, you can run MGN with the default replication settings.

The replication options, include:
+ The subnet within which the replication server is launched. The subnet can use both IPv4 and IPv6 CIDRs.
+ Replication Server instance type
+ Target storage type (Amazon EBS or FSx for ONTAP)
+ Security groups
+ IP Version - you can choose IPv4 or IPv6.

## Staging area subnet
<a name="subnet"></a>

Choose the **Staging area subnet** that you want to allocate as the staging area subnet for all of your replication servers. If you chose to use IPv6, you must choose a subnet that uses IPv6 CIDRs.

The best practice is to create a single dedicated, separate subnet for all of your migration waves using your AWS account. Learn more about creating subnets in [this AWS VPC article](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html).

If a default subnet does not exist, select a specific subnet. The drop-down menu contains a list of all subnets that are available in the console's AWS Region. 

**Note**  
Changing the subnet does not significantly interfere with ongoing data replication, although there may be a minor delay of several minutes while the servers are moved from one subnet to another. 

### Using multiple subnets
<a name="multiple-subnets"></a>

The best practice is to use a single staging area subnet for all of your migration waves within a single AWS account. You may want to use multiple subnets in certain cases, such as the migration of thousands of servers. 

**Note**  
Using more than one staging area subnet might result in higher compute consumption as more replication servers are needed. 

### Launching replication servers in Availability Zones
<a name="availability-zones"></a>

If you want your replication servers to be launched in a specific Availability Zone, then select or create a subnet in that specific Availability Zone. Learn more about using Availability Zones in [this Amazon Elastic Compute Cloud article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html). 

## Replication server instance type
<a name="instance-type"></a>

Choose the **Replication server instance type**. This determines the instance type and size that is used for the launch of each replication server. 

The best practice is to not change the default replication server instance type unless there is a business need for doing so. By default, AWS Transform MGN uses the **t3.small** instance type. This is the most cost effective instance type and should work well for most common workloads. You can change the replication server instance type to speed up the initial sync of data from your source servers to AWS. Changing the instance type will likely lead to increased compute costs. 

You can choose the **Replication server instance** type from the drop-down menu, which contains all available types. Recommended and commonly used instance types are displayed first. You can also search for a specific instance type in the search box.

You can change the replication server instance type for servers that are replicating too slowly or servers that are constantly busy or experience frequent spikes. These are the most common instance type changes: 
+ Servers with less than 26 disks – Change the instance type to **m5.large**. Increase the instance type to m5.xlarge or higher as needed. 
+ Servers with more than 26 disks, or servers in AWS Regions that do not support m5 instance types – change the instance type to **m4.large**. Increase to m4.xlarge or higher, as needed. 

**Note**  
Changing the replication server instance type will not affect data replication. Data replication will automatically continue from where it left off, using the new instance type you selected.
By default, replication servers are automatically assigned a public IP address from Amazon's public IP space.
Replication Servers are only supported on x86\_64 CPU architecture instance types.

## Dedicated instance for replication server
<a name="dedicated-replication-server"></a>

Choose whether you would like to use a **Dedicated instance for replication server**. 

When an external server is very write-intensive, the replication of data from its disks to a shared Replication Server can interfere with the data replication of other servers. In these cases you should choose the **Use dedicated replication server** option (and also consider changing Replication server instance type).

Otherwise, choose the **Do not use dedicated replication server** option.

**Note**  
Using a dedicated replication server may increase the Amazon EC2 cost you incur during replication. 

## Target storage type
<a name="ebs-volume"></a>

AWS Transform MGN supports two target storage types for replication. You can select the storage type that best suits your workload requirements:
+ **Amazon Elastic Block Store (Amazon EBS)** – The default storage type. Amazon EBS volumes are used by the replication servers. For configuration details, see [Amazon EBS configuration](ebs-storage.md).
+ **Amazon FSx for NetApp ONTAP (FSx for ONTAP)** – Enterprise file storage with NetApp ONTAP capabilities. When selecting FSx for ONTAP, you must provide an FSx Storage Secret ARN and a security group configured for iSCSI access. For setup instructions, see [FSx for ONTAP configuration](fsx-ontap.md).

## Store snapshots in AWS Local Zone
<a name="local-zone-snapshots"></a>

MGN does not require special configuration for Local Zones. If you select a subnet in a Local Zone, MGN launches the replication server in that Local Zone the same way it would in any Availability Zone.

When you replicate to a Local Zone, you can store Amazon EBS snapshots in the Local Zone instead of the parent AWS Region. By default, snapshots of Amazon EBS volumes in a Local Zone are stored in the parent AWS Region. If you replicate to a Local Zone that supports local snapshots, you can store the snapshots locally in the Local Zone to meet data residency requirements.

Local snapshots are supported only in Local Zones where MGN offers this feature. If MGN supports local snapshots in the Local Zone that contains your staging area subnet, the option to store snapshots locally is available. If MGN does not support the Local Zone, the option is not available and snapshots are stored in the parent AWS Region. Local snapshots are supported in the Istanbul, Türkiye Local Zone (eu-central-1-ist-1a), which has the Europe (Frankfurt) Region as its parent Region, and in additional Local Zones.

For more information about local snapshots in Local Zones, see [Local snapshots in Local Zones](https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-localzones.html) in the Amazon EBS User Guide.

## Always use AWS Transform MGN security group
<a name="cirrus-security-group"></a>

Choose whether you would like to **Always use the AWS Transform MGN security group**. 

A security group acts as a virtual firewall, which controls the inbound and outbound traffic of the staging area subnet. 

The best practice is to have AWS Transform MGN automatically attach and monitor the default AWS Transform MGN security group. This group opens inbound TCP Port 1500 for receiving the transferred replicated data. When the default AWS Transform MGN security group is activated, MGN will constantly monitor whether the rules within this security group are enforced, in order to maintain uninterrupted data replication. If these rules are altered, MGN will automatically fix the issue. 

Select the **Always use AWS Transform MGN security group** check box to allow data to flow from your source servers to the replication servers, and to allow the replication servers to communicate their state to the AWS Transform MGN servers. 

To opt out, clear the check box. Clearing the check box is not recommended. 

Additional security groups can be chosen from the Additional security groups dropdown. The list of available security groups changes according to the **Staging area subnet** you selected. 

You can search for a specific security group within the search box.

You can add security groups via the AWS Management Console, and they will appear on the security group drop-down list in the AWS Transform MGN Console. Learn more about AWS security groups in [this VPC article](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html). 

You can use the default AWS Transform MGN security group, or you can select another security group. However, take into consideration that any selected security group that is not the AWS Transform MGN default, will be added to the default group, since the default security group is essential for the operation of MGN. 

## Data routing and throttling
<a name="data-routing"></a>

AWS Transform MGN allows you to control how data is routed from your source servers to the replication servers on AWS through the **Data routing and throttling** settings. 

By default, data is sent from the source servers to the replication servers over the public internet, using the public IP that was automatically assigned to the replication servers. Transferred data is always encrypted in transit.

**Note**  
The **Data routing and throttling** view differs slightly between the replication template view and the individual source server replication settings view, but the instructions apply to both views. 

### Use private IP for data replication
<a name="use-private-ip"></a>

Choose the **Use private IP** option if you want to route the replicated data from your source servers to the staging area subnet through a private network with a VPN, AWS Direct Connect, VPC peering, or another type of existing private connection. 

Choose **Do not use private IP** if you do not want to route the replicated data through a private network. 

**Important**  
Data replication will not work unless you have already set up the VPN, AWS Direct Connect, or VPC peering in the AWS Console. 

**Note**  
Use of private IP is not supported for IPv6.
If you selected the Default subnet, it is highly unlikely that the private IP is used for that subnet. Ensure that Private IP (VPN, AWS Direct Connect, or VPC peering) is used for your chosen subnet if you wish to use this option.
You can safely switch between a private connection and a public connection for individual server settings choosing the **Use private IP** or **Do not use private IP** option, even after data replication has begun. This switch will only cause a short pause in replication, and will not have any long-term effect on the replication.
Choosing the **Use private IP** option will not create a new private connection. 

You should use this option if you want to:
+ Allocate a dedicated bandwidth for replication
+ Use another level of encryption
+ Add another layer of security by transferring the replicated data from one private IP address (source) to another private IP address (on AWS)

#### Network architecture diagram – private IP
<a name="private-link-diagram"></a>

 The following diagram illustrates the high-level interaction between the different replication system components when using private IP or VPC endpoint. 

![MGN network architecture diagram featuring a private link/VPC](http://docs.aws.amazon.com/mgn/latest/ug/images/AWS-MGN-Network-Architecture-Private-Link.png)


#### Create public IP
<a name="public-ip"></a>

When the **Use private IP** option is chosen, you will have the option to create a public IP. Public IPs are used by default. Choose **Create public IP** if you want to create a public IP. Choose **Do not create a public IP** if you do not want to create a public IP. 

### Throttle bandwidth
<a name="route-control"></a>

You can control the amount of network bandwidth used for data replication per server. By default, AWS Transform MGN will use all available network bandwidth utilizing five concurrent connections. 

Choose **Throttle bandwidth** if you want to control the transfer rate of data sent from your source servers to the Replication Servers over TCP Port 1500. Otherwise, choose **Do not throttle bandwidth**. 

If you chose to throttle bandwidth, the **Throttle network bandwidth** (per server, in Mbps) box will appear. Enter your desired bandwidth in Mbps. 

## Replication resources tags
<a name="replication-tags"></a>

Add custom **Replication resources tags** to resources created by AWS Transform MGN in your AWS account. 

These are resources required to facilitate data replication, testing and cutover. Each tag consists of a key and an optional value. You can add a custom tag to all of the AWS resources that are created on your AWS account during the normal operation of AWS Transform MGN.

To add a new tag, take the following steps:

1. Choose **Add new tag**. 

1. Enter a **Custom tag key** and an optional tag value. 

**Note**  
MGN already adds tags to every resource it creates, including service tags and user tags. 

These resources include:
+ Amazon EC2 instances
+ Amazon EC2 launch templates
+ Amazon EBS volumes
+ Snapshots
+ Security groups (optional)

Learn more about AWS Tags in [this Amazon EC2 article](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html). 