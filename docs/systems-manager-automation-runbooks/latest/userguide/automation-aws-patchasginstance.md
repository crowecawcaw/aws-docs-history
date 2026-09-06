

# `AWS-PatchAsgInstance`
<a name="automation-aws-patchasginstance"></a>

**Description**

Patch Amazon Elastic Compute Cloud (Amazon EC2) instances in an Auto Scaling group.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-PatchAsgInstance)

**Important**  
This runbook applies an `AutoPatchInstanceInASG` tag to the target instance during execution. This tag prevents the runbook from executing twice on the same instance simultaneously — it is not a patch compliance indicator. If the patching step fails, the tag value might still be set to `Completed` even though the runbook execution status reports `Failed`.  
To verify patch compliance on the instance, use [DescribeInstancePatchStates](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatchStates.html) or [ListComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListComplianceItems.html) instead.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ InstanceId

  Type: String

  Description: (Required) ID of the instance to patch. Don't specify an instance ID that is configured to run during a maintenance window.
+ LambdaRoleArn

  Type: String

  Description: (Optional) The ARN of the role that allows the Lambda created by Automation to perform the actions on your behalf. If not specified, a transient role will be created to run the Lambda function.
+ WaitForInstance

  Type: String

  Default: PT2M

  Description: (Optional) Duration that the Automation should sleep to allow the instance to come back into service.
+ WaitForReboot

  Type: String

  Default: PT5M

  Description: (Optional) Duration that the Automation should sleep to allow a patched instance to reboot.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ssm:StartAutomationExecution`
+ `ssm:GetAutomationExecution`
+ `ssm:GetCommandInvocation`
+ `ssm:GetParameter`
+ `ssm:SendCommand`
+ `cloudformation:CreateStack`
+ `cloudformation:DeleteStack`
+ `cloudformation:DescribeStacks`
+ `ec2:CreateTags`
+ `ec2:DescribeInstances`
+ `ec2:RunInstances`
+ `iam:AttachRolePolicy`
+ `iam:CreateRole`
+ `iam:DeleteRole`
+ `iam:DeleteRolePolicy`
+ `iam:DetachRolePolicy`
+ `iam:GetRole`
+ `iam:PassRole`
+ `iam:PutRolePolicy`
+ `lambda:CreateFunction`
+ `lambda:DeleteFunction`
+ `lambda:GetFunction`
+ `lambda:InvokeFunction`