# Deactivate an MFA device

If you are having trouble signing in with a multi-factor authentication (MFA) device as an
IAM user, contact your administrator for help.

As an administrator, you can deactivate the device for another IAM user. This allows the
user to sign in without using MFA. You might do this as a temporary solution while the MFA
device is replaced, or if the device is temporarily unavailable. However, we recommend that
you enable a new device for the user as soon as possible. To learn how to enable a new MFA
device, see [AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md").

###### Note

If you use the API or AWS CLI to delete a user from your AWS account, you must
deactivate or delete the user's MFA device. You make this change as part of the process of
removing the user. For more information about removing users, see [Remove or deactivate an IAM user](id_users_remove.md "id_users_remove.md").

###### Topics

- [Deactivating MFA devices (console)](#deactive-mfa-console "#deactive-mfa-console")
- [Deactivating MFA devices (AWS CLI)](#deactivate-mfa-cli "#deactivate-mfa-cli")
- [Deactivating MFA devices (AWS API)](#deactivate-mfa-api "#deactivate-mfa-api")

## Deactivating MFA devices (console)

###### To deactivate an MFA device for another IAM

user (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. To deactivate the MFA device for a user, choose the name of the user whose MFA you
   want to remove.
4. Choose the **Security credentials** tab.
5. Under **​Multi-factor authentication (MFA)**, choose the radio
   button next to the MFA device, choose **Remove**, and then choose
   **Remove**.

The device is removed from AWS. It cannot be used to sign in or authenticate
requests until it is reactivated and associated with an AWS user or
AWS account root user.

###### To deactivate the MFA device for your AWS account root user

(console)

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

###### Note

As the root user, you can't sign in to the **Sign in as IAM user** page. If you see the
**Sign in as IAM user** page, choose **Sign in using root user email** near the bottom of
the page. For help signing in as the root user, see [Signing in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to- root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to- root-user-sign-in-tutorial.md") in the
_AWS Sign-In User Guide_. 2. On the right side of the navigation bar, choose on your account name, and then
choose **Security credentials**. If necessary, choose
**Continue to Security credentials**.

![Security credentials in the navigation menu](images/security-credentials-root.shared.console.png) 3. In the **Multi-factor authentication (MFA)** section, choose the
radio button next the MFA device that you want to deactivate and choose
**Remove**. 4. Choose **Remove**.

The MFA device is deactivated for the AWS account. Check the email that is
associated with your AWS account for a confirmation message from Amazon Web Services. The
email informs you that your Amazon Web Services multi-factor authentication (MFA) has been
deactivated. The message will come from `@amazon.com` or `@aws.amazon.com`.

###### Note

Unassigned virtual MFA devices in your AWS account are deleted when you’re adding
new virtual MFA devices either via the AWS Management Console or during the sign-in process. Unassigned
virtual MFA devices are devices in your account but not used by account root user or
IAM users for the sign-in process. They’re deleted so new virtual MFA devices can be
added to your account. It also allows you to reuse device names.

## Deactivating MFA devices (AWS CLI)

###### To deactivate an MFA device for an IAM user (AWS CLI)

- Run this command: [`aws iam deactivate-mfa-device`](../../../cli/latest/reference/iam/deactivate-mfa-device.md "../../../cli/latest/reference/iam/deactivate-mfa-device.md")

## Deactivating MFA devices (AWS API)

###### To deactivate an MFA device for an IAM user (AWS API)

- Call this operation: [`DeactivateMFADevice`](../APIReference/API_DeactivateMFADevice.md "../APIReference/API_DeactivateMFADevice.md")
