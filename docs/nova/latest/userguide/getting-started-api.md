

# Getting started with the API
<a name="getting-started-api"></a>

**Note**  
This documentation is for Amazon Nova Version 1. Amazon Nova 2 is now available with new models and enhanced capabilities. For information on how to get started with Amazon Nova 2, visit [Getting started with the API](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-api.html).

To get started with the API, you need credentials to grant programmatic access. If the following sections pertain to you, expand them and follow the instructions. Otherwise, proceed through the remaining sections.

## I'm new to AWS
<a name="new-to-aws"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## I need to install the AWS CLI or an AWS SDK
<a name="api-cli-sdk-install"></a>

To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

To install an AWS SDK, select the tab that corresponds to the programming language that you want to use at [Tools to Build on AWS](https://aws.amazon.com/developer/tools/). AWS software development kits (SDKs) are available for many popular programming languages. Each SDK provides an API, code examples, and documentation that make it easier for developers to build applications in their preferred language. SDKs automatically perform useful tasks for you, such as:
+ Cryptographically sign your service requests
+ Retry requests
+ Handle error responses

## Get credentials to grant programmatic access
<a name="grant-program-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.



| Which principal needs programmatic access? | To | By | 
| --- | --- | --- | 
| IAM users | Limit the duration of long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Authenticating using IAM user credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs and tools, see [Authenticate using long-term credentials](https://docs.aws.amazon.com/sdkref/latest/guide/access-iam-users.html) in the *AWS SDKs and Tools Reference Guide*. <br />+  For AWS APIs, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) in the *IAM User Guide*.  | 
| IAM roles | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. | 
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.+  For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html) in the *AWS Command Line Interface User Guide*. <br />+  For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) in the *AWS SDKs and Tools Reference Guide*.  | 

## How to configure access keys for an IAM user
<a name="create-user-time-bound"></a>

If you decide to use access keys for an IAM user, AWS recommends that you set an expiration for the IAM user by including a restrictive inline policy.

**Important**  
Heed the following warnings:  
**Do NOT** use your account's root credentials to access AWS resources. These credentials provide unrestricted account access and are difficult to revoke.
**Do NOT** put literal access keys or credential information in your application files. If you do, you create a risk of accidentally exposing your credentials if, for example, you upload the project to a public repository.
**Do NOT** include files that contain credentials in your project area.
Manage your access keys securely. Do not provide your access keys to unauthorized parties, even to help [find your account identifiers](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html). By doing this, you might give someone permanent access to your account.
Be aware that any credentials stored in the shared AWS credentials file are stored in plaintext.

For more details, see [Best practices for managing AWS access keys](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) in the AWS General Reference.

**Create an IAM user**

1. On the AWS Management Console Home page, select the IAM service or navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, select **Users** and then select **Create user**.

1. Follow the guidance in the IAM console to set up a programmatic user (without access to the AWS Management Console) and without permissions.

**Restrict user access to a limited time window**

Any IAM user access keys that you create are long-term credentials. To ensure that these credentials expire in case they are mishandled, you can make these credentials time-bound by creating an inline policy that specifies a date after which the keys will no longer be valid.

1. Open the IAM user that you just created. In the **Permissions** tab, choose **Add permissions** and then choose **Create inline policy**.

1. In the JSON editor, specify the following permissions. To use this policy, replace the value for `aws:CurrentTime` timestamp value in the example policy with your own end date.
**Note**  
IAM recommends that you limit your access keys to 12 hours.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Deny",
         "Action": "*",
         "Resource": "*",
         "Condition": {
           "DateGreaterThan": {
             "aws:CurrentTime": "{{2024-01-01T00:00:00Z}}"
           }
         }
       }
     ]
   }
   ```

------

**Create an access key**

1. On the **User details** page, select the **Security credentials** tab. In the **Access keys** section, choose **Create access key**.

1. Indicate that you plan to use these access keys as **Other** and choose **Create access key**.

1. On the **Retrieve access key** page, choose **Show** to reveal the value of your user's secret access key. You can copy the credentials or download a .csv file.

**Important**  
When you no longer need this IAM user, we recommend that you remove it and align with the [AWS security best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials), we recommend that you require your human users to use temporary credentials through [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) when accessing AWS.

## Attach Amazon Bedrock permissions to a user or role
<a name="br-permissions"></a>

After setting up credentials for programmatic access, you need to configure permissions for a user or IAM role to have access a set of Amazon Bedrock-related actions. To set up these permissions, do the following:

1. On the AWS Management Console Home page, select the IAM service or navigate to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Select **Users** or **Roles** and then select your user or role.

1. In the **Permissions** tab, choose **Add permissions** and then choose **Add AWS managed policy**. Choose the [AmazonBedrockFullAccess]() AWS managed policy.

1. To allow the user or role to subscribe to models, choose **Create inline policy** and then specify the following permissions in the JSON editor:

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
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

------

## Request access to Amazon Nova models
<a name="request-access-nova"></a>

Request access to the Amazon Nova models through the Amazon Bedrock console by following the steps at [Request access to an Amazon Bedrock foundation model](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html#getting-started-model-access).

## Generate a response for a text prompt using an Amazon Nova model
<a name="try-nova"></a>

After you've fulfilled all the prerequisites, select a tab to test out making model invocation requests to Amazon Nova models with a [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) request and using the method specified in the tab:

------
#### [ AWS CLI ]

To install the AWS CLI, follow the steps at [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Verify that you've set up your credentials to use Boto3 by following the steps at [Get credentials to grant programmatic access](#grant-program-access).

To generate a response for a text prompt in Amazon Nova Lite by using the AWS CLI, run the following command in a terminal:

```
aws bedrock-runtime converse \
    --model-id us.amazon.nova-lite-v1:0 \
    --messages '[{"role": "user", "content": [{"text": "Write a short poem"}]}]'
```

------
#### [ Python (Boto3) ]

To install Boto3, follow the steps at [Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html) in the Boto3 documentation. Verify that you've set up your credentials to use Boto3 by following the steps at [Get credentials to grant programmatic access](#grant-program-access).

To create an Amazon Bedrock Runtime client and generate a response for a text prompt in Amazon Nova Lite by using the Python SDK (Boto3), run the following Python script:

```
import boto3
import json

client = boto3.client(service_name="bedrock-runtime")

messages = [
    {"role": "user", "content": [{"text": "Write a short poem"}]},
]

model_response = client.converse(
    modelId="us.amazon.nova-lite-v1:0", 
    messages=messages
)

print("\n[Full Response]")
print(json.dumps(model_response, indent=2))

print("\n[Response Content Text]")
print(model_response["output"]["message"]["content"][0]["text"])
```

------
#### [ LangChain ]

To install LangChain for AWS, follow the steps at [AWS](https://python.langchain.com/docs/integrations/providers/aws/) in the LangChain documentation. Verify that you've set up your credentials to use Boto3 by following the steps at [Get credentials to grant programmatic access](#grant-program-access).

To generate a response for a text prompt in Amazon Nova Lite by using LangChain, run the following script:

```
from langchain_aws import ChatBedrockConverse

llm = ChatBedrockConverse(model="us.amazon.nova-lite-v1:0")

messages = [
    ("user", "Write a short poem")
]

llm.invoke(messages)
```

------

After you've familiarized yourself with Amazon Nova, you can proceed to more advanced tasks:

1. Try prompting the model to describe an image or a video. For more information, see [Multimodal support for Amazon Nova](modalities.md).

1. Try generating images using Amazon Nova Canvas. For more information, see [Generating images with Amazon Nova Canvas](image-generation.md).

1. Try generating videos using Amazon Nova Reel. For more information, see [Generating videos with Amazon Nova Reel](video-generation.md).

1. Send the model a document and ask about its content. For more information, see [Document understanding](modalities-document.md).

1. Provide the model with tools and make a request with a prompt to see it use the tool. For more information, see [Tool use (function calling) with Amazon Nova](tool-use.md).