# Troubleshoot impaired Amazon EC2 Windows instance using EC2Rescue

EC2Rescue for Windows Server is an easy-to-use tool that you run on an Amazon EC2 Windows Server
instance to diagnose and troubleshoot possible problems. It is valuable for collecting log
files and troubleshooting issues and also proactively searching for possible areas of
concern. It can even examine Amazon EBS root volumes from other instances and collect relevant
logs for troubleshooting Windows Server instances using that volume. The following are some
common issues that EC2Rescue can address:

- Instance connectivity issues due to firewall, Remote Desktop Protocol (RDP), or
  network interface configuration
- Operating system boot issues due to a stop error, boot loop, or corrupted
  registry
- Issues that might need advanced log analysis and troubleshooting
  EC2Rescue for Windows Server has two different modules:

- A **data collector module** that collects data from all
  different sources
- An **analyzer module** that parses the data collected
  against a series of predefined rules to identify issues and provide suggestions
  The EC2Rescue for Windows Server tool only runs on Amazon EC2 instances running Windows Server 2012
  and later. When the tool starts, it checks whether it is running on an Amazon EC2 instance.

###### Note

The `AWSSupport-ExecuteEC2Rescue` AWS Systems Manager Automation runbook uses the
EC2Rescue tool to troubleshoot and, where possible, fix common connectivity issues with
the specified EC2 instance. For more information, and to run this automation, see
[>AWSSupport-ExecuteEC2Rescue](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-executeec2rescue.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-executeec2rescue.md").

If you are using a Linux instance, see [Troubleshoot impaired Amazon EC2 Linux instance using EC2Rescue](Linux-Server-EC2Rescue.md "Linux-Server-EC2Rescue.md").

###### Topics

- [Troubleshoot using EC2Rescue GUI](ec2rw-gui.md "ec2rw-gui.md")
- [Troubleshoot using EC2Rescue CLI](ec2rw-cli.md "ec2rw-cli.md")
- [Troubleshoot using EC2Rescue and Systems Manager](ec2rw-ssm.md "ec2rw-ssm.md")
