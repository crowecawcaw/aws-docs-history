After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Step 1: Set Up an Account and Create an Administrator

User

Before you use Amazon Kinesis Data Analytics for the first time, complete the following
tasks:

1. [Sign Up for AWS](#setting-up-signup "#setting-up-signup")
2. [Create an IAM User](#setting-up-iam "#setting-up-iam")

## Sign Up for AWS

When you sign up for Amazon Web Services, your AWS account is automatically signed
up for all services in AWS, including Amazon Kinesis Data Analytics. You are charged only for the
services that you use.

With Kinesis Data Analytics, you pay only for the resources you use.

If you are a new AWS customer, you can get started with Kinesis Data Analytics for free. For more
information, see [AWS Free Usage
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next task. If you don't have an AWS account,
perform the steps in the following procedure to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Note your AWS account ID because you'll need it for the next task.

## Create an IAM User

Services in AWS, such as Amazon Kinesis Data Analytics, require that you provide
credentials when you access them so that the service can determine whether you
have permissions to access the resources owned by that service. The console
requires your password. You can create access keys for your AWS account to
access the AWS CLI or API. However, we don't recommend that you access AWS using
the credentials for your AWS account. Instead, we recommend that you use
AWS Identity and Access Management (IAM). Create an IAM user, add the user to an IAM group with
administrative permissions, and then grant administrative permissions to the
IAM user that you created. You can then access AWS using a special URL and
that IAM user's credentials.

If you signed up for AWS, but you haven't created an IAM user for yourself, you can create one
using the IAM console.

The Getting Started exercises in this guide assume that you have a user
(`adminuser`) with administrator privileges. Follow the procedure
to create `adminuser` in your account.

###### To create an administrator user and sign in to the console

1. Create an administrator user called `adminuser` in your AWS account. For
   instructions, see
   [Creating Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md")
   in the _IAM User Guide_.
2. A user can sign in to the AWS Management Console using a special URL. For more information, [How Users
   Sign In to Your Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
   _IAM User Guide_.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

## Next Step

[Step 2: Set Up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")
