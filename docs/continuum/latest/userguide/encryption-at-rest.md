

# Encryption at rest in AWS Continuum

By default, AWS Continuum encrypts all of your data at rest using AWS owned encryption keys. You don't need to configure anything for this default encryption.

You can optionally use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt your data, giving you full control over the encryption keys that protect your resources. AWS Continuum encrypts your content on the server side with that key before it stores it.

You can use resource-level customer managed keys with AWS Continuum. When you create an Environment or a GitHub or GitLab integration, you can specify a KMS key to encrypt the content that belongs to that resource:
+ **Environments** – Encrypts the Environment's content, including security findings, issue details and artifacts, generated patches, context artifacts, and build artifacts.
+ **GitHub and GitLab integrations** – Encrypts the integration's credentials and the content AWS Continuum handles for the integration, such as pull request submissions.

For the required AWS KMS permissions, see [Required AWS KMS permissions](#encryption-at-rest-permissions).

## How AWS Continuum uses customer managed keys
<a name="encryption-at-rest-how-it-works"></a>

AWS Continuum uses the [AWS KMS Hierarchical keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html) to encrypt your data with customer managed keys. When you specify a KMS key while creating a resource, AWS Continuum creates a branch key protected by your KMS key and stores it in a key store. For each encryption operation, the Hierarchical keyring derives a unique wrapping key from the active branch key, which encrypts a unique data key for each object.

The Hierarchical keyring provides the following benefits:
+ **Per-resource encryption scope** – Each Environment and each integration has its own branch key, so data for different resources is encrypted under separate keys.
+ **Fewer calls to AWS KMS** – AWS Continuum caches branch key material for up to 15 minutes, so most operations don't call AWS KMS. This is also the longest time AWS Continuum can keep using a key after you revoke its access.

AWS Continuum doesn't use grants. It accesses your KMS key with your own credentials when it handles your API requests, and with its service principal for work that runs in the background.

### Encryption context
<a name="encryption-at-rest-encryption-context"></a>

AWS Continuum uses an encryption context in every cryptographic operation with your KMS key. The encryption context is a set of non-secret key-value pairs that AWS KMS binds to the ciphertext as additional authenticated data.


| Resource | Encryption context key | Value | 
| --- | --- | --- | 
| Environment | aws:continuum:environment | The Environment's ARN, for example arn:aws:continuum:us-east-1:111122223333:environments/{{environment-id}} | 
| GitHub or GitLab integration | aws-crypto-ec:aws:continuum:integration | The integration's ARN, for example arn:aws:continuum:us-east-1:111122223333:integrations/{{integration-id}} | 

AWS Continuum sets these encryption context keys on its requests to AWS KMS. Use them as shown in key policy conditions and when you search CloudTrail logs.

You can use the encryption context in your key policy to limit how AWS Continuum uses the key to specific resource types or resources. You can also use it to identify AWS Continuum requests in AWS CloudTrail logs.

### Default encryption
<a name="encryption-at-rest-default"></a>

When you create a resource without specifying a customer managed key, AWS Continuum encrypts it with AWS owned keys. No additional configuration is required.

## Prerequisites
<a name="encryption-at-rest-prerequisites"></a>

Before you configure a customer managed key, complete the following prerequisites:
+ Create a symmetric encryption KMS key in AWS KMS, in the same AWS Region where you use AWS Continuum. The key must meet the following requirements:
  + Key type: Symmetric
  + Key usage: Encrypt and decrypt
  + Key spec: `SYMMETRIC_DEFAULT`
  + Key state: Enabled

  For instructions, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.
+ Configure the key policy to grant AWS Continuum the required AWS KMS permissions for the resources you create.

## Required AWS KMS permissions
<a name="encryption-at-rest-permissions"></a>

AWS Continuum accesses your KMS key with two identities:
+ **Your IAM role (synchronous operations)** – When you call a AWS Continuum API, such as `CreateEnvironment`, `CreateCodeScan`, or `GetFinding`, AWS Continuum calls AWS KMS on your behalf with your credentials. These requests include the `kms:ViaService` condition key with the value `continuum.{{region}}.amazonaws.com`, where {{region}} is the AWS Region where you use AWS Continuum. For example, `continuum.us-east-1.amazonaws.com`.
+ **The AWS Continuum service principal (asynchronous operations)** – For work that runs outside your API request, such as scans (including scans triggered by repository events), builds, analysis agents, and branch key rotation, AWS Continuum calls AWS KMS with its service principal, `continuum.amazonaws.com`. These requests include the `aws:SourceArn` condition key set to the ARN of the Environment or integration they act on.

When you create a resource with a customer managed key, AWS Continuum checks that both identities can use the key before it creates anything. It makes a `Decrypt` dry run with your role and another with its service principal, which encrypt no data. If either check fails, the request fails with an `AccessDeniedException` that includes the AWS KMS request ID, and AWS Continuum creates no resource.

### Key policy for Environments
<a name="encryption-at-rest-policy-environments"></a>

The following key policy grants AWS Continuum the permissions required to encrypt and decrypt Environment content.

Replace the following placeholder values in the policy:
+ `111122223333` – Your AWS account ID
+ `MyRole` – The IAM role you use to call AWS Continuum
+ `us-east-1` – The AWS Region where you use AWS Continuum

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowKeyMetadataValidationForEnvironments",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyRole}}" },
      "Action": ["kms:DescribeKey"],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "continuum.{{us-east-1}}.amazonaws.com" }
      }
    },
    {
      "Sid": "AllowBranchKeyCreationAndCallerAccessForEnvironments",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyRole}}" },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "continuum.{{us-east-1}}.amazonaws.com" },
        "StringLike": {
          "kms:EncryptionContext:aws:continuum:environment": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:environments/*"
        }
      }
    },
    {
      "Sid": "AllowAsynchronousDataAccessAndRotationForEnvironments",
      "Effect": "Allow",
      "Principal": { "Service": "continuum.amazonaws.com" },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:continuum:environment": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:environments/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:environments/*"
        }
      }
    }
  ]
}
```

The policy contains three statements:
+ **AllowKeyMetadataValidationForEnvironments** – Grants `kms:DescribeKey` so that AWS Continuum can confirm, when you create an Environment, that your key exists, is enabled, and is a symmetric encryption key. The `kms:ViaService` condition allows the call only through AWS Continuum.
+ **AllowBranchKeyCreationAndCallerAccessForEnvironments** – Grants `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` so that AWS Continuum can create the Environment's branch key with your credentials, and `kms:Decrypt` so that AWS Continuum can check your access at creation and read and write Environment content when you call AWS Continuum APIs. The encryption context condition limits these operations to Environments in your account.
+ **AllowAsynchronousDataAccessAndRotationForEnvironments** – Grants the AWS Continuum service principal `kms:Decrypt` for background work on Environment content, and `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` to rotate the Environment's branch key. This statement also allows the service principal's `Decrypt` dry run when you create an Environment. The encryption context and `aws:SourceArn` conditions limit each request to the Environment it acts on.

Your role doesn't need `kms:GenerateDataKey`. AWS Continuum derives data keys from the branch key, so AWS KMS sees only `kms:Decrypt` when AWS Continuum encrypts content.

**Important**  
To rotate branch keys, your key policy must grant `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` to the AWS Continuum service principal (`continuum.amazonaws.com`). Otherwise branch key rotation fails. For more information, see [Rotate your active branch key](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/rotate-branch-key.html) in the *AWS Encryption SDK Developer Guide*.

### Key policy for GitHub and GitLab integrations
<a name="encryption-at-rest-policy-integrations"></a>

The following key policy grants AWS Continuum the permissions required to encrypt and decrypt integration credentials and content. Amazon Simple Storage Service integrations don't support customer managed keys.

Replace the following placeholder values in the policy:
+ `111122223333` – Your AWS account ID
+ `MyRole` – The IAM role you use to call AWS Continuum
+ `us-east-1` – The AWS Region where you use AWS Continuum

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowKeyMetadataValidationForIntegrations",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyRole}}" },
      "Action": ["kms:DescribeKey"],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "continuum.{{us-east-1}}.amazonaws.com" }
      }
    },
    {
      "Sid": "AllowCallerAccessValidationForIntegrations",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::{{111122223333}}:role/{{MyRole}}" },
      "Action": ["kms:Decrypt", "kms:Encrypt"],
      "Resource": "*",
      "Condition": {
        "StringEquals": { "kms:ViaService": "continuum.{{us-east-1}}.amazonaws.com" },
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:continuum:integration": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:integrations/*"
        }
      }
    },
    {
      "Sid": "AllowServiceKeyValidationForIntegrations",
      "Effect": "Allow",
      "Principal": { "Service": "continuum.amazonaws.com" },
      "Action": ["kms:DescribeKey"],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:integrations/*"
        }
      }
    },
    {
      "Sid": "AllowAsynchronousDataAccessForIntegrations",
      "Effect": "Allow",
      "Principal": { "Service": "continuum.amazonaws.com" },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:continuum:integration": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:integrations/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:continuum:{{us-east-1}}:{{111122223333}}:integrations/*"
        }
      }
    }
  ]
}
```

The policy contains four statements:
+ **AllowKeyMetadataValidationForIntegrations** – Grants `kms:DescribeKey` so that AWS Continuum can confirm, when you create an integration, that your key exists, is enabled, and is a symmetric encryption key.
+ **AllowCallerAccessValidationForIntegrations** – Grants `kms:Decrypt` and `kms:Encrypt` so that AWS Continuum can check, when you create an integration, that you can use the key for that integration. These checks are dry runs and encrypt no data.
+ **AllowServiceKeyValidationForIntegrations** – Grants the AWS Continuum service principal `kms:DescribeKey` so that it can validate your key when it sets up the integration's encryption. `DescribeKey` requests carry no encryption context, so only the `aws:SourceArn` condition limits this statement.
+ **AllowAsynchronousDataAccessForIntegrations** – Grants the AWS Continuum service principal `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` to create the integration's branch key, and `kms:Encrypt` and `kms:Decrypt` to encrypt and decrypt the integration's credentials and content. This statement also allows the service principal's `Decrypt` dry run when you create an integration. The encryption context and `aws:SourceArn` conditions limit each request to the integration it acts on.

**Note**  
To use the same KMS key for Environments and integrations, combine the statements from both policies into one key policy.

## Changing the encryption configuration
<a name="encryption-at-rest-change"></a>

You can't add, change, or remove the KMS key of an existing Environment or integration. To use a different key, create a new resource with that key. Data in the existing resource stays encrypted under its original key.

## Key rotation
<a name="encryption-at-rest-rotation"></a>

When your key policy grants the rotation permissions, AWS Continuum can rotate a resource's branch key. Branch key rotation creates a new active version of the branch key and keeps all earlier versions. After rotation:
+ New data is encrypted with the new branch key version.
+ Data encrypted earlier stays readable with the earlier versions.
+ No data needs to be re-encrypted.

Branch key rotation is separate from AWS KMS key rotation. You can enable automatic rotation of your customer managed key independently. For more information, see [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS Key Management Service Developer Guide*.

## Scoping down access to your KMS key
<a name="encryption-at-rest-scoping"></a>

The example key policies already apply the following controls. You can tighten them further, for example to specific Environment or integration ARNs instead of `*`.
+ **`kms:ViaService`** – Statements for your role require `kms:ViaService` = `continuum.{{region}}.amazonaws.com`, so your role can use the key only through AWS Continuum.
+ **Confused deputy protection (`aws:SourceArn`)** – Every request from the AWS Continuum service principal includes `aws:SourceArn` = the ARN of the Environment or integration it acts on. The `ArnLike` conditions ensure that AWS Continuum can use your key only for your own resources. For more information, see [The confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.
+ **Encryption context** – The `kms:EncryptionContext:aws:continuum:environment` and `kms:EncryptionContext:aws-crypto-ec:aws:continuum:integration` conditions limit each statement to one resource type and to resources in your account.

## Considerations
<a name="encryption-at-rest-considerations"></a>
+ **Customer managed keys apply to new resources only.** Resources created before you configure a customer managed key keep using AWS owned keys. AWS Continuum doesn't migrate existing data.
+ **You specify the key at creation.** You can't add or change the KMS key of an existing resource.
+ **You can use multiple keys.** For example, you can use one key for production Environments and another for test Environments.
+ **Disabling or deleting the key makes data inaccessible.** If you disable the key, schedule it for deletion, or remove the permissions for AWS Continuum, AWS Continuum can't decrypt data encrypted under it, after at most the 15-minute cache period. AWS Continuum operations on affected resources fail until access is restored. Deleting the key permanently prevents access to all data encrypted under it.
+ **AWS KMS quotas apply.** Requests to your key count toward your [AWS KMS request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html). Branch key caching keeps the number of requests low under normal use.

## Monitoring how AWS Continuum uses your KMS key
<a name="encryption-at-rest-monitoring"></a>

You can use AWS CloudTrail to audit the requests AWS Continuum makes to AWS KMS. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in the *AWS Key Management Service Developer Guide*.


| `eventName` | When | Identity | Expected values | 
| --- | --- | --- | --- | 
| DescribeKey | Creating an Environment or integration | Your role, with invokedBy = continuum.amazonaws.com. For integrations, also the AWS Continuum service principal | Your key ARN | 
| Decrypt (dry run) | Creating an Environment or integration | Your role, and the AWS Continuum service principal | errorCode = DryRunOperationException (the check passed); encryptionContext = the new resource's ARN | 
| Encrypt (dry run) | Creating an integration | Your role | errorCode = DryRunOperationException; encryptionContext = aws-crypto-ec:aws:continuum:integration → integration ARN | 
| GenerateDataKeyWithoutPlaintext, ReEncrypt | Creating the resource's branch key, and branch key rotation | Your role at creation; the AWS Continuum service principal for rotation and integrations | encryptionContext includes the resource's ARN | 
| Decrypt | Reading or writing content | Your role for API calls; the AWS Continuum service principal for background work | encryptionContext = the resource's ARN; service principal requests carry the resource's ARN as source ARN | 