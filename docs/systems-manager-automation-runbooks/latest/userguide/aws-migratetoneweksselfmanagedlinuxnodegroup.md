# `AWS-MigrateToNewEKSSelfManagedNodeGroup`

**Description**

The `AWS-MigrateToNewEKSSelfManagedNodeGroup` runbook helps you create
a new Amazon Elastic Kubernetes Service (Amazon EKS) Linux node group to migrate your existing application to.
For more information, see [Migrating to
a new node group](../../../eks/latest/userguide/migrate-stack.md "../../../eks/latest/userguide/migrate-stack.md") in the **Amazon EKS User Guide**.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-MigrateToNewEKSSelfManagedLinuxNodeGroup "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-MigrateToNewEKSSelfManagedLinuxNodeGroup")

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

- OldStackName

Type: String

Description: (Required) The name or stack ID of your existing AWS CloudFormation
stack.

- NewStackName

Type: String

Description: (Optional) The name of the new AWS CloudFormation stack that is created
for your new node group. If you don't specify a value for this parameter,
the stack name is created using the format:
`NewNodeGroup-`ClusterName`-`AutomationExecutionID``.

- ClusterControlPlaneSecurityGroup

Type: String

Description: (Optional) The ID of the security group you want nodes to use
to communicate with the Amazon EKS control plane. If you don't specify a value
for this parameter, the security group specified in your existing AWS CloudFormation
stack is used.

- NodeInstanceType

Type: String

Description: (Optional) The instance type that you want to use for the new
node group. If you don't specify a value for this parameter, the instance
type specified in your existing AWS CloudFormation stack is used.

- NodeGroupName

Type: String

Description: (Optional) The name of your new node group. If you don't
specify a value for this parameter, the node group name specified in your
existing AWS CloudFormation stack is used.

- NodeAutoScalingGroupDesiredCapacity

Type: String

Description: (Optional) The desired number of nodes to scale to when your
new stack is created. This number must be greater than or equal to the
`NodeAutoScalingGroupMinSize` value and less than or equal to
the `NodeAutoScalingGroupMaxSize`. If you don't specify a value
for this parameter, the node group desired capacity specified in your
existing AWS CloudFormation stack is used.

- NodeAutoScalingGroupMaxSize

Type: String

Description: (Optional) The maximum number of nodes that your node group
can scale out to. If you don't specify a value for this parameter, the node
group maximum size specified in your existing AWS CloudFormation stack is used.

- NodeAutoScalingGroupMinSize

Type: String

Description: (Optional) The minimum number of nodes that your node group
can scale in to. If you don't specify a value for this parameter, the node
group minimum size specified in your existing AWS CloudFormation stack is used.

- NodeImageId

Type: String

Description: (Optional) The ID of the Amazon Machine Image (AMI) that you want the
node group to use.

- NodeImageIdSSMParam

Type: String

Description: (Optional) The public Systems Manager parameter for the AMI that you
want the node group to use.

- NodeVolumeSize

Type: String

Description: (Optional) The size of the root volume for your nodes in GiB.
If you don't specify a value for this parameter, the node volume size
specified in your existing AWS CloudFormation stack is used.

- NodeVolumeType

Type: String

Description: (Optional) The type of Amazon EBS volume you want to use for the
root volume of your nodes. If you don't specify a value for this parameter,
the volume type specified in your existing AWS CloudFormation stack is used.

- KeyName

Type: String

Description: (Optional) The key pair you want to assign to your nodes. If
you don't specify a value for this parameter, the key pair specified in your
existing AWS CloudFormation stack is used.

- Subnets

Type: StringList

Description: (Optional) A comma-separated list of the subnet IDs that you
want to use for your new node group. If you don't specify a value for this
parameter, the subnets specified in your existing AWS CloudFormation stack is
used.

- DisableIMDSv1

Type: Boolean

Description: (Optional) Specify `true` to disable Instance
Metadata Service Version 1 (IMDSv1). By default, nodes support IMDSv1 and
IMDSv2.

- BootstrapArguments

Type: String

Description: (Optional) Additional arguments you want to pass to the node
bootstrap script.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:GetParameters`
- `autoscaling:CreateAutoScalingGroup`
- `autoscaling:CreateOrUpdateTags`
- `autoscaling:DeleteTags`
- `autoscaling:DescribeAutoScalingGroups`
- `autoscaling:DescribeScalingActivities`
- `autoscaling:DescribeScheduledActions`
- `autoscaling:SetDesiredCapacity`
- `autoscaling:TerminateInstanceInAutoScalingGroup`
- `autoscaling:UpdateAutoScalingGroup`
- `cloudformation:CreateStack`
- `cloudformation:DescribeStackResource`
- `cloudformation:DescribeStacks`
- `cloudformation:UpdateStack`
- `ec2:AuthorizeSecurityGroupEgress`
- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:CreateLaunchTemplateVersion`
- `ec2:CreateLaunchTemplate`
- `ec2:CreateSecurityGroup`
- `ec2:CreateTags`
- `ec2:DeleteLaunchTemplate`
- `ec2:DeleteSecurityGroup`
- `ec2:DescribeAvailabilityZones`
- `ec2:DescribeImages`
- `ec2:DescribeInstanceAttribute`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeInstances`
- `ec2:DescribeKeyPairs`
- `ec2:DescribeLaunchTemplateVersions`
- `ec2:DescribeLaunchTemplates`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeSubnets`
- `ec2:DescribeVpcs`
- `ec2:RevokeSecurityGroupEgress`
- `ec2:RevokeSecurityGroupIngress`
- `ec2:RunInstances`
- `ec2:TerminateInstances`
- `iam:AddRoleToInstanceProfile`
- `iam:AttachRolePolicy`
- `iam:CreateInstanceProfile`
- `iam:CreateRole`
- `iam:GetInstanceProfile`
- `iam:GetRole`
- `iam:PassRole`

**Document Steps**

- DetermineParameterValuesForNewNodeGroup (aws:executeScript) - Gathers the
  parameter values to use for the new node group.
- CreateStack (aws:createStack) - Creates the AWS CloudFormation stack for the new node
  group.
- GetNewStackNodeInstanceRole (aws:executeAwsApi) - Gets the node instance
  role.
- GetNewStackSecurityGroup (aws:executeAwsApi) - The step gets the node
  security group.
- AddIngressRulesToNewNodeSecurityGroup (aws:executeAwsApi) - Adds ingress
  rules to the newly created security group so it can accept traffic from the
  one assigned to your previous node group.
- AddIngressRulesToOldNodeSecurityGroup (aws:executeAwsApi) - Adds ingress
  rules to the previous security group so it can accept traffic from the one
  assigned to your newly created node group.
- VerifyStackComplete (aws:assertAwsResourceProperty) - Verifies the new
  stack status is `CREATE_COMPLETE`.

**Outputs**

DetermineParameterValuesForNewNodeGroup.NewStackParameters - The parameters used
to create the new stack.

GetNewStackNodeInstanceRole.NewNodeInstanceRole - The node instance role for the
new node group.

GetNewStackSecurityGroup.NewNodeSecurityGroup - The ID of the security group for
the new node group.

DetermineParameterValuesForNewNodeGroup.NewStackName - The AWS CloudFormation stack name for
the new node group.

CreateStack.StackId - The AWS CloudFormation stack ID for the new node group.
