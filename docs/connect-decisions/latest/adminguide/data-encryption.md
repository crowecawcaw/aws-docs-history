

# Data Encryption
<a name="data-encryption"></a>

This topic provides information specific to Amazon Connect Decisions about encryption in transit and encryption at rest.

## Encryption in Transit
<a name="data-encryption-in-transit"></a>

All communication between customers and Amazon Connect Decisions and between Amazon Connect Decisions and its downstream dependencies is protected using TLS 1.2 or higher connections.

## Encryption at Rest
<a name="data-encryption-at-rest"></a>

All data at rest is encrypted using server-side encryption. No additional configuration is required as encryption is handled transparently by the service.

By default, Amazon Connect Decisions encrypts your data using AWS owned encryption keys from AWS Key Management Service (AWS KMS). You don't have to take any action to protect the AWS owned keys that encrypt your data. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the *AWS Key Management Service Developer Guide*.

You can optionally configure a customer managed KMS key for full control over the key lifecycle, including creation, rotation, disabling, and access policy management.

### Encrypting data at rest using customer managed KMS keys
<a name="data-encryption-customer-managed-kms-keys"></a>

#### How Amazon Connect Decisions uses a customer managed KMS key
<a name="data-encryption-how-uses-cmk"></a>

When you configure a customer managed KMS key, Amazon Connect Decisions uses it to encrypt all data in your instance at rest. This includes data stored across the service's underlying infrastructure.

The service accesses your key through three mechanisms:
+ **Service principal** — The `scn.amazonaws.com` service principal calls KMS directly for Encrypt, Decrypt, and GenerateDataKey operations, passing encryption context and confused deputy headers.
+ **Grants** — The service creates grants on your key when you create an instance. These grants enable dependent AWS services to encrypt and decrypt data using your key. Grants are retired when the instance is deleted.
+ **Instance role via FAS** — A service-linked role accesses your key through the `scn.<region>.amazonaws.com` ViaService condition when you interact with the console.

**Encryption context:** All direct KMS operations include the following encryption context:

```
{"aws:scn:arn": "arn:aws:scn:<region>:<account-id>:instance/<instance-id>"}
```

**Data key caching:** Amazon Connect Decisions caches data keys for up to 15 minutes. This means that after you disable or revoke access to your KMS key, the service may continue to use a cached data key for up to 15 minutes before operations begin to fail.

#### Configuring a customer managed KMS key
<a name="data-encryption-configuring-cmk"></a>

Amazon Connect Decisions supports symmetric encryption KMS keys only. Multi-region keys are supported.

##### Configuring permissions to use a customer managed KMS key
<a name="data-encryption-configuring-permissions"></a>

To use a customer managed KMS key, configure your key policy following these three steps:

1. **Create a KMS key** with the base policy below.

1. **Create an Amazon Connect Decisions instance** and select that key.

1. **(Optional, recommended)** Update the key policy with instance-level restrictions.

##### Step 1 — Create a key with the base policy
<a name="data-encryption-step1-base-policy"></a>

Open the [AWS KMS console](https://console.aws.amazon.com/kms), choose **Create key**, and replace the default policy with the following. Replace `<customer-account-id>` with your AWS account ID and `<region>` with your AWS Region.

```
{
          "Version": "2012-10-17",		 	 	 
          "Statement": [
            {
              "Sid": "AllowAccountRootFullAccess",
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::<customer-account-id>:root"
              },
              "Action": "kms:*",
              "Resource": "*"
            },
            {
              "Sid": "AllowScnRetrievalOfKeyMetadata",
              "Effect": "Allow",
              "Principal": {
                "Service": "scn.amazonaws.com"
              },
              "Action": "kms:DescribeKey",
              "Resource": "*",
              "Condition": {
                "StringEquals": {
                  "aws:SourceAccount": "<customer-account-id>"
                }
              }
            },
            {
              "Sid": "AllowScnEncryptDecryptWithContext",
              "Effect": "Allow",
              "Principal": {
                "Service": "scn.amazonaws.com"
              },
              "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey",
                "kms:GenerateDataKeyWithoutPlaintext"
              ],
              "Resource": "*",
              "Condition": {
                "StringEquals": {
                  "aws:SourceAccount": "<customer-account-id>"
                }
              }
            },
            {
              "Sid": "AllowScnCryptoViaDependencyServices",
              "Effect": "Allow",
              "Principal": {
                "Service": "scn.amazonaws.com"
              },
              "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
              ],
              "Resource": "*",
              "Condition": {
                "StringEquals": {
                  "kms:ViaService": [
                    "redshift-serverless.<region>.amazonaws.com",
                    "aoss.<region>.amazonaws.com",
                    "dynamodb.<region>.amazonaws.com",
                    "s3.<region>.amazonaws.com"
                  ]
                }
              }
            },
            {
              "Sid": "AllowScnCreateGrantForDependencyServices",
              "Effect": "Allow",
              "Principal": {
                "Service": "scn.amazonaws.com"
              },
              "Action": "kms:CreateGrant",
              "Resource": "*",
              "Condition": {
                "ForAllValues:StringEquals": {
                  "kms:GrantOperations": [
                    "Encrypt",
                    "Decrypt",
                    "GenerateDataKey",
                    "GenerateDataKeyWithoutPlaintext",
                    "DescribeKey",
                    "RetireGrant",
                    "ReEncryptFrom",
                    "ReEncryptTo",
                    "CreateGrant"
                  ]
                },
                "Bool": {
                  "kms:GrantIsForAWSResource": "true"
                }
              }
            },
            {
              "Sid": "AllowInstanceRoleDescribeKey",
              "Effect": "Allow",
              "Principal": {
                "AWS": "*"
              },
              "Action": "kms:DescribeKey",
              "Resource": "*",
              "Condition": {
                "ArnLike": {
                  "aws:PrincipalArn": "arn:aws:iam::<customer-account-id>:role/service-role/scn-instance-role-*"
                },
                "StringEquals": {
                  "kms:ViaService": "scn.<region>.amazonaws.com"
                }
              }
            },
            {
              "Sid": "AllowInstanceRoleEncryptDecrypt",
              "Effect": "Allow",
              "Principal": {
                "AWS": "*"
              },
              "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey*"
              ],
              "Resource": "*",
              "Condition": {
                "ArnLike": {
                  "aws:PrincipalArn": "arn:aws:iam::<customer-account-id>:role/service-role/scn-instance-role-*"
                },
                "StringEquals": {
                  "kms:ViaService": "scn.<region>.amazonaws.com"
                }
              }
            },
            {
              "Sid": "AllowInstanceRoleCreateGrant",
              "Effect": "Allow",
              "Principal": {
                "AWS": "*"
              },
              "Action": "kms:CreateGrant",
              "Resource": "*",
              "Condition": {
                "ArnLike": {
                  "aws:PrincipalArn": "arn:aws:iam::<customer-account-id>:role/service-role/scn-instance-role-*"
                },
                "StringEquals": {
                  "kms:ViaService": "scn.<region>.amazonaws.com"
                },
                "ForAllValues:StringEquals": {
                  "kms:GrantOperations": [
                    "Encrypt",
                    "Decrypt",
                    "GenerateDataKey",
                    "GenerateDataKeyWithoutPlaintext",
                    "DescribeKey",
                    "CreateGrant"
                  ]
                },
                "Bool": {
                  "kms:GrantIsForAWSResource": "true"
                }
              }
            }
          ]
        }
```

**Policy statement explanations:**
+ **AllowAccountRootFullAccess** — Ensures the key owner retains full control. Required to prevent key lockout.
+ **AllowScnRetrievalOfKeyMetadata** — Allows the service to validate key configuration during instance creation. Scoped to your account via `aws:SourceAccount`.
+ **AllowScnEncryptDecryptWithContext** — Allows direct cryptographic operations on your data. After Step 3, this is further scoped to your specific instance via encryption context.
+ **AllowScnCryptoViaDependencyServices** — Allows cryptographic operations through dependency services that don't support encryption context. Scoped via `kms:ViaService` to specific service endpoints.
+ **AllowScnCreateGrantForDependencyServices** — Allows grant creation for dependency services. Limited to listed operations and restricted to AWS resources only.
+ **AllowInstanceRoleDescribeKey** — Allows the instance's service-linked role to describe the key through FAS.
+ **AllowInstanceRoleEncryptDecrypt** — Allows the instance role to decrypt and generate data keys via FAS.
+ **AllowInstanceRoleCreateGrant** — Allows the instance role to create grants for downstream integrations.

##### Step 2 — Create your Amazon Connect Decisions instance
<a name="data-encryption-step2-create-instance"></a>

During instance creation, select **Customer managed key** under the encryption settings and choose the key you created in Step 1.

**Important**  
You cannot change this selection after instance creation. If you need to use a different key in the future, you must create a new instance.

##### Step 3 (optional) — Add instance-level restrictions
<a name="data-encryption-step3-instance-restrictions"></a>

After creating your instance, update the key policy to restrict access to only that instance. This prevents other instances in the same account from using the key.

Replace `<customer-account-id>`, `<region>`, and `<instance-id>` (the UUID visible on the Amazon Connect Decisions console).

The changes from the base policy are:
+ Add `aws:SourceArn` conditions to service principal statements, restricting to your instance ARN.
+ Add `kms:EncryptionContext:aws:scn:arn` conditions to cryptographic operations, requiring the encryption context match your instance.

Updated policy (showing only the statements that change):

**AllowScnRetrievalOfKeyMetadata** — add `ArnLike` condition:

```
"Condition": {
          "StringEquals": {
            "aws:SourceAccount": "<customer-account-id>"
          },
          "ArnLike": {
            "aws:SourceArn": "arn:aws:scn:<region>:<customer-account-id>:instance/<instance-id>"
          }
        }
```

**AllowScnEncryptDecryptWithContext** — add `EncryptionContext` and `SourceArn` conditions:

```
"Condition": {
          "StringEquals": {
            "aws:SourceAccount": "<customer-account-id>",
            "kms:EncryptionContext:aws:scn:arn": "arn:aws:scn:<region>:<customer-account-id>:instance/<instance-id>"
          },
          "ArnLike": {
            "aws:SourceArn": "arn:aws:scn:<region>:<customer-account-id>:instance/<instance-id>"
          }
        }
```

**AllowInstanceRoleEncryptDecrypt** — add `EncryptionContext` condition:

```
"Condition": {
          "ArnLike": {
            "aws:PrincipalArn": "arn:aws:iam::<customer-account-id>:role/scn-instance-role-*"
          },
          "StringEquals": {
            "kms:EncryptionContext:aws:scn:arn": "arn:aws:scn:<region>:<customer-account-id>:instance/<instance-id>",
            "kms:ViaService": "scn.<region>.amazonaws.com"
          }
        }
```

##### Creating a new instance with a customer managed KMS key
<a name="data-encryption-creating-instance-with-cmk"></a>

You select the KMS key during instance creation in the Amazon Connect Decisions console. For more information about creating an instance, see [Creating an Amazon Connect Decisions instance](https://docs.aws.amazon.com/connect-decisions/latest/adminguide/creating-your-instance.html).

##### Changing encryption configuration on an existing instance
<a name="data-encryption-changing-encryption-config"></a>

Amazon Connect Decisions does not support changing the KMS key on an active instance. If you need to use a different key, you must create a new instance configured with the desired key. Data encrypted with the previous key is not retained on the new instance.

##### Scoping down access to the customer managed KMS key
<a name="data-encryption-scoping-down-access"></a>

You can restrict access to your key using the following mechanisms:
+ **Encryption context** — Use `kms:EncryptionContext:aws:scn:arn` in your key policy to restrict operations to a specific instance (see Step 3).
+ **Confused deputy protection** — The service passes `aws:SourceAccount` and `aws:SourceArn` on KMS calls. Use these conditions to ensure only your account and instance can access the key.
+ **kms:ViaService** — The instance role accesses the key only through `scn.<region>.amazonaws.com`, preventing direct use outside of the service.
+ **Grant constraints** — Grants are scoped with `kms:GrantIsForAWSResource` and limited to explicitly listed operations.

**Note**  
Dependency services (Redshift Serverless, OpenSearch Serverless, DynamoDB) do not support encryption context or confused deputy headers. Access for these services is scoped using `kms:ViaService` only.

### Monitoring Amazon Connect Decisions interaction with AWS KMS
<a name="data-encryption-monitoring-kms"></a>

You can use AWS CloudTrail to track KMS requests that Amazon Connect Decisions makes on your behalf. Look for log entries with the following values:


| Field | Expected value | 
| --- | --- | 
| eventName | `Decrypt`, `GenerateDataKey`, `CreateGrant` | 
| userIdentity.invokedBy | `scn.amazonaws.com` | 
| requestParameters.encryptionContext | `{"aws:scn:arn": "arn:aws:scn:<region>:<account-id>:instance/<instance-id>"}` | 

You can filter CloudTrail events using these values to audit when and how Amazon Connect Decisions accesses your KMS key.

For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html).