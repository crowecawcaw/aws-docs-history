# Deactivating AWS GovCloud (US) MFA devices

If you are having trouble signing in with a multi-factor authentication (MFA) device as an IAM user, contact your administrator for help.

As an administrator, you can deactivate the device for another IAM user. This allows the user to sign in without using MFA. You might do this as a temporary solution while the MFA device is replaced, or if the device is temporarily unavailable. However, we recommend that you enable a new device for the user as soon as possible. To learn how to enable a new MFA device, see [Enabling MFA devices for users in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa_enable.md "../../../IAM/latest/UserGuide/id_credentials_mfa_enable.md").

## Deactivating MFA devices (console)

To deactivate an MFA device for another IAM user (console)

1. Sign in to the AWS Management Console and open the IAM console at https://signin.amazonaws-us-gov.com/iam/
2. In the navigation pane, choose **Users**.
3. To deactivate the MFA device for a user, choose the name of the user whose MFA you want to remove.
4. Choose the **Security credentials** tab. Next to **Assigned MFA device**, choose **Manage**.
5. In the **Manage MFA device** wizard, choose **Remove**, and then choose **Remove**.

The device is removed from AWS. It cannot be used to sign in or authenticate requests until it is reactivated and associated with an AWS user.

## Deactivating MFA devices (AWS CLI)

To [deactivate an MFA device](../../../cli/latest/reference/iam/deactivate-mfa-device.md "../../../cli/latest/reference/iam/deactivate-mfa-device.md") for an IAM user (AWS CLI) run this command:

```
aws iam deactivate-mfa-device
```

Example to deactivate an MFA device:

```
aws iam deactivate-mfa-device --user-name Bob --serial-number arn:aws-us-gov:iam::210987654321:mfa/BobsMFADevice
```

This command deactivates the virtual MFA device with the ARN `arn:aws-us-gov:iam::210987654321:mfa/BobsMFADevice` that is associated with the user `Bob`.

## Deactivating MFA devices (AWS API)

###### To deactivate an MFA device for an IAM user (AWS API)

- Call this operation: [DeactivateMFADevice](../../../IAM/latest/APIReference/API_DeactivateMFADevice.md "../../../IAM/latest/APIReference/API_DeactivateMFADevice.md")
