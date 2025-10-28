End of support notice: On October 31, 2025, AWS
will discontinue support for Amazon Lookout for Vision. After October 31, 2025, you will
no longer be able to access the Lookout for Vision console or Lookout for Vision resources.
For more information, visit this [blog post](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision "https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision").

# Data encryption

The following information explains where Amazon Lookout for Vision uses data encryption to protect your data.

## Encryption at rest

### Images

To train your model, Amazon Lookout for Vision makes a copy of your source training and test images. The copied images are
encrypted at rest in Amazon Simple Storage Service (S3) using server-side
encryption with an AWS owned key or a key that you provide.
The keys are stored using AWS Key Management Service (SSE-KMS). Your source images are unaffected.
For more information, see [Training your model](model-train.md "model-train.md").

### Amazon Lookout for Vision models

By default, trained models and manifest files are encrypted in Amazon S3
using server-side encryption with KMS keys stored in AWS Key Management Service (SSE-KMS).
Lookout for Vision uses an AWS owned key. For more information, see [Protecting Data Using Server-Side Encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md"). Training results are written
to the bucket specified in the `output_bucket` input parameter to `CreateModel`.
The training results are encrypted using the configured encryption settings for the bucket (`output_bucket`).

### Amazon Lookout for Vision console bucket

The Amazon Lookout for Vision console creates an Amazon S3 bucket (console bucket) that you can use
to manage your projects. The console bucket is encrypted using the default Amazon S3 encryption.
For more information, see [Amazon Simple Storage Service default encryption for S3 buckets](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md").
If you are using your own KMS key, configure the console bucket after it is created.
For more information, see [Protecting Data Using Server-Side Encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md"). Amazon Lookout for Vision blocks public access to
the console bucket.

## Encryption in transit

Amazon Lookout for Vision API endpoints only support secure connections over HTTPS. All communication is encrypted with Transport Layer Security (TLS).

## Key management

You can use AWS Key Management Service (KMS) to manage encryption for the input images that
you store in Amazon S3 buckets. For more information, see
[Step 5: (Optional) Using your own AWS Key Management Service key](su-kms-encryption.md "su-kms-encryption.md").

By default your images are encrypted with a key that AWS owns and manages. You can also
choose to use your own AWS Key Management Service (KMS) key. For more information, see [AWS Key Management Service concepts](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys").
