This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Custom KMS key setup for data retention service

To use your own KMS keys with the data retention service, create keys with the following
configurations before launching the product:

Retention Key

- Key type: Symmetric (`SYMMETRIC_DEFAULT`)
- Key usage: Encrypt and decrypt
- Key rotation: Recommended to enable

Password Recovery Key

- Key type: Asymmetric (`ECC_NIST_P384`)
- Key usage: Key agreement
- Key rotation: Not supported for asymmetric keys

## Custom KMS key policy setup

1. Create your KMS keys with the required configurations above.
2. Copy each key's **Key ID** from the KMS
   console.
3. Launch the data retention product in Service Catalog, entering the Key IDs
   into the `KmsKeyId` and `PasswordRecoveryKeyId`
   fields.
4. After the stack completes, navigate to the **Outputs** tab.
5. Copy the values for `DRSCustomerCrossAccountRoleArn` and
   `DecryptionLambdaRoleArn`.
6. Open the KMS console and select your custom retention key.
7. In the **Key policy** section, choose **Switch to policy view**.
8. Choose **Edit**.
9. Add the following statements into your key policy's `"Statement"`
   array, replacing the placeholder ARNs with the values from step 5.
10. Choose **Save changes**.
11. Repeat steps 6–10 for the password recovery key using the password recovery
    statements below.

### Retention key — Statements to add

```
{
  "Sid": "EnclaveGenerateDataKey",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DRSCustomerCrossAccountRoleArn}"
  },
  "Action": "kms:GenerateDataKey",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:RecipientAttestation:PCR0": "*",
      "kms:RecipientAttestation:PCR1": "*",
      "kms:RecipientAttestation:PCR2": "*"
    },
    "ForAnyValue:StringEquals": {
      "kms:EncryptionContextKeys": [
        "aws:wickr:network:id",
        "aws:wickr:app:id"
      ]
    }
  }
},
{
  "Sid": "EnclaveDescribeKey",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DRSCustomerCrossAccountRoleArn}"
  },
  "Action": "kms:DescribeKey",
  "Resource": "*"
},
{
  "Sid": "EnclaveDecryptWithAttestation",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DRSCustomerCrossAccountRoleArn}"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:RecipientAttestation:PCR0": "*",
      "kms:RecipientAttestation:PCR1": "*",
      "kms:RecipientAttestation:PCR2": "*"
    },
    "ForAnyValue:StringEquals": {
      "kms:EncryptionContextKeys": "aws:wickr:app:id"
    }
  }
},
{
  "Sid": "DecryptLambdaDecrypt",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DecryptionLambdaRoleArn}"
  },
  "Action": "kms:Decrypt",
  "Resource": "*",
  "Condition": {
    "ForAnyValue:StringEquals": {
      "kms:EncryptionContextKeys": "aws:wickr:network:id"
    }
  }
}
```

Purpose of each statement can be found at [Encryption at rest](encryption-rest.md "encryption-rest.md") under the section **Configuring permissions to use a customer managed KMS
key**.

### Password recovery key — Statements to add

```
{
  "Sid": "EnclaveDeriveSharedSecret",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DRSCustomerCrossAccountRoleArn}"
  },
  "Action": "kms:DeriveSharedSecret",
  "Resource": "*",
  "Condition": {
    "StringLike": {
      "kms:RecipientAttestation:PCR0": "*",
      "kms:RecipientAttestation:PCR1": "*",
      "kms:RecipientAttestation:PCR2": "*"
    }
  }
},
{
  "Sid": "CustomerGetPublicKey",
  "Effect": "Allow",
  "Principal": {
    "AWS": "{DRSCustomerCrossAccountRoleArn}"
  },
  "Action": [
    "kms:DescribeKey",
    "kms:GetPublicKey"
  ],
  "Resource": "*"
}

```

Purpose of each statement:

**EnclaveDeriveSharedSecret**

- kms:DeriveSharedSecret — Invoked by the Nitro Enclave to perform ECDH key
  agreement using the password recovery key's private key. This derives a shared
  secret that is used to decrypt your password during the migration
  workflow. Only permitted when the enclave provides a valid Nitro Enclave attestation document
  (PCR0/1/2 conditions), ensuring the key agreement cannot occur outside the
  enclave.

**CustomerGetPublicKey**

- kms:GetPublicKey — Allows retrieval of the password recovery key's ECC
  P-384 public key. This is used by thepassword collection script running on the
  customer's machine to perform local ECDH encryption of the password.
- kms:DescribeKey — Allows retrieval of key metadata (key spec, usage, status) for validation.

### Example — Retention key

Before:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "YourExistingStatements",
      "Effect": "...",
      "...": "..."
    }
  ]
}
```

After:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "YourExistingStatements",
      "Effect": "...",
      "...": "..."
     },
    {
      "Sid": "EnclaveGenerateDataKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{account-id}:role/DRSCustomerCrossAccountRole-{network-id}-{region}"
      },
      "Action": "kms:GenerateDataKey",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:RecipientAttestation:PCR0": "*",
          "kms:RecipientAttestation:PCR1": "*",
          "kms:RecipientAttestation:PCR2": "*"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": [
            "aws:wickr:network:id",
            "aws:wickr:app:id"
          ]
        }
      }
    },
    {
      "Sid": "EnclaveDescribeKey",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{account-id}:role/DRSCustomerCrossAccountRole-{network-id}-{region}"
      },
      "Action": "kms:DescribeKey",
      "Resource": "*"
    },
    {
      "Sid": "EnclaveDecryptWithAttestation",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{account-id}:role/DRSCustomerCrossAccountRole-{network-id}-{region}"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:RecipientAttestation:PCR0": "*",
          "kms:RecipientAttestation:PCR1": "*",
          "kms:RecipientAttestation:PCR2": "*"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:wickr:app:id"
        }
      }
    },
    {
      "Sid": "DecryptLambdaDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{account-id}:role/{DecryptionLambdaRoleName}"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:wickr:network:id"
        }
      }
    }
  ]
}
```
