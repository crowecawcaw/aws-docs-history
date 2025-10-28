# API keys for Amazon Bedrock

Amazon Bedrock is a fully managed service that offers foundation models from leading AI companies
and Amazon. You can access Amazon Bedrock through the AWS Management Console and programmatically using the AWS CLI, or
AWS API. When making programmatic requests to Amazon Bedrock, you can authenticate using either [temporary
security credentials](id_credentials_temp_request.md "id_credentials_temp_request.md") or Amazon Bedrock API keys. Amazon Bedrock supports two types of API keys:

- **Short-term API keys** – A short-term API key is a
  pre-signed URL that uses AWS Signature Version 4. Short-term API keys share the same
  permissions and expiration as the credentials of the identity that generates the API key and
  are valid for up to 12 hours or the remaining time of your console session, whichever is
  shorter. You can use the Amazon Bedrock console, Python package
  `aws-bedrock-token-generator`, and packages for other programming languages to
  generate short-term API keys. For more information, see [Generate Amazon Bedrock API keys for easy access to
  the Amazon Bedrock API](../../../bedrock/latest/userguide/api-keys.md "../../../bedrock/latest/userguide/api-keys.md") in the _Amazon Bedrock User Guide_.
- **Long-term API keys** – Long-term API keys are
  associated with an IAM user and generated using IAM [service-specific credentials](id_credentials_service-specific-creds.md "id_credentials_service-specific-creds.md"). These
  credentials are designed for use with only Amazon Bedrock, enhancing security by limiting credential
  scope. You can set an expiration time for when the long-term API key expires. You can use
  the IAM or Amazon Bedrock console, the AWS CLI, or the AWS API to generate long-term API
  keys.
  An IAM user can have up to two long-term API keys for Amazon Bedrock, which help you implement
  secure key rotation practices.

When you generate a long-term API key, the AWS managed policy [AmazonBedrockLimitedAccess](../../../bedrock/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockLimitedAccess "../../../bedrock/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonBedrockLimitedAccess") is automatically attached to the IAM user. This policy
grants access to core Amazon Bedrock API operations. If you require additional Amazon Bedrock access, you can modify
the permissions for the IAM user. For information about modifying permissions, see [Adding and removing IAM identity
permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md"). For more information about how to use an
Amazon Bedrock key, see [Use
an Amazon Bedrock API key](../../../bedrock/latest/userguide/api-keys-use.md "../../../bedrock/latest/userguide/api-keys-use.md") in the _Amazon Bedrock User Guide_.

###### Note

Long-term API keys have a higher security risk compared to short-term API keys. We
recommend using short-term API keys or temporary security credentials when possible. If you
use long-term API keys, we recommend implementing regular key rotation practices.

## Prerequisites

Before you can generate an Amazon Bedrock long-term API key from the IAM console, you must meet
these prerequisites:

- An IAM user to associate with the long-term API key. For instructions on creating an
  IAM user, see [Create an IAM user in your AWS account](id_users_create.md "id_users_create.md").
- Ensure you have the following IAM policy permissions to manage service-specific
  credentials for an IAM user. The example policy grants permission to create, list,
  update, delete, and reset service-specific credentials. Replace the
  `username` value in the Resource element with
  the name of the IAM user you will generate Amazon Bedrock API keys for:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ManageBedrockServiceSpecificCredentials",
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceSpecificCredential",
 "iam:ListServiceSpecificCredentials",
 "iam:UpdateServiceSpecificCredential",
 "iam:DeleteServiceSpecificCredential",
 "iam:ResetServiceSpecificCredential"
 ],
 "Resource": "arn:aws:iam::*:user/`username`"
 }
 ]
}`

```

## Generating a long-term API Key for

Amazon Bedrock (console)

###### To generate an Amazon Bedrock long-term API key (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Users**.
3. Select the IAM user you want to generate Amazon Bedrock long-term API keys for.
4. Choose the tab **Security credentials**.
5. In the section **API keys for Amazon Bedrock**, choose **Generate API
   Key**.
6. For **API key expiration**, do one of the following:
   - Select an API key expiration duration of **1**,
     **5** , **30**, **90**, or
     **365** days.
   - Choose **Custom duration** to specify a custom API key expiration
     date.
   - Select **Never expires** (not recommended)

7. Choose **Generate API key**.
8. Copy or download your API key. This is the only time you can view the API key
   value.

###### Important

Store your API key securely. After you close the dialog box, you cannot retrieve the
API key again. If you lose or forget your secret access key, you cannot retrieve it.
Instead, create a new access key and make the old key inactive.

## Generating a long-term API Key for Amazon Bedrock

(AWS CLI)

To generate an Amazon Bedrock long-term API key using the AWS CLI, use the following steps:

1. Create an IAM user that will be used with Amazon Bedrock using the [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html") command:

```
aws iam create-user \
    --user-name `BedrockAPIKey_1`
```

2. Attach the AWS managed policy `AmazonBedrockLimitedAccess` to the Amazon Bedrock
   IAM user using the [attach-user-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html") command:

```
aws iam attach-user-policy --user-name `BedrockAPIKey_1` \
    --policy-arn arn:aws:iam::aws:policy/AmazonBedrockLimitedAccess
```

3. Generate the Amazon Bedrock long-term API key using the [create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html") command. For the credential age, you can
   specify a value between 1-36600 days. If you don't specify a credential age, the API key
   will not expire.

To generate a long-term API key with an expiration of 30 days:

```
aws iam create-service-specific-credential \
    --user-name `BedrockAPIKey_1` \
    --service-name bedrock.amazonaws.com \
    --credential-age-days `30`
```

The returned `ServiceApiKeyValue` in the response is your long-term Amazon Bedrock API
key. Store the `ServiceApiKeyValue` value securely, as you cannot retrieve it
later.

### List long-term API keys (AWS CLI)

To list Amazon Bedrock long-term API keys metadata for a specific user, use the [list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html") command with the `--user-name`
parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --user-name `BedrockAPIKey_1`
```

To list all Amazon Bedrock long-term API keys metadata in the account, use the [list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html") command with the `--all-users`
parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --all-users
```

### Update long-term API key status

(AWS CLI)

To update the status of a long-term API key for Amazon Bedrock, use the [update-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html") command:

```
aws iam update-service-specific-credential \
    --user-name "`BedrockAPIKey_1`" \
    --service-specific-credential-id "`ACCA1234EXAMPLE1234`" \
    --status `Inactive|Active`
```

## Generating a long-term API Key for Amazon Bedrock (AWS

API)

You can use the following API operations to generate and manage long-term API keys for
Amazon Bedrock:

- [CreateServiceSpecificCredential](../APIReference/API_CreateServiceSpecificCredential.md "../APIReference/API_CreateServiceSpecificCredential.md")
- [ListServiceSpecificCredentials](../APIReference/API_ListServiceSpecificCredentials.md "../APIReference/API_ListServiceSpecificCredentials.md")
- [UpdateServiceSpecificCredential](../APIReference/API_UpdateServiceSpecificCredential.md "../APIReference/API_UpdateServiceSpecificCredential.md")
- [DeleteServiceSpecificCredential](../APIReference/API_DeleteServiceSpecificCredential.md "../APIReference/API_DeleteServiceSpecificCredential.md")
- [ResetServiceSpecificCredential](../APIReference/API_ResetServiceSpecificCredential.md "../APIReference/API_ResetServiceSpecificCredential.md")
