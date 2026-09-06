

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Storage related FAQs
<a name="Storage-Related-FAQ"></a>

This section contains answers to frequently asked questions about storage options in AWS Transform MGN.

## What target storage types does MGN support?
<a name="faq-storage-types"></a>

MGN supports two target storage types:
+ **Amazon EBS** – The default storage type. Source server disks are replicated to Amazon EBS volumes and launched as standard Amazon EC2 instances with Amazon EBS attached storage.
+ **Amazon FSx for NetApp ONTAP** – Data volumes are replicated to an FSx for ONTAP file system and attached to the target instance via iSCSI. The boot volume always remains on Amazon EBS.

You configure the target storage type in the replication template or per-server replication settings.

## Can I use FSx for ONTAP for some servers and Amazon EBS for others?
<a name="faq-fsx-ebs-mix"></a>

Yes. The target storage type is configured at the replication template level and can be overridden per source server. You can migrate some servers to FSx for ONTAP and others to Amazon EBS within the same account and region.

## Do I need to pre-install iSCSI packages on my source server?
<a name="faq-fsx-iscsi-packages"></a>

MGN automatically installs iSCSI initiator and multipath packages on the target instance during the post-boot conversion. However, you must pre-install these packages on the source server if:
+ The target instance does not have network access to OS package repositories (air-gapped environments or private subnets without a NAT gateway).
+ The operating system uses subscription-based repositories (SUSE SLES, RHEL, CentOS) where credentials are tied to the source instance.

For the required packages by operating system, see the [Supported Linux operating systems](Supported-Operating-Systems.md#Supported-Operating-Systems-Linux) table and the [FSx ONTAP configuration guide](fsx-ontap.md).

## What happens to FSx replication volumes after finalize cutover?
<a name="faq-fsx-replication-volumes-after-cutover"></a>

After finalize cutover, MGN creates a FlexClone of the replication volume, splits it to make it independent, and then deletes the original replication volume. The target volume (FlexClone) remains attached to your cutover instance. This process is automatic and typically completes within minutes, though it may take longer for large volumes.

## I initialized MGN before FSx for ONTAP support was available. Do I need to do anything?
<a name="faq-fsx-reinitialize"></a>

Yes. You must reinitialize MGN to create the required AWS managed roles (`AWSApplicationMigrationFsxProxyRole` and `AWSApplicationMigrationFsxProxyLinkRole`). In the MGN console, navigate to [Getting started](getting-started.md) and choose **Reinitialize**.