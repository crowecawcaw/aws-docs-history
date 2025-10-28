# `AWS-CreateDSManagementInstance`

**Description**

The `AWS-CreateDSManagementInstance` runbook creates an Amazon Elastic Compute Cloud
(Amazon EC2) Windows instance that you can use to manage your AWS Directory Service directory. The
management instance can't be used to manage AD Connector directories.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateDSManagementInstance "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateDSManagementInstance")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- AmiID

Type: String

Default: `{{
 ssm:/aws/service/ami-windows-latest/Windows_Server-2019-English-Full-Base
 }}`

Description: (Required) The ID of the Amazon Machine Image (AMI) you want to use to
launch the management instance.

- DirectoryId

Type: String

Description: (Required) The ID of the AWS Directory Service directory you want to manage.
The instance is joined to the directory you specify.

- IamInstanceProfileName

Type: String

Description: (Required) The name you specify is applied to the IAM
instance profile that is created by the automation and attached to the
management instance.

- InstanceType

Type: String

Default: t3.medium

Allowed values:

    + t2.nano
    + t2.micro
    + t2.small
    + t2.medium
    + t2.large
    + t2.xlarge
    + t2.2xlarge
    + t3.nano
    + t3.micro
    + t3.small
    + t3.medium
    + t3.large
    + t3.xlarge
    + t3.2xlarge

Description: (Required) The type of instance you want to launch.

- KeyPairName

Type: String

Description: (Optional) The key pair to use when creating the instance. If
you do not specify a value, no key pair is associated with the
instance.

- RemoteAccessCidr

Type: String

Description: (Required) The CIDR block you want to allow RDP traffic (port 3389) from. The CIDR block you specify is applied to an inbound rule that's
added to the security group created by the automation.

- SecurityGroupName

Type: String

Description: (Required) The name you specify is applied to the security
group that is created by the automation and associated with the management
instance.

- Tags

Type: MapList

Description: (Optional) A key-value pair you want to apply to the
resources created by the automation.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ds:DescribeDirectories`
- `ec2:AuthorizeSecurityGroupIngress`
- `ec2:CreateSecurityGroup`
- `ec2:CreateTags`
- `ec2:DeleteSecurityGroup`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DescribeKeyPairs`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeVpcs`
- `ec2:RunInstances`
- `ec2:TerminateInstances`
- `iam:AddRoleToInstanceProfile`
- `iam:AttachRolePolicy`
- `iam:CreateInstanceProfile`
- `iam:CreateRole`
- `iam:DeleteInstanceProfile`
- `iam:DeleteRole`
- `iam:DetachRolePolicy`
- `iam:GetInstanceProfile`
- `iam:GetRole`
- `iam:ListAttachedRolePolicies`
- `iam:ListInstanceProfiles`
- `iam:ListInstanceProfilesForRole`
- `iam:PassRole`
- `iam:RemoveRoleFromInstanceProfile`
- `iam:TagInstanceProfile`
- `iam:TagRole`
- `ssm:CreateDocument`
- `ssm:DeleteDocument`
- `ssm:DescribeInstanceInformation`
- `ssm:GetAutomationExecution`
- `ssm:GetParameters`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:ListDocuments`
- `ssm:SendCommand`
- `ssm:StartAutomationExecution`

**Document Steps**

- `aws:executeAwsApi` - Gathers details about the directory you
  specify in the `DirectoryId` parameter.
- `aws:executeAwsApi` - Gets the CIDR block of the virtual private
  cloud (VPC) where the directory was launched.
- `aws:executeAwsApi` - Creates a security group using the value
  you specify in the `SecurityGroupName` parameter.
- `aws:executeAwsApi` - Creates an inbound rule for the newly
  created security group that allows RDP traffic from the CIDR you specify in
  the `RemoteAccessCidr` parameter.
- `aws:executeAwsApi` - Creates an IAM role and instance profile
  using the value you specify in the `IamInstanceProfileName`
  parameter.
- `aws:executeAwsApi` - Launches an Amazon EC2 instance based on the
  values you specify in the runbook parameters.
- `aws:executeAwsApi` - Creates an AWS Systems Manager document to join the
  newly launched instance to your directory.
- `aws:runCommand` - Joins the new instance to your directory.
- `aws:runCommand` - Installs remote server administration tools on
  the new instance.
