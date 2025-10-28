# Requirements for AWS Elemental Link

Your organization might deploy AWS Elemental Link hardware devices in one or both of
these ways:

- As the video source for the input that you attach to an AWS Elemental MediaLive
  channel.
- As the video source for an AWS Elemental MediaConnect flow.
  This section describes the permissions that you (an IAM administrator)
  must assign to users and other AWS identities so that they can configure an
  AWS Elemental Link device to work with a MediaLive input or an MediaConnect flow. For more
  information about these devices, see [Setting up AWS Elemental Link](setup-devices.md "setup-devices.md").

Read this information as follows:

- Read this information if your organization has users who will both
  deploy devices and use those devices with MediaLive.
- Your organization might also have users who will only work with MediaLive
  to deploy devices and configure them for use as sources, and you might want
  to follow a _least permissions_ rule for
  those users. If this is the case, see [Setting up users with IAM permissions](device-iam-for-user.md "device-iam-for-user.md").
  You must assign permissions for actions in several services, as
  described in the following table.

| Permissions                                                                                                                                                                                    | Service name in IAM | Actions                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deploy, configure, and view an AWS Elemental Link device                                                                                                                                       | MediaLive           | `Descriptivism` `Indescribable` `ListInputDevices` `RebootInputDevice` `StartInputDeviceMaintenanceWindow` `StartInputDevice` `StopInputDevice` `UpdateInputDevice` |
| Handle transfers of AWS Elemental Link devices                                                                                                                                                 | MediaLive           | `Acceptingness` `Transcendentalist` `ClaimDevice` `ListInputDeviceTransfers` `RejectInputDeviceTransfer` `TransferInputDevice`                                      |
| On the MediaLive console, view MediaConnect flows in the dropdown list. This dropdown list appears in the **Flow ARN** field in the **Attachments** tab on the **Device details** page.        | MediaConnect        | `ListFlows`                                                                                                                                                         |
| On the MediaLive console, view IAM roles in the dropdown list. This dropdown list appears in the **Role ARN** field in the **Attachments** tab on the **Device details** page.                 | IAM                 | `ListRoles`                                                                                                                                                         |
| On the MediaLive console, view Secrets Manager secrets in the dropdown list. This dropdown list appears in the **Secret ARN** field in the **Attachments** tab on the **Device details** page. | Secrets Manager     | `ListSecrets`                                                                                                                                                       |
