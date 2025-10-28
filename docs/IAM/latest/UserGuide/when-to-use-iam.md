# When do I use IAM?

AWS Identity and Access Management is a core infrastructure service that provides the foundation for access control
based on identities within AWS. You use IAM every time you access your AWS account. The
way you use IAM will depend on the specific responsibilities and job functions within your
organization. Users of AWS services use IAM to access the AWS resources required for their
day-to-day work, with administrators granting the appropriate permissions. IAM administrators,
on the other hand, are responsible for managing IAM identities and writing policies to control
access to resources. Regardless of your role, you interact with IAM whenever you authenticate
and authorize access to AWS resources. This could involve signing in as an IAM user,
assuming an IAM role, or leveraging identity federation for seamless access. Understanding the
various IAM capabilities and use cases is crucial for effectively managing secure access to
your AWS environment. When it comes to creating policies and permissions, IAM provides a
flexible and granular approach. You can define trust policies to control which principals can
assume a role, in addition to identity-based policies that specify the actions and resources a
user or role can access. By configuring these IAM policies, you can help ensure that users and
applications have the appropriate level of permissions to perform their required tasks.

## When you are performing different job

functions

AWS Identity and Access Management is a core infrastructure service that provides the foundation for access control
based on identities within AWS. You use IAM every time you access your AWS
account.

How you use IAM differs, depending on the work that you do in AWS.

- Service user – If you use an AWS service to do your job, then your administrator
  provides you with the credentials and permissions that you need. As you use more advanced
  features to do your work, you might need additional permissions. Understanding how access
  is managed can help you request the right permissions from your administrator.
- Service administrator – If you're in charge of an AWS resource at your company, you
  probably have full access to IAM. It's your job to determine which IAM features and
  resources your service users should access. You must then submit requests to your IAM
  administrator to change the permissions of your service users. Review the information on
  this page to understand the basic concepts of IAM.
- IAM administrator – If you're an IAM administrator, you manage IAM identities
  and write policies to manage access to IAM.

## When you are authorized to access AWS

resources

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](reference_sigv.md "reference_sigv.md") in the _IAM User Guide_.

## When you sign-in as an IAM user

An _[IAM user](id_users.md "id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](best-practices.md#bp-users-federation-idp "best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](id_groups.md "id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](gs-identities-iam-users.md "gs-identities-iam-users.md") in the _IAM User Guide_.

## When you assume an IAM role

An _[IAM role](id_roles.md "id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](id_roles_use_switch-role-console.md "id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](id_roles_manage-assume.md "id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](access_policies-cross-account-resource-access.md "access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## When you create policies and

permissions

You grant permissions to a user by creating a policy, which is a document that lists the
actions that a user can perform and the resources those actions can affect. Any actions or
resources that are not explicitly allowed are denied by default. Policies can be created and
attached to principals (users, groups of users, roles assumed by users, and resources).

You can use these policies with an IAM role:

- **Trust policy** – Defines which [principal](../../../glossary/latest/reference/glos-chap.md#principal "../../../glossary/latest/reference/glos-chap.md#principal") can assume the role, and under which conditions. A trust policy is a
  specific type of resource-based policy for IAM roles. A role can have only one trust
  policy.
- **Identity-based policies (inline and managed)** –
  These policies define the permissions that the user of the role is able to perform (or is
  denied from performing), and on which resources.

Use the [Example IAM identity-based policies](access_policies_examples.md "access_policies_examples.md") to help you define permissions for your IAM identities. After you find the policy that
you need, choose view the policy to view the JSON for the policy. You can use the JSON policy
document as a template for your own policies.

###### Note

If you are using IAM Identity Center to manage your users,
you assign permission sets in IAM Identity Center instead of attaching a permissions policy to a
principal. When you assign a permission set to a group or user in AWS IAM Identity Center, IAM Identity Center creates
corresponding IAM roles in each account, and attaches the policies specified in the
permission set to those roles. IAM Identity Center manages the role, and allows the authorized users
you’ve defined to assume the role. If you modify the permission set, IAM Identity Center ensures that the
corresponding IAM policies and roles are updated accordingly.

For more information about IAM Identity Center, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the
_AWS IAM Identity Center User Guide_.
