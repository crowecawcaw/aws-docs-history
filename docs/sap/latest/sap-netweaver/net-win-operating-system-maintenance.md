# Operating System Maintenance

In general, operating system maintenance across large numbers of EC2 instances can be managed by:

- Tools specific to each operating system, such as Microsoft System Center
- Third-party products, such as those available in AWS Marketplace
- Using AWS Systems Manager

## Patching

You can follow SAP recommended patching processes to update your landscape on AWS. For operating system patching, with [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/systems-manager-patch.md "../../../systems-manager/latest/userguide/systems-manager-patch.md") you can roll out OS patches as per your corporate policies. There are multiple key features like:

- Scheduling based on tags
- Auto-approving patches with lists of approved and rejected patches
- Defining patch baselines

AWS Systems Manager Patch Manager integrates with IAM, AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager Operations Work](../../../systems-manager/latest/userguide/patch-manager-how-it-works.md "../../../systems-manager/latest/userguide/patch-manager-how-it-works.md"). If AWS Systems Manager Patch Manager does not satisfy your requirements, there are third-party products available as well. Some of these products are available in the [AWS Marketplace](https://aws.amazon.com/marketplace "https://aws.amazon.com/marketplace").

## Maintenance Window

[AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md") lets you define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system, updating drivers, installing software, or applying patches.

## Administrator Access

You can access the backend SAP systems for administration purposes using:

- [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md")
- Remote Desktop Protocol (RDP)
- Secure Shell (SSH)
