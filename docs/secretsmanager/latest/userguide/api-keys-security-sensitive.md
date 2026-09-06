

# Manage API keys for security-sensitive workloads
<a name="api-keys-security-sensitive"></a>

AWS Secrets Manager helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets throughout their lifecycles. This page provides prescriptive guidance for managing API keys and third-party credentials in security-sensitive workloads. Combine automatic rotation with customer managed AWS KMS keys and least-privilege IAM policies. Also configure VPC endpoint access to minimize the exposure window and blast radius of a compromised credential.

## Store API keys in AWS Secrets Manager
<a name="api-keys-storage"></a>

This section describes how to structure your API key secrets for optimal rotation and retrieval. Store each API key as a separate secret with a structured JSON value. With this structure, your application can retrieve individual fields, and Secrets Manager can pass the correct values to a rotation function.

The following example shows a common JSON structure for third-party API key secrets. The actual fields depend on the requirements of your provider — review the provider's documentation for the specific credentials and metadata you need to store.

```
{
  "apiKey": "your-api-key-value",
  "apiKeyId": "key-identifier",
  "endpoint": "https://api.example.com/v1",
  "provider": "example-service"
}
```


**Example secret structure for API keys**  

| Field | Example value | Purpose | 
| --- | --- | --- | 
| `apiKey` | `sk_live_abc123...` | The credential value your application uses to authenticate with the third-party API. | 
| `apiKeyId` | `key_001` | Identifier for the key on the provider's side. Used during rotation to create a new key and delete the old one. | 
| `endpoint` | `https://api.example.com/v1` | API endpoint URL. Store with the key so retrieval returns everything the application needs to connect. | 
| `provider` | `stripe` | Provider name. Useful for tagging, filtering, and rotation function logic that handles multiple providers. | 

Tag each secret with metadata to support IAM policy conditions and organizational filtering. For example, you can tag secrets with the owning team, environment, and compliance scope using the AWS CLI or console:

```
aws secretsmanager tag-resource \
    --secret-id prod/payments/stripe-api-key \
    --tags Key=Team,Value=payments Key=Environment,Value=production \
           Key=Provider,Value=stripe Key=Compliance,Value=pci-dss
```

For more information about creating secrets, see [Create an AWS Secrets Manager secret](create_secret.md).

## Encryption configuration
<a name="api-keys-encryption"></a>

Secrets Manager encrypts every secret value at rest using a AWS KMS key. For security-sensitive workloads, choose the encryption key based on your compliance and access control requirements.


**KMS key options for API key secrets**  

| Key type | When to use | Security considerations | 
| --- | --- | --- | 
| AWS managed key (`aws/secretsmanager`) | Default for most workloads. No additional cost or key management overhead. | The key policy is restricted to Secrets Manager operations only and cannot be modified. Cannot be used for cross-account access. | 
| Customer managed key | Compliance requirements (for example, PCI DSS, HIPAA, SOC 2, or other applicable standards). Cross-account secret sharing. Key usage auditing requirements. | You control the key policy. You can restrict which principals can decrypt. You can disable or schedule key deletion independently of the secret. Provides an independent audit trail through . | 

For security-sensitive workloads, use a customer managed key with the following key policy conditions:
+ `kms:ViaService` – Restrict key usage to requests originating from Secrets Manager (`secretsmanager.<region>.amazonaws.com`).
+ `kms:EncryptionContext:SecretARN` – Restrict decryption to specific secret ARNs by matching the Secrets Manager encryption context.
+ Separate keys per compliance boundary – Use different AWS KMS keys for secrets in different compliance scopes (for example, PCI compared to non-PCI).

For a complete explanation of the encryption and decryption process, see [Secret encryption and decryption in AWS Secrets Manager](security-encryption.md).

## Automatic rotation for API keys
<a name="api-keys-rotation"></a>

Automatic rotation reduces the exposure window of compromised credentials. Secrets Manager invokes a Lambda function on a schedule. The function creates a new API key at the provider, updates the secret value, and deletes the old key.

Secrets Manager provides managed rotation functions for some third-party providers through managed external secrets. For more information about this feature and the list of supported providers, see [Managed external secrets Partners](mes-partners.md). For providers without managed rotation support, you implement a custom Lambda rotation function that calls the provider's API to create and delete keys.

### Rotation function lifecycle
<a name="api-keys-rotation-function"></a>

A rotation Lambda function implements four steps. Secrets Manager invokes the function once for each step, passing a `Step` parameter. If any step fails, Secrets Manager automatically retries the entire rotation.


**Rotation steps for API keys**  

| Step | Action for API keys | Failure handling | 
| --- | --- | --- | 
| `createSecret` | Call the provider API to create a new key. Store the new key value in Secrets Manager with the `AWSPENDING` staging label. | If key creation fails, the rotation does not move on to the next step. The existing key remains active as `AWSCURRENT`. | 
| `setSecret` | For API keys created at the provider, this step is typically a no-op. This step is used when a random key is generated in Secrets Manager and needs to be set at the provider — which is not the typical API key flow. | If this step fails, the rotation does not proceed to `testSecret`. | 
| `testSecret` | Retrieve the `AWSPENDING` value from Secrets Manager and make a test API call to the provider to verify the new key works. | If the test fails, delete the pending key at the provider and raise an exception. | 
| `finishSecret` | Move `AWSCURRENT` to the new key. The old key moves to `AWSPREVIOUS`. Optionally delete the old key at the provider. | If the label update fails, the rotation does not complete. The new key exists but is not yet labeled `AWSCURRENT`. | 

For the complete rotation function template and implementation guidance, see [Lambda rotation functions](rotate-secrets_lambda-functions.md).

### Rotation schedule configuration
<a name="api-keys-rotation-schedule"></a>

Set the rotation interval based on your compliance requirements and internal security policies. Refer to the applicable compliance standards for your workload to determine the appropriate rotation frequency.

Use a rotation window to control when rotation occurs. This prevents rotation from running during peak traffic or maintenance windows:

```
aws secretsmanager rotate-secret \
    --secret-id prod/payments/stripe-api-key \
    --rotation-rules '{
        "ScheduleExpression": "cron(0 4 ? * SUN *)",
        "Duration": "2h"
    }'
```

For schedule expression syntax, see [Rotation schedules](rotate-secrets_schedule.md).

## Retrieve secrets efficiently
<a name="api-keys-access-patterns"></a>

Secrets Manager supports 10,000 transactions per second on `GetSecretValue` calls. Most applications do not experience throttling. For applications with very high call volumes or latency-sensitive paths, use a caching solution to reduce API calls and improve response times.

Secrets Manager provides caching clients for several languages, as well as a Lambda extension that caches secrets locally within the execution environment. For more information about caching options, see [Get a Secrets Manager secret value using Java with client-side caching](retrieving-secrets_cache-java.md), [Get a Secrets Manager secret value using Python with client-side caching](retrieving-secrets_cache-python.md), and [Get a Secrets Manager secret value using Go with client-side caching](retrieving-secrets_cache-go.md).

For all access patterns, configure IAM policies that restrict `secretsmanager:GetSecretValue` to the specific secrets each application needs:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Allow",
    "Action": "secretsmanager:GetSecretValue",
    "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:prod/payments/*",
    "Condition": {
      "StringEquals": {
        "aws:ResourceTag/Environment": "production"
      }
    }
  }]
}
```

## Security hardening for sensitive workloads
<a name="api-keys-security-hardening"></a>

The following practices provide defense in depth for API keys in environments with strict security requirements (for example, PCI DSS, SOC 2, HIPAA, or other applicable compliance frameworks):

**Restrict network access with VPC endpoints**  
Create an interface VPC endpoint for Secrets Manager so secret retrieval never traverses the public internet. Apply an endpoint policy that restricts which secrets can be accessed through the endpoint. For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md).

**Apply resource policies to secrets**  
Attach a resource policy to each secret that explicitly denies access from principals outside your account or outside specific VPC endpoints. This provides a second authorization boundary independent of IAM identity policies.

**Monitor secret access with **  
 automatically logs all Secrets Manager API calls, including `GetSecretValue`, `PutSecretValue`, and `RotateSecret`. For security-sensitive secrets, create a Amazon CloudWatch alarm that triggers on unexpected `GetSecretValue` calls — for example, calls from unrecognized source IP addresses or IAM principals.

**Use `AWSPREVIOUS` for graceful rotation**  
During rotation, Secrets Manager maintains the previous key value with the `AWSPREVIOUS` staging label. If your provider invalidates the previous key when a new key is created, configure your application to fall back to `AWSPREVIOUS` if `AWSCURRENT` returns an authentication error. This prevents downtime during the brief window between key creation and label update.

**Validate resource policies before attaching**  
Secrets without a resource policy already block public access. When you attach a resource policy to your secret, use the `ValidateResourcePolicy` API to ensure your policy does not grant broad public access. You can also use the `BlockPublicPolicy` parameter with `PutResourcePolicy` to prevent attaching policies that grant public access. Use the `aws:PrincipalOrgID` condition key in resource policies to prevent access from principals outside your organization.

## Frequently asked questions
<a name="api-keys-faq"></a>

This section answers common questions about API key rotation and secret management in AWS Secrets Manager.

### How do I handle the overlap period during rotation?
<a name="api-keys-faq-overlap"></a>

This is only necessary if the provider invalidates the existing key when a new key is created. If the provider supports multiple active keys simultaneously, both keys work during the rotation period without application-side fallback logic. For providers that invalidate the old key, configure your application to retry with `AWSPREVIOUS` if the current key returns a 401 or 403 error. Delete the old key at the provider in the `finishSecret` step only after you confirm the new key is working.

### What if my provider doesn't support programmatic key creation?
<a name="api-keys-faq-not-rotating"></a>

If the provider requires manual key creation (through a web console, for example), you can't fully automate rotation. Instead, use a rotation function that sends a notification (through Amazon Simple Notification Service) when rotation is due, prompting an operator to create the key manually and update the secret value. Set the rotation schedule to match your compliance rotation requirement and use Amazon CloudWatch alarms on `days_since_last_rotation` to detect missed rotations.

### How do I avoid API throttling when retrieving secrets?
<a name="api-keys-faq-throttling"></a>

Secrets Manager supports 10,000 transactions per second on `GetSecretValue`. Most applications do not experience throttling. If your application makes an exceptionally high volume of calls, use a caching client or the Lambda Parameters and Secrets extension. These cache the secret value in memory and refresh periodically, reducing the number of API calls. Set the cache TTL to a value shorter than your rotation interval so the application picks up new keys after rotation.

### Should I use one secret per environment or one secret with versions?
<a name="api-keys-faq-multiple-environments"></a>

Use separate secrets for each environment (for example, `prod/payments/stripe` and `dev/payments/stripe`). This allows different IAM policies, rotation schedules, and encryption keys per environment. Secret versions (staging labels) are for rotation state management, not environment separation.