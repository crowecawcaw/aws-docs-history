# Amazon EventBridge and AWS Identity and Access Management

To access Amazon EventBridge, you need credentials that AWS can use to authenticate your requests.
Your credentials must have permissions to access AWS resources, such as retrieving event
data from other AWS resources. The following sections provide details on how you can use
[AWS Identity and Access Management (IAM)](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") and EventBridge to help
secure your resources by controlling who can access them.

###### Topics

- [Authentication](#eb-authentication "#eb-authentication")
- [Access control](#eb-access-control "#eb-access-control")
- [Managing access permissions to your Amazon EventBridge
  resources](eb-manage-iam-access.md "eb-manage-iam-access.md")
- [Using identity-based policies (IAM policies) for
  Amazon EventBridge](eb-use-identity-based.md "eb-use-identity-based.md")
- [Using resource-based policies for Amazon EventBridge](eb-use-resource-based.md "eb-use-resource-based.md")
- [Cross-service confused deputy
  prevention in Amazon EventBridge](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [Resource-based policies for Amazon EventBridge schemas](eb-resource-based-schemas.md "eb-resource-based-schemas.md")
- [Amazon EventBridge permissions reference](eb-permissions-reference.md "eb-permissions-reference.md")
- [Using IAM policy conditions in Amazon EventBridge](eb-use-conditions.md "eb-use-conditions.md")
- [Using service-linked roles for
  EventBridge](using-service-linked-roles.md "using-service-linked-roles.md")

## Authentication

You can access AWS as any of the following types of identities:

- **AWS account root user** – When you sign
  up for AWS, you provide an email address and password that is associated with
  your account. These are your _root credentials_, and they
  provide complete access to all of your AWS resources.

###### Important

For security reasons, we recommend that you use the root credentials only
to create an _administrator_, which is an _IAM
user_ with full permissions to your account. Then you can use
this administrator to create other users and roles with limited
permissions. For more information, see [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users") and [Creating an
Admin User and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
_IAM User Guide_.

- **IAM user** – An [IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity within
  your account that has specific permissions, for example, permission to send
  event data to a target in EventBridge. You can use an IAM sign-in credentials to sign in to secure AWS webpages such as the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"), [AWS Discussion Forums](https://forums.aws.amazon.com/ "https://forums.aws.amazon.com/"), or the
  [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

In addition to sign-in credentials, you can also generate [access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") for
each user. You can use these keys when you access AWS services
programmatically to cryptographically sign your request, either through [one of the SDKs](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/") or by using the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). If you don’t use AWS
tools, you must sign the request yourself with _Signature Version
4_, a protocol for authenticating inbound API requests. For more
information about authenticating requests, see [Signature Version 4 Signing
Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _Amazon Web Services General Reference_.

- **IAM role** – An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is another IAM identity
  that you can create in your account that has specific permissions. It's similar
  to an _IAM user_, but it isn't associated with a specific
  person. Using an IAM role, you can obtain temporary access keys to access
  AWS services and resources. IAM roles with temporary credentials are useful
  in the following situations:
  - **Federated user access** – Instead
    of creating a user, you can use identities from AWS Directory Service, your
    enterprise user directory, or a web identity provider (IdP). These are
    known as _federated users_. AWS assigns a role to a
    federated user when the user requests access through an [identity
    provider](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md"). For more information about federated users, see
    [Federated Users and Roles](../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles "../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles") in the
    _IAM User Guide_.
  - **Cross-account access** – You can
    use an IAM role in your account to grant another account permission to
    access your account’s resources. For an example, see [Tutorial:
    Delegate Access Across AWS Accounts Using IAM Roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") in
    the _IAM User Guide_.
  - **AWS service access** – You can
    use an IAM role in your account to grant an AWS service permission
    to access your account’s resources. For example, you can create a role
    that allows Amazon Redshift to load data stored in an Amazon S3 bucket into an
    Amazon Redshift cluster. For more information, see [Creating a Role
    to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
    _IAM User Guide_.
  - **Applications running on Amazon EC2** –
    For Amazon EC2 applications that need access to EventBridge, you can either store
    access keys in the EC2 instance or you can use an IAM role to manage
    temporary credentials. To assign an AWS role to an EC2 instance, you
    create an instance profile that is attached to the instance. An instance
    profile contains the role, and it provides temporary credentials to
    applications running on the EC2 instance. For more information, see
    [Using
    Roles for Applications on Amazon EC2](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
    _IAM User Guide_.

## Access control

To create or access EventBridge resources, you need both valid credentials and permissions.
For example, to invoke AWS Lambda, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS) targets, you
must have permissions to those services.
