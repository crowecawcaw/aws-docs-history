# Setting up Amazon SQS

Before you can use Amazon SQS for the first time, you must complete the following steps:

## Step 1: Create an AWS account and IAM user

To access any AWS service, you first need to create an [AWS account](https://aws.amazon.com/ "https://aws.amazon.com/"), an Amazon.com account that can use AWS products. You can
use your AWS account to view your activity and usage reports and to manage
authentication and access.

To avoid using your AWS account root user for Amazon SQS actions, it is a best practice
to create an IAM user for each person who needs administrative access to Amazon SQS.

### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Step 2: Grant programmatic access

To use Amazon SQS actions (for example, using Java or through the AWS Command Line Interface), you need an
access key ID and a secret access key.

###### Note

The access key ID and secret access key are specific to AWS Identity and Access Management. Don't confuse
them with credentials for other AWS services, such as Amazon EC2 key pairs.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM                                                          | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Login for AWS local development](../../../cli/latest/userguide/cli-configure-sign-in.md "../../../cli/latest/userguide/cli-configure-sign-in.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs, see [Login for AWS local development](../../../sdkref/latest/guide/access-login.md "../../../sdkref/latest/guide/access-login.md") in the<br>_AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                                                             |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                                   | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Step 3: Get ready to use the example code

This guide includes examples that use the AWS SDK for Java. To run the example code,
follow the set-up instructions in [Getting Started with
AWS SDK for Java 2.0](../../../sdk-for-java/latest/developer-guide.md "../../../sdk-for-java/latest/developer-guide.md").

You can develop AWS applications in other programming languages, such as Go,
JavaScript, Python and Ruby. For more information, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools/#sdk "https://aws.amazon.com/developer/tools/#sdk").

###### Note

You can explore Amazon SQS without writing code with tools such as the AWS Command Line Interface
(AWS CLI) or Windows PowerShell. You can find AWS CLI examples in the [Amazon SQS section](../../../cli/latest/reference/sqs/index.md "../../../cli/latest/reference/sqs/index.md") of the
_AWS CLI Command Reference_. You can find Windows PowerShell examples
in the Amazon Simple Queue Service section of the _[AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference.md "../../../powershell/latest/reference.md")_.

## Next steps

You are now ready for [Getting started](sqs-getting-started.md "sqs-getting-started.md") with
managing Amazon SQS queues and messages using the AWS Management Console.
