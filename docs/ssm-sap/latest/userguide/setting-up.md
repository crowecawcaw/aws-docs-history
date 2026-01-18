# Setting up Systems Manager for SAP

If you are new to AWS, begin with the following topics. When you sign up for AWS, your AWS account is automatically signed up for all services in AWS, including Systems Manager for SAP.

###### Topics

- [Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
- [Create an IAM user](#setting-up-create-iam-user "#setting-up-create-iam-user")

## Sign up for AWS

###### To sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

1. Open https://portal.aws.amazon.com/billing/signup.
2. Follow the online instructions.

Part of the sign-up procedure involves email verification and either receiving a phone call or SMS to enter a verification code.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

## Create an IAM user

To create an administrator user, choose one of the following options.

| Choose one way to manage your administrator | To                                                                                                                                                                                                                                                                                                                                                | By                                                                                                                                                                                                                                          | You can also                                                                                                                                                                                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In IAM Identity Center<br>(Recommended)     | Use short-term credentials to access AWS.<br>This aligns with the security best practices. For information about best practices, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity Center User Guide_.                         | Configure programmatic access by [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. |
| In IAM<br>(Not recommended)                 | Use long-term credentials to access AWS.                                                                                                                                                                                                                                                                                                          | Following the instructions in [Create an IAM user for emergency access](../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md "../../../IAM/latest/UserGuide/getting-started-emergency-iam-user.md") in the _IAM User Guide_. | Configure programmatic access by [Manage access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_.                            |
