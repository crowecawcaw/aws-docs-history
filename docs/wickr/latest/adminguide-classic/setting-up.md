This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Setting up for AWS Wickr

If you're a new AWS customer, complete the setup prerequisites that are listed on this page
before you start using AWS Wickr. For these setup procedures, you use the AWS Identity and Access Management (IAM)
service. For complete information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

###### Topics

- [Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
- [Create an IAM user](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [What's next](#setting-up.next "#setting-up.next")

## Sign up for AWS

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an IAM user

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                  | By                                                                                                                                                                                                                                                       | You can also                                                                                                                                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center (Recommended)        | Use short-term credentials to access AWS.This aligns with the security best<br>practices. For information about best practices, see [Security best<br>practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the<br>_AWS IAM Identity Center User Guide_.                                   | Configure programmatic access by [Configuring the AWS CLI to use<br>AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM (Not recommended)                    | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                            | Following the instructions in [Creating your first IAM<br>admin user and user group](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md") in the _IAM User Guide_. | Configure programmatic access by [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                          |

###### Note

You can also assign the `AWSWickrFullAccess` managed policy to grant full
administrative permission to the Wickr service. For more information, see [AWS managed policy:
AWSWickrFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSWickrFullAccess").

## What's next

You completed the prerequisite set up steps. To begin configuring Wickr, see [Getting started with AWS Wickr](getting-started.md "getting-started.md").
