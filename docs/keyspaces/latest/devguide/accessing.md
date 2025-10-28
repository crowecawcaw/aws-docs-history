# Accessing Amazon Keyspaces (for Apache Cassandra)

You can access Amazon Keyspaces using the console, AWS CloudShell, programmatically by running a
`cqlsh` client, the AWS SDK, or by using an Apache 2.0 licensed Cassandra driver. Amazon Keyspaces
supports drivers and clients that are compatible with Apache Cassandra 3.11.2.
Before accessing Amazon Keyspaces, you must complete setting up AWS Identity and Access Management and then grant an IAM identity access permissions to Amazon Keyspaces.

## Setting up AWS Identity and Access Management

### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

## Setting up Amazon Keyspaces

Access to Amazon Keyspaces resources is managed using [IAM](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"). Using IAM, you
can attach policies to IAM users, roles, and federated identities that grant read and
write permissions to specific resources in Amazon Keyspaces.

To get started with granting permissions to an IAM identity, you can use one of the
AWS managed policies for Amazon Keyspaces:

- [AmazonKeyspacesFullAccess](../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesFullAccess.md") – this policy grants permissions to
  access all resources in Amazon Keyspaces with full access to all features.
- [AmazonKeyspacesReadOnlyAccess_v2](../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md "../../../aws-managed-policy/latest/reference/AmazonKeyspacesReadOnlyAccess_v2.md") – this policy grants read-only permissions to Amazon Keyspaces.

For a detailed explanation of the actions defined in the managed policies, see [AWS managed policies for Amazon Keyspaces](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

To limit the scope of actions that an IAM identity can perform or limit the
resources that the identity can access, you can create a custom policy that uses the
`AmazonKeyspacesFullAccess` managed policy as a template and remove all
permissions that you don't need. You can also limit access to specific keyspaces or
tables. For more information about how to restrict actions or limit access to specific
resources in Amazon Keyspaces, see [How Amazon Keyspaces works with
IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

To access Amazon Keyspaces after you have created the AWS account and created a policy that
grants an IAM identity access to Amazon Keyspaces, continue to one of the following
sections:

- [Using the console](console_keyspaces.md "console_keyspaces.md")
- [Using AWS CloudShell](using-aws-with-cloudshell.md "using-aws-with-cloudshell.md")
