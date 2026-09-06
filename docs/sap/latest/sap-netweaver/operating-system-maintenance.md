

# Operating System Maintenance
<a name="operating-system-maintenance"></a>

In general, operating system maintenance across large estates of EC2 instances can be managed by:
+ Tools specific to each operating system, such as Microsoft System Center 2019
+ Third-party products, such as those available on AWS Marketplace
+  AWS Systems Manager

 AWS Systems Manager can help with the following key operating system maintenance tasks.

## Patching
<a name="patching"></a>

You can follow SAP recommended patching processes to update your landscape on AWS. For operating system patching, use [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) to roll out OS patches as per your corporate policies. Patch manager includes features like:
+ Scheduling based on tags
+ Auto-approving patches with lists of approved and rejected patches
+ Defining patch baselines

 AWS Systems Manager Patch Manager integrates with AWS Identity and Access Management (IAM), AWS CloudTrail, and Amazon CloudWatch Events to provide a secure patching experience that includes event notifications and the ability to audit usage. For details about the process, see [How Patch Manager Operations Work](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works.html). If AWS Systems Manager Patch Manager does not fulfil your requirements, there are third-party products available on the [AWS Marketplace](https://aws.amazon.com/marketplace).

## Maintenance Window
<a name="maintenance-window"></a>

 [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html) let you define a schedule for when to perform potentially disruptive actions on your instances, such as patching an operating system, updating drivers, or installing software or patches.

## Automation using Documents
<a name="automation-using-documents"></a>

 [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) simplifies common maintenance and deployment tasks of Amazon EC2 instances and other AWS resources. Automation enables you to do the following:
+ Build Automation workflows to configure and manage instances and AWS resources.
+ Create custom workflows or use pre-defined workflows maintained by AWS.
+ Receive notifications about Automation tasks and workflows by using Amazon CloudWatch Events.
+ Monitor Automation progress and execution details by using the Amazon EC2 or the AWS Systems Manager console.

There are many AWS provided documents specific to Windows already available.