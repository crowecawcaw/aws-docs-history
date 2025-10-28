# Configure access to the EC2 Serial Console

To configure access to the serial console, you must grant serial console access at the
account level and then configure IAM policies to grant access to your users. For Linux
instances you must also configure a password-based user on every instance so that your users
can use the serial console for troubleshooting.

EC2 Serial Console uses a virtual serial port connection to interact with an instance.
This connection is independent of the instance VPC, so that you can work with the
instance operating system and run troubleshooting tools even if there are boot failures
or network configuration issues. Because this connection is outside of the VPC network,
EC2 Serial Console does not use the instance security group or the subnet network ACL to
authorize traffic to the instance.

###### Before you begin

Verify that the [prerequisites](ec2-serial-console-prerequisites.md "ec2-serial-console-prerequisites.md")
are met.

###### Contents

- [Levels of access to the EC2 Serial Console](#serial-console-access-levels "#serial-console-access-levels")
- [Manage account access to the EC2 Serial Console](#serial-console-account-access "#serial-console-account-access")
- [Configure IAM policies for EC2 Serial Console access](#serial-console-iam "#serial-console-iam")
- [Set an OS user password on a Linux instance](#set-user-password "#set-user-password")

## Levels of access to the EC2 Serial Console

By default, there is no access to the serial console at the account level. You need to
explicitly grant access to the serial console at the account level. For more information,
see [Manage account access to the EC2 Serial Console](#serial-console-account-access "#serial-console-account-access").

You can use a service control policy (SCP) to allow access to the serial console within
your organization. You can then have granular access control at the user level by using an
IAM policy to control access. By using a combination of SCP and IAM policies, you have
different levels of access control to the serial console.

**Organization level**

You can use a service control policy (SCP) to allow access to the serial console
for member accounts within your organization. For more information about SCPs, see
[Service control
policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

**Instance level**

You can configure the serial console access policies by using IAM PrincipalTag and
ResourceTag constructions and by specifying instances by their ID. For more
information, see [Configure IAM policies for EC2 Serial Console access](#serial-console-iam "#serial-console-iam").

**User level**

You can configure access at the user level by configuring an IAM policy to allow
or deny a specified user the permission to push the SSH public key to the serial
console service of a particular instance. For more information, see [Configure IAM policies for EC2 Serial Console access](#serial-console-iam "#serial-console-iam").

**OS level** (Linux instances only)

You can set a user password at the guest OS level. This provides access to the
serial console for some use cases. However, to monitor the logs, you don't need a
password-based user. For more information, see [Set an OS user password on a Linux instance](#set-user-password "#set-user-password").

## Manage account access to the EC2 Serial Console

By default, there is no access to the serial console at the account level. You need to
explicitly grant access to the serial console at the account level.

This setting is configured at the account level, either directly in the account or by
using a declarative policy. It must be configured in each AWS Region where you want to
grant access to the serial console. Using a declarative policy allows you to apply the
setting across multiple Regions simultaneously, as well as across multiple accounts
simultaneously. When a declarative policy is in use, you can't modify the setting directly
within an account. This topic describes how to configure the setting directly within an
account. For information about using declarative policies, see [Declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide._

###### Contents

- [Grant permission to users to manage
  account access](configure-access-to-serial-console.md#sc-account-access-permissions "configure-access-to-serial-console.md#sc-account-access-permissions")
- [View account access status to the serial
  console](configure-access-to-serial-console.md#sc-view-account-access "configure-access-to-serial-console.md#sc-view-account-access")
- [Grant account access to the serial console](configure-access-to-serial-console.md#sc-grant-account-access "configure-access-to-serial-console.md#sc-grant-account-access")
- [Deny account access to the serial console](configure-access-to-serial-console.md#sc-deny-account-access "configure-access-to-serial-console.md#sc-deny-account-access")

### Grant permission to users to manage

account access

To allow your users to manage account access to the EC2 serial console, you need to
grant them the required IAM permissions.

The following policy grants permissions to view the account status, and to allow and
prevent account access to the EC2 serial console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:GetSerialConsoleAccessStatus",
 "ec2:EnableSerialConsoleAccess",
 "ec2:DisableSerialConsoleAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in
the _IAM User Guide_.

### View account access status to the serial

console

Console

###### To view account access to the serial console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the left navigation pane, choose **EC2 Dashboard**.
3. From **Account attributes**, choose **EC2 Serial
   Console**.
4. On the **EC2 Serial Console** tab, the value of
   **EC2 Serial Console access** is either
   **Allowed** or **Prevented**.

AWS CLI

###### To view account access to the serial console

Use the [get-serial-console-access-status](../../../cli/latest/reference/ec2/get-serial-console-access-status.md "../../../cli/latest/reference/ec2/get-serial-console-access-status.md") command.

```
aws ec2 get-serial-console-access-status
```

The following is example output. A value of `true` indicates that
the account is allowed access to the serial console.

```
{
    "SerialConsoleAccessEnabled": true,
    "ManagedBy": "account"
}
```

The `ManagedBy` field indicates the entity that configured the setting.
The possible values are `account` (configured directly) or
`declarative-policy`. For more information, see [Declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

PowerShell

###### To view account access to the serial console

Use the [Get-EC2SerialConsoleAccessStatus](../../../powershell/latest/reference/items/Get-EC2SerialConsoleAccessStatus.md "../../../powershell/latest/reference/items/Get-EC2SerialConsoleAccessStatus.md")
cmdlet.

```
Get-EC2SerialConsoleAccessStatus -Select *
```

The following is example output. A value of `True` indicates that
the account is allowed access to the serial console.

```
ManagedBy SerialConsoleAccessEnabled
--------- --------------------------
account   True
```

The `ManagedBy` field indicates the entity that configured the setting.
The possible values are `account` (configured directly) or
`declarative-policy`. For more information, see [Declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

### Grant account access to the serial console

Console

###### To grant account access to the serial console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the left navigation pane, choose **EC2 Dashboard**.
3. From **Account attributes**, choose **EC2 Serial
   Console**.
4. Choose **Manage**.
5. To allow access to the EC2 serial console of all instances in the account, select
   the **Allow** checkbox.
6. Choose **Update**.

AWS CLI

###### To grant account access to the serial console

Use the [enable-serial-console-access](../../../cli/latest/reference/ec2/enable-serial-console-access.md "../../../cli/latest/reference/ec2/enable-serial-console-access.md") command.

```
aws ec2 enable-serial-console-access
```

The following is example output.

```
{
    "SerialConsoleAccessEnabled": true
}
```

PowerShell

###### To grant account access to the serial console

Use the [Enable-EC2SerialConsoleAccess](../../../powershell/latest/reference/items/Enable-EC2SerialConsoleAccess.md "../../../powershell/latest/reference/items/Enable-EC2SerialConsoleAccess.md")
cmdlet.

```
Enable-EC2SerialConsoleAccess
```

The following is example output.

```
True
```

### Deny account access to the serial console

Console

###### To deny account access to the serial console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the left navigation pane, choose **EC2 Dashboard**.
3. From **Account attributes**, choose **EC2 Serial
   Console**.
4. Choose **Manage**.
5. To prevent access to the EC2 serial console of all instances in the account, clear
   the **Allow** checkbox.
6. Choose **Update**.

AWS CLI

###### To deny account access to the serial console

Use the [disable-serial-console-access](../../../cli/latest/reference/ec2/disable-serial-console-access.md "../../../cli/latest/reference/ec2/disable-serial-console-access.md") command.

```
aws ec2 disable-serial-console-access
```

The following is example output.

```
{
    "SerialConsoleAccessEnabled": false
}
```

PowerShell

###### To deny account access to the serial console

Use the [Disable-EC2SerialConsoleAccess](../../../powershell/latest/reference/items/Disable-EC2SerialConsoleAccess.md "../../../powershell/latest/reference/items/Disable-EC2SerialConsoleAccess.md")
cmdlet.

```
Disable-EC2SerialConsoleAccess
```

The following is example output.

```
False
```

## Configure IAM policies for EC2 Serial Console access

By default, your users do not have access to the serial console. Your organization must
configure IAM policies to grant your users the required access. For more information, see
[Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

For serial console access, create a JSON policy document that includes the
`ec2-instance-connect:SendSerialConsoleSSHPublicKey` action. This action grants
a user permission to push the public key to the serial console service, which starts a
serial console session. We recommend restricting access to specific EC2 instances.
Otherwise, all users with this permission can connect to the serial console of all EC2
instances.

###### Example IAM policies

- [Explicitly allow access to the serial
  console](#iam-explicitly-allow-access "#iam-explicitly-allow-access")
- [Explicitly deny access to the serial
  console](#serial-console-IAM-policy "#serial-console-IAM-policy")
- [Use resource tags to control access to the serial
  console](#iam-resource-tags "#iam-resource-tags")

### Explicitly allow access to the serial

console

By default, no one has access to the serial console. To grant access to the serial
console, you need to configure a policy to explicitly allow access. We recommend
configuring a policy that restricts access to specific instances.

The following policy allows access to the serial console of a specific instance,
identified by its instance ID.

Note that the `DescribeInstances`, `DescribeInstanceTypes`, and
`GetSerialConsoleAccessStatus` actions do not support resource-level
permissions, and therefore all resources, indicated by the `*` (asterisk), must
be specified for these actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDescribeInstances",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "ec2:GetSerialConsoleAccessStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowinstanceBasedSerialConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-0598c7d356eba48d7`"
 }
 ]
}`

```

### Explicitly deny access to the serial

console

The following IAM policy allows access to the serial console of all instances, denoted
by the `*` (asterisk), and explicitly denies access to the serial console of a
specific instance, identified by its ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSerialConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "ec2-instance-connect:SendSerialConsoleSSHPublicKey",
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "ec2:GetSerialConsoleAccessStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DenySerialConsoleAccess",
 "Effect": "Deny",
 "Action": [
 "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/`i-0598c7d356eba48d7`"
 }
 ]
}`

```

### Use resource tags to control access to the serial

console

You can use resource tags to control access to the serial console of an
instance.

Attribute-based access control is an authorization strategy that defines permissions
based on tags that can be attached to users and AWS resources. For example, the
following policy allows a user to initiate a serial console connection for an instance
only if that instance's resource tag and the principal's tag have the same
`SerialConsole` value for the tag key.

For more information about using tags to control access to your AWS resources, see
[Controlling
access to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources") in the _IAM User Guide_.

Note that the `DescribeInstances`, `DescribeInstanceTypes`, and
`GetSerialConsoleAccessStatus` actions do not support resource-level
permissions, and therefore all resources, indicated by the `*` (asterisk), must
be specified for these actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDescribeInstances",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeInstanceTypes",
 "ec2:GetSerialConsoleAccessStatus"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowTagBasedSerialConsoleAccess",
 "Effect": "Allow",
 "Action": [
 "ec2-instance-connect:SendSerialConsoleSSHPublicKey"
 ],
 "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:instance/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/`SerialConsole`": "${aws:PrincipalTag/`SerialConsole`}"
 }
 }
 }
 ]
}`

```

## Set an OS user password on a Linux instance

You can connect to the serial console without a password. However, to _use_ the serial console for troubleshooting a Linux instance, the
instance must have a password-based OS user.

You can set the password for any OS user, including the root user. Note that the root
user can modify all files, while each OS user might have limited permissions.

You must set a user password for every instance for which you will use the serial
console. This is a one-time requirement for each instance.

###### Note

By default, AMIs provided by AWS are not configured with a password-based user.
If you launched your instance using an AMI that already has the root user password
configured, you can skip these instructions.

###### To set an OS user password on a Linux instance

1. [Connect](connect-to-linux-instance.md "connect-to-linux-instance.md") to your instance. You can
   use any method for connecting to your instance, except the EC2 Serial Console connection
   method.
2. To set the password for a user, use the **passwd** command. In the
   following example, the user is `root`.

```
`[ec2-user ~]$` sudo passwd root
```

The following is example output.

```
Changing password for user root.
New password:
```

3. At the `New password` prompt, enter the new password.
4. At the prompt, re-enter the password.
