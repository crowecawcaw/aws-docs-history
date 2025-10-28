# Turning on the

advanced-instances tier

AWS Systems Manager offers a standard-instances tier and an advanced-instances tier for
non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. The standard-instances tier lets
you register a maximum of 1,000 hybrid-activated machines per AWS account per
AWS Region. The advanced-instances tier is also required to use Patch Manager to
patch Microsoft-released applications on non-EC2 nodes, and to connect to
non-EC2 nodes using Session Manager. For more information, see Turning on the
advanced-instances tier.

This section describes how to configure your hybrid and multicloud environment
to use the advanced-instances tier.

###### Before you begin

Review pricing details for advanced instances. Advanced instances are
available on a per-use-basis. For more information see, [AWS Systems Manager
Pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

## Configuring

permissions to turn on the advanced-instances tier

Verify that you have permission in AWS Identity and Access Management (IAM) to change your
environment from the standard-instances tier to the advanced-instances tier.
You must either have the `AdministratorAccess` IAM policy
attached to your user, group, or role, or you must have permission to change
the Systems Manager activation-tier service setting. The activation-tier setting uses
the following API operations:

- [GetServiceSetting](../APIReference/API_GetServiceSetting.md "../APIReference/API_GetServiceSetting.md")
- [UpdateServiceSetting](../APIReference/API_UpdateServiceSetting.md "../APIReference/API_UpdateServiceSetting.md")
- [ResetServiceSetting](../APIReference/API_ResetServiceSetting.md "../APIReference/API_ResetServiceSetting.md")

Use the following procedure to add an inline IAM policy to a user
account. This policy allows a user to view the current managed-instance tier
setting. This policy also allows the user to change or reset the current
setting in the specified AWS account and AWS Region.

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. In the list, choose the name of the user to embed a policy
   in.
4. Choose the **Permissions** tab.
5. On the right side of the page, under **Permission
   policies**, choose **Add inline
   policy**.
6. Choose the **JSON** tab.
7. Replace the default content with the following:

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
 "ssm:ResetServiceSetting",
 "ssm:UpdateServiceSetting"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:servicesetting/ssm/managed-instance/activation-tier"
 }
 ]
}`

```

8. Choose **Review policy**.
9. On the **Review policy** page, for
   **Name**, enter a name for the inline policy.
   For example: `Managed-Instances-Tier`.
10. Choose **Create policy**.

Administrators can specify read-only permission by assigning the following
inline policy to the user.

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

For more information about creating and editing IAM policies, see [Creating IAM
Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

## Turning on the

advanced-instances tier (console)

The following procedure shows you how to use the Systems Manager console to change
_all_ non-EC2 nodes that were added using
managed-instance activation, in the specified AWS account and
AWS Region, to use the advanced-instances tier.

###### Before you begin

Verify that the console is open in the AWS Region where you created
your managed instances. You can switch Regions by using the list in the
top, right corner of the console.

Verify that you have completed the setup requirements for your Amazon Elastic Compute Cloud
(Amazon EC2) instances and non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. For
information, see [Setting up managed nodes for
AWS Systems Manager](systems-manager-setting-up-nodes.md "systems-manager-setting-up-nodes.md").

###### Important

The following procedure describes how to change an account-level
setting. This change results in charges being billed to your
account.

###### To turn on the advanced-instances tier (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose **Settings**, and then choose
   **Change instance tier settings**.
4. Review the information in the dialog box about changing account
   settings.
5. If you approve, choose the option to accept, and then choose
   **Change setting**.

The system can take several minutes to complete the process of moving all
instances from the standard-instances tier to the advanced-instances
tier.

###### Note

For information about changing back to the standard-instances tier,
see [Reverting from the
advanced-instances tier to the standard-instances tier](fleet-manager-revert-to-standard-tier.md "fleet-manager-revert-to-standard-tier.md").

## Turning on the

advanced-instances tier (AWS CLI)

The following procedure shows you how to use the AWS Command Line Interface to change
_all_ on-premises servers and VMs that were added
using managed-instance activation, in the specified AWS account and
AWS Region, to use the advanced-instances tier.

###### Important

The following procedure describes how to change an account-level
setting. This change results in charges being billed to your
account.

###### To turn on the advanced-instances tier using the AWS CLI

1. Open the AWS CLI and run the following command. Replace each
   `example resource placeholder` with
   your own information.

Linux & macOS

```
aws ssm update-service-setting \
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier \
    --setting-value advanced
```

Windows

```
aws ssm update-service-setting ^
    --setting-id arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier ^
    --setting-value advanced
```

There is no output if the command succeeds. 2. Run the following command to view the current service settings for
managed nodes in the current AWS account and AWS Region.

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
        "SettingValue": "advanced",
        "LastModifiedDate": 1555603376.138,
        "LastModifiedUser": "arn:aws:sts::123456789012:assumed-role/Administrator/User_1",
        "ARN": "arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/managed-instance/activation-tier",
        "Status": "PendingUpdate"
    }
}
```

## Turning on the

advanced-instances tier (PowerShell)

The following procedure shows you how to use the AWS Tools for Windows PowerShell to change
_all_ on-premises servers and VMs that were added
using managed-instance activation, in the specified AWS account and
AWS Region, to use the advanced-instances tier.

###### Important

The following procedure describes how to change an account-level
setting. This change results in charges being billed to your
account.

###### To turn on the advanced-instances tier using PowerShell

1. Open AWS Tools for Windows PowerShell and run the following command. Replace each
   `example resource placeholder` with
   your own information.

```
Update-SSMServiceSetting `
    -SettingId "arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier" `
    -SettingValue "advanced"
```

There is no output if the command succeeds. 2. Run the following command to view the current service settings for
managed nodes in the current AWS account and AWS Region.

```
Get-SSMServiceSetting `
    -SettingId "arn:aws:ssm:`region`:`aws-account-id`:servicesetting/ssm/managed-instance/activation-tier"
```

The command returns information like the following.

```
ARN:arn:aws:ssm:us-east-2:123456789012:servicesetting/ssm/managed-instance/activation-tier
LastModifiedDate : 4/18/2019 4:02:56 PM
LastModifiedUser : arn:aws:sts::123456789012:assumed-role/Administrator/User_1
SettingId        : /ssm/managed-instance/activation-tier
SettingValue     : advanced
Status           : PendingUpdate
```

The system can take several minutes to complete the process of moving all
nodes from the standard-instances tier to the advanced-instances
tier.

###### Note

For information about changing back to the standard-instances tier,
see [Reverting from the
advanced-instances tier to the standard-instances tier](fleet-manager-revert-to-standard-tier.md "fleet-manager-revert-to-standard-tier.md").
