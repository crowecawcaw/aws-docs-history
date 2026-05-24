# Set up to use AWS Cloud Map

The overview and procedures in the following sections are meant to help you get started with
AWS and prepare you to start using AWS Cloud Map.

###### Topics

- [Sign Up for AWS](#setting-up-sign-up-for-aws "#setting-up-sign-up-for-aws")
- [Access the API, AWS CLI, AWS Tools for Windows PowerShell, or the AWS SDKs](#setting-up-access-account-api-cli "#setting-up-access-account-api-cli")
- [Set Up the AWS Command Line Interface or AWS Tools for Windows PowerShell](#setting-up-aws-cli "#setting-up-aws-cli")
- [Download an AWS SDK](#setting-up-sdk "#setting-up-sdk")

## Sign Up for AWS

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Access the API, AWS CLI, AWS Tools for Windows PowerShell, or the AWS SDKs

To use the API, the AWS CLI, AWS Tools for Windows PowerShell, or the AWS SDKs, you must create _access
keys_. These keys consist of an access key ID and secret access key, which are used
to sign programmatic requests that you make to AWS.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Set Up the AWS Command Line Interface or AWS Tools for Windows PowerShell

The AWS Command Line Interface (AWS CLI) is a unified tool for managing AWS services. For information about
how to install and configure the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

If you have experience with Windows PowerShell, you might prefer to use AWS Tools for Windows PowerShell. For more
information, see [Setting up the
AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md") in the _AWS Tools for PowerShell User Guide_.

## Download an AWS SDK

If you're using a programming language that AWS provides an SDK for, we recommend that you
use an SDK instead of the AWS Cloud Map API. Using an SDK has several benefits. SDKs make
authentication simpler, integrate easily with your development environment, and provide access to
AWS Cloud Map commands. For more information, see [Tools for
Amazon Web Services](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").
