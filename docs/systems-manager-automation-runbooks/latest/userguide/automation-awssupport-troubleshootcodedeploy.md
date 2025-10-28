# `AWSSupport-TroubleshootCodeDeploy`

**Description**

The
`AWSSupport-TroubleshootCodeDeploy`
runbook helps diagnose why an
AWS CodeDeploy deployment failed on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The runbook outputs
steps to help you resolve the issue or troubleshoot further. Best practices for
CodeDeploy are also provided to help you avoid similar issues in the future.

This runbook can help you to resolve the following issues:

- The CodeDeploy agent is not installed or not running on the Amazon EC2
  instance
- The Amazon EC2 instance does not have an AWS Identity and Access Management (IAM) instance profile
  attached
- The IAM instance profile attached to the Amazon EC2 instance does not have
  the required Amazon Simple Storage Service (Amazon S3) permissions
- A revision stored in Amazon S3 is missing, or the Amazon S3 bucket used is in an
  AWS Region that is different than the Amazon EC2 instance
- Application specification (AppSpec) file issues
- "File already exists at location" errors
- Failed CodeDeploy managed lifecycle event hooks
- Failed customer managed lifecycle event hooks
- Scale-in events during the deployment

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCodeDeploy "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCodeDeploy")

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

- DeploymentId

Type: String

Description: (Required) The ID of the deployment which failed.

- InstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 instance where the deployment
failed.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `codedeploy:GetDeployment`
- `codedeploy:GetDeploymentTarget`
- `ec2:DescribeInstances`

**Document Steps**

- `aws:executeAwsApi`

* Verifies the values provided for the
  `DeploymentId`
  and
  `InstanceId`
  parameters.

- `aws:executeScript`

* Collects information from the Amazon EC2
  instance such as the state of the instance and IAM instance profile
  details.

- `aws:executeScript`

* Reviews the specified deployment, and
  returns an analysis regarding why the deployment failed.
