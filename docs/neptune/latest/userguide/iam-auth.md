# Authenticating your Amazon Neptune database with AWS Identity and Access Management

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use Neptune resources. IAM is an AWS service that you can
use with no additional charge.

You can use AWS Identity and Access Management (IAM) to authenticate to your Neptune DB instance
or DB cluster. When IAM database authentication is enabled, each request must be
signed using AWS Signature Version 4.

AWS Signature Version 4 adds authentication information to AWS requests.
For security, all requests to Neptune DB clusters with IAM authentication
enabled must be signed with an access key. This key consists of an access key
ID and secret access key. The authentication is managed externally using IAM policies.

Neptune authenticates on connection, and for WebSockets connections it verifies the
permissions periodically to ensure that the user still has access.

###### Note

- Revoking, deleting, or rotating of credentials associated with the IAM user
  is not recommended because it does not terminate any connections that are
  already open.
- There are limits on the number of concurrent WebSocket connections per database
  instance, and on how long a connection can remain open. For more information, see [WebSockets Limits](limits.md#limits-websockets "limits.md#limits-websockets").

## IAM Use Depends on Your Role

How you use AWS Identity and Access Management (IAM) differs, depending on the work you do in Neptune.

**Service user** – If you use the Neptune
service to do your job, then your administrator provides you with the credentials
and permissions that you need for using the Neptune data plane. As you need more access
to do your work, understanding how data access is managed can help you request the
right permissions from your administrator.

**Service administrator** – If you're in charge
of Neptune resources at your company, you probably have access to Neptune
management actions, which correspond to the [Neptune
managment API](api.md "api.md"). It may also be your job to determine which Neptune
data-access actions and resources service users need in order to do their jobs.
An IAM administrator can then apply IAM policies to change the permissions
of your service users.

**IAM administrator** – If you're an IAM
administrator, you will need to write IAM policies to manage both management
and data access to Neptune. To view example Neptune identity-based policies
that you can use, see [Using different kinds of IAM policies for
controlling access to Neptune](security-iam-access-manage.md#iam-auth-policy "security-iam-access-manage.md#iam-auth-policy").

## Authenticating with Identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### IAM Users and Groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM Roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.
