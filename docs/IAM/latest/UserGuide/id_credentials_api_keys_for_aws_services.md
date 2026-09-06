

# API keys for AWS services
<a name="id_credentials_api_keys_for_aws_services"></a>

Some AWS services support API keys for authenticating programmatic requests in addition to standard IAM credentials such as temporary security credentials and long-term access keys. AWS offers two types of API keys:
+ **Long-term API keys** – Long-term API keys are associated with an IAM user and generated using IAM [service-specific credentials](id_credentials_service-specific-creds.md). These credentials are designed for use with only a single AWS service, enhancing security by limiting credential scope. You can set an expiration time for when the long-term API key expires. To generate long-term API keys, you can use the IAM or service-specific console, the AWS CLI, or AWS API.
+ **Short-term API keys** – A short-term API key is a pre-signed URL that uses AWS Signature Version 4. Short-term API keys share the same permissions and expiration as the credentials of the identity that generates the API key and are valid for up to 12 hours or the remaining time of your console session, whichever is shorter. You can use the Amazon Bedrock/Claude Platform on AWS console, Python, and packages for other programming languages to generate short-term API keys. For more information, see [Generate Amazon Bedrock API keys for easy access to the Amazon Bedrock API](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) in the *Amazon Bedrock User Guide* and [Authentication](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html) in the *Claude Platform on AWS User Guide*.

**Note**  
Long-term API keys have a higher security risk compared to short-term API keys. We recommend using short-term API keys or temporary security credentials when possible. If you use long-term API keys, we recommend implementing regular key rotation practices.

## Services that support API keys
<a name="id_credentials_api_keys_supported_services"></a>

The following table lists the AWS services that support API keys and the type of API key each service supports.


| \# | Service | Long-term API keys | Short-term API keys | Managed policy auto-attached | Service-specific documentation | 
| --- | --- | --- | --- | --- | --- | 
| 1 | Amazon Bedrock | Yes | Yes | [AmazonBedrockLimitedAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockLimitedAccess.html) | [Use an Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-use.html) | 
| 2 | Claude Platform on AWS | Yes | Yes | [AnthropicInferenceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AnthropicInferenceAccess.html) | [Authentication](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html) | 
| 3 | Amazon CloudWatch | Yes | N/A | [CloudWatchAPIKeyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.html) | [Setting up bearer token authentication for Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-MetricsBearerTokenAuth.html) | 
| 4 | Amazon CloudWatch Logs | Yes | N/A | [CloudWatchLogsAPIKeyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.html) | [Setting up bearer token authentication](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints_BearerTokenAuth.html) | 

When you generate a long-term API key for a service, the corresponding AWS managed policy is automatically attached to the IAM user, granting access to core operations for that service. If you require additional access, you can modify the permissions for the IAM user. For information about modifying permissions, see [Adding and removing IAM identity permissions](access_policies_manage-attach-detach.md).

To learn more about API keys for specific services, refer to the Service-specific documentation links in the table above.

## Prerequisites for long-term API keys
<a name="id_credentials_api_keys_prerequisites"></a>

Before you can generate a long-term API key in the IAM console, you must meet these prerequisites:
+ An IAM user to associate with the long-term API key. For instructions on creating an IAM user, see [Create an IAM user in your AWS account](id_users_create.md).
+ You must have the following IAM policy permissions to manage service-specific credentials for an IAM user. The example policy grants permission to create, list, update, delete, and reset service-specific credentials. Replace the `{{username}}` value in the Resource element with the name of the IAM user you will generate long-term API keys for:

------
#### [ JSON ]

****  

  ```
  {
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
              "Resource": "arn:aws:iam::*:user/{{username}}"
          }
      ]
  }
  ```

------

## Generating a long-term API key (console)
<a name="id_credentials_api_keys_console_create"></a>

**To generate a long-term API key for a specific service in the IAM console**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Users**.

1. Choose the IAM user you want to generate a long-term API key for.

1. Choose the **Security credentials** tab.

1. In the **API keys** section, choose **Generate API key**.

1. From the **AWS service** dropdown list, choose the service that you want the API key to authenticate to.

1. For **API key expiration**, do one of the following:
   + Choose an API key expiration duration of **1**, **5**, **30**, **90**, or **365** days.
   + Choose **Custom duration** to specify a custom API key expiration date.
   + Choose **Never expires** (not recommended).

1. Choose **Generate API key**.

1. Copy or download your API key. This is the only time you can view the API key value.
**Important**  
Store your API key securely. After you close the dialog box, you cannot retrieve the API key again. If you lose or forget your API key, you cannot retrieve it. Instead, generate a new API key and make the old key inactive.

## Generating a long-term API key (AWS CLI)
<a name="id_credentials_api_keys_cli_create"></a>

To generate a long-term API key using the AWS CLI, use the following steps:

1. Create an IAM user that will be used with the service using the [ create-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-user.html) command:

   ```
   aws iam create-user \
       --user-name {{APIKeyUser_1}}
   ```

1. Attach the AWS managed policy to the IAM user using the [ attach-user-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/attach-user-policy.html) command.

   For Amazon Bedrock:

   ```
   aws iam attach-user-policy --user-name {{APIKeyUser_1}} \
       --policy-arn arn:aws:iam::aws:policy/AmazonBedrockLimitedAccess
   ```

   For Claude Platform on AWS:

   ```
   aws iam attach-user-policy --user-name {{APIKeyUser_1}} \
       --policy-arn arn:aws:iam::aws:policy/AnthropicInferenceAccess
   ```

   For Amazon CloudWatch:

   ```
   aws iam attach-user-policy --user-name {{APIKeyUser_1}} \
       --policy-arn arn:aws:iam::aws:policy/CloudWatchAPIKeyAccess
   ```

   For Amazon CloudWatch Logs:

   ```
   aws iam attach-user-policy --user-name {{APIKeyUser_1}} \
       --policy-arn arn:aws:iam::aws:policy/CloudWatchLogsAPIKeyAccess
   ```

1. Generate the long-term API key using the [ create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html) command.

   For Amazon Bedrock:

   ```
   aws iam create-service-specific-credential \
       --user-name {{APIKeyUser_1}} \
       --service-name bedrock.amazonaws.com \
       --credential-age-days {{30}}
   ```

   For Claude Platform on AWS:

   ```
   aws iam create-service-specific-credential \
       --user-name {{APIKeyUser_1}} \
       --service-name aws-external-anthropic.amazonaws.com \
       --credential-age-days {{30}}
   ```

   For Amazon CloudWatch:

   ```
   aws iam create-service-specific-credential \
       --user-name {{APIKeyUser_1}} \
       --service-name cloudwatch.amazonaws.com \
       --credential-age-days {{30}}
   ```

   For Amazon CloudWatch Logs:

   ```
   aws iam create-service-specific-credential \
       --user-name {{APIKeyUser_1}} \
       --service-name logs.amazonaws.com \
       --credential-age-days {{30}}
   ```
**Note**  
The `--credential-age-days` parameter is optional. You can specify a value between 1–36600 days. If you omit this parameter, the API key does not expire.

The returned `ServiceApiKeyValue` in the response is your long-term API key for the respective service. Store the `ServiceApiKeyValue` value securely, as you cannot retrieve it later.

### List long-term API keys (AWS CLI)
<a name="id_credentials_api_keys_cli_list"></a>

To list long-term API keys metadata for a specific user, use the [ list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html) command with the `--user-name` parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --user-name {{APIKeyUser_1}}
```

**Note**  
Replace `bedrock.amazonaws.com` with the appropriate service name (for example, `logs.amazonaws.com` for Amazon CloudWatch Logs or `aws-external-anthropic.amazonaws.com` for Claude Platform on AWS).

To list all long-term API keys metadata in the account, use the [ list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html) command with the `--all-users` parameter:

```
aws iam list-service-specific-credentials \
    --service-name bedrock.amazonaws.com \
    --all-users
```

### Update long-term API key status (AWS CLI)
<a name="id_credentials_api_keys_cli_update"></a>

To update the status of a long-term API key, use the [ update-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html) command:

```
aws iam update-service-specific-credential \
    --user-name "{{APIKeyUser_1}}" \
    --service-specific-credential-id "{{ACCA1234EXAMPLE1234}}" \
    --status {{Inactive|Active}}
```

## Generating a long-term API key (AWS API)
<a name="id_credentials_api_keys_api"></a>

You can use the following IAM API operations to manage long-term API keys for any supported service:
+  [CreateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html) 
+  [ListServiceSpecificCredentials](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServiceSpecificCredentials.html) 
+  [UpdateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateServiceSpecificCredential.html) 
+  [DeleteServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteServiceSpecificCredential.html) 
+  [ResetServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html) 

## Short-term API keys (select services)
<a name="id_credentials_api_keys_short_term"></a>

Short-term API keys are currently supported by select services.

For information on generating and using short-term API keys with Amazon Bedrock, see [Generate an API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-generate.html) in the *Amazon Bedrock User Guide*.

For information on generating and using short-term API keys for Claude Platform on AWS, see [Authentication](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html) in the *Claude Platform on AWS User Guide*.

## Service-specific information
<a name="id_credentials_api_keys_service_info"></a>
+ For more information about using API keys with Amazon Bedrock, see [Use an Amazon Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys-use.html) in the *Amazon Bedrock User Guide*.
+ For more information about using API keys with Claude Platform on AWS, see [Authentication](https://docs.aws.amazon.com/claude-platform/latest/userguide/authentication.html) in the *Claude Platform on AWS User Guide*.
+ For more information about using API keys with Amazon CloudWatch, see [Setting up bearer token authentication for Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLP-MetricsBearerTokenAuth.html) in the *Amazon CloudWatch User Guide*.
+ For more information about using API keys with Amazon CloudWatch Logs, see [Setting up bearer token authentication](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_HTTP_Endpoints_BearerTokenAuth.html) in the *Amazon CloudWatch Logs User Guide*.