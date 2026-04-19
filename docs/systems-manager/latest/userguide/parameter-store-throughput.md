# Changing Parameter Store throughput

Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process for [GetParameter](../APIReference/API_GetParameter.md "../APIReference/API_GetParameter.md"), [GetParameters](../APIReference/API_GetParameters.md "../APIReference/API_GetParameters.md"), and [PutParameter](../APIReference/API_PutParameter.md "../APIReference/API_PutParameter.md") API calls for your AWS account and Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can typically use this default setting without additional cost.

For higher-volume workloads, you can enable higher throughput, which increases the maximum number of supported transactions per second for your account and Region, at a cost. Increased throughput allows you to operate Parameter Store at higher volumes to support applications and workloads that need concurrent access to multiple parameters. If you're experiencing `ThrottlingException: Rate exceeded` errors, we recommend enabling higher throughput.

Throughput operates independently of parameter tiers, but the two are often used together to meet performance and scale requirements:

Standard parameters (default tier) are designed for most workloads. They support up to 10,000 parameters per Region, with values up to 4 KB, and incur no additional storage cost.
Advanced parameters support larger values (up to 8 KB), higher parameter counts (up to 100,000), and additional features such as parameter policies. These capabilities come with additional charges.

While parameter tiers control storage limits and feature availability, throughput settings control request volume. For example, you might use standard parameters with default throughput for simple applications, or combine advanced parameters with higher throughput to support large-scale, high-frequency access patterns. In general, increasing throughput is necessary when your application exceeds default TPS limits (for example, during bursts of concurrent reads or writes), regardless of which parameter tier you use.

You can enable or disable higher throughput at any time from the Parameter Store **Settings** page or by using the AWS CLI.

For more information about maximum throughput and other Parameter Store quotas, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm").

###### Important

Increasing the throughput quota incurs a charge on your AWS account. For more information, see [AWS Systems Manager Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

###### Topics

- [Increasing throughput using the console](#parameter-store-throughput-increasing "#parameter-store-throughput-increasing")
- [Increasing throughput using the AWS CLI](#parameter-store-throughput-increasing-cli "#parameter-store-throughput-increasing-cli")
- [Increasing throughput (PowerShell)](#parameter-store-throughput-increasing-ps "#parameter-store-throughput-increasing-ps")

## Increasing throughput using the console

The following procedure describes how to use the Systems Manager console to increase the
number of transactions per second that Parameter Store can process for the current
AWS account and AWS Region.

###### To increase Parameter Store throughput using the console

###### Tip

If you haven't created a parameter yet, you can use the AWS Command Line Interface
(AWS CLI) or AWS Tools for Windows PowerShell to increase throughput. For information, see [Increasing throughput using the AWS CLI](#parameter-store-throughput-increasing-cli "#parameter-store-throughput-increasing-cli") and
[Increasing throughput (PowerShell)](#parameter-store-throughput-increasing-ps "#parameter-store-throughput-increasing-ps").

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Choose the **Settings** tab.
4. Choose the **Manage settings**.
5. In the **Parameter throughput** section, choose an option.
6. If prompted, select the option to approve the changes and authorize charges. Choose
   **Save settings**.

## Increasing throughput using the AWS CLI

The following procedure shows how to use the AWS CLI to increase the number of
transactions per second that Parameter Store can process for the current AWS account
and AWS Region.

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

## Increasing throughput (PowerShell)

The following procedure shows how to use the Tools for Windows PowerShell to increase the number of
transactions per second that Parameter Store can process for the current AWS account
and AWS Region.

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
