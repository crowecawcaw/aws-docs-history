# Multi-factor authentication for AWS account root user

Multi-factor authentication (MFA) is a simple and effective mechanism to enhance your
security. The first factor — your password — is a secret that you memorize, also known as a
knowledge factor. Other factors can be possession factors (something you have, such as a
security key) or inherence factors (something you are, such as a biometric scan). For
increased security, we strongly recommend that you configure multi-factor authentication (MFA)
to help protect your AWS resources.

###### Note

All AWS account types (standalone, management, and member accounts) require MFA to be
configured for their root user. Users must register MFA within 35 days of their first sign-in
attempt to access the AWS Management Console if MFA is not already enabled.

You can enable MFA for the AWS account root user and IAM users. When you enable MFA for the root user,
it only affects the root user credentials. For more information about how to enable MFA for your
IAM users, see [AWS Multi-factor authentication in IAM](id_credentials_mfa.md "id_credentials_mfa.md").

###### Note

AWS accounts managed using AWS Organizations may have the option to [centrally manage root access](id_root-user.md#id_root-user-access-management "id_root-user.md#id_root-user-access-management") for member
accounts to prevent credential recovery and access at scale. If this option is enabled, you
can delete root user credentials from member accounts, including passwords and MFA, effectively
preventing sign-in as the root user, password recovery, or setting up MFA. Alternatively, if
you prefer to maintain password-based sign-in methods, secure your account by registering
MFA to enhance account protection.

Before you enable MFA for your root user, review and [update
your account settings and contact information](../../../accounts/latest/reference/manage-acct-update-root-user.md "../../../accounts/latest/reference/manage-acct-update-root-user.md") to make sure that you have access to
the email and phone number. If your MFA device is lost, stolen, or not working, you can still
sign in as the root user by verifying your identity using that email and phone number. To learn
about signing in using alternative factors of authentication, see [Recover an MFA protected identity in
IAM](id_credentials_mfa_lost-or-broken.md "id_credentials_mfa_lost-or-broken.md"). To disable this feature, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

AWS supports the following MFA types for your root user:

- [Passkeys and security keys](#passkeys-security-keys-for-root "#passkeys-security-keys-for-root")
- [Virtual authenticator applications](#virtual-auth-apps-for-root "#virtual-auth-apps-for-root")
- [Hardware TOTP tokens](#hardware-totp-token-for-root "#hardware-totp-token-for-root")

## Passkeys and security keys

AWS Identity and Access Management supports passkeys and security keys for MFA. Based on FIDO standards, passkeys
use public key cryptography to provide strong, phishing-resistant authentication that is
more secure than passwords. AWS supports two types of passkeys: device-bound passkeys
(security keys) and synced passkeys.

- **Security keys**: These are physical devices, like a
  YubiKey, used as a second factor for authentication. A single security key can support
  multiple root user accounts and IAM users.
- **Synced passkeys**: These use credential managers from
  providers such as Google, Apple, Microsoft accounts, and third-party services like
  1Password, Dashlane, and Bitwarden as a second factor.

You can use built-in biometric authenticators, like Touch ID on Apple MacBooks, to
unlock your credential manager and sign in to AWS. Passkeys are created with your chosen
provider using your fingerprint, face, or device PIN. You can also use a cross-device
authentication (CDA) passkey from one device, like a mobile device or hardware security key,
to sign in on another device like a laptop. For more information, see [cross-device authentication](https://passkeys.dev/docs/reference/terms/#cross-device-authentication-cda "https://passkeys.dev/docs/reference/terms/#cross-device-authentication-cda") (CDA).

You can sync passkeys across your devices to facilitate sign-ins with AWS, enhancing
usability and recoverability. For more information about enabling passkeys and security
keys, see [Enable a passkey or security key for the root user
(console)](enable-fido-mfa-for-root.md "enable-fido-mfa-for-root.md").

The FIDO Alliance maintains a list of all [FIDO Certified
products](https://fidoalliance.org/certification/fido-certified-products/ "https://fidoalliance.org/certification/fido-certified-products/") that are compatible with FIDO specifications.

## Virtual authenticator applications

A virtual authenticator application runs on a phone or other device and emulates a
physical device. Virtual authenticator apps implement the [time-based one-time password (TOTP)
algorithm](https://datatracker.ietf.org/doc/html/rfc6238 "https://datatracker.ietf.org/doc/html/rfc6238") and support multiple tokens on a single device. The user must type a
valid code from the device when prompted during sign-in. Each token assigned to a user must
be unique. A user can't type a code from another user's token to authenticate.

We do recommend that you use a virtual MFA device while waiting for hardware purchase
approval or while you wait for your hardware to arrive. For a list of a few supported apps
that you can use as virtual MFA devices, see [Multi-Factor Authentication
(MFA)](https://aws.amazon.com/iam/features/mfa/?audit=2019q1 "https://aws.amazon.com/iam/features/mfa/?audit=2019q1"). For instructions on setting up a virtual MFA device with AWS, see [Enable a virtual MFA device for the root user
(console)](enable-virt-mfa-for-root.md "enable-virt-mfa-for-root.md").

## Hardware TOTP tokens

A hardware device generates a six-digit numeric code based on the [time-based one-time password (TOTP)
algorithm](https://datatracker.ietf.org/doc/html/rfc6238 "https://datatracker.ietf.org/doc/html/rfc6238"). The user must type a valid code from the device on a second webpage
during sign-in. Each MFA device assigned to a user must be unique. A user cannot type a code
from another user's device to be authenticated. For information on supported hardware MFA
devices, see [Multi-Factor
Authentication (MFA)](https://aws.amazon.com/iam/features/mfa/?audit=2019q1 "https://aws.amazon.com/iam/features/mfa/?audit=2019q1"). For instructions on setting up a hardware TOTP token with
AWS, see [Enable a hardware TOTP token for the root user
(console)](enable-hw-mfa-for-root.md "enable-hw-mfa-for-root.md").

If you want to use a physical MFA device, we recommend that you use FIDO security keys
as an alternative to hardware TOTP devices. FIDO security keys offer the benefits of no
battery requirements, phishing resistance, and they support multiple root and IAM users on
a single device for enhanced security.

###### Topics

- [Enable a passkey or security key for the root user
  (console)](enable-fido-mfa-for-root.md "enable-fido-mfa-for-root.md")
- [Enable a virtual MFA device for the root user
  (console)](enable-virt-mfa-for-root.md "enable-virt-mfa-for-root.md")
- [Enable a hardware TOTP token for the root user
  (console)](enable-hw-mfa-for-root.md "enable-hw-mfa-for-root.md")
