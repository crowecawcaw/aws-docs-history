# Encryption outcomes for EBS direct APIs

When you start a new snapshot using [StartSnapshot](../APIReference/API_StartSnapshot.md "../APIReference/API_StartSnapshot.md"), the encryption status depends on the values that you specify for
**Encrypted**, **KmsKeyArn**,
and **ParentSnapshotId**, and whether your AWS account is
enabled for [encryption by default](encryption-by-default.md "encryption-by-default.md").

###### Note

- You might need additional IAM permissions to use the EBS direct APIs with encryption.
  For moreinformation, see [Permissions to use AWS KMS keys](ebsapi-permissions.md#ebsapi-kms-permissions "ebsapi-permissions.md#ebsapi-kms-permissions").
- If Amazon EBS encryption by default is enabled on your AWS account, you can't create
  unencrypted snapshots.
- If Amazon EBS encryption by default is enabled on your AWS account, you cannot start a new
  snapshot using an unencrypted parent snapshot. You must first encrypt the parent snapshot by
  copying it. For more information, see [Copy an Amazon EBS snapshot](ebs-copy-snapshot.md "ebs-copy-snapshot.md").

###### Topics

- [Encryption outcomes: Unencrypted parent snapshot](#ebs-direct-api-unencr-outcomes-parent "#ebs-direct-api-unencr-outcomes-parent")
- [Encryption outcomes: Encrypted parent snapshot](#ebs-direct-api-encr-outcomes-parent "#ebs-direct-api-encr-outcomes-parent")
- [Encryption outcomes: No parent snapshot](#ebs-direct-api-encr-outcomes-noparent "#ebs-direct-api-encr-outcomes-noparent")

## Encryption outcomes: Unencrypted parent snapshot

The following table describes the encryption outcome for each possible combination of settings
when specifying an unencrypted parent snapshot.

| ParentSnapshotId | Encrypted                    | KmsKeyArn | Encryption by default | Result                                        |
| ---------------- | ---------------------------- | --------- | --------------------- | --------------------------------------------- |
| Unencrypted      | Omitted                      | Omitted   | Enabled               | The request fails with `ValidationException`. |
| Disabled         | The snapshot is unencrypted. |
| Specified        | Enabled                      |
| Disabled         |
| Unencrypted      | True                         | Omitted   | Enabled               | The request fails with `ValidationException`. |
| Disabled         |
| Specified        | Enabled                      |
| Disabled         |
| Unencrypted      | False                        | Omitted   | Enabled               | The request fails with `ValidationException`. |
| Disabled         |
| Specified        | Enabled                      |
| Disabled         |

## Encryption outcomes: Encrypted parent snapshot

The following table describes the encryption outcome for each possible combination of settings
when specifying an encrypted parent snapshot.

| ParentSnapshotId | Encrypted | KmsKeyArn                                     | Encryption by default | Result                                                                      |
| ---------------- | --------- | --------------------------------------------- | --------------------- | --------------------------------------------------------------------------- |
| Encrypted        | Omitted   | Omitted                                       | Enabled               | The snapshot is encrypted using the same KMS key<br>as the parent snapshot. |
| Disabled         |
| Specified        | Enabled   | The request fails with `ValidationException`. |
| Disabled         |
| Encrypted        | True      | Omitted                                       | Enabled               | The request fails with `ValidationException`.                               |
| Disabled         |
| Specified        | Enabled   |
| Disabled         |
| Encrypted        | False     | Omitted                                       | Enabled               | The request fails with `ValidationException`.                               |
| Disabled         |
| Specified        | Enabled   |
| Disabled         |

## Encryption outcomes: No parent snapshot

The following tables describe the encryption outcome for each possible combination of settings
when not using a parent snapshot.

| ParentSnapshotId | Encrypted                    | KmsKeyArn                                                                   | Encryption by default | Result                                                                   |
| ---------------- | ---------------------------- | --------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------ |
| Omitted          | True                         | Omitted                                                                     | Enabled               | The snapshot is encrypted using the default KMS key for your account. \* |
| Disabled         |
| Specified        | Enabled                      | The snapshot is encrypted using the KMS key specified for<br>**KmsKeyArn**. |
| Disabled         |
| Omitted          | False                        | Omitted                                                                     | Enabled               | The request fails with `ValidationException`.                            |
| Disabled         | The snapshot is unencrypted. |
| Specified        | Enabled                      | The request fails with `ValidationException`.                               |
| Disabled         |
| Omitted          | Omitted                      | Omitted                                                                     | Enabled               | The snapshot is encrypted using the default KMS key for your account. \* |
| Disabled         | The snapshot is unencrypted. |
| Specified        | Enabled                      | The snapshot is encrypted using the KMS key specified for<br>**KmsKeyArn**. |
| Disabled         |

\* This default KMS key could be a customer managed key or the default AWS managed KMS key for
Amazon EBS encryption.
