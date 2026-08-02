# Encryption at rest

AWS IoT SiteWise encrypts all Scenario Discovery session data at rest. By default, AWS IoT SiteWise uses an
AWS owned key to encrypt your data at no additional charge and with no administrative
overhead. You can also choose to encrypt session data with a customer managed key for full
control and auditability of the encryption key that protects your resources.

## Encryption options

When you create a workspace, you choose one of the following encryption types:

- **SITEWISE\_DEFAULT\_ENCRYPTION** – AWS IoT SiteWise
  encrypts your session data using an AWS owned key at no additional charge. No
  configuration is required.
- **KMS\_BASED\_ENCRYPTION** – AWS IoT SiteWise encrypts your
  session data using a customer managed key that you specify. You maintain full control
  over the key.

###### Important

The encryption configuration is set at workspace creation and cannot be changed after
the workspace is created.

## How AWS IoT SiteWise uses a customer managed key

When you configure a workspace with a customer managed key, AWS IoT SiteWise uses that key to
encrypt the following data:

- **Video** – All video streams captured and stored
  for the workspace.
- **Annotations** – All annotation data associated
  with sessions in the workspace.
- **Telemetry** – All telemetry data collected and
  stored for the workspace.

AWS IoT SiteWise uses envelope encryption to protect your session data. During data ingestion,
AWS IoT SiteWise calls `kms:GenerateDataKey` scoped through source-context conditions
(`aws:SourceAccount` and `aws:SourceArn`) to generate data encryption
keys.

AWS IoT SiteWise uses a KMS grant through FAS (Forward Access Session) to perform KMS operations
on your behalf. The grant is scoped to the workspace and enables AWS IoT SiteWise to call
`GenerateDataKey`, `Decrypt`, and `ReEncrypt` operations.
AWS IoT SiteWise retires the grant when the associated workspace is deleted.

In addition, AWS IoT SiteWise configures underlying AWS managed data stores (such as Amazon S3 and
Amazon OpenSearch Serverless) to use your customer managed key. This means that session data
stored in these services is encrypted with your key, providing end-to-end encryption under
your control. You might see CloudTrail events from these AWS services using your KMS
key – this is expected behavior.

## Configuring encryption

When you create a workspace, specify the encryption configuration using the
`encryptionConfiguration` parameter with the following fields:

- **encryptionType** (required) – The type of
  encryption to use. Valid values are `SITEWISE_DEFAULT_ENCRYPTION` and
  `KMS_BASED_ENCRYPTION`.
- **kmsKeyId** (required when encryptionType is
  `KMS_BASED_ENCRYPTION`) – The ID, ARN, alias name, or alias ARN of
  the customer managed key. The key must be a symmetric key with ENCRYPT\_DECRYPT
  usage.

## Key policy

To allow AWS IoT SiteWise to use a customer managed key, the key policy must grant the necessary
permissions. The following is a least-privilege key policy with six statements:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSiteWiseIngestionGenerateDataKey",
      "Effect": "Allow",
      "Principal": {
        "Service": "iotsitewise.amazonaws.com"
      },
      "Action": "kms:GenerateDataKey*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:iotsitewise:us-east-1:111122223333:workspace/*"
        }
      }
    },
    {
      "Sid": "AllowSiteWiseDecryptDescribeReEncrypt",
      "Effect": "Allow",
      "Principal": {
        "Service": "iotsitewise.amazonaws.com"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:ReEncrypt*"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowSiteWiseToEncryptDataViaGrant",
      "Effect": "Allow",
      "Principal": {
        "Service": "iotsitewise.amazonaws.com"
      },
      "Action": "kms:CreateGrant",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
          "kms:GrantOperations": [
            "Decrypt",
            "GenerateDataKey",
            "ReEncrypt"
          ]
        }
      }
    },
    {
      "Sid": "AllowCustomerRoleDescribeKeyViaSiteWise",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/YourRole"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "iotsitewise.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowCustomerRoleDecryptViaSiteWise",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/YourRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "iotsitewise.us-east-1.amazonaws.com"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:iotsitewise:subscriberId": "111122223333"
        }
      }
    },
    {
      "Sid": "AllowCustomerRoleCreateGrantViaSiteWise",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/YourRole"
      },
      "Action": "kms:CreateGrant",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "iotsitewise.us-east-1.amazonaws.com"
        },
        "StringLike": {
          "kms:EncryptionContext:aws:iotsitewise:subscriberId": "111122223333"
        },
        "ForAllValues:StringEquals": {
          "kms:GrantOperations": [
            "Decrypt",
            "GenerateDataKey",
            "ReEncrypt"
          ]
        }
      }
    }
  ]
}
```

### Explanation of each policy statement

The following describes the purpose of each statement in the key policy:

- **AllowSiteWiseIngestionGenerateDataKey** –
  Allows the AWS IoT SiteWise service to call `kms:GenerateDataKey*` to create data
  encryption keys during data ingestion. The `aws:SourceAccount` and
  `aws:SourceArn` conditions scope access to your account and workspace,
  preventing the confused deputy problem.
- **AllowSiteWiseDecryptDescribeReEncrypt** –
  Allows the AWS IoT SiteWise service to call `kms:Decrypt`,
  `kms:DescribeKey`, and `kms:ReEncrypt*`. These operations do
  not carry the workspace source ARN in the request context, so source conditions are
  not applied to this statement.
- **AllowSiteWiseToEncryptDataViaGrant** –
  Allows the AWS IoT SiteWise service to call `kms:CreateGrant` to create a grant
  scoped to `Decrypt`, `GenerateDataKey`, and
  `ReEncrypt` operations. The `kms:GrantOperations` condition
  restricts the grant to only these operations.
- **AllowCustomerRoleDescribeKeyViaSiteWise** –
  Allows your IAM role to call `kms:DescribeKey` through FAS. AWS IoT SiteWise
  invokes this during workspace creation to validate that the key exists, is in ENABLED
  state, has KeySpec of SYMMETRIC\_DEFAULT, and has KeyUsage of ENCRYPT\_DECRYPT.
- **AllowCustomerRoleDecryptViaSiteWise** –
  Allows your IAM role to call `kms:Decrypt` through FAS. AWS IoT SiteWise uses
  this to verify that the calling principal has Decrypt permissions on the key. The
  `kms:ViaService` condition ensures this permission is only usable through
  AWS IoT SiteWise, and the encryption context condition scopes access to your account.
- **AllowCustomerRoleCreateGrantViaSiteWise** –
  Allows your IAM role to call `kms:CreateGrant` through FAS during
  workspace creation. AWS IoT SiteWise uses this grant to invoke `GenerateDataKey`,
  `Decrypt`, and `ReEncrypt` operations for the lifetime of the
  workspace. The grant operations condition limits what the grant can authorize.

## Creating a workspace with a customer managed key

To create a workspace with a customer managed key, specify the
`--encryption-configuration` parameter in the `CreateWorkspace` API
request:

```
aws iotsitewise create-workspace \
    --workspace-name my-workspace \
    --encryption-configuration encryptionType=KMS_BASED_ENCRYPTION,kmsKeyId=arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
    --region us-east-1
```

## Scoping down access to the customer managed key

### Encryption context

AWS IoT SiteWise includes the following encryption context key-value pair in every AWS KMS
request:

```
"aws:iotsitewise:subscriberId": "<CustomerAccountId>"
```

You can use `kms:EncryptionContext` conditions in the key policy to
further restrict which resources can use the key for encryption and decryption. The
encryption context also appears in plaintext in AWS CloudTrail logs. Each grant that
AWS IoT SiteWise creates includes an encryption context constraint, so the grant cannot be used to
encrypt or decrypt data for another workspace or AWS account.

### Confused deputy protection

The `aws:SourceArn` and `aws:SourceAccount` conditions prevent
the confused deputy problem by ensuring only your workspace can trigger key usage. These
conditions apply to `GenerateDataKey` only. The `Decrypt`,
`DescribeKey`, and `ReEncrypt` operations do not carry the
workspace source ARN in the request context, so source conditions cannot be applied to
those operations.

### kms:ViaService condition

The `kms:ViaService` condition key restricts key usage to Forward Access
Session requests that come from AWS IoT SiteWise:

```
"kms:ViaService": "iotsitewise.us-east-1.amazonaws.com"
```

This ensures that the customer role permissions in the key policy are only usable
when the request originates from AWS IoT SiteWise, preventing direct use of the key outside the
service context.

## Monitoring KMS usage with CloudTrail

AWS CloudTrail logs all KMS API calls made by AWS IoT SiteWise and underlying AWS services on
your customer managed key. Use the CloudTrail console or the `LookupEvents`
operation to search for log entries. The following are examples of CloudTrail events you can
expect to see.

### CreateGrant (Amazon OpenSearch Serverless)

Amazon OpenSearch Serverless creates a grant to use your customer managed key for
encrypting indexed session data:

```
{
  "eventSource": "kms.amazonaws.com",
  "eventName": "CreateGrant",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "aoss.amazonaws.com"
  },
  "requestParameters": {
    "granteePrincipal": "aoss.us-east-1.amazonaws.com",
    "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "constraints": {
      "encryptionContextSubset": {
        "aws:aoss:arn": "arn:aws:aoss:us-east-1:111122223333:collection/*"
      }
    },
    "retiringPrincipal": "aoss.us-east-1.amazonaws.com",
    "operations": ["Decrypt", "GenerateDataKey"]
  }
}
```

### GenerateDataKey (Amazon S3)

Amazon S3 uses your customer managed key to encrypt stored video data:

```
{
  "eventSource": "kms.amazonaws.com",
  "eventName": "GenerateDataKey",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "fas.s3.amazonaws.com"
  },
  "requestParameters": {
    "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "keySpec": "AES_256",
    "encryptionContext": {
      "aws:s3:arn": "arn:aws:s3:::iotsitewise-workspace-111122223333-us-east-1"
    }
  }
}
```

### GenerateDataKey (AWS IoT SiteWise)

AWS IoT SiteWise generates data keys for internal encryption operations:

```
{
  "eventSource": "kms.amazonaws.com",
  "eventName": "GenerateDataKey",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "AWS Internal"
  },
  "requestParameters": {
    "keyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "keySpec": "AES_256",
    "encryptionContext": {
      "aws:iotsitewise:subscriberId": "111122223333"
    }
  }
}
```
