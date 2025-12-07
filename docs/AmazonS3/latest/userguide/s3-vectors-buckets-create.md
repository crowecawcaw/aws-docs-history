# Creating a vector bucket

You can create a vector bucket using the S3 console or the AWS CLI. All data stored in vector buckets
are always encrypted at rest. By default, vector buckets use SSE-S3 to encrypt vector data.
You can
choose to configure buckets to use server-side encryption with AWS Key Management Service
(AWS KMS) keys (SSE-KMS) instead. The bucket encryption settings can’t be changed after a
vector bucket is created, so it's important to choose the appropriate encryption method
based on your security requirements and compliance needs. For more information about
security in vector buckets, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md").

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Vector buckets**.
3. Choose **Create vector bucket**.
4. For **Vector bucket name**, enter a name for your bucket.

The bucket name must follow the naming rules:

    * Bucket name must be between 3 and 63 characters long.
    * Bucket name can only include lowercase letters, numbers, and hyphens.
    * Bucket name must be unique within your AWS account for an AWS Region.

For more information about vector bucket naming rules, see [Vector bucket naming rules](s3-vectors-buckets-naming.md "s3-vectors-buckets-naming.md").

###### Important

You can't change the vector bucket name after you create the bucket. 5. For **Encryption**, choose one of the following options:

    * **Don't specify encryption type** – Amazon S3 automatically applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for new vectors. Choose this option for the simplest setup with no additional configuration.
    * **Specify encryption type** – Choose a specific encryption method:




    	+ **Server-side encryption with Amazon S3 managed keys (SSE-S3)** – Explicitly choose to use SSE-S3. Amazon S3 encrypts your vector data as it writes it to storage and decrypts it when you access it. AWS manages all encryption keys automatically.
    	+ **Server-side encryption with AWS Key Management Service keys (SSE-KMS)** – Uses customer managed keys (CMKs) in AWS KMS, giving you more control over your encryption keys, key rotation, and access policies.


    	If you select SSE-KMS, you have additional options:




    		- **Choose from your AWS KMS keys** – Select an existing customer managed key from your account.
    		- **Enter AWS KMS key ARN** – Specify the full ARN of a KMS key (required format).
    		- **Create a KMS key** – Opens the AWS KMS console to create a new customer managed key.
    	KMS key requirements:




    		- The KMS key must be in the same Region as the vector bucket.
    		- You must specify the full KMS key ARN (key IDs and aliases aren't supported).
    		- You must grant the S3 Vectors service principal (`indexing.s3vectors.amazonaws.com`) the `kms:Decrypt` permission to use the key.
    		 For more information about an example AWS KMS key policy, see [Data protection and encryption in S3 Vectors](s3-vectors-data-encryption.md "s3-vectors-data-encryption.md").
    	For detailed information about encryption options and KMS key setup, see [Using SSE-KMS encryption](s3-vectors-data-encryption.md#s3-vectors-sse-kms-encryption "s3-vectors-data-encryption.md#s3-vectors-sse-kms-encryption").

###### Important

Encryption settings can't be changed after the vector bucket is created. Choose carefully based on your long-term security and compliance requirements. 6. Under **Tags (Optional)**, you can add tags as key-value pairs to help track and organize vector index costs using AWS Billing and Cost Management. Enter a **Key** and a **Value**. To add another tag, choose **Add Tag**. You can enter up to 50 tags for a vector index. For more information, see [Using tags with S3 vector buckets](s3-vectors-tags.md "s3-vectors-tags.md"). 7. Choose **Create vector bucket**.
After creation, you'll see a confirmation message. The new vector bucket appears in your vector buckets list and is ready for creating vector indexes within the bucket.

You can create a vector bucket with SSE-S3 encryption using the following command. To use this example, replace the `user input placeholders` with your own information.

```
aws s3vectors create-vector-bucket \
   --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

To create a vector bucket with SSE-KMS encryption using a customer managed KMS key:

```
aws s3vectors create-vector-bucket \
   --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
   --encryption-configuration '{"sseType": "aws:kms", "kmsKeyArn": "arn:aws:kms:`us-east-1`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"}'
```

SDK for Python

```
import boto3

# Create a S3 Vectors client in the AWS Region of your choice.
s3vectors = boto3.client("s3vectors", region_name="us-west-2")

#Create a vector bucket
s3vectors.create_vector_bucket(vectorBucketName="media-embeddings")
```
