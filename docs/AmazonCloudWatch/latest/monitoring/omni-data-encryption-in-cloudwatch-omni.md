

# Data encryption in CloudWatch Omni
<a name="omni-data-encryption-in-cloudwatch-omni"></a>

CloudWatch Omni encrypts your data at rest and in transit. This page describes what is encrypted, which keys are used, and what your AWS KMS key policy must allow.

To choose what content enters your telemetry, see [Protect sensitive data](omni-data-protection.md). To configure a customer managed key on your space, see [Set up Omni](omni-set-up-omni.md).

**Encryption at rest**


| Store | Default encryption | Customer managed key | 
| --- | --- | --- | 
| Telemetry in your space, held in the CloudWatch Dataset | Managed by CloudWatch Omni | Supported for enabled accounts. Configure the key on the space. | 
| Evaluation job and configuration metadata | AWS KMS key | Supported | 
| Staging storage in Amazon S3 | SSE-S3, with versioning and TLS-enforced access | — | 
| Forward access session credentials | A dedicated service-managed AWS KMS key. These credentials are envelope-encrypted, bound by encryption context to the job that uses them, and never written to logs. | Service-managed | 

**Important**  
Customer managed key support is enabled per account, so the option might not appear when you configure your space. Removing a customer managed key from a space requires `kms:Decrypt` on the outgoing key, so the caller can still read data already written under it.

**Files that CloudWatch Omni writes to your own machine are not encrypted by the service.** When you use the IDE extension and local development tools, telemetry can be written under a local `.omni/` directory, including raw prompts and responses. These files are plaintext and rely on your operating-system file permissions. Local mode keeps your telemetry off the network until you choose to send it, but it does not encrypt it at rest. Protecting these files is your responsibility, and the sample `.gitignore` that ships with the tooling re-includes several `.omni/` data files, so raw trace content can be committed to source control. Available in the IDE extension only.

**Key management**

If you use a customer managed AWS KMS key, your key policy must allow the following. Your policy needs **both** of the first two statements: when you attach the key with [AssociateDatasetKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AssociateDatasetKmsKey.html), CloudWatch checks your own access to the key before it checks the service's, so a policy that grants only the CloudWatch service principal is denied for the caller and the key is rejected.

1. **Dry-run checks signed by the CloudWatch service principal.** When you attach a customer managed key to a space, CloudWatch Omni performs dry-run `kms:Decrypt` and `kms:GenerateDataKey` calls against your key, using the encryption context `{"aws:cloudwatch:arn":"arn:aws:cloudwatch:<region>:<account-id>:space/<space-id>"}`. Both must succeed, or the key is rejected when you attach it. The service repeats the check on later requests. A key policy that is narrowed after you attach the key fails closed rather than silently. These calls are signed by the CloudWatch service principal, `cloudwatch.amazonaws.com`, and not by you. Grant that principal both actions on the encryption context above, and condition the statement on `aws:SourceArn` for the space ARN. Because the context is an ARN, you can grant on `arn:aws:cloudwatch:<region>:<account-id>:space/*` before you create a space, then narrow to a specific space afterward.

1. **`kms:DescribeKey` for the principal that configures the key.** Grant this in a statement of its own, with no encryption context condition. `DescribeKey` requests do not carry an encryption context, so this action cannot sit under the condition that scopes the crypto grants.

1. **Crypto operations on evaluation metadata.** When you configure a customer managed key for evaluation metadata, the service requires `kms:Decrypt`, `kms:DescribeKey`, and `kms:GenerateDataKey` on that key.

**Scope of the dataset key:** AssociateDatasetKmsKey and DisassociateDatasetKmsKey operate on the Dataset, which holds your space's telemetry. The key is associated at the Dataset level rather than per signal type, so associating a customer managed key covers everything the Dataset holds, and disassociating it reverts all of it.

**Sample key policy**

The following sample key policy covers every way CloudWatch Omni uses your key: the space and Dataset checks described above, the material the service encrypts on your behalf, forwarded telemetry entering the Dataset, and reads by the space operator role. Add the statements you need to your key policy. Replace `111122223333` with your account ID and `us-east-1` with your Region.

```
{
  "Version": "2012-10-17",
  "Id": "omni-cmk-key-policy",
  "Statement": [
    {
      "Sid": "EnableRootKeyAdministration",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
      },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowCloudWatchIntelligenceDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowCloudWatchIntelligenceEncryptionService",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:cloudwatch:account": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowOmniIntelligenceBranchKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws-crypto-ec:aws:cloudwatch:account": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowCloudWatchDatasetDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudwatch:us-east-1:111122223333:dataset/default"
        }
      }
    },
    {
      "Sid": "AllowCloudWatchDatasetEncryption",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333",
          "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:us-east-1:111122223333:dataset/default"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudwatch:us-east-1:111122223333:dataset/default"
        }
      }
    },
    {
      "Sid": "AllowCloudWatchSpaceDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudwatch:us-east-1:111122223333:space/*"
        }
      }
    },
    {
      "Sid": "AllowCloudWatchSpaceEncryptionService",
      "Effect": "Allow",
      "Principal": {
        "Service": "cloudwatch.amazonaws.com"
      },
      "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:us-east-1:111122223333:space/*"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:cloudwatch:us-east-1:111122223333:space/*"
        }
      }
    },
    {
      "Sid": "AllowCallerDatasetForwarding",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/CloudWatchOmniDatasetIntegrationExecutionRole"
      },
      "Action": [
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws:cloudwatch:arn": "arn:aws:cloudwatch:us-east-1:111122223333:dataset/default",
          "kms:ViaService": "cloudwatch.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowOperatorRoleDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/CloudWatchOmniOperatorRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "cloudwatch.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowOperatorRoleIntelligenceDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/CloudWatchOmniOperatorRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:EncryptionContext:aws-crypto-ec:aws:cloudwatch:account": "111122223333"
        }
      }
    }
  ]
}
```

What each group of statements is for:
+ **Root key administration** keeps your account able to manage the key. Do not remove it.
+ **The `cloudwatch.amazonaws.com` statements** let the service encrypt and read your space content, your Dataset, and the analysis material the service builds from your telemetry. The encryption-context and `aws:SourceArn` conditions restrict each statement so the key can be used only for CloudWatch Omni resources in your own account.
+ **`AllowCallerDatasetForwarding`** lets the Dataset integration execution role write forwarded logs and traces into a Dataset encrypted with this key. If you created your own execution role, use its name here. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).
+ **The operator-role statements** let the space operator role read data encrypted under the key, only through CloudWatch (`kms:ViaService`).

**Encryption in transit**

All communication with CloudWatch Omni service endpoints uses HTTPS with TLS. The public API endpoints require a minimum of TLS 1.2. We recommend TLS 1.3, and the service supports post-quantum hybrid key exchange. Amazon S3 access is TLS-enforced.

Telemetry ingestion is over HTTPS and is authenticated with Signature Version 4. Unsigned requests are rejected with an HTTP 403 response.

**Important**  
CloudWatch Omni does not offer FIPS 140-3 validated endpoints. If you require FIPS 140-3 validated cryptographic modules, review this limitation before you send telemetry.

**Operational data that CloudWatch Omni records about you**

Request logs and audit events are delivered to AWS CloudTrail as management events, and include the resource ARN, the calling principal, the account ID, and the organization ID. Service metadata such as timestamps and resource identifiers is encrypted with AWS managed keys.