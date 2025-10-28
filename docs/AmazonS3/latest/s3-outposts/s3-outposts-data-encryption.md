# Data encryption in S3 on Outposts

By default, all data stored in Amazon S3 on Outposts is encrypted by using server-side encryption
with Amazon S3 managed encryption keys (SSE-S3). For more information, see [Using server-side encryption with Amazon S3 managed keys (SSE-S3)](../userguide/UsingServerSideEncryption.md "../userguide/UsingServerSideEncryption.md") in the _Amazon S3 User Guide_.

You can optionally use server-side encryption with customer-provided encryption keys
(SSE-C). To use SSE-C, specify an encryption key as part of your object API requests.
Server-side encryption encrypts only the object data, not the object metadata. For more
information, see [Using server-side encryption with customer-provided keys](../userguide/ServerSideEncryptionCustomerKeys.md "../userguide/ServerSideEncryptionCustomerKeys.md") in the _Amazon S3 User Guide_.

###### Note

S3 on Outposts doesn't support server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS).
