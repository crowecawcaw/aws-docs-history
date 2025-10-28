# Permissions management

Manage permissions to control access to human and machine identities that require
access to AWS and your workloads. Permissions allow you to control who can access what, and under
what conditions. By setting permissions to specific human and machine identities, you grant them access
to specific service actions on specific resources. Additionally, you can specify conditions that
must be true for access to be granted.

There are a number of ways to grant access to different types of resources. One way is
by using different policy types.

[Identity-based policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in IAM are _managed_ or
_inline_, and attach to IAM identities, including users,
groups, or roles. These policies let you specify what that identity can do (its permissions).
Identity-based policies can be further categorized.

**Managed policies** – Standalone identity-based policies
that you can attach to multiple users, groups, and roles in your AWS account. There are two
types of managed policies:

- **AWS-managed policies** – Managed policies that are
  created and managed by AWS.
- **Customer-managed policies** – Managed policies that you
  create and manage in your AWS account. Customer-managed policies provide more precise
  control over your policies than AWS-managed policies.
  Managed polices are the preferred method for applying permissions. However, you also can
  use inline policies that you add directly to a single user, group, or role. Inline policies
  maintain a strict one-to-one relationship between a policy and an identity. Inline policies
  are deleted when you delete the identity.

In most cases, you should create your own customer-managed policies following the
principle of [least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege").

[Resource-based policies](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") are attached to a resource. For example, an S3 bucket
policy is a resource-based policy. These policies grant permission to a principal that can
be in the same account as the resource or in another account. For a list of services that
support resource-based policies, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md").

[Permissions boundaries](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/ "https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/") use a managed policy to set the maximum permissions that an
administrator can set. This allows you to delegate the ability to create and manage
permissions to developers, such as the creation of an IAM role, but limit the permissions they
can grant so that they cannot escalate their permission using what they have created.

[Attribute-based
access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in AWS allows you to grant permissions based on attributes, which are called tags. These tags can be attached to IAM principals (users or roles) and to
AWS resources. Administrators can create reusable IAM policies that apply
permissions based on the attributes of the IAM principal. For example, as an administrator
you can use a single IAM policy to grant developers in your organization access to AWS
resources that match their project tags. As the team of developers adds resources
to projects, permissions are automatically applied based on attributes, eliminating the need for
policy updates for each new resource.

[Organizations service control policies (SCP)](../../../IAM/latest/UserGuide/access_policies.md#policies_scp "../../../IAM/latest/UserGuide/access_policies.md#policies_scp") define the maximum permissions for
account members of an organization or organizational unit (OU). SCPs _limit_ permissions that identity-based policies or resource-based policies
grant to entities (users or roles) within the account, but _do
not grant_ permissions.

[Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") assume a role or a federated user. Pass session policies when
using the AWS CLI or AWS API Session policies to limit the permissions that the role or
user's identity-based policies grant to the session. These policies _limit_ permissions for a created session, but _do not
grant_ permissions. For more information, see [Session Policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session").

###### Best practices

- [SEC03-BP01 Define access requirements](sec_permissions_define.md "sec_permissions_define.md")
- [SEC03-BP02 Grant least privilege access](sec_permissions_least_privileges.md "sec_permissions_least_privileges.md")
- [SEC03-BP03 Establish emergency access
  process](sec_permissions_emergency_process.md "sec_permissions_emergency_process.md")
- [SEC03-BP04 Reduce permissions continuously](sec_permissions_continuous_reduction.md "sec_permissions_continuous_reduction.md")
- [SEC03-BP05 Define permission guardrails for
  your organization](sec_permissions_define_guardrails.md "sec_permissions_define_guardrails.md")
- [SEC03-BP06 Manage access based on lifecycle](sec_permissions_lifecycle.md "sec_permissions_lifecycle.md")
- [SEC03-BP07 Analyze public and cross-account access](sec_permissions_analyze_cross_account.md "sec_permissions_analyze_cross_account.md")
- [SEC03-BP08 Share resources securely within your organization](sec_permissions_share_securely.md "sec_permissions_share_securely.md")
- [SEC03-BP09 Share resources securely with a third party](sec_permissions_share_securely_third_party.md "sec_permissions_share_securely_third_party.md")
