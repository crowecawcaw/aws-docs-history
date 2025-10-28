# `AWSConfigRemediation-ModifyEBSVolumeType`

**Description**

The `AWSConfigRemediation-ModifyEBSVolumeType` runbook modifies the
volume type of an Amazon Elastic Block Store (Amazon EBS) volume. After the volume type is modified, the
volume enters an `optimizing` state. For information about monitoring the
progress of volume modifications, see [Monitor the progress of
volume modifications](../../../AWSEC2/latest/UserGuide/monitoring-volume-modifications.md "../../../AWSEC2/latest/UserGuide/monitoring-volume-modifications.md") in the _Amazon EC2 User Guide_ .

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ModifyEBSVolumeType "https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-ModifyEBSVolumeType")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf.

- EbsVolumeId

Type: String

Description: (Required) The ID of the Amazon EBS volume that you want to
modify.

- EbsVolumeType

Type: String

Valid values: standard | io1 | io2 | gp2 | gp3 | sc1 | st1

Description: The volume type you want to change the Amazon EBS volume to. For
information about Amazon EBS volume types, see [Amazon EBS volume
types](../../../AWSEC2/latest/UserGuide/ebs-volume-types.md "../../../AWSEC2/latest/UserGuide/ebs-volume-types.md") in the _Amazon EC2 User Guide_ .
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ec2:DescribeVolumes`
- `ec2:ModifyVolume`

**Document Steps**

- `aws:waitForAwsResourceProperty` - Verifies the state of the
  volume is `available` or `in-use` .
- `aws:executeAwsApi` - Modifies the Amazon EBS volume you specify in
  the `EbsVolumeId` parameter.
- `aws:waitForAwsResourceProperty` - Verifies the type of the
  volume has been changed to the value you specified in the
  `EbsVolumeType` parameter.
