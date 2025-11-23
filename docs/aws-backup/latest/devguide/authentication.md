# Authentication

Access to AWS Backup or the AWS services that you are backing up requires credentials that
AWS can use to authenticate your requests. You can access AWS as any of the following
types of identities:

- **AWS account root user** – When you sign up
  for AWS, you provide an email address and password that is associated with your AWS
  account. This is your _AWS account root user_. Its credentials
  provide complete access to all of your AWS resources.

###### Important

For security reasons, we recommend that you use the root user only to create an
_administrator_. The administrator is an _IAM
user_ with full permissions to your AWS account. You can then use this
admin user to create other IAM users and roles with limited permissions. For more
information, see [IAM
Best Practices](../../../IAM/latest/UserGuide/best-practices.md#create-iam-users "../../../IAM/latest/UserGuide/best-practices.md#create-iam-users") and [Creating Your First IAM
Admin User and Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_.

- **IAM user** – An [IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity within your
  AWS account that has specific custom permissions (for example, permissions to create a
  backup vault to store your backups in). You can use an IAM user name and password to
  sign in to secure AWS webpages like the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"), [AWS Discussion Forums](https://forums.aws.amazon.com/ "https://forums.aws.amazon.com/"),
  or the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

In addition to a user name and password, you can also generate [access keys](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") for each user.
You can use these keys when you access AWS services programmatically, either through
[one of the several SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") or by using the
[AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The SDK and AWS CLI
tools use the access keys to cryptographically sign your request. If you don't use the
AWS tools, you must sign the request yourself. For more information about
authenticating requests, see [Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the
_AWS General Reference_.

- **IAM role** – An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is another IAM identity that
  you can create in your account that has specific permissions. It is similar to an IAM
  user, but it is not associated with a specific person. An IAM role enables you to
  obtain temporary access keys that can be used to access AWS services and resources.
  IAM roles with temporary credentials are useful in the following situations:
  - Federated user access – Instead of creating an IAM user, you can use
    pre-existing user identities from Directory Service, your enterprise user directory, or a web
    identity provider. These are known as _federated users_. AWS
    assigns a role to a federated user when access is requested through an [identity provider](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md"). For more
    information about federated users, see [Federated Users and Roles](../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles "../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles") in the
    _IAM User Guide_.
  - Cross-account administration – You can use an IAM role in your account
    to grant another AWS account permissions to administer your account's resources.
    For an example, see [Tutorial: Delegate
    Access Across AWS accounts Using IAM Roles](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") in the
    _IAM User Guide_.
  - AWS service access – You can use an IAM role in your account to grant
    an AWS service permissions to access your account's resources. For more
    information, see [Creating a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
    _IAM User Guide_.
  - Applications running on Amazon Elastic Compute Cloud (Amazon EC2) – You can use an IAM role to
    manage temporary credentials for applications running on an Amazon EC2 instance and
    making AWS API requests. This is preferable to storing access keys within the EC2
    instance. To assign an AWS role to an EC2 instance and make it available to all of
    its applications, you create an instance profile that is attached to the instance.
    An instance profile contains the role and enables programs running on the EC2
    instance to get temporary credentials. For more information, see [Using an IAM Role to Grant
    Permissions to Applications Running on Amazon EC2 Instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
    _IAM User Guide_.
