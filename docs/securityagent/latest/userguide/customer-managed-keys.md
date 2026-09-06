

# Customer managed keys for AWS Security Agent
<a name="customer-managed-keys"></a>

By default, AWS Security Agent encrypts all data at rest using AWS-managed encryption keys. You can optionally use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt your data, giving you full control over the encryption keys that protect your resources.

 AWS Security Agent supports resource-level customer managed keys. When you create a top-level resource such as an Agent Space or integration, you can specify a KMS key to encrypt all data belonging to that resource and its subresources. For example, specifying a customer managed key when creating an Agent Space encrypts all data associated with that Agent Space, including Agent Space configurations, penetration test configurations, jobs, and execution details, security findings, discovered endpoints, and screenshots. You can also provide AWS resources that are already encrypted with your own customer managed key, such as S3 buckets, CloudWatch Logs log groups, or Secrets Manager secrets. For the required KMS permissions, see [Required KMS permissions](#cmk-required-permissions).

## How customer managed keys work
<a name="_how_customer_managed_keys_work"></a>

 AWS Security Agent uses the [AWS KMS Hierarchical keyring](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/use-hierarchical-keyring.html) to encrypt your data with customer managed keys. When you specify a KMS key during resource creation, the service creates a branch key protected by your KMS key and stores it in an Amazon DynamoDB-based key store. For each encryption operation, the Hierarchical keyring derives a unique wrapping key from the active branch key, which encrypts a unique data encryption key for each request.

The Hierarchical keyring provides the following benefits:
+  **Per-resource encryption scope** – Each top-level resource has its own branch key, so data for different resources is encrypted under separate keys.
+  **Automatic key rotation** – AWS Security Agent periodically rotates branch keys. After rotation, new data is encrypted with the new branch key version, while older versions are retained to decrypt previously encrypted data.

### Encryption context
<a name="_encryption_context"></a>

 AWS Security Agent uses encryption context in all cryptographic operations with your KMS key. The encryption context is a set of non-secret key-value pairs that provides additional authenticated data for the encryption operation.

The encryption context key follows the format `aws:securityagent:_<resource-type>_`, where ` <resource-type> ` is the type of resource being encrypted (for example, `agent-space` or `integration`). The value is the Amazon Resource Name (ARN) of the resource.

**Note**  
For integrations, the encryption context key includes the `aws-crypto-ec:` prefix, resulting in the format `aws-crypto-ec:aws:securityagent:integration`.

You can use the encryption context to scope down your KMS key policy to specific resource types. For more information, see [Required KMS permissions](#cmk-required-permissions).

### Default encryption
<a name="_default_encryption"></a>

When you create a resource without specifying a customer managed key, AWS Security Agent encrypts the resource using AWS-managed encryption keys provided by the underlying storage services (Amazon DynamoDB and Amazon S3). No additional configuration is required for default encryption.

### Default KMS key for applications
<a name="_default_kms_key_for_applications"></a>

You can set a default KMS key at the application level. When a default KMS key is configured, AWS Security Agent uses it as the fallback for new Agent Spaces and integrations when you don’t explicitly specify a KMS key during resource creation.

To set a default KMS key, specify the `defaultKmsKeyId` parameter when creating or updating your application using the AWS CLI or SDK. The console prompts you to specify a default KMS key during application setup.

When you explicitly specify a KMS key during resource creation, it takes precedence over the application-level default.

## Prerequisites
<a name="_prerequisites"></a>

Before you configure a customer managed key, complete the following prerequisites:
+ Create a symmetric encryption KMS key in AWS KMS. The key must meet the following requirements:
  + Key type: Symmetric
  + Key usage: Encrypt and decrypt
  + Key spec: `SYMMETRIC_DEFAULT` 
  + Key state: Enabled

    For instructions, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the * AWS Key Management Service Developer Guide*.
+ Configure the KMS key policy and IAM policies to grant AWS Security Agent the required permissions. For details, see [Required KMS permissions](#cmk-required-permissions).

## Required KMS permissions
<a name="cmk-required-permissions"></a>

 AWS Security Agent requires KMS permissions in two scenarios:
+  **Encrypting data within AWS Security Agent** – When you specify a customer managed key for an Agent Space or integration, the service needs permissions to use that key for cryptographic operations on your data.
+  **Using CMK-encrypted AWS resources** – When you provide AWS resources encrypted with a customer managed key (such as S3 buckets, CloudWatch Logs log groups, or Secrets Manager secrets), the service needs permissions to use those keys to access the encrypted resources.

 AWS Security Agent accesses your KMS key using different identities depending on the operation:
+  ** AWS Management Console operations** – When administrators create or manage resources in the AWS Management Console (for example, creating an Agent Space or updating an application), the service uses the administrator role to call AWS KMS.
+  **Web application operations** – When IAM Identity Center users access data through the AWS Security Agent web application (for example, viewing penetration test results or starting a penetration test), the service uses the application role created during AWS Security Agent setup to call AWS KMS.
+  **Accessing customer-provided resources** – When the service accesses customer-provided AWS resources during penetration testing (such as S3 buckets, CloudWatch Logs log groups, and Secrets Manager secrets), it uses the penetration test service role to call AWS KMS.
+  **Asynchronous workflows** – For background operations that run outside of any user session (for example, penetration testing execution, code review processing, and branch key rotation), the service uses its own service principal (`securityagent.amazonaws.com`) to call AWS KMS on your behalf.

The following sections describe the required permissions for each identity.

### Key policy
<a name="cmk-key-policy"></a>

Your KMS key policy must grant AWS Security Agent permission to use the key for cryptographic operations. The required key policy statements depend on which resource types you plan to encrypt and which CMK-encrypted AWS resources you provide to the service.

#### Key policy for Agent Spaces
<a name="_key_policy_for_agent_spaces"></a>

The following key policy grants AWS Security Agent the permissions required to encrypt and decrypt Agent Space data, including penetration test results and screenshots.

Replace the following placeholder values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` MyRole ` – The IAM role you use to manage AWS Security Agent in the console
+  ` MyApplicationRole ` – The application role created during AWS Security Agent setup
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent

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
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
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
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
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
    },
    {
      "Sid": "AllowAsynchronousDataAccessForCodeRemediation",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*"
    }
  ]
}
```

**Important**  
To rotate branch keys, your KMS key policy must grant `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` permissions to the AWS Security Agent service principal (`securityagent.amazonaws.com`), or branch key rotation will fail. For more information about the required permissions, see [Rotate a branch key](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/rotate-branch-key.html).

#### Key policy for integrations
<a name="_key_policy_for_integrations"></a>

The following key policy grants AWS Security Agent the permissions required to encrypt and decrypt integration data, including code review findings.

Replace the following placeholder values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` MyRole ` – The IAM role you use to manage AWS Security Agent in the console
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent

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
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
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
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
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

**Note**  
You can combine the Agent Space, integration, and security requirement pack key policy statements into a single key policy if you want to use the same KMS key for multiple resource types.

#### Key policy for security requirement packs
<a name="_key_policy_for_security_requirement_packs"></a>

The following key policy grants AWS Security Agent the permissions required to encrypt and decrypt security requirement pack data. Security requirement packs do not use a web application role. The policy uses two access paths:
+  **Synchronous path** – When you call the API, the service uses your forwarded credentials to call AWS KMS on your behalf (via the `kms:ViaService` condition).
+  **Asynchronous path** – For asynchronous operations where the packs can be used, the service uses its own service principal to call AWS KMS directly.

Replace the following values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` MyRole ` – The IAM role you use to invoke security requirement pack operations
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowKeyMetadataValidation",
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
      "Sid": "AllowUseOfHierarchicalKeyringForSecurityPacks",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyRole"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "securityagent.us-east-1.amazonaws.com"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:security-requirement-pack": "arn:aws:securityagent:us-east-1:111122223333:security-requirement-pack/*"
        }
      }
    },
    {
      "Sid": "AllowAsynchronousDataAccessForSecurityPacks",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Decrypt",
        "kms:ReEncryptTo",
        "kms:ReEncryptFrom"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:securityagent:security-requirement-pack": "arn:aws:securityagent:us-east-1:111122223333:security-requirement-pack/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:securityagent:us-east-1:111122223333:security-requirement-pack/*"
        }
      }
    }
  ]
}
```

The policy contains three statements:
+  **AllowKeyMetadataValidation** – Grants `kms:DescribeKey` so that AWS Security Agent can validate that your customer managed key exists, is enabled, and uses symmetric encryption when you specify a CMK during resource creation. Uses the `kms:ViaService` condition to ensure the call originates through the service.
+  **AllowUseOfHierarchicalKeyringForSecurityPacks** – Grants `kms:GenerateDataKeyWithoutPlaintext` (create new branch keys), `kms:ReEncryptTo` and `kms:ReEncryptFrom` (rotate existing branch keys), and `kms:Decrypt` (retrieve existing branch keys) for hierarchical keyring operations. These operations use your forwarded credentials through the synchronous path and are scoped to security requirement pack resources by the encryption context condition.
+  **AllowAsynchronousDataAccessForSecurityPacks** – Grants `kms:GenerateDataKeyWithoutPlaintext`, `kms:Decrypt`, `kms:ReEncryptTo`, and `kms:ReEncryptFrom` to the AWS Security Agent service principal for asynchronous operations when no caller credentials are available.

Unlike the Agent Spaces key policy, the security requirement pack policy does not include a web application role principal. Security requirement packs are accessed through the AWS Management Console using your administrator role, not through the AWS Security Agent web application. All synchronous operations use the single caller role (via `kms:ViaService`).

**Note**  
If you use the same KMS key for both Agent Spaces and security requirement packs, you can combine the key policy statements from both sections into a single key policy.

#### Key policy for CMK-encrypted AWS resources
<a name="key_policy_for_cmk_encrypted_shared_aws_resources"></a>

If you provide AWS resources encrypted with a customer managed key to AWS Security Agent, you must update the key policy on each resource’s KMS key to grant the necessary permissions. This applies to the following resources:
+  **S3 buckets** – If you provide learning resources from an S3 bucket encrypted with a customer managed key (SSE-KMS), the key policy must allow the penetration test service role to decrypt objects.
+  **Secrets Manager secrets** – If your penetration test credentials are stored in Secrets Manager secrets encrypted with a customer managed key, the key policy must allow the penetration test service role to decrypt those secrets. If the web application creates secrets on your behalf, the key policy must also allow the application role to encrypt those secrets.
+  **CloudWatch Logs log groups** – If the CloudWatch Logs log group used for storing penetration test execution logs is encrypted with a customer managed key, the key policy must allow CloudWatch Logs to validate the KMS key through the service role and allow the CloudWatch Logs service principal to perform cryptographic operations.

**Important**  
 AWS Security Agent may also create CloudWatch Logs log groups and Secrets Manager secrets on your behalf. When configuring your KMS key policy, include the corresponding statements for these service-created resources as well.

The following key policy statements grant the required permissions for CMK-encrypted resources. Include only the statements that apply to your configuration. If a resource uses the same KMS key you specified for your Agent Space, add these statements to that key’s policy. If a resource uses a different KMS key, add these statements to that key’s policy instead.

Replace the following placeholder values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` MyApplicationRole ` – The application role created during AWS Security Agent setup
+  ` MyPenTestServiceRole ` – The penetration test service role
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowKmsKeyAccessForCreatingSecrets",
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
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "secretsmanager.*.amazonaws.com",
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-1:111122223333:secret:*"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyDecryptionForS3Objects",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyPenTestServiceRole"
      },
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "s3.*.amazonaws.com",
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::YOUR-BUCKET-NAME*"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyDecryptionForSecretsManagerSecrets",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyPenTestServiceRole"
      },
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "secretsmanager.*.amazonaws.com",
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-1:111122223333:secret:YOUR-SECRET-NAME*"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyValidationForCloudWatchLogsLogGroups",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/MyPenTestServiceRole"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "logs.*.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyAccessForCloudWatchLogsLogGroups",
      "Effect": "Allow",
      "Principal": {
        "Service": "logs.us-east-1.amazonaws.com"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:logs:arn": "arn:aws:logs:us-east-1:111122223333:log-group:YOUR-LOG-GROUP-NAME*"
        }
      }
    }
  ]
}
```

**Note**  
The `AllowKmsKeyDecryptionForS3Objects` statement is required only if you provide learning resources from S3 buckets encrypted with a customer managed key. For more information about configuring SSE-KMS for S3, see [Protecting data with SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).
The `AllowKmsKeyDecryptionForSecretsManagerSecrets` statement is required only if your penetration test credentials are stored in Secrets Manager secrets encrypted with a customer managed key. The service role needs access to decrypt secrets during penetration testing. For more information about secret encryption, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).
The `AllowKmsKeyValidationForCloudWatchLogsLogGroups` statement grants the service role `kms:DescribeKey` so that CloudWatch Logs can validate the KMS key through the service role when associating it with a log group.
The `AllowKmsKeyAccessForCreatingSecrets` statement is required if the web application creates Secrets Manager secrets on your behalf using a customer managed key. The application role needs `kms:GenerateDataKey` and `kms:Decrypt` to encrypt the secret with your KMS key.
The `AllowKmsKeyAccessForCloudWatchLogsLogGroups` statement grants the CloudWatch Logs service principal (`logs.us-east-1.amazonaws.com`) the permissions it requires to encrypt and decrypt log data. This statement is also required if AWS Security Agent creates a log group on your behalf when you don’t provide an existing one. For more information, see [Encrypt log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).
If multiple resources share the same KMS key, you can combine the statements into a single key policy.

### Administrator role
<a name="cmk-admin-role"></a>

No additional IAM policy is required for the administrator role (the IAM role you use to manage AWS Security Agent in the console).

### Application role
<a name="cmk-application-role"></a>

In addition to the KMS key policy, attach the following IAM policy to the application role specified during AWS Security Agent setup. This policy grants the role permissions to use your customer managed keys for encrypting and decrypting Agent Space data and creating secrets in AWS Secrets Manager.

Replace the following placeholder values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent
+ The KMS key ARNs in `Resource` – The ARNs of your KMS keys

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

**Note**  
The application role is an IAM role that you specify or that the console creates during AWS Security Agent setup. The web application assumes this role to retrieve penetration test execution logs and create Secrets Manager secrets on your behalf.  
The `AllowKmsKeyAccessForCreatingSecrets` statement is required if you configure authentication resources for penetration tests and choose to enter credentials directly instead of specifying an existing secret. The web application creates a secret on your behalf, and the application role needs the permissions in this statement to encrypt the secret with the customer managed key specified for your Agent Space. Update the `Resource` ARNs in this statement to match the KMS key used for your Agent Space.

### Service role
<a name="cmk-service-role"></a>

During penetration testing, AWS Security Agent assumes the penetration test service role to access your AWS resources. If any of these resources are encrypted with a customer managed key, you must grant the service role permissions to use the corresponding KMS keys. This applies to the following resources:
+  **S3 buckets** – If you provide learning resources (such as API documents, threat models, or source code) from an S3 bucket encrypted with a customer managed key, the service role needs permissions to decrypt objects in that bucket. For more information about configuring SSE-KMS for S3, see [Protecting data with SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html).
+  **Secrets Manager secrets** – If your penetration test credentials are stored in Secrets Manager secrets encrypted with a customer managed key, the service role needs permissions to decrypt those secrets. For more information about secret encryption, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html).
+  **CloudWatch Logs log groups** – If the CloudWatch Logs log group used for storing penetration test execution logs is encrypted with a customer managed key (including log groups created by AWS Security Agent on your behalf), the service role needs `kms:DescribeKey` permission to validate the key. The CloudWatch Logs service principal handles the actual encryption and decryption of log data, and those permissions are granted through the key policy (see [Key policy](#cmk-key-policy)). For more information about encrypting log data, see [Encrypt log data in CloudWatch Logs using AWS KMS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html).

**Important**  
If you use a different KMS key for encrypting these resources than the one you specified for your Agent Space, you must grant the service role permissions for each KMS key that protects a resource the service role accesses during penetration testing.

Attach the following IAM policy to the penetration test service role. Include only the statements that apply to your configuration.

Replace the following placeholder values in the policy:
+  ` 111122223333 ` – Your AWS account ID
+  ` us-east-1 ` – The AWS Region where you use AWS Security Agent
+ The KMS key ARNs in `Resource` – The ARNs of the customer managed keys used to encrypt each resource

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowKmsAccessForEncryptedS3Buckets",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE-S3-KEY-ID"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "s3.*.amazonaws.com",
          "kms:EncryptionContext:aws:s3:arn": "arn:aws:s3:::YOUR-BUCKET-NAME*"
        }
      }
    },
    {
      "Sid": "AllowKmsAccessForEncryptedSecrets",
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt"
      ],
      "Resource": [
        "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE-SECRETS-KEY-ID"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "secretsmanager.*.amazonaws.com",
          "kms:EncryptionContext:SecretARN": "arn:aws:secretsmanager:us-east-1:111122223333:secret:YOUR-SECRET-NAME*"
        }
      }
    },
    {
      "Sid": "AllowKmsKeyValidationForCloudWatchLogsLogGroups",
      "Effect": "Allow",
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": [
        "arn:aws:kms:us-east-1:111122223333:key/EXAMPLE-CLOUDWATCH-LOGS-KEY-ID"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:ViaService": "logs.*.amazonaws.com"
        }
      }
    }
  ]
}
```

**Note**  
The `AllowKmsAccessForEncryptedS3Buckets` statement is required only if you provide learning resources from S3 buckets encrypted with a customer managed key. Update the `Resource` ARN to match the KMS key used to encrypt your S3 bucket, and update the `kms:EncryptionContext:aws:s3:arn` value to match your bucket name.
The `AllowKmsAccessForEncryptedSecrets` statement is required only if your penetration test credentials are stored in Secrets Manager secrets encrypted with a customer managed key. Update the `Resource` ARN to match the KMS key used to encrypt your secrets, and update the `kms:EncryptionContext:SecretARN` value to match your secret name.
The `AllowKmsKeyValidationForCloudWatchLogsLogGroups` statement is required only if your CloudWatch Logs log group is encrypted with a customer managed key, including log groups created by AWS Security Agent on your behalf. Update the `Resource` ARN to match the KMS key used to encrypt your log group.
If multiple resources share the same KMS key, you can combine the statements and list the shared key ARN once in the `Resource` field.

## Create a resource with a customer managed key
<a name="_create_a_resource_with_a_customer_managed_key"></a>

You can specify a customer managed key when setting up AWS Security Agent or when creating individual resources. The KMS key encrypts all data belonging to that resource and its subresources.

### Set a default KMS key during setup (console)
<a name="_set_a_default_kms_key_during_setup_console"></a>

You can configure a default KMS key during the initial AWS Security Agent setup. This key is used as the default for new Agent Spaces and integrations unless you specify a different key.

1. On the **Set up AWS Security Agent** page, expand the **Encryption - optional** section.

1. Select **Customize encryption settings (advanced)**.

1. For **Choose an AWS KMS key**, select a KMS key from your account, or enter a KMS key ARN.

1. Complete the remaining setup steps and choose **Set up AWS Security Agent**.

 AWS Security Agent validates the KMS key to confirm that it exists, is enabled, and uses symmetric encryption. If validation fails, setup does not proceed and you receive an error message.

### Create an Agent Space with a customer managed key (console)
<a name="_create_an_agent_space_with_a_customer_managed_key_console"></a>

1. In the AWS Security Agent console, navigate to the **Agent Spaces** page.

1. Choose **Create Agent Space**.

1. Enter a name and optional description for your Agent Space.

1. Expand the **Advanced** section.

1. Under **Data encryption**, choose one of the following:
   +  **Use application default key** – Uses the default KMS key configured during AWS Security Agent setup. This option is selected by default if a default key is configured.
   +  **Use a different key** – Specify a different KMS key for this Agent Space. Select **Customize encryption settings (advanced)**, then for **Choose an AWS KMS key**, select a KMS key from your account or enter an ARN.

1. Choose **Create**.

### Create an integration with a customer managed key (console)
<a name="_create_an_integration_with_a_customer_managed_key_console"></a>

1. In the AWS Security Agent console, navigate to the **Integrations** page.

1. Choose **Add integration** and select your provider (for example, GitHub).

1. Complete **Step 1: Install and authorize** the provider application.

1. In **Step 2: Register details**, enter a registration name and configure the provider settings.

1. In the **Data encryption** section, select **Customize encryption settings (advanced)**.

1. For **Choose an AWS KMS key**, select a KMS key from your account, or enter a KMS key ARN.

1. Choose **Connect**.

### Create a resource with a customer managed key (AWS CLI or SDK)
<a name="create_a_resource_with_a_customer_managed_key_shared_aws_cli_or_sdk"></a>

To specify a customer managed key using the AWS CLI or SDK:
+ Include the `defaultKmsKeyId` parameter when calling `CreateApplication` to set a default KMS key for your application. This key is used as the fallback when creating Agent Spaces or integrations without an explicit KMS key.
+ Include the `kmsKeyId` parameter when calling `CreateAgentSpace` or `CreateIntegration` to encrypt a specific resource. This takes precedence over the application-level default.

For parameter details, see the [AWS Security Agent API Reference](https://docs.aws.amazon.com/securityagent/latest/APIReference/Welcome.html).

If you don’t specify a KMS key, AWS Security Agent uses the application-level default KMS key if one is configured. Otherwise, the resource is encrypted with AWS-managed keys.

## Key rotation
<a name="_key_rotation"></a>

 AWS Security Agent automatically rotates branch keys on a periodic basis. Branch key rotation creates a new active version of the branch key while retaining all previous versions. After rotation:
+ New data is encrypted with the new branch key version.
+ Previously encrypted data remains decryptable using the older branch key version.
+ No data re-encryption is required.

Branch key rotation is separate from KMS key rotation. You can enable automatic KMS key rotation for your customer managed key independently. For more information, see [Rotating KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the * AWS Key Management Service Developer Guide*.

After a branch key rotation, there is a brief period during which cached copies of the previous branch key may still be used for new encryption operations. This window is determined by the internal cache time-to-live (TTL) and does not affect the security of your data.

## Considerations
<a name="_considerations"></a>

Keep the following in mind when using customer managed keys with AWS Security Agent:
+  **Customer managed keys apply to new resources only.** Existing resources created before you configure a customer managed key continue to use AWS-managed encryption. There is no migration of existing data.
+  **Customer managed keys are specified at creation time.** You specify the KMS key when creating a resource. You cannot add or change the KMS key for an existing resource.
+  **Multiple KMS keys are supported.** You can use different KMS keys for different resources. For example, you can use one key for production Agent Spaces and a different key for development Agent Spaces.
+  **Disabling or deleting a KMS key makes data inaccessible.** If you disable or schedule deletion of a KMS key, AWS Security Agent cannot decrypt data encrypted under that key. Affected resources become inaccessible until the key is re-enabled. Deleting a KMS key permanently prevents access to all data encrypted under that key.
+  **Key policy permissions are required.** If you remove the required permissions from your KMS key policy, AWS Security Agent cannot access encrypted data. Ensure that the key policy grants permissions for the administrator role (used to manage the service in the AWS Console), the application role (used by the web application), the penetration test service role (assumed by agents to run penetration tests), and the AWS Security Agent service principal as described in [Required KMS permissions](#cmk-required-permissions).
+  ** AWS KMS quotas apply.** Cryptographic operations against your KMS key count toward your AWS KMS request quotas. Under normal usage, the hierarchical keyring architecture minimizes KMS calls through branch key caching. For more information, see [Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) in the * AWS Key Management Service Developer Guide*.