# `AWS-QuarantineEC2Instance`

**Description**

With the `AWS-QuarantineEC2Instance` runbook, you can assign a security group
to an Amazon Elastic Compute Cloud (Amazon EC2) instance that doesn't allow any inbound or outbound traffic.

###### Important

Changes to the RDP settings should be carefully reviewed before running this
runbook.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-QuarantineEC2Instance "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-QuarantineEC2Instance")

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

- InstanceId

Type: String

Description: (Required) The ID of the managed instance to manage the RDP settings
of.

- IsolationSecurityGroup

Type: String

Description: (Required) The name of the security group that you want to assign to
the instance to prevent inbound or outbound traffic.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `autoscaling:DescribeAutoScalingInstances`
- `autoscaling:DetachInstances`
- `ec2:CreateSecurityGroup`
- `ec2:CreateSnapshot`
- `ec2:DescribeInstances`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSnapshots`
- `ec2:ModifyInstanceAttribute`
- `ec2:RevokeSecurityGroupEgress`
- `ec2:RevokeSecurityGroupIngress`

**Document Steps**

- `aws:executeAwsApi` - Gathers details about the instance.
- `aws:executeScript` - Verifies the instance isn't part of an Auto
  Scaling group.
- `aws:executeAwsApi` - Creates a snapshot of the root volume attached to
  the instance.
- `aws:waitForAwsResourceProperty` - Waits for the snapshot state to be
  `completed`.
- `aws:executeAwsApi` - Assigns the security group specified in the
  `IsolationSecurityGroup` parameter to your instance.

**Outputs**

`GetEC2InstanceResources.RevokedSecurityGroupsIds`

`GetEC2InstanceResources.RevokedSecurityGroupsNames`

`createSnapshot.SnapId`
