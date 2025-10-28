# Setting encryption in S3 Vectors

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

This topic explains how to view the encryption configuration for your S3 vector
buckets.

Before you begin, make sure you have the following:

- An S3 vector bucket with encryption configured.
- Appropriate permissions to view bucket properties.

###### To configure encryption for a vector bucket

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. Choose **Create vector bucket**.
4. For **Bucket name**, enter a name for your bucket.

The bucket name must:

    * Be unique within your account for this AWS Region
    * Be between 3 and 63 characters long
    * Consist only of lowercase letters, numbers, and hyphens (-)

5.  For **Encryption**, choose one of the following options:
    - **Don't specify encryption type** – Amazon S3 applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for new objects.
    - **Specify encryption type** – Choose a specific encryption method:
      - **Server-side encryption with Amazon S3 managed keys (SSE-S3)** – Amazon S3 encrypts your data at the object level as it writes it to disks and decrypts it when you access it.
      - **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** – Similar to SSE-S3, but uses customer managed keys (CMKs) in AWS KMS, giving you more control over your keys. For more information about customer managed keys, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

      If you select this option, under **AWS KMS key**, choose one of the following options:

          - **Choose from your AWS KMS keys** – Select an existing KMS key from the dropdown list
          - **Enter AWS KMS key ARN** – Enter the Amazon Resource Name (ARN) of a KMS key
          - **Create a KMS key** – Create a new customer managed key in the AWS KMS console. For more information, see [Creating symmetric customer managed keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the *AWS Key Management Service Developer Guide*.

###### Note

The following requirements apply to the KMS key:

    * AWS KMS key ID must not be empty
    * Your KMS key must be in the same Region where this bucket is being created
    * AWS KMS key ARN must start with "arn:aws:kms:"

###### Important

Encryption settings can't be changed after the vector bucket is created. 6. If you chose **Enter AWS KMS key ARN**, enter the ARN in the text field provided. 7. If you chose **Create a KMS key**, the console opens the AWS KMS console in a new tab. For instructions on creating a KMS key, see [Creating symmetric customer managed keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_. 8. Choose **Create vector bucket**.

###### Important

When using KMS encryption, ensure that the IAM principals that need to access objects in the bucket have the necessary KMS permission (kms:Decrypt) for the selected KMS key.
The following example shows how to create a vector bucket with the SSE-S3 encryption
configuration by using the AWS CLI. To use this example, replace the `user input
 placeholders` with your own information.

```
aws s3vectors create-vector-bucket \
        --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
        --encryption-configuration '{"sseType": "AES256"}'
```

The following examples shows how to create a vector bucket that uses the SSE-KMS
encryption configuration with a customer managed key. To use this example, replace the `user
 input placeholders` with your own information.

```
aws s3vectors create-vector-bucket \
        --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
        --encryption-configuration '{"sseType": "aws:kms", "kmsKeyArn": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"}'
```
