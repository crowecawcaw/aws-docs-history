# Create and configure AWS credentials for Amazon Keyspaces

To access Amazon Keyspaces programmatically with the AWS CLI, the AWS SDK, or with Cassandra client
drivers and the SigV4 plugin, you need an IAM user with access keys. When you use Amazon Keyspaces
programmatically, you provide your AWS access keys so that AWS can verify your identity
in programmatic calls. Your access keys consist of an access key ID (for example,
AKIAIOSFODNN7EXAMPLE) and a secret access key (for example,
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY). This topic walks you through the required steps
in this process.

Security best practices recommend that you create IAM users with limited permissions and instead associate IAM roles with the
permissions needed to perform specific tasks. IAM users can then temporarily assume IAM roles to perform the required tasks. For example, IAM users
in your account using the Amazon Keyspaces console can switch to a role
to temporarily use the permissions of the role in the console. The users give up their original permissions and take on the permissions
assigned to the role. When the users exit the role, their original permissions are restored. The credentials the users use to assume
the role are temporary. On the contrary, IAM users have long-term credentials, which presents a security risk if instead of assuming
roles they have permissions directly assigned to them. To help mitigate this
risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these
users when they are no longer needed. For more information about roles, see [Common scenarios for roles: Users, applications, and services](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md") in the _IAM User Guide_.

###### Topics

- [Credentials required by the AWS CLI, the AWS SDK, or the Amazon Keyspaces SigV4 plugin for Cassandra client drivers](SigV4_credentials.md "SigV4_credentials.md")
- [Create temporary credentials to connect to Amazon Keyspaces using an IAM role and the SigV4 plugin](temporary.credentials.md "temporary.credentials.md")
- [Create an IAM user for programmatic access
  to Amazon Keyspaces in your AWS account](access.credentials.md "access.credentials.md")
- [Create new access keys for an IAM user](create.md "create.md")
- [Store access keys for programmatic access](aws.credentials.md "aws.credentials.md")
