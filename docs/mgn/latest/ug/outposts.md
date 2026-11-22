

# Migrating to AWS Outposts

AWS Outposts brings AWS infrastructure and services to your on-premises data center. An Outpost operates as an extension of an AWS Region and hosts subnets, Amazon EBS volumes, and Amazon EC2 instances that are associated with resources in the parent Region. With AWS Transform MGN, you can use an Outpost as a replication and cutover target for your migration.

This topic describes the Outpost-specific behavior, constraints, and settings that apply when you migrate to an Outpost. For the standard migration workflow, see the rest of this guide.

## Downloading the AWS Replication Agent
<a name="outposts-agent-download"></a>

The AWS Replication Agent installation file (both the initial download and any subsequent full agent download) always comes from the public Amazon S3 URL. This requires connectivity from the source server to the parent AWS Region. AWS PrivateLink is supported for this download. This transfer is the agent installation file only. No replication data is transferred during the download.

## Staging storage
<a name="outposts-snapshot-storage"></a>

Staging storage holds your replication data, including the snapshots that MGN creates during the staging and cutover processes. The staging storage location is determined by the [staging area subnet](replication-server-settings.md#subnet) that you choose in the [replication settings](replication-settings-template.md). When the staging area subnet is on an Outpost, you choose where snapshots are stored with the **Outpost snapshot storage** setting. The location applies to all snapshots that MGN creates for the source server.
+ **Store on Outpost** – Replicated data goes from your source environment to the Outpost and stays there. Only control traffic goes to the parent AWS Region, for example source server metadata and the calls from the replication servers to MGN. If you use post-launch actions with AWS Systems Manager, the command output is also sent to the Region. This option requires Amazon S3 on Outposts. On first-generation (Gen1) Outposts, it's the default when your Outpost has Amazon S3 on Outposts. Local storage uses your Outpost capacity, so size your migration waves so that the snapshots for each wave fit in the available capacity. For more information, see [What is Amazon S3 on Outposts?](https://docs.aws.amazon.com/AmazonS3/latest/s3-outposts/S3onOutposts.html) in the *Amazon S3 on Outposts User Guide*.
+ **Store in AWS Region** – Replicated data goes from your source environment to the replication servers on the Outpost. MGN stores the snapshots in Amazon S3 in the parent AWS Region, and the snapshot data goes over the Outpost service link. Use this option if your Outpost doesn't support local snapshots, which require Amazon S3 on Outposts.

**Note**  
On second-generation (Gen2) Outposts, snapshots must be stored in the AWS Region. Use **Store in AWS Region**.

**Important**  
Changing the snapshot storage location after replication starts triggers a full resync. Snapshots in the previous location can no longer be used.

If you move the staging area subnet to a different Outpost, from an Outpost to the Region, or from the Region to an Outpost, MGN creates new staging volumes in the new location. With **Store on Outpost**, the existing snapshots can't be used in a different location, and MGN replicates the data again. With **Store in AWS Region**, MGN creates the new staging volumes from the existing snapshots.

## Replication settings for Outposts
<a name="outposts-replication-settings"></a>

To migrate to an Outpost, select a subnet within the Outpost as your [staging area subnet](replication-server-settings.md#subnet). When you select an Outpost subnet, MGN validates the remaining replication settings against what is available on that Outpost:
+ **Instance type** – The replication server instance type must be available on the Outpost.
+ **Disk types** – For the staging disks, you can use **Auto** or GP2 on all Outposts, and GP3 on second-generation (Gen2) Outposts. For large disks, the default staging disk type must be GP2, or GP3 on a Gen2 Outpost.
+ **Disk limits** – A staging disk on an Outpost can be at most 16 TiB, for every disk type, including **Auto** and GP3 on a Gen2 Outpost. A source disk larger than 16 TiB can't be staged or launched on an Outpost, even though MGN supports source disks up to 64 TiB in a Region. A GP3 staging disk can have at most 16,000 IOPS and 1,000 MiB/s throughput. For the limits in a Region, see [Disk size by staging disk type](ebs-storage.md#staging-disk-size).
+ **Security groups** – Security groups must match the selected subnet.
+ **Encryption** – Encryption is required and can't be set to **None**.
+ **Snapshot storage** – You must select an **Outpost snapshot storage** location. **Store on Outpost** requires Amazon S3 on Outposts.
+ **Local Zone snapshot storage** – You can't store snapshots in a Local Zone when the staging area subnet is on an Outpost.

When you move the staging area subnet to an Outpost, MGN validates all replicating disks of the source server against these limits.

The AWS Replication Agent installer accepts disks up to 64 TiB, because it doesn't know where the server will stage. MGN checks the disk sizes when you save the replication settings of a server, for each disk including disks set to **Auto**, and when you move the staging area subnet to an Outpost, for all disks of the server. If a disk is too large, MGN displays the following error:

**The {{size}} GiB disk size is too large. The maximum disk size on an Outpost is 16384 GiB. See https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html.**

When you plan capacity, account for more than the staging volumes. Launching test and cutover instances on an Outpost requires free Amazon EBS capacity of about twice the size of the source server disks. For more information, see [Launch settings for Outposts](#outposts-launch-settings).

If the required replication instance type is unavailable because you have reached a capacity limit on the Outpost, MGN displays the following error:

**Data replication is stalled as you have reached a resource limit in your staging area.**

## Launch settings for Outposts
<a name="outposts-launch-settings"></a>

The following [launch settings](launch-settings.md) are supported when you launch test and cutover instances on an Outpost:
+ Start instance upon launch
+ Copy private IP
+ Transfer server tags
+ Bring your own license (BYOL) for Windows servers

MGN validates the following [EC2 launch template](ec2-launch.md) settings against the Outpost before the launch:
+ **Subnet** – Must be on the same Outpost as the staging area subnet. You can't launch to a different Outpost or outside the Outpost. If the staging area subnet is in the AWS Region, you can't launch to an Outpost.
+ **Security groups** – Must match the subnet.
+ **Instance type** – Must be available on the Outpost.
+ **Capacity** – The Outpost must have enough capacity for all servers in the launch: instances of the selected instance type, Amazon EBS capacity, Amazon S3 on Outposts capacity (with **Store on Outpost**), and free IP addresses in the subnets.

If a setting doesn't match the Outpost, MGN fails the launch of that server. The other servers in the launch continue.

MGN creates the launched Amazon EBS volumes with the volume types that the Outpost supports. On first-generation (Gen1) Outposts, all volumes are GP2. On Gen2 Outposts, GP2 volumes stay GP2, and other volume types are GP3. MGN limits GP3 IOPS and throughput to what Outposts supports. A volume initialization rate is not applied on an Outpost. Launching on an Outpost has the same 16 TiB disk limit as staging.

Launching test and cutover instances on an Outpost requires free Amazon EBS capacity of about twice the size of the source server disks, in addition to the staging volumes. The conversion server uses one copy, and the launched instance uses the other. Before a launch, MGN checks the free capacity of the Outpost for all servers in the launch. If the Outpost doesn't have enough capacity, MGN fails the launch of the server with the following error:

**Outpost {{Outpost ARN}} does not have sufficient {{resource}} for this launch. The launch needs {{required}}, and the available quantity is {{available}}. Make more {{resource}} available, or launch fewer servers at the same time.**

## Permissions for Outposts
<a name="outposts-permissions"></a>

When the staging area subnet is on an Outpost, MGN uses the following read-only actions to validate the Outpost and to check its capacity before a launch. MGN calls these actions with the permissions of the principal that calls MGN.


**Actions that MGN uses for Outposts**  

| Action | Use | 
| --- | --- | 
| `ec2:DescribeInstanceTypeOfferings` | Find the instance types that are available on the Outpost. | 
| `s3-outposts:ListOutpostsWithS3` | Find whether the Outpost has Amazon S3 on Outposts, which **Store on Outpost** requires. | 
| `cloudwatch:GetMetricData` | Read the capacity metrics of the Outpost before a launch. | 

The `AWSApplicationMigrationFullAccess` managed policy includes these actions. If you use your own policies, add these actions to the principals that call MGN. You can limit `cloudwatch:GetMetricData` to calls that MGN makes for you with the `aws:CalledVia` condition key:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MgnOutpostsValidation",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstanceTypeOfferings",
                "s3-outposts:ListOutpostsWithS3"
            ],
            "Resource": "*"
        },
        {
            "Sid": "MgnOutpostsCapacityCheck",
            "Effect": "Allow",
            "Action": "cloudwatch:GetMetricData",
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": "mgn.amazonaws.com"
                }
            }
        }
    ]
}
```

If `ec2:DescribeInstanceTypeOfferings` or `s3-outposts:ListOutpostsWithS3` is denied, MGN rejects the replication settings. Before a launch, MGN skips a capacity check that it can't run, and the launch can fail later if the Outpost doesn't have enough capacity. MGN always blocks a launch to a location that doesn't match the staging area.

## Data that goes to the Region
<a name="outposts-data-flow"></a>

Replicated data always goes from your source servers to the replication servers on the Outpost, whichever snapshot storage option you choose.

The following always go to the parent AWS Region:
+ Control traffic, such as source server metadata and the calls from the replication servers to MGN, over TCP port 443.
+ The AWS Replication Agent installation file, which is downloaded from the public Amazon S3 URL in the Region. AWS PrivateLink is supported.
+ Command output from post-launch actions, if you use post-launch actions with AWS Systems Manager.

Snapshots depend on the **Outpost snapshot storage** setting:
+ **Store on Outpost** – Snapshots are stored on the Outpost in Amazon S3 on Outposts. No snapshot data goes to the Region.
+ **Store in AWS Region** – Snapshots are stored in Amazon S3 in the parent Region, and the snapshot data goes over the Outpost service link.

Second-generation (Gen2) Outposts don't support local snapshots. On a Gen2 Outpost, use **Store in AWS Region**.

The route that replicated data takes from your source servers to the Outpost depends on your network. With public IP routing, replication traffic leaves your premises before it reaches the Outpost. To make sure that your replication data goes directly to the Outpost, use private IP connectivity. For more information, see [Architecture diagram for migration to Outposts](#outposts-network-architecture).

## Considerations and constraints
<a name="outposts-considerations"></a>

Review the following considerations and constraints before you migrate to an Outpost:
+ **Outposts racks only** – MGN supports Outposts racks. Outposts servers aren't supported.
+ **Instance types** – Only the instance types available on your Outpost are supported. The available types are a subset of the Nitro-based instance types and depend on the hardware configuration of your Outpost.
+ **Amazon EBS storage** – You must have Amazon EBS storage available on the Outpost rack.
+ **Amazon EBS volume types** – Only the Amazon EBS volume types available on your Outpost are supported (Gen1 Outposts support GP2; Gen2 Outposts support GP2 and GP3). Disks on an Outpost can be at most 16 TiB, which is lower than the 64 TiB limit for migrations to an AWS Region.
+ **Storage capacity** – Outpost storage is finite and managed by you. Plan your migration waves so that each wave fits within the capacity available on the Outpost.
+ **Capacity release delay** – After you delete local snapshots and the volumes that use them, the Amazon S3 on Outposts capacity can take up to 72 hours to become available. With **Store on Outpost**, delete test instances well before your maintenance window, and move servers to **Ready for cutover** early enough for capacity to free up before you launch cutover instances.
+ **Encryption** – Amazon EBS encryption is required. You cannot set encryption to **None** when the staging area is on an Outpost. You can use the AWS managed key (`aws/ebs`) or your own symmetric customer managed key in AWS KMS. Snapshots are encrypted with the same key as their volumes. If you change the encryption key, MGN can't use the existing snapshots and replicates the data again with the new key.
+ **No IPv6 support** – Migration to Outposts does not support IPv6.
+ **No FSx for ONTAP support** – Migration to Outposts does not support FSx for ONTAP as a target.

## Architecture diagram for migration to Outposts
<a name="outposts-network-architecture"></a>

The following diagram shows the MGN network architecture when you migrate to an Outpost. The AWS Replication Agent on each source server communicates with MGN in the parent AWS Region over TCP port 443 and sends replicated data to the replication servers in the staging area subnet on the Outpost over TCP port 1500. The Outpost communicates with the parent Region over TCP port 443. Snapshots are stored either locally on the Outpost or in Amazon S3 in the parent Region, depending on your snapshot storage setting.

To make sure that your replication data goes directly to the Outpost, you can use private IP connectivity between your source servers and the replication servers on the Outpost, for example the Outpost local gateway, AWS Direct Connect, or a VPN. With public IP routing, replication traffic leaves your premises before it reaches the Outpost.

![MGN network architecture for migration to an Outpost. Source servers with the AWS Replication Agent send control traffic to MGN in the AWS Region and replicated data to replication servers in the staging area subnet on the Outpost. Test and cutover instances run in a migrated resources subnet on the same Outpost. Snapshots are stored locally on the Outpost or in Amazon S3 in the AWS Region.](https://docs.aws.amazon.com/mgn/latest/ug/images/outposts-network-architecture.png)
