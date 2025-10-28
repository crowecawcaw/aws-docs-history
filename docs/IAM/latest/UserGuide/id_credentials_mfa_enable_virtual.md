# Assign a virtual MFA device in the

AWS Management Console

You can use a phone or other device as a virtual multi-factor authentication (MFA) device.
To do this, install a mobile app that is compliant with [RFC
6238, a standards-based TOTP (time-based one-time password) algorithm](https://datatracker.ietf.org/doc/html/rfc6238 "https://datatracker.ietf.org/doc/html/rfc6238"). These apps
generate a six-digit authentication code. Because they can run on unsecured mobile devices,
virtual MFA might not provide the same level of security as phishing resistant options such as
[FIDO2](https://en.wikipedia.org/wiki/FIDO_Alliance#FIDO2 "https://en.wikipedia.org/wiki/FIDO_Alliance#FIDO2") security keys
and passkeys.

If you are considering moving to FIDO2 security keys for MFA, we strongly recommend that
you continue using a virtual MFA device while you wait for any hardware purchase approvals or
for your hardware to arrive.

Most virtual MFA apps support creating multiple virtual devices, allowing you to use the
same app for multiple AWS accounts or users. You can register up to **eight** MFA devices of any combination of [MFA types](https://aws.amazon.com/iam/features/mfa/ "https://aws.amazon.com/iam/features/mfa/") with your AWS account root user and
IAM users. You only need one MFA device to sign in to the AWS Management Console or create a session
through the AWS CLI. We recommend that you register multiple MFA devices. For authenticator
applications, we also recommend enabling the cloud backup or sync feature to help you avoid
losing access to your account if you lose or break your device.

AWS requires a virtual MFA app that produces a six-digit OTP. For a list of virtual MFA
apps that you can use, see [Multi-Factor Authentication](https://aws.amazon.com/iam/features/mfa/?audit=2019q1 "https://aws.amazon.com/iam/features/mfa/?audit=2019q1").

###### Topics

- [Permissions required](#mfa_enable_virtual_permissions-required "#mfa_enable_virtual_permissions-required")
- [Enable a virtual MFA device for an
  IAM user (console)](#enable-virt-mfa-for-iam-user "#enable-virt-mfa-for-iam-user")
- [Replace a virtual MFA device](#replace-virt-mfa "#replace-virt-mfa")

## Permissions required

To manage virtual MFA devices for your IAM user, you must have the permissions from
the following policy: [AWS:
Allows MFA-authenticated IAM users to manage their own MFA device on the Security
credentials page](reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.md "reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.md").

## Enable a virtual MFA device for an

IAM user (console)

You can use IAM in the AWS Management Console to enable and manage a virtual MFA device for an
IAM user in your account. You can attach tags to your IAM resources, including virtual
MFA devices, to identify, organize, and control access to them. You can tag virtual MFA
devices only when you use the AWS CLI or AWS API. To enable and manage an MFA device using
the AWS CLI or AWS API, see [Assign MFA devices
in the AWS CLI or AWS API](id_credentials_mfa_enable_cliapi.md "id_credentials_mfa_enable_cliapi.md"). For more information about tagging
IAM resources, see [Tags for AWS Identity and Access Management resources](id_tags.md "id_tags.md").

###### Note

You must have physical access to the hardware that will host the user's virtual MFA
device in order to configure MFA. For example, you might configure MFA for a user who
will use a virtual MFA device running on a smartphone. In that case, you must have the
smartphone available in order to finish the wizard. Because of this, you might want to
let users configure and manage their own virtual MFA devices. In that case, you must
grant users the permissions to perform the necessary IAM actions. For more information
and for an example of an IAM policy that grants these permissions, see the [IAM tutorial: Permit users to manage
their credentials and MFA settings](tutorial_users-self-manage-mfa-and-creds.md "tutorial_users-self-manage-mfa-and-creds.md") and example policy [AWS:
Allows MFA-authenticated IAM users to manage their own MFA device on the Security
credentials page](reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.md "reference_policies_examples_aws_my-sec-creds-self-manage-mfa-only.md").

###### To enable a virtual MFA device for an IAM user (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. In the **Users** list, choose the name of the IAM user.
4. Choose the **Security Credentials** tab. Under
   **Multi-factor authentication (MFA)**, choose **Assign
   MFA device**.
5. In the wizard, type a **Device name**, choose
   **Authenticator app**, and then choose
   **Next**.

IAM generates and displays configuration information for the virtual MFA device,
including a QR code graphic. The graphic is a representation of the "secret
configuration key" that is available for manual entry on devices that do not support
QR codes. 6. Open your virtual MFA app. For a list of apps that you can use for hosting virtual
MFA devices, see [Multi-Factor
Authentication](http://aws.amazon.com/iam/details/mfa/ "http://aws.amazon.com/iam/details/mfa/").

If the virtual MFA app supports multiple virtual MFA devices or accounts, choose
the option to create a new virtual MFA device or account. 7. Determine whether the MFA app supports QR codes, and then do one of the
following:

    * From the wizard, choose **Show QR code**, and then use the
     app to scan the QR code. This might be a camera icon or **Scan
     code** option that uses the device's camera to scan the
     code.
    * From the wizard, choose **Show secret key**, and then type
     the secret key into your MFA app.

When you are finished, the virtual MFA device starts generating one-time
passwords. 8. On the **Set up device** page, in the **MFA code
1** box, type the one-time password that currently appears in the virtual
MFA device. Wait up to 30 seconds for the device to generate a new one-time password.
Then type the second one-time password into the **MFA code 2** box.
Choose **Add MFA**.

###### Important

Submit your request immediately after generating the codes. If you generate the
codes and then wait too long to submit the request, the MFA device successfully
associates with the user but the MFA device is out of sync. This happens because
time-based one-time passwords (TOTP) expire after a short period of time. If this
happens, you can [resync the
device](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md").

The virtual MFA device is now ready for use with AWS. For information about using MFA
with the AWS Management Console, see [MFA enabled sign-in](console_sign-in-mfa.md "console_sign-in-mfa.md").

###### Note

Unassigned virtual MFA devices in your AWS account are deleted when you’re adding
new virtual MFA devices either via the AWS Management Console or during the sign-in process. Unassigned
virtual MFA devices are devices in your account but not used by account root user or
IAM users for the sign-in process. They’re deleted so new virtual MFA devices can be
added to your account. It also allows you to reuse device names.

- To view unassigned virtual MFA devices in your account, you can use either the
  [list-virtual-mfa-devices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-virtual-mfa-devices.html") AWS CLI command or [API](../APIReference/API_ListVirtualMFADevices.md "../APIReference/API_ListVirtualMFADevices.md")
  call.
- To deactivate a virtual MFA device, you can use either the [deactivate-mfa-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/deactivate-mfa-device.html") AWS CLI command or [API](../APIReference/API_DeactivateMFADevice.md "../APIReference/API_DeactivateMFADevice.md") call. The
  device will become unassigned.
- To attach an unassigned virtual MFA device to your AWS account root user or
  IAM users, you'll need the authentication code generated by the device along with
  either the [enable-mfa-device](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/enable-mfa-device.html") AWS CLI command or [API](../APIReference/API_EnableMFADevice.md "../APIReference/API_EnableMFADevice.md") call.

## Replace a virtual MFA device

Your AWS account root user and IAM users can register up to **eight** MFA devices of any combination of MFA types. If the user loses a
device or needs to replace it for any reason, deactivate the old device. Then you can add
the new device for the user.

- To deactivate the device currently associated with another IAM user, see [Deactivate an MFA device](id_credentials_mfa_disable.md "id_credentials_mfa_disable.md").
- To add a replacement virtual MFA device for another IAM user, follow the steps
  in the procedure [Enable a virtual MFA device for an
  IAM user (console)](#enable-virt-mfa-for-iam-user "#enable-virt-mfa-for-iam-user") above.
- To add a replacement virtual MFA device for the AWS account root user, follow the steps in
  the procedure [Enable a virtual MFA device for the root user
  (console)](enable-virt-mfa-for-root.md "enable-virt-mfa-for-root.md").
