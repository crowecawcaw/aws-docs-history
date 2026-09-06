

# Encryption outcomes for EBS direct APIs
<a name="ebsapis-using-encryption"></a>

When you start a new snapshot using [ StartSnapshot](https://docs.aws.amazon.com/ebs/latest/APIReference/API_StartSnapshot.html), the encryption status depends on the values that you specify for **Encrypted**, **KmsKeyArn**, and **ParentSnapshotId**, and whether your AWS account is enabled for [encryption by default](encryption-by-default.md).

**Note**  
You might need additional IAM permissions to use the EBS direct APIs with encryption. For moreinformation, see [Permissions to use AWS KMS keys](ebsapi-permissions.md#ebsapi-kms-permissions).
If Amazon EBS encryption by default is enabled on your AWS account, you can't create unencrypted snapshots.
If Amazon EBS encryption by default is enabled on your AWS account, you cannot start a new snapshot using an unencrypted parent snapshot. You must first encrypt the parent snapshot by copying it. For more information, see [Copy an Amazon EBS snapshot](ebs-copy-snapshot.md).

**Topics**
+ [Encryption outcomes: Unencrypted parent snapshot](#ebs-direct-api-unencr-outcomes-parent)
+ [Encryption outcomes: Encrypted parent snapshot](#ebs-direct-api-encr-outcomes-parent)
+ [Encryption outcomes: No parent snapshot](#ebs-direct-api-encr-outcomes-noparent)

## Encryption outcomes: Unencrypted parent snapshot
<a name="ebs-direct-api-unencr-outcomes-parent"></a>

The following table describes the encryption outcome for each possible combination of settings when specifying an unencrypted parent snapshot.



- **Unencrypted**
  - **Encrypted:** Omitted
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled / **Result:** The request fails with ValidationException.
  - **Encryption by default:** Disabled / **Result:** The snapshot is unencrypted.
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled

- **Unencrypted**
  - **Encrypted:** True
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **Result:** The request fails with ValidationException.

- **Unencrypted**
  - **Encrypted:** False
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **Result:** The request fails with ValidationException.



## Encryption outcomes: Encrypted parent snapshot
<a name="ebs-direct-api-encr-outcomes-parent"></a>

The following table describes the encryption outcome for each possible combination of settings when specifying an encrypted parent snapshot.



- **Encrypted**
  - **Encrypted:** Omitted
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled / **Result:** The snapshot is encrypted using the same KMS key as the parent snapshot.
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled / **Result:** The request fails with ValidationException.
  - **Encryption by default:** Disabled

- **Encrypted**
  - **Encrypted:** True
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **Result:** The request fails with ValidationException.

- **Encrypted**
  - **Encrypted:** False
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled
  - **Encryption by default:** Disabled
  - **Result:** The request fails with ValidationException.



## Encryption outcomes: No parent snapshot
<a name="ebs-direct-api-encr-outcomes-noparent"></a>

The following tables describe the encryption outcome for each possible combination of settings when not using a parent snapshot.



- **Omitted**
  - **Encrypted:** True
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled / **Result:** The snapshot is encrypted using the default KMS key for your account. \*
  - **Encryption by default:** Disabled
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled / **Result:** The snapshot is encrypted using the KMS key specified for KmsKeyArn.
  - **Encryption by default:** Disabled

- **Omitted**
  - **Encrypted:** False
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled / **Result:** The request fails with ValidationException.
  - **Encryption by default:** Disabled / **Result:** The snapshot is unencrypted.
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled / **Result:** The request fails with ValidationException.
  - **Encryption by default:** Disabled

- **Omitted**
  - **Encrypted:** Omitted
  - **KmsKeyArn:** Omitted / **Encryption by default:** Enabled / **Result:** The snapshot is encrypted using the default KMS key for your account. \*
  - **Encryption by default:** Disabled / **Result:** The snapshot is unencrypted.
  - **KmsKeyArn:** Specified / **Encryption by default:** Enabled / **Result:** The snapshot is encrypted using the KMS key specified for KmsKeyArn.
  - **Encryption by default:** Disabled



\* This default KMS key could be a customer managed key or the default AWS managed KMS key for Amazon EBS encryption.