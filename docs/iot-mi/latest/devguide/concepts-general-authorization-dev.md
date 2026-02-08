# General/Custom Authorization requirements for connector developers

General Authorization enables your connector to use credentials
(such as API keys, tokens, or username/password combinations) instead of OAuth 2.0
user tokens. Unlike OAuth 2.0, which provides user-level authorization through account
linking, General Authorization allows a single set of credentials to control devices
across multiple end users.

###### Note

Throughout this documentation, Custom Authorization is referred to as General Authorization.
Both terms describe the same authorization mechanism. In the following sections, we use
"General Authorization" for consistency.

This section explains how to implement General Authorization support in your
connector AWS Lambda function. If you are a customer configuring General Authorization
for an existing connector, see [General/Custom Authorization requirements](concepts-general-authorization.md "concepts-general-authorization.md").

###### Topics

- [What is General Authorization?](#what-is-general-auth-dev "#what-is-general-auth-dev")
- [How General Authorization uses AWS Secrets Manager](#general-auth-secrets-manager-dev "#general-auth-secrets-manager-dev")
- [General Authorization request format](#general-auth-request-format "#general-auth-request-format")
- [General Authorization workflow](#general-auth-workflow-dev "#general-auth-workflow-dev")
- [Lambda permissions for GeneralAuthorization](#general-auth-lambda-permissions-dev "#general-auth-lambda-permissions-dev")

## What is General Authorization?

General Authorization is any non-OAuth authorization mechanism that allows your connector
to authorize with third-party platforms using customer credentials. With
General Authorization, Managed integrations delegates credential management to your connector,
and a single set of credentials can control devices across multiple end users.

This is useful for scenarios where you have a business relationship with the
device vendor and need to manage devices at scale without individual user
authorization flows.

### When to use General Authorization

Consider implementing General Authorization support in your connector when:

- The third-party platform does not support OAuth 2.0
- The third-party platform provides custom authorization material such as API keys or
  credentials that can reside in AWS Secrets Manager
- You need to manage devices at scale without individual user authorization flows

###### Note

Your connector can implement both authorization types in parallel, providing compatibility
with diverse authorization frameworks.

## How General Authorization uses AWS Secrets Manager

AWS Secrets Manager is a secret storage service that protects sensitive
credentials such as API keys and tokens. Secrets are encrypted using AWS Key Management Service keys.
For more information, see the [AWS Secrets Manager User
Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

For General Authorization, customers store authorization credentials in Secrets Manager,
and grant your C2C connector permission to access these secrets. When managed integrations
invokes your connector, it provides the Secrets Manager ARN and version ID in the request header.
Your connector retrieves the secret value and uses it to authorize with the
third-party platform.

This approach ensures that managed integrations never handles long-term credentials directly.
Your connector maintains full control over credential management and token generation,
making the solution extensible to any authorization mechanism supported by your
third-party platform.

###### Important

Managed integrations does not access or manage the credentials stored in the customer's
AWS Secrets Manager. Your connector has full control over credential
retrieval, parsing, and usage.

###### Important

We recommend that you don't log sensitive credentials or tokens in any logs. If
however they are stored in logs, we recommend that you use CloudWatch Logs data protection
policies to mask the tokens in the logs. For more information, see [Help protect
sensitive log data with masking](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md").

## General Authorization request format

When Managed integrations invokes your connector for a General Authorization account
association, the request header contains a AWS Secrets Manager reference
instead of an OAuth token. The request structure is consistent across all connector
operations (`AWS.ActivateUser`, `AWS.DiscoverDevices`,
`AWS.SendCommand`, and `AWS.DeactivateUser`).

###### Example: General Authorization Request

```
{
  "header": {
    "auth": {
      "secretsManager": {
        "arn": "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-api-key-AbCdEf",
        "versionId": "a1b2c3d4-5678-90ab-cdef-1234567890ab"
      },
      "type": "GeneralAuthorization"
    }
  },
  "payload": {
    "operationName": "AWS.DiscoverDevices",
    "operationVersion": "1.0",
    "connectorId": "Your-Connector-Id",
    ...
  }
}
```

###### Example: OAuth 2.0 Request (for comparison)

```
{
  "header": {
    "auth": {
      "token": "ashriu32yr97feqy7afsaf",
      "type": "OAuth2.0"
    }
  },
  "payload": {
    "operationName": "AWS.DiscoverDevices",
    "operationVersion": "1.0",
    "connectorId": "Your-Connector-Id",
    ...
  }
}
```

###### Note

Your connector must handle both request formats. Check the `auth.type`
field to determine which authorization method to use for each request.

## General Authorization workflow

When your connector receives a General Authorization request, follow this workflow:

- **Check authorization type** - Check the `auth.type` field in the request header to determine
  if the request uses General Authorization
- **Extract Secrets Manager reference** - Extract the AWS Secrets Manager ARN and version ID from the
  `auth.secretsManager` object
- **Retrieve secret** - Call the AWS Secrets Manager `GetSecretValue` API
  using the provided ARN and version ID
- **Parse credentials** - Parse the secret value to extract authorization credentials (the format
  depends on your third-party platform's requirements)
- **Generate tokens (if needed)** - If needed, use the credentials to generate an access token or perform
  additional authorization steps required by the third-party platform
- **Authorize API calls** - Use the credentials or generated token to authorize API calls to the
  third-party platform
- **Process operation** - Process the connector operation (`AWS.DiscoverDevices`,
  `AWS.SendCommand`, etc.) using the authorized connection

###### Note

Your connector is responsible for all credential management, including token
generation, refresh, and error handling. Managed integrations only provides the reference to
the secret; it does not manage the credentials themselves.

## Lambda permissions for GeneralAuthorization

Your connector Lambda execution role must have permission to retrieve secrets
from the customer's AWS Secrets Manager. Add the following permissions
to your Lambda execution role policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:*:*:secret:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "secretsmanager.*.amazonaws.com"
        }
      }
    }
  ]
}
```

**Permission Explanation**

- `secretsmanager:GetSecretValue` - Allows your Lambda to retrieve secret values
- `kms:Decrypt` - Required because secrets are encrypted using AWS Key Management Service keys

###### Note

The example policy allows access to any secret. In production, you should
restrict the `Resource` field to only the secrets your connector needs.
However, since customers create their own secrets, you may need to use a wildcard
or document the naming convention customers should follow.

The customer will also grant your Lambda permission to access their specific
secret through the secret's resource policy.
