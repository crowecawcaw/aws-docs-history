# Set up to use AWS Cloud Map

The overview and procedures in the following sections are meant to help you get started with
 AWS and prepare you to start using AWS Cloud Map.

###### Topics

* [Sign Up for AWS](#setting-up-sign-up-for-aws "#setting-up-sign-up-for-aws")
* [Access the API, AWS CLI, AWS Tools for Windows PowerShell, or the
 AWS SDKs](#setting-up-access-account-api-cli "#setting-up-access-account-api-cli")
* [Set Up the AWS Command Line Interface or AWS Tools for Windows PowerShell](#setting-up-aws-cli "#setting-up-aws-cli")
* [Download an AWS SDK](#setting-up-sdk "#setting-up-sdk")

## Sign Up for AWS


### Sign up for an AWS account


If you do not have an AWS account, complete the following steps to create one.


###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.


Part of the sign-up procedure involves receiving a phone call or text message and entering 
 a verification code on the phone keypad.


When you sign up for an AWS account, an *AWS account root user* is created. The root user has access to all AWS services
 and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
 Account**.


### Create a user with administrative access


After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you 
don't use the root user for everyday tasks.


###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.


For help signing in by using root user, see [Signing in as the root user](https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial "https://docs.aws.amazon.com/signin/latest/userguide/console-sign-in-tutorials.html#introduction-to-root-user-sign-in-tutorial") in the *AWS Sign-In User Guide*.
2. Turn on multi-factor authentication (MFA) for your root user.


For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/enable-virt-mfa-for-root.html") in the *IAM User Guide*.

###### Create a user with administrative access

1. Enable IAM Identity Center.


For instructions, see [Enabling
 AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
 *AWS IAM Identity Center User Guide*.
2. In IAM Identity Center, grant administrative access to a user.


For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
 *AWS IAM Identity Center User Guide*.

###### Sign in as the user with administrative access

* To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.


For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html "https://docs.aws.amazon.com/signin/latest/userguide/iam-id-center-sign-in-tutorial.html") in the *AWS Sign-In User Guide*.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.


For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the *AWS IAM Identity Center User Guide*.
2. Assign users to a group, and then assign single sign-on access to the group.


For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the *AWS IAM Identity Center User Guide*.

## Access the API, AWS CLI, AWS Tools for Windows PowerShell, or the
 AWS SDKs


To use the API, the AWS CLI, AWS Tools for Windows PowerShell, or the AWS SDKs, you must create *access
 keys*. These keys consist of an access key ID and secret access key, which are used
 to sign programmatic requests that you make to AWS.


Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.


To grant users programmatic access, choose one of the following options.




| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| Workforce identity (Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html") in the *AWS Command Line Interface User Guide*. <br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html "https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html") in the *AWS SDKs and Tools Reference Guide*. |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html") in the *IAM User Guide*. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html") in the *AWS Command Line Interface User Guide*. <br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html "https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html") in the *AWS SDKs and Tools Reference Guide*. <br>• For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html") in the *IAM User Guide*. | ## Set Up the AWS Command Line Interface or AWS Tools for Windows PowerShell The AWS Command Line Interface (AWS CLI) is a unified tool for managing AWS services. For information about how to install and configure the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html") in the *AWS Command Line Interface User Guide*. If you have experience with Windows PowerShell, you might prefer to use AWS Tools for Windows PowerShell. For more information, see [Setting up the AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html "https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html") in the *AWS Tools for PowerShell User Guide*. ## Download an AWS SDK If you're using a programming language that AWS provides an SDK for, we recommend that you use an SDK instead of the AWS Cloud Map API. Using an SDK has several benefits. SDKs make authentication simpler, integrate easily with your development environment, and provide access to AWS Cloud Map commands. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
