# Replatforming script prerequisites

This section covers the steps necessary to run the Windows to Linux replatforming
script.

###### Contents

- [Prerequisites to run the replatforming script](#replatform-sql-server-prerequisites "#replatform-sql-server-prerequisites")
- [Prerequisites for replatforming to an
  existing EC2 instance](#existing-linux-prerequisites "#existing-linux-prerequisites")

## Prerequisites to run the replatforming script

In order to run the Windows to Linux replatforming assistant for Microsoft SQL
Server Databases script, you must do the following:

1. ###### Install the AWS PowerShell module

To install the AWS PowerShell module, follow the steps listed in [Installing the AWS Tools for PowerShell on Windows](../../../powershell/latest/userguide/pstools-getting-set-up-windows.md "../../../powershell/latest/userguide/pstools-getting-set-up-windows.md"). We
recommend that you use PowerShell 3.0 or later for the backup script to work
properly. 2. ###### Install the Windows to Linux replatforming assistant PowerShell backup
script

To run the Windows to Linux replatforming assistant,
download the PowerShell backup script: [MigrateSQLServerToEC2Linux.ps1](https://awsec2-server-upgrade-prod.s3.us-west-1.amazonaws.com/MigrateSQLServerToEC2Linux.ps1 "https://awsec2-server-upgrade-prod.s3.us-west-1.amazonaws.com/MigrateSQLServerToEC2Linux.ps1"). 3. ###### Add an AWS user profile to the AWS SDK store

To add and configure the AWS user profile, see the steps listed in
[Managing Profiles](../../../powershell/latest/userguide/specifying-your-aws-credentials.md#managing-profiles "../../../powershell/latest/userguide/specifying-your-aws-credentials.md#managing-profiles") in the _AWS Tools for PowerShell
User Guide_. [Set the following IAM policy](../../../powershell/latest/userguide/pstools-iam-policy.md "../../../powershell/latest/userguide/pstools-iam-policy.md") for your user profile.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::123456789012:role/DevTeam*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "ec2:RebootInstances",
 "ssm:SendCommand",
 "ssm:GetAutomationExecution",
 "ec2:DescribeInstances",
 "ssm:ListCommands",
 "ec2:CreateTags",
 "s3:CreateBucket",
 "ec2:RunInstances",
 "s3:ListBucket",
 "ssm:GetCommandInvocation",
 "s3:PutEncryptionConfiguration",
 "ec2:DescribeImages",
 "s3:PutObject",
 "s3:GetObject",
 "ssm:StartAutomationExecution",
 "ssm:DescribeInstanceInformation",
 "s3:DeleteObject",
 "ssm:ListCommandInvocations",
 "s3:DeleteBucket",
 "ec2:DescribeInstanceStatus"
 ],
 "Resource": "*"
 }
 ]
}`

```

4. ###### Create an IAM instance profile role

To create an IAM instance profile role in order to run Systems Manager on EC2 Linux,
see the steps listed under [Create an IAM instance
profile for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md") in the
_AWS Systems Manager User Guide_.

## Prerequisites for replatforming to an

existing EC2 instance

To replatform to an existing instance running Microsoft SQL Server 2017 on Linux,
you must:

1. Configure the EC2 instance with an AWS Identity and Access Management (IAM) instance profile and
   attach the `AmazonSSMManagedInstanceCore` managed policy.

For information about creating an IAM instance profile for Systems Manager and
attaching it to an instance, see the following topics in the
_AWS Systems Manager User Guide_:

    * [Create an
     IAM instance profile for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md")
    * [Attach an IAM instance profile to an Amazon EC2
     instance](../../../systems-manager/latest/userguide/setup-launch-managed-instance.md "../../../systems-manager/latest/userguide/setup-launch-managed-instance.md")

2. Verify that SSM Agent is installed on your EC2 instance. For more
   information, see [Working with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/sysman-install-ssm-win.md "../../../systems-manager/latest/userguide/sysman-install-ssm-win.md") in
   the _AWS Systems Manager User Guide_.
3. Verify that the EC2 instance has enough free disk space to download and
   restore the Microsoft SQL Server backups.
