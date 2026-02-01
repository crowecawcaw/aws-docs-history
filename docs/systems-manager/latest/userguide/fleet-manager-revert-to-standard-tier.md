• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Reverting from the

advanced-instances tier to the standard-instances tier

This section describes how to change hybrid-activated nodes running in the
advanced-instances tier back to the standard-instances tier. This configuration
applies to all hybrid-activated nodes in an AWS account and a single
AWS Region.

###### Before you begin

Review the following important details.

###### Note

- You can't revert back to the standard-instance tier if you're
  running more than 1,000 hybrid-activated nodes in the account and
  Region. You must first deregister nodes until you have 1,000 or
  fewer. This also applies to Amazon Elastic Compute Cloud (Amazon EC2) instances that use a
  Systems Manager hybrid activation (which isn't a common scenario). For more
  information, see [Deregistering managed nodes
  in a hybrid and multicloud environment](fleet-manager-deregister-hybrid-nodes.md "fleet-manager-deregister-hybrid-nodes.md").
- After you revert, you won't be able to use Session Manager, a tool in
  AWS Systems Manager, to interactively access your hybrid-activated
  nodes.
- After you revert, you won't be able to use Patch Manager, a tool in
  AWS Systems Manager, to patch applications released by Microsoft on
  hybrid-activated nodes.
- The process of reverting all hybrid-activated nodes back to the
  standard-instance tier can take 30 minutes or more to
  complete.
  This section describes how to revert all hybrid-activated nodes in an
  AWS account and AWS Region from the advanced-instances tier to the
  standard-instances tier.

## Reverting to the

standard-instances tier (console)

The following procedure shows you how to use the Systems Manager console to change
all hybrid-activated nodes in your [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment to use the
standard-instances tier in the specified AWS account and
AWS Region.

###### To revert to the standard-instances tier (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Select the **Account settings** dropdown and
   choose **Instance tier settings**.
4. Choose **Change account setting**.
5. Review the information in the pop-up about changing account
   settings, and then if you approve, choose the option to accept and
   continue.

## Reverting to the

standard-instances tier (AWS CLI)

The following procedure shows you how to use the AWS Command Line Interface to change all
hybrid-activated nodes in your [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment to use the
standard-instances tier in the specified AWS account and
AWS Region.

###### To revert to the standard-instances tier using the AWS CLI

1. Open the AWS CLI and run the following command. Replace each
   `example resource placeholder` with
   your own information.

Linux & macOS

```
aws ssm update-service-setting \
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier \
    --setting-value standard
```

Windows

```
aws ssm update-service-setting ^
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier ^
    --setting-value standard
```

There is no output if the command succeeds. 2. Run the following command 30 minutes later to view the settings
for managed instances in the current AWS account and
AWS Region.

Linux & macOS

```
aws ssm get-service-setting \
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier
```

Windows

```
aws ssm get-service-setting ^
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier
```

The command returns information like the following.

```
{
    "ServiceSetting": {
        "SettingId": "/ssm/managed-instance/activation-tier",
        "SettingValue": "standard",
        "LastModifiedDate": 1555603376.138,
        "LastModifiedUser": "System",
        "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/managed-instance/activation-tier",
        "Status": "Default"
    }
}
```

The status changes to _Default_ after the
request has been approved.

## Reverting to the

standard-instances tier (PowerShell)

The following procedure shows you how to use AWS Tools for Windows PowerShell to change
hybrid-activated nodes in your hybrid and multicloud environment to use the
standard-instances tier in the specified AWS account and
AWS Region.

###### To revert to the standard-instances tier using PowerShell

1. Open AWS Tools for Windows PowerShell and run the following command.

```
Update-SSMServiceSetting `
    -SettingId "arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier" `
    -SettingValue "standard"
```

There is no output if the command succeeds. 2. Run the following command 30 minutes later to view the settings
for managed instances in the current AWS account and
AWS Region.

```
Get-SSMServiceSetting `
    -SettingId "arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier"
```

The command returns information like the following.

```
ARN: arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/managed-instance/activation-tier
LastModifiedDate : 4/18/2019 4:02:56 PM
LastModifiedUser : System
SettingId        : /ssm/managed-instance/activation-tier
SettingValue     : standard
Status           : Default

```

The status changes to _Default_ after the
request has been approved.
