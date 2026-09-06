

# Accessing Amazon Keyspaces (for Apache Cassandra)
<a name="accessing"></a>

You can access Amazon Keyspaces using the console, AWS CloudShell, programmatically by running a `cqlsh` client, the AWS SDK, or by using an Apache 2.0 licensed Cassandra driver. Amazon Keyspaces supports drivers and clients that are compatible with Apache Cassandra 3.11.2. Before accessing Amazon Keyspaces, you must complete setting up AWS Identity and Access Management and then grant an IAM identity access permissions to Amazon Keyspaces.

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Setting up Amazon Keyspaces
<a name="SettingUp.KEY"></a>

 Access to Amazon Keyspaces resources is managed using [ IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html). Using IAM, you can attach policies to IAM users, roles, and federated identities that grant read and write permissions to specific resources in Amazon Keyspaces. 

To get started with granting permissions to an IAM identity, you can use one of the AWS managed policies for Amazon Keyspaces:
+ [AmazonKeyspacesFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.html) – this policy grants permissions to access all resources in Amazon Keyspaces with full access to all features.
+ [AmazonKeyspacesReadOnlyAccess\_v2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.html) – this policy grants read-only permissions to Amazon Keyspaces.

For a detailed explanation of the actions defined in the managed policies, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md).

To limit the scope of actions that an IAM identity can perform or limit the resources that the identity can access, you can create a custom policy that uses the `AmazonKeyspacesFullAccess` managed policy as a template and remove all permissions that you don't need. You can also limit access to specific keyspaces or tables. For more information about how to restrict actions or limit access to specific resources in Amazon Keyspaces, see [How Amazon Keyspaces works with IAM](security_iam_service-with-iam.md). 

To access Amazon Keyspaces after you have created the AWS account and created a policy that grants an IAM identity access to Amazon Keyspaces, continue to one of the following sections:
+ [Using the console](console_keyspaces.md)
+ [Using AWS CloudShell](using-aws-with-cloudshell.md)