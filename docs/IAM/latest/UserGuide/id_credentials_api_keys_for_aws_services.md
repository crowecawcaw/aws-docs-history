# API keys for AWS services

You can access AWS services through the AWS Management Console and programmatically using the AWS CLI or
AWS API. When making programmatic requests to services like Amazon Bedrock and Amazon CloudWatch Logs, you can
authenticate using IAM credentials (for example, temporary security credentials or long-term
access keys) or API keys. There are two types of API keys:

- **Long-term API keys** – Long-term API keys are
  associated with an IAM user and generated using IAM [service-specific credentials](id_credentials_service-specific-creds.md "id_credentials_service-specific-creds.md"). These
  credentials are designed for use with only a single AWS service, enhancing security by
  limiting credential scope. You can set an expiration time for the long-term API key. You can use the IAM or service-specific console (for example, Amazon Bedrock or CloudWatch Logs
  console), the AWS CLI, or AWS API to generate long-term API keys.
- **Short-term API keys** (only supported by Amazon Bedrock)
  – A short-term API key is a pre-signed URL that uses AWS Signature Version 4.
  Short-term API keys share the same permissions and expiration as the credentials of the
  identity that generates the API key and are valid for up to 12 hours or the remaining time
  of your console session, whichever is shorter. You can use the Amazon Bedrock console, Python package
  `aws-bedrock-token-generator`, and packages for other programming languages to
  generate short-term API keys. For more information, see [Generate Amazon Bedrock API keys for easy access to
  the Amazon Bedrock API](../../../bedrock/latest/userguide/api-keys.md "../../../bedrock/latest/userguide/api-keys.md") in the _Amazon Bedrock User Guide_.

###### Note

Long-term API keys have a higher security risk compared to short-term API keys. We
recommend using short-term API keys or temporary security credentials when possible. If you
use long-term API keys, we recommend implementing regular key rotation practices.

## Supported services

The following table lists the AWS services that support API keys and the type of API key
each service supports.

| #   | Service                | Long-term API keys | Short-term API keys | Managed policy auto-attached                                                                                                                                                          |
| --- | ---------------------- | ------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Amazon Bedrock         | Yes                | Yes                 | [AmazonBedrockLimitedAccess](../../../aws-managed-policy/latest/reference/AmazonBedrockLimitedAccess.md "../../../aws-managed-policy/latest/reference/AmazonBedrockLimitedAccess.md") |
| 2   | Amazon CloudWatch Logs | Yes                | N/A                 | [CloudWatchLogsAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md") |

When you generate a long-term API key for a service, the corresponding AWS managed
policy is automatically attached to the IAM user, granting access to core operations for
that service. If you require additional access, you can modify the permissions for the
IAM user. For information about modifying permissions, see [Adding and removing IAM identity permissions](access_policies_manage-attach-detach.md "access_policies_manage-attach-detach.md"). For more information on how to use an Amazon Bedrock
key, see [Use an
Amazon Bedrock API key](../../../bedrock/latest/userguide/api-keys-use.md "../../../bedrock/latest/userguide/api-keys-use.md") in the _Amazon Bedrock User Guide_. For more information on
how to use bearer token for Amazon CloudWatch Logs, see [Bearer token
authentication](../../../AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints_BearerTokenAuth.md "../../../AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints_BearerTokenAuth.md") in the _CloudWatch Logs User Guide_.

## Prerequisites for long-term API keys

Before you can generate a long-term API key in the IAM console, you must meet these
prerequisites:

- An IAM user to associate with the long-term API key. For instructions on creating an
  IAM user, see [Create an IAM user in your AWS account](id_users_create.md "id_users_create.md").
- You must have the following IAM policy permissions to manage service-specific
  credentials for an IAM user. The example policy grants permission to create, list,
  update, delete, and reset service-specific credentials. Replace the
  `username` value in the Resource element with
  the name of the IAM user you will generate long-term API keys for:

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

## Generating a long-term API key (console)

###### To generate a long-term API key for a specific service in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Users**.
3. Choose the IAM user you want to generate a long-term API key for.
4. Choose the **Security credentials** tab.
5. In the **API keys** section, choose **Generate API
   key**.
6. From the **AWS service** dropdown list, choose the service that
   you want the API key to authenticate to.
7. For **API key expiration**, do one of the following:
   - Choose an API key expiration duration of **1**,
     **5**, **30**, **90**, or
     **365** days.
   - Choose **Custom duration** to specify a custom API key expiration
     date.
   - Choose **Never expires** (not recommended).

8. Choose **Generate API key**.
9. Copy or download your API key. This is the only time you can view the API key
   value.

###### Important

Store your API key securely. After you close the dialog box, you cannot retrieve the
API key again. If you lose or forget your API key, you cannot retrieve it.
Instead, generate a new API key and make the old key inactive.

## Generating a long-term API key (AWS CLI)

To generate a long-term API key using the AWS CLI, use the following steps:

1. Create an IAM user that will be used with Amazon Bedrock or Amazon CloudWatch Logs using the [create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html") command:

```
aws iam create-user \
    --user-name `APIKeyUser_1`
```

2. Attach the AWS managed policy to the IAM user using the [attach-user-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html") command.

For Amazon Bedrock:

```
aws iam attach-user-policy --user-name `APIKeyUser_1` \
    --policy-arn arn:aws:iam::aws:policy/AmazonBedrockLimitedAccess
```

For Amazon CloudWatch Logs:

```
aws iam attach-user-policy --user-name `APIKeyUser_1` \
    --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsAPIKeyAccess
```

3. Generate the long-term API key using the [create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html") command.

For Amazon Bedrock:

```
aws iam create-service-specific-credential \
    --user-name `APIKeyUser_1` \
    --service-name bedrock.amazonaws.com \
    --credential-age-days `30`
```

For Amazon CloudWatch Logs:

```
aws iam create-service-specific-credential \
    --user-name `APIKeyUser_1` \
    --service-name logs.amazonaws.com \
    --credential-age-days `30`
```

###### Note

The `--credential-age-days` parameter is optional. You can specify a
value between 1–36600 days. If you omit this parameter, the API key does not
expire.

The returned `ServiceApiKeyValue` in the response is your long-term API key for
the respective service. Store the `ServiceApiKeyValue` value securely, as you
cannot retrieve it later.

### List long-term API keys (AWS CLI)

To list long-term API keys metadata for a specific user, use the [list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html") command with the `--user-name`
parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --user-name `APIKeyUser_1`
```

###### Note

Replace `bedrock.amazonaws.com` with the appropriate service name (for
example, `logs.amazonaws.com` for Amazon CloudWatch Logs).

To list all long-term API keys metadata in the account, use the [list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html") command with the `--all-users`
parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --all-users
```

### Update long-term API key status (AWS CLI)

To update the status of a long-term API key, use the [update-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html") command:

```
aws iam update-service-specific-credential \
    --user-name "`APIKeyUser_1`" \
    --service-specific-credential-id "`ACCA1234EXAMPLE1234`" \
    --status `Inactive|Active`
```

## Generating a long-term API key (AWS API)

You can use the following IAM API operations to manage long-term API keys for any
supported service:

- [CreateServiceSpecificCredential](../APIReference/API_CreateServiceSpecificCredential.md "../APIReference/API_CreateServiceSpecificCredential.md")
- [ListServiceSpecificCredentials](../APIReference/API_ListServiceSpecificCredentials.md "../APIReference/API_ListServiceSpecificCredentials.md")
- [UpdateServiceSpecificCredential](../APIReference/API_UpdateServiceSpecificCredential.md "../APIReference/API_UpdateServiceSpecificCredential.md")
- [DeleteServiceSpecificCredential](../APIReference/API_DeleteServiceSpecificCredential.md "../APIReference/API_DeleteServiceSpecificCredential.md")
- [ResetServiceSpecificCredential](../APIReference/API_ResetServiceSpecificCredential.md "../APIReference/API_ResetServiceSpecificCredential.md")

## Short-term API keys (Amazon Bedrock)

Short-term API keys are currently supported by Amazon Bedrock only. For information on
generating and using short-term API keys, see [Generate an API key](../../../bedrock/latest/userguide/api-keys-generate.md "../../../bedrock/latest/userguide/api-keys-generate.md") in the
_Amazon Bedrock User Guide_.

## Service-specific information

- For more information about using API keys with Amazon Bedrock, see [Use an Amazon Bedrock API
  key](../../../bedrock/latest/userguide/api-keys-use.md "../../../bedrock/latest/userguide/api-keys-use.md") in the _Amazon Bedrock User Guide_.
- For more information about using API keys with Amazon CloudWatch Logs, see [Log ingestion through HTTP
  endpoints](../../../AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints.md "../../../AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints.md") in the _Amazon CloudWatch Logs User Guide_.
