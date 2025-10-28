# MFA for Identity Center directory

users

###### Important

MFA in IAM Identity Center is currently not supported for [external identity providers](manage-your-identity-source-idp.md "manage-your-identity-source-idp.md").

IAM Identity Center comes preconfigured with multi-factor authentication (MFA) turned on by default so
that all users must sign in with MFA in addition to their user name and password. This
ensures that users must sign in to the AWS access portal using the following two factors:

- Their user name and password. This is the first factor and is something users
  know.
- Either a code, security key, or biometrics. This is the second factor and is
  something users have (possession) or are (biometric). The second factor might be
  either an authentication code generated from their mobile device, a security key
  connected to their computer, or user’s biometric scan.
  Together, these multiple factors provide increased security by preventing unauthorized
  access to your AWS resources unless a valid MFA challenge has been successfully
  completed.

Each user can register up to two virtual authenticator apps, which are one-time password
authenticator applications installed on your mobile device or tablet, and six FIDO
authenticators, which include built-in authenticators and security keys, for a total of
**eight** MFA devices. Learn more about [Available MFA types for IAM Identity Center](mfa-types.md "mfa-types.md").

###### Topics

- [Available MFA types for IAM Identity Center](mfa-types.md "mfa-types.md")
- [Configure MFA in IAM Identity Center](mfa-configure.md "mfa-configure.md")
- [Register an MFA device for users](how-to-register-device.md "how-to-register-device.md")
- [Renaming and deleting MFA devices in
  IAM Identity Center](how-to-manage-device.md "how-to-manage-device.md")
