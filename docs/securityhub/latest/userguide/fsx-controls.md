# Security Hub controls for Amazon FSx

These AWS Security Hub controls evaluate the Amazon FSx service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [FSx.1] FSx for OpenZFS file systems should be configured to copy tags to backups and volumes

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2,
NIST.800-53.r5 CM-2(2)

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:**
[fsx-openzfs-copy-tags-enabled](../../../config/latest/developerguide/fsx-openzfs-copy-tags-enabled.md "../../../config/latest/developerguide/fsx-openzfs-copy-tags-enabled.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon FSx for OpenZFS file system is configured to copy tags to backups and volumes. The control fails if the OpenZFS file system isn't configured to copy tags to backups and volumes.

Identification and inventory of your IT assets is an important aspect of governance and security. Tags help you
categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have
many resources of the same type because you can quickly identify a specific resource based on the tags that you assigned to it.

### Remediation

For information about configuring an FSx for OpenZFS file system to copy tags to backups and volumes, see [Updating a file system](../../../fsx/latest/OpenZFSGuide/updating-file-system.md "../../../fsx/latest/OpenZFSGuide/updating-file-system.md") in the _Amazon FSx for OpenZFS User Guide_.

## [FSx.2] FSx for Lustre file systems should be configured to copy tags to backups

**Related requirements:** NIST.800-53.r5 CP-9, NIST.800-53.r5 CM-8

**Category:** Identify > Inventory > Tagging

**Severity:** Low

**Resource type:** `AWS::FSx::FileSystem`

**AWS Config rule:**
[fsx-lustre-copy-tags-to-backups](../../../config/latest/developerguide/fsx-lustre-copy-tags-to-backups.md "../../../config/latest/developerguide/fsx-lustre-copy-tags-to-backups.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether an Amazon FSx for Lustre file system is configured to copy tags to backups and volumes. The
control fails if the Lustre file system isn't configured to copy tags to backups and volumes.

Identification and inventory of your IT assets is an important aspect of governance and security. Tags help you
categorize your AWS resources in different ways, for example, by purpose, owner, or environment. This is useful when you have
many resources of the same type because you can quickly identify a specific resource based on the tags that you assigned to it.

### Remediation

For information about configuring an FSx for Lustre file system to copy tags to backups, see [Copying backups within the same AWS account](../../../fsx/latest/LustreGuide/copying-backups-same-account.md "../../../fsx/latest/LustreGuide/copying-backups-same-account.md") in the _Amazon FSx for Lustre User Guide_.

## [FSx.3] FSx for OpenZFS file systems should be configured for Multi-AZ deployment

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::FSx::FileSystem`

**AWS Config rule:**
[fsx-openzfs-deployment-type-check](../../../config/latest/developerguide/fsx-openzfs-deployment-type-check.md "../../../config/latest/developerguide/fsx-openzfs-deployment-type-check.md")

**Schedule type:** Periodic

**Parameters:**
`deploymentTypes: MULTI_AZ_1` (not customizable)

This control checks whether an Amazon FSx for OpenZFS file system is configured to use the multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use the Multi-AZ deployment type.

Amazon FSx for OpenZFS supports several deployment types for file systems: _Multi-AZ (HA)_, _Single-AZ (HA)_, and _Single-AZ (non-HA)_. The deployment types offer different levels of availability and durability. Multi-AZ (HA) file systems are composed of a high-availability (HA) pair of file servers that are spread across two Availability Zones (AZs). We recommend using the Multi-AZ (HA) deployment type for most production workloads due to the high availability and durability model that it provides.

### Remediation

You can configure an Amazon FSx for OpenZFS file system to use the Multi-AZ deployment type when you create the file system. You can't change the deployment type for an existing FSx for OpenZFS file system.

For information about deployment types and options for FSx for OpenZFS file systems, see [Availability and durability for Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/availability-durability.md "../../../fsx/latest/OpenZFSGuide/availability-durability.md") and [Managing file system resources](../../../fsx/latest/OpenZFSGuide/managing-file-systems.md "../../../fsx/latest/OpenZFSGuide/managing-file-systems.md") in the _Amazon FSx for OpenZFS User Guide_.

## [FSx.4] FSx for NetApp ONTAP file systems should be configured for Multi-AZ deployment

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::FSx::FileSystem`

**AWS Config rule:**
[fsx-ontap-deployment-type-check](../../../config/latest/developerguide/fsx-ontap-deployment-type-check.md "../../../config/latest/developerguide/fsx-ontap-deployment-type-check.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter         | Description                                                                                                                                                                         | Type | Allowed custom values      | Security Hub default value |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | -------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deploymentTypes` | A list of deployment types to include in the evaluation. The control generates a `FAILED` finding if a file system isn't configured to use a deployment type specified in the list. | Enum | `MULTI_AZ_1`, `MULTI_AZ_2` | `MULTI_AZ_1`, `MULTI_AZ_2` | This control checks whether an Amazon FSx for NetApp ONTAP file system is configured to use a multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use a Multi-AZ deployment type. You can optionally specify a list of deployment types to include in the evaluation. Amazon FSx for NetApp ONTAP supports several deployment types for file systems: _Single-AZ 1_, _Single-AZ 2_, _Multi-AZ 1_, and _Multi-AZ 2_. The deployment types offer different levels of availability and durability. We recommend using a Multi-AZ deployment type for most production workloads due to the high availability and durability model that Multi-AZ deployment types provide. Multi-AZ file systems support all the availability and durability features of Single-AZ file systems. In addition, they're designed to provide continuous availability to data even when an Availability Zone (AZ) is unavailable. ### Remediation You can't change the deployment type for an existing Amazon FSx for NetApp ONTAP file system. However, you can back up the data, and then restore it on a new file system that uses a Multi-AZ deployment type. For information about deployment types and options for FSx for ONTAP file systems, see [Availability, durability, and deployment options](../../../fsx/latest/ONTAPGuide/high-availability-AZ.md "../../../fsx/latest/ONTAPGuide/high-availability-AZ.md") and [Managing file systems](../../../fsx/latest/ONTAPGuide/managing-file-systems.md "../../../fsx/latest/ONTAPGuide/managing-file-systems.md") in the _FSx for ONTAP User Guide_. ## [FSx.5] FSx for Windows File Server file systems should be configured for Multi-AZ deployment **Category:** Recover > Resilience > High availability **Severity:** Medium **Resource type:** `AWS::FSx::FileSystem` **AWS Config rule:** [fsx-windows-deployment-type-check](../../../config/latest/developerguide/fsx-windows-deployment-type-check.md "../../../config/latest/developerguide/fsx-windows-deployment-type-check.md") **Schedule type:** Periodic **Parameters:** `deploymentTypes: MULTI_AZ_1` (not customizable) This control checks whether an Amazon FSx for Windows File Server file system is configured to use the multiple Availability Zones (Multi-AZ) deployment type. The control fails if the file system isn't configured to use the Multi-AZ deployment type. Amazon FSx for Windows File Server supports two deployment types for file systems: _Single-AZ_ and _Multi-AZ_. The deployment types offer different levels of availability and durability. Single-AZ file systems are composed of a single Windows file server instance and a set of storage volumes within a single Availability Zone (AZ). Multi-AZ file systems are composed of a high-availability cluster of Windows file servers spread across two Availability Zones. We recommend using the Multi-AZ deployment type for most production workloads due to the high availability and durability model that it provides. ### Remediation You can configure an Amazon FSx for Windows File Server file system to use the Multi-AZ deployment type when you create the file system. You can't change the deployment type for an existing FSx for Windows File Server file system. For information about deployment types and options for FSx for Windows File Server file systems, see [Availability and durability: Single-AZ and Multi-AZ file systems](../../../fsx/latest/WindowsGuide/high-availability-multiAZ.md "../../../fsx/latest/WindowsGuide/high-availability-multiAZ.md") and [Getting started with Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/getting-started.md "../../../fsx/latest/WindowsGuide/getting-started.md") in the _Amazon FSx for Windows File Server User Guide_. |
