

# Setting up bearer token authentication
<a name="CWL_HTTP_Endpoints_BearerTokenAuth"></a>

Before you can send logs using bearer token authentication with any of the HTTP ingestion endpoints, you need to:
+ Create an IAM user with CloudWatch Logs permissions
+ Generate service-specific credentials (bearer token)
+ Create a log group and log stream
+ Enable bearer token authentication on the log group

**Important**  
We recommend using SigV4 authentication with short-term credentials for all workloads where this is possible. SigV4 provides the strongest security posture. Restrict the use of API keys (bearer tokens) to scenarios where short-term credential-based authentication is not feasible. When you are ready to incorporate CloudWatch Logs into applications with greater security requirements, you should switch to short-term credentials. For more information, see [Alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) in the *IAM User Guide*.

## Option 1: Quick start using the AWS console
<a name="CWL_HTTP_Endpoints_Console_Setup"></a>

The AWS Management Console provides a streamlined workflow to generate API keys for HTTP endpoint access.

**To set up HTTP endpoint access using the console**

1. Sign in to the AWS Management Console.

1. Navigate to **CloudWatch** > **Settings** > **Logs**.

1. In the API Keys section, choose **Generate API key**.

1. For **API key expiration**, do one of the following:
   + Select an API key expiration duration of **1**, **5**, **30**, **90**, or **365** days.
   + Choose **Custom duration** to specify a custom API key expiration date.
   + Select **Never expires** (not recommended).

1. Choose **Generate API key**.

   The console automatically:
   + Creates a new IAM user with appropriate permissions
   + Attaches the [CloudWatchLogsAPIKeyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.html) managed policy (includes `logs:PutLogEvents` and `logs:CallWithBearerToken` permissions)
   + Generates service-specific credentials (API key)

1. Copy and securely save the displayed credentials:
   + **API Key ID** (Service-specific credential ID)
   + **API Key Secret** (Bearer token)
**Important**  
Save the API Key Secret immediately. It cannot be retrieved later. If you lose it, you'll need to generate a new API key.

1. Create the log group and log stream where your logs will be stored:

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

1. Enable bearer token authentication on the log group:

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
+ `logs:PutLogEvents` – Send log events to CloudWatch Logs
+ `logs:CallWithBearerToken` – Authenticate using bearer token
+ `kms:Describe*`, `kms:GenerateDataKey*`, `kms:Decrypt` – Access KMS-encrypted log groups (with condition restricting to logs service)

## Option 2: Manual setup
<a name="CWL_HTTP_Endpoints_Manual_Setup"></a>

If you prefer more control over the IAM configuration or need to customize permissions, you can set up the HTTP endpoint access manually.

### Step 1: Create an IAM user
<a name="CWL_HTTP_Endpoints_Manual_Step1"></a>

Create an IAM user that will be used for log ingestion:

1. Sign in to the AWS Management Console and navigate to IAM.

1. In the left navigation pane, choose **Users**.

1. Choose **Create user**.

1. Enter a user name (for example, `cloudwatch-logs-hlc-user`).

1. Choose **Next**.

1. Attach one of the following IAM policies:

   **Option A: Use the managed policy (recommended)**

   Attach the [CloudWatchLogsAPIKeyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.html) managed policy.

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

1. Choose **Next** and then **Create user**.

**Note**  
The KMS permissions are required if you plan to send logs to KMS-encrypted log groups. The condition restricts KMS access to only keys used via CloudWatch Logs service.

### Step 2: Generate service-specific credentials (API key)
<a name="CWL_HTTP_Endpoints_Manual_Step2"></a>

Generate the CloudWatch Logs API key using the [CreateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html) API. You can also use the [create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html) CLI command. For the credential age, you can specify a value between 1–36600 days. If you don't specify a credential age, the API key will not expire.

To generate an API key with an expiration of 30 days:

```
aws iam create-service-specific-credential \
    --user-name cloudwatch-logs-hlc-user \
    --service-name logs.amazonaws.com \
    --credential-age-days 30
```

The response is a [ServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ServiceSpecificCredential.html) object. The `ServiceCredentialSecret` value is your CloudWatch Logs API key (bearer token).

**Important**  
Store the `ServiceCredentialSecret` value securely, as you cannot retrieve it later. If you lose it, you'll need to generate a new API key.

### Step 3: Create log group and log stream
<a name="CWL_HTTP_Endpoints_Manual_Step3"></a>

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
<a name="CWL_HTTP_Endpoints_Manual_Step4"></a>

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
<a name="CWL_HTTP_Endpoints_API_Key_Permissions"></a>

The generation and usage of CloudWatch Logs API keys is controlled by actions and condition keys in both the CloudWatch Logs and IAM services.

### Controlling the generation of CloudWatch Logs API keys
<a name="CWL_HTTP_Endpoints_Control_Generation"></a>

The [iam:CreateServiceSpecificCredential](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.html#awsidentityandaccessmanagementiam-actions-as-permissions) action controls the generation of a service-specific key (such as a CloudWatch Logs API key). You can scope this action to IAM users as a resource to limit the users for which a key can be generated.

You can use the following condition keys to impose conditions on the permission for the `iam:CreateServiceSpecificCredential` action:
+ [iam:ServiceSpecificCredentialAgeDays](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ServiceSpecificCredentialAgeDays) – Lets you specify, in the condition, the key's expiration time in days. For example, you can use this condition key to only allow the creation of API keys that expire within 90 days.
+ [iam:ServiceSpecificCredentialServiceName](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html#ck_ServiceSpecificCredentialAgeDays) – Lets you specify, in the condition, the name of a service. For example, you can use this condition key to only allow the creation of API keys for CloudWatch Logs and not other services.

### Controlling the usage of CloudWatch Logs API keys
<a name="CWL_HTTP_Endpoints_Control_Usage"></a>

The `logs:CallWithBearerToken` action controls the use of a CloudWatch Logs API key. To prevent an identity from using CloudWatch Logs API keys, attach a policy that denies the `logs:CallWithBearerToken` action to the IAM user associated with the key.

### Example policies
<a name="CWL_HTTP_Endpoints_Permission_Examples"></a>

#### Prevent an identity from generating and using CloudWatch Logs API keys
<a name="CWL_HTTP_Endpoints_Deny_Generation_And_Use"></a>

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

**Warning**  
This policy will prevent the creation of credentials for all AWS services that support creating service-specific credentials. For more information, see [Service-specific credentials for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_service-specific-creds.html).

#### Prevent an identity from using CloudWatch Logs API keys
<a name="CWL_HTTP_Endpoints_Deny_Use"></a>

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
<a name="CWL_HTTP_Endpoints_Allow_Expire_90"></a>

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

## Rotating API keys
<a name="CWL_HTTP_Endpoints_Rotating_Keys"></a>

Regularly rotating your API keys reduces the risk of unauthorized access. We recommend establishing a rotation schedule that aligns with your organization's security policies.

### Rotation process
<a name="CWL_HTTP_Endpoints_Rotation_Process"></a>

To rotate an API key without interrupting log delivery, follow this procedure:

1. Create a new (secondary) credential for the IAM user:

   ```
   aws iam create-service-specific-credential \
       --user-name cloudwatch-logs-hlc-user \
       --service-name logs.amazonaws.com \
       --credential-age-days 90
   ```

1. (Optional) Store the new credential in AWS Secrets Manager for secure retrieval and automated rotation.

1. Import the new credential into your vendor's portal or update your application configuration to use the new API key.

1. Set the original credential to inactive:

   ```
   aws iam update-service-specific-credential \
       --user-name cloudwatch-logs-hlc-user \
       --service-specific-credential-id ACCA1234EXAMPLE1234 \
       --status Inactive
   ```

1. Verify that log delivery is not impacted by monitoring the `IncomingBytes` metric for your log group in CloudWatch. For more information, see [Monitoring with CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html).

1. After confirming successful delivery with the new key, delete the previous credential:

   ```
   aws iam delete-service-specific-credential \
       --service-specific-credential-id ACCA1234EXAMPLE1234
   ```

### Monitoring key expiration
<a name="CWL_HTTP_Endpoints_Monitor_Expiration"></a>

To check the creation date and status of your existing API keys, use the [list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html) command:

```
aws iam list-service-specific-credentials \
    --user-name cloudwatch-logs-hlc-user \
    --service-name logs.amazonaws.com
```

The response includes `CreateDate` and `Status` for each credential. Use this information to identify keys that are approaching expiration or have been active longer than your rotation policy allows.

## Responding to a compromised API key
<a name="CWL_HTTP_Endpoints_Compromised_Keys"></a>

If you suspect that an API key has been compromised, take the following steps immediately:

1. **Deactivate the key immediately** to prevent further unauthorized use:

   ```
   aws iam update-service-specific-credential \
       --user-name cloudwatch-logs-hlc-user \
       --service-specific-credential-id ACCA1234EXAMPLE1234 \
       --status Inactive
   ```

1. **Review CloudTrail logs** to determine the scope of unauthorized access. See [Logging API key usage with CloudTrail](#CWL_HTTP_Endpoints_CloudTrail_Logging) for how to enable auditing of API key usage.

1. **Create a replacement key** following the rotation process described in [Rotation process](#CWL_HTTP_Endpoints_Rotation_Process).

1. **Delete the compromised key** after the replacement is in place:

   ```
   aws iam delete-service-specific-credential \
       --service-specific-credential-id ACCA1234EXAMPLE1234
   ```

1. **Attach a deny policy** if you need to immediately block all bearer token access for the IAM user while you investigate:

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

**Note**  
To carry out these actions through the API, you must authenticate with AWS credentials and not with a CloudWatch Logs API key.

You can also use the following IAM API operations to manage compromised keys:
+ [ResetServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResetServiceSpecificCredential.html) – Reset the key to generate a new password without deleting the credential. The key must not have expired.

## Security best practices for API keys
<a name="CWL_HTTP_Endpoints_Security_Best_Practices"></a>

Follow these best practices to protect your CloudWatch Logs API keys:
+ **Never embed API keys in source code.** Do not hard-code API keys in application code or commit them to version control systems. If a key is accidentally committed to a public repository, AWS automated scanning may flag it and you should rotate the key immediately.
+ **Use a secrets manager.** Store API keys in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) or an equivalent secrets management solution. This enables centralized access control, audit logging, and automated rotation.
+ **Set an expiration on all keys.** Always specify a `--credential-age-days` value when creating API keys. To enforce a maximum key lifetime across your organization, use the `iam:ServiceSpecificCredentialAgeDays` IAM condition key. For an example, see [Allow the creation of CloudWatch Logs keys only if they expire within 90 days](#CWL_HTTP_Endpoints_Allow_Expire_90).
+ **Apply least-privilege permissions.** Scope the IAM user's permissions to only the log groups and actions required. Use the managed [CloudWatchLogsAPIKeyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchLogsAPIKeyAccess.html) policy as a starting point and restrict further as needed.
+ **Enable CloudTrail logging.** Audit API key usage by enabling CloudTrail data events for `AWS::Logs::LogGroupAuthorization`. See [Logging API key usage with CloudTrail](#CWL_HTTP_Endpoints_CloudTrail_Logging).
+ **Monitor with IAM Access Analyzer.** Use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to identify unused credentials and overly permissive policies associated with your API key IAM users.
+ **Rotate keys regularly.** Establish a rotation schedule and follow the process described in [Rotating API keys](#CWL_HTTP_Endpoints_Rotating_Keys).

## Logging API key usage with CloudTrail
<a name="CWL_HTTP_Endpoints_CloudTrail_Logging"></a>

You can use AWS CloudTrail to log data events for CloudWatch Logs API key usage. CloudWatch Logs emits `AWS::Logs::LogGroupAuthorization` data events for `CallWithBearerToken` calls, enabling you to audit when and how API keys are used to send logs.

To enable CloudTrail logging for CloudWatch Logs API key usage:

**Note**  
The S3 bucket that you specify for the trail must have a bucket policy that allows CloudTrail to write log files to it. For more information, see [Amazon S3 bucket policy for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.html).

1. Create a trail:

   ```
   aws cloudtrail create-trail \
       --name cloudwatch-logs-api-key-audit \
       --s3-bucket-name my-cloudtrail-bucket \
       --region us-east-1
   ```

1. Configure advanced event selectors to capture CloudWatch Logs log group authorization events:

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

1. Start trail logging:

   ```
   aws cloudtrail start-logging \
       --name cloudwatch-logs-api-key-audit \
       --region us-east-1
   ```