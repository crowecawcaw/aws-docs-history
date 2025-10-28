# `AWS-UpdateAmazonECSAgent`

**Description**

The `AWS-UpdateAmazonECSAgent` runbook updates the Amazon Elastic Container Service (Amazon ECS)
agent on the Amazon Elastic Compute Cloud (Amazon EC2) instance you specify. This runbook only supports Amazon Linux
and Amazon Linux 2 instances.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateAmazonECSAgent "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateAmazonECSAgent")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ClusterARN

Type: StringList

Description: (Required) The Amazon Resource Name (ARN) of the Amazon ECS
cluster your container instances is registered with.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:GetCommandInvocation`
- `ec2:DescribeImages`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeImage`
- `ec2:DescribeInstance`
- `ec2:DescribeInstanceAttribute`
- `ecs:DescribeContainerInstances`
- `ecs:DescribeClusters`
- `ecs:ListContainerInstances`
- `ecs:UpdateContainerAgent`

**Document Steps**

`aws:executeScript` - Updates the Amazon ECS agent on the Amazon ECS cluster you
specify in the `ClusterARN` parameters.

**Outputs**

UpdateAmazonECSAgent.UpdatedContainers - The ID of the instance where the update
of the Amazon ECS agent succeeded.

UpdateAmazonECSAgent.FailedContainers - The ID of the instance where the update of
the Amazon ECS agent failed.

UpdateAmazonECSAgent.InProgressContainers - The ID of the instance where the
update of the Amazon ECS agent is in progress.
