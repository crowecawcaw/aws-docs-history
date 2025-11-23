# Identity and Access Management for AWS Clean Rooms

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use AWS Clean Rooms resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security-iam-audience "#security-iam-audience")
- [Authenticating with identities](#security-iam-auth-with-identities "#security-iam-auth-with-identities")
- [Managing access using policies](#security-iam-managing-access "#security-iam-managing-access")
- [How AWS Clean Rooms works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Identity-based policy examples for
  AWS Clean Rooms](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Troubleshooting AWS Clean Rooms identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")
- [Cross-service confused deputy
  prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [IAM behaviors for AWS Clean Rooms ML](ml-behaviors.md "ml-behaviors.md")
- [IAM behaviors for Clean Rooms ML Custom Models](ml-behaviors-byom.md "ml-behaviors-byom.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting AWS Clean Rooms identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How AWS Clean Rooms works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policy examples for
  AWS Clean Rooms](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be _authenticated_ (signed in to AWS) as the AWS account root user, as an IAM user, or by assuming
an IAM role.

You can sign in to AWS as a federated identity by using credentials provided through an
identity source. AWS IAM Identity Center (IAM Identity Center) users or your company's single sign-on authentication are examples of
federated identities. When you sign in as a federated identity, your administrator previously set up identity
federation using IAM roles. When you access AWS by using federation, you are indirectly assuming a
role.

Depending on the type of user you are, you can sign in to the AWS Management Console or the AWS access
portal. For more information about signing in to AWS, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the
_AWS Sign-In User Guide_.

If you access AWS programmatically, AWS provides a software development kit (SDK) and a command line
interface (CLI) to cryptographically sign your requests using your credentials. If you don't use AWS tools,
you must sign requests yourself. For more information about using the recommended method to sign requests
yourself, see [Signature Version 4
signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.

Regardless of the authentication method that you use, you might be required to provide
additional security information. For example, AWS recommends that you use multi-factor authentication (MFA) to
increase the security of your account. To learn more, see [Multi-factor authentication](../../../singlesignon/latest/userguide/enable-mfa.md "../../../singlesignon/latest/userguide/enable-mfa.md") in the
_AWS IAM Identity Center User Guide_ and [Using multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in
the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity that has complete access to all
AWS services and resources in the account. This identity is called the AWS account
_root user_ and is accessed by signing in with the email address and password that you used to
create the account. We strongly recommend that you do not use the root user for your everyday tasks. Safeguard your
root user credentials and use them to perform the tasks that only the root user can perform. For the complete list of
tasks that require you to sign in as the root user, see [AWS account root user credentials and IAM
identities](../../../general/latest/gr/root-vs-iam.md#aws_tasks-that-require-root "../../../general/latest/gr/root-vs-iam.md#aws_tasks-that-require-root") in the _AWS General Reference_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities
or resources. A policy is an object in AWS that, when associated with an identity or
resource, defines their permissions. AWS evaluates these policies when a principal (user,
root user, or role session) makes a request. Permissions in the policies determine whether the
request is allowed or denied. Most policies are stored in AWS as JSON documents. For more
information about the structure and contents of JSON policy documents, see [Overview of JSON
policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

Every IAM entity (user or role) starts with no permissions. By default, users can do
nothing, not even change their own password. To give a user permission to do something, an
administrator must attach a permissions policy to a user. Or the administrator can add the
user to a group that has the intended permissions. When an administrator gives permissions
to a group, all users in that group are granted those permissions.

IAM policies define permissions for an action regardless of the method that you use to
perform the operation. For example, suppose that you have a policy that allows the
`iam:GetRole` action. A user with that policy can get role information from
the AWS Management Console, the AWS CLI, or the AWS API.

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

Identity-based policies can be further categorized as _inline
policies_ or _managed policies_. Inline
policies are embedded directly into a single user, group, or role. Managed policies are
standalone policies that you can attach to multiple users, groups, and roles in your
AWS account. Managed policies include AWS managed policies and customer managed
policies. To learn how to choose between a managed policy or an inline policy, see
[Choosing between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#choosing-managed-or-inline "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#choosing-managed-or-inline") in the
_IAM User Guide_.

### Resource-based policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service
administrators can use them to control access to a specific resource. For the resource where the policy is attached, the policy defines what actions
a specified principal can perform on that resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals
can include accounts, users, roles, federated users, or AWS services.

Resource-based policies are inline policies that are located in that service. You
can't use AWS managed policies from IAM in a resource-based policy.

### Other policy types

AWS supports additional, less-common policy types. These policy types can set the
maximum permissions granted to you by the more common policy types.

- **Permissions boundaries** – A permissions
  boundary is an advanced feature in which you set the maximum permissions that an
  identity-based policy can grant to an IAM entity (IAM user or role). You can
  set a permissions boundary for an entity. The resulting permissions are the
  intersection of entity's identity-based policies and its permissions
  boundaries. Resource-based policies that specify the user or role in the
  `Principal` field are not limited by the permissions boundary. An
  explicit deny in any of these policies overrides the allow. For more information
  about permissions boundaries, see [Permissions boundaries for
  IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – SCPs
  are JSON policies that specify the maximum permissions for an organization or
  organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and
  centrally managing multiple AWS accounts that your business owns. If you enable
  all features in an organization, then you can apply service control policies
  (SCPs) to any or all of your accounts. The SCP limits permissions for entities in
  member accounts, including each AWS account root user. For more information about Organizations and
  SCPs, see [How SCPs
  work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Session policies are
  advanced policies that you pass as a parameter when you programmatically create a
  temporary session for a role or federated user. The resulting session's
  permissions are the intersection of the user or role's identity-based
  policies and the session policies. Permissions can also come from a resource-based
  policy. An explicit deny in any of these policies overrides the allow. For more
  information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy types

When multiple types of policies apply to a request, the resulting permissions are
more complicated to understand. To learn how AWS determines whether to allow a request
when multiple policy types are involved, see [Policy evaluation
logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.
