# Getting started with the API

Before you get started with APIs, follow these procedures if you are new to AWS or
need to install the AWS CLI or an AWS SDK. If neither of these apply to you, move to
[Get credentials to grant programmatic
access](#grant-program-access "#grant-program-access").

If you do not have an AWS account, complete the following steps to create
one. Alternatively, you can start building for free with Amazon Nova at [nova.amazon.com/dev](https://nova.amazon.com/dev "https://nova.amazon.com/dev").

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text
message and entering a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root
user_ is created. The root user has access to all AWS
services and resources in the account. As a security best practice,
assign administrative access to a user and use only the root user to
perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").
AWS sends you a confirmation email after the sign-up process is complete. At
any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/")
and choosing **My Account**.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root
   user** and entering your AWS account email address. On
   the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In
User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user
(console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User
Guide_.
To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").

To install an AWS SDK, select the tab that corresponds to the programming
language that you want to use at [Tools to Build on
AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

AWS software development kits (SDKs) are available for many popular
programming languages. Each SDK provides an API, code examples and documentation that make it easier for developers to build applications in their
preferred language. SDKs automatically perform useful tasks for you, such
as:

- Cryptographically sign your service requests
- Retry requests
- Handle error responses

## Get credentials to grant programmatic

access

Users need programmatic access if they want to interact with AWS outside of the
AWS Management Console. The way to grant programmatic access depends on the type
of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which principal needs programmatic access? | To                                                                                                                  | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM users                                  | Limit the duration of long-term credentials to sign programmatic<br>requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to<br>use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md")<br>in the _AWS Command Line Interface User<br>Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in<br>the _AWS SDKs and Tools Reference<br>Guide_.<br>• For AWS APIs, see [Managing access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the<br>_IAM User Guide_. |
| IAM roles                                  | Use temporary credentials to sign programmatic requests to the<br>AWS CLI, AWS SDKs, or AWS APIs.                   | Follow the instructions in [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the<br>_IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Users managed in IAM Identity Center       | Use temporary credentials to sign programmatic requests to the<br>AWS CLI, AWS SDKs, or AWS APIs.                   | Following the instructions for the interface that you want to<br>use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use IAM Identity<br>Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line<br>Interface User Guide_.<br>• For AWS SDKs, tools and AWS APIs, see [IAM Identity Center authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the<br>_AWS SDKs and Tools Reference<br>Guide_.                                                                                                                                                                                                                               |

## Attach Amazon Bedrock permissions to a user or

role

After setting up credentials for programmatic access, you need to configure
permissions for a user or IAM role to have access to Amazon Bedrock-related actions. To set
up these permissions, do the following:

1. On the AWS Management Console Home page, select the IAM service or
   navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Select **Users** or **Roles** and then
   select your user or role.
3. In the **Permissions** tab, choose **Add
   permissions** and then choose **Add AWS managed
   policy**. Choose the [AmazonBedrockFullAccess](../../../bedrock/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess "../../../bedrock/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockFullAccess") AWS managed policy.
4. To allow the user or role to subscribe to models, choose **Create
   inline policy** and then specify the following permissions in
   the JSON editor:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "MarketplaceBedrock",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ViewSubscriptions",
        "aws-marketplace:Unsubscribe",
        "aws-marketplace:Subscribe"
      ],
      "Resource": "*"
    }
  ]
}
```

## Generate a response for a text prompt using an

Amazon Nova model

After you've fulfilled all the prerequisites, you can test making model invocation
requests to Amazon Nova models with a [Converse](../../../bedrock/latest/APIReference/API_runtime_Converse.md "../../../bedrock/latest/APIReference/API_runtime_Converse.md") request.

To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). Verify that
you've set up your credentials to use Boto3 by following the steps at [Get credentials to grant programmatic
access](#grant-program-access "#grant-program-access").

To generate a response for a text prompt in Nova 2 Lite by using the
AWS CLI, run the following command in a terminal:

```
aws bedrock-runtime converse \
  --model-id us.amazon.nova-2-lite-v1:0 \
  --messages '[{"role":"user","content":[{"text":"Write a short poem"}]}]' \
  --additional-model-request-fields '{"reasoningConfig":{"type":"enabled","maxReasoningEffort":"low"}}'
```
