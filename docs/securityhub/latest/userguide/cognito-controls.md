# Security Hub CSPM controls for Amazon Cognito

These AWS Security Hub CSPM controls evaluate the Amazon Cognito service and resources. The controls might not
be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [Cognito.1] Cognito user pools should have threat protection

activated with full function enforcement mode for standard authentication

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::Cognito::UserPool`

**AWS Config rule:**
[cognito-user-pool-advanced-security-enabled](../../../config/latest/developerguide/cognito-user-pool-advanced-security-enabled.md "../../../config/latest/developerguide/cognito-user-pool-advanced-security-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter      | Description                                                            | Type   | Allowed custom values | Security Hub CSPM default value |
| -------------- | ---------------------------------------------------------------------- | ------ | --------------------- | ------------------------------- |
| `SecurityMode` | The threat protection enforcement mode that the control checks<br>for. | String | `AUDIT`, `ENFORCED`   | `ENFORCED`                      |

This control checks whether an Amazon Cognito user pool has threat protection activated with
the enforcement mode set to full function for standard authentication. The control fails
if the user pool has threat protection deactivated or if the enforcement mode isn't set
to full function for standard authentication. Unless you provide custom parameter
values, Security Hub CSPM uses the default value of `ENFORCED` for enforcement mode set
to full function for standard authentication.

After you create an Amazon Cognito user pool, you can activate threat protection and customize
the actions that are taken in response to different risks. Or, you can use audit mode to
gather metrics on detected risks without applying any security mitigations. In audit
mode, threat protection publishes metrics to Amazon CloudWatch. You can see metrics after Amazon Cognito
generates its first event.

### Remediation

For information about activating threat protection for an Amazon Cognito user pool, see
[Advanced security with threat protection](../../../cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.md "../../../cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.md") in the _Amazon Cognito
Developer Guide_.

## [Cognito.2] Cognito identity pools should not allow

unauthenticated identities

**Category:** Protect > Secure access management >
Passwordless authentication

**Severity:** Medium

**Resource type:**
`AWS::Cognito::IdentityPool`

**AWS Config rule:**
[cognito-identity-pool-unauth-access-check](../../../config/latest/developerguide/cognito-identity-pool-unauth-access-check.md "../../../config/latest/developerguide/cognito-identity-pool-unauth-access-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Cognito identity pool is configured to allow
unauthenticated identities. The control fails if guest access is activated (the
`AllowUnauthenticatedIdentities` parameter is set to `true`)
for the identity pool.

If an Amazon Cognito identity pool allows unauthenticated identities, the identity pool
provides temporary AWS credentials to users who haven't authenticated through an
identity provider (guests). This creates security risks because it allows anonymous
access to AWS resources. If you deactivate guest access, you can help ensure that only
properly authenticated users can access your AWS resources, which reduces the risk of
unauthorized access and potential security breaches. As a best practice, an identity
pool should require authentication through supported identity providers. If
unauthenticated access is necessary, it's important to carefully restrict permissions
for unauthenticated identities, and regularly review and monitor their usage.

### Remediation

For information about deactivating guest access for an Amazon Cognito identity pool, see
[Activate or deactivate guest access](../../../cognito/latest/developerguide/identity-pools.md#enable-or-disable-unauthenticated-identities "../../../cognito/latest/developerguide/identity-pools.md#enable-or-disable-unauthenticated-identities") in the _Amazon Cognito Developer
Guide_.

## [Cognito.3] Password policies for Cognito user pools should

have strong configurations

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::Cognito::UserPool`

**AWS Config rule:**
[cognito-user-pool-password-policy-check](../../../config/latest/developerguide/cognito-user-pool-password-policy-check.md "../../../config/latest/developerguide/cognito-user-pool-password-policy-check.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter                   | Description                                                             | Type    | Allowed custom values | Security Hub CSPM default value |
| --------------------------- | ----------------------------------------------------------------------- | ------- | --------------------- | ------------------------------- |
| `minLength`                 | The minimum number of characters that a password must contain.          | Integer | `8` to `128`          | `8`                             |
| `requireLowercase`          | Require at least one lowercase character in a password.                 | Boolean | `True`, `False`       | `True`                          |
| `requireUppercase`          | Require at least one uppercase character in a password.                 | Boolean | `True`, `False`       | `True`                          |
| `requireNumbers`            | Require at least one number in a password.                              | Boolean | `True`, `False`       | `True`                          |
| `requireSymbols`            | Require at least one symbol in a password.                              | Boolean | `True`, `False`       | `True`                          |
| `temporaryPasswordValidity` | The maximum number of days that a password can exist before it expires. | Integer | `7` to `365`          | `7`                             |

This control checks whether the password policy for an Amazon Cognito user pool requires
the use of strong passwords, based on recommended settings for password policies. The
control fails if the password policy for the user pool doesn't require strong passwords.
You can optionally specify custom values for the policy settings that the control
checks.

Strong passwords are a security best practice for Amazon Cognito user pools. Weak
passwords can expose users' credentials to systems that guess passwords and try to
access data. This is especially the case for applications that are open to the internet.
Password policies are a central element of the security of user directories. By using a
password policy, you can configure a user pool to require password complexity and other
settings that comply with your security standards and requirements.

### Remediation

For information about creating or updating the password policy for an Amazon Cognito
user pool, see [Adding user pool password requirements](../../../cognito/latest/developerguide/managing-users-passwords.md#user-pool-settings-policies "../../../cognito/latest/developerguide/managing-users-passwords.md#user-pool-settings-policies") in the _Amazon Cognito Developer Guide_.

## [Cognito.4] Cognito user pools should have threat protection activated with full function enforcement mode for custom authentication

**Category:** Protect > Secure access management

**Severity:** Medium

**Resource type:**
`AWS::Cognito::UserPool`

**AWS Config rule:**
[cognito-userpool-cust-auth-threat-full-check](../../../config/latest/developerguide/cognito-userpool-cust-auth-threat-full-check.md "../../../config/latest/developerguide/cognito-userpool-cust-auth-threat-full-check.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Cognito user pool has threat protection activated with the enforcement mode set to full function for custom authentication.
The control fails if the user pool has threat protection disabled or if the enforcement mode isn't set to full function for custom authentication.

Threat protection, formerly called advanced security features, is a set of monitoring tools for unwanted activity in your user pool, and configuration tools to automatically shut down potentially malicious activity.
After you create an Amazon Cognito user pool, you can activate threat protection with full function enforcement mode for custom authentication and customize the actions that are taken in response to different risks.
Full-function mode includes a set of automatic reactions to detect unwanted activity and compromised passwords.

### Remediation

For information about activating threat protection for an Amazon Cognito
user pool, see [Advanced security with threat protection](../../../cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.md "../../../cognito/latest/developerguide/cognito-user-pool-settings-threat-protection.md") in the _Amazon Cognito Developer Guide_.

## [Cognito.5] MFA should be enabled for Cognito user pools

**Category:** Protect > Secure access management > Multi-factor authentication

**Severity:** Medium

**Resource type:**
`AWS::Cognito::UserPool`

**AWS Config rule:**
[cognito-user-pool-mfa-enabled](../../../config/latest/developerguide/cognito-user-pool-mfa-enabled.md "../../../config/latest/developerguide/cognito-user-pool-mfa-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Cognito user pool configured with a password-only sign-in policy has multi-factor authentication (MFA) enabled.
The control fails if the user pool configured with a password-only sign-in policy does not have MFA enabled.

Multi-factor authentication (MFA) adds a something you have authentication factor to the something you know factor (typically username and password). For federated users, Amazon Cognito delegates authentication to the identity provider (IdP) and doesn't offer additional authentication factors.
However, if you have local users with password authentication, configuring MFA for the user pool increases their security.

###### Note

This control is not applicable for federated users and users signing in with passwordless factors.

### Remediation

For information about how to configure MFA for an Amazon Cognito
user pool, see [Adding MFA to a user pool](../../../cognito/latest/developerguide/user-pool-settings-mfa.md "../../../cognito/latest/developerguide/user-pool-settings-mfa.md") in the _Amazon Cognito Developer Guide_.

## [Cognito.6] Cognito user pools should have deletion protection enabled

**Category:** Protect > Data Protection > Data deletion protection

**Severity:** Medium

**Resource type:**
`AWS::Cognito::UserPool`

**AWS Config rule:**
[cognito-user-pool-deletion-protection-enabled](../../../config/latest/developerguide/cognito-user-pool-deletion-protection-enabled.md "../../../config/latest/developerguide/cognito-user-pool-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Amazon Cognito user pool has deletion protection enabled. The control fails if deletion protection is disabled for the user pool.

Deletion protection helps ensure that your user pool is not accidentally deleted. When you configure a user pool with deletion protection, the pool cannot be deleted by any user. Deletion protection prevents you from requesting the deletion of a user pool unless you first modify the pool and deactivate deletion protection.

### Remediation

To configure deletion protection for an Amazon Cognito
user pool, see [User pool deletion protection](../../../cognito/latest/developerguide/user-pool-settings-deletion-protection.md "../../../cognito/latest/developerguide/user-pool-settings-deletion-protection.md") in the _Amazon Cognito Developer Guide_.
