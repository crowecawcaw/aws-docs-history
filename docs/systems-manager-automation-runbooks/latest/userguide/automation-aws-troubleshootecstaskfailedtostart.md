# `AWSSupport-TroubleshootECSTaskFailedToStart`

**Description**

The `AWSSupport-TroubleshootECSTaskFailedToStart` runbook helps you
troubleshoot why an Amazon Elastic Container Service (Amazon ECS) task in an Amazon ECS cluster failed to start. You
must run this runbook in the same AWS Region as your task that failed to start.
The runbook analyzes the following common issues that can prevent a task from
starting:

- Network connectivity to the configured container registry
- Missing IAM permissions required by the task execution role
- VPC endpoint connectivity
- Security group rule configuration
- AWS Secrets Manager secrets references
- Logging configuration

###### Note

If the analysis determines that network connectivity needs to be tested, a
Lambda function and requisite IAM role are created in your account. These
resources are used to simulate the network connectivity of your failed task. The
automation deletes these resources when they're no longer required. However, if
the automation fails to delete the resources, you must do so manually.

When a Lambda IAM role is provided, the automation will use it instead of creating a new one.
The provided Lambda IAM role must include the AWS managed policy `AWSLambdaVPCAccessExecutionRole` and
have a trust policy that allows it to be assumed by the Lambda service principal `lambda.amazonaws.com`.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootECSTaskFailedToStart "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootECSTaskFailedToStart")

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

- LambdaRoleArn

Type: String

Description: (Optional) The ARN of the IAM role that allows the AWS Lambda
function to access the required AWS services and resources. If no role is specified,
this Systems Manager Automation will create one IAM role for Lambda in your account with the
name `NetworkToolSSMRunbookExecution<ExecutionId>` that includes the
managed policy: `AWSLambdaVPCAccessExecutionRole`.

- ClusterName

Type: String

Description: (Required) The name of the Amazon ECS cluster where the task
failed to start.

- CloudwatchRetentionPeriod

Type: Integer

Description: (Optional) The retention period, in days, for the Lambda
function logs to be stored in Amazon CloudWatch Logs. This is only necessary if the
analysis determines network connectivity needs to be tested.

Valid values: 1 | 3 | 5 | 7 | 14 | 30 | 60 | 90

Default: 30

- TaskId

Type: String

Description: (Required) The ID of the failed task. Use the most recently
failed task.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudtrail:LookupEvents`
- `ec2:DeleteNetworkInterface`
- `ec2:DescribeDhcpOptions`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeIamInstanceProfileAssociations`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkAcls`
- `ec2:DescribeNetworkInterfaces`
- `ec2:DescribeRouteTables`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcEndpoints`
- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `elasticfilesystem:DescribeFileSystems`
- `elasticfilesystem:DescribeMountTargets`
- `elasticfilesystem:DescribeMountTargetSecurityGroups`
- `elasticfilesystem:DescribeFileSystemPolicy`
- `ecr:DescribeImages`
- `ecr:GetRepositoryPolicy`
- `ecs:DescribeContainerInstances`
- `ecs:DescribeServices`
- `ecs:DescribeTaskDefinition`
- `ecs:DescribeTasks`
- `iam:AttachRolePolicy`
- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:DetachRolePolicy`
- `iam:GetInstanceProfile`
- `iam:GetRole`
- `iam:ListRoles`
- `iam:ListUsers`
- `iam:PassRole`
- `iam:SimulateCustomPolicy`
- `iam:SimulatePrincipalPolicy`
- `kms:DescribeKey`
- `lambda:CreateFunction`
- `lambda:DeleteFunction`
- `lambda:GetFunctionConfiguration`
- `lambda:InvokeFunction`
- `lambda:TagResource`
- `logs:DescribeLogGroups`
- `logs:PutRetentionPolicy`
- `secretsmanager:DescribeSecret`
- `ssm:DescribeParameters`
- `sts:GetCallerIdentity`
  When `LambdaRoleArn` is provided, the automation does not need to create the
  role and the following permissions can be excluded:

- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:AttachRolePolicy`
- `iam:DetachRolePolicy`

**Document Steps**

- `aws:executeScript` - Verifies that the user or role who started
  the automation has the required IAM permissions. If you don't have
  sufficient permissions to use this runbook, the missing required permissions
  are included in the output of the automation.
- `aws:branch` - Branches based on whether you have permissions
  to all required actions for the runbook.
- `aws:executeScript` - Creates a Lambda function in your VPC if
  the analysis determines network connectivity needs to be tested.
- `aws:branch` - Branches based on the results of the previous
  step.
- `aws:executeScript` - Analyzes possible causes for the failure
  to start your task.
- `aws:executeScript` - Deletes resources created by this
  automation.
- `aws:executeScript` - Formats the output of the automation to
  return the results of the analysis to the console. You can review the
  analysis after this step before the automation completes.
- `aws:branch` - Branches based on whether the Lambda function and
  associated resources were created and need to be deleted.
- `aws:sleep` - Sleeps for 30 minutes so the elastic network
  interface for the Lambda function can be deleted.
- `aws:executeScript` - Deletes the Lambda function network
  interface.
- `aws:executeScript` - Formats the output of the Lambda function
  network interface deletion step.
