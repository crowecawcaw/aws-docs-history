# Data encryption using AWS KMS

Storage Gateway uses SSL/TLS (Secure Socket Layers/Transport Layer Security) to
encrypt data that is transferred between your gateway appliance and AWS storage. By
default, Storage Gateway uses Amazon S3-Managed encryption keys (SSE-S3) to server-side encrypt
all data it stores in Amazon S3. You have an option to use the Storage Gateway API to configure your
gateway to encrypt data stored in the cloud using server-side encryption with AWS Key Management Service
(SSE-KMS) keys.

###### Encrypting a file share

You can configure the file shares on your S3 File Gateway to encrypt stored objects with
AWS KMS–managed keys by using SSE-KMS or DSSE-KMS. For information about supported
file share encryption methods, see [Encrypt objects stored by File Gateway in Amazon S3](encrypt-objects-stored-by-file-gateway-in-amazon-s3.md "encrypt-objects-stored-by-file-gateway-in-amazon-s3.md").

**When using AWS KMS to encrypt your data, keep the following in
mind:**

- Your data is encrypted at rest in the cloud. That is, the data is encrypted in
  Amazon S3.
- IAM users must have the required permissions to call the AWS KMS API operations.
  For more information, see [Using IAM policies with
  AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") in the _AWS Key Management Service Developer Guide_.

###### Important

When you use an AWS KMS key for server-side encryption, you must choose a symmetric key.
Storage Gateway does not support asymmetric keys. For more information, see [Using
symmetric and asymmetric keys](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the
_AWS Key Management Service Developer Guide_.

For more information about AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")
