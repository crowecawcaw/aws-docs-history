AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Identity and access management in AWS Migration Hub

Access to AWS Migration Hub requires credentials that AWS can use to authenticate your requests.
Those credentials must have permissions to access AWS resources, such as an Migration Hub
ProgressUpdateStream or an Amazon EC2 instance. The following sections provide details on how you
can use [AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and Migration Hub to
help secure your resources by controlling who can access them:

- [Authentication](#authentication "#authentication")
- [Access control](#access-control "#access-control")

## Authentication

You can access AWS as any of the following types of identities:

- **AWS account root user**

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

- **IAM users and groups**

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

- **IAM role**

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.
IAM roles with temporary credentials are useful in the
following situations:

    + **Federated user access** –

    To assign permissions to a federated identity, you create a role and define permissions for the role. When a federated identity authenticates, the identity is associated with the role and is granted the permissions that are defined by the role. For information about roles for federation, see [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the *IAM User Guide*.

    If you use IAM Identity Center, you configure a permission set. To control what your identities can access after they authenticate, IAM Identity Center correlates the permission set to a role in IAM.
    For information about permissions sets, see [Permission sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the *AWS IAM Identity Center User Guide*.
    + **AWS service access** –

     A service role is an [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform
     actions on your behalf. An IAM administrator can create, modify, and delete a service role from within IAM. For
     more information, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the *IAM User Guide*.
    + **Applications running on Amazon EC2** –

     You can use an IAM role to manage temporary credentials for applications that are running on an EC2 instance and making AWS CLI or AWS API requests.
     This is preferable to storing access keys within the EC2 instance. To assign an AWS role to an EC2 instance and make it
     available to all of its applications, you create an instance profile that is attached to the
     instance. An instance profile contains the role and enables programs that are running on the EC2 instance to
     get temporary credentials. For more information, see [Use an IAM role to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
     *IAM User Guide*.

## Access control

You can have valid credentials to authenticate your requests, but unless you have
permissions you cannot create or access AWS Migration Hub resources. For example, you must
have permissions to create a Migration Hub API type, `ProgressUpdateStream`, to use
the AWS Application Discovery Service, and to use AWS migration tools.

The following sections describe how to manage permissions for AWS Migration Hub.

- [AWS Migration Hub roles and policies](policy-templates.md "policy-templates.md")
- [AWS Migration Hub API Permissions: Actions
  and Resources Reference](migrationhub-api-permissions-ref.md "migrationhub-api-permissions-ref.md")
- [AWS Migration Hub Authentication and Access
  Control Explained](auth-and-access-explained.md "auth-and-access-explained.md")
