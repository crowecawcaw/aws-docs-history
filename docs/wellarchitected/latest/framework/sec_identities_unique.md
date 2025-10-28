# SEC02-BP02 Use temporary credentials

When doing any type of authentication, it's best to use temporary
credentials instead of long-term credentials to reduce or eliminate
risks, such as credentials being inadvertently disclosed, shared, or
stolen.

**Desired outcome:** To reduce the
risk of long-term credentials, use temporary credentials wherever
possible for both human and machine identities. Long-term
credentials create many risks, such as exposure through uploads to
public repositories. By using temporary credentials, you
significantly reduce the chances of credentials becoming
compromised.

**Common anti-patterns:**

- Developers using long-term access keys from IAM users rather
  than obtaining temporary credentials from the CLI using
  federation.
- Developers embedding long-term access keys in their code and
  uploading that code to public Git repositories.
- Developers embedding long-term access keys in mobile apps that
  are then made available in app stores.
- Users sharing long-term access keys with other users, or
  employees leaving the company with long-term access keys still
  in their possession.
- Using long-term access keys for machine identities when
  temporary credentials could be used.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use temporary security credentials instead of long-term
credentials for all AWS API and CLI requests. API and CLI requests
to AWS services must, in nearly every case, be signed using
[AWS access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md"). These requests can be signed with either
temporary or long-term credentials. The only time you should use
long-term credentials, also known as long-term access keys, is if
you are using an
[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") or the
[AWS account root user](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md"). When you federate to AWS or assume an
[IAM
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") through other methods, temporary credentials are
generated. Even when you access the AWS Management Console using
sign-in credentials, temporary credentials are generated for you
to make calls to AWS services. There are few situations where you
need long-term credentials and you can accomplish nearly all tasks
using temporary credentials.

Avoiding the use of long-term credentials in favor of temporary
credentials should go hand in hand with a strategy of reducing the
usage of IAM users in favor of federation and IAM roles. While IAM users have been used for both human and machine identities in the
past, we now recommend not using them to avoid the risks in using
long-term access keys.

### Implementation steps

#### Human identities

For workforce identities like employees, administrators,
developers, and operators:

- You should [rely on a
  centralized identity provider](../security-pillar/sec_identities_identity_provider.md "../security-pillar/sec_identities_identity_provider.md") and
  [require
  human users to use federation with an identity provider to
  access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp"). Federation
  for your users can be done either with
  [direct
  federation to each AWS account](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/") or using
  [AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") and the identity provider of
  your choice. Federation provides a number of advantages
  over using IAM users in addition to eliminating long-term
  credentials. Your users can also request temporary
  credentials from the command line for
  [direct
  federation](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/ "https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/") or by using
  [IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md"). This means that there are few uses
  cases that require IAM users or long-term credentials for
  your users.

For third-party identities:

- When granting third parties,
  such as software as a service (SaaS) providers, access to
  resources in your AWS account, you can use
  [cross-account
  roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") and
  [resource-based
  policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md"). Additionally, you can use the
  [Amazon Cognito OAuth 2.0 grant](../../../cognito/latest/developerguide/federation-endpoints-oauth-grants.md "../../../cognito/latest/developerguide/federation-endpoints-oauth-grants.md") client credentials flow for B2B
  SaaS customers or partners.

User identities that access your AWS resources through web
browsers, client applications, mobile apps, or interactive
command-line tools:

- If you need to grant applications for
  consumers or customers access to your AWS resources, you can
  use
  [Amazon Cognito identity pools](../../../cognito/latest/developerguide/identity-pools.md "../../../cognito/latest/developerguide/identity-pools.md") or
  [Amazon Cognito user pools](../../../cognito/latest/developerguide/cognito-user-identity-pools.md "../../../cognito/latest/developerguide/cognito-user-identity-pools.md") to provide temporary credentials.
  The permissions for the credentials are configured through IAM
  roles. You can also define a separate IAM role with limited
  permissions for guest users who are not authenticated.

#### Machine identities

For machine identities, you might need to use long-term
credentials. In these cases, you should
[require
workloads to use temporary credentials with IAM roles to
access AWS](../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles "../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles").

- For
  [Amazon Elastic Compute Cloud](https://aws.amazon.com/pm/ec2/ "https://aws.amazon.com/pm/ec2/") (Amazon EC2), you can use
  [roles
  for Amazon EC2](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md").
- [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") allows you to configure a
  [Lambda
  execution role to grant the service permissions](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") to
  perform AWS actions using temporary credentials. There are
  many other similar models for AWS services to grant
  temporary credentials using IAM roles.
- For IoT devices, you can use the
  [AWS IoT Core credential provider](../../../iot/latest/developerguide/authorizing-direct-aws.md "../../../iot/latest/developerguide/authorizing-direct-aws.md") to request temporary
  credentials.
- For on-premises systems or systems that run outside of AWS
  that need access to AWS resources, you can use
  [IAM
  Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").

There are scenarios where temporary credentials are not
supported, which require the use of long-term credentials. In
these situations, [audit and
rotate these credentials periodically](../security-pillar/sec_identities_audit.md "../security-pillar/sec_identities_audit.md") and
[rotate
access keys regularly](../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials "../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials"). For highly restricted IAM user
access keys, consider the following additional security
measures:

- Grant highly restricted permissions:
  - Adhere to the principle of least privilege (be
    specific about actions, resources, and conditions).
  - Consider granting the IAM user only the
    AssumeRole operation for one
    specific role. Depending on the on-premise
    architecture, this approach helps isolate and secure
    the long-term IAM credentials.

- Limit the allowed network sources and IP addresses in the
  IAM role trust policy.
- Monitor usage and set up alerts for unused permissions or
  misuse (using AWS CloudWatch Logs metric filters and
  alarms).
- Enforce
  [permission
  boundaries](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") (service control policies (SCPs) and
  permission boundaries complement each other - SCPs are
  coarse-grained, while permission boundaries are
  fine-grained).
- Implement a process to provision and securely store (in an
  on-premise vault) the credentials.

Some other options for scenarios requiring long-term
credentials include:

- Build your own token vending API (using Amazon API Gateway).
- For scenarios where you must use long-term credentials or
  credentials other than AWS access keys (such as database
  logins), you can use a service designed to handle the
  management of secrets, such as
  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/"). Secrets Manager simplifies the
  management, rotation, and secure storage of encrypted
  secrets. Many AWS services support a
  [direct
  integration](../../../secretsmanager/latest/userguide/integrating.md "../../../secretsmanager/latest/userguide/integrating.md") with Secrets Manager.
- For multi-cloud integrations, you can use identity
  federation based on your source credential service
  provider (CSP) credentials (see
  [AWS STS AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md")).

For more information about rotating long-term credentials, see
[rotating
access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey").

## Resources

**Related best practices:**

- [SEC02-BP03 Store and use
  secrets securely](../security-pillar/sec_identities_secrets.md "../security-pillar/sec_identities_secrets.md")
- [SEC02-BP04 Rely on a
  centralized identity provider](../security-pillar/sec_identities_identity_provider.md "../security-pillar/sec_identities_identity_provider.md")
- [SEC03-BP08 Share
  resources securely within your organization](../security-pillar/sec_permissions_share_securely.md "../security-pillar/sec_permissions_share_securely.md")

**Related documents:**

- [Temporary
  Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md")
- [AWS Credentials](../../../general/latest/gr/aws-sec-cred-types.md "../../../general/latest/gr/aws-sec-cred-types.md")
- [IAM
  Security Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [IAM
  Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
- [IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/")
- [Identity
  Providers and Federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md")
- [Rotating
  Access Keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#Using_RotateAccessKey")
- [Security
  Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control "https://aws.amazon.com/security/partner-solutions/#access-control")
- [The
  AWS Account Root User](../../../IAM/latest/UserGuide/id_root-user.md "../../../IAM/latest/UserGuide/id_root-user.md")
- [Access
  AWS using a Google Cloud Platform native workload
  identity](https://aws.amazon.com/blogs/security/access-aws-using-a-google-cloud-platform-native-workload-identity/ "https://aws.amazon.com/blogs/security/access-aws-using-a-google-cloud-platform-native-workload-identity/")
- [How
  to access AWS resources from Microsoft Entra ID tenants using
  AWS Security Token Service](https://aws.amazon.com/blogs/security/how-to-access-aws-resources-from-microsoft-entra-id-tenants-using-aws-security-token-service/ "https://aws.amazon.com/blogs/security/how-to-access-aws-resources-from-microsoft-entra-id-tenants-using-aws-security-token-service/")

**Related videos:**

- [Managing user
  permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E "https://youtu.be/aEIqeFCcK7E")
- [Mastering
  identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc "https://www.youtube.com/watch?v=vbjFjMNVEpc")
