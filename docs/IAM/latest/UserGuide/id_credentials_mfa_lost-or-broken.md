# Recover an MFA protected identity in

IAM

If your [virtual MFA device](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md") or [hardware TOTP token](id_credentials_mfa_enable_physical.md "id_credentials_mfa_enable_physical.md") appears to be
functioning properly, but you can't use it to access your AWS resources, it might be out of
synchronization with AWS. For information about synchronizing a virtual MFA device or hardware
MFA device, see [Resynchronize virtual and hardware MFA
devices](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md"). [FIDO security keys](id_credentials_mfa_enable_fido.md "id_credentials_mfa_enable_fido.md") do not go out of
sync.

If the [MFA device](id_credentials_mfa.md "id_credentials_mfa.md") for a AWS account root user is lost,
damaged, or not working, you can recover access to your account. IAM users must contact an
administrator to deactivate the device.

###### Important

We recommend that you activate multiple MFA devices. Registering multiple MFA devices
helps ensure continued access if a device is lost or broken. Your AWS account root user and IAM users
can register up to eight MFA devices of any type.

## Prerequisite – Use another MFA

device

If your [multi-factor authentication (MFA) device](id_credentials_mfa.md "id_credentials_mfa.md")
is lost, damaged, or not working, you can sign in using another MFA device registered to the
same root user or IAM user.

###### To sign in using another MFA device

1. Sign in to the [AWS Management Console](url-comsole-domain.md "url-comsole-domain.md") with your
   AWS account ID or account alias and password.
2. On the **Additional verification required** page or
   **Multi-factor authentication** page, choose **Try another MFA
   method**.
3. Authenticate with the type of MFA device that you selected.
4. The next step varies based on whether you successfully signed in with an alternate MFA
   device.
   - If you have successfully signed in, you can [Resynchronize virtual and hardware MFA
     devices](id_credentials_mfa_sync.md "id_credentials_mfa_sync.md"), which
     may resolve the issue. If your MFA device is lost or broken, you can deactivate it.
     For instructions on deactivating any MFA device type, see [Deactivate an MFA device](id_credentials_mfa_disable.md "id_credentials_mfa_disable.md").
   - If you can't sign in with MFA, use the steps in [Recovering a root user MFA device](#root-mfa-lost-or-broken "#root-mfa-lost-or-broken") or [Recovering an IAM user MFA device](#iam-user-mfa-lost-or-broken "#iam-user-mfa-lost-or-broken")
     to recover your MFA protected identity.

## Recovering a root user MFA device

If you can't sign in with MFA, you can use alternative methods of authentication to sign
in by verifying your identity using the email and the primary contact phone number registered
with your account.

Confirm you are able to access the email and primary contact phone number associated with
your account before you use alternative authentication factors to sign in as a root user. If you
need to update the primary contact phone number, sign in as an IAM user with _Administrator_ access instead of the root user. For additional
instructions on updating the account contact information, see [Editing contact
information](../../../accounts/latest/reference/manage-acct-update-contact-primary.md "../../../accounts/latest/reference/manage-acct-update-contact-primary.md") in the _AWS Billing User Guide_. If you do not have access
to an email and primary contact phone number, you must contact [AWS Support](https://support.aws.amazon.com/#/contacts/aws-mfa-support "https://support.aws.amazon.com/#/contacts/aws-mfa-support").

###### Important

We recommend that you keep the email address and contact phone number linked to your
root user up to date for a successful account recovery. For more information, see [Update the primary
contact for your AWS account](../../../accounts/latest/reference/manage-acct-update-contact-primary.md "../../../accounts/latest/reference/manage-acct-update-contact-primary.md") in the _AWS Account Management Reference
Guide_.

###### To sign in using alternative factors of authentication as an AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.
2. On the **Additional verification required** page, select an MFA
   method to authenticate with and choose **Next**.

###### Note

You might see alternative text, such as **Sign in using
MFA**, **Troubleshoot your authentication
device**, or **Troubleshoot MFA**, but the
functionality is the same. If you can't use alternative authentication factors to verify
your account email address and primary contact phone number, contact [AWS Support](https://support.aws.amazon.com/#/contacts/aws-mfa-support "https://support.aws.amazon.com/#/contacts/aws-mfa-support") to
deactivate your MFA device. 3. Depending on the type of MFA you are using, you will see a different page, but the
**Troubleshoot MFA** option functions the same. On the
**Additional verification required** page or **Multi-factor
authentication** page, choose **Troubleshoot
MFA**. 4. If required, type your password again and choose **Sign
in**. 5. On the **Troubleshoot your authentication device** page, in the
**Sign in using alternative factors of authentication** section, choose
**Sign in using alternative factors**. 6. On the **Sign in using alternative factors of authentication** page,
authenticate your account by verifying the email address, choose **Send
verification email**. 7. Check the email that is associated with your AWS account for a message from
Amazon Web Services (recover-mfa-no-reply@verify.signin.aws). Follow the directions in the
email.

If you don't see the email in your account, check your spam folder, or return to your
browser and choose **Resend the email**. 8. After you verify your email address, you can continue authenticating your account. To
verify your primary contact phone number, choose **Call me now**. 9. Answer the call from AWS and, when prompted, enter the 6-digit number from the AWS
website on your phone keypad.

If you don't receive a call from AWS, choose **Sign in** to sign in
to the console again and start over. Or see [Lost or unusable
Multi-Factor Authentication (MFA) device](https://support.aws.amazon.com/#/contacts/aws-mfa-support "https://support.aws.amazon.com/#/contacts/aws-mfa-support") to contact support for help. 10. After you verify your phone number, you can sign in to your account by choosing
**Sign in to the console**. 11. The next step varies depending on the type of MFA you are using:

    * For a virtual MFA device, remove the account from your device. Then go to the
     [AWS Security
     Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") page and delete the old MFA virtual device entity before you
     create a new one.
    * For a FIDO security key, go to the [AWS Security
     Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") page and deactivate the old FIDO security key before enabling a
     new one.
    * For a hardware TOTP token, contact the third-party provider for help with fixing
     or replacing the device. You can continue to sign in using alternative factors of
     authentication until you receive your new device. After you have the new hardware MFA
     device, go to the [AWS
     Security Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") page and delete the old MFA device.

###### Note

You don't have to replace a lost or stolen MFA device with the same type of device.
For example, if you break your FIDO security key and order a new one, you can use
virtual MFA or a hardware TOTP token until the new FIDO key arrives.

###### Important

If your MFA device is missing or stolen, change your root user password after signing in
and establishing your replacement MFA device. An attacker may have stolen the authentication
device and might also have your current password. For more information, see [Change the password for the AWS account root user](root-user-password.md "root-user-password.md").

## Recovering an IAM user MFA device

If you are an IAM user that can't sign in with MFA, you can't recover an MFA device by
yourself. You must contact an administrator to deactivate the device. Then you can enable a
new device.

###### To get help for an MFA device as an IAM user

1. Contact the AWS administrator or other person who gave you the user name and
   password for the IAM user. The administrator must deactivate the MFA device as described
   in [Deactivate an MFA device](id_credentials_mfa_disable.md "id_credentials_mfa_disable.md")
   so that you can sign in.
2. The next step varies depending on the type of MFA you are using:
   - For a virtual MFA device, remove the account from your device. Then enable the
     virtual device as described in [Assign a virtual MFA device in the
     AWS Management Console](id_credentials_mfa_enable_virtual.md "id_credentials_mfa_enable_virtual.md").
   - For a FIDO security key, contact the third-party provider for help with replacing
     the device. When you receive the new FIDO security key, enable it as described in
     [Assign a passkey or security key in the
     AWS Management Console](id_credentials_mfa_enable_fido.md "id_credentials_mfa_enable_fido.md").
   - For a hardware TOTP token, contact the third-party provider for help with fixing
     or replacing the device. After you have the new physical MFA device, enable the device
     as described in [Assign a hardware TOTP token in the
     AWS Management Console](id_credentials_mfa_enable_physical.md "id_credentials_mfa_enable_physical.md").

###### Note

You don't have to replace a lost or stolen MFA device with the same type of device.
You can have up to eight MFA devices of any combination. For example, if you break your
FIDO security key and order a new one, you can use virtual MFA or a hardware TOTP token
until the new FIDO key arrives. 3. If your MFA device is missing or stolen, also change your password in case an attacker
has stolen the authentication device and might also have your current password. For more
information, see [Manage passwords for
IAM users](id_credentials_passwords_admin-change-user.md "id_credentials_passwords_admin-change-user.md")
