# Accessing Amazon Keyspaces (for Apache Cassandra)

You can access Amazon Keyspaces using the console, AWS CloudShell, programmatically by running a
`cqlsh` client, the AWS SDK, or by using an Apache 2.0 licensed Cassandra driver. Amazon Keyspaces
supports drivers and clients that are compatible with Apache Cassandra 3.11.2.
Before accessing Amazon Keyspaces, you must complete setting up AWS Identity and Access Management and then grant an IAM identity access permissions to Amazon Keyspaces.

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Setting up Amazon Keyspaces

Access to Amazon Keyspaces resources is managed using [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"). Using IAM, you
can attach policies to IAM users, roles, and federated identities that grant read and
write permissions to specific resources in Amazon Keyspaces.

To get started with granting permissions to an IAM identity, you can use one of the
AWS managed policies for Amazon Keyspaces:

- [AmazonKeyspacesFullAccess](../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md") – this policy grants permissions to
  access all resources in Amazon Keyspaces with full access to all features.
- [AmazonKeyspacesReadOnlyAccess\_v2](../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md") – this policy grants read-only permissions to Amazon Keyspaces.

For a detailed explanation of the actions defined in the managed policies, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

To limit the scope of actions that an IAM identity can perform or limit the
resources that the identity can access, you can create a custom policy that uses the
`AmazonKeyspacesFullAccess` managed policy as a template and remove all
permissions that you don't need. You can also limit access to specific keyspaces or
tables. For more information about how to restrict actions or limit access to specific
resources in Amazon Keyspaces, see [How Amazon Keyspaces works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

To access Amazon Keyspaces after you have created the AWS account and created a policy that
grants an IAM identity access to Amazon Keyspaces, continue to one of the following
sections:

- [Using the console](console_keyspaces.md "console_keyspaces.md")
- [Using AWS CloudShell](using-aws-with-cloudshell.md "using-aws-with-cloudshell.md")
