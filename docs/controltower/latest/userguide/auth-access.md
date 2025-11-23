# Identity and access management in AWS Control Tower

To perform any operation in your landing zone, such as provisioning accounts in Account Factory or
creating new organizational units (OUs) in the AWS Control Tower console, either AWS Identity and Access Management (IAM) or
AWS IAM Identity Center require you to authenticate that you're an approved AWS user. For example, if
you're using the AWS Control Tower console, you authenticate your identity by providing your AWS
credentials, as provided by your administrator.

After you authenticate your identity, IAM controls your access to AWS with a defined
set of permissions on a specific set of operations and resources. If you are an account
administrator, you can use IAM to control the access of other IAM users to the resources
that are associated with your account.

###### Topics

- [Authentication](#authentication "#authentication")
- [Access control](#access-control "#access-control")
- [Working with AWS IAM Identity Center and AWS Control Tower](sso.md "sso.md")
- [Overview of managing access permissions to
  your AWS Control Tower resources](access-control-overview.md "access-control-overview.md")
- [Prevent cross-service impersonation](prevent-confused-deputy.md "prevent-confused-deputy.md")
- [Using identity-based policies (IAM
  policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md")

## Authentication

You have access to AWS as any of the following types of identities:

- **AWS account root user** – When you first
  create an AWS account, you begin with an identity that has complete access to
  all AWS services and resources in the account. This identity is called the
  AWS account root user. You have access to this identity when you sign in with the
  email address and password that you used to create the account. We strongly
  recommend that you do not use the root user for your everyday tasks, even the
  administrative ones. Instead, adhere to the [best practice of
  using the root user only to create your first IAM Identity Center user (recommended) or
  IAM user (not a best practice in most use cases)](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users"). Then securely
  lock away the root user credentials and use them to perform only a few account and
  service management tasks. For more information, see [When to sign in as a root user](root-login.md "root-login.md").
- **IAM user** – An [IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity within
  your AWS account that has specific, customized permissions. You can use the
  IAM user credentials to sign in to secure AWS webpages such as the AWS
  Management Console, AWS Discussion Forums, or the AWS Support Center. AWS
  best practices recommend that you create an IAM Identity Center user instead of an IAM user,
  because there is more security risk when you create an IAM user that has
  long-term credentials.

If you must create an IAM user for a certain purpose, in addition to sign-in
credentials, you can generate access keys for each IAM user. You can use these
keys when you call AWS services programmatically, either through one of the
several SDKs or by using the AWS Command Line Interface (CLI). The SDK and CLI
tools use the access keys to cryptographically sign your request. If you don’t
use AWS tools, you must sign the request yourself. AWS Control Tower supports Signature
Version 4, a protocol for authenticating inbound API requests. For more
information about authenticating requests, see
[Signature
Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the AWS General Reference.

- **IAM role** – An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity
  that you can create in your account that has specific permissions. An IAM role
  is similar to an IAM user in that it is an AWS identity, and it has
  permissions policies that determine what the identity can and cannot do in
  AWS. However, instead of being uniquely associated with one person, a role is
  intended to be assumable by anyone who needs it. Also, a role does not have
  standard long-term credentials such as a password or access keys associated with
  it. Instead, when you assume a role, it provides you with temporary security
  credentials for your role session. IAM roles with temporary credentials are
  useful in the following situations:
  - **Federated user access** – Instead
    of creating an IAM user, you can use existing identities from Directory Service,
    your enterprise user directory, or a web identity provider. These are
    known as _federated users_. AWS assigns a role to a
    federated user when access is requested through an identity provider.
    For more information about federated users, see [Federated Users and Roles](../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles "../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles") in the
    _IAM User Guide_.
  - **AWS service access** – A
    service role is an IAM role that a service assumes to perform actions
    in your account on your behalf. When you set up some AWS service
    environments, you must define a role for the service to assume. This
    service role must include all the permissions that are required for the
    service to access the AWS resources that it needs. Service roles vary
    from service to service, but many allow you to choose your permissions
    as long as you meet the documented requirements for that service.
    Service roles provide access only within your account and cannot be used
    to grant access to services in other accounts. You can create, modify,
    and delete a service role from within IAM. For example, you can create
    a role that allows Amazon Redshift to access an Amazon S3 bucket on your behalf and then
    load data from that bucket into an Amazon Redshift cluster. For more information,
    see [Creating
    a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
    _IAM User Guide_.
  - **Applications running on Amazon EC2** –
    You can use an IAM role to manage temporary credentials for
    applications that are running on an Amazon EC2 instance and making AWS CLI
    or AWS API requests. This is preferable to storing access keys within
    the Amazon EC2 instance. To assign an AWS role to an Amazon EC2 instance and
    make it available to all of its applications, you create an instance
    profile that is attached to the instance. An instance profile contains
    the role and enables programs that are running on the Amazon EC2 instance to
    get temporary credentials. For more information, see [Using an IAM
    Role to Grant Permissions to Applications Running on Amazon EC2
    Instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
    _IAM User Guide_.

- **IAM Identity Center user** Authentication to the IAM Identity Center user
  portal is controlled by the directory that you have connected to IAM Identity Center. However,
  authorization to the AWS accounts that are available to end users from within
  the user portal is determined by two factors:
  - Who has been assigned access to those AWS accounts in the AWS
    IAM Identity Center console. For more information, see [Single Sign-On Access](../../../singlesignon/latest/userguide/useraccess.md "../../../singlesignon/latest/userguide/useraccess.md") in
    the _AWS IAM Identity Center User Guide_.
  - What level of permissions have been granted to the end-users in the
    AWS IAM Identity Center console to allow them the appropriate access to those AWS
    accounts. For more information, see [Permission Sets](../../../singlesignon/latest/userguide/permissionsets.md "../../../singlesignon/latest/userguide/permissionsets.md") in
    the _AWS IAM Identity Center User Guide_.

## Access control

To create, update, delete, or list AWS Control Tower resources, or other AWS resources in
your landing zone you need permissions to perform the operation, and you need permissions to
access the corresponding resources. In addition, to perform the operation
programmatically, you need valid access keys.

The following sections describe how to manage permissions for AWS Control Tower:

###### Topics

- [Overview of managing access permissions to
  your AWS Control Tower resources](access-control-overview.md "access-control-overview.md")
- [Using identity-based policies (IAM
  policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md")
