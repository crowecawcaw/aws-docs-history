# Customer managed keys for AWS Security Agent

By default, AWS Security Agent encrypts all data at rest using AWS-managed encryption keys. You can optionally use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt your data, giving you full control over the encryption keys that protect your resources.

AWS Security Agent supports resource-level customer managed keys. When you create a top-level resource such as an Agent Space or integration, you can specify a KMS key to encrypt all data belonging to that resource and its subresources. For example, specifying a customer managed key when creating an Agent Space encrypts all data associated with that Agent Space, including Agent Space configurations, penetration test configurations, jobs, and execution details, security findings, discovered endpoints, and screenshots.

## How customer managed keys work

AWS Security Agent uses the [AWS KMS Hierarchical keyring](../../../encryption-sdk/latest/developer-guide/use-hierarchical-keyring.md "../../../encryption-sdk/latest/developer-guide/use-hierarchical-keyring.md") to encrypt your data with customer managed keys. When you specify a KMS key during resource creation, the service creates a branch key protected by your KMS key and stores it in an Amazon DynamoDB-based key store. For each encryption operation, the Hierarchical keyring derives a unique wrapping key from the active branch key, which encrypts a unique data encryption key for each request.

The Hierarchical keyring provides the following benefits:

- **Per-resource encryption scope** – Each top-level resource has its own branch key, so data for different resources is encrypted under separate keys.
- **Automatic key rotation** – AWS Security Agent periodically rotates branch keys. After rotation, new data is encrypted with the new branch key version, while older versions are retained to decrypt previously encrypted data.

### Encryption context

AWS Security Agent uses encryption context in all cryptographic operations with your KMS key. The encryption context is a set of non-secret key-value pairs that provides additional authenticated data for the encryption operation.

The encryption context key follows the format `aws:securityagent:_<resource-type>_`, where `*<resource-type>*` is the type of resource being encrypted (for example, `agent-space` or `integration`). The value is the Amazon Resource Name (ARN) of the resource.

You can use the encryption context to scope down your KMS key policy to specific resource types. For more information, see [Configure a KMS key policy](#cmk-key-policy "#cmk-key-policy").

### Default encryption

When you create a resource without specifying a customer managed key, AWS Security Agent encrypts the resource using AWS-managed encryption keys provided by the underlying storage services (Amazon DynamoDB and Amazon S3). No additional configuration is required for default encryption.

### Default KMS key for applications

You can set a default KMS key at the application level. When a default KMS key is configured, AWS Security Agent uses it as the fallback for new Agent Spaces and integrations when you don’t explicitly specify a KMS key during resource creation.

To set a default KMS key, specify the `defaultKmsKeyId` parameter when creating or updating your application using the AWS CLI or SDK. The console prompts you to specify a default KMS key during application setup.

When you explicitly specify a KMS key during resource creation, it takes precedence over the application-level default.

## Prerequisites

Before you configure a customer managed key, complete the following prerequisites:

- Create a symmetric encryption KMS key in AWS KMS. The key must meet the following requirements:
  - Key type: Symmetric
  - Key usage: Encrypt and decrypt
  - Key spec: `SYMMETRIC_DEFAULT`
  - Key state: Enabled

  For instructions, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

- Configure the KMS key policy to grant AWS Security Agent the required permissions. For details, see [Configure a KMS key policy](#cmk-key-policy "#cmk-key-policy").

## Configure a KMS key policy

Your KMS key policy must grant AWS Security Agent permission to use the key for cryptographic operations. The required permissions depend on which resource types you plan to encrypt.

AWS Security Agent accesses your KMS key using different identities depending on the operation:

- **AWS Management Console operations** – When administrators create or manage resources in the AWS Console (for example, creating an Agent Space or updating an application), the service uses your IAM credentials to call AWS KMS.
- **Web application operations** – When users access data through the AWS Security Agent web application (for example, viewing penetration test results or starting a penetration test), the service uses the application role created during AWS Security Agent setup to call AWS KMS.
- **Asynchronous workflows** – For background operations that run outside of any user session (for example, penetration testing execution, code review processing, and branch key rotation), the service uses its own service principal (`securityagent.amazonaws.com`) to call AWS KMS on your behalf.

Your key policy must include statements for all three identities.

### Key policy for Agent Spaces

The following key policy grants AWS Security Agent the permissions required to encrypt and decrypt Agent Space data, including penetration test results and screenshots.

Replace the following placeholder values in the policy:

- `*111122223333*` – Your AWS account ID
- `*MyRole*` – The IAM role you use to manage AWS Security Agent in the console
- `*MyApplicationRole*` – The application role created during AWS Security Agent setup
- `*us-east-1*` – The AWS Region where you use AWS Security Agent

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowKeyMetadataValidationForApplicationAndAgentSpaces",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyRole"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowUseOfHierarchicalKeyringForAgentSpaces",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyRole"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncrypt*",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:agent-space": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        },
        "StringEquals": {
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowSynchronousDataAccessForAgentSpaces",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyApplicationRole"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:agent-space": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        },
        "StringEquals": {
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowAsynchronousDataAccessForAgentSpaces",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:agent-space": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        }
      }
    }
  ]
}
```

###### Important

To rotate branch keys, your KMS key policy must grant `kms:GenerateDataKeyWithoutPlaintext` and `kms:ReEncrypt*` permissions to the AWS Security Agent service principal (`securityagent.amazonaws.com`), or branch key rotation will fail. For more information about the required permissions, see [Rotate a branch key](../../../database-encryption-sdk/latest/devguide/rotate-branch-key.md "../../../database-encryption-sdk/latest/devguide/rotate-branch-key.md").

### Key policy for integrations

The following key policy grants AWS Security Agent the permissions required to encrypt and decrypt integration data, including code review findings.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowKeyAccessValidationForIntegrations",
      "Effect": "Allow",
      "Principal": {
          "AWS": "arn:aws:iam::111122223333:role/MyRole"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:securityagent:integration": "arn:aws:securityagent:us-east-1:111122223333:integration/*"
        },
        "StringEquals": {
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowKeyMetadataValidationForIntegrations",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },
    {
      "Sid": "AllowAsynchronousDataAccessForIntegrations",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:securityagent:us-east-1:111122223333:integration/*"
        },
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:securityagent:integration": "arn:aws:securityagent:us-east-1:111122223333:integration/*"
        }
      }
    }
  ]
}
```

###### Note

You can combine the Agent Space and integration key policy statements into a single key policy if you want to use the same KMS key for both resource types.

### IAM policy for the application role

In addition to the KMS key policy, attach the following IAM policy to the application role specified during AWS Security Agent setup. This policy grants the role permissions to use your customer managed keys for encrypting and decrypting Agent Space data and creating secrets in AWS Secrets Manager.

Replace the following placeholder values in the policy:

- `*111122223333*` – Your AWS account ID
- `*us-east-1*` – The AWS Region where you use AWS Security Agent
- The KMS key ARNs in `Resource` – The ARNs of your KMS keys

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSynchronousDataAccessForAgentSpaces",
      "Effect": "Allow",
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890cd"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333",
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:agent-space": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyAccessForCreatingSecrets",
      "Effect": "Allow",
      "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890cd"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "secretsmanager.*.amazonaws.com",
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-1:111122223333:secret:*"
        }
      }
    }
  ]
}
```

###### Note

The application role is an IAM role that you specify or that the console creates during AWS Security Agent setup. The web application assumes this role to retrieve penetration test execution logs and create Secrets Manager secrets on your behalf.

The `AllowKmsKeyAccessForCreatingSecrets` statement is required if you configure authentication resources for penetration tests and choose to enter credentials directly instead of specifying an existing secret. The web application creates a secret on your behalf, and the application role needs the permissions in this statement to encrypt the secret with the customer managed key specified for your Agent Space. Update the `Resource` ARNs in this statement to match the KMS key used for your Agent Space.

If your CloudWatch Logs log group for storing penetration test execution logs is encrypted with a customer managed key, you must update the KMS key policy to allow CloudWatch Logs to decrypt log events. Otherwise, the web application cannot display log events. For instructions, see [Encrypt log data in CloudWatch Logs using AWS KMS](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md").

## Create a resource with a customer managed key

You can specify a customer managed key when setting up AWS Security Agent or when creating individual resources. The KMS key encrypts all data belonging to that resource and its subresources.

### Set a default KMS key during setup (console)

You can configure a default KMS key during the initial AWS Security Agent setup. This key is used as the default for new Agent Spaces and integrations unless you specify a different key.

1. On the **Set up AWS Security Agent** page, expand the **Encryption - optional** section.
2. Select **Customize encryption settings (advanced)**.
3. For **Choose an AWS KMS key**, select a KMS key from your account, or enter a KMS key ARN.
4. Complete the remaining setup steps and choose **Set up AWS Security Agent**.

AWS Security Agent validates the KMS key to confirm that it exists, is enabled, and uses symmetric encryption. If validation fails, setup does not proceed and you receive an error message.

### Create an Agent Space with a customer managed key (console)

1. In the AWS Security Agent console, navigate to the **Agent Spaces** page.
2. Choose **Create Agent Space**.
3. Enter a name and optional description for your Agent Space.
4. Expand the **Advanced** section.
5. Under **Data encryption**, choose one of the following:
   - **Use application default key** – Uses the default KMS key configured during AWS Security Agent setup. This option is selected by default if a default key is configured.
   - **Use a different key** – Specify a different KMS key for this Agent Space. Select **Customize encryption settings (advanced)**, then for **Choose an AWS KMS key**, select a KMS key from your account or enter an ARN.

6. Choose **Create**.

### Create an integration with a customer managed key (console)

1. In the AWS Security Agent console, navigate to the **Integrations** page.
2. Choose **Add integration** and select your provider (for example, GitHub).
3. Complete **Step 1: Install and authorize** the provider application.
4. In **Step 2: Register details**, enter a registration name and configure the provider settings.
5. In the **Data encryption** section, select **Customize encryption settings (advanced)**.
6. For **Choose an AWS KMS key**, select a KMS key from your account, or enter a KMS key ARN.
7. Choose **Connect**.

### Create a resource with a customer managed key (AWS CLI or SDK)

To specify a customer managed key using the AWS CLI or SDK:

- Include the `defaultKmsKeyId` parameter when calling `CreateApplication` to set a default KMS key for your application. This key is used as the fallback when creating Agent Spaces or integrations without an explicit KMS key.
- Include the `kmsKeyId` parameter when calling `CreateAgentSpace` or `CreateIntegration` to encrypt a specific resource. This takes precedence over the application-level default.

For parameter details, see the [AWS Security Agent API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

If you don’t specify a KMS key, AWS Security Agent uses the application-level default KMS key if one is configured. Otherwise, the resource is encrypted with AWS-managed keys.

## Key rotation

AWS Security Agent automatically rotates branch keys on a periodic basis. Branch key rotation creates a new active version of the branch key while retaining all previous versions. After rotation:

- New data is encrypted with the new branch key version.
- Previously encrypted data remains decryptable using the older branch key version.
- No data re-encryption is required.

Branch key rotation is separate from KMS key rotation. You can enable automatic KMS key rotation for your customer managed key independently. For more information, see [Rotating KMS keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS Key Management Service Developer Guide_.

After a branch key rotation, there is a brief period during which cached copies of the previous branch key may still be used for new encryption operations. This window is determined by the internal cache time-to-live (TTL) and does not affect the security of your data.

## Considerations

Keep the following in mind when using customer managed keys with AWS Security Agent:

- **Customer managed keys apply to new resources only.** Existing resources created before you configure a customer managed key continue to use AWS-managed encryption. There is no migration of existing data.
- **Customer managed keys are specified at creation time.** You specify the KMS key when creating a resource. You cannot add or change the KMS key for an existing resource.
- **Multiple KMS keys are supported.** You can use different KMS keys for different resources. For example, you can use one key for production Agent Spaces and a different key for development Agent Spaces.
- **Disabling or deleting a KMS key makes data inaccessible.** If you disable or schedule deletion of a KMS key, AWS Security Agent cannot decrypt data encrypted under that key. Affected resources become inaccessible until the key is re-enabled. Deleting a KMS key permanently prevents access to all data encrypted under that key.
- **Key policy permissions are required.** If you remove the required permissions from your KMS key policy, AWS Security Agent cannot access encrypted data. Ensure that the key policy grants permissions for your IAM role, the web application role, and the service principal as described in [Configure a KMS key policy](#cmk-key-policy "#cmk-key-policy").
- **AWS KMS quotas apply.** Cryptographic operations against your KMS key count toward your AWS KMS request quotas. Under normal usage, the hierarchical keyring architecture minimizes KMS calls through branch key caching. For more information, see [Request quotas](../../../kms/latest/developerguide/requests-per-second.md "../../../kms/latest/developerguide/requests-per-second.md") in the _AWS Key Management Service Developer Guide_.
