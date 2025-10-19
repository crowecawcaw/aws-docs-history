# Setting up AWS Cloud Control API

To use AWS Cloud Control API, you'll need to have an AWS account in which you have set yourself up as
 an AWS Identity and Access Management (IAM) administrator user.

###### Topics

* [Sign up for AWS](#setting-up-aws-sign-up "#setting-up-aws-sign-up")
* [Create an IAM user](#setting-up-create-iam-user "#setting-up-create-iam-user")

## Sign up for AWS


If you do not have an AWS account, complete the following steps to create one.


###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.


Part of the sign-up procedure involves receiving a phone call or text message and entering 
 a verification code on the phone keypad.


When you sign up for an AWS account, an *AWS account root user* is created. The root user has access to all AWS services
 and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks").

## Create an IAM user


To create an administrator user, choose one of the following options.




| Choose one way to manage your administrator | To | By | You can also |
| --- | --- | --- | --- |
| In IAM Identity Center (Recommended) | Use short-term credentials to access AWS.This aligns with the security best practices. For information about best practices, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp") in the *IAM User Guide*. | Following the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the *AWS IAM Identity Center User Guide*. | Configure programmatic access by [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html") in the *AWS Command Line Interface User Guide*. |
| In IAM (Not recommended) | Use long-term credentials to access AWS. | Following the instructions in [Create an IAM user for emergency access](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-emergency-iam-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started-emergency-iam-user.html") in the *IAM User Guide*. | Configure programmatic access by [Manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html") in the *IAM User Guide*. |
