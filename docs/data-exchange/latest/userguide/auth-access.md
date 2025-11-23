# Identity and access management in AWS Data Exchange

To perform any operation in AWS Data Exchange, such as creating an import job using an AWS SDK, or
subscribing to a product in the AWS Data Exchange console, AWS Identity and Access Management (IAM) requires that you
authenticate that you're an approved AWS user. For example, if you're using the AWS Data Exchange
console, you authenticate your identity by providing your AWS sign-in credentials.

After you authenticate your identity, IAM controls your access to AWS with a defined
set of permissions on a set of operations and resources. If you're an account administrator,
you can use IAM to control the access of other users to the resources that are associated
with your account.

###### Topics

- [Authentication](#authentication "#authentication")
- [Access control](access-control.md "access-control.md")
- [AWS Data Exchange API permissions: actions and resources
  reference](api-permissions-ref.md "api-permissions-ref.md")
- [AWS managed policies for AWS Data Exchange](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

## Authentication

You can access AWS with any of the following types of identities:

- **AWS account root user** –

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

- **User** – A [user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md") is an identity in your
  AWS account that has specific custom permissions. You can use your IAM
  credentials to sign in to secure AWS webpages like the AWS Management Console or the
  AWS Support Center.
- **IAM role** –

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

Roles with temporary credentials are useful in the following situations:

    + **Federated user access** – Instead
     of creating a user, you can use existing identities from Directory Service, your
     enterprise user directory, or a web identity provider. These are known
     as *federated users*. AWS assigns a role to a
     federated user when access is requested through an identity provider.
     For more information about federated users, see [Federated Users and Roles](../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles "../../../IAM/latest/UserGuide/introduction_access-management.md#intro-access-roles").
    + **AWS service access** – A
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
     a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").
    + **Applications running on Amazon EC2** –
     You can use an IAM role to manage temporary credentials for
     applications that are running on an Amazon EC2 instance and making AWS CLI or
     AWS API requests. This is preferable to storing access keys in the
     Amazon EC2 instance. To assign an AWS role to an Amazon EC2 instance and make it
     available to all of its applications, you create an instance profile
     that is attached to the instance. An instance profile contains the role
     and enables programs that are running on the Amazon EC2 instance to get
     temporary credentials. For more information, see [Using an IAM
     Role to Grant Permissions to Applications Running on Amazon EC2
     Instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md").
