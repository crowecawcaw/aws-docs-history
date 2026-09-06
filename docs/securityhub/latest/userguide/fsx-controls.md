

# Security Hub CSPM controls for Amazon FSx
<a name="fsx-controls"></a>

These AWS Security Hub CSPM controls evaluate the Amazon FSx service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [FSx.1] FSx for OpenZFS file systems should be configured to copy tags to backups and volumes
<a name="fsx-1"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:** [fsx-openzfs-copy-tags-enabled](https://docs.aws.amazon.com/config/latest/developerguide/fsx-openzfs-copy-tags-enabled.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon FSx for OpenZFS file system is configured to copy tags to backups and volumes. The control fails if the OpenZFS file system isn't configured to copy tags to backups and volumes.

Identification and inventory of your IT assets is an important aspect of governance and security. Tags help you categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type because you can quickly identify a specific resource based on the tags that you assigned to it.

### Remediation
<a name="fsx-1-remediation"></a>

For information about configuring an FSx for OpenZFS file system to copy tags to backups and volumes, see [Updating a file system](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/updating-file-system.html) in the *Amazon FSx for OpenZFS User Guide*.

## [FSx.2] FSx for Lustre file systems should be configured to copy tags to backups
<a name="fsx-2"></a>

**Related requirements:** NIST.800-53.r5 CP-9, NIST.800-53.r5 CM-8

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:** [fsx-lustre-copy-tags-to-backups](https://docs.aws.amazon.com/config/latest/developerguide/fsx-lustre-copy-tags-to-backups.html)

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon FSx for Lustre file system is configured to copy tags to backups and volumes. The control fails if the Lustre file system isn't configured to copy tags to backups and volumes.

Identification and inventory of your IT assets is an important aspect of governance and security. Tags help you categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have many resources of the same type because you can quickly identify a specific resource based on the tags that you assigned to it.

### Remediation
<a name="fsx-2-remediation"></a>

For information about configuring an FSx for Lustre file system to copy tags to backups, see [Copying backups within the same AWS account](https://docs.aws.amazon.com/fsx/latest/LustreGuide/copying-backups-same-account.html) in the *Amazon FSx for Lustre User Guide*.

## [FSx.3] FSx for OpenZFS file systems should be configured for Multi-AZ deployment
<a name="fsx-3"></a>

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:** [fsx-openzfs-deployment-type-check](https://docs.aws.amazon.com/config/latest/developerguide/fsx-openzfs-deployment-type-check.html)

**Schedule type:** Periodic

**Parameters:** `deploymentTypes: MULTI_AZ_1` (not customizable)

This control checks whether an Amazon FSx for OpenZFS file system is configured to use the multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use the Multi-AZ deployment type.

Amazon FSx for OpenZFS supports several deployment types for file systems: *Multi-AZ (HA)*, *Single-AZ (HA)*, and *Single-AZ (non-HA)*. The deployment types offer different levels of availability and durability. Multi-AZ (HA) file systems are composed of a high-availability (HA) pair of file servers that are spread across two Availability Zones (AZs). We recommend using the Multi-AZ (HA) deployment type for most production workloads due to the high availability and durability model that it provides.

### Remediation
<a name="fsx-3-remediation"></a>

You can configure an Amazon FSx for OpenZFS file system to use the Multi-AZ deployment type when you create the file system. You can't change the deployment type for an existing FSx for OpenZFS file system.

For information about deployment types and options for FSx for OpenZFS file systems, see [Availability and durability for Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/availability-durability.html) and [Managing file system resources](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-file-systems.html) in the *Amazon FSx for OpenZFS User Guide*.

## [FSx.4] FSx for NetApp ONTAP file systems should be configured for Multi-AZ deployment
<a name="fsx-4"></a>

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:** [fsx-ontap-deployment-type-check](https://docs.aws.amazon.com/config/latest/developerguide/fsx-ontap-deployment-type-check.html)

**Schedule type:** Periodic

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `deploymentTypes` | A list of deployment types to include in the evaluation. The control generates a `FAILED` finding if a file system isn't configured to use a deployment type specified in the list. | Enum | `MULTI_AZ_1`, `MULTI_AZ_2` | `MULTI_AZ_1`, `MULTI_AZ_2` | 

This control checks whether an Amazon FSx for NetApp ONTAP file system is configured to use a multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use a Multi-AZ deployment type. You can optionally specify a list of deployment types to include in the evaluation.

Amazon FSx for NetApp ONTAP supports several deployment types for file systems: *Single-AZ 1*, *Single-AZ 2*, *Multi-AZ 1*, and *Multi-AZ 2*. The deployment types offer different levels of availability and durability. We recommend using a Multi-AZ deployment type for most production workloads due to the high availability and durability model that Multi-AZ deployment types provide. Multi-AZ file systems support all the availability and durability features of Single-AZ file systems. In addition, they're designed to provide continuous availability to data even when an Availability Zone (AZ) is unavailable.

### Remediation
<a name="fsx-4-remediation"></a>

You can't change the deployment type for an existing Amazon FSx for NetApp ONTAP file system. However, you can back up the data, and then restore it on a new file system that uses a Multi-AZ deployment type.

For information about deployment types and options for FSx for ONTAP file systems, see [Availability, durability, and deployment options](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/high-availability-AZ.html) and [Managing file systems](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-file-systems.html) in the *FSx for ONTAP User Guide*. 

## [FSx.5] FSx for Windows File Server file systems should be configured for Multi-AZ deployment
<a name="fsx-5"></a>

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:** [fsx-windows-deployment-type-check](https://docs.aws.amazon.com/config/latest/developerguide/fsx-windows-deployment-type-check.html)

**Schedule type:** Periodic

**Parameters:** `deploymentTypes: MULTI_AZ_1` (not customizable)

This control checks whether an Amazon FSx for Windows File Server file system is configured to use the multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use the Multi-AZ deployment type.

Amazon FSx for Windows File Server supports two deployment types for file systems: *Single-AZ* and *Multi-AZ*. The deployment types offer different levels of availability and durability. Single-AZ file systems are composed of a single Windows file server instance and a set of storage volumes within a single Availability Zone (AZ). Multi-AZ file systems are composed of a high-availability cluster of Windows file servers spread across two Availability Zones. We recommend using the Multi-AZ deployment type for most production workloads due to the high availability and durability model that it provides.

### Remediation
<a name="fsx-5-remediation"></a>

You can configure an Amazon FSx for Windows File Server file system to use the Multi-AZ deployment type when you create the file system. You can't change the deployment type for an existing FSx for Windows File Server file system.

For information about deployment types and options for FSx for Windows File Server file systems, see [Availability and durability: Single-AZ and Multi-AZ file systems](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/high-availability-multiAZ.html) and [Getting started with Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started.html) in the *Amazon FSx for Windows File Server User Guide*. 