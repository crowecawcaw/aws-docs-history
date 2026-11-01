

# Setting up bearer token authentication for traces
<a name="xray-opentelemetry-bearer-token"></a>

You can send traces to the X-Ray OpenTelemetry Protocol (OTLP) traces endpoint (`https://xray.{{region}}.amazonaws.com/v1/traces`) with an X-Ray API key (bearer token) instead of AWS Signature Version 4 (SigV4). Use bearer token authentication for workloads where you can't use the AWS SDK or short-term credentials, such as applications running on premises or in another cloud, CI/CD pipelines, or third-party tools that only support a static `Authorization` header.

**Prefer SigV4 with short-term credentials**  
SigV4 with short-term credentials provides the strongest security posture, so use it wherever you can. Use API keys only where short-term credentials aren't practical, and switch to short-term credentials when your application has greater security requirements. For more information, see [Alternatives to long-term access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles) in the *IAM User Guide*.

An X-Ray API key is an IAM service-specific credential for `xray.amazonaws.com`, owned by an IAM user. A request with an API key has exactly the permissions of that IAM user. API keys work only for sending spans to the OTLP traces endpoint, which is authorized as `xray:PutTraceSegments`. You can't use them to call the X-Ray APIs that require SigV4, including the `PutTraceSegments` API and the APIs that read trace data.

Bearer token authentication has the following requirements and limitations:

**Requirements and limitations**
+ **Transaction Search** – The OTLP traces endpoint requires Transaction Search, which sends spans to Amazon CloudWatch Logs. Enable it before you send traces. For more information, see [Transaction Search](xray-transactionsearch.md).
+ **TLS** – Requests must use HTTPS. Requests sent over plain HTTP are rejected.
+ **Endpoints** – API keys work with the standard and FIPS traces endpoints (`https://xray-fips.{{region}}.amazonaws.com/v1/traces`, in Regions that have FIPS endpoints) and through interface VPC endpoints for X-Ray.
+ **Regions** – Bearer token authentication is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Thailand), Asia Pacific (Tokyo), Canada (Central), Canada West (Calgary), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), and South America (São Paulo).
+ **Keys per user** – IAM allows two X-Ray API keys per IAM user, so that you can rotate keys without downtime.

## Create an IAM user and an API key
<a name="xray-opentelemetry-bearer-token-setup"></a>

**To create an IAM user for trace ingestion**

1. Open the [IAM console](https://console.aws.amazon.com/iam/) and choose **Users**, **Create user**.

1. Enter a user name, for example **xray-traces-api-key-user**, and choose **Next**.

1. Attach one of the following policies, and then choose **Next** and **Create user**.
   + **Recommended** – The `AWSXRayAPIKeyAccess` AWS managed policy. For more information, see [IAM managed policies for X-Ray](security_iam_id-based-policy-examples.md#xray-permissions-managedpolicies).
   + A customer managed policy with the same two permissions. `xray:CallWithBearerToken` allows the user to authenticate with an API key, and `xray:PutTraceSegments` is the action that authorizes sending spans to the OTLP traces endpoint.

     ```
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Sid": "XRayTracesWithAPIKey",
                 "Effect": "Allow",
                 "Action": [
                     "xray:CallWithBearerToken",
                     "xray:PutTraceSegments"
                 ],
                 "Resource": "*"
             }
         ]
     }
     ```

**Note**  
If you send spans to custom log groups with the `x-aws-log-group` and `x-aws-log-stream` headers, the IAM user also needs permission to write to those log groups, the same as with SigV4 (for example, `logs:PutLogEvents` and `logs:CreateLogStream`).

To create the API key, use the IAM console or the [CreateServiceSpecificCredential](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceSpecificCredential.html) API. In the IAM console, open the user, choose the **Security credentials** tab, and in **API keys for AWS services** generate a key for X-Ray.

The following AWS CLI command creates an API key that expires after 30 days. Replace {{xray-traces-api-key-user}} with the name of your IAM user. You can set a credential age from 1 to 36,600 days. If you don't set one, the key doesn't expire.

```
aws iam create-service-specific-credential \
    --user-name {{xray-traces-api-key-user}} \
    --service-name xray.amazonaws.com \
    --credential-age-days 30
```

The `ServiceCredentialSecret` value in the response is your API key (bearer token). Store it securely, for example in AWS Secrets Manager. You can't retrieve it later. If you lose it, create a new key.

## Send traces with an API key
<a name="xray-opentelemetry-bearer-token-send"></a>

Send the API key in the `Authorization` header with the `Bearer` scheme. The endpoint accepts `application/x-protobuf` and `application/json` payloads. The following example sends an OTLP JSON payload to US East (N. Virginia).

```
curl -X POST "https://xray.us-east-1.amazonaws.com/v1/traces" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ${{XRAY_API_KEY}}" \
     -d @{{spans.json}}
```

With the OpenTelemetry Collector, use the [bearertokenauth](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/bearertokenauthextension) extension instead of `sigv4auth`, and read the key from a file or an environment variable.

```
extensions:
  bearertokenauth:
    filename: "/etc/otel/xray-api-key"

receivers:
  otlp:
    protocols:
      http:
        endpoint: "0.0.0.0:4318"

processors:
  batch:

exporters:
  otlphttp/traces:
    compression: gzip
    traces_endpoint: "https://xray.us-east-1.amazonaws.com/v1/traces"
    auth:
      authenticator: bearertokenauth

service:
  extensions: [bearertokenauth]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlphttp/traces]
```

To read the key from an environment variable instead, use `token: "${env:XRAY_API_KEY}"` in the `bearertokenauth` extension.

**Important**  
Never put API keys directly in collector configuration files or source code. Configuration files are often committed to version control. Read the key from a mounted secret with `filename`, or from an environment variable that your secrets manager injects.

The endpoint returns HTTP 403 when the API key is invalid, expired, or inactive, or when the IAM user isn't allowed `xray:CallWithBearerToken` or `xray:PutTraceSegments`. It returns HTTP 503 when the request can't be authenticated because of a temporary service issue. Retry 503 responses with backoff.

## Control who can create and use X-Ray API keys
<a name="xray-opentelemetry-bearer-token-permissions"></a>

The `iam:CreateServiceSpecificCredential` action controls who can create API keys. Use the `iam:ServiceSpecificCredentialServiceName` condition key to limit it to `xray.amazonaws.com`, and the `iam:ServiceSpecificCredentialAgeDays` condition key to require keys to expire.

The `xray:CallWithBearerToken` action controls whether an IAM user's API keys can be used. X-Ray evaluates it against identity-based policies only. To stop an identity from using X-Ray API keys, deny `xray:CallWithBearerToken` for that identity, or in a service control policy for your organization.

The following policy allows creating X-Ray API keys only for a specific IAM user, and only if the keys expire within 90 days.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceSpecificCredential",
            "Resource": "arn:aws:iam::{{111122223333}}:user/{{xray-traces-api-key-user}}",
            "Condition": {
                "StringEquals": {
                    "iam:ServiceSpecificCredentialServiceName": "xray.amazonaws.com"
                },
                "NumericLessThanEquals": {
                    "iam:ServiceSpecificCredentialAgeDays": "90"
                }
            }
        }
    ]
}
```

The following policy prevents an identity from using X-Ray API keys.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "xray:CallWithBearerToken",
            "Resource": "*"
        }
    ]
}
```

To allow API keys to be used only from specific networks, add an `aws:SourceIp` condition to the statement that allows `xray:CallWithBearerToken` and `xray:PutTraceSegments`. Don't rely only on `aws:SourceIp` conditions on downstream actions, such as the Amazon CloudWatch Logs actions used for custom log groups. `aws:SourceIp` matches public IP addresses only. For requests that come through an interface VPC endpoint, use `aws:SourceVpce` or `aws:VpcSourceIp` instead.

## Rotate and revoke API keys
<a name="xray-opentelemetry-bearer-token-manage"></a>

**To rotate an API key without interrupting trace delivery**

1. Create a second key for the same IAM user.

   ```
   aws iam create-service-specific-credential \
       --user-name {{xray-traces-api-key-user}} \
       --service-name xray.amazonaws.com \
       --credential-age-days 90
   ```

1. Update your collector or application to use the new key.

1. Set the old key to inactive and confirm that traces still arrive.

   ```
   aws iam update-service-specific-credential \
       --user-name {{xray-traces-api-key-user}} \
       --service-specific-credential-id {{ACCA1234EXAMPLE1234}} \
       --status Inactive
   ```

1. Delete the old key.

   ```
   aws iam delete-service-specific-credential \
       --user-name {{xray-traces-api-key-user}} \
       --service-specific-credential-id {{ACCA1234EXAMPLE1234}}
   ```

To list a user's X-Ray API keys with their creation date and status, run `aws iam list-service-specific-credentials --user-name {{xray-traces-api-key-user}} --service-name xray.amazonaws.com`.

If an API key might be compromised, set it to inactive or delete it immediately. To block all API key use by the IAM user while you investigate, attach a policy that denies `xray:CallWithBearerToken`. Changes to a key's status or the user's permissions take effect within about five minutes. Then review AWS CloudTrail data events to see how the key was used, and create a replacement key. You must use AWS credentials, not an API key, to manage API keys.

## Audit API key usage
<a name="xray-opentelemetry-bearer-token-monitor"></a>

CloudTrail records requests to the OTLP traces endpoint as `PutTraceSegments` data events for the `AWS::XRay::Trace` resource type. For a request made with an API key, the event's `userIdentity` is the IAM user that owns the key, and `additionalEventData` contains `"callWithBearerToken": true`. Requests signed with SigV4 don't include this field, so you can use it to find every request made with an API key. CloudTrail doesn't log data events by default. For more information, see [X-Ray data events in CloudTrail](xray-api-cloudtrail.md#cloudtrail-data-events).

The following example shows the relevant fields of an event for a request made with an API key.

```
{
    "eventSource": "xray.amazonaws.com",
    "eventName": "PutTraceSegments",
    "eventCategory": "Data",
    "userIdentity": {
        "type": "IAMUser",
        "arn": "arn:aws:iam::{{111122223333}}:user/{{xray-traces-api-key-user}}",
        "accountId": "{{111122223333}}",
        "userName": "{{xray-traces-api-key-user}}"
    },
    "additionalEventData": {
        "callWithBearerToken": true,
        "protocol": "OTLP"
    },
    "resources": [
        {
            "type": "AWS::XRay::Trace"
        }
    ]
}
```

Follow these best practices for X-Ray API keys:

**Best practices for X-Ray API keys**
+ Set an expiration on every key, and enforce a maximum key age with the `iam:ServiceSpecificCredentialAgeDays` condition key.
+ Use one IAM user per application or integration, with only the permissions it needs.
+ Store keys in a secrets manager, never in source code or configuration files.
+ Rotate keys regularly, and use IAM Access Analyzer to find unused credentials and overly permissive policies.