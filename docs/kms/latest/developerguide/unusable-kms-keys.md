# How unusable KMS keys affect data keys

When a KMS key becomes unusable, the effect is almost immediate (subject to eventual
consistency). The [key state](key-state.md "key-state.md") of the KMS key changes to
reflect its new condition, and all requests to use the KMS key in [cryptographic operations](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations") fail.

However, the effect on data keys encrypted by the KMS key, and on data encrypted by
the data key, is delayed until the KMS key is used again, such as to decrypt the data
key.

KMS keys can become unusable for a variety of reasons, including the following
actions that you might perform.

- [Disabling the KMS key](enabling-keys.md "enabling-keys.md")
- [Scheduling the KMS key for
  deletion](deleting-keys.md "deleting-keys.md")
- [Deleting the key
  material](importing-keys-delete-key-material.md "importing-keys-delete-key-material.md") from a KMS key with imported key material, or allowing the
  imported key material to expire. If a KMS key with `EXTERNAL` origin
  has multiple key materials associated, the deletion or expiration of any key material
  will cause the key to become unusable.
- [Disconnecting the AWS CloudHSM key store](disconnect-keystore.md "disconnect-keystore.md")
  that hosts the KMS key, or [deleting the key
  from the AWS CloudHSM cluster](fix-keystore.md#fix-cmk-failed "fix-keystore.md#fix-cmk-failed") that serves as key material for the
  KMS key.
- [Disconnecting the external key
  store](about-xks-disconnecting.md "about-xks-disconnecting.md") that hosts the KMS key, or any other action that interferes
  with encryption and decryption requests to the external key store proxy,
  including deleting the external key from its external key manager.
  This effect is particularly important for the many AWS services that use data keys
  to protect the resources that the service manages. The following example uses Amazon Elastic Block Store
  (Amazon EBS) and Amazon Elastic Compute Cloud (Amazon EC2). Different AWS services use data keys in different ways.
  For details, see the Data protection section of the Security chapter for the
  AWS service.

For example, consider this scenario:

1. You [create an encrypted
   EBS volume](../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md "../../../AWSEC2/latest/UserGuide/ebs-creating-volume.md") and specify a KMS key to protect it. Amazon EBS asks AWS KMS
   to use your KMS key to [generate an
   encrypted data key](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md") for the volume. Amazon EBS stores the encrypted data
   key with the volume's metadata.
2. When you attach the EBS volume to an EC2 instance, Amazon EC2 uses your KMS key
   to decrypt the EBS volume's encrypted data key. Amazon EC2 uses the data key in the
   Nitro hardware, which is responsible for encrypting all disk I/O to the EBS
   volume. The data key persists in the Nitro hardware while the EBS volume is
   attached to the EC2 instance.
3. You perform an action that makes the KMS key unusable. This has no immediate
   effect on the EC2 instance or the EBS volume. Amazon EC2 uses the data key—not
   the KMS key—to encrypt all disk I/O while the volume is attached to the
   instance.
4. However, when the encrypted EBS volume is detached from the EC2 instance,
   Amazon EBS removes the data key from the Nitro hardware. The next time the encrypted
   EBS volume is attached to an EC2 instance, the attachment fails, because Amazon EBS
   cannot use the KMS key to decrypt the volume's encrypted data key. To use the
   EBS volume again, you must make the KMS key usable again.
