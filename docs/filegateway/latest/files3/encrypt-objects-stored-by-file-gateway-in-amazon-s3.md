# Encrypt objects stored

by File Gateway in Amazon S3

S3 File Gateway supports the following methods of server-side encryption for the data that it
stores in Amazon S3:

- **SSE-S3** — By default, all new objects
  uploaded to Amazon S3 buckets use server-side encryption with Amazon S3 managed keys. For
  more information, see [Using
  server-side encryption with Amazon S3 managed keys](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the
  _Amazon Simple Storage Service User Guide_.
- **SSE-KMS** — You can configure your file
  share to use server-side encryption with AWS Key Management Service (AWS KMS) managed keys. AWS KMS
  is a service that combines secure, highly available hardware and software to
  provide a key management system scaled for the cloud. For more information, see
  [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service
  Developer Guide_.
- **DSSE-KMS** — Dual-layer server-side
  encryption with AWS KMS keys applies two layers of encryption to objects when they
  are uploaded to Amazon S3. This helps fulfill compliance standards for multilayer
  encryption. For more information, see [Using dual-layer
  server-side encryption with AWS KMS keys](../../../AmazonS3/latest/userguide/UsingDSSEncryption.md "../../../AmazonS3/latest/userguide/UsingDSSEncryption.md") in the _Amazon Simple Storage Service
  User Guide_.

###### Note

There are additional charges for using DSSE-KMS and AWS KMS keys. For more
information, see [AWS KMS
pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").
You can specify an encryption method when you create a new file share by using the
Storage Gateway console or the Storage Gateway API. For console procedures, see [Create an NFS file share with a custom
configuration](CreatingAnNFSFileShare.md "CreatingAnNFSFileShare.md") or [Create an SMB file share with a custom
configuration](CreatingAnSMBFileShare.md "CreatingAnSMBFileShare.md"). For
information about the corresponding API commands, see [CreateNFSFileShare](../../../storagegateway/latest/APIReference/API_CreateNFSFileShare.md "../../../storagegateway/latest/APIReference/API_CreateNFSFileShare.md") or [CreateSMBFileShare](../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md "../../../storagegateway/latest/APIReference/API_CreateSMBFileShare.md") in the _AWS Storage Gateway API
Reference_.

You can also update encryption settings for an existing file share using the
Storage Gateway console, or the Storage Gateway API. For the console procedure, see [Change the server-side encryption method
for an existing file share](edit-file-share-encryption.md "edit-file-share-encryption.md").
For information about the corresponding API commands, see [UpdateNFSFileShare](../../../storagegateway/latest/APIReference/API_UpdateNFSFileShare.md "../../../storagegateway/latest/APIReference/API_UpdateNFSFileShare.md") or [UpdateSMBFileShare](../../../storagegateway/latest/APIReference/API_UpdateSMBFileShare.md "../../../storagegateway/latest/APIReference/API_UpdateSMBFileShare.md") in the _AWS Storage Gateway API
Reference_.

###### Note

After you update the encryption method, the gateway uses the new method for all
new objects it creates in Amazon S3 and for any stored objects that it updates or
modifies in the future. Existing Amazon S3 objects will only receive the new encryption
method if they are updated or modified by the gateway.

###### Important

Make sure that your file share uses the same encryption type as the Amazon S3 bucket
where it stores your data.

If you configure your File Gateway to use SSE-KMS or DSSE-KMS for encryption, you
must manually add `kms:Encrypt`, `kms:Decrypt`,
`kms:ReEncrypt*`, `kms:GenerateDataKey`, and
`kms:DescribeKey` permissions to the IAM role associated with the
file share. For more information, see [Using
Identity-Based Policies (IAM Policies) for Storage Gateway](using-identity-based-policies.md "using-identity-based-policies.md").
