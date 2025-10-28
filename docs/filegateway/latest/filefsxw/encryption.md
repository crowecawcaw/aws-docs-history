Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Data encryption using AWS KMS

Amazon FSx File Gateway supports SMB encryption up to the latest SMB v3.1.1
specification, including AES 128 CCM and AES 128 GCM. Compatible clients will connect using
encryption automatically. Additionally, FSx File Gateway uses SMB encryption when it communicates
with FSx for Windows File Server in AWS. You must configure an AWS Direct Connect link to AWS, and set
appropriate policies to allow SMB traffic and management traffic to pass through to
AWS.

###### Encrypting a file system

For information see, [Data Encryption in Amazon FSx](../../../fsx/latest/WindowsGuide/encryption.md "../../../fsx/latest/WindowsGuide/encryption.md") in
the _Amazon FSx for Windows File Server User Guide_.

**When using AWS KMS to encrypt your data, keep the following in
mind:**

- Your data is encrypted at rest in the cloud. That is, the data is encrypted in
  Amazon FSx.
- IAM users must have the required permissions to call the AWS KMS API operations.
  For more information, see [Using IAM policies with
  AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") in the _AWS Key Management Service Developer Guide_.

###### Important

When you use an AWS KMS key for server-side encryption, you must choose a symmetric key.
Storage Gateway does not support asymmetric keys. For more information, see [Using
symmetric and asymmetric keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the
_AWS Key Management Service Developer Guide_.

For more information about AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
