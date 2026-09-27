

# Getting started with the API
<a name="getting-started-api"></a>

Before you get started with APIs, follow these procedures if you are new to AWS or need to install the AWS CLI or an AWS SDK. If neither of these apply to you, move to [Get credentials to grant programmatic access](#grant-program-access).

## I'm new to AWS
<a name="new-to-aws"></a>

If you do not have an AWS account, create one before you continue. Alternatively, you can start building for free with Amazon Nova at [nova.amazon.com/dev](https://nova.amazon.com/dev).

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## I need to install the AWS CLI or an AWS SDK
<a name="install-cli-sdk"></a>

To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

To install an AWS SDK, select the tab that corresponds to the programming language that you want to use at [Tools to Build on AWS](https://aws.amazon.com/developer/tools/).

AWS software development kits (SDKs) are available for many popular programming languages. Each SDK provides an API, code examples and documentation that make it easier for developers to build applications in their preferred language. SDKs automatically perform useful tasks for you, such as:
+ Cryptographically sign your service requests
+ Retry requests
+ Handle error responses

## Get credentials to grant programmatic access
<a name="grant-program-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.


| Which principal needs programmatic access? | To | By | 
| --- | --- | --- | 
| IAM users | Limit the duration of long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. +  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.   | 
| IAM roles | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Follow the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. | 
| Users managed in IAM Identity Center | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. +  For the AWS CLI, see [Configuring the AWS CLI to use IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.   | 

## Attach Amazon Bedrock permissions to a user or role
<a name="attach-permissions"></a>

After setting up credentials for programmatic access, you need to configure permissions for a user or IAM role to have access to Amazon Bedrock-related actions. To set up these permissions, do the following:

1. On the AWS Management Console Home page, select the IAM service or navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Select **Users** or **Roles** and then select your user or role.

1. In the **Permissions** tab, choose **Add permissions** and then choose **Add AWS managed policy**. Choose the [AmazonBedrockFullAccess](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockFullAccess) AWS managed policy.

1. To allow the user or role to subscribe to models, choose **Create inline policy** and then specify the following permissions in the JSON editor:

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

## Generate a response for a text prompt using an Amazon Nova model
<a name="generate-response"></a>

After you've fulfilled all the prerequisites, you can test making model invocation requests to Amazon Nova models with a [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) request.

To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Verify that you've set up your credentials to use Boto3 by following the steps at [Get credentials to grant programmatic access](#grant-program-access).

To generate a response for a text prompt in Nova 2 Lite by using the AWS CLI, run the following command in a terminal:

```
aws bedrock-runtime converse \
  --model-id us.amazon.nova-2-lite-v1:0 \
  --messages '[{"role":"user","content":[{"text":"Write a short poem"}]}]' \
  --additional-model-request-fields '{"reasoningConfig":{"type":"enabled","maxReasoningEffort":"low"}}'
```