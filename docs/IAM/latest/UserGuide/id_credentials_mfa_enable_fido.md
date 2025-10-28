# Assign a passkey or security key in the

AWS Management Console

Passkeys are a type of [multi-factor authentication (MFA)
device](id_credentials_mfa.md "id_credentials_mfa.md") that you can use to protect your AWS resources. AWS supports synced passkeys
and device-bound passkeys also known as security keys.

Synced passkeys allow IAM users to access their FIDO sign-in credentials on many of their
devices, even new ones, without having to re-enroll every device on every account. Synced
passkeys include first-party credential managers like Google, Apple, and Microsoft and
third-party credential managers such as 1Password, Dashlane, and Bitwarden as a second factor.
You can also use on-device biometrics (e.g., TouchID, FaceID) to unlock your chosen credential
manager to use passkeys.

Alternatively, device-bound passkeys are bound to a FIDO security key that you plug into a
USB port on your computer and then tap when prompted to securely complete the sign-in process.
If you already use a FIDO security key with other services, and it has an [AWS supported
configuration](id_credentials_mfa_fido_supported_configurations.md "id_credentials_mfa_fido_supported_configurations.md") (for example, the YubiKey 5 Series from Yubico), you can also use it with
AWS. Otherwise, you need to purchase a FIDO security key if you want to use WebAuthn for MFA
in AWS. Additionally, FIDO security keys can support multiple IAM or root users on the same
device, enhancing their utility for account security. For specifications and purchase
information for both device types, see [Multi-Factor Authentication](http://aws.amazon.com/iam/details/mfa/ "http://aws.amazon.com/iam/details/mfa/").

You can register up to **eight** MFA devices of any combination
of the [currently supported MFA
types](https://aws.amazon.com/iam/features/mfa/ "https://aws.amazon.com/iam/features/mfa/") with your AWS account root user and IAM users. With multiple MFA devices, you only need
one MFA device to sign in to the AWS Management Console or create a session through the AWS CLI as that user.
We recommend that you register multiple MFA devices. For example, you can register a built-in
authenticator and also register a security key that you keep in a physically secure location. If
you’re unable to use your built-in authenticator, then you can use your registered security key.
For authenticator applications, we also recommend enabling the cloud backup or sync feature in
those apps to help you avoid losing access to your account if you lose or break your device with
the authenticator apps.

###### Note

We recommend that you require your human users to use temporary credentials when accessing
AWS. Your users can federate into AWS with an identity provider where they authenticate
with their corporate credentials and MFA configurations. To manage access to AWS and
business applications, we recommend that you use IAM Identity Center. For more information, see the [IAM Identity Center User
Guide](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

###### Topics

- [Permissions
  required](#enable-fido-mfa-for-iam-user-permissions-required "#enable-fido-mfa-for-iam-user-permissions-required")
- [Enable a passkey or security key for your
  own IAM user (console)](#enable-fido-mfa-for-own-iam-user "#enable-fido-mfa-for-own-iam-user")
- [Enable a passkey or security key for another
  IAM user (console)](#enable-fido-mfa-for-iam-user "#enable-fido-mfa-for-iam-user")
- [Replace a passkey or security key](#replace-fido-mfa "#replace-fido-mfa")
- [Supported configurations
  for using passkeys and security keys](id_credentials_mfa_fido_supported_configurations.md "id_credentials_mfa_fido_supported_configurations.md")

## Permissions

required

To manage a FIDO passkey for your own IAM user while protecting sensitive MFA-related
actions, you must have the permissions from the following policy:

###### Note

The ARN values are static values and are not an indicator of what protocol was used to
register the authenticator. We have deprecated U2F, so all new implementations use
WebAuthn.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowManageOwnUserMFA",
 "Effect": "Allow",
 "Action": [
 "iam:DeactivateMFADevice",
 "iam:EnableMFADevice",
 "iam:GetUser",
 "iam:ListMFADevices",
 "iam:ResyncMFADevice"
 ],
 "Resource": "arn:aws:iam::*:user/${aws:username}"
 },
 {
 "Sid": "DenyAllExceptListedIfNoMFA",
 "Effect": "Deny",
 "NotAction": [
 "iam:EnableMFADevice",
 "iam:GetUser",
 "iam:ListMFADevices",
 "iam:ResyncMFADevice"
 ],
 "Resource": "*",
 "Condition": {
 "BoolIfExists": {
 "aws:MultiFactorAuthPresent": "false"
 }
 }
 }
 ]
}`

```

## Enable a passkey or security key for your

own IAM user (console)

You can enable a passkey or security key for your own IAM user from the AWS Management Console only,
not from the AWS CLI or AWS API. Before you can enable a security key, you must have physical
access to the device.

###### To enable a passkey or security key for your own IAM user (console)

1. Use your AWS account ID or account alias, your IAM user name, and your password to sign in
   to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").

###### Note

For your convenience, the AWS sign-in page uses a browser cookie to remember your
IAM user name and account information. If you previously signed in as a different user,
choose **Sign in to a different account** near the bottom of the page to
return to the main sign-in page. From there, you can type your AWS account ID or account
alias to be redirected to the IAM user sign-in page for your account.

To get your AWS account ID, contact your administrator. 2. In the navigation bar on the upper right, choose your user name, and then choose
**Security credentials**.

![AWS Management Console Security credentials link](images/security-credentials-user.shared.console.png) 3. On the selected IAM user's page, choose the **Security
credentials** tab. 4. Under **Multi-factor authentication (MFA)**, choose **Assign
MFA device**. 5. On the **MFA device name** page, enter a **Device
name**, choose **Passkey or Security Key**, and then choose
**Next**. 6. On **Set up device**, set up your passkey. Create a passkey with
biometric data like your face or fingerprint, with a device pin, or by inserting the FIDO
security key into your computer's USB port and tapping it. 7. Follow the instructions on your browser and then choose
**Continue**.

You have now registered your passkey or security key for use with AWS. For information
about using MFA with the AWS Management Console, see [MFA enabled sign-in](console_sign-in-mfa.md "console_sign-in-mfa.md").

## Enable a passkey or security key for another

IAM user (console)

You can enable a passkey or security for another IAM user from the AWS Management Console only, not
from the AWS CLI or AWS API.

###### To enable a passkey or security for another IAM user (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Under **Users**, choose the name of the user for whom you want to
   enable MFA.
4. On the selected IAM user page, choose the **Security Credentials**
   tab.
5. Under **Multi-factor authentication (MFA)**, choose **Assign
   MFA device**.
6. On the **MFA device name** page, enter a **Device
   name**, choose **Passkey or Security Key**, and then choose
   **Next**.
7. On **Set up device**, set up your passkey. Create a passkey with
   biometric data like your face or fingerprint, with a device pin, or by inserting the FIDO
   security key into your computer's USB port and tapping it.
8. Follow the instructions on your browser and then choose
   **Continue**.

You have now registered a passkey or security key for another IAM user to use with
AWS. For information about using MFA with the AWS Management Console, see [MFA enabled sign-in](console_sign-in-mfa.md "console_sign-in-mfa.md").

## Replace a passkey or security key

You can have up to eight MFA devices of any combination of the [currently supported MFA types](https://aws.amazon.com/iam/features/mfa/ "https://aws.amazon.com/iam/features/mfa/")
assigned to a user at a time with your AWS account root user and IAM users. If the user loses a FIDO
authenticator or needs to replace it for any reason, you must first deactivate the old FIDO
authenticator. Then you can add a new MFA device for the user.

- To deactivate the device currently associated with an IAM user, see [Deactivate an MFA device](id_credentials_mfa_disable.md "id_credentials_mfa_disable.md").
- To add a new FIDO security key for an IAM user, see [Enable a passkey or security key for your
  own IAM user (console)](#enable-fido-mfa-for-own-iam-user "#enable-fido-mfa-for-own-iam-user").

If you don't have access to a new passkey or security key, you can enable a new virtual
MFA device or hardware TOTP token. See one of the following for instructions:

- [Assign a virtual MFA device in the
  AWS Management Console](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md")
- [Assign a hardware TOTP token in the
  AWS Management Console](id_credentials_mfa_enable_physical.md "id_credentials_mfa_enable_physical.md")
