• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Increasing or resetting Parameter Store

throughput

Increasing Parameter Store throughput increases the maximum number of transactions per
second (TPS) that Parameter Store, a tool in AWS Systems Manager, can process. Increased throughput
allows you to operate Parameter Store at higher volumes to support applications and
workloads that need concurrent access to multiple parameters. You can increase the
quota up to the max throughput on the **Settings** tab.

The Parameter Store throughput setting applies to all transactions created by all
IAM users in the current AWS account and AWS Region. The throughput setting
applies to standard and advanced parameters.

###### Note

Typically, updates are immediately visible in Service Quotas. In rare cases, it can
take up to 24 hours for an update to be reflected.

For more information about max throughput default and maximum limits, see [AWS Systems Manager
endpoints and quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm").

Increasing the throughput quota incurs a charge on your AWS account. For more
information, see [AWS Systems Manager
Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

###### Topics

- [Configuring permissions
  to change Parameter Store throughput](#parameter-store-throughput-permissions "#parameter-store-throughput-permissions")
- [Increasing or resetting
  throughput using the console](#parameter-store-throughput-increasing "#parameter-store-throughput-increasing")
- [Increasing or
  resetting throughput using the AWS CLI](#parameter-store-throughput-increasing-cli "#parameter-store-throughput-increasing-cli")
- [Increasing or
  resetting throughput (PowerShell)](#parameter-store-throughput-increasing-ps "#parameter-store-throughput-increasing-ps")

## Configuring permissions

to change Parameter Store throughput

Verify that you have permission in IAM to change Parameter Store throughput by
doing one of the following:

- Make sure that the `AdministratorAccess` policy is attached
  to your IAM entity (user, group, or role).
- Make sure that you have permission to change the throughput service
  setting by using the following API operations:
  - [GetServiceSetting](../APIReference/API_GetServiceSetting.md "../APIReference/API_GetServiceSetting.md")
  - [UpdateServiceSetting](../APIReference/API_UpdateServiceSetting.md "../APIReference/API_UpdateServiceSetting.md")
  - [ResetServiceSetting](../APIReference/API_ResetServiceSetting.md "../APIReference/API_ResetServiceSetting.md")

Grant the following permissions to the IAM entity to allow a user to view
and change the parameter-throughput setting for parameters in a specific
AWS Region in an AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/parameter-store/high-throughput-enabled"
 }
 ]
}`

```

Administrators can specify read-only permission by assigning the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetServiceSetting"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "ssm:ResetServiceSetting",
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "*"
 }
 ]
}`

```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Increasing or resetting

throughput using the console

The following procedure shows how to use the Systems Manager console to increase the
number of transactions per second that Parameter Store can process for the current
AWS account and AWS Region. It also shows how to revert to the standard
settings if you no longer need increased throughput or no longer want to incur
charges.

###### To increase or reset Parameter Store throughput using the console

###### Tip

If you haven't created a parameter yet, you can use the AWS Command Line Interface
(AWS CLI) or AWS Tools for Windows PowerShell to increase throughput. For information, see [Increasing or
resetting throughput using the AWS CLI](#parameter-store-throughput-increasing-cli "#parameter-store-throughput-increasing-cli") and
[Increasing or
resetting throughput (PowerShell)](#parameter-store-throughput-increasing-ps "#parameter-store-throughput-increasing-ps").

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose the **Settings** tab.
4. To increase throughput, choose **Set limit**.

-or-

To revert to the default limit, choose **Reset
limit**. 5. If you are increasing the limit, do the following:

    * Select the check box for **I accept that changing this
     setting incurs charges on my
     AWS account**.
    * Choose **Set limit**.

-or-

If you are resetting the limit to the default, do the
following:

    * Select the check box for **I accept that resetting to
     the default throughput limit causes Parameter Store to process
     fewer transactions per second**.
    * Choose **Reset limit**.

## Increasing or

resetting throughput using the AWS CLI

The following procedure shows how to use the AWS CLI to increase the number of
transactions per second that Parameter Store can process for the current AWS account
and AWS Region. You can also revert to the default limit.

###### To increase Parameter Store throughput using the AWS CLI

1. Open the AWS CLI and run the following command to increase the
   transactions per second that Parameter Store can process in the current
   AWS account and AWS Region.

```
aws ssm update-service-setting --setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled --setting-value true
```

There is no output if the command succeeds. 2. Run the following command to view the current throughput service
settings for Parameter Store in the current AWS account and
AWS Region.

```
aws ssm get-service-setting --setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled
```

The system returns information similar to the following:

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/parameter-store/high-throughput-enabled",
        "SettingValue": "true",
        "LastModifiedDate": 1556551683.923,
        "LastModifiedUser": "arn:aws:sts::123456789012:assumed-role/Administrator/Jasper",
        "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled",
        "Status": "Customized"
    }
}
```

If you no longer need increased throughput, or if you no longer want to incur
charges, you can revert to the standard settings. To revert your settings, run
the following command.

```
aws ssm reset-service-setting --setting-id arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled
```

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/parameter-store/high-throughput-enabled",
        "SettingValue": "false",
        "LastModifiedDate": 1555532818.578,
        "LastModifiedUser": "System",
        "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled",
        "Status": "Default"
    }
}
```

## Increasing or

resetting throughput (PowerShell)

The following procedure shows how to use the Tools for Windows PowerShell to increase the number of
transactions per second that Parameter Store can process for the current AWS account
and AWS Region. You can also revert to the default limit.

###### To increase Parameter Store throughput using PowerShell

1. Increase Parameter Store throughput in the current AWS account and
   AWS Region using the AWS Tools for PowerShell (Tools for PowerShell).

```
Update-SSMServiceSetting -SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled" -SettingValue "true" -Region `region`
```

There is no output if the command succeeds. 2. Run the following command to view the current throughput service
settings for Parameter Store in the current AWS account and
AWS Region.

```
Get-SSMServiceSetting -SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled" -Region `region`
```

The systems returns information similar to the following:

```
ARN              : arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled
LastModifiedDate : 4/29/2019 3:35:44 PM
LastModifiedUser : arn:aws:sts::123456789012:assumed-role/Administrator/Jasper
SettingId        : /ssm/parameter-store/high-throughput-enabled
SettingValue     : true
Status           : Customized

```

If you no longer need increased throughput, or if you no longer want to incur
charges, you can revert to the standard settings. To revert your settings, run
the following command.

```
Reset-SSMServiceSetting -SettingId "arn:aws:ssm:`region`:`account-id`:servicesetting/ssm/parameter-store/high-throughput-enabled" -Region `region`
```

The system returns information similar to the following:

```
ARN              : arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled
LastModifiedDate : 4/17/2019 8:26:58 PM
LastModifiedUser : System
SettingId        : /ssm/parameter-store/high-throughput-enabled
SettingValue     : false
Status           : Default
```
