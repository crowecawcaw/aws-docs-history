# `AWS-SetupJupyter`

**Description**

The `AWS-SetupJupyter` runbook helps you set up Jupyter Notebook on an
Amazon Elastic Compute Cloud (Amazon EC2) instance. You can either specify an existing instance, or provide an
Amazon Machine Image (AMI) ID for the automation to launch and set up a new instance. Before you
begin, you must create a `SecureString` parameter in Parameter Store to use as the
password for Jupyter Notebook. Parameter Store is a tool in AWS Systems Manager. For information about
creating parameters, see [Creating
parameters](../../../systems-manager/latest/userguide/sysman-paramstore-su-create.md "../../../systems-manager/latest/userguide/sysman-paramstore-su-create.md") in the _AWS Systems Manager User Guide_.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-SetupJupyter "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-SetupJupyter")

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

- AmiId

Type: String

Description: (Optional) The ID of the AMI that you want to use to launch a new
instance and set up Jupyter Notebook.

- InstanceId

Type: String

Description: (Required) The ID of the instance that you want to set up Jupyter
Notebook on.

- InstanceType

Type: String

Default: t3.medium

Description: (Optional) If you're launching a new instance to set up Jupyter
Notebook, specify the instance type that you want to use.

- JupyterPasswordSSMKey

Type: String

Description: (Required) The name of the `SecureString` parameter in
Parameter Store that you want to use as the password for Jupyter Notebook.

- KeyPairName

Type: String

Description: (Optional) The key pair that you want to associate with the newly
launched instance.

- RemoteAccessCidr

Type: String

Default: 0.0.0.0/0

Description: (Optional) The CIDR range that you want to allow SSH traffic
from.

- RoleName

Type: String

Default: SSMManagedInstanceProfileRole

Description: (Optional) The name of the instance profile for the newly launched
instance.

- StackName

Type: String

Default: CreateManagedInstanceStack{{automation:EXECUTION\_ID}}

Description: (Optional) The AWS CloudFormation stack name that you want the automation to
use.

- SubnetId

Type: String

Default: Default

Description: (Optional) The subnet that you want to launch the new instance to
use.

- VpcId

Type: String

Default: Default

Description: (Optional) The ID of the virtual private cloud (VPC) that you want to
launch the new instance in to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:GetAutomationExecution`
- `ssm:GetCommandInvocation`
- `ssm:GetParameter`
- `ssm:SendCommand`
- `ssm:StartAutomationExecution`
- `cloudformation:CreateStack`
- `cloudformation:DeleteStack`
- `cloudformation:DescribeStacks`
- `ec2:DescribeInstances`
- `ec2:DescribeKeyPairs`
- `ec2:RunInstances`
- `iam:AttachRolePolicy`
- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:DeleteRolePolicy`
- `iam:DetachRolePolicy`
- `iam:GetRole`
- `iam:PassRole`
- `iam:PutRolePolicy`
- `lambda:CreateFunction`
- `lambda:DeleteFunction`
- `lambda:GetFunction`
- `lambda:InvokeFunction`

**Document Steps**

- `aws:executeScript` - Sets up Jupyter Notebook on the instance you
  specify, or on a newly launched instance, using the values that you specify for the
  runbook input parameters.
