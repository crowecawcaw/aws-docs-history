# Authenticating with identities

Authentication is how you sign in to AWS using your identity
credentials. You must
be _authenticated_ (signed in to AWS) as the
AWS account root user, as an IAM user, or by assuming an IAM
role.

You can sign in to AWS as a federated identity by using
credentials provided through an identity source. AWS IAM
Identity Center (IAM Identity Center) users, your company's
single sign-on authentication, and your Google or Facebook
credentials are examples of federated identities. When you sign
in as a federated identity, your administrator previously set up
identity federation using IAM roles. When you access AWS by
using federation, you are indirectly assuming a role.

Depending on the type of user you are, you can sign in to the
AWS Management Console or the AWS access portal. For more
information about signing in to AWS,
see [How
to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS
Sign-In User Guide_.

If you access AWS programmatically, AWS provides a software
development kit (SDK) and a command line interface (CLI) to
cryptographically sign your requests by using your credentials.
If you don't use AWS tools, you must sign requests yourself. For
more information about using the recommended method to sign
requests yourself,
see [Signing
AWS API requests](../../../IAM/latest/UserGuide/reference_aws-signing.md "../../../IAM/latest/UserGuide/reference_aws-signing.md") in the _IAM User
Guide_.

Regardless of the authentication method that you use, you may be
required to provide additional security information. For
example, AWS recommends that you use multi-factor authentication
(MFA) to increase the security of your account. To learn more,
see [Multi-factor
authentication](../../../singlesignon/latest/userguide/enable-mfa.md "../../../singlesignon/latest/userguide/enable-mfa.md") in the _AWS IAM Identity Center
User
Guide_ and [Using
multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in
the _IAM User Guide_.

**AWS account root user**

When you create an AWS account, you begin with one sign-in
identity that has complete access to all AWS services and
resources in the account. This identity is called the AWS
account _root user_ and is accessed by
signing in with the e-mail address and password that you used to
create the account. Never use the root user for your everyday
tasks and take steps to safeguard your root user credentials.
Only use them to perform tasks that only the root user can
perform. For the complete list of tasks that require you to sign
in as the root user,
see [Tasks
that require root user credentials](../../../IAM/latest/UserGuide/root-user-tasks.md "../../../IAM/latest/UserGuide/root-user-tasks.md") in the _IAM
User Guide_.

**Federated identity**

It is best practice to require human users, including those that
need administrator access, to use federation with an identity
provider to access AWS services by using temporary credentials.

A _federated identity_ is a user from your
enterprise user directory, a web identity provider, the AWS
Directory Service, the Identity Center directory, or any user
that accesses AWS services by using credentials provided through
an identity source. When federated identities access AWS
accounts, they assume roles, and the roles provide temporary
credentials.

For centralized access management, we recommend that you use AWS
IAM Identity Center. You can create users and groups in IAM
Identity Center, or you can connect and synchronize to a set of
users and groups in your own identity source for use across all
your AWS accounts and applications. For information about IAM
Identity Center,
see [What
is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity
Center User Guide_.

**IAM users and groups**

An [_IAM
user_](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity within your AWS account
that has specific permissions for a single person or
application. We recommend relying on temporary credentials
instead of creating IAM users who have long-term credentials
such as passwords and access keys. If you have a specific use
case that requires long-term credentials with IAM users, we
recommend that you rotate access keys. For more information,
see [Rotate
access keys regularly for use cases that require long-term
credentials](../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials "../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials") in the _IAM User Guide_.

An[_IAM
group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") is an identity that specifies a
collection of IAM users. You can't sign in as a group. You can
use groups to specify permissions for multiple users at a time.
Groups make permissions easier to manage for large sets of
users. For example, you could have a group
named _IAMAdmins_ and give that group
permissions to administer IAM resources.

Users are different from roles. A user is uniquely associated
with one person or application, but a role is intended to be
assumable by anyone who needs it. Users have permanent long-term
credentials, but roles provide temporary credentials. To learn
more,
see [When
to create an IAM user (instead of a role)](../../../IAM/latest/UserGuide/id.md#id_which-to-choose "../../../IAM/latest/UserGuide/id.md#id_which-to-choose") in
the _IAM User Guide_.

**IAM roles**

An[_IAM
role_](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an identity within your AWS account
that has specific permissions. It is similar to an IAM user, but
is not associated with a specific person. You can temporarily
assume an IAM role in the AWS Management Console
by [switching
roles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md"). You can assume a role by calling an AWS CLI or AWS
API operation or by using a custom URL. For more information
about methods for using roles,
see [Using
IAM roles](../../../IAM/latest/UserGuide/id_roles_use.md "../../../IAM/latest/UserGuide/id_roles_use.md") in the _IAM User Guide_.

IAM roles with temporary credentials are useful in the following
situations:

- **Federated user access** –
  To assign permissions to a federated identity, you create a
  role and define permissions for the role. When a federated
  identity authenticates, the identity is associated with the
  role and is granted the permissions that are defined by the
  role. For information about roles for federation,
  see [Creating
  a role for a third-party Identity Provider](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in
  the _IAM User Guide_. If you use IAM
  Identity Center, you configure a permission set. To control
  what your identities can access after they authenticate, IAM
  Identity Center correlates the permission set to a role in
  IAM. For information about permissions sets,
  see [Permission
  sets](../../../singlesignon/latest/userguide/permissionsetsconcept.md "../../../singlesignon/latest/userguide/permissionsetsconcept.md") in the _AWS IAM Identity Center User
  Guide_.
- **Temporary IAM user
  permissions** – An IAM user or role can assume an
  IAM role to temporarily take on different permissions for a
  specific task.
- **Cross-account access** –
  You can use an IAM role to allow someone (a trusted
  principal) in a different account to access resources in
  your account. Roles are the primary way to grant
  cross-account access. However, with some AWS services, you
  can attach a policy directly to a resource (instead of using
  a role as a proxy). To learn the difference between roles
  and resource-based policies for cross-account access,
  see [Cross
  account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM
  User Guide_.
- **Cross-service access** –
  Some AWS services use features in other AWS services. For
  example, when you make a call in a service, it's common for
  that service to run applications in Amazon EC2 or store
  objects in Amazon S3. A service might do this using the
  calling principal's permissions, using a service role, or
  using a service-linked role.
  - **Service role** – A
    service role is
    an [IAM
    role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that a service assumes to perform actions on
    your behalf. An IAM administrator can create, modify,
    and delete a service role from within IAM. For more
    information,
    see [Creating
    a role to delegate permissions to an AWS
    service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User
    Guide_.
  - **Service-linked role** –
    A service-linked role is a type of service role that is
    linked to an AWS service. The service can assume the
    role to perform an action on your behalf. Service-linked
    roles appear in your AWS account and are owned by the
    service. An IAM administrator can view, but not edit the
    permissions for service-linked roles.

- **Applications running on Amazon
  EC2** – You can use an IAM role to manage temporary
  credentials for applications that are running on an EC2
  instance and making AWS CLI or AWS API requests. This is
  preferable to storing access keys within the EC2 instance.
  To assign an AWS role to an EC2 instance and make it
  available to its applications, you create an instance
  profile that is attached to the instance. An instance
  profile contains the role and enables programs that are
  running on the EC2 instance to get temporary credentials.
  For more information,
  see [Using
  an IAM role to grant permissions to applications running on
  Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the _IAM User
  Guide_.

To learn whether to use IAM roles or IAM users,
see [When
to create an IAM role (instead of a user)](../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role "../../../IAM/latest/UserGuide/id.md#id_which-to-choose_role") in
the _IAM User Guide_.
