End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 1: Set Up an AWS Account and Create an Administrator

User

Before you use Amazon Lex for the first time, complete the following tasks:

1. [Sign Up for AWS](#gs-account-create "#gs-account-create")
2. [Create a user](#gs-account-user "#gs-account-user")

## Sign Up for AWS

If you already have an AWS account, skip this task.

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed
up for all services in AWS, including Amazon Lex. You are charged only for the services
that you use.

With Amazon Lex, you pay only for the resources that you use. If you are a new AWS
customer, you can get started with Amazon Lex for free. For more information, see [AWS Free Usage Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next task. If you don't have an
AWS account, use the following procedure to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Write down your AWS account ID because you'll need it for the next task.

## Create a user

Services in AWS, such as Amazon Lex, require that you provide credentials when you
access them so that the service can determine whether you have permissions to access
the resources owned by that service. The console requires your password. However, we
don't recommend that you access AWS using the credentials for your
AWS account. Instead, we recommend that you:

- Use AWS Identity and Access Management (IAM) to create a user
- Add the user to an IAM group with administrative permissions
- Grant administrative permissions to the user that you
  created.

You can then access AWS using a special URL and the user's
credentials.

The Getting Started exercises in this guide assume that you have a user
(`adminuser`) with administrator privileges. Follow the procedure to
create `adminuser` in your account.

###### To create an administrator user and sign in to the console

1. Create an administrator user called `adminuser` in your AWS
   account. For instructions, see [Creating
   Your First User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
   _IAM User Guide_.
2. As a user, you can sign in to the AWS Management Console using a special URL. For more
   information, [How Users
   Sign In to Your Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
   _IAM User Guide_.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

## Next Step

[Step 2: Set Up the AWS Command Line Interface](gs-set-up-cli.md "gs-set-up-cli.md")
