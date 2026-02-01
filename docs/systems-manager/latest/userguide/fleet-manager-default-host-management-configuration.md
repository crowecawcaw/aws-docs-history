• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Managing EC2

instances automatically with Default Host Management Configuration

The Default Host Management Configuration setting allows AWS Systems Manager to manage your
Amazon EC2 instances automatically as _managed instances_. A
managed instance is an EC2 instance that is configured for use with Systems Manager.

The benefits of managing your instances with Systems Manager include the following:

- Connect to your EC2 instances securely using Session Manager.
- Perform automated patch scans using Patch Manager.
- View detailed information about your instances using Systems Manager Inventory.
- Track and manage instances using Fleet Manager.
- Keep SSM Agent up to date automatically.
  _Fleet Manager, Inventory, Patch Manager, and Session Manager are tools in
  Systems Manager._

Using Default Host Management Configuration, you can manage EC2 instances without
having to manually create an AWS Identity and Access Management (IAM) instance profile. Instead, Default Host
Management Configuration creates and applies a default IAM role to ensure that Systems Manager
has permissions to manage all instances in the AWS account and AWS Region where it's
activated.

If the permissions provided aren't sufficient for your use case, you can also add
policies to the default IAM role created by the Default Host Management Configuration.
Alternatively, if you don't need permissions for all of the capabilities provided by the
default IAM role, you can create your own custom role and policies. Any changes made
to the IAM role you choose for Default Host Management Configuration applies to all
managed Amazon EC2 instances in the Region and account.

For more information about the policy used by Default Host Management Configuration,
see [AWS
managed policy: AmazonSSMManagedEC2InstanceDefaultPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSSMManagedEC2InstanceDefaultPolicy").

###### Implement least privilege access

The procedures in this topic are intended to be performed only by administrators.
Therefore, we recommend implementing _least privilege
access_ in order to prevent non-administrative users from configuring
or modifying the Default Host Management Configuration. To view example policies
that restrict access to the Default Host Management Configuration, see [Least privilege policy examples for
Default Host Management Configuration](#least-privilege-examples "#least-privilege-examples")
later in this topic.

###### Important

Registration information for instances registered using Default Host Management
Configuration is stored locally in the `var/lib/amazon/ssm` or
`C:\ProgramData\Amazon` directories. Removing these
directories or their files will prevent the instance from acquiring the necessary
credentials to connect to Systems Manager using Default Host Management Configuration. In
these cases, you must use an IAM instance profile to provide the required
permissions to your instance, or recreate the instance.

###### Topics

- [Prerequisites](#dhmc-prerequisites "#dhmc-prerequisites")
- [Activating the Default Host Management Configuration
  setting](#dhmc-activate "#dhmc-activate")
- [Deactivating the Default Host Management
  Configuration setting](#dhmc-deactivate "#dhmc-deactivate")
- [Least privilege policy examples for
  Default Host Management Configuration](#least-privilege-examples "#least-privilege-examples")

## Prerequisites

In order to use Default Host Management Configuration in the AWS Region and
AWS account where you activate the setting, the following requirements must be
met.

- An instance to be managed must use Instance Metadata Service Version 2
  (IMDSv2).

Default Host Management Configuration doesn't support Instance Metadata
Service Version 1. For information about transitioning to IMDSv2, see [Transition to using Instance Metadata Service Version 2](../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md "../../../AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.md") in the
_Amazon EC2 User Guide_

- SSM Agent version 3.2.582.0 or later must be installed on the instance to
  be managed.

For information about checking the version of SSM Agent installed on your
instance, see [Checking the SSM Agent version number](ssm-agent-get-version.md "ssm-agent-get-version.md").

For information about updating SSM Agent, see [Automatically updating
SSM Agent](ssm-agent-automatic-updates.md#ssm-agent-automatic-updates-console "ssm-agent-automatic-updates.md#ssm-agent-automatic-updates-console").

- You, as the administrator performing the tasks in this topic, must have
  permissions for the [GetServiceSetting](../APIReference/API_GetServiceSetting.md "../APIReference/API_GetServiceSetting.md"), [ResetServiceSetting](../APIReference/API_ResetServiceSetting.md "../APIReference/API_ResetServiceSetting.md"), and [UpdateServiceSetting](../APIReference/API_UpdateServiceSetting.md "../APIReference/API_UpdateServiceSetting.md") API operations. Additionally, you must
  have permissions for the `iam:PassRole` permission for the
  `AWSSystemsManagerDefaultEC2InstanceManagementRole` IAM
  role. The following is an example policy providing these permissions.
  Replace each `example resource placeholder` with
  your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting",
 "ssm:ResetServiceSetting",
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "ssm.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

- If an IAM instance profile is already attached to an EC2 instance that
  is to be managed using Systems Manager, you must remove any permissions from it that
  allow the `ssm:UpdateInstanceInformation` operation. SSM Agent
  attempts to use instance profile permissions before using the Default Host
  Management Configuration permissions. If you allow the
  `ssm:UpdateInstanceInformation` operation in your own IAM
  instance profile, the instance will not use the Default Host Management
  Configuration permissions.

## Activating the Default Host Management Configuration

setting

You can activate Default Host Management Configuration from the Fleet Manager console,
or by using the AWS Command Line Interface or AWS Tools for Windows PowerShell.

You must turn on the Default Host Management Configuration one by one in each
Region you where you want your Amazon EC2 instances managed by this setting.

After turning on Default Host Management Configuration, it might take up to 30
minutes for your instances to use the credentials of the role you choose in step 5
in the following procedure.

###### To activate Default Host Management Configuration (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Account management, Configure Default Host Management
   Configuration**.
4. Turn on **Enable Default Host Management
   Configuration**.
5. Choose the AWS Identity and Access Management (IAM) role used to enable Systems Manager tools for your
   instances. We recommend using the default role provided by Default Host
   Management Configuration. It contains the minimum set of permissions
   necessary to manage your Amazon EC2 instances using Systems Manager. If you prefer to use a
   custom role, the role's trust policy must allow Systems Manager as a trusted entity.
6. Choose **Configure** to complete setup.

###### To activate Default Host Management Configuration (command line)

1. Create a JSON file on your local machine containing the following trust
   relationship policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"",
 "Effect":"Allow",
 "Principal":{
 "Service":"ssm.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

2. Open the AWS CLI or Tools for Windows PowerShell and run one of the following commands, depending
   on the operating system type of your local machine, to create a service role
   in your account. Replace each `example resource
placeholder` with your own information.

Linux & macOS

```
aws iam create-role \
--role-name `AWSSystemsManagerDefaultEC2InstanceManagementRole` \
--path /service-role/ \
--assume-role-policy-document `file://trust-policy.json`
```

Windows

```
aws iam create-role ^
--role-name `AWSSystemsManagerDefaultEC2InstanceManagementRole` ^
--path /service-role/ ^
--assume-role-policy-document `file://trust-policy.json`
```

PowerShell

```
New-IAMRole `
-RoleName "`AWSSystemsManagerDefaultEC2InstanceManagementRole`" `
-Path "/service-role/" `
-AssumeRolePolicyDocument "`file://trust-policy.json`"
```

3. Run the following command to attach the
   `AmazonSSMManagedEC2InstanceDefaultPolicy` managed policy to
   your newly created role. Replace each `example resource
placeholder` with your own information.

Linux & macOS

```
aws iam attach-role-policy \
--policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedEC2InstanceDefaultPolicy \
--role-name `AWSSystemsManagerDefaultEC2InstanceManagementRole`
```

Windows

```
aws iam attach-role-policy ^
--policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedEC2InstanceDefaultPolicy ^
--role-name `AWSSystemsManagerDefaultEC2InstanceManagementRole`
```

PowerShell

```
Register-IAMRolePolicy `
-PolicyArn "arn:aws:iam::aws:policy/AmazonSSMManagedEC2InstanceDefaultPolicy" `
-RoleName "`AWSSystemsManagerDefaultEC2InstanceManagementRole`"
```

4. Open the AWS CLI or Tools for Windows PowerShell and run the following command. Replace each
   `example resource placeholder` with your own
   information.

Linux & macOS

```
aws ssm update-service-setting \
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role \
--setting-value `service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`
```

Windows

```
aws ssm update-service-setting ^
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role ^
--setting-value `service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`
```

PowerShell

```
Update-SSMServiceSetting `
-SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role" `
-SettingValue "`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`"
```

There is no output if the command succeeds. 5. Run the following command to view the current service settings for Default
Host Management Configuration in the current AWS account and
AWS Region.

Linux & macOS

```
aws ssm get-service-setting \
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role
```

Windows

```
aws ssm get-service-setting ^
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role
```

PowerShell

```
Get-SSMServiceSetting `
-SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role"
```

The command returns information like the following.

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/managed-instance/default-ec2-instance-management-role",
        "SettingValue": "service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole",
        "LastModifiedDate": "2022-11-28T08:21:03.576000-08:00",
        "LastModifiedUser": "System",
        "ARN": "arn:aws:ssm:us-east-2:-123456789012:servicesetting/ssm/managed-instance/default-ec2-instance-management-role",
        "Status": "Custom"
    }
}
```

## Deactivating the Default Host Management

Configuration setting

You can deactivate Default Host Management Configuration from the Fleet Manager
console, or by using the AWS Command Line Interface or AWS Tools for Windows PowerShell.

You must turn off the Default Host Management Configuration setting one by one in
each Region where you no longer want your your Amazon EC2 instances managed by this
configuration. Deactivating it in one Region doesn't deactivate it in all
Regions.

If you deactivate Default Host Management Configuration, and you have not attached
an instance profile to your Amazon EC2 instances that allows access to Systems Manager, they will
no longer be managed by Systems Manager.

###### To deactivate Default Host Management Configuration (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Account management, Default Host Management
   Configuration**.
4. Turn off **Enable Default Host Management
   Configuration**.
5. Choose **Configure** to disable Default Host Management
   Configuration.

###### To deactivate Default Host Management Configuration (command line)

- Open the AWS CLI or Tools for Windows PowerShell and run the following command. Replace each
  `example resource placeholder` with your own
  information.

Linux & macOS

```
aws ssm reset-service-setting \
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role
```

Windows

```
aws ssm reset-service-setting ^
--setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role
```

PowerShell

```
Reset-SSMServiceSetting `
-SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role"
```

## Least privilege policy examples for

Default Host Management Configuration

The following sample policies demonstrate how to prevent members of your
organization from making changes to the Default Host Management Configuration
setting in your account.

### Service control policy for AWS Organizations

The following policy demonstrates how to prevent non-administrative members in
your AWS Organizations from updating your Default Host Management Configuration setting.
Replace each `example resource placeholder` with your
own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Deny",
 "Action": [
 "ssm:UpdateServiceSetting",
 "ssm:ResetServiceSetting"
 ],
 "Resource": "arn:aws:ssm:*:*:servicesetting/ssm/managed-instance/default-ec2-instance-management-role",
 "Condition": {
 "StringNotEqualsIgnoreCase": {
 "aws:PrincipalTag/job-function": [
 "administrator"
 ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "ssm.amazonaws.com"
 },
 "StringNotEqualsIgnoreCase": {
 "aws:PrincipalTag/job-function": [
 "administrator"
 ]
 }
 }
 },
 {
 "Effect": "Deny",
 "Resource": "arn:aws:iam::*:role/`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DeleteRole"
 ],
 "Condition": {
 "StringNotEqualsIgnoreCase": {
 "aws:PrincipalTag/job-function": [
 "administrator"
 ]
 }
 }
 }
 ]
}`

```

### Policy for IAM principals

The following policy demonstrates how to prevent IAM groups, roles, or users
in your AWS Organizations from updating your Default Host Management Configuration
setting. Replace each `example resource placeholder`
with your own information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ssm:UpdateServiceSetting",
 "ssm:ResetServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/managed-instance/default-ec2-instance-management-role"
 },
 {
 "Effect": "Deny",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:DeleteRole",
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/`service-role/AWSSystemsManagerDefaultEC2InstanceManagementRole`"
 }
 ]
}`

```
