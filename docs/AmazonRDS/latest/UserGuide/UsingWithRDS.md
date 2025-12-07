# Identity and access management for Amazon RDS

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Amazon RDS resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [How Amazon RDS works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Identity-based policy
  examples for Amazon RDS](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [AWS managed policies for Amazon RDS](rds-security-iam-awsmanpol.md "rds-security-iam-awsmanpol.md")
- [Amazon RDS updates to AWS managed policies](rds-manpol-updates.md "rds-manpol-updates.md")
- [Preventing cross-service confused deputy problems](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md")
- [Troubleshooting Amazon RDS identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs, depending on the work you do in Amazon RDS.

**Service user** – If you use the Amazon RDS service to do your job, then your administrator provides you
with the credentials and permissions that you need. As you use more Amazon RDS features to do your work, you might need additional permissions.
Understanding how access is managed can help you request the right permissions from your administrator. If you cannot access a feature in
Amazon RDS, see [Troubleshooting Amazon RDS identity and access](security_iam_troubleshoot.md "security_iam_troubleshoot.md").

**Service administrator** – If you're in charge of Amazon RDS resources at your company, you probably have
full access to Amazon RDS. It's your job to determine which Amazon RDS features and resources your employees should access. You must then
submit requests to your administrator to change the permissions of your service users. Review the information on this page to understand the
basic concepts of IAM. To learn more about how your company can use IAM with Amazon RDS, see [How Amazon RDS works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

**Administrator** – If you're an administrator, you might want to learn details about how you can
write policies to manage access to Amazon RDS. To view example Amazon RDS identity-based policies that you can use in IAM, see [Identity-based policy
examples for Amazon RDS](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

You can authenticate to your DB instance using IAM database authentication.

IAM database authentication works with the following DB engines:

- RDS for MariaDB
- RDS for MySQL
- RDS for PostgreSQL

For more information
about authenticating to your DB instance
using IAM, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](UsingWithRDS.md "UsingWithRDS.md").

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity within your AWS account that
has specific permissions. It is similar to a user, but is not associated with a specific person. You can temporarily assume an IAM role in
the AWS Management Console by [switching roles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md"). You can assume a role by calling an AWS CLI
or AWS API operation or by using a custom URL. For more information about methods for using roles, see [Using IAM roles](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md") in the _IAM User Guide_.

IAM roles with temporary credentials are useful in the following situations:

- **Temporary user permissions** – A user can assume an IAM role to temporarily take on
  different permissions for a specific task.
- **Federated user access** –

To assign permissions to a federated identity, you create a role and define permissions for the role. When a federated identity authenticates, the identity is associated with the role and is granted the permissions that are defined by the role. For information about roles for federation, see [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_.

If you use IAM Identity Center, you configure a permission set. To control what your identities can access after they authenticate, IAM Identity Center correlates the permission set to a role in IAM.
For information about permissions sets, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User Guide_.

- **Cross-account access** – You can use an
  IAM role to allow someone (a trusted principal) in a different account to access
  resources in your account. Roles are the primary way to grant cross-account
  access. However, with some AWS services, you can attach a policy directly to a
  resource (instead of using a role as a proxy). To learn the difference between
  roles and resource-based policies for cross-account access, see [How IAM roles
  differ from resource-based policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
  _IAM User Guide_.
- **Cross-service access** –

Some AWS services use features in other AWS services. For example, when you make a call in a service,
it's common for that service to run applications in Amazon EC2 or store objects in Amazon S3. A service might do this
using the calling principal's permissions, using a service role, or using a service-linked role.

    + **Forward access sessions** –

     Forward access sessions (FAS) use the permissions of the principal calling an AWS service, combined with the requesting AWS service to make requests to downstream services. For policy details
     when making FAS requests, see [Forward access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").
    + **Service role** –

     A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
     actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
     more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the *IAM User Guide*.
    + **Service-linked role** –

     A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
     Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
     but not edit the permissions for service-linked roles.

- **Applications running on Amazon EC2** –

You can use an IAM role to manage temporary credentials for applications that are running on an EC2 instance and making AWS CLI or AWS API requests.
This is preferable to storing access keys within the EC2 instance. To assign an AWS role to an EC2 instance and make it
available to all of its applications, you create an instance profile that is attached to the
instance. An instance profile contains the role and enables programs that are running on the EC2 instance to
get temporary credentials. For more information, see [Use an IAM role to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_.

To learn whether to use IAM roles, see [When to create an IAM role (instead of a
user)](../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role "../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to IAM identities or AWS resources. A policy is an object in AWS that,
when associated with an identity or resource, defines their permissions. AWS evaluates these policies when an entity (root user, user, or IAM
role) makes a request. Permissions in the policies determine whether the request is allowed or denied. Most policies are stored in AWS as JSON
documents. For more information about the structure and contents of JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

An administrator can use policies to specify who has access to AWS resources, and what actions they can perform on those resources. Every
IAM entity (permission set or role) starts with no permissions. In other words, by default, users can do nothing, not even change their own password. To give a
user permission to do something, an administrator must attach a permissions policy to a user. Or the administrator can add the user to a group that has
the intended permissions. When an administrator gives permissions to a group, all users in that group are granted those permissions.

IAM policies define permissions for an action regardless of the method that you use to perform the operation. For example, suppose that you have a
policy that allows the `iam:GetRole` action. A user with that policy can get role information from the AWS Management Console, the AWS CLI, or the AWS
API.

### Identity-based policies

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as a permission set or role. These
policies control what actions that identity can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

Identity-based policies can be further categorized as _inline policies_ or _managed
policies_. Inline policies are embedded directly into a single permission set or role. Managed policies are standalone policies that you
can attach to multiple permission sets and roles in your AWS account. Managed policies include AWS managed policies and customer managed
policies. To learn how to choose between a managed policy or an inline policy, see [Choosing between managed policies and inline
policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#choosing-managed-or-inline "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#choosing-managed-or-inline") in the _IAM User Guide_.

For information about AWS managed policies that are specific to
Amazon RDS, see
[AWS managed policies for Amazon RDS](rds-security-iam-awsmanpol.md "rds-security-iam-awsmanpol.md").

### Other policy types

AWS supports additional, less-common policy types. These policy types can set the maximum permissions granted to you by the more common policy
types.

- **Permissions boundaries** – A permissions
  boundary is an advanced feature in which you set the maximum permissions that an
  identity-based policy can grant to an IAM entity (permission set or role). You can
  set a permissions boundary for an entity. The resulting permissions are the
  intersection of entity's identity-based policies and its permissions boundaries.
  Resource-based policies that specify the permission set or role in the
  `Principal` field are not limited by the permissions boundary. An
  explicit deny in any of these policies overrides the allow. For more information
  about permissions boundaries, see [Permissions boundaries for
  IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – SCPs are JSON policies that specify the maximum permissions for
  an organization or organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and centrally managing multiple AWS accounts
  that your business owns. If you enable all features in an organization, then you can apply service control policies (SCPs) to any or all of
  your accounts. The SCP limits permissions for entities in member accounts, including each AWS account root user. For more information about Organizations and
  SCPs, see [How SCPs work](../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md "../../../organizations/latest/userguide/orgs_manage_policies_about-scps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Session policies are
  advanced policies that you pass as a parameter when you programmatically create a
  temporary session for a role or federated user. The resulting session's
  permissions are the intersection of the permission sets or role's identity-based policies and
  the session policies. Permissions can also come from a resource-based policy. An
  explicit deny in any of these policies overrides the allow. For more information,
  see [Session
  policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines
whether to allow a request when multiple policy types are involved, see [Policy
evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.
