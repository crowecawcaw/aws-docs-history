

# Launching a directory administration instance in your AWS Managed Microsoft AD Active Directory
<a name="console_instance"></a>

This procedure launches an Amazon EC2 directory administration Windows instance in the AWS Management Console using AWS Systems Manager Automation to manage your directories. You can also accomplish this by running the automation [AWS-CreateDSManagementInstance](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-create-ds-management-instance.html) in the AWS Systems Manager Automation console directly.

For more information, see the following links:
+ [Simplifying Active Directory domain join with AWS Systems Manager](https://aws.amazon.com/blogs/modernizing-with-aws/simplifying-active-directory-domain-join-with-aws-systems-manager-2/)
+ [How do I use AWS Systems Manager to join a running EC2 Windows instances to my Directory Service domain?](https://repost.aws/knowledge-center/ec2-systems-manager-dx-domain)

## Prerequisites
<a name="console_instance_prereqs"></a>

The following prerequisites are required to complete this tutorial:
+ You will need to set up AWS Systems Manager. For more information, see [Setting up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-console.html).
+ You will need an [IAM instance profile role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) that allows Systems Manager and AWS Managed Microsoft AD.
  + For more information on Systems Manager, see [Configure instance permissions required for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html).
  + The IAM instance role needs the following AWS managed policies so your EC2 directory administration Windows instance can domain join your AWS Managed Microsoft AD:
    + **`AmazonSSMManagedInstanceCore`**
    + **`AmazonSSMDirectoryServiceAccess`**
+ The VPC connected to your AWS Managed Microsoft AD needs to allow access to public Directory Service endpoints. For more information, see [Prerequisites for creating a AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_prereqs).
+ You must have the following permissions enabled in your account to launch a directory administration EC2 instance from the console:
  + `ds:DescribeDirectories`
  + `ec2:AuthorizeSecurityGroupIngress`
  + `ec2:CreateSecurityGroup`
  + `ec2:CreateTags`
  + `ec2:DeleteSecurityGroup`
  + `ec2:DescribeInstances`
  + `ec2:DescribeInstanceStatus`
  + `ec2:DescribeKeyPairs`
  + `ec2:DescribeSecurityGroups`
  + `ec2:DescribeVpcs`
  + `ec2:RunInstances`
  + `ec2:TerminateInstances`
  + `iam:AddRoleToInstanceProfile`
  + `iam:AttachRolePolicy`
  + `iam:CreateInstanceProfile`
  + `iam:CreateRole`
  + `iam:DeleteInstanceProfile`
  + `iam:DeleteRole`
  + `iam:DetachRolePolicy`
  + `iam:GetInstanceProfile`
  + `iam:GetRole`
  + `iam:ListAttachedRolePolicies`
  + `iam:ListInstanceProfiles`
  + `iam:ListInstanceProfilesForRole`
  + `iam:PassRole`
  + `iam:RemoveRoleFromInstanceProfile`
  + `iam:TagInstanceProfile`
  + `iam:TagRole`
  + `ssm:CreateDocument`
  + `ssm:DeleteDocument`
  + `ssm:DescribeInstanceInformation`
  + `ssm:GetAutomationExecution`
  + `ssm:GetParameters`
  + `ssm:ListCommandInvocations`
  + `ssm:ListCommands`
  + `ssm:ListDocuments`
  + `ssm:SendCommand`
  + `ssm:StartAutomationExecution`
  + `ssm:GetDocument`

## Launching a directory administration EC2 instance in the AWS Management Console
<a name="console_instance_launch"></a>

1. Sign in to the [Directory Service console](https://console.aws.amazon.com/directoryservicev2/).

1. Under **Active Directory**, choose **Directories**.

1. Choose the **Directory ID** of the directory where you want to launch a directory administration EC2 instance.

1. On the directory page, in the top right corner, choose **Actions**.

1. In the **Actions** dropdown list, choose **Launch directory administration EC2 instance**.

1. On the **Launch directory administration EC2 instance** page, under **Input parameters**, complete the fields.

   1. (Optional) You can provide a key pair for the instance. From the **Key Pair Name - *optional*** dropdown list, select a key pair.

   1. (Optional) Choose **View AWS CLI command** to see an example that you use in the AWS CLI to run this automation.

1. Choose **Submit**.

1. You're taken back to the directory page. A green flashbar displays at the top of your screen to indicate that you successfully began the launch.

## Viewing directory administration EC2 instance
<a name="view_console_instances"></a>

If you haven't launched any EC2 instances for a directory, a dash (**-**) displays under **Directory administration EC2 instance**.

1. Under **Active Directory**, choose **Directories** and select the directory you want to view. 

1. Under **Directory details**, under **Directory administration EC2 instance**, choose one or all of your instances to view.

1. When you choose an instance, you're routed to the EC2 **Connect to instance** page to connect a remote desktop to your instance.