# Data encryption using AWS KMS

Storage Gateway uses SSL/TLS (Secure Socket Layers/Transport Layer Security) to encrypt data that
is transferred between your gateway appliance and AWS storage. By default, Storage Gateway
uses Amazon S3-Managed Encryption Keys (SSE-S3) to server-side encrypt all data it stores in
Amazon S3. You have an option to use the Storage Gateway API to configure your gateway to encrypt
data stored in the cloud using server-side encryption with AWS Key Management Service (SSE-KMS) keys.

###### Important

When you use an AWS KMS key for server-side encryption, you must choose a symmetric key.
Storage Gateway does not support asymmetric keys. For more information, see [Using
symmetric and asymmetric keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the
_AWS Key Management Service Developer Guide_.

###### Encrypting a file share

For a file share, you can configure your gateway to encrypt your objects with
AWS KMS–managed keys by using SSE-KMS. For information on using the Storage Gateway
API to encrypt data written to a file share, see [CreateNFSFileShare](../APIReference/API_CreateNFSFileShare.md "../APIReference/API_CreateNFSFileShare.md") in the _AWS Storage Gateway API Reference_.

###### Encrypting a volume

For cached and stored volumes, you can configure your gateway to encrypt volume data
stored in the cloud with AWS KMS–managed keys by using the Storage Gateway API. You
can specify one of the managed keys as the KMS key. The key that you use to encrypt your
volume can't be changed after the volume is created. For information on using the
Storage Gateway API to encrypt data written to a cached or stored volume, see [CreateCachediSCSIVolume](../APIReference/API_CreateCachediSCSIVolume.md "../APIReference/API_CreateCachediSCSIVolume.md") or [CreateStorediSCSIVolume](../APIReference/API_CreateStorediSCSIVolume.md "../APIReference/API_CreateStorediSCSIVolume.md") in the
_AWS Storage Gateway API Reference_.

###### Encrypting a tape

For a virtual tape, you can configure your gateway to encrypt tape data stored in the
cloud with AWS KMS–managed keys by using the Storage Gateway API. You can specify one
of the managed keys as the KMS key. The key that you use to encrypt your tape data can't
be changed after the tape is created. For information on using the Storage Gateway API to
encrypt data written to a virtual tape, see [CreateTapes](../APIReference/API_CreateTapes.md "../APIReference/API_CreateTapes.md") in
the _AWS Storage Gateway API Reference_.

When using AWS KMS to encrypt your data*,* keep the
following in mind:

- Your data is encrypted at rest in the cloud. That is, the data is encrypted in
  Amazon S3.
- IAM users must have the required permissions to call the AWS KMS API operations.
  For more information, see [Using IAM policies with
  AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") in the _AWS Key Management Service Developer Guide_.
- If you delete or deactivate your AWS AWS KMS key or revoke the grant token, you
  can't access the data on the volume or tape. For more information, see [Deleting
  KMS keys](../../../kms/latest/developerguide/deleting-keys.md "../../../kms/latest/developerguide/deleting-keys.md") in the _AWS Key Management Service Developer Guide_.
- If you create a snapshot from a volume that is KMS-encrypted, the snapshot is
  encrypted. The snapshot inherits the volume's KMS key.
- If you create a new volume from a snapshot that is KMS-encrypted, the volume is
  encrypted. You can specify a different KMS key for the new volume.

###### Note

Storage Gateway doesn't support creating an unencrypted volume from a recovery
point of a KMS-encrypted volume or a KMS-encrypted snapshot.
For more information about AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
