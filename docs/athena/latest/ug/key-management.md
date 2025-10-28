# Key management

Amazon Athena supports AWS Key Management Service (AWS KMS) to encrypt datasets in Amazon S3 and Athena query
results. AWS KMS uses customer managed keys to encrypt your Amazon S3 objects and relies on [envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping").

In AWS KMS, you can perform the following actions:

- [Create keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md")
- [Import your own key material for
  new customer managed keys](../../../kms/latest/developerguide/importing-keys.md "../../../kms/latest/developerguide/importing-keys.md")

###### Note

Athena supports only symmetric keys for reading and writing data.

For more information, see [What is
AWS Key Management Service](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the _AWS Key Management Service Developer Guide_, and [How Amazon Simple Storage Service uses AWS KMS](../../../kms/latest/developerguide/services-s3.md "../../../kms/latest/developerguide/services-s3.md").
To view the keys in your account that AWS creates and manages for you, in the navigation pane, choose **AWS managed keys**.

If you are uploading or accessing objects encrypted by SSE-KMS, use AWS Signature
Version 4 for added security. For more information, see [Specifying the
signature version in request authentication](../../../AmazonS3/latest/userguide/UsingAWSSDK.md#specify-signature-version "../../../AmazonS3/latest/userguide/UsingAWSSDK.md#specify-signature-version") in the
_Amazon Simple Storage Service User Guide_.

If your Athena workloads encrypt a large amount of data, you can use Amazon S3 Bucket Keys
to reduce costs. For more information, see [Reducing the cost of SSE-KMS with
Amazon S3 Bucket keys](../../../AmazonS3/latest/userguide/bucket-key.md "../../../AmazonS3/latest/userguide/bucket-key.md") in the _Amazon Simple Storage Service User Guide_.
