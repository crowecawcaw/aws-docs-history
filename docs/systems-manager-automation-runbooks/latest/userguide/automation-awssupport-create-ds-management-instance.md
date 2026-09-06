

# `AWS-CreateDSManagementInstance`
<a name="automation-awssupport-create-ds-management-instance"></a>

 **Description** 

 The `AWS-CreateDSManagementInstance` runbook creates an Amazon Elastic Compute Cloud (Amazon EC2) Windows instance that you can use to manage your AWS Directory Service directory. The management instance can't be used to manage AD Connector directories. 

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-CreateDSManagementInstance) 

**Note**  
By default, this runbook reuses an existing domain join document in your account if one is already present for the directory. To have the runbook always use the AWS owned public document `AWS-JoinDirectoryServiceDomain-V2` instead, set the `UseAWSManagedDomainJoinDocument` parameter to `true`. We recommend using `true`, and following the principle of least privilege when granting AWS Systems Manager document permissions such as `ssm:CreateDocument`. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the AWS Identity and Access Management User Guide.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
+ AmiID

  Type: String

   Default: `{{ ssm:/aws/service/ami-windows-latest/Windows_Server-2019-English-Full-Base }}` 

  Description: (Optional) Amazon Machine Image (AMI) id to use for launching the instance. By Default the instance will launch with the latest Microsoft Windows Server 2019 Base AMI.
+ DirectoryId

  Type: String

  Description: (Required) The Directory Id of your Directory Service directory.
+ IamInstanceProfileName

  Type: String

  Description: (Optional) IAM instance profile name. By Default, if no instance profile exists with the name AmazonSSMDirectoryServiceInstanceProfileRole, an instance profile with the name AmazonSSMDirectoryServiceInstanceProfileRole will be created.

  Default: AmazonSSMDirectoryServiceInstanceProfileRole
+ InstanceType

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

  Description: (Optional) Type of instance to launch. Default is t3.medium.
+ KeyPairName

  Type: String

  Description: (Optional) Key pair to use when launching instance. Windows does not support ED25519 key pairs. By Default the instance is launched without a key pair (NoKeyPair).

  Default: NoKeyPair
+ RemoteAccessCidr

  Type: String

  Description: (Optional) Creates Security group with port for RDP (Port range 3389) open to IPs specified by CIDR (default is 0.0.0.0/0). If the security group already exists it will not be modified and rules will not be changed.

  Default: 0.0.0.0/0
+ SecurityGroupName

  Type: String

  Description: (Optional) Security group name. By Default, if no security group exists with the name AmazonSSMDirectoryServiceSecurityGroup, a security group with the name AmazonSSMDirectoryServiceSecurityGroup will be created.

  Default: AmazonSSMDirectoryServiceSecurityGroup
+ Tags

  Type: MapList

  Description: (Optional) A key-value pair you want to apply to the resources created by the automation.

  Default: ` [ {"Key":"Description","Value":"Created by AWS Systems Manager Automation"}, {"Key":"Created By","Value":"AWS Systems Manager Automation"} ]`
+ UseAWSManagedDomainJoinDocument

  Type: String

  Valid values: `false` \| `true`

  Default: `false`

  Description: (Optional) Determines which document the runbook uses to join the new instance to your directory. When set to `true`, the runbook uses the AWS owned public document `AWS-JoinDirectoryServiceDomain-V2`. When set to `false` (the default), the runbook reuses the directory's existing domain join document if one is present, and otherwise creates one, runs it, and then deletes it. We recommend setting this parameter to `true`.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ds:DescribeDirectories` 
+  `ec2:AuthorizeSecurityGroupIngress` 
+  `ec2:CreateSecurityGroup` 
+  `ec2:CreateTags` 
+  `ec2:DeleteSecurityGroup` 
+  `ec2:DescribeInstances` 
+  `ec2:DescribeInstanceStatus` 
+  `ec2:DescribeKeyPairs` 
+  `ec2:DescribeSecurityGroups` 
+  `ec2:DescribeVpcs` 
+  `ec2:RunInstances` 
+  `ec2:TerminateInstances` 
+  `iam:AddRoleToInstanceProfile` 
+  `iam:AttachRolePolicy` 
+  `iam:CreateInstanceProfile` 
+  `iam:CreateRole` 
+  `iam:DeleteInstanceProfile` 
+  `iam:DeleteRole` 
+  `iam:DetachRolePolicy` 
+  `iam:GetInstanceProfile` 
+  `iam:GetRole` 
+  `iam:ListAttachedRolePolicies` 
+  `iam:ListInstanceProfiles` 
+  `iam:ListInstanceProfilesForRole` 
+  `iam:PassRole` 
+  `iam:RemoveRoleFromInstanceProfile` 
+  `iam:TagInstanceProfile` 
+  `iam:TagRole` 
+  `ssm:CreateDocument` 
+  `ssm:DeleteDocument` 
+  `ssm:DescribeInstanceInformation` 
+  `ssm:GetAutomationExecution` 
+  `ssm:GetParameters` 
+  `ssm:ListCommandInvocations` 
+  `ssm:ListCommands` 
+  `ssm:ListDocuments` 
+  `ssm:SendCommand` 
+  `ssm:StartAutomationExecution` 

 **Document Steps** 
+  `aws:executeAwsApi` - Gathers details about the directory you specify in the `DirectoryId` parameter. 
+  `aws:executeAwsApi` - Gets the CIDR block of the virtual private cloud (VPC) where the directory was launched. 
+  `aws:executeAwsApi` - Creates a security group using the value you specify in the `SecurityGroupName` parameter. 
+  `aws:executeAwsApi` - Creates an inbound rule for the newly created security group that allows RDP traffic from the CIDR you specify in the `RemoteAccessCidr` parameter. 
+  `aws:executeAwsApi` - Creates an IAM role and instance profile using the value you specify in the `IamInstanceProfileName` parameter. 
+  `aws:executeAwsApi` - Launches an Amazon EC2 instance based on the values you specify in the runbook parameters. 
+  `aws:branch` - Determines which document to use for the domain join, based on the value of the `UseAWSManagedDomainJoinDocument` parameter. 
+  `aws:runCommand` - Joins the new instance to your directory. 
+  `aws:runCommand` - Installs remote server administration tools on the new instance. 