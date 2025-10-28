# Setting up users with IAM permissions

This section describes the permissions that an IAM administrator must assign to users
and other AWS identities so that they can configure a Link device to work with a
MediaLive input or an MediaConnect flow.

This information supplements the information about setting up a user to work with all
MediaLive features. Read this information as follows:

- Read this section if your organization has users who will only work with MediaLive to
  deploy devices and configure them for use as sources, and you want to follow a _least permissions_ rule.
- If your organization has users who will deploy devices, use those devices, and use
  all MediaLive features, see [Requirements for AWS Elemental Link](requirements-for-link.md "requirements-for-link.md"). You should revise their
  existing policies to include the device permissions.
  This section assumes that you have already performed these tasks:

- You have performed the initial setup described in [Preliminary steps for setting up to use MediaLive](setting-up.md "setting-up.md") in
  order to sign up for MediaLive and to create an administrator.
- You have read the recommendations in [Identity and Access Management for
  AWS Elemental MediaLive](security-iam.md "security-iam.md")about how to
  create administrators, users, and other AWS identities.

###### Topics

- [Required permissions](#device-iam-permissions "#device-iam-permissions")
- [Creating the policy](#device-iam-policy "#device-iam-policy")

## Required permissions

You must assign permissions for actions in several services, as described in the
following table.

| Permissions                                                                                                                                                                                    | Service name in IAM | Actions                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View, configure, and manage a Link device                                                                                                                                                      | medialive           | `DescribeInputDevice` `DescribeInputDeviceThumbnail` `ListInputDevices` `RebootInputDevice` `StartInputDeviceMaintenanceWindow` `StartInputDevice` `StopInputDevice` `UpdateInputDevice` |
| Handle transfers of Link devices                                                                                                                                                               | medialive           | `AcceptInputDeviceTransfer` `CancelInputDeviceTransfer` `ClaimDevice` `ListInputDeviceTransfers` `RejectInputDeviceTransfer` `TransferInputDevice`                                       |
| On the MediaLive console, view MediaConnect flows in the dropdown list. This dropdown list appears in the **Flow ARN** field in the **Attachments** tab on the **Device details** page.        | mediaconnect        | `ListFlows`                                                                                                                                                                              |
| On the MediaLive console, view Secrets Manager secrets in the dropdown list. This dropdown list appears in the **Secret ARN** field in the **Attachments** tab on the **Device details** page. | secretsmanager      | `ListSecrets`                                                                                                                                                                            |
| On the MediaLive console, view IAM roles in the dropdown list. This dropdown list appears in the **Role ARN** field in the **Attachments** tab on the **Device details** page.                 | iam                 | `ListRoles`                                                                                                                                                                              | ## Creating the policy 1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 2. In the navigation pane on the left, choose **Policies**. Choose **Create Policy**, then choose the **JSON** tab. 3. In the **Policy editor**, clear the sample content and paste the policy that appears after this procedure. 4. Give the policy a name that makes it clear that this policy is for using Link. For example, `ElementalLinkAccess`. 5. Choose **Create policy**. Sample policy: JSON `` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "medialive:DescribeInputDevice", "medialive:DescribeInputDeviceThumbnail", "medialive:ListInputDevices", "medialive:RebootInputDevice", "medialive:StartInputDeviceMaintenanceWindow", "medialive:StartInputDevice", "medialive:StopInputDevice", "medialive:UpdateInputDevice" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "medialive:AcceptInputDeviceTransfer", "medialive:CancelInputDeviceTransfer", "medialive:ClaimDevice", "medialive:ListInputDeviceTransfers", "medialive:RejectInputDeviceTransfer", "medialive:TransferInputDevice" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "mediaconnect:ListFlows" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "secretsmanager:ListSecrets" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "iam:ListRoles" ], "Resource": [ "*" ] } ] }` `` |
