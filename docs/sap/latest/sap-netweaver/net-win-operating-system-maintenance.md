

# Operating System Maintenance
<a name="net-win-operating-system-maintenance"></a>

In general, operating system maintenance across large numbers of EC2 instances can be managed by:
+ Tools specific to each operating system, such as Microsoft System Center
+ Third-party products, such as those available in AWS Marketplace
+ Using AWS Systems Manager

## Patching
<a name="net-win-patching"></a>

You can follow SAP recommended patching processes to update your landscape on AWS. For operating system patching, with [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) you can roll out OS patches as per your corporate policies. There are multiple key features like:
+ Scheduling based on tags
+ Auto-approving patches with lists of approved and rejected patches
+ Defining patch baselines

 AWS Systems Manager Patch Manager integrates with IAM, AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager Operations Work](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works.html). If AWS Systems Manager Patch Manager does not satisfy your requirements, there are third-party products available as well. Some of these products are available in the [AWS Marketplace](https://aws.amazon.com/marketplace).

## Maintenance Window
<a name="net-win-maintenance-window"></a>

 [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) lets you define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system, updating drivers, installing software, or applying patches.

## Administrator Access
<a name="net-win-administrator-access"></a>

You can access the backend SAP systems for administration purposes using:
+  [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) 
+ Remote Desktop Protocol (RDP)
+ Secure Shell (SSH)