# Update management for Amazon EC2 instances

We recommend that you regularly patch, update, and secure the operating system and
applications on your EC2 instances. You can use [AWS Systems Manager Patch
Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md") to automate the process of installing security-related updates for both the
operating system and applications.

For EC2 instances in an Auto Scaling group, you can use the [AWS-PatchAsgInstance](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-patchasginstance.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-patchasginstance.md") runbook to help avoid instances that are
undergoing patching from being replaced. Alternatively, you can use any automatic update
services or recommended processes for installing updates that are provided by the application
vendor.

###### Resources

- AL2023 – [Updating AL2023](../../../linux/al2023/ug/updating.md "../../../linux/al2023/ug/updating.md") in the
  _Amazon Linux 2023 User Guide_
- AL2 – [Manage software on your Amazon Linux 2 instance](../../../linux/al2/ug/managing-software.md "../../../linux/al2/ug/managing-software.md")
  in the _Amazon Linux 2 User Guide_
- Windows instances – [Update management](ec2-windows-security-best-practices.md#ec2-windows-update-management "ec2-windows-security-best-practices.md#ec2-windows-update-management")
