# `AWS-CreateWorkSpace`

**Description**

The `AWS-CreateWorkSpace` runbook creates a new Amazon WorkSpaces virtual
desktop, known as a WorkSpace, based on the values that you specify for the input
parameters. For information about WorkSpaces, see [What is Amazon WorkSpaces?](../../../workspaces/latest/adminguide/amazon-workspaces.md "../../../workspaces/latest/adminguide/amazon-workspaces.md") in the
_Amazon WorkSpaces Administration Guide_.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateWorkspace "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateWorkspace")

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

- BundleId

Type: String

Description: (Required) The ID of the bundle to use for the
WorkSpace.

- ComputeTypeName

Type: String

Valid values: VALUE | STANDARD | PERFORMANCE | POWER | GRAPHICS | POWERPRO
| GRAPHICSPRO Description: (Optional) The compute type for your WorkSpace. <br>• DirectoryId Type: String Description: (Required) The ID of the directory to add your WorkSpace to. <br>• RootVolumeEncryptionEnabled Type: Boolean Valid values: true | false Default: false Description: (Optional) Determines whether the root volume of the WorkSpace is encrypted. <br>• RootVolumeSizeGib Type: Integer Description: (Required) The size of the root volume for the WorkSpace. <br>• RunningMode Type: String Valid values: ALWAYS_ON | AUTO_STOP Description: (Required) The running mode of the WorkSpace. <br>• RunningModeAutoStopTimeoutInMinutes Type: Integer Description: (Optional) The time after a user logs off when the WorkSpaces stops. Specify a value in 60-minute intervals. <br>• Tags Type: String Description: (Optional) Tags that you want to apply to the WorkSpace. <br>• UserName Type: String Description: (Required) The user name to associate with the WorkSpace. <br>• UserVolumeEncryptionEnabled Type: Boolean Valid values: true | false Default: false Description: (Optional) Determines whether the user volume of the WorkSpace is encrypted. <br>• UserVolumeSizeGib Type: Integer Description: (Required) The size of the user volume for the WorkSpace. <br>• VolumeEncryptionKey Type: String Description: (Optional) The symmetric AWS Key Management Service key that you want to use to encrypt data stored on your WorkSpace. **Required IAM permissions** The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully. <br>• `workspaces:CreateWorkspaces` <br>• `workspaces:DescribeWorkspaces` **Document Steps** <br>• `aws:executeScript` - Creates a WorkSpace based on the values that you specify for the input parameters. <br>• `aws:waitForAwsResourceProperty` - Verifies the state of the WorkSpace is `AVAILABLE`. **Outputs** `CreateWorkspace.WorkspaceId`
