# `AWS-ExtendEbsVolume`

**Description**

The `AWS-ExtendEbsVolume` runbook increases the size of an Amazon EBS volume
and extends the file system. This automation supports the `xfs`
and `ext4` file systems.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ExtendEbsVolume "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-ExtendEbsVolume")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- DriveLetter

Type: String

Description: (Optional) The letter of the drive whose file system you want
to extend. This parameter is required for Windows
instances.

- InstanceId

Type: String

Description: (Optional) The ID of the Amazon EC2 instance that the Amazon EBS volume
you want to extend is attached to.

- KeepSnapshot

Type: Boolean

Default: true

Description: (Optional) Determines whether to keep the snapshot created
before increasing the size of your Amazon EBS volume.

- MountPoint

Type: String

Description: (Optional) The mount point of the drive whose file system you
want to extend. This parameter is required for Linux instances.

- SizeGib

Type: String

Description: (Required) The size in GiB that you want to modify your Amazon EBS
volume to.

- VolumeId

Type: String

Description: (Required) The ID of the EBS volume that you want to
extend.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateSnapshot`
- `ec2:CreateTags`
- `ec2:DeleteSnapshot`
- `ec2:DescribeVolumes`
- `ec2:ModifyVolume`
- `ssm:DescribeInstanceInformation`
- `ssm:GetCommandInvocation`
- `ssm:SendCommand`

**Document Steps**

- `aws:executeScript` - Increases the size of the volume to the
  value that you specify in the `VolumeId` parameter and extends
  the file system.
