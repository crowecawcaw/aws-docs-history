# General/Custom Authorization requirements

General Authorization enables access to devices, allowing you to control
multiple devices using credentials without requiring individual user credentials.
Unlike OAuth 2.0, which provides user-level authorization, General Authorization uses
pre-shared keys, tokens, or other authorization mechanisms stored in
AWS Secrets Manager.

With General Authorization, your C2C connector can support authorization mechanisms
beyond OAuth 2.0, including API keys, bearer tokens, and custom authorization schemes
provided by third-party platforms. This approach is particularly useful for scenarios where
devices are managed at a program or organization level rather than by individual end
users.

## How C2C connectors use secrets for General Authorization

AWS Secrets Manager is a secret storage service that protects sensitive
credentials such as API keys and tokens. Secrets are encrypted using AWS Key Management Service keys. For more information, see the [AWS Secrets Manager User
Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

For General Authorization, you store authorization credentials in Secrets Manager, and grant
your C2C connector permission to access these secrets. When managed integrations invokes your
connector, it provides the Secrets Manager ARN and version ID. Your connector retrieves the secret
value and uses it to authenticate with the third-party platform.

This approach ensures that managed integrations never handles your long-term credentials directly.
Your connector maintains full control over credential management and token generation,
making the solution extensible to any authorization mechanism supported by your
third-party platform.

###### Important

We recommend that you don't log sensitive credentials or tokens in any logs. If
however they are stored in logs, we recommend that you use CloudWatch Logs data protection
policies to mask the tokens in the logs. For more information, see [Help protect
sensitive log data with masking](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md").

## How to create a secret for General Authorization

To create a secret for General Authorization, follow the steps in [Create an
AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager User Guide.

You must create your secret with a customer-managed AWS KMS key for your
C2C connector to read the secret value. For more information, see [Permissions for the AWS KMS key](../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz "../../../secretsmanager/latest/userguide/security-encryption.md#security-encryption-authz") in the AWS Secrets Manager User Guide.

Store your authorization credentials in the secret using a JSON structure. The exact
format depends on your third-party platform's authorization requirements. Common examples
include:

- API keys: `{"apiKey": "your-api-key-value"}`
- Bearer tokens: `{"token": "your-bearer-token"}`
- Username and password: `{"username": "your-username", "password":
"your-password"}`
- Machine-to-machine OAuth credentials: `{"client_id": "your-client-id",
"client_secret": "your-client-secret", "audience":
"your-audience"}`

You must also configure the IAM policies described in the following section to grant
your C2C connector access to retrieve the secret.

## Grant access for C2C connector to retrieve the secret

To allow managed integrations to retrieve the secret value from Secrets Manager, include the following
permissions in the resource policy for the secret when you create it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "`c2c-connector-account-id`"
      },
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceArn": "arn:aws:iotmanagedintegrations:`region`:`account-id`:account-association/`account-association-id`"
        }
      }
    }
  ]
}
```

This policy grants managed integrations permission to retrieve the secret value on behalf of your
C2C connector. The condition key helps prevent the confused deputy problem by ensuring
that only requests originating from your specific account association can access the
secret.
