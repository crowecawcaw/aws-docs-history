# SEC02-BP04 Rely on a centralized identity provider

For workforce identities (employees and contractors), rely on an
identity provider that allows you to manage identities in a
centralized place. This makes it easier to manage access across
multiple applications and systems, because you are creating,
assigning, managing, revoking, and auditing access from a single
location.

**Desired outcome:** You have a
centralized identity provider where you centrally manage workforce
users, authentication policies (such as requiring multi-factor
authentication (MFA)), and authorization to systems and applications
(such as assigning access based on a user's group membership or
attributes). Your workforce users sign in to the central identity
provider and federate (single sign-on) to internal and external
applications, removing the need for users to remember multiple
credentials. Your identity provider is integrated with your human
resources (HR) systems so that personnel changes are automatically
synchronized to your identity provider. For example, if someone
leaves your organization, you can automatically revoke access to
federated applications and systems (including AWS). You have enabled
detailed audit logging in your identity provider and are monitoring
these logs for unusual user behavior.

**Common anti-patterns:**

- You do not use federation and single-sign on. Your workforce
  users create separate user accounts and credentials in multiple
  applications and systems.
- You have not automated the lifecycle of identities for workforce
  users, such as by integrating your identity provider with your
  HR systems. When a user leaves your organization or changes
  roles, you follow a manual process to delete or update their
  records in multiple applications and systems.

**Benefits of establishing this best
practice:** By using a centralized identity provider, you
have a single place to manage workforce user identities and
policies, the ability to assign access to applications to users and
groups, and the ability to monitor user sign-in activity. By
integrating with your human resources (HR) systems, when a user
changes roles, these changes are synchronized to the identity
provider and automatically updates their assigned applications and
permissions. When a user leaves your organization, their identity is
automatically disabled in the identity provider, revoking their
access to federated applications and systems.

**Level of risk exposed if this best practice
is not established**: High

## Implementation guidance

**Guidance for workforce users accessing
AWS** Workforce users like employees and contractors in
your organization may require access to AWS using the AWS Management Console or AWS Command Line Interface (AWS CLI) to
perform their job functions. You can grant AWS access to your
workforce users by federating from your centralized identity
provider to AWS at two levels: direct federation to each AWS account or federating to multiple accounts in your
[AWS organization](../../../organizations/latest/userguide/orgs_getting-started_concepts.md "../../../organizations/latest/userguide/orgs_getting-started_concepts.md").

To federate your workforce users directly with each AWS account,
you can use a centralized identity provider to federate to
[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") in that account. The flexibility of IAM
allows you to enable a separate
[SAML
2.0](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md") or an
[Open
ID Connect (OIDC)](../../../IAM/latest/UserGuide/id_roles_providers_create_oidc.md "../../../IAM/latest/UserGuide/id_roles_providers_create_oidc.md") Identity Provider for each AWS account
and use federated user attributes for access control. Your
workforce users will use their web browser to sign in to the
identity provider by providing their credentials (such as
passwords and MFA token codes). The identity provider issues a
SAML assertion to their browser that is submitted to the AWS Management Console sign in URL to allow the user to single sign-on
to the
[AWS Management Console by assuming an IAM Role](../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md "../../../IAM/latest/UserGuide/id_roles_providers_enable-console-saml.md"). Your users can
also obtain temporary AWS API credentials for use in the
[AWS CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") or
[AWS SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") from
[AWS STS](../../../STS/latest/APIReference/welcome.md "../../../STS/latest/APIReference/welcome.md") by
[assuming
the IAM role using a SAML assertion](../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md "../../../STS/latest/APIReference/API_AssumeRoleWithSAML.md") from the identity
provider.

To federate your workforce users with multiple accounts in your
AWS organization, you can use
[_AWS IAM Identity Center_](https://aws.amazon.com/single-sign-on/ "https://aws.amazon.com/single-sign-on/") to centrally manage access
for your workforce users to AWS accounts and applications. You
enable Identity Center for your organization and configure your
identity source. IAM Identity Center provides a default identity
source directory which you can use to manage your users and
groups. Alternatively, you can choose an external identity source
by
[_connecting
to your external identity provider_](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") using SAML
2.0 and
[automatically
provisioning](../../../singlesignon/latest/userguide/provision-automatically.md "../../../singlesignon/latest/userguide/provision-automatically.md") users and groups using SCIM, or
[_connecting
to your Microsoft AD Directory_](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md") using
[AWS Directory Service](https://aws.amazon.com/directoryservice/ "https://aws.amazon.com/directoryservice/"). Once an identity source is configured,
you can assign access to users and groups to AWS accounts by
defining least-privilege policies in your
[permission
sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md"). Your workforce users can authenticate through your
central identity provider to sign in to the
[AWS access portal](../../../singlesignon/latest/userguide/using-the-portal.md "../../../singlesignon/latest/userguide/using-the-portal.md") and single-sign on to the AWS accounts and
cloud applications assigned to them. Your users can configure the
[AWS CLI v2](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") to authenticate with Identity Center and get
credentials to run AWS CLI commands. Identity Center also allows
single-sign on access to AWS applications such as
[Amazon SageMaker AI Studio](../../../sagemaker/latest/dg/onboard-sso-users.md "../../../sagemaker/latest/dg/onboard-sso-users.md") and
[AWS IoT Sitewise Monitor portals](../../../iot-sitewise/latest/userguide/monitor-getting-started.md "../../../iot-sitewise/latest/userguide/monitor-getting-started.md").

After you follow the preceding guidance, your workforce users will
no longer need to use IAM users and groups for normal operations
when managing workloads on AWS. Instead, your users and groups are
managed outside of AWS and users are able to access AWS resources
as a _federated identity_. Federated identities
use the groups defined by your centralized identity provider. You
should identify and remove IAM groups, IAM users, and long-lived
user credentials (passwords and access keys) that are no longer
needed in your AWS accounts. You can
[find
unused credentials](../../../IAM/latest/UserGuide/id_credentials_finding-unused.md "../../../IAM/latest/UserGuide/id_credentials_finding-unused.md") using
[IAM
credential reports](../../../IAM/latest/UserGuide/id_credentials_getting-report.md "../../../IAM/latest/UserGuide/id_credentials_getting-report.md"),
[delete
the corresponding IAM users](../../../IAM/latest/UserGuide/id_users_manage.md "../../../IAM/latest/UserGuide/id_users_manage.md") and
[delete
IAM groups.](../../../IAM/latest/UserGuide/id_groups_manage_delete.md "../../../IAM/latest/UserGuide/id_groups_manage_delete.md") You can apply a
[Service
Control Policy (SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") to your organization that helps
prevent the creation of new IAM users and groups, enforcing that
access to AWS is via federated identities.

###### Note

You are responsible for handling the rotation of SCIM
access tokens as described in the
[Automatic
provisioning](../../../singlesignon/latest/userguide/provision-automatically.md "../../../singlesignon/latest/userguide/provision-automatically.md") documentation. Additionally, you are
responsible for rotating the certificates supporting your
identity federation.

**Guidance for users of your
applications** You can manage the identities of users of
your applications, such as a mobile app, using
[_Amazon Cognito_](https://aws.amazon.com/cognito/ "https://aws.amazon.com/cognito/") as your centralized identity provider.
Amazon Cognito enables authentication, authorization, and user
management for your web and mobile apps. Amazon Cognito provides
an identity store that scales to millions of users, supports
social and enterprise identity federation, and offers advanced
security features to help protect your users and business. You can
integrate your custom web or mobile application with Amazon Cognito to add user authentication and access control to your
applications in minutes. Built on open identity standards such as
SAML and Open ID Connect (OIDC), Amazon Cognito supports various
compliance regulations and integrates with frontend and backend
development resources.

### Implementation steps

**Steps for workforce users accessing
AWS**

- Federate your workforce users to AWS using a centralized
  identity provider using one of the following approaches:
  - Use IAM Identity Center to enable single sign-on to
    multiple AWS accounts in your AWS organization by
    federating with your identity provider.
  - Use IAM to connect your identity provider directly to
    each AWS account, enabling federated fine-grained
    access.

- Identify and remove IAM users and groups that are replaced
  by federated identities.

**Steps for users of your
applications**

- Use Amazon Cognito as a centralized identity provider
  towards your applications.
- Integrate your custom applications with Amazon Cognito using
  OpenID Connect and OAuth. You can develop your custom
  applications using the Amplify libraries that provide simple
  interfaces to integrate with a variety of AWS services, such
  as Amazon Cognito for authentication.

## Resources

**Related best practices:**

- [SEC02-BP06 Employ user groups
  and attributes](../security-pillar/sec_identities_groups_attributes.md "../security-pillar/sec_identities_groups_attributes.md")
- [SEC03-BP02 Grant
  least privilege access](../security-pillar/sec_permissions_least_privileges.md "../security-pillar/sec_permissions_least_privileges.md")
- [SEC03-BP06 Manage
  access based on lifecycle](../security-pillar/sec_permissions_lifecycle.md "../security-pillar/sec_permissions_lifecycle.md")

**Related documents:**

- [Identity
  federation in AWS](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/")
- [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [AWS Identity and Access Management Best practices](https://aws.amazon.com/iam/resources/best-practices/ "https://aws.amazon.com/iam/resources/best-practices/")
- [Getting
  started with IAM Identity Center delegated
  administration](https://aws.amazon.com/blogs/security/getting-started-with-aws-sso-delegated-administration/ "https://aws.amazon.com/blogs/security/getting-started-with-aws-sso-delegated-administration/")
- [How
  to use customer managed policies in IAM Identity Center for
  advanced use cases](https://aws.amazon.com/blogs/security/how-to-use-customer-managed-policies-in-aws-single-sign-on-for-advanced-use-cases/ "https://aws.amazon.com/blogs/security/how-to-use-customer-managed-policies-in-aws-single-sign-on-for-advanced-use-cases/")
- [AWS CLI v2: IAM Identity Center credential provider](../../../sdkref/latest/guide/feature-sso-credentials.md "../../../sdkref/latest/guide/feature-sso-credentials.md")

**Related videos:**

- [AWS re:Inforce
  2022 - AWS Identity and Access Management (IAM) deep
  dive](https://youtu.be/YMj33ToS8cI "https://youtu.be/YMj33ToS8cI")
- [AWS re:Invent
  2022 - Simplify your existing workforce access with IAM Identity Center](https://youtu.be/TvQN4OdR_0Y "https://youtu.be/TvQN4OdR_0Y")
- [AWS re:Invent
  2018: Mastering Identity at Every Layer of the Cake](https://youtu.be/vbjFjMNVEpc "https://youtu.be/vbjFjMNVEpc")

**Related examples:**

- [Workshop:
  Using AWS IAM Identity Center to achieve strong identity
  management](https://catalog.us-east-1.prod.workshops.aws/workshops/590f8439-42c7-46a1-8e70-28ee41498b3a/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/590f8439-42c7-46a1-8e70-28ee41498b3a/en-US")

**Related tools:**

- [AWS Security Competency Partners: Identity and Access
  Management](https://aws.amazon.com/security/partner-solutions/ "https://aws.amazon.com/security/partner-solutions/")
- [saml2aws](https://github.com/Versent/saml2aws "https://github.com/Versent/saml2aws")
