# Setting up bearer token authentication

Before you can send logs using bearer token authentication with any of the HTTP ingestion endpoints, you need to:

- Create an IAM user with CloudWatch Logs permissions
- Generate service-specific credentials (bearer token)
- Create a log group and log stream
- Enable bearer token authentication on the log group

###### Note

API key (bearer token) for HTTP endpoint access is currently in preview and available in the following AWS Regions: `us-east-1`, `us-west-1`, `us-west-2`, and `us-east-2`. Please check this documentation for updates in future.

## Option 1: Simplified setup using the AWS console (recommended)

The AWS Management Console provides a streamlined workflow to generate API keys for HTTP endpoint access.

###### To set up HTTP endpoint access using the console

1. Sign in to the AWS Management Console.
2. Navigate to **CloudWatch** > **Settings** > **Logs**.
3. In the API Keys section, choose **Generate API key**.
4. For **API key expiration**, do one of the following:
   - Select an API key expiration duration of **1**, **5**, **30**, **90**, or **365** days.
   - Choose **Custom duration** to specify a custom API key expiration date.
   - Select **Never expires** (not recommended).

5. Choose **Generate API key**.

The console automatically:

    * Creates a new IAM user with appropriate permissions
    * Attaches the [CloudWatchLogsAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md") managed policy (includes `logs:PutLogEvents` and `logs:CallWithBearerToken` permissions)
    * Generates service-specific credentials (API key)

6. Copy and securely save the displayed credentials:
   - **API Key ID** (Service-specific credential ID)
   - **API Key Secret** (Bearer token)

###### Important

Save the API Key Secret immediately. It cannot be retrieved later. If you lose it, you'll need to generate a new API key. 7. Create the log group and log stream where your logs will be stored:

```
# Create the log group
aws logs create-log-group \
    --log-group-name /aws/hlc-logs/my-application \
    --region us-east-1

# Create the log stream
aws logs create-log-stream \
    --log-group-name /aws/hlc-logs/my-application \
    --log-stream-name application-stream-001 \
    --region us-east-1
```

8. Enable bearer token authentication on the log group:

```
aws logs put-bearer-token-authentication \
    --log-group-identifier /aws/hlc-logs/my-application \
    --bearer-token-authentication-enabled \
    --region us-east-1
```

Verify the configuration:

```
aws logs describe-log-groups \
    --log-group-name-prefix /aws/hlc-logs/my-application \
    --region us-east-1
```

**Permissions included:** The automatically created IAM user will have the following permissions:

- `logs:PutLogEvents` – Send log events to CloudWatch Logs
- `logs:CallWithBearerToken` – Authenticate using bearer token
- `kms:Describe*`, `kms:GenerateDataKey*`, `kms:Decrypt` – Access KMS-encrypted log groups (with condition restricting to logs service)

## Option 2: Manual setup

If you prefer more control over the IAM configuration or need to customize permissions, you can set up the HTTP endpoint access manually.

### Step 1: Create an IAM user

Create an IAM user that will be used for log ingestion:

1. Sign in to the AWS Management Console and navigate to IAM.
2. In the left navigation pane, choose **Users**.
3. Choose **Create user**.
4. Enter a user name (for example, `cloudwatch-logs-hlc-user`).
5. Choose **Next**.
6. Attach one of the following IAM policies:

**Option A: Use the managed policy (recommended)**

Attach the [CloudWatchLogsAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.md") managed policy.

**Option B: Create a custom policy**

Create and attach the following IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "LogsAPIs",
            "Effect": "Allow",
            "Action": [
                "logs:CallWithBearerToken",
                "logs:PutLogEvents"
            ],
            "Resource": "*"
        },
        {
            "Sid": "KMSAPIs",
            "Effect": "Allow",
            "Action": [
                "kms:Describe*",
                "kms:GenerateDataKey*",
                "kms:Decrypt"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": [
                        "logs.*.amazonaws.com"
                    ]
                }
            },
            "Resource": "arn:aws:kms:*:*:key/*"
        }
    ]
}
```

7. Choose **Next** and then **Create user**.

###### Note

The KMS permissions are required if you plan to send logs to KMS-encrypted log groups. The condition restricts KMS access to only keys used via CloudWatch Logs service.

### Step 2: Generate service-specific credentials (API key)

Generate the CloudWatch Logs API key using the [CreateServiceSpecificCredential](../../../IAM/latest/APIReference/API_CreateServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_CreateServiceSpecificCredential.md") API. You can also use the [create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html") CLI command. For the credential age, you can specify a value between 1–36600 days. If you don't specify a credential age, the API key will not expire.

To generate an API key with an expiration of 30 days:

```
aws iam create-service-specific-credential \
    --user-name cloudwatch-logs-hlc-user \
    --service-name logs.amazonaws.com \
    --credential-age-days 30
```

The response is a [ServiceSpecificCredential](../../../IAM/latest/APIReference/API_ServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_ServiceSpecificCredential.md") object. The `ServiceCredentialSecret` value is your CloudWatch Logs API key (bearer token).

###### Important

Store the `ServiceCredentialSecret` value securely, as you cannot retrieve it later. If you lose it, you'll need to generate a new API key.

### Step 3: Create log group and log stream

Create the log group and log stream where your logs will be stored:

```
# Create the log group
aws logs create-log-group \
    --log-group-name /aws/hlc-logs/my-application \
    --region us-east-1

# Create the log stream
aws logs create-log-stream \
    --log-group-name /aws/hlc-logs/my-application \
    --log-stream-name application-stream-001 \
    --region us-east-1
```

### Step 4: Enable bearer token authentication

Enable bearer token authentication on the log group:

```
aws logs put-bearer-token-authentication \
    --log-group-identifier /aws/hlc-logs/my-application \
    --bearer-token-authentication-enabled \
    --region us-east-1
```

Verify the configuration:

```
aws logs describe-log-groups \
    --log-group-name-prefix /aws/hlc-logs/my-application \
    --region us-east-1
```

## Control permissions for generating and using CloudWatch Logs API keys

The generation and usage of CloudWatch Logs API keys is controlled by actions and condition keys in both the CloudWatch Logs and IAM services.

### Controlling the generation of CloudWatch Logs API keys

The [iam:CreateServiceSpecificCredential](../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md#awsidentityandaccessmanagementiam-actions-as-permissions "../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md#awsidentityandaccessmanagementiam-actions-as-permissions") action controls the generation of a service-specific key (such as a CloudWatch Logs API key). You can scope this action to IAM users as a resource to limit the users for which a key can be generated.

You can use the following condition keys to impose conditions on the permission for the `iam:CreateServiceSpecificCredential` action:

- [iam:ServiceSpecificCredentialAgeDays](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays") – Lets you specify, in the condition, the key's expiration time in days. For example, you can use this condition key to only allow the creation of API keys that expire within 90 days.
- [iam:ServiceSpecificCredentialServiceName](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays") – Lets you specify, in the condition, the name of a service. For example, you can use this condition key to only allow the creation of API keys for CloudWatch Logs and not other services.

### Controlling the usage of CloudWatch Logs API keys

The `logs:CallWithBearerToken` action controls the use of a CloudWatch Logs API key. To prevent an identity from using CloudWatch Logs API keys, attach a policy that denies the `logs:CallWithBearerToken` action to the IAM user associated with the key.

### Example policies

#### Prevent an identity from generating and using CloudWatch Logs API keys

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCWLAPIKeys",
            "Effect": "Deny",
            "Action": [
                "iam:CreateServiceSpecificCredential",
                "logs:CallWithBearerToken"
            ],
            "Resource": "*"
        }
    ]
}
```

###### Warning

This policy will prevent the creation of credentials for all AWS services that support creating service-specific credentials. For more information, see [Service-specific credentials for IAM users](../../../IAM/latest/UserGuide/id_credentials_service-specific-creds.md "../../../IAM/latest/UserGuide/id_credentials_service-specific-creds.md").

#### Prevent an identity from using CloudWatch Logs API keys

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "logs:CallWithBearerToken",
            "Resource": "*"
        }
    ]
}
```

#### Allow the creation of CloudWatch Logs keys only if they expire within 90 days

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceSpecificCredential",
            "Resource": "arn:aws:iam::123456789012:user/username",
            "Condition": {
                "StringEquals": {
                    "iam:ServiceSpecificCredentialServiceName": "logs.amazonaws.com"
                },
                "NumericLessThanEquals": {
                    "iam:ServiceSpecificCredentialAgeDays": "90"
                }
            }
        }
    ]
}
```

## Handle compromised CloudWatch Logs API keys

If your API key becomes compromised, you should revoke permissions to use it. You can use the following IAM API operations to manage compromised keys:

- [UpdateServiceSpecificCredential](../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_UpdateServiceSpecificCredential.md") – Set the status of the key to inactive. You can reactivate the key later.
- [ResetServiceSpecificCredential](../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.md") – Reset the key. This generates a new password for the key.
- [DeleteServiceSpecificCredential](../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_DeleteServiceSpecificCredential.md") – Delete the key permanently.

###### Note

To carry out these actions through the API, you must authenticate with AWS credentials and not with a CloudWatch Logs API key.

### Change the status of a CloudWatch Logs API key

To deactivate a key, use the [update-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/update-service-specific-credential.html") command:

```
aws iam update-service-specific-credential \
    --user-name cloudwatch-logs-hlc-user \
    --service-specific-credential-id ACCA1234EXAMPLE1234 \
    --status Inactive
```

To reactivate the key, change the status to `Active`.

### Reset a CloudWatch Logs API key

If the value of your key has been compromised or you no longer have it, reset it using the [reset-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/reset-service-specific-credential.html") command. The key must not have expired yet. If it's already expired, delete the key and create a new one.

```
aws iam reset-service-specific-credential \
    --service-specific-credential-id ACCA1234EXAMPLE1234
```

### Delete a CloudWatch Logs API key

If you no longer need a key or it has expired, delete it using the [delete-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-service-specific-credential.html") command:

```
aws iam delete-service-specific-credential \
    --service-specific-credential-id ACCA1234EXAMPLE1234
```

### Attach IAM policies to remove permissions for using a CloudWatch Logs API key

To prevent an identity from making calls with a CloudWatch Logs API key, attach the following policy to the IAM user associated with the key:

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Deny",
        "Action": "logs:CallWithBearerToken",
        "Resource": "*"
    }
}
```

## Logging API key usage with CloudTrail

You can use AWS CloudTrail to log data events for CloudWatch Logs API key usage. CloudWatch Logs emits `AWS::Logs::LogGroupAuthorization` data events for `CallWithBearerToken` calls, enabling you to audit when and how API keys are used to send logs.

To enable CloudTrail logging for CloudWatch Logs API key usage:

###### Note

The S3 bucket that you specify for the trail must have a bucket policy that allows CloudTrail to write log files to it. For more information, see [Amazon S3 bucket policy for CloudTrail](../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md").

1. Create a trail:

```
aws cloudtrail create-trail \
    --name cloudwatch-logs-api-key-audit \
    --s3-bucket-name my-cloudtrail-bucket \
    --region us-east-1
```

2. Configure advanced event selectors to capture CloudWatch Logs log group authorization events:

```
aws cloudtrail put-event-selectors \
    --region us-east-1 \
    --trail-name cloudwatch-logs-api-key-audit \
    --advanced-event-selectors '[{
        "Name": "CloudWatch Logs API key authorization events",
        "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::Logs::LogGroupAuthorization"] }
        ]
    }]'
```

3. Start trail logging:

```
aws cloudtrail start-logging \
    --name cloudwatch-logs-api-key-audit \
    --region us-east-1
```
