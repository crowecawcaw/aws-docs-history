# Step 1: Set up an AWS Account and

create an administrator User

Before you use Amazon Lex V2 for the first time, complete the following
tasks:

1. [Sign Up for AWS](#gs-account-create "#gs-account-create")
2. [Create an IAM user](#gs-account-user "#gs-account-user")

## Sign Up for AWS

If you already have an AWS account, skip this task.

When you sign up for Amazon Web Services (AWS), your AWS account is
automatically signed up for all services in AWS, including
Amazon Lex V2. You are charged only for the services that you
use.

With Amazon Lex V2, you pay only for the resources that you use. If
you are a new AWS customer, you can get started with Amazon Lex V2
for free. For more information, see [AWS Free Usage
Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").

If you already have an AWS account, skip to the next task.
If you don't have an AWS account, use the following procedure
to create one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

Write down your AWS account ID because you'll need it for
the next task.

## Create an IAM user

Services in AWS, such as Amazon Lex V2, require that you provide
credentials when you access them so that the service can
determine whether you have permissions to access the resources
owned by that service.

Create an IAM user account to access your account for Amazon Lex V2:

- Use AWS Identity and Access Management (IAM) to create an IAM user
- Add the user to an IAM group with administrative
  permissions
- Grant administrative permissions to the IAM user
  that you created.

You can then access AWS using a special URL and the IAM user's
credentials.

The Getting Started exercises in this guide assume that you
have a user (`adminuser`) with administrator
privileges. Follow the procedure to create
`adminuser` in your account.

###### To create an administrator user and sign in to the

console

1. Create an administrator user called
   `adminuser` in your AWS account. For
   instructions, see [Creating Your First IAM user and Administrators
   Group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the
   _IAM User Guide_.
2. As a user, you can sign in to the AWS Management Console using a
   special URL. For more information, [How Users Sign In to Your Account](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
   _IAM User Guide_.

For more information about IAM, see the following:

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/")
- [Getting started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md")
- [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")

## Grant programmatic access

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Next step

[Step 2: Getting started
(console)](gs-console.md "gs-console.md")
