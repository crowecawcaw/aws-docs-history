# Manage AWS Builder ID multi-factor authentication (MFA)

Multi-factor authentication (MFA) is a simple and effective mechanism to enhance your
security. The first factor — your password — is a secret that you memorize, also known as a
knowledge factor. Other factors can be possession factors (something you have, such as a
security key) or inherence factors (something you are, such as a biometric scan). We
strongly recommend that you configure MFA to add an additional layer for your
AWS Builder ID.

You can register a built-in authenticator and also register a security key that you keep
in a physically secure location. If you're unable to use your built-in authenticator, then
you can use your registered security key. For authenticator applications, you can also
enable the cloud backup or sync feature in those apps. This helps you avoid losing access to
your profile if you lose or break your MFA device.

## Key points

- We recommend that you register multiple MFA devices. If you lose access to all
  registered MFA devices, you will be unable to recover your AWS Builder ID.
- We recommend that you periodically review your registered MFA devices to
  ensure they are up to date and functional. Additionally, you should store those
  devices in a place that is physically secure when not in use.
- If you created your account using **Continue with
  Google**, you can enable multi-factor authentication through your Google
  account. For details, see [Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop "https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop").

## Available MFA types for AWS Builder ID

AWS Builder ID supports the following multi-factor authentication (MFA) device
types.

### FIDO2 authenticators

[FIDO2](https://fidoalliance.org/fido2/ "https://fidoalliance.org/fido2/") is a standard that
includes CTAP2 and [WebAuthn](https://www.w3.org/TR/webauthn-2/ "https://www.w3.org/TR/webauthn-2/")
and is based on public key cryptography. FIDO credentials are phishing-resistant
because they are unique to the website that the credentials were created such as
AWS.

AWS supports the two most common form factors for FIDO authenticators: built-in
authenticators and security keys. See below for more information about the most
common types of FIDO authenticators.

###### Topics

- [Built-in authenticators](#built-in-auth-aws_builder_id "#built-in-auth-aws_builder_id")
- [Security keys](#security-keys-aws_builder_id "#security-keys-aws_builder_id")
- [Password managers, passkey providers,
  and other FIDO authenticators](#other-mfa-aws_builder_id "#other-mfa-aws_builder_id")

#### Built-in authenticators

Some devices have built-in authenticators, such as TouchID on MacBook or a
Windows Hello-compatible camera. If your device is compatible with FIDO
protocols, including WebAuthn, you can use your fingerprint or face as second
factor. For more information, see [FIDO Authentication](https://fidoalliance.org/fido2/ "https://fidoalliance.org/fido2/").

#### Security keys

You can purchase a FIDO2-compatible external USB, BLE, or NFC-connected
security key. When you’re prompted for an MFA device, tap the key’s sensor.
YubiKey or Feitian make compatible devices. For a list of all compatible
security keys, see [FIDO
Certified Products](https://fidoalliance.org/certification/fido-certified-products/ "https://fidoalliance.org/certification/fido-certified-products/ ").

#### Password managers, passkey providers,

and other FIDO authenticators

Multiple third party providers support FIDO authentication in mobile
applications, as features in password managers, smart cards with a FIDO mode,
and other form factors. These FIDO-compatible devices can work with IAM Identity Center, but
we recommend that you test a FIDO authenticator yourself before enabling this
option for MFA.

###### Note

Some FIDO authenticators can create discoverable FIDO credentials known as
passkeys. Passkeys may be bound to the device that creates them, or they may be
syncable and backed up to a cloud. For example, you can register a passkey using
Apple Touch ID on a supported Macbook, and then log in to a site from a Windows
laptop using Google Chrome with your passkey in iCloud by following the
on-screen prompts at sign-in. For more information about which devices support
syncable passkeys and current passkey interoperability between operating systems
and browsers, see [Device
Support](https://passkeys.dev/device-support/ "https://passkeys.dev/device-support/") at [passkeys.dev](https://passkeys.dev/ "https://passkeys.dev/"),
a resource maintained by the FIDO Alliance And World Wide Web Consortium (W3C).

### Authenticator applications

Authenticator apps are one-time password (OTP)-based third party-authenticators.
You can use an authenticator application installed on your mobile device or tablet
as an authorized MFA device. The third-party authenticator application must be
compliant with RFC 6238, which is a standards-based time-based one-time password
(TOTP) algorithm capable of generating six-digit authentication codes.

When prompted for MFA, you must enter a valid code from your authenticator app
within the input box presented. Each MFA device assigned to a user must be unique.
Two authenticator apps can be registered for any given user.

You can choose from the following well-known third-party authenticator apps.
However, any TOTP-compliant application works with AWS Builder ID MFA.

| Operating system | Tested authenticator app                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Android          | [1Password](https://play.google.com/store/apps/details?id=com.onepassword.android "https://play.google.com/store/apps/details?id=com.onepassword.android"), [Authy](https://play.google.com/store/apps/details?id=com.authy.authy "https://play.google.com/store/apps/details?id=com.authy.authy"), [Duo Mobile](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile "https://play.google.com/store/apps/details?id=com.duosecurity.duomobile"), [Microsoft Authenticator](https://play.google.com/store/apps/details?id=com.azure.authenticator "https://play.google.com/store/apps/details?id=com.azure.authenticator"), [Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2 "https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2") |
| iOS              | [1Password](https://apps.apple.com/us/app/1password-password-manager/id1511601750 "https://apps.apple.com/us/app/1password-password-manager/id1511601750"), [Authy](https://apps.apple.com/us/app/authy/id494168017 "https://apps.apple.com/us/app/authy/id494168017"), [Duo<br>Mobile](https://apps.apple.com/us/app/duo-mobile/id422663827 "https://apps.apple.com/us/app/duo-mobile/id422663827"), [Microsoft Authenticator](https://apps.apple.com/us/app/microsoft-authenticator/id983156458 "https://apps.apple.com/us/app/microsoft-authenticator/id983156458"), [Google Authenticator](https://apps.apple.com/us/app/google-authenticator/id388497605 "https://apps.apple.com/us/app/google-authenticator/id388497605")                                                                                                                    |

## Register your AWS Builder ID MFA device

###### Note

After you sign up for MFA, sign out, and then sign in on the same device, you
might not be prompted for MFA on trusted devices.

###### To register your MFA device using an authenticator app

1. Sign in to your AWS Builder ID profile at [https://profile.aws.amazon.com](https://profile.aws.amazon.com "https://profile.aws.amazon.com").
2. Choose **Security**.
3. On the **Security** page, choose **Register
   device**.
4. On the **Register MFA device** page, choose
   **Authenticator app**.
5. AWS Builder ID operates and displays configuration information, including a QR code
   graphic. The graphic is a representation of the "secret configuration key" that
   is available for manual entry in authenticator apps that do not support QR
   codes.
6. Open your authenticator app. For a list of apps, see [Authenticator applications](#auth-apps-aws_builder_id "#auth-apps-aws_builder_id").

If the authenticator app supports multiple MFA devices or accounts, choose the
option to create a new MFA device or account. 7. Determine whether the MFA app supports QR codes, and then do one of the
following on the **Set up your authenticator app** page:

    1. Choose **Show QR code**, and then use the app to scan
     the QR code. For example, you might choose the camera icon or choose an
     option similar to **Scan code**. Then use the device's
     camera to scan the code.
    2. Choose **Show secret key**, and then enter that
     secret key into your MFA app.

When you finish, your authenticator app will generate and display a one-time
password. 8. In the **Authenticator code** box, enter the one-time
password that currently appears in your authenticator app. Choose
**Assign MFA**.

###### Important

Submit your request immediately after generating the code. If you generate
the code and then wait too long to submit the request, the MFA device is
successfully associated with your AWS Builder ID, but the MFA device is out of
sync. This happens because time-based one-time passwords (TOTP) expire after
a short period of time. If this happens, you can resync the device. For more
information, see [I get the message 'An unexpected error has
occurred' when I try to register or sign in with an authenticator app](troubleshooting-builder-id-issues.md#syncing-mfa-aws_builder_id "troubleshooting-builder-id-issues.md#syncing-mfa-aws_builder_id"). 9. To give your device a friendly name in AWS Builder ID, choose
**Rename**. This name helps you distinguish this device
from others that you register.

The MFA device is now ready for use with AWS Builder ID.

## Register a security key as your AWS Builder ID

MFA device

###### To register your MFA device using a security key

1. Sign in to your AWS Builder ID profile at [https://profile.aws.amazon.com](https://profile.aws.amazon.com "https://profile.aws.amazon.com").
2. Choose **Security**.
3. On the **Security** page, choose **Register
   device**.
4. On the **Register MFA device** page, choose
   **Security key**.
5. Ensure that your security key is enabled. If you use a separate physical
   security key, connect it to your computer.
6. Follow the instructions on your screen. Your experience varies based on your
   operating system and browser.
7. To give your device a friendly name in AWS Builder ID, choose
   **Rename**. This name helps you distinguish this device
   from others that you register.

The MFA device is now ready for use with AWS Builder ID.

## Rename your AWS Builder ID MFA device

###### To rename your MFA device

1. Sign in to your AWS Builder ID profile at [https://profile.aws.amazon.com](https://profile.aws.amazon.com "https://profile.aws.amazon.com").
2. Choose **Security**. When you arrive at the page, you see
   that **Rename** is grayed out.
3. Select the MFA device that you want to change. This allows you to choose
   **Rename**. Then a dialog box appears.
4. In the prompt that opens, enter the new name in **MFA device
   name**, and choose **Rename**. The renamed device
   appears under **Multi-factor authentication (MFA)
   devices**.

## Delete your MFA device

We recommend that you keep two or more active MFA devices. Before you remove a device,
see [Register your AWS Builder ID MFA device](#register-mfa-aws_builder_id "#register-mfa-aws_builder_id") to register a replacement MFA device.
To disable multi-factor authentication for your AWS Builder ID, remove all registered MFA
devices from your profile.

###### To delete an MFA device

1. Sign in to your AWS Builder ID profile at [https://profile.aws.amazon.com](https://profile.aws.amazon.com "https://profile.aws.amazon.com").
2. Choose **Security**.
3. Select the MFA device that you want to change and choose
   **Delete**.
4. In the **Delete MFA device?** modal, follow the instructions
   to delete your device.
5. Choose **Delete**.

The deleted device no longer appears under **Multi-factor authentication (MFA)
devices**.
