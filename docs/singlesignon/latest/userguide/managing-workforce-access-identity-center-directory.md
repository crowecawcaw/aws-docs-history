# Managing access for users in the Identity Center directory

Learn how to manage passwords and multi-factor authentication (MFA) for users in the IAM Identity Center directory. These security features help protect user accounts.

###### Note

These features do not apply to Active Directory users or external identity provider users.

Administrators can manage both passwords and MFA through the IAM Identity Center console. These security features work only with the built-in Identity Center directory.

## Password management

Password management includes these capabilities:

- Reset passwords with email instructions
- Generate one-time passwords
- Configure automatic email verification for API-created users

AWS enforces fixed security requirements, including complexity rules and password reuse restrictions.

## MFA

MFA is enabled by default and supports up to eight devices per user.

Supported device types include:

- Authenticator apps
- Security keys
- Built-in biometric authenticators

Administrators can register and manage MFA devices for users.

###### Topics

- [Setting up user passwords](set-up-user-passwords.md "set-up-user-passwords.md")
- [MFA for Identity Center directory
  users](enable-mfa.md "enable-mfa.md")
