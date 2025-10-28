# Identity and access management in

Amazon Route 53

To perform any operation on Amazon Route 53 resources, such as registering a domain or updating a
record, AWS Identity and Access Management (IAM) requires you to authenticate that you're an approved AWS user.
If you're using the Route 53 console, you authenticate your identity by providing your AWS
user name and a password.

After you authenticate your identity, IAM controls your access to AWS by verifying
that you have permissions to perform operations and to access resources. If you are an
account administrator, you can use IAM to control the access of other users to the
resources that are associated with your account.

This chapter explains how to use [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md")
and Route 53 to help secure your resources.

###### Topics

- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Access control](#access-control "#access-control")
- [Overview of managing access permissions to
  your Amazon Route 53 resources](access-control-overview.md "access-control-overview.md")
- [Using identity-based policies
  (IAM policies) for Amazon Route 53](access-control-managing-permissions.md "access-control-managing-permissions.md")
- [Using Service-Linked Roles for
  Amazon Route 53 Resolver](using-service-linked-roles.md "using-service-linked-roles.md")
- [AWS managed policies for Amazon Route 53](security-iam-awsmanpol-route53.md "security-iam-awsmanpol-route53.md")
- [Using IAM policy conditions for
  fine-grained access control](specifying-conditions-route53.md "specifying-conditions-route53.md")
- [Amazon Route 53 API permissions: Actions, resources,
  and conditions reference](r53-api-permissions-ref.md "r53-api-permissions-ref.md")

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or AWS Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Access control

To create, update, delete, or list Amazon Route 53 resources, you need permissions to perform the
operation, and you need permission to access the corresponding resources.

The following sections describe how to manage permissions for Route 53. We recommend that
you read the overview first.

###### Topics
