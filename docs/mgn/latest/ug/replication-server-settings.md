NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Replication template reference

Replication servers are lightweight Amazon EC2 instances that are used to replicate
data between your source servers and AWS. Replication servers are automatically
launched and terminated as needed. You can modify the behavior of the replication
servers by modifying the settings for a single source server or multiple source
servers. Alternatively, you can run MGN with the default replication
settings.

The replication options, include:

- The subnet within which the replication server is launched. The subnet can
  use both IPv4 and IPv6 CIDRs.
- Replication Server instance type
- Target storage type (Amazon EBS or FSx for ONTAP)
- Security groups
- IP Version - you can choose IPv4 or IPv6.

## Staging area subnet

Choose the **Staging area subnet** that you want
to allocate as the staging area subnet for all of your replication servers. If you chose to
use IPv6, you must choose a subnet that uses IPv6 CIDRs.

The best practice is to create a single dedicated, separate subnet for all of
your migration waves using your AWS account. Learn more about creating subnets
in [this AWS VPC article](../../../vpc/latest/userguide/working-with-vpcs.md "../../../vpc/latest/userguide/working-with-vpcs.md").

If a default subnet does not exist, select a specific subnet. The drop-down
menu contains a list of all subnets that are available in the console's
AWS Region.

###### Note

Changing the subnet does not significantly interfere with ongoing data
replication, although there may be a minor delay of several minutes while
the servers are moved from one subnet to another.

### Using multiple subnets

The best practice is to use a single staging area subnet for all of your
migration waves within a single AWS account. You may want to use multiple
subnets in certain cases, such as the migration of thousands of servers.

###### Note

Using more than one staging area subnet might result in higher compute
consumption as more replication servers are needed.

### Launching replication servers in Availability Zones

If you want your replication servers to be launched in a specific
Availability Zone, then select or create a subnet in that specific
Availability Zone. Learn more about using Availability Zones in [this Amazon Elastic Compute Cloud article](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md").

## Replication server instance type

Choose the **Replication server instance type**.
This determines the instance type and size that is used for the launch
of each replication server.

The best practice is to not change the default replication server instance
type unless there is a business need for doing so. By default, AWS Transform MGN uses the **t3.small** instance type. This is the most
cost effective instance type and should work well for most common workloads. You
can change the replication server instance type to speed up the initial sync of
data from your source servers to AWS. Changing the instance type will likely
lead to increased compute costs.

You can choose the **Replication server
instance** type from the drop-down menu, which
contains all available types. Recommended and commonly used instance
types are displayed first. You can also search for a specific instance type in the search box.

You can change the replication server instance type for servers that are
replicating too slowly or servers that are constantly busy or experience
frequent spikes. These are the most common instance type changes:

- Servers with less than 26 disks – Change the instance type to
  **m5.large**. Increase the instance type to m5.xlarge or higher as needed.
- Servers with more than 26 disks, or servers in AWS Regions that do
  not support m5 instance types – change the instance type to **m4.large**.
  Increase to m4.xlarge or higher, as needed.

###### Note

- Changing the replication server instance type will not affect data
  replication. Data replication will automatically continue from where
  it left off, using the new instance type you selected.
- By default, replication servers are automatically assigned a
  public IP address from Amazon's public IP space.
- Replication Servers are only supported on x86\_64 CPU architecture
  instance types.

## Dedicated instance for replication server

Choose whether you would like to use a **Dedicated
instance for replication server**.

When an external server is very write-intensive, the replication of data from
its disks to a shared Replication Server can interfere with the data replication
of other servers. In these cases you should choose the **Use
dedicated replication server** option (and also consider changing
Replication server instance type).

Otherwise, choose the **Do not use dedicated replication
server** option.

###### Note

Using a dedicated replication server may increase the Amazon EC2 cost you incur
during replication.

## Target storage type

AWS Transform MGN supports two target storage types for replication. You can select
the storage type that best suits your workload requirements:

- **Amazon Elastic Block Store (Amazon EBS)** – The default
  storage type. Amazon EBS volumes are used by the replication servers. For
  configuration details, see
  [Amazon EBS configuration](ebs-storage.md "ebs-storage.md").
- **Amazon FSx for NetApp ONTAP (FSx for ONTAP)** – Enterprise file
  storage with NetApp ONTAP capabilities. When selecting FSx for ONTAP, you
  must provide an FSx Storage Secret ARN and a security group configured for
  iSCSI access. For setup instructions, see
  [FSx for ONTAP configuration](fsx-ontap.md "fsx-ontap.md").

## Store snapshots in AWS Local Zone

MGN does not require special configuration for Local Zones. If you select
a subnet in a Local Zone, MGN launches the replication server in that Local
Zone the same way it would in any Availability Zone.

When you replicate to a Local Zone, you can store Amazon EBS snapshots in the
Local Zone instead of the parent AWS Region. By default, snapshots of Amazon EBS
volumes in a Local Zone are stored in the parent AWS Region. If you replicate
to a Local Zone that supports local snapshots, you can store the snapshots
locally in the Local Zone to meet data residency requirements. This setting is
available only when the staging area subnet is in a supported Local Zone. For
more information about local snapshots in Local Zones, see [Local snapshots in Local Zones](../../../ebs/latest/userguide/snapshots-localzones.md "../../../ebs/latest/userguide/snapshots-localzones.md") in the Amazon EBS User
Guide.

## Always use Application Migration Service security group

Choose whether you would like to **Always use the
Application Migration Service security group**.

A security group acts as a virtual firewall, which controls the inbound and
outbound traffic of the staging area subnet.

The best practice is to have AWS Transform MGN automatically attach and monitor the
default Application Migration Service Security Group. This group opens inbound
TCP Port 1500 for receiving the transferred replicated data. When the default
Application Migration Service Security Group is activated, MGN will constantly
monitor whether the rules within this security group are enforced, in order to
maintain uninterrupted data replication. If these rules are altered, MGN will
automatically fix the issue.

Select the **Always use Application Migration Service
security group** option to allow data to flow from your source
servers to the replication servers, and that the replication servers can
communicate their state to the AWS Transform MGN servers.

Otherwise, select the **Do not use Application Migration
Service security group option**. Selecting this option is not
recommended.

Additional security groups can be chosen from the Additional security groups
dropdown. The list of available security groups changes according to the
**Staging area subnet** you selected.

You can search for a specific security group within the search box.

You can add security groups via the AWS Management Console, and they will appear on the
security group drop-down list in the AWS Transform MGN Console. Learn more about AWS
security groups in [this VPC article](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md").

You can use the default Application Migration Service security group, or you
can select another security group. However, take into consideration that any
selected security group that is not the Application Migration Service default,
will be added to the default group, since the default security group is
essential for the operation of MGN.

## Data routing and throttling

AWS Transform MGN allows you to control how data is routed from your source servers to
the replication servers on AWS through the **Data routing
and throttling** settings.

By default, data is sent from the source servers to the replication servers
over the public internet, using the public IP that was automatically assigned to
the replication servers. Transferred data is always encrypted in transit.

###### Note

The **Data routing and throttling** view
differs slightly between the replication template view and the individual
source server replication settings view, but the instructions apply to both
views.

### Use private IP for data replication

Choose the **Use private IP** option if you
want to route the replicated data from your source servers to the staging
area subnet through a private network with a VPN,
AWS Direct Connect, VPC peering, or another type of existing
private connection.

Choose **Do not use private IP** if you do
not want to route the replicated data through a private network.

###### Important

Data replication will not work unless you have already set up the VPN,
AWS Direct Connect, or VPC peering in the AWS Console.

###### Note

- Use of private IP is not supported for IPv6.
- If you selected the Default subnet, it is highly unlikely that
  the private IP is used for that subnet. Ensure that Private IP
  (VPN, AWS Direct Connect, or VPC peering) is used for
  your chosen subnet if you wish to use this option.
- You can safely switch between a private connection and a
  public connection for individual server settings choosing the
  **Use private IP** or **Do not use private IP** option, even
  after data replication has begun. This switch will only cause a
  short pause in replication, and will not have any long-term
  effect on the replication.
- Choosing the **Use private IP**
  option will not create a new private connection.

You should use this option if you want to:

- Allocate a dedicated bandwidth for replication
- Use another level of encryption
- Add another layer of security by transferring the replicated data
  from one private IP address (source) to another private IP address
  (on AWS)

#### Network architecture diagram – private IP

The following diagram illustrates the high-level interaction between
the different replication system components when using private IP or VPC
endpoint.

![MGN network architecture diagram featuring a private link/VPC](images/AWS-MGN-Network-Architecture-Private-Link.png)

#### Create public IP

When the **Use private IP** option is
chosen, you will have the option to create a public IP. Public IPs are
used by default. Choose **Create public
IP** if you want to create a public IP. Choose **Do not create a public IP** if you do not want
to create a public IP.

### Throttle bandwidth

You can control the amount of network bandwidth used for data replication
per server. By default, AWS Transform MGN will use all available network bandwidth
utilizing five concurrent connections.

Choose **Throttle bandwidth** if you want to
control the transfer rate of data sent from your source servers to the
Replication Servers over TCP Port 1500. Otherwise, choose **Do not throttle bandwidth**.

If you chose to throttle bandwidth, the **Throttle
network bandwidth** (per server, in Mbps) box will appear.
Enter your desired bandwidth in Mbps.

## Replication resources tags

Add custom **Replication resources tags** to
resources created by AWS Transform MGN in your AWS account.

These are resources required to facilitate data replication, testing and
cutover. Each tag consists of a key and an optional value. You can add a custom
tag to all of the AWS resources that are created on your AWS account during
the normal operation of AWS Transform MGN.

To add a new tag, take the following steps:

1. Choose **Add new tag**.
2. Enter a **Custom tag key** and an
   optional tag value.

###### Note

MGN already adds tags to every resource it creates, including service
tags and user tags.

These resources include:

- Amazon EC2 instances
- Amazon EC2 launch templates
- Amazon EBS volumes
- Snapshots
- Security groups (optional)

Learn more about AWS Tags in [this Amazon EC2 article](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").
