# SEC02-BP01 Use strong sign-in mechanisms

Sign-ins (authentication using sign-in credentials) can present
risks when not using mechanisms like multi-factor authentication
(MFA), especially in situations where sign-in credentials have been
inadvertently disclosed or are easily guessed. Use strong sign-in
mechanisms to reduce these risks by requiring MFA and strong
password policies.

**Desired outcome:** Reduce the risks
of unintended access to credentials in AWS by using strong sign-in
mechanisms for [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") users, the
[AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md"),
[AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"), and
third-party identity providers. This means requiring MFA, enforcing
strong password policies, and detecting anomalous login behavior.

**Common anti-patterns:**

- Not enforcing a strong password policy for your identities
  including complex passwords and MFA.
- Sharing the same credentials among different users.
- Not using detective controls for suspicious sign-ins.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

There are several ways for human identities to sign in to AWS. It
is an AWS best practice to rely on a centralized identity provider
using federation (direct SAML 2.0 federation between AWS IAM and
the centralized IdP or using AWS IAM Identity Center) when
authenticating to AWS. In this case, establish a secure sign-in
process with your identity provider or Microsoft Active Directory.

When you first open an AWS account, you begin with an AWS account
root user. You should only use the account root user to set up
access for your users (and for
[tasks
that require the root user](../../../accounts/latest/reference/root-user-tasks.md "../../../accounts/latest/reference/root-user-tasks.md")). It's important to turn on
multi-factor authentication (MFA) for the account root user
immediately after opening your AWS account and to secure the root
user using the
[AWS best practice guide](sec_securely_operate_aws_account.md "sec_securely_operate_aws_account.md").

AWS IAM Identity Center is designed for workforce users, and you
can create and manage user identities within the service and
secure the sign-in process with MFA. AWS Cognito, on the other
hand, is designed for customer identity and access management
(CIAM), which provides user pools and identity providers for
external user identities in your applications.

If you create users in AWS IAM Identity Center, secure the sign-in
process in that service and
[turn
on MFA](../../../singlesignon/latest/userguide/enable-mfa.md "../../../singlesignon/latest/userguide/enable-mfa.md"). For external user identities in your applications,
you can use
[Amazon Cognito user pools](../../../cognito/index.md "../../../cognito/index.md") and secure the sign-in process in that
service or through one of the supported identity providers in
Amazon Cognito user pools.

Additionally, for users in AWS IAM Identity Center, you can use
[AWS Verified Access](../../../verified-access/latest/ug/what-is-verified-access.md "../../../verified-access/latest/ug/what-is-verified-access.md") to provide an additional layer of security
by verifying the user's identity and device posture before they
are granted access to AWS resources.

If you are using
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") users, secure the sign-in process
using IAM.

You can use both AWS IAM Identity Center and direct IAM federation
simultaneously to manage access to AWS. You can use IAM federation
to manage access to the AWS Management Console and services and IAM Identity Center to manage access to business applications like Quick Suite or Amazon Q Business.

Regardless of the sign-in method, it's critical to enforce a
strong sign-in policy.

### Implementation steps

The following are general strong sign-in recommendations. The
actual settings you configure should be set by your company
policy or use a standard like
[NIST
800-63](https://pages.nist.gov/800-63-3/sp800-63b.html "https://pages.nist.gov/800-63-3/sp800-63b.html").

- Require MFA. It's an
  [IAM
  best practice to require MFA](../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users "../../../IAM/latest/UserGuide/best-practices.md#enable-mfa-for-privileged-users") for human identities and
  workloads. Turning on MFA provides an additional layer of
  security requiring that users provide sign-in credentials
  and a one-time password (OTP) or a cryptographically
  verified and generated string from a hardware device.
- Enforce a minimum password length, which is a primary factor
  in password strength.
- Enforce password complexity to make passwords more difficult
  to guess.
- Allow users to change their own passwords.
- Create individual identities instead of shared credentials.
  By creating individual identities, you can give each user a
  unique set of security credentials. Individual users provide
  the ability to audit each user's activity.

IAM Identity Center recommendations:

- IAM Identity Center provides a predefined
  [password
  policy](../../../singlesignon/latest/userguide/password-requirements.md "../../../singlesignon/latest/userguide/password-requirements.md") when using the default directory that
  establishes password length, complexity, and reuse
  requirements.
- [Turn
  on MFA](../../../singlesignon/latest/userguide/mfa-enable-how-to.md "../../../singlesignon/latest/userguide/mfa-enable-how-to.md") and configure the context-aware or always-on
  setting for MFA when the identity source is the default
  directory, AWS Managed Microsoft AD, or AD Connector.
- Allow users to
  [register
  their own MFA devices](../../../singlesignon/latest/userguide/how-to-allow-user-registration.md "../../../singlesignon/latest/userguide/how-to-allow-user-registration.md").

Amazon Cognito user pools directory recommendations:

- Configure the
  [Password
  strength](../../../cognito/latest/developerguide/user-pool-settings-policies.md "../../../cognito/latest/developerguide/user-pool-settings-policies.md") settings.
- [Require
  MFA](../../../cognito/latest/developerguide/user-pool-settings-mfa.md "../../../cognito/latest/developerguide/user-pool-settings-mfa.md") for users.
- Use the Amazon Cognito user pools
  [advanced
  security settings](../../../cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.md "../../../cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.md") for features like
  [adaptive
  authentication](../../../cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.md "../../../cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.md") which can block suspicious sign-ins.

IAM user recommendations:

- Ideally you are using IAM Identity Center or direct
  federation. However, you might have the need for IAM users.
  In that case,
  [set
  a password policy](../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md "../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md") for IAM users. You can use the
  password policy to define requirements such as minimum
  length or whether the password requires non-alphabetic
  characters.
- Create an IAM policy to
  [enforce
  MFA sign-in](../../../IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.md#tutorial_mfa_step1 "../../../IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.md#tutorial_mfa_step1") so that users are allowed to manage their
  own passwords and MFA devices.

## Resources

**Related best practices:**

- [SEC02-BP03 Store and use
  secrets securely](../security-pillar/sec_identities_secrets.md "../security-pillar/sec_identities_secrets.md")
- [SEC02-BP04 Rely on a
  centralized identity provider](../security-pillar/sec_identities_identity_provider.md "../security-pillar/sec_identities_identity_provider.md")
- [SEC03-BP08 Share
  resources securely within your organization](../security-pillar/sec_permissions_share_securely.md "../security-pillar/sec_permissions_share_securely.md")

**Related documents:**

- [AWS IAM Identity Center Password Policy](../../../singlesignon/latest/userguide/password-requirements.md "../../../singlesignon/latest/userguide/password-requirements.md")
- [IAM user password policy](../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md "../../../IAM/latest/UserGuide/id_credentials_passwords_account-policy.md")
- [Setting
  the AWS account root user password](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md")
- [Amazon Cognito password policy](../../../cognito/latest/developerguide/user-pool-settings-policies.md "../../../cognito/latest/developerguide/user-pool-settings-policies.md")
- [AWS credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md")
- [IAM
  security best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")

**Related videos:**

- [Managing user
  permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E "https://youtu.be/aEIqeFCcK7E")
- [Mastering
  identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc "https://www.youtube.com/watch?v=vbjFjMNVEpc")
