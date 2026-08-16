# Setting up bearer token authentication for Metrics

###### Note

This page covers bearer token authentication for the CloudWatch Metrics OTLP
endpoint. For CloudWatch Logs bearer token authentication, see
[Setting
up bearer token authentication for Logs](../logs/CWL_HTTP_Endpoints_BearerTokenAuth.md "../logs/CWL_HTTP_Endpoints_BearerTokenAuth.md") in the
_CloudWatch Logs User Guide_.

Before you can send metrics using bearer token authentication with the CloudWatch OTLP
endpoint, you need to:

- Create an IAM user with CloudWatch Metrics permissions
- Generate service-specific credentials (API key)

###### Important

We recommend using SigV4 authentication with short-term credentials for all
workloads where this is possible. SigV4 provides the strongest security posture.
Restrict the use of API keys (bearer tokens) to scenarios where short-term
credential-based authentication is not feasible, such as sending metrics from
non-AWS environments, third-party vendors, or platforms that do not support the
AWS SDK. When you are ready to incorporate CloudWatch Metrics into applications with
greater security requirements, switch to short-term credentials. For more
information, see
[Alternatives
to long-term access keys](../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles "../../../IAM/latest/UserGuide/best-practices.md#bp-workloads-use-roles") in the
_IAM User Guide_.

###### Important

The CloudWatch OTLP endpoint requires TLS (HTTPS). Bearer token requests sent over
plain HTTP are rejected. Always use
`https://monitoring.`AWS Region`.amazonaws.com/v1/metrics`
when configuring your client.

## Option 1: Quick start using the AWS console

The AWS Management Console provides a streamlined workflow to generate API
keys for OTLP endpoint access.

###### To set up OTLP endpoint access using the console

1. Sign in to the AWS Management Console.
2. Navigate to **CloudWatch** >
   **Settings** > **Global**.
3. In the API Keys section, choose **Generate API key**.
4. For **API key expiration**, do one of the following:

   - Select an API key expiration duration of
     **1**, **5**,
     **30**, **90**, or
     **365** days.
   - Choose **Custom duration** to specify a
     custom API key expiration date.
   - Select **Never expires** (not
     recommended).

5. Choose **Generate API key**.

The console automatically:

- Creates a new IAM user with appropriate permissions
- Attaches the
  [CloudWatchAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md")
  managed policy (includes `cloudwatch:PutMetricData` and
  `cloudwatch:CallWithBearerToken` permissions)
- Generates service-specific credentials (API key)

###### To save and verify your API key

1. Copy and securely save the displayed credentials:

   - **API Key ID** (Service-specific
     credential ID)
   - **API Key Secret** (Bearer
     token)
     The console also offers the option to store your API key directly in
     [AWS
     Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") during generation. If you choose to store in
     Secrets Manager, the key is automatically updated on reset and deleted on
     key deletion.

###### Important

Save the API Key Secret immediately. You can't retrieve it later.
If you lose it, you must generate a new API key. 2. Send a test metric to verify your setup:

```
curl -X POST "https://monitoring.us-east-1.amazonaws.com/v1/metrics" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer `YOUR_API_KEY`" \
     -d '{"resourceMetrics":[]}'
```

## Option 2: Manual setup

If you prefer more control over the IAM configuration or need to customize
permissions, you can set up the OTLP endpoint access manually.

### Step 1: Create an IAM user

Create an IAM user for metric ingestion:

###### To create an IAM user for metric ingestion

1. Sign in to the AWS Management Console and navigate to
   IAM.
2. In the left navigation pane, choose
   **Users**.
3. Choose **Create user**.
4. Enter a user name (for example,
   `cloudwatch-metrics-api-key-user`).
5. Choose **Next**.
6. Attach one of the following IAM policies:

**Option A: Use the managed policy
(recommended)**

Attach the
[CloudWatchAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md")
managed policy.

**Option B: Create a custom
policy**

Create and attach the following IAM policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchMetricsAPIs",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:CallWithBearerToken",
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*"
        },
        {
            "Sid": "KMSDecryptForCMKDatasets",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "cloudwatch.*.amazonaws.com",
                    "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:*:*:dataset/*"
                }
            },
            "Resource": "arn:aws:kms:*:*:key/*"
        }
    ]
}
```

7. Choose **Next** and then choose
   **Create user**.

###### Note

The KMS permissions are required if you plan to send metrics to
datasets that use customer-managed KMS keys (CMK). The conditions
restrict KMS access to only keys used through the CloudWatch service for
dataset resources.

### Step 2: Generate service-specific credentials (API key)

Generate the CloudWatch Metrics API key using the
[CreateServiceSpecificCredential](../../../IAM/latest/APIReference/API_CreateServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_CreateServiceSpecificCredential.md")
API. You can also use the
[create-service-specific-credential](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-service-specific-credential.html")
AWS CLI command. For the credential age, you can specify a value between
1–36600 days. If you don't specify a credential age, the API key won't
expire.

To generate an API key with an expiration of 30 days:

```
aws iam create-service-specific-credential \
    --user-name cloudwatch-metrics-api-key-user \
    --service-name cloudwatch.amazonaws.com \
    --credential-age-days 30
```

The response is a
[ServiceSpecificCredential](../../../IAM/latest/APIReference/API_ServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_ServiceSpecificCredential.md")
object. The `ServiceCredentialSecret` value is your CloudWatch Metrics
API key (bearer token).

###### Important

Store the `ServiceCredentialSecret` value securely. You
can't retrieve it later. If you lose it, you must generate a new API
key.

### Step 3: Send metrics

You can immediately send metrics to the OTLP endpoint using your bearer
token:

```
curl -X POST "https://monitoring.us-east-1.amazonaws.com/v1/metrics" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer `YOUR_API_KEY`" \
     -d '{"resourceMetrics":[]}'
```

The endpoint accepts both `application/json` and
`application/x-protobuf` content types.

## Control permissions for generating and using CloudWatch Metrics API keys

### Controlling the generation of CloudWatch Metrics API keys

The
[`iam:CreateServiceSpecificCredential`](../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md#awsidentityandaccessmanagementiam-actions-as-permissions "../../../service-authorization/latest/reference/list_awsidentityandaccessmanagementiam.md#awsidentityandaccessmanagementiam-actions-as-permissions")
action controls the generation of a service-specific key (such as a CloudWatch
Metrics API key). You can scope this action to IAM users as a resource to
limit the users for which a key can be generated.

You can use the following condition keys to impose conditions on the
permission for the `iam:CreateServiceSpecificCredential`
action:

- [`iam:ServiceSpecificCredentialAgeDays`](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialAgeDays")
  — Lets you specify, in the condition, the key's expiration
  time in days.
- [`iam:ServiceSpecificCredentialServiceName`](../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialServiceName "../../../IAM/latest/UserGuide/reference_policies_iam-condition-keys.md#ck_ServiceSpecificCredentialServiceName")
  — Lets you specify, in the condition, the name of a
  service.

### Controlling the usage of CloudWatch Metrics API keys

The `cloudwatch:CallWithBearerToken` action controls the use
of a CloudWatch Metrics API key. To prevent an identity from using CloudWatch Metrics
API keys, attach a policy that denies the
`cloudwatch:CallWithBearerToken` action to the IAM user
associated with the key.

###### Note

Bearer tokens for CloudWatch Metrics can only be used with the OTLP metrics
ingestion endpoint
(`https://monitoring.`AWS Region`.amazonaws.com/v1/metrics`).
They cannot be used to call any other CloudWatch API or endpoint, including
query APIs (`GetMetricData`, `ListMetrics`,
`DescribeAlarms`), the PromQL query endpoint, the OTLP traces
endpoint, or the OTLP logs endpoint.

### Example policies

**Prevent an identity from generating and using CloudWatch
Metrics API keys:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyCWMetricsAPIKeys",
            "Effect": "Deny",
            "Action": [
                "iam:CreateServiceSpecificCredential",
                "cloudwatch:CallWithBearerToken"
            ],
            "Resource": "*"
        }
    ]
}
```

###### Warning

This policy prevents the creation of credentials for all AWS
services that support creating service-specific credentials. For more
information, see
[Service-specific
credentials for IAM users](../../../IAM/latest/UserGuide/id_credentials_service-specific-creds.md "../../../IAM/latest/UserGuide/id_credentials_service-specific-creds.md") in the
_IAM User Guide_.

**Prevent an identity from using CloudWatch Metrics API
keys:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "cloudwatch:CallWithBearerToken",
            "Resource": "*"
        }
    ]
}
```

**Allow the creation of CloudWatch Metrics keys only if
they expire within 90 days:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceSpecificCredential",
            "Resource": "arn:aws:iam::123456789012:user/`username`",
            "Condition": {
                "StringEquals": {
                    "iam:ServiceSpecificCredentialServiceName": "cloudwatch.amazonaws.com"
                },
                "NumericLessThanEquals": {
                    "iam:ServiceSpecificCredentialAgeDays": "90"
                }
            }
        }
    ]
}
```

## Using bearer tokens with the OpenTelemetry Collector

When using bearer tokens, you do not need the `sigv4auth`
extension. Use the
[bearertokenauth](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/bearertokenauthextension "https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/bearertokenauthextension")
extension to securely provide your API key from a file or environment
variable:

```
extensions:
  bearertokenauth:
    filename: "/etc/otel/cw-api-key"

exporters:
  otlphttp:
    tls:
      insecure: false
    endpoint: https://monitoring.us-east-1.amazonaws.com/v1/metrics
    auth:
      authenticator: bearertokenauth

receivers:
  otlp:
    protocols:
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    send_batch_size: 200
    timeout: 10s

service:
  extensions: [bearertokenauth]
  pipelines:
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp]
```

Alternatively, you can reference an environment variable instead of a
file:

```
extensions:
  bearertokenauth:
    token: "${env:CW_API_KEY}"
```

###### Important

Never hardcode API keys directly in collector configuration files.
Configuration files are often committed to version control or stored in
deployment manifests. Use `filename` to read from a mounted
secret, or `${env:VAR}` to read from an environment variable
injected by your secrets manager.

###### Note

With bearer token authentication, you do not need the
`sigv4auth` extension, AWS credentials files, IAM roles, or
IRSA configuration. This makes the collector configuration portable across
any environment — AWS, on-premises, or other cloud providers.

## Rotating API keys

Regularly rotating your API keys reduces the risk of unauthorized access. You should
recommend establishing a rotation schedule that aligns with your organization's
security policies.

### Rotation process

To rotate an API key without interrupting metric delivery, follow this
procedure:

###### To rotate an API key

1. Create a new (secondary) credential for the IAM user:

```
aws iam create-service-specific-credential \
    --user-name cloudwatch-metrics-api-key-user \
    --service-name cloudwatch.amazonaws.com \
    --credential-age-days 90
```

###### Note

IAM allows a maximum of 2 service-specific credentials per
IAM user per service. Delete or deactivate old credentials
before creating new ones if you have reached this limit. 2. (Optional) Store the new credential in AWS Secrets Manager for
secure retrieval and automated rotation. 3. Update your OpenTelemetry Collector configuration or application
to use the new API key. 4. Set the original credential to inactive:

```
aws iam update-service-specific-credential \
    --user-name cloudwatch-metrics-api-key-user \
    --service-specific-credential-id `ACCA1234EXAMPLE1234` \
    --status Inactive
```

5. Verify that metric delivery is not impacted. Send a test request
   using the new key and confirm you receive an HTTP 200 response. You
   can also monitor your application's existing CloudWatch metrics to confirm
   data continues to arrive.
6. After confirming successful delivery with the new key, delete the
   previous credential:

```
aws iam delete-service-specific-credential \
    --service-specific-credential-id `ACCA1234EXAMPLE1234`
```

### Monitoring key expiration

To check the creation date and status of your existing API keys, use the
[list-service-specific-credentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-service-specific-credentials.html")
command:

```
aws iam list-service-specific-credentials \
    --user-name cloudwatch-metrics-api-key-user \
    --service-name cloudwatch.amazonaws.com
```

The response includes `CreateDate` and `Status` for
each credential. Use this information to identify keys that are approaching
expiration or have been active longer than your rotation policy allows.

## Responding to a compromised API key

If you suspect that an API key has been compromised, take the following steps
immediately:

###### To respond to a compromised API key

1. **Deactivate the key immediately** to
   prevent further unauthorized use:

```
aws iam update-service-specific-credential \
    --user-name cloudwatch-metrics-api-key-user \
    --service-specific-credential-id `ACCA1234EXAMPLE1234` \
    --status Inactive
```

2. **Review CloudTrail logs** to determine
   the scope of unauthorized access. See
   [Logging API key usage with CloudTrail](#CloudWatch-OTLP-MetricsBearerTokenAuth-CloudTrail "#CloudWatch-OTLP-MetricsBearerTokenAuth-CloudTrail") for how to
   enable auditing of API key usage.
3. **Create a replacement key** following
   the rotation process described in
   [Rotation process](#CloudWatch-OTLP-MetricsBearerTokenAuth-Rotation-Process "#CloudWatch-OTLP-MetricsBearerTokenAuth-Rotation-Process").
4. **Delete the compromised key** after the
   replacement is in place:

```
aws iam delete-service-specific-credential \
    --service-specific-credential-id `ACCA1234EXAMPLE1234`
```

5. **Attach a deny policy** if you need to
   immediately block all bearer token access for the IAM user while you
   investigate:

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Deny",
        "Action": "cloudwatch:CallWithBearerToken",
        "Resource": "*"
    }
}
```

###### Note

To carry out these actions through the API, you must authenticate with
AWS credentials and not with a CloudWatch Metrics API key. Bearer tokens can
only be used for metric ingestion, not for IAM management
operations.

You can also use the following IAM API operations to manage compromised
keys:

- [ResetServiceSpecificCredential](../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.md "../../../IAM/latest/APIReference/API_ResetServiceSpecificCredential.md")
  — Reset the key to generate a new password without deleting the
  credential. The key must not have expired.

## Security best practices for API keys

Follow these best practices to protect your CloudWatch Metrics API keys:

- **Never embed API keys in source
  code.** Do not hard-code API keys in application code, collector
  configuration files, or version control systems. Use the
  `bearertokenauth` extension with `filename` or
  `${env:VAR}` to inject secrets at runtime.
- **Use a secrets manager.** Store API keys
  in
  [AWS
  Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") or an equivalent secrets management
  solution. This enables centralized access control, audit logging, and
  automated rotation.
- **Set an expiration on all keys.** Always
  specify a `--credential-age-days` value when creating API
  keys. To enforce a maximum key lifetime across your organization, use the
  `iam:ServiceSpecificCredentialAgeDays` IAM condition
  key.
- **Apply least-privilege permissions.**
  Use the managed
  [CloudWatchAPIKeyAccess](../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchAPIKeyAccess.md")
  policy as a starting point and restrict further as needed.
- **Enable CloudTrail logging.** Audit API
  key usage by enabling CloudTrail data events for
  `AWS::CloudWatch::Metric`. See
  [Logging API key usage with CloudTrail](#CloudWatch-OTLP-MetricsBearerTokenAuth-CloudTrail "#CloudWatch-OTLP-MetricsBearerTokenAuth-CloudTrail").
- **Monitor with IAM Access
  Analyzer.** Use
  [IAM
  Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") to identify unused credentials and overly
  permissive policies associated with your API key IAM users.
- **Rotate keys regularly.** Establish a
  rotation schedule and follow the process described in
  [Rotating API keys](#CloudWatch-OTLP-MetricsBearerTokenAuth-Rotation "#CloudWatch-OTLP-MetricsBearerTokenAuth-Rotation").

## Logging API key usage with CloudTrail

You can use AWS CloudTrail to log data events for CloudWatch Metrics OTLP
ingestion. CloudWatch emits `AWS::CloudWatch::Metric` data events for
calls to the OTLP endpoint, enabling you to audit metric ingestion activity
including API key usage.

###### Note

The S3 bucket that you specify for the trail must have a bucket policy
that allows CloudTrail to write log files to it. For more information, see
[Amazon
S3 bucket policy for CloudTrail](../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/create-s3-bucket-policy-for-cloudtrail.md") in the
_AWS CloudTrail User Guide_.

###### To enable CloudTrail logging for CloudWatch Metrics API key usage

1. Create a trail:

```
aws cloudtrail create-trail \
    --name cloudwatch-metrics-api-key-audit \
    --s3-bucket-name `my-cloudtrail-bucket` \
    --region us-east-1
```

2. Configure advanced event selectors to capture CloudWatch Metrics write
   (ingestion) data events:

```
aws cloudtrail put-event-selectors \
    --region us-east-1 \
    --trail-name cloudwatch-metrics-api-key-audit \
    --advanced-event-selectors '[{
        "Name": "CloudWatch Metrics write data events",
        "FieldSelectors": [
            { "Field": "eventCategory", "Equals": ["Data"] },
            { "Field": "resources.type", "Equals": ["AWS::CloudWatch::Metric"] },
            { "Field": "readOnly", "Equals": ["false"] }
        ]
    }]'
```

3. Start trail logging:

```
aws cloudtrail start-logging \
    --name cloudwatch-metrics-api-key-audit \
    --region us-east-1
```

The `readOnly: false` filter limits logging to write operations
(PutMetricData), which includes all OTLP ingestion calls. To identify bearer
token usage among these events, query your trail logs (through Athena or CloudTrail
Lake) and filter by the IAM user name associated with your API key (for
example, `cloudwatch-metrics-api-key-user`). Events from OTLP
ingestion include `AdditionalEventData.protocol` set to
`OTLP` in the event payload, which you can use in post-hoc queries
to distinguish them from classic PutMetricData SDK calls.
