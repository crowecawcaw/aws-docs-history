# Manage quorum authentication (M of N access control) using

CloudHSM CLI

AWS CloudHSM clusters support quorum authentication, also known as M of N access control. This
feature requires HSM users to cooperate for certain operations, adding an extra layer of
protection.

With quorum authentication, no single user on the HSM can perform quorum-controlled operations on
the HSM. Instead, a minimum number of HSM users (at least 2) must cooperate to do these
operations.

Quorum authentication can control the following operations:

- HSM user management by [admin](understanding-users.md#admin "understanding-users.md#admin"): Creating and deleting HSM
  users or changing a different HSM user's password. For more information, see [User management with quorum authentication enabled
  for AWS CloudHSM using CloudHSM CLI](quorum-auth-chsm-cli-admin.md "quorum-auth-chsm-cli-admin.md").
  Key points about quorum authentication in AWS CloudHSM.

- An HSM user can sign their own quorum token—that is, providing
  one of the required approvals for quorum authentication.
- You choose the minimum number of quorum approvers, which ranges from two (2) to eight (8).
- HSMs can store up to 1024 quorum tokens. When this limit is reached, the HSM purges an expired token to create a new one.
- Tokens expire ten minutes after creation by default.
- For clusters with MFA enabled, the same key is used for quorum authentication and
  multi-factor authentication (MFA). See [Using CloudHSM CLI
  to manage MFA](login-mfa-token-sign.md "login-mfa-token-sign.md") for more information.
- Each HSM can contain one token per Admin service and multiple tokens per Crypto User service.
  The following topics provide more information about quorum authentication in AWS CloudHSM.

###### Topics

- [Quorum authentication process for CloudHSM CLI](quorum-auth-chsm-cli-overview.md "quorum-auth-chsm-cli-overview.md")
- [Supported AWS CloudHSM service names and types
  for quorum authentication with CloudHSM CLI](quorum-auth-chsm-cli-service-names.md "quorum-auth-chsm-cli-service-names.md")
- [Set up quorum authentication for AWS CloudHSM
  admins using CloudHSM CLI](quorum-auth-chsm-cli-first-time.md "quorum-auth-chsm-cli-first-time.md")
- [User management with quorum authentication enabled
  for AWS CloudHSM using CloudHSM CLI](quorum-auth-chsm-cli-admin.md "quorum-auth-chsm-cli-admin.md")
- [Change the quorum minimum value for AWS CloudHSM
  using CloudHSM CLI](quorum-auth-chsm-cli-min-value.md "quorum-auth-chsm-cli-min-value.md")
