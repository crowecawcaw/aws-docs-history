# Step 5: (Optional) Encrypt training files

You can choose one of the following options to encrypt the Amazon Rekognition Custom Labels manifest files and
image files that are in a console bucket or an external Amazon S3 bucket.

- Use an Amazon S3 key (SSE-S3).
- Use your AWS KMS key.

###### Note

The calling [IAM principal](../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal%23intro-structure-principal "../../../IAM/latest/UserGuide/intro-structure.md#intro-structure-principal%23intro-structure-principal") need permissions to decrypt the files.
For more information, see
[Decrypting files encrypted with AWS Key Management Service](#su-kms-encryption "#su-kms-encryption").
For information about encrypting an Amazon S3 bucket, see
[Setting default server-side encryption behavior for Amazon S3 buckets](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md").

## Decrypting files encrypted with AWS Key Management Service

If you use AWS Key Management Service (KMS) to encrypt your Amazon Rekognition Custom Labels manifest files and
image files, add the IAM principal that calls Amazon Rekognition Custom Labels to the
key policy of the KMS key. Doing this lets Amazon Rekognition Custom Labels decrypt your manifest and image files
before training. For more information, see
[My Amazon S3 bucket
has default encryption using a custom AWS KMS key. How can I allow users to download from and upload to the bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-access-default-encryption/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-bucket-access-default-encryption/")

The IAM principal needs the following permissions on the KMS key.

- kms:GenerateDataKey
- kms:Decrypt

For more information, see
[Protecting Data Using Server-Side Encryption with KMS keys Stored in AWS Key Management Service (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

## Encrypting copied training and test images

To train your model, Amazon Rekognition Custom Labels makes a copy of your source training and test images.
By default the copied images are encrypted at rest with a key that AWS owns and manages. You can also
choose to use your own AWS KMS key. If you use your own
KMS key, you need the following permissions on the KMS key.

- kms:CreateGrant
- kms:DescribeKey

You optionally specify the KMS key when you train the model with the console or when you call the `CreateProjectVersion`
operation. The KMS key you use doesn't need to be the same KMS key that you use to encrypt manifest and image files in your Amazon S3 bucket.
For more information, see [Step 5: (Optional) Encrypt training files](su-encrypt-bucket.md "su-encrypt-bucket.md").

For more information, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"). Your source images are unaffected.

For information about training a model, see [Training an Amazon Rekognition Custom Labels model](training-model.md "training-model.md").
