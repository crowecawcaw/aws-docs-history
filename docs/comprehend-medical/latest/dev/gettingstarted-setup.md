# Step 1: Set up an AWS account and create an

administrator user

Before you use Amazon Comprehend Medical for the first time, complete the following tasks:

1. [Sign up for AWS](#setting-up-signup-med "#setting-up-signup-med")
2. [Create an IAM User](#setting-up-iam-med "#setting-up-iam-med")

## Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically signed up
for all AWS services, including Amazon Comprehend Medical. You are charged only for the services that
you use.

With Amazon Comprehend Medical, you pay only for the resources that you use. If you are a new AWS
customer, you can get started with Amazon Comprehend Medical for free. For more information, see [AWS Free Usage Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next section.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Record your AWS account ID because you'll need it for the next task.

## Create an IAM User

Services in AWS, such as Amazon Comprehend Medical, require that you provide credentials when you
access them. This allows the service to determine whether you have permissions to
access the service's resources.

We strongly recommend that you access AWS using AWS Identity and Access Management (IAM), not the
credentials for your AWS account. To use IAM to access AWS, create an IAM user,
add the user to an IAM group with administrative permissions, and then grant
administrative permissions to the IAM user. You can then access AWS using a
special URL and the IAM user's credentials.

The Getting Started exercises in this guide assume that you have a user with
administrator privileges, `adminuser`.

###### To create an administrator and sign in to the console

1. Create a user named `adminuser` in your AWS account. For
   instructions, see [Creating
   Your First IAM User and Administrators Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
   _IAM User Guide_.
2. Sign in to the AWS Management Console using a special URL. For more information, see
   [How
   Users Sign In to Your Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
   _IAM User Guide_.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

## Next step

[Step 2: Set up the AWS Command Line Interface (AWS CLI)](gettingstarted-awscli.md "gettingstarted-awscli.md")
