# `AWS-AttachEBSVolume`

**Description**

Attach an Amazon Elastic Block Store (Amazon EBS) volume to an Amazon Elastic Compute Cloud (Amazon EC2) instance.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AttachEBSVolume "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-AttachEBSVolume")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- Device

Type: String

Description: (Required) The device name (for example, /dev/sdh or xvdh
).

- InstanceId

Type: String

Description: (Required) The ID of the instance where you want to attach
the volume.

- VolumeId

Type: String

Description: (Required) The ID of the Amazon EBS volume. The volume and
instance must be in the same Availability Zone.
